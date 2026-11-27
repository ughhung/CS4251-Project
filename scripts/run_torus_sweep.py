#!/usr/bin/env python3
"""Run the torus matrix in ASTRA-sim Docker and journal each run's progress."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import math
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath
from threading import Event, Lock, local
from time import monotonic


PROJECT = Path(__file__).resolve().parents[1]
ASTRA = PROJECT / "astra-sim"
NS3 = ASTRA / "extern/network_backend/ns-3"
SCRATCH = NS3 / "build/scratch"
SIMULATOR = SCRATCH / "ns3.42-AstraSimNetwork-default"
CONFIG = NS3 / "scratch/config/config_ring32.txt"
RUNS = ASTRA / "runs/torus_sweep"
TOPOLOGIES = ASTRA / "extern/network_backend/csg-htsim/sim/datacenter/topologies"
MEMORY = ASTRA / "examples/remote_memory/analytical/no_memory_expansion.json"
CONTAINER_ROOT = PurePosixPath("/app/astra-sim")
OUTPUT_FILES = {
    "FCT_OUTPUT_FILE": "fct.txt",
    "QLEN_MON_FILE": "qlen.txt",
    "PFC_OUTPUT_FILE": "pfc.txt",
    "TRACE_OUTPUT_FILE": "mix.tr",
}
RANKS = set(range(32))
WORKLOADS = (
    ("baseline", "baseline", "dense32_validmb"),
    ("straggler", "straggler", "dense32_validmb"),
    ("straggler_1_5", "straggler_1_5", "dense32_validmb"),
    ("moe32_uniform", "moe32", "moe32_top1_uniform_paircoll"),
    ("moe32_zipf075", "moe32", "moe32_top1_zipf075_paircoll"),
)
TIMESTAMP = re.compile(r"^\[(\d{4}-\d\d-\d\d[ T]\d\d:\d\d:\d\d[^\]]*)\]")
FINISHED = re.compile(r"sys\[(\d+)\] finished,\s+\d+ cycles")
STATUS_LOCK = Lock()


class SweepInterrupted(Exception):
    """An active job was cancelled by the sweep."""


class SimulationStalled(Exception):
    """The simulator has produced no observable output within the idle limit."""


def check_cancelled(stop: Event) -> None:
    if stop.is_set():
        raise SweepInterrupted


@dataclass
class Topology:
    filename: str
    args: list[str]
    logical: Path
    system: Path

    @property
    def name(self) -> str:
        return Path(self.filename).stem


def load_topologies(path: Path) -> list[Topology]:
    topologies = []
    for block in re.split(r"(?m)^-{3,}\s*$", path.read_text()):
        if not block.strip():
            continue
        shared = None
        logical = system = None
        commands = []
        for raw in block.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("A="):
                (value,) = shlex.split(line[2:])
                shared = shlex.split(value)
            elif line.startswith("logical topology ="):
                logical = PROJECT / line.partition("=")[2].strip()
            elif line.startswith("ring collective file ="):
                system = PROJECT / line.partition("=")[2].strip()
            else:
                words = shlex.split(line)
                if words[:3] != ["python3", "gen_topo.py", "torus"] or words[-2] != "-o":
                    raise ValueError(f"Unrecognized topology command: {line}")
                commands.append((words[3:-2], words[-1]))
        if shared is None or logical is None or system is None or not commands:
            raise ValueError("Each topology group needs A, commands, a logical topology, and a collective file")
        for args, filename in commands:
            if not re.fullmatch(r"[\w-]+\.txt", filename):
                raise ValueError(f"Invalid topology filename: {filename}")
            expanded = [part for arg in args for part in (shared if arg == "$A" else [arg])]
            topologies.append(Topology(filename, expanded, logical, system))
    if not topologies or len({topo.name for topo in topologies}) != len(topologies):
        raise ValueError("Expected a nonempty list of uniquely named topologies")
    return topologies


def container_path(path: Path) -> str:
    return str(CONTAINER_ROOT / path.relative_to(ASTRA))


def workload_path(directory: str, prefix: str) -> Path:
    return ASTRA / "traces" / directory / prefix


def config_field(config: str, key: str) -> re.Pattern:
    pattern = re.compile(rf"(?m)^([ \t]*{key})[ \t]+(\S+)[^\S\r\n]*$")
    if len(pattern.findall(config)) != 1:
        raise ValueError(f"Expected one {key} path in {CONFIG}")
    return pattern


def config_input(config: str, key: str) -> Path:
    value = PurePosixPath(config_field(config, key).search(config)[2])
    if value.is_absolute():
        return ASTRA / value.relative_to(CONTAINER_ROOT)
    # Resolve legacy relative paths from the original simulator working directory.
    return (SCRATCH / str(value)).resolve()


def preflight(topologies: list[Topology], container: str, workloads=WORKLOADS) -> str:
    config = CONFIG.read_text()
    required = {MEMORY, config_input(config, "FLOW_FILE"), config_input(config, "TRACE_FILE")}
    for topo in topologies:
        required.update((topo.logical, topo.system))
    for _, directory, prefix in workloads:
        workload = workload_path(directory, prefix)
        required.add(workload.with_suffix(".json"))
        required.update(workload.with_suffix(f".{rank}.et") for rank in RANKS)
    missing = sorted(str(path) for path in required if not path.is_file())
    if missing:
        raise ValueError("Missing input files:\n" + "\n".join(missing))
    for key in ("TOPOLOGY_FILE", *OUTPUT_FILES):
        config_field(config, key)
    state = subprocess.check_output(["docker", "inspect", container], text=True)
    (info,) = json.loads(state)
    if not info["State"]["Running"]:
        raise ValueError(f"Docker container {container} is stopped")
    mounts = []
    for mount in info["Mounts"]:
        destination = PurePosixPath(mount["Destination"])
        if CONTAINER_ROOT.is_relative_to(destination):
            mounts.append((destination, mount))
    if not mounts:
        raise ValueError(f"{container} has no mount covering {CONTAINER_ROOT}")
    destination, mount = max(mounts, key=lambda item: len(item[0].parts))
    source = Path(mount["Source"]) / CONTAINER_ROOT.relative_to(destination)
    if source.resolve() != ASTRA.resolve() or not mount["RW"]:
        raise ValueError(f"{container} must mount {ASTRA} read-write at {CONTAINER_ROOT}")
    overridden = [
        m["Destination"] for m in info["Mounts"]
        if PurePosixPath(m["Destination"]) != CONTAINER_ROOT
        and PurePosixPath(m["Destination"]).is_relative_to(CONTAINER_ROOT)
    ]
    if overridden:
        raise ValueError(f"Nested mounts hide workspace paths: {', '.join(overridden)}")
    subprocess.run(
        ["docker", "exec", container, "sh", "-c",
         'test -x "$1" && command -v sha256sum >/dev/null',
         "torus-preflight", container_path(SIMULATOR)], check=True,
    )
    return config


def allowed_container_cpus(container: str) -> list[int]:
    status = subprocess.check_output(
        ["docker", "exec", container, "sh", "-c",
         'command -v taskset >/dev/null || { echo "taskset is required for --pin-cpus" >&2; exit 1; }; '
         "cat /proc/self/status"],
        text=True, timeout=15,
    )
    match = re.search(r"(?m)^Cpus_allowed_list:[ \t]*([\d,-]+)[ \t]*$", status)
    if not match:
        raise ValueError(f"Could not read the allowed CPUs in container {container}")
    cpus = set()
    for part in match[1].split(","):
        first, _, last = part.partition("-")
        cpus.update(range(int(first), int(last or first) + 1))
    if not cpus:
        raise ValueError(f"No allowed CPUs found in container {container}")
    return sorted(cpus)


def stamp() -> str:
    return datetime.now().astimezone().isoformat()


def print_status(message: str, *, run: tuple[int, int] | None = None, file=None) -> None:
    prefix = f"[{stamp()}]"
    if run is not None:
        prefix += f" [run {run[0]}/{run[1]}]"
    with STATUS_LOCK:
        print("\n".join(f"{prefix} {line}" for line in message.splitlines()),
              file=file, flush=True)


def record(journal, event: str, **fields) -> None:
    with STATUS_LOCK:
        journal.write(json.dumps({"event": event, "time": stamp(), **fields}) + "\n")
        journal.flush()
        os.fsync(journal.fileno())


def find_log(run_dir: Path, started: datetime, ended: datetime):
    """Snapshot completion and statistics from this job's log and rotations."""
    sources = []
    lines = []
    ranks = set()
    for path in sorted((run_dir / "log").glob("log*.log")):
        if not re.fullmatch(r"log(?:\.\d+)?\.log", path.name):
            continue
        matched = False
        with path.open(errors="replace") as handle:
            for line in handle:
                match = TIMESTAMP.match(line)
                if not match:
                    continue
                try:
                    logged = datetime.fromisoformat(match[1])
                except ValueError:
                    continue
                if logged.tzinfo is None:
                    logged = logged.replace(tzinfo=started.tzinfo)
                if not started <= logged <= ended:
                    continue
                matched = True
                if completion := FINISHED.search(line):
                    ranks.add(int(completion[1]))
                lines.append((logged, line))
        if matched:
            sources.append(path)
    if ranks != RANKS:
        return None, sources, ranks
    snapshot = run_dir / "run.log"
    lines.sort(key=lambda entry: entry[0])
    snapshot.write_text("".join(line for _, line in lines))
    return snapshot, sources, ranks


