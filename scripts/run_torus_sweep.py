#!/usr/bin/env python3
"""Run the torus matrix in ASTRA-sim Docker and journal each run's progress."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath


PROJECT = Path(__file__).resolve().parents[1]
ASTRA = PROJECT / "astra-sim"
NS3 = ASTRA / "extern/network_backend/ns-3"
SCRATCH = NS3 / "build/scratch"
CONFIG = NS3 / "scratch/config/config_ring32.txt"
OUTPUT = NS3 / "scratch/output"
TOPOLOGIES = ASTRA / "extern/network_backend/csg-htsim/sim/datacenter/topologies"
MEMORY = ASTRA / "examples/remote_memory/analytical/no_memory_expansion.json"
CONTAINER_ROOT = PurePosixPath("/app/astra-sim")
DEFAULT_LOG = ASTRA / "log/log/log.log"
LOG_ROOTS = (ASTRA / "log", SCRATCH / "log")
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


def preflight(topologies: list[Topology], container: str, workloads=WORKLOADS) -> None:
    required = {CONFIG, MEMORY, OUTPUT / "flow.txt", OUTPUT / "trace.txt"}
    for topo in topologies:
        required.update((topo.logical, topo.system))
    for _, directory, prefix in workloads:
        workload = workload_path(directory, prefix)
        required.add(workload.with_suffix(".json"))
        required.update(workload.with_suffix(f".{rank}.et") for rank in RANKS)
    missing = sorted(str(path) for path in required if not path.is_file())
    if missing:
        raise ValueError("Missing input files:\n" + "\n".join(missing))
    if len(re.findall(r"(?m)^TOPOLOGY_FILE[ \t]+[^\r\n]+", CONFIG.read_text())) != 1:
        raise ValueError(f"Expected one TOPOLOGY_FILE in {CONFIG}")
    for topo in topologies:
        container_path(topo.system)
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
        ["docker", "exec", "-w", container_path(SCRATCH), container,
         "test", "-x", "./ns3.42-AstraSimNetwork-default"], check=True,
    )


def stamp() -> str:
    return datetime.now().astimezone().isoformat()


def record(journal, event: str, **fields) -> None:
    journal.write(json.dumps({"event": event, "time": stamp(), **fields}) + "\n")
    journal.flush()
    os.fsync(journal.fileno())


def file_state(path: Path):
    try:
        stat = path.stat()
    except FileNotFoundError:
        return None
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns


def log_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.log") if path.is_file())


def log_state() -> dict:
    """Keep the old end of each file so append and rotation can be detected."""
    old = {}
    for root in LOG_ROOTS:
        for path in log_files(root):
            with path.open("rb") as handle:
                stat = os.fstat(handle.fileno())
                offset = max(0, stat.st_size - 256)
                handle.seek(offset)
                old[stat.st_dev, stat.st_ino] = (offset, handle.read(256), stat.st_size)
    return old


def current_log_lines(path: Path, old: dict, started: datetime, ended: datetime):
    with path.open("rb") as handle:
        stat = os.fstat(handle.fileno())
        offset, tail, size = old.get((stat.st_dev, stat.st_ino), (0, b"", 0))
        if size and stat.st_size >= size:
            handle.seek(offset)
            if handle.read(len(tail)) != tail:
                size = 0
        else:
            size = 0
        handle.seek(size)
        lines = []
        clean = size == 0
        for raw in handle:
            line = raw.decode("utf-8", errors="replace")
            match = TIMESTAMP.match(line)
            if match:
                try:
                    logged = datetime.fromisoformat(match[1])
                except ValueError:
                    clean = False
                    continue
                if logged.tzinfo is None:
                    logged = logged.replace(tzinfo=started.tzinfo)
                if started <= logged <= ended:
                    lines.append((logged, line))
                    continue
            if line.strip():
                clean = False
    return lines, clean


def completed_ranks(lines) -> set[int]:
    return {int(match[1]) for _, line in lines if (match := FINISHED.search(line))}


def find_log(old: dict, started: datetime, ended: datetime, snapshot: Path):
    # Prefer the canonical path, then search its tree, then the actual run cwd.
    for root in LOG_ROOTS:
        paths = sorted(log_files(root), key=lambda path: (path != DEFAULT_LOG, path))
        rotated = {}
        for path in paths:
            lines, clean = current_log_lines(path, old, started, ended)
            if lines:
                base = re.sub(r"\.\d+\.log$", ".log", path.name)
                rotated.setdefault(path.with_name(base), []).append((path, lines, clean))
        for segments in rotated.values():
            lines = sorted(
                (line for _, entries, _ in segments for line in entries),
                key=lambda item: item[0],
            )
            if completed_ranks(lines) == RANKS:
                sources = [path for path, _, _ in segments]
                if len(segments) == 1 and segments[0][2]:
                    return sources[0], sources
                snapshot.write_text("".join(line for _, line in lines))
                return snapshot, sources
    return None, []


def container_time(container: str) -> datetime:
    value = subprocess.check_output(
        ["docker", "exec", container, "date", "+%Y-%m-%dT%H:%M:%S.%N%z"], text=True,
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


def prepare_topology(topo: Topology, original_config: str, target: Path) -> None:
    subprocess.run(
        [sys.executable, str(PROJECT / "scripts/gen_topo.py"), "torus",
         *topo.args, "-o", str(target)], check=True,
    )
    destination = TOPOLOGIES / topo.filename
    replace_file(destination, target.read_bytes())
    for directory in {directory for _, directory, _ in WORKLOADS}:
        logical_path = ASTRA / "traces" / directory / topo.logical.name
        replace_file(logical_path, topo.logical.read_bytes())
    updated = re.sub(
        r"(?m)^TOPOLOGY_FILE[ \t]+[^\r\n]+",
        lambda _: f"TOPOLOGY_FILE {container_path(destination)}", original_config,
    )
    replace_file(CONFIG, updated.encode())


def simulate(container: str, topo: Topology, directory: str, prefix: str, run_dir: Path):
    workload = workload_path(directory, prefix)
    # The container shell publishes its PID before exec so an interrupted
    # host can stop the simulator before touching the shared config again.
    pid_path = SCRATCH / f".torus-{run_dir.parent.name}-{run_dir.name}.pid"
    command = [
        "docker", "exec", "-w", container_path(SCRATCH), container,
        "sh", "-c", 'printf "%s\\n" "$$" > "$1" || exit 1; shift; exec "$@"',
        "torus-sweep", container_path(pid_path), "./ns3.42-AstraSimNetwork-default",
        f"--workload-configuration={container_path(workload)}",
        f"--comm-group-configuration={container_path(workload.with_suffix('.json'))}",
        f"--system-configuration={container_path(topo.system)}",
        f"--remote-memory-configuration={container_path(MEMORY)}",
        f"--network-configuration={container_path(CONFIG)}",
        f"--logical-topology-configuration={container_path(workload.parent / topo.logical.name)}",
    ]
    with (run_dir / "simulator.log").open("wb") as output:
        with subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT,
                              start_new_session=True) as process:
            try:
                return process.wait()
            except KeyboardInterrupt:
                if process.poll() is None:
                    # Allow the exec wrapper to publish its PID if interrupted at launch.
                    for _ in range(20):
                        if pid_path.is_file():
                            break
                        try:
                            process.wait(timeout=0.1)
                            break
                        except subprocess.TimeoutExpired:
                            pass
                if process.poll() is None and pid_path.is_file():
                    pid = pid_path.read_text().strip()
                    if pid.isdecimal():
                        subprocess.run(["docker", "exec", container, "kill", "-TERM", pid],
                                       check=False)
                        try:
                            process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            subprocess.run(["docker", "exec", container, "kill", "-KILL", pid],
                                           check=False)
                if process.poll() is None and not pid_path.is_file():
                    process.terminate()
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


def run_one(container: str, topo: Topology, workload, batch: Path, journal, outcomes):
    label, directory, prefix = workload
    fields = {"topology": topo.name, "trace": label}
    key = (topo.name, label)
    run_dir = batch / f"{label}_{topo.name}"
    run_dir.mkdir()
    print(f"Running {label} on {topo.name}", flush=True)
    old_logs = log_state()
    outputs = [OUTPUT / name for name in ("fct.txt", "qlen.txt", "pfc.txt", "mix.tr")]
    old_outputs = {path: file_state(path) for path in outputs}
    started = container_time(container)
    record(journal, "simulation_started", **fields, container_start=started.isoformat())
    outcomes[key] = "simulation_pending"
    exit_code = simulate(container, topo, directory, prefix, run_dir)
    outcomes[key] = "analysis_pending" if exit_code == 0 else "simulation_failed"
    record(journal, "simulation_finished", **fields, exit_code=exit_code,
           simulator_log=str(run_dir / "simulator.log"))

    def finish(status, **details):
        record(journal, "analysis_finished", **fields, status=status, **details)
        outcomes[key] = status if exit_code == 0 else "simulation_failed"
        print(f"{label} on {topo.name}: {status}", flush=True)

    if exit_code:
        finish("skipped", reason=f"Simulator exited with status {exit_code}")
        return
    ended = container_time(container)
    log, sources = find_log(old_logs, started, ended, run_dir / "run.log")
    if log is None:
        finish("skipped", reason="No fresh log contains all 32 rank completions",
               container_start=started.isoformat(), container_end=ended.isoformat())
        return
    stale = [path.name for path in outputs if file_state(path) in (None, old_outputs[path])]
    if stale:
        finish("skipped", reason=f"Missing or unchanged NS-3 output: {', '.join(stale)}")
        return
    report = PROJECT / "results" / f"{report_stem(topo.name, label)}.md"
    record(journal, "analysis_started", **fields, log=str(log),
           log_sources=[str(path) for path in sources], container_end=ended.isoformat())
    with (run_dir / "analysis.log").open("w+") as output:
        result = subprocess.run(
            [sys.executable, "scripts/analyze_ns3_results.py", str(OUTPUT.relative_to(PROJECT)),
             "--log", str(log), "-o", str(report.relative_to(PROJECT))],
            cwd=PROJECT, stdout=output, stderr=subprocess.STDOUT,
        )
        output.seek(0)
        messages = output.read().splitlines()
    actual_report = PROJECT / messages[-1] if messages else None
    if result.returncode or actual_report is None or not actual_report.is_file():
        finish("failed", reason="Analyzer did not produce a report",
               analyzer_log=str(run_dir / "analysis.log"))
    else:
        finish("success", report=str(actual_report), log=str(log))


def run_sweep(container: str, topologies: list[Topology], results: Path, reports: dict) -> int:
    batch_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    batch = results / f"torus_sweep_{batch_id}"
    batch.mkdir()
    backups = batch / "backups"
    backups.mkdir()
    files = {CONFIG}
    files.update(
        ASTRA / "traces" / directory / topo.logical.name
        for topo in topologies for _, directory, _ in WORKLOADS
    )
    original = {}
    for path in sorted(files):
        if path.exists():
            backup = backups / path.relative_to(ASTRA)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, backup)
            original[path] = backup
        else:
            original[path] = None
    plan = [(topo.name, label) for topo in topologies for label, _, _ in WORKLOADS]
    outcomes = dict.fromkeys(plan, "not_started")
    journal_path = batch.with_suffix(".jsonl")
    with journal_path.open("x") as journal:
        record(journal, "planned", runs=[{"topology": topo, "trace": label}
                                       for topo, label in plan])
        print(f"Progress journal: {journal_path}", flush=True)
        interrupted = False
        try:
            for topo in topologies:
                pending = []
                for workload in WORKLOADS:
                    label = workload[0]
                    report = reports.get((topo.name, label))
                    if report is None:
                        pending.append(workload)
                        continue
                    outcomes[topo.name, label] = "already_reported"
                    record(journal, "run_skipped", topology=topo.name, trace=label,
                           reason="Report already exists", report=str(report))
                    print(f"Skipping {label} on {topo.name}: {report.name} exists", flush=True)
                if not pending:
                    continue
                try:
                    prepare_topology(topo, original[CONFIG].read_bytes().decode(), batch / topo.filename)
                except (OSError, ValueError, subprocess.SubprocessError) as error:
                    for label, _, _ in pending:
                        outcomes[topo.name, label] = "skipped"
                        record(journal, "run_skipped", topology=topo.name, trace=label,
                               reason=f"Topology setup failed: {error}")
                    continue
                for workload in pending:
                    label = workload[0]
                    key = (topo.name, label)
                    try:
                        run_one(container, topo, workload, batch, journal, outcomes)
                    except KeyboardInterrupt:
                        record(journal, "run_interrupted", topology=topo.name, trace=label,
                               previous_status=outcomes[key])
                        raise
                    except (OSError, ValueError, subprocess.SubprocessError) as error:
                        previous = outcomes[key]
                        outcomes[key] = "failed"
                        if previous == "analysis_pending":
                            record(journal, "analysis_finished", topology=topo.name, trace=label,
                                   status="failed", reason=str(error))
                        else:
                            record(journal, "run_error", topology=topo.name, trace=label,
                                   previous_status=previous, reason=str(error))
        except KeyboardInterrupt:
            interrupted = True
        finally:
            restore_errors = []
            for path, backup in original.items():
                try:
                    if backup is None:
                        path.unlink(missing_ok=True)
                    else:
                        replace_file(path, backup.read_bytes())
                except OSError as error:
                    restore_errors.append(str(error))
            counts = {status: list(outcomes.values()).count(status)
                      for status in sorted(set(outcomes.values()))}
            record(journal, "summary", interrupted=interrupted, counts=counts,
                   restore_errors=restore_errors)
            print(json.dumps(counts), flush=True)
            for error in restore_errors:
                print(f"Restore failed: {error}", file=sys.stderr)
    if interrupted:
        return 130
    completed = counts.get("success", 0) + counts.get("already_reported", 0)
    return int(completed != len(plan) or bool(restore_errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--container", default="d873db5c7fa0")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the matrix without accessing Docker or writing files")
    parser.add_argument("--missing-only", action="store_true",
                        help="Run only combinations without a report in results/")
    args = parser.parse_args()
    try:
        topologies = load_topologies(PROJECT / "topologies/torus_list.txt")
        results = PROJECT / "results"
        plan = [(topo.name, label) for topo in topologies for label, _, _ in WORKLOADS]
        if args.dry_run:
            reports = existing_reports(results, plan) if args.missing_only else {}
            for topo in topologies:
                for label, directory, prefix in WORKLOADS:
                    if (topo.name, label) in reports:
                        continue
                    print(topo.name, label, workload_path(directory, prefix).relative_to(PROJECT),
                          topo.logical.relative_to(PROJECT), topo.system.relative_to(PROJECT))
            print(f"{len(topologies)} topologies, {len(plan) - len(reports)} runs, "
                  f"{len(reports)} existing reports skipped")
            return 0
        results.mkdir(exist_ok=True)
        with (results / ".torus_sweep.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise ValueError("A torus sweep is already running in this workspace") from None
            reports = existing_reports(results, plan) if args.missing_only else {}
            pending = [(topology, trace) for topology, trace in plan if (topology, trace) not in reports]
            if not pending:
                print(f"All {len(plan)} runs already have reports in {results}.", flush=True)
                return 0
            pending_topologies = {topology for topology, _ in pending}
            pending_traces = {trace for _, trace in pending}
            preflight([topo for topo in topologies if topo.name in pending_topologies],
                      args.container, [workload for workload in WORKLOADS if workload[0] in pending_traces])
            return run_sweep(args.container, topologies, results, reports)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"Torus sweep could not proceed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    def interrupt(_signal, _frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGTERM, interrupt)
    sys.exit(main())
