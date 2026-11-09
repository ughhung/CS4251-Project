#!/usr/bin/env python3
"""Generate a Markdown report from an ASTRA-sim NS-3 result directory.

The script understands the files emitted by the NS-3 backend:
  fct.txt, qlen.txt, pfc.txt, flow.txt, trace.txt, and mix.tr.

The packet trace is the binary TraceFormat record used by the backend. The
current format is 56 bytes per record; the trailing SimSetting block is left
out of the packet-record scan.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import math
import re
import struct
from collections import Counter
from pathlib import Path
from statistics import mean


FCT_FIELDS = ("source", "destination", "sport", "dport", "size", "start_ns", "fct_ns", "standalone_ns")
TRACE_RECORD_SIZE = 56
TRACE_HEADER = struct.Struct("<QHBBIIIHBBBB")
EVENT_NAMES = {0: "Recv", 1: "Enqu", 2: "Dequ", 3: "Drop"}


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    values = sorted(values)
    return values[int((len(values) - 1) * fraction)]


def fmt_num(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:,.3f}"
    return f"{value:,}"


def fmt_time_ns(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    value = float(value)
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.3f} s"
    if value >= 1_000_000:
        return f"{value / 1_000_000:.3f} ms"
    if value >= 1_000:
        return f"{value / 1_000:.3f} us"
    return f"{value:.0f} ns"


def fmt_bytes(value: int | None) -> str:
    if value is None:
        return "n/a"
    value = float(value)
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if abs(value) < 1024 or unit == "TiB":
            return f"{value:,.2f} {unit}"
        value /= 1024
    return "n/a"


def read_fct(path: Path) -> dict:
    rows = []
    malformed = 0
    with path.open() as handle:
        for line_no, line in enumerate(handle, 1):
            fields = line.split()
            if not fields:
                continue
            if len(fields) != 8:
                malformed += 1
                continue
            try:
                rows.append(
                    {
                        "source": fields[0],
                        "destination": fields[1],
                        "sport": int(fields[2]),
                        "dport": int(fields[3]),
                        "size": int(fields[4]),
                        "start_ns": int(fields[5]),
                        "fct_ns": int(fields[6]),
                        "standalone_ns": int(fields[7]),
                    }
                )
            except ValueError:
                malformed += 1

    fcts = [row["fct_ns"] for row in rows]
    standalone = [row["standalone_ns"] for row in rows]
    slowdowns = [
        row["fct_ns"] / row["standalone_ns"]
        for row in rows
        if row["standalone_ns"] > 0
    ]
    grouped = {}
    for size in sorted({row["size"] for row in rows}):
        group = [row for row in rows if row["size"] == size]
        gfct = [row["fct_ns"] for row in group]
        gbase = [row["standalone_ns"] for row in group]
        gslow = [
            row["fct_ns"] / row["standalone_ns"]
            for row in group
            if row["standalone_ns"] > 0
        ]
        grouped[size] = {
            "count": len(group),
            "median_fct": percentile(gfct, 0.50),
            "p95_fct": percentile(gfct, 0.95),
            "max_fct": max(gfct) if gfct else None,
            "median_standalone": percentile(gbase, 0.50),
            "mean_slowdown": mean(gslow) if gslow else None,
        }

    network_end = max(
        (row["start_ns"] + row["fct_ns"] for row in rows), default=None
    )
    return {
        "rows": len(rows),
        "malformed": malformed,
        "total_bytes": sum(row["size"] for row in rows),
        "mean_fct": mean(fcts) if fcts else None,
        "median_fct": percentile(fcts, 0.50),
        "p95_fct": percentile(fcts, 0.95),
        "max_fct": max(fcts) if fcts else None,
        "median_standalone": percentile(standalone, 0.50),
        "median_slowdown": percentile(slowdowns, 0.50),
        "p95_slowdown": percentile(slowdowns, 0.95),
        "max_slowdown": max(slowdowns) if slowdowns else None,
        "network_end_ns": network_end,
        "by_size": grouped,
    }


def read_qlen(path: Path) -> dict:
    result = {
        "records": 0,
        "first_ns": None,
        "last_ns": None,
        "max_bytes": None,
        "max_switch": None,
        "max_port": None,
        "malformed": 0,
    }
    with path.open() as handle:
        for line in handle:
            fields = line.split()
            if len(fields) < 6 or fields[0] != "time":
                if fields:
                    result["malformed"] += 1
                continue
            try:
                timestamp = int(fields[1])
                switch = int(fields[2])
            except ValueError:
                result["malformed"] += 1
                continue
            result["records"] += 1
            result["first_ns"] = timestamp if result["first_ns"] is None else min(result["first_ns"], timestamp)
            result["last_ns"] = timestamp if result["last_ns"] is None else max(result["last_ns"], timestamp)
            for index in range(3, len(fields) - 1):
                if fields[index] != "j":
                    continue
                try:
                    port = int(fields[index + 1])
                    queued = int(fields[index + 2])
                except (ValueError, IndexError):
                    continue
                if result["max_bytes"] is None or queued > result["max_bytes"]:
                    result.update(max_bytes=queued, max_switch=switch, max_port=port)
    result["observed_duration_ns"] = (
        result["last_ns"] - result["first_ns"]
        if result["first_ns"] is not None and result["last_ns"] is not None
        else None
    )
    return result


def read_pfc(path: Path) -> dict:
    count = 0
    first = last = None
    with path.open() as handle:
        for line in handle:
            fields = line.split()
            if not fields:
                continue
            count += 1
            try:
                timestamp = int(fields[0])
                first = timestamp if first is None else min(first, timestamp)
                last = timestamp if last is None else max(last, timestamp)
            except ValueError:
                pass
    return {"events": count, "first_ns": first, "last_ns": last}


def read_simple_counts(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open() as handle:
        return sum(1 for line in handle if line.strip())


def read_flow_count(path: Path) -> int | None:
    """Read the first-line flow count used by the NS-3 flow input file."""
    if not path.exists():
        return None
    try:
        first = path.read_text().split()
        return int(first[0]) if first else None
    except ValueError:
        return None


def read_trace_nodes(path: Path) -> list[int]:
    if not path.exists():
        return []
    tokens = path.read_text().split()
    if not tokens:
        return []
    try:
        count = int(tokens[0])
        return [int(token) for token in tokens[1 : count + 1]]
    except ValueError:
        return []


def read_mix_trace(path: Path, record_size: int = TRACE_RECORD_SIZE) -> dict:
    """Parse binary TraceFormat records and skip any trailing SimSetting bytes."""
    result = {
        "records": 0,
        "invalid_records": 0,
        "first_ns": None,
        "last_ns": None,
        "events": Counter(),
        "node_types": Counter(),
        "max_qlen": None,
        "max_qlen_node": None,
        "max_qlen_interface": None,
        "max_packet_bytes": None,
        "max_time_ns": None,
        "bytes_by_event": Counter(),
        "setting_entries": 0,
        "window_bytes": None,
        "trace_offset": 0,
        "interface_rates": {},
        "dequeue_bytes_by_interface": Counter(),
        "packet_queue_durations": [],
        "unmatched_dequeues": 0,
        "enqueue_key_collisions": 0,
    }
    if record_size < TRACE_HEADER.size:
        raise ValueError("trace record size must be at least 32 bytes")
    pending_enqueues = {}
    with path.open("rb") as handle:
        # mix.tr begins with SimSetting: uint32 entry count, followed by
        # (uint16 node, uint8 interface, uint64 bit-rate) entries and a
        # uint32 window bound. The packet records follow that header.
        prefix = handle.read(4)
        if len(prefix) == 4:
            entry_count = struct.unpack("<I", prefix)[0]
            settings_size = 4 + entry_count * 11 + 4
            valid_header = (
                entry_count <= 100_000
                and path.stat().st_size >= settings_size
                and (path.stat().st_size - settings_size) % record_size == 0
            )
            if valid_header:
                settings = handle.read(entry_count * 11)
                window = handle.read(4)
                if len(settings) == entry_count * 11 and len(window) == 4:
                    result["setting_entries"] = entry_count
                    result["window_bytes"] = struct.unpack("<I", window)[0]
                    result["trace_offset"] = settings_size
                    for index in range(entry_count):
                        offset = index * 11
                        node, interface, rate = struct.unpack_from("<HBQ", settings, offset)
                        result["interface_rates"][(node, interface)] = rate
                else:
                    handle.seek(0)
            else:
                handle.seek(0)
        while True:
            block = handle.read(record_size)
            if len(block) < record_size:
                break
            try:
                time_ns, node, interface, _qidx, qlen, _sip, _dip, size, _l3, event, _ecn, node_type = TRACE_HEADER.unpack_from(block)
            except struct.error:
                result["invalid_records"] += 1
                continue
            # Detect a trace generated with a different ABI rather than
            # presenting nonsensical values as valid utilization results.
            if event not in EVENT_NAMES or node_type not in (0, 1) or node > 65535:
                result["invalid_records"] += 1
                continue
            result["records"] += 1
            result["events"][EVENT_NAMES[event]] += 1
            result["node_types"]["switch" if node_type else "host"] += 1
            result["first_ns"] = time_ns if result["first_ns"] is None else min(result["first_ns"], time_ns)
            result["last_ns"] = time_ns if result["last_ns"] is None else max(result["last_ns"], time_ns)
            result["max_time_ns"] = time_ns if result["max_time_ns"] is None else max(result["max_time_ns"], time_ns)
            result["bytes_by_event"][EVENT_NAMES[event]] += size
            if event == 2:  # Dequ: bytes leaving an interface
                result["dequeue_bytes_by_interface"][(node, interface)] += size
            if event in (1, 2):  # Enqu/Dequ: data-packet union fields
                # The data union is: uint16 sport, uint16 dport, uint32 seq,
                # uint64 timestamp, uint16 page, uint16 payload.
                sport, dport, sequence, _packet_ts, page, _payload = struct.unpack_from(
                    "<HHI4xQHH", block, 32
                )
                packet_key = (node, interface, _qidx, _sip, _dip, sport, dport, sequence, page)
                if event == 1:
                    if packet_key in pending_enqueues:
                        result["enqueue_key_collisions"] += 1
                    pending_enqueues[packet_key] = time_ns
                elif packet_key in pending_enqueues:
                    enqueue_time = pending_enqueues.pop(packet_key)
                    if time_ns >= enqueue_time:
                        result["packet_queue_durations"].append(time_ns - enqueue_time)
                    else:
                        result["unmatched_dequeues"] += 1
                else:
                    # The backend can emit a second Dequ record for the same
                    # packet through its RDMA-QP dequeue trace source.
                    result["unmatched_dequeues"] += 1
            if result["max_qlen"] is None or qlen > result["max_qlen"]:
                result.update(max_qlen=qlen, max_qlen_node=node, max_qlen_interface=interface)
            if result["max_packet_bytes"] is None or size > result["max_packet_bytes"]:
                result["max_packet_bytes"] = size
    result["trailing_bytes"] = path.stat().st_size % record_size
    result["recognized"] = (
        result["records"] > 0
        and result["invalid_records"] <= max(10, result["records"] // 10)
        and (result["max_time_ns"] or 0) <= 10**15
    )
    durations = result["packet_queue_durations"]
    result["packet_queue_count"] = len(durations)
    result["packet_queue_median_ns"] = percentile(durations, 0.50)
    result["packet_queue_p95_ns"] = percentile(durations, 0.95)
    result["packet_queue_max_ns"] = max(durations) if durations else None
    result["packet_queue_mean_ns"] = mean(durations) if durations else None
    # Keep the report object compact after calculating summary statistics.
    result.pop("packet_queue_durations", None)
    if result["recognized"] and result["first_ns"] is not None and result["last_ns"] > result["first_ns"]:
        duration_seconds = (result["last_ns"] - result["first_ns"]) / 1e9
        utilizations = []
        for key, byte_count in result["dequeue_bytes_by_interface"].items():
            rate = result["interface_rates"].get(key)
            if rate:
                utilizations.append((key, byte_count * 8 / duration_seconds / rate))
        result["interface_utilizations"] = utilizations
    else:
        result["interface_utilizations"] = []
    return result


def read_completion_log(path: Path | None) -> dict:
    if path is None or not path.exists():
        return {
            "ranks": 0,
            "max_cycles": None,
            "min_cycles": None,
            "max_exposed_cycles": None,
            "cycles": {},
            "roofline_stats": {},
        }
    pattern = re.compile(
        r"sys\[(\d+)\] finished,\s+(\d+) cycles"
        r"(?:,\s+exposed communication\s+(\d+) cycles)?"
    )
    metric_pattern = re.compile(
        r"sys\[(\d+)\],\s*([^:]+):\s*"
        r"([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)\s*(%)?"
    )
    cycles = {}
    exposed_cycles = []
    roofline_stats = {}
    with path.open(errors="replace") as handle:
        for line in handle:
            match = pattern.search(line)
            if match:
                cycles[int(match.group(1))] = int(match.group(2))
                if match.group(3) is not None:
                    exposed_cycles.append(int(match.group(3)))
            metric_match = metric_pattern.search(line)
            if metric_match:
                rank = int(metric_match.group(1))
                metric = metric_match.group(2).strip()
                value = float(metric_match.group(3))
                unit = metric_match.group(4) or ""
                roofline_stats.setdefault(rank, {})[metric] = {
                    "value": value,
                    "unit": unit,
                }
    rank_cycles = cycles.values()
    return {
        "ranks": len(cycles),
        "max_cycles": max(rank_cycles, default=None),
        "min_cycles": min(rank_cycles, default=None),
        "max_exposed_cycles": max(exposed_cycles, default=None),
        "cycles": cycles,
        "roofline_stats": roofline_stats,
    }


def md_row(values: list[object]) -> str:
    return "| " + " | ".join(str(value) for value in values) + " |"


def generate_report(result_dir: Path, output: Path, completion_log: Path | None, trace_record_size: int) -> None:
    fct_path = result_dir / "fct.txt"
    qlen_path = result_dir / "qlen.txt"
    pfc_path = result_dir / "pfc.txt"
    mix_path = result_dir / "mix.tr"
    flow_path = result_dir / "flow.txt"
    trace_path = result_dir / "trace.txt"

    fct = read_fct(fct_path) if fct_path.exists() else {"rows": 0, "by_size": {}}
    qlen = read_qlen(qlen_path) if qlen_path.exists() else {}
    pfc = read_pfc(pfc_path) if pfc_path.exists() else {"events": 0}
    mix = read_mix_trace(mix_path, trace_record_size) if mix_path.exists() else {}
    completion = read_completion_log(completion_log)
    roofline_stats = completion.get("roofline_stats", {})

    lines = [
        f"# ASTRA-sim NS-3 Results Report",
        "",
        f"Result directory: `{result_dir}`",
        "",
        "## Completion summary",
        "",
        md_row(["Metric", "Result"]),
        md_row(["---", "---"]),
        md_row(["ASTRA workload ranks with completion log", completion.get("ranks", 0) or "not supplied"]),
        md_row(["Total workload completion (cycles)", fmt_num(completion.get("max_cycles")) if completion.get("max_cycles") is not None else "not available; supply --log" ]),
        md_row(["Fastest rank completion (cycles)", fmt_num(completion.get("min_cycles"))]),
        md_row(["Maximum exposed communication (cycles)", fmt_num(completion.get("max_exposed_cycles"))]),
        md_row(["Completed network flows", fmt_num(fct.get("rows"))]),
        md_row(["Total bytes sent", fmt_num(fct.get("total_bytes"))]),
        md_row(["Network-flow finish proxy", fmt_time_ns(fct.get("network_end_ns"))]),
        "",
        "The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.",
        "",
        "## Roofline statistics",
        "",
    ]
    if not roofline_stats:
        if completion_log is None or not completion_log.exists():
            lines.append(
                "Roofline statistics are unavailable because the simulator log was not supplied or could not be found. Pass the run's log with `--log`; ASTRA-sim emits these metrics when roofline is enabled."
            )
        else:
            lines.append(
                "No roofline statistics were found in the supplied log. Confirm that roofline was enabled for that run."
            )
    else:
        metrics = sorted(
            {
                metric
                for rank_stats in roofline_stats.values()
                for metric in rank_stats
            }
        )
        metric_units = {
            metric: next(
                (
                    values[metric]["unit"]
                    for values in roofline_stats.values()
                    if metric in values
                ),
                "",
            )
            for metric in metrics
        }
        rank_ids = sorted(set(completion.get("cycles", {})) | set(roofline_stats))
        lines += [
            "Summary across ranks (arithmetic mean of ranks that logged each metric):",
            "",
            md_row(["Metric", "Mean", "Minimum", "Maximum", "Ranks reported"]),
            md_row(["---", "---", "---", "---", "---"]),
        ]
        for metric in metrics:
            values = [
                rank_stats[metric]["value"]
                for rank_stats in roofline_stats.values()
                if metric in rank_stats
            ]
            unit = metric_units[metric]
            label = f"{metric} ({unit})" if unit else metric
            lines.append(
                md_row(
                    [
                        label,
                        f"{mean(values):,.3f}{unit}",
                        f"{min(values):,.3f}{unit}",
                        f"{max(values):,.3f}{unit}",
                        fmt_num(len(values)),
                    ]
                )
            )
        lines += [
            "",
            "Per-rank values:",
            "",
            md_row(["Rank", "Metric", "Value"]),
            md_row(["---", "---", "---"]),
        ]
        for rank in rank_ids:
            rank_stats = roofline_stats.get(rank, {})
            for metric in metrics:
                unit = metric_units[metric]
                value = (
                    f"{rank_stats[metric]['value']:,.3f}{rank_stats[metric]['unit']}"
                    if metric in rank_stats
                    else "n/a"
                )
                lines.append(md_row([rank, metric, value]))
    lines += [
        "",
        "## Flow-completion metrics",
        "",
        md_row(["Metric", "Value"]),
        md_row(["---", "---"]),
        md_row(["Mean FCT", fmt_time_ns(fct.get("mean_fct"))]),
        md_row(["Median FCT", fmt_time_ns(fct.get("median_fct"))]),
        md_row(["p95 FCT", fmt_time_ns(fct.get("p95_fct"))]),
        md_row(["Maximum FCT", fmt_time_ns(fct.get("max_fct"))]),
        md_row(["Median standalone time", fmt_time_ns(fct.get("median_standalone"))]),
        md_row(["Median FCT / standalone", f"{fct.get('median_slowdown', float('nan')):.3f}x" if fct.get("median_slowdown") is not None else "n/a"]),
        md_row(["p95 FCT / standalone", f"{fct.get('p95_slowdown', float('nan')):.3f}x" if fct.get("p95_slowdown") is not None else "n/a"]),
        md_row(["Maximum FCT / standalone", f"{fct.get('max_slowdown', float('nan')):.3f}x" if fct.get("max_slowdown") is not None else "n/a"]),
        "",
        "## FCT by message size",
        "",
        md_row(["Size", "Flows", "Median FCT", "p95 FCT", "Max FCT", "Median standalone", "Mean slowdown"]),
        md_row(["---", "---", "---", "---", "---", "---", "---"]),
    ]
    for size, group in fct.get("by_size", {}).items():
        lines.append(md_row([
            fmt_bytes(size), fmt_num(group["count"]), fmt_time_ns(group["median_fct"]),
            fmt_time_ns(group["p95_fct"]), fmt_time_ns(group["max_fct"]),
            fmt_time_ns(group["median_standalone"]),
            f"{group['mean_slowdown']:.3f}x" if group["mean_slowdown"] is not None else "n/a",
        ]))

    lines += ["", "## Queue metrics", "", md_row(["Metric", "Result"]), md_row(["---", "---"])]
    if qlen:
        lines += [
            md_row(["Queue records", fmt_num(qlen.get("records"))]),
            md_row(["Observed queue interval", f"{fmt_time_ns(qlen.get('first_ns'))} to {fmt_time_ns(qlen.get('last_ns'))}"]),
            md_row(["Observed queue duration", fmt_time_ns(qlen.get("observed_duration_ns"))]),
            md_row(["Maximum sampled queue", fmt_bytes(qlen.get("max_bytes"))]),
            md_row(["Maximum queue location", f"switch {qlen.get('max_switch')}, port {qlen.get('max_port')}" if qlen.get("max_bytes") is not None else "n/a"]),
        ]
    else:
        lines.append(md_row(["Queue data", "qlen.txt not supplied"]))
    lines += [
        "",
        "The queue interval is the time span covered by non-empty queue records; it is not per-flow queueing duration.",
        "",
        "## PFC and flow inputs",
        "",
        md_row(["Metric", "Result"]),
        md_row(["---", "---"]),
        md_row(["PFC events", fmt_num(pfc.get("events"))]),
        md_row(["Static flows declared", fmt_num(read_flow_count(flow_path))]),
        md_row(["Trace nodes listed", fmt_num(len(read_trace_nodes(trace_path)))]),
        "",
        "## Packet trace",
        "",
    ]
    if mix:
        lines += [
            md_row(["Metric", "Result"]),
            md_row(["---", "---"]),
            md_row(["Trace records recognized", fmt_num(mix.get("records"))]),
            md_row(["Invalid/unrecognized records", fmt_num(mix.get("invalid_records"))]),
            md_row(["Trace format recognized", "yes" if mix.get("recognized") else "no; check ABI/record size"]),
            md_row(["Packet trace interval", f"{fmt_time_ns(mix.get('first_ns'))} to {fmt_time_ns(mix.get('last_ns'))}" if mix.get("recognized") else "unavailable (trace format mismatch)"]),
            md_row(["Maximum sampled packet queue", fmt_bytes(mix.get("max_qlen")) if mix.get("recognized") else "unavailable"]),
            md_row(["Maximum packet size", fmt_bytes(mix.get("max_packet_bytes")) if mix.get("recognized") else "unavailable"]),
            md_row(["SimSetting interface entries", fmt_num(mix.get("setting_entries"))]),
            md_row(["SimSetting window", fmt_bytes(mix.get("window_bytes"))]),
            md_row(["Events", ", ".join(f"{key}: {value:,}" for key, value in sorted(mix.get("events", {}).items())) or "n/a"]),
            md_row(["Bytes by event", ", ".join(f"{key}: {fmt_bytes(value)}" for key, value in sorted(mix.get("bytes_by_event", {}).items())) or "n/a"]),
            md_row(["Observed interface utilization", (
                f"{len(mix.get('interface_utilizations', []))} interfaces; "
                f"mean {mean(v for _, v in mix['interface_utilizations']) * 100:.3f}%, "
                f"max {max(v for _, v in mix['interface_utilizations']) * 100:.3f}%"
                if mix.get("interface_utilizations") else "n/a"
            )]),
            md_row(["Matched packet queue durations", fmt_num(mix.get("packet_queue_count"))]),
            md_row(["Median packet queue time", fmt_time_ns(mix.get("packet_queue_median_ns"))]),
            md_row(["p95 packet queue time", fmt_time_ns(mix.get("packet_queue_p95_ns"))]),
            md_row(["Maximum packet queue time", fmt_time_ns(mix.get("packet_queue_max_ns"))]),
            md_row(["Mean packet queue time", fmt_time_ns(mix.get("packet_queue_mean_ns"))]),
            md_row(["Unmatched/duplicate dequeues", fmt_num(mix.get("unmatched_dequeues"))]),
            md_row(["Enqueue-key collisions", fmt_num(mix.get("enqueue_key_collisions"))]),
        ]
    else:
        lines.append(md_row(["Packet trace", "mix.tr not supplied"]))
    lines += [
        "",
        "This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.",
        "",
        "## Scaling",
        "",
        "This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.",
        "",
    ]
    # Exclusive creation guarantees that a report path is never overwritten,
    # including when two analyzer runs happen to choose the same timestamp.
    with output.open("x", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def choose_output_path(results_dir: Path, requested: Path | None) -> Path:
    """Choose a fresh Markdown path, preserving an explicit unused path."""
    if requested is None:
        parent = Path(__file__).resolve().parents[1] / "results"
        parent.mkdir(parents=True, exist_ok=True)
        stem = "report"
        suffix = ".md"
        add_timestamp = True
    else:
        parent = requested.parent
        stem = requested.stem if requested.suffix else requested.name
        suffix = requested.suffix or ".md"
        add_timestamp = requested.exists()
        if not add_timestamp:
            return requested

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    candidate = parent / f"{stem}_{timestamp}{suffix}"
    counter = 1
    while candidate.exists():
        candidate = parent / f"{stem}_{timestamp}_{counter}{suffix}"
        counter += 1
    return candidate


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results_dir", type=Path, help="Directory containing fct.txt, qlen.txt, pfc.txt, mix.tr, etc.")
    parser.add_argument(
        "-o", "--output", type=Path,
        help="Markdown report path (default: timestamped report in project results/; if it exists, a timestamped path is used)",
    )
    parser.add_argument(
        "--log", type=Path,
        help="ASTRA-sim stdout/spdlog file with completion lines and optional roofline statistics",
    )
    parser.add_argument("--trace-record-size", type=int, default=TRACE_RECORD_SIZE, help="Binary mix.tr record size; default: 56")
    args = parser.parse_args()
    if not args.results_dir.is_dir():
        parser.error(f"result directory does not exist: {args.results_dir}")
    output = choose_output_path(args.results_dir, args.output)
    while True:
        try:
            generate_report(args.results_dir, output, args.log, args.trace_record_size)
            break
        except FileExistsError:
            # Another run may have claimed the candidate between selection and
            # file creation. Generate a fresh timestamped candidate and retry.
            output = choose_output_path(args.results_dir, output)
    print(output)


if __name__ == "__main__":
    main()