def container_time(container: str) -> datetime:
    value = subprocess.check_output(
        ["docker", "exec", container, "date", "+%Y-%m-%dT%H:%M:%S.%N%z"],
        text=True, timeout=15,
    )
    return datetime.fromisoformat(value.strip())


def replace_file(path: Path, contents: bytes) -> None:
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_bytes(contents)
        if path.exists():
            shutil.copymode(path, temporary)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def prepare_topology(topo: Topology) -> Path:
    destination = TOPOLOGIES / topo.filename
    with tempfile.TemporaryDirectory(dir=TOPOLOGIES, prefix=".torus-") as directory:
        generated = Path(directory) / topo.filename
        subprocess.run(
            [sys.executable, str(PROJECT / "scripts/gen_topo.py"), "torus",
             *topo.args, "-o", str(generated)], check=True,
        )
        replace_file(destination, generated.read_bytes())
    return destination


def prepare_run_dir(label: str, topology: str, batch_id: str) -> Path:
    pair_dir = RUNS / f"{label}_{topology}"
    run_dir = pair_dir / "attempts" / batch_id
    run_dir.mkdir(parents=True)
    link = pair_dir / f".latest-{batch_id}"
    try:
        link.symlink_to(run_dir.relative_to(pair_dir), target_is_directory=True)
        link.replace(pair_dir / "latest")
    finally:
        link.unlink(missing_ok=True)
    return run_dir


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def save_manifest(run_dir: Path, manifest: dict) -> None:
    replace_file(run_dir / "manifest.json", (json.dumps(manifest, indent=2) + "\n").encode())


def stage_run(container: str, topo: Topology, directory: str, prefix: str,
              run_dir: Path, config: str, generated: Path, fields: dict) -> dict:
    input_dir = run_dir / "inputs"
    output_dir = run_dir / "output"
    input_dir.mkdir()
    output_dir.mkdir()
    inputs = {}

    def stage(name: str, source: Path, destination: Path) -> Path:
        shutil.copyfile(source, destination)
        inputs[name] = {"source": str(source), "path": container_path(destination),
                        "sha256": sha256(destination)}
        return destination

    topology = stage("physical_topology", generated, input_dir / topo.filename)
    logical = stage("logical_topology", topo.logical, input_dir / "logical_topology.json")
    system = stage("system", topo.system, input_dir / "system.json")
    memory = stage("remote_memory", MEMORY, input_dir / "remote_memory.json")
    workload = workload_path(directory, prefix)
    staged_prefix = input_dir / prefix
    groups = stage("comm_group", workload.with_suffix(".json"), staged_prefix.with_suffix(".json"))
    for rank in sorted(RANKS):
        suffix = f".{rank}.et"
        stage(f"trace_rank_{rank}", workload.with_suffix(suffix), staged_prefix.with_suffix(suffix))
    flow = stage("flow_input", config_input(config, "FLOW_FILE"), input_dir / "flow.txt")
    trace = stage("trace_nodes", config_input(config, "TRACE_FILE"), input_dir / "trace.txt")
    # The analyzer expects the two input files alongside the simulator outputs.
    for path in (flow, trace):
        (output_dir / path.name).symlink_to(Path("..") / input_dir.name / path.name)
    config_paths = {
        "TOPOLOGY_FILE": topology,
        "FLOW_FILE": flow,
        "TRACE_FILE": trace,
        **{key: output_dir / name for key, name in OUTPUT_FILES.items()},
    }
    for key, path in config_paths.items():
        config = config_field(config, key).sub(lambda m: f"{m[1]} {container_path(path)}", config)
    staged_config = run_dir / "config_ring32.txt"
    staged_config.write_text(config)
    inputs["network_config"] = {"source": str(CONFIG), "path": container_path(staged_config),
                                "sha256": sha256(staged_config)}
    inputs["simulator"] = {"path": container_path(SIMULATOR), "sha256": sha256(SIMULATOR)}
    checksums = run_dir / "inputs.sha256"
    checksums.write_text("".join(f"{item['sha256']}  {item['path']}\n" for item in inputs.values()))
    simulator = [
        container_path(SIMULATOR),
        f"--workload-configuration={container_path(staged_prefix)}",
        f"--comm-group-configuration={container_path(groups)}",
        f"--system-configuration={container_path(system)}",
        f"--remote-memory-configuration={container_path(memory)}",
        f"--network-configuration={container_path(staged_config)}",
        f"--logical-topology-configuration={container_path(logical)}",
    ]
    if "container_cpu" in fields:
        simulator = ["taskset", "-c", str(fields["container_cpu"]), *simulator]
    manifest = {
        **fields, "container": container, "container_workdir": container_path(run_dir),
        "simulator_command": simulator, "inputs": inputs,
        "checksums_sha256": sha256(checksums), "output_dir": str(output_dir),
        "simulator_log": str(run_dir / "simulator.log"),
    }
    save_manifest(run_dir, manifest)
    return manifest


def activity_state(paths: tuple[Path, ...]) -> tuple:
    state = []
    for path in paths:
        try:
            info = path.stat()
            state.append((info.st_ino, info.st_size, info.st_mtime_ns))
        except FileNotFoundError:
            state.append(None)
    return tuple(state)


def wait_for_process(process: subprocess.Popen, stop: Event, *,
                     idle_timeout: float | None = None, activity: tuple[Path, ...] = ()) -> int:
    last_change = monotonic()
    previous = activity_state(activity)
    while True:
        try:
            return process.wait(timeout=1 if idle_timeout is not None else 0.25)
        except subprocess.TimeoutExpired:
            check_cancelled(stop)
            if idle_timeout is not None:
                current = activity_state(activity)
                now = monotonic()
                if current != previous:
                    previous = current
                    last_change = now
                elif now - last_change >= idle_timeout:
                    raise SimulationStalled(f"No simulator log or output changes for {idle_timeout / 60:g} minutes")


def stop_process(process: subprocess.Popen) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def stop_simulator(container: str, run_dir: Path, process: subprocess.Popen) -> None:
    # A wrapper still starting will see this marker before it launches ASTRA-sim.
    (run_dir / "simulator.cancelled").touch()
    pid_path = run_dir / "simulator.pid"
    try:
        for _ in range(20):
            if process.poll() is not None:
                return
            pid = pid_path.read_text().strip() if pid_path.is_file() else ""
            if pid.isdecimal():
                break
            try:
                process.wait(timeout=0.1)
                return
            except subprocess.TimeoutExpired:
                pass
        else:
            return
        for sig in ("TERM", "KILL"):
            subprocess.run(["docker", "exec", container, "kill", f"-{sig}", pid],
                           check=True, timeout=5, capture_output=True)
            try:
                process.wait(timeout=5)
                return
            except subprocess.TimeoutExpired:
                pass
        print_status(f"Could not confirm simulator exit in {run_dir}", file=sys.stderr)
    except (OSError, subprocess.SubprocessError) as error:
        if process.poll() is None:
            print_status(f"Could not confirm simulator exit in {run_dir}: {error}", file=sys.stderr)
    finally:
        stop_process(process)


def simulate(container: str, run_dir: Path, manifest: dict, stop: Event, *,
             stall_timeout: float | None) -> tuple[int | None, str | None]:
    # Publish the PID before verification so an interrupted sweep can stop this job.
    pid_path = run_dir / "simulator.pid"
    command = [
        "docker", "exec", "-w", container_path(run_dir), container, "sh", "-c",
        'printf "%s\\n" "$$" > simulator.pid || exit 1; '
        'test ! -e simulator.cancelled || exit 130; '
        'printf "%s  inputs.sha256\\n" "$1" | sha256sum -c --strict --quiet || exit 1; '
        'sha256sum -c --strict inputs.sha256 || exit 1; '
        'test ! -e simulator.cancelled || exit 130; '
        'printf "%s\\n" "$1" > inputs.verified || exit 1; shift; exec "$@"',
        "torus-sweep", manifest["checksums_sha256"], *manifest["simulator_command"],
    ]
    activity = (run_dir / "simulator.log", run_dir / "log/log.log",
                run_dir / "log/err.log", *(run_dir / "output" / name for name in OUTPUT_FILES.values()))
    with (run_dir / "simulator.log").open("wb") as output:
        with subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT,
                              start_new_session=True) as process:
            try:
                return wait_for_process(process, stop, idle_timeout=stall_timeout, activity=activity), None
            except SimulationStalled as error:
                stop_simulator(container, run_dir, process)
                return process.returncode, str(error)
            except SweepInterrupted:
                stop_simulator(container, run_dir, process)
                raise
            finally:
                pid_path.unlink(missing_ok=True)


def report_stem(topology: str, trace: str) -> str:
    return f"report_{trace}_{topology}"


def existing_reports(results: Path, plan) -> dict:
    reports = {}
    for topology, trace in plan:
        stem = report_stem(topology, trace)
        exact = results / f"{stem}.md"
        timestamped = re.compile(
            rf"{re.escape(stem)}_\d{{8}}_\d{{6}}_\d{{6}}(?:_\d+)?\.md"
        )
        candidates = [exact, *sorted(
            (path for path in results.glob(f"{stem}_*.md") if timestamped.fullmatch(path.name)),
            reverse=True,
        )]
        for path in candidates:
            if path.is_file() and path.stat().st_size > 0:
                reports[topology, trace] = path
                break
    return reports


def run_one(container: str, topo: Topology, workload, run_dir: Path, journal, outcomes, *,
            run, skip_packet_trace: bool, config: str, generated: Path, stop: Event,
            stall_timeout: float | None, cpu: int | None):
    label, directory, prefix = workload
    fields = {"topology": topo.name, "trace": label, "run_number": run[0], "total_runs": run[1]}
    key = (topo.name, label)
    cpu_message = ""
    if cpu is not None:
        fields["container_cpu"] = cpu
        cpu_message = f" (Docker VM CPU {cpu})"
    print_status(f"Running {label} on {topo.name}{cpu_message}", run=run)
    manifest = stage_run(container, topo, directory, prefix, run_dir, config, generated, fields)
    output_dir = run_dir / "output"
    manifest_path = str(run_dir / "manifest.json")
    started = container_time(container)
    check_cancelled(stop)
    manifest["container_start"] = started.isoformat()
    save_manifest(run_dir, manifest)
    record(journal, "simulation_started", **fields, container_start=started.isoformat(),
           manifest=manifest_path)
    outcomes[key] = "simulation_pending"
    exit_code, stall_reason = simulate(container, run_dir, manifest, stop, stall_timeout=stall_timeout)
    simulation_status = ("stalled" if stall_reason else "failed" if exit_code else "success")
    outcomes[key] = "analysis_pending" if simulation_status == "success" else f"simulation_{simulation_status}"
    record(journal, "simulation_finished", **fields, exit_code=exit_code,
           status=simulation_status, **({"reason": stall_reason} if stall_reason else {}),
           simulator_log=manifest["simulator_log"], manifest=manifest_path)
    receipt = run_dir / "inputs.verified"
    verified = receipt.is_file() and receipt.read_text().strip() == manifest["checksums_sha256"]
    manifest["simulation"] = {"status": simulation_status, "exit_code": exit_code,
                              "container_inputs_verified": verified}
    if stall_reason:
        manifest["simulation"]["reason"] = stall_reason
    save_manifest(run_dir, manifest)

    def finish(status, **details):
        manifest.setdefault("analysis", {}).update(status=status, **details)
        save_manifest(run_dir, manifest)
        record(journal, "analysis_finished", **fields, status=status, manifest=manifest_path, **details)
        if simulation_status == "success":
            outcomes[key] = status
        message = f"{label} on {topo.name}: {status}"
        if reason := details.get("reason"):
            message += f". {reason}"
        print_status(message, run=run)

    if stall_reason:
        finish("skipped", reason=stall_reason)
        return
    if exit_code:
        reason = f"Simulator exited with status {exit_code}" if verified else (
            f"Simulator launch or input verification failed with status {exit_code}"
        )
        finish("skipped", reason=reason)
        return
    if not verified:
        finish("skipped", reason="Missing or invalid in-container input verification receipt")
        return
    check_cancelled(stop)
    ended = container_time(container)
    manifest["container_end"] = ended.isoformat()
    log, sources, ranks = find_log(run_dir, started, ended)
    manifest["completion_log"] = {
        "sources": [str(path) for path in sources], "completed_ranks": sorted(ranks),
    }
    if log is None:
        finish("skipped", reason="Job log does not contain all 32 rank completions during the run")
        return
    manifest["completion_log"].update(path=str(log), sha256=sha256(log))
    outputs = [output_dir / name for name in OUTPUT_FILES.values()]
    missing = [path.name for path in outputs if not path.is_file()]
    if missing:
        finish("skipped", reason=f"Missing job output: {', '.join(missing)}")
        return
    manifest["outputs"] = {path.name: path.stat().st_size for path in outputs}
    report = PROJECT / "results" / f"{report_stem(topo.name, label)}.md"
    analyzer = PROJECT / "scripts/analyze_ns3_results.py"
    command = [sys.executable, str(analyzer),
               str(output_dir), "--log", str(log), "-o", str(report)]
    if skip_packet_trace:
        command.append("--skip-packet-trace")
    check_cancelled(stop)
    manifest["analysis"] = {"status": "started", "command": command,
                            "analyzer_sha256": sha256(analyzer)}
    save_manifest(run_dir, manifest)
    record(journal, "analysis_started", **fields, log=str(log), manifest=manifest_path,
           log_sources=[str(path) for path in sources], container_end=ended.isoformat(),
           skip_packet_trace=skip_packet_trace, output_dir=str(output_dir))
    print_status(f"Analyzing {label} on {topo.name}", run=run)
    with (run_dir / "analysis.log").open("w+") as output:
        with subprocess.Popen(command, cwd=PROJECT, stdout=output, stderr=subprocess.STDOUT,
                              start_new_session=True) as process:
            try:
                analysis_exit = wait_for_process(process, stop)
            except SweepInterrupted:
                stop_process(process)
                manifest["analysis"]["status"] = "interrupted"
                save_manifest(run_dir, manifest)
                raise
        output.seek(0)
        messages = output.read().splitlines()
    actual_report = PROJECT / messages[-1] if messages else None
    if analysis_exit or actual_report is None or not actual_report.is_file():
        finish("failed", reason="Analyzer did not produce a report",
               analyzer_log=str(run_dir / "analysis.log"))
    else:
        finish("success", report=str(actual_report), report_sha256=sha256(actual_report), log=str(log))
        try:
            shutil.rmtree(output_dir)
        except OSError as error:
            cleanup = {"status": "failed", "reason": str(error)}
            print_status(f"Raw output cleanup failed: {error}", run=run, file=sys.stderr)
        else:
            cleanup = {"status": "removed"}
        manifest["raw_output_cleanup"] = cleanup
        save_manifest(run_dir, manifest)
        record(journal, "raw_output_cleanup", **fields, output_dir=str(output_dir), **cleanup)


def run_sweep(container: str, topologies: list[Topology], results: Path, reports: dict, *,
              skips: dict, skip_packet_trace: bool, config: str, jobs: int,
              stall_timeout: float | None, worker_cpus: list[int]) -> int:
    batch_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    plan = [(topo.name, label) for topo in topologies for label, _, _ in WORKLOADS]
    run_numbers = {key: (number, len(plan)) for number, key in enumerate(plan, 1)}
    outcomes = dict.fromkeys(plan, "not_started")
    journal_path = results / f"torus_sweep_{batch_id}.jsonl"
    with journal_path.open("x") as journal:
        record(journal, "planned", jobs=jobs, stall_timeout_seconds=stall_timeout,
               worker_cpus=worker_cpus,
               runs=[{"topology": topo, "trace": label} for topo, label in plan])
        print_status(f"Progress journal: {journal_path}")
        print_status(f"Running up to {jobs} jobs concurrently")
        stop = Event()
        worker = local()
        cpu_slots = iter(worker_cpus)
        cpu_lock = Lock()

        def assign_cpu() -> None:
            with cpu_lock:
                worker.cpu = next(cpu_slots)

        def run_job(topo: Topology, workload, generated: Path) -> None:
            if stop.is_set():
                return
            label = workload[0]
            key = (topo.name, label)
            run = run_numbers[key]
            fields = {"topology": topo.name, "trace": label,
                      "run_number": run[0], "total_runs": run[1]}
            cpu = getattr(worker, "cpu", None)
            if cpu is not None:
                fields["container_cpu"] = cpu
            try:
                run_dir = prepare_run_dir(label, topo.name, batch_id)
                run_one(container, topo, workload, run_dir,
                        journal, outcomes, run=run, skip_packet_trace=skip_packet_trace,
                        config=config, generated=generated, stop=stop, stall_timeout=stall_timeout,
                        cpu=cpu)
            except SweepInterrupted:
                record(journal, "run_interrupted", **fields, previous_status=outcomes[key])
                print_status(f"Interrupted {label} on {topo.name}", run=run)
            except (OSError, ValueError, subprocess.SubprocessError) as error:
                previous = outcomes[key]
                if previous != "success":
                    outcomes[key] = "failed"
                if previous == "analysis_pending":
                    record(journal, "analysis_finished", **fields, status="failed", reason=str(error))
                else:
                    record(journal, "run_error", **fields, previous_status=previous, reason=str(error))
                print_status(f"{label} on {topo.name}: {error}", run=run, file=sys.stderr)

        interrupted = False
        executor = ThreadPoolExecutor(max_workers=jobs, initializer=assign_cpu if worker_cpus else None)
        futures = []
        try:
            for topo in topologies:
                pending = []
                for workload in WORKLOADS:
                    label = workload[0]
                    key = (topo.name, label)
                    if key in skips:
                        skip = skips[key]
                        outcomes[key] = "known_skipped"
                        run = run_numbers[key]
                        record(journal, "run_skipped", topology=topo.name, trace=label,
                               run_number=run[0], total_runs=run[1], status="known_skipped",
                               reason=skip["reason"], evidence=skip.get("evidence"))
                        print_status(f"Skipping {label} on {topo.name}: {skip['reason']}", run=run)
                        continue
                    report = reports.get((topo.name, label))
                    if report is None:
                        pending.append(workload)
                        continue
                    outcomes[topo.name, label] = "already_reported"
                    run = run_numbers[topo.name, label]
                    record(journal, "run_skipped", topology=topo.name, trace=label,
                           run_number=run[0], total_runs=run[1],
                           reason="Report already exists", report=str(report))
                    print_status(f"Skipping {label} on {topo.name}: {report.name} exists", run=run)
                if not pending:
                    continue
                try:
                    generated = prepare_topology(topo)
                except (OSError, ValueError, subprocess.SubprocessError) as error:
                    for label, _, _ in pending:
                        outcomes[topo.name, label] = "skipped"
                        run = run_numbers[topo.name, label]
                        record(journal, "run_skipped", topology=topo.name, trace=label,
                               run_number=run[0], total_runs=run[1],
                               reason=f"Topology setup failed: {error}")
                        print_status(f"Skipping {label} on {topo.name}: {error}", run=run, file=sys.stderr)
                    continue
                for workload in pending:
                    futures.append(executor.submit(run_job, topo, workload, generated))
            for future in as_completed(futures):
                future.result()
        except KeyboardInterrupt:
            interrupted = True
            stop.set()
            print_status("Stopping active jobs")
        finally:
            stop.set()
            executor.shutdown(wait=True, cancel_futures=True)
            counts = {status: list(outcomes.values()).count(status)
                      for status in sorted(set(outcomes.values()))}
            record(journal, "summary", interrupted=interrupted, counts=counts)
            print_status(json.dumps(counts))
    if interrupted:
        return 130
    completed = sum(counts.get(status, 0) for status in ("success", "already_reported", "known_skipped"))
    return int(completed != len(plan))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--container", default="d873db5c7fa0")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the matrix without accessing Docker or writing files")
    parser.add_argument("--missing-only", action="store_true",
                        help="Run only combinations without a report in results/")
    parser.add_argument("--skip-packet-trace", action="store_true",
                        help="Generate reports without scanning mix.tr")
    parser.add_argument("--jobs", type=int, default=1,
                        help="Maximum concurrent jobs, including analysis (default: 1)")
    parser.add_argument("--pin-cpus", action="store_true",
                        help="Pin each simulator worker to a distinct allowed Docker VM CPU")
    parser.add_argument("--stall-timeout-minutes", type=float, metavar="MINUTES",
                        help="Stop a simulation after this long without log or output changes")
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be at least 1")
    stall_timeout = None
    if args.stall_timeout_minutes is not None:
        stall_timeout = args.stall_timeout_minutes * 60
        if not math.isfinite(stall_timeout) or stall_timeout <= 0:
            parser.error("--stall-timeout-minutes must be a finite positive number")
    try:
        topologies = load_topologies(PROJECT / "topologies/torus_list_copy.txt")
        results = PROJECT / "results"
        plan = [(topo.name, label) for topo in topologies for label, _, _ in WORKLOADS]
        skip_list = json.loads((PROJECT / "topologies/torus_skips.json").read_text())
        skips = {}
        for topology, trace in plan:
            skip = skip_list.get(topology, {}).get(trace)
            if skip is not None:
                if not isinstance(skip, dict) or not isinstance(skip.get("reason"), str) or not skip["reason"].strip():
                    raise ValueError(f"Missing skip reason for {trace} on {topology}")
                skips[topology, trace] = skip
        eligible = [key for key in plan if key not in skips]
        if args.dry_run:
            reports = existing_reports(results, eligible) if args.missing_only else {}
            jobs = ((topo, workload) for topo in topologies for workload in WORKLOADS)
            for number, (topo, (label, directory, prefix)) in enumerate(jobs, 1):
                if (topo.name, label) in skips:
                    print_status(f"Skipping {label} on {topo.name}: {skips[topo.name, label]['reason']}",
                                 run=(number, len(plan)))
                    continue
                if (topo.name, label) in reports:
                    continue
                workload = workload_path(directory, prefix).relative_to(PROJECT)
                print_status(f"{topo.name} {label} {workload} "
                             f"{topo.logical.relative_to(PROJECT)} {topo.system.relative_to(PROJECT)}",
                             run=(number, len(plan)))
            print_status(f"{len(topologies)} topologies, {len(eligible) - len(reports)} runs, "
                         f"{len(reports)} existing reports skipped, {len(skips)} configured skips, "
                         f"up to {args.jobs} concurrent")
            if args.pin_cpus:
                print_status("CPU pinning enabled. Worker CPUs are selected at launch.")
            return 0
        results.mkdir(exist_ok=True)
        with (results / ".torus_sweep.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise ValueError("A torus sweep is already running in this workspace") from None
            reports = existing_reports(results, eligible) if args.missing_only else {}
            pending = [key for key in eligible if key not in reports]
            if not pending and not skips:
                print_status(f"All {len(plan)} runs already have reports in {results}.")
                return 0
            config = ""
            jobs = args.jobs
            worker_cpus = []
            if pending:
                pending_topologies = {topology for topology, _ in pending}
                pending_traces = {trace for _, trace in pending}
                config = preflight([topo for topo in topologies if topo.name in pending_topologies],
                                   args.container,
                                   [workload for workload in WORKLOADS if workload[0] in pending_traces])
                if args.pin_cpus:
                    worker_cpus = allowed_container_cpus(args.container)[:min(jobs, len(pending))]
                    jobs = len(worker_cpus)
                    print_status("Worker Docker VM CPUs: " + ", ".join(map(str, worker_cpus)))
            return run_sweep(args.container, topologies, results, reports, skips=skips,
                             skip_packet_trace=args.skip_packet_trace, config=config, jobs=jobs,
                             stall_timeout=stall_timeout, worker_cpus=worker_cpus)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print_status(f"Torus sweep could not proceed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    def interrupt(_signal, _frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGTERM, interrupt)
    sys.exit(main())
