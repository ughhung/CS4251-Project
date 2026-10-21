# ASTRA-sim NS-3: Reproducing the 32-Rank Ring Experiment

This guide is a beginner-friendly recipe for reproducing the 32-rank ring experiment, understanding every input, and interpreting the outputs.

## Experiment at a glance

- 32 ASTRA-sim ranks (simulated compute endpoints).
- One logical ring containing ranks 0 through 31.
- A physical network with 32 hosts and 32 switches. Each host connects to one switch; the switches form a ring.
- Workload prefix: traces/tai-trace/dense32_validmb.
- Native ring collective configuration: astra-sim/examples/system/native_collectives/Ring_4chunks.json.
- NS-3 links: 25 Gb/s and 0.005 ms delay.

## Files and what they mean

| File | Purpose |
| --- | --- |
| [traces/tai-trace/dense32_validmb](traces/tai-trace/dense32_validmb) | Workload prefix. Its rank files are normally dense32_validmb.0.et through dense32_validmb.31.et. |
| [traces/tai-trace/dense32_validmb.json](traces/tai-trace/dense32_validmb.json) | Communication groups. Groups list participating rank IDs; they are not switches. |
| [traces/tai-trace/logical_topology.json](traces/tai-trace/logical_topology.json) | Logical collective topology. Current content: {"logical-dims":["32"]}. |
| [astra-sim/examples/system/native_collectives/Ring_4chunks.json](astra-sim/examples/system/native_collectives/Ring_4chunks.json) | ASTRA system model and ring collective settings. |
| [astra-sim/examples/remote_memory/analytical/no_memory_expansion.json](astra-sim/examples/remote_memory/analytical/no_memory_expansion.json) | Remote-memory model used by this run. |
| [astra-sim/extern/network_backend/ns-3/scratch/topology/32nodes_ring_topology.txt](astra-sim/extern/network_backend/ns-3/scratch/topology/32nodes_ring_topology.txt) | Physical NS-3 topology. |
| [astra-sim/extern/network_backend/ns-3/scratch/config/config_ring32.txt](astra-sim/extern/network_backend/ns-3/scratch/config/config_ring32.txt) | NS-3 settings and input/output paths. |
| [scripts/analyze_ns3_results.py](scripts/analyze_ns3_results.py) | Parses outputs and creates a Markdown metrics report. |

The executable was run in a container where the repository is mounted at /app/astra-sim and traces are under /root/traces/tai-trace. Paths in configuration files must exist inside the runtime environment.

## Logical topology, physical topology, ranks, and groups

A rank is one simulated compute endpoint, analogous to one distributed-training process or accelerator. Rank IDs are 0 through 31.

The logical topology describes the order used by a collective. The current file is:

~~~json
{"logical-dims":["32"]}
~~~

This means one logical ring of 32 ranks. A multidimensional example is:

~~~json
{"logical-dims":["8","4"]}
~~~

The product of the dimensions must equal 32.

The physical topology describes where packets travel. A logical edge from rank 0 to rank 1 can travel through several physical switches. This separation lets the same collective be tested on different networks.

A communication group is a workload-defined set of ranks, for example:

~~~json
{"0":[0,1,2,3,4,5,6,7]}
~~~

This says operation group 0 contains eight ranks. A singleton group such as {"13":[13]} contains one rank. Group IDs do not represent switches.

## System configuration and collective algorithms

Ring_4chunks.json selects ASTRA-sim's native ring collective implementation. A collective is a communication operation involving several ranks, such as all-reduce, all-gather, or broadcast. A ring algorithm passes data chunks around a circular rank order until the operation is complete.

preferred-dataset-splits: 4 tells the system model to divide a collective's data into four preferred pieces. It does not mean there are four switches. The same JSON also sets compute, memory, endpoint-delay, and algorithm assumptions. Keep it unchanged when comparing physical network designs.

## Physical topology format

The supplied topology starts like this:

~~~text
64 32 64
32 33 34 ... 63
0 32 25Gbps 0.005ms 0
1 33 25Gbps 0.005ms 0
...
31 63 25Gbps 0.005ms 0
32 33 25Gbps 0.005ms 0
...
63 32 25Gbps 0.005ms 0
~~~

The format is:

~~~text
<total nodes> <switch count> <link count>
<switch IDs>
<source> <destination> <bandwidth> <delay> <error rate>
~~~

Nodes 0--31 are hosts; nodes 32--63 are switches. Each host attaches to its corresponding switch. The switches form a ring. The host/switch form is intentional: a direct host-only ring triggered the NS-3 error “We assume at least one NIC is alive” during route setup.

## Network configuration

config_ring32.txt contains absolute container paths such as:

~~~text
TOPOLOGY_FILE /app/astra-sim/extern/network_backend/ns-3/scratch/topology/32nodes_ring_topology.txt
FLOW_FILE /app/astra-sim/extern/network_backend/ns-3/scratch/output/flow.txt
TRACE_FILE /app/astra-sim/extern/network_backend/ns-3/scratch/output/trace.txt
TRACE_OUTPUT_FILE /app/astra-sim/extern/network_backend/ns-3/scratch/output/mix.tr
FCT_OUTPUT_FILE /app/astra-sim/extern/network_backend/ns-3/scratch/output/fct.txt
PFC_OUTPUT_FILE /app/astra-sim/extern/network_backend/ns-3/scratch/output/pfc.txt
QLEN_MON_FILE /app/astra-sim/extern/network_backend/ns-3/scratch/output/qlen.txt
~~~

It also controls payload size, buffers, congestion control, QCN/PFC, and simulator stop time. Create the output directory before running.

TRACE_FILE selects which physical node IDs are packet-traced. The recorded run selected five nodes (0--4), so utilization from mix.tr covered only those traced interfaces. For whole-topology tracing, use 64 followed by IDs 0 through 63; the binary trace will be much larger.

## Reproduce the run

Inside the container:

~~~bash
mkdir -p /app/astra-sim/extern/network_backend/ns-3/scratch/output
mkdir -p /root/runs/ring32
cd /app/astra-sim/extern/network_backend/ns-3/build/scratch
./ns3.42-AstraSimNetwork-default \
  --workload-configuration=/root/traces/tai-trace/dense32_validmb \
  --comm-group-configuration=/root/traces/tai-trace/dense32_validmb.json \
  --system-configuration=/app/astra-sim/examples/system/native_collectives/Ring_4chunks.json \
  --remote-memory-configuration=/app/astra-sim/examples/remote_memory/analytical/no_memory_expansion.json \
  --network-configuration=/app/astra-sim/extern/network_backend/ns-3/scratch/config/config_ring32.txt \
  --logical-topology-configuration=/root/traces/tai-trace/logical_topology.json
~~~

For a background run with a saved log:

~~~bash
nohup ./ns3.42-AstraSimNetwork-default \
  --workload-configuration=/root/traces/tai-trace/dense32_validmb \
  --comm-group-configuration=/root/traces/tai-trace/dense32_validmb.json \
  --system-configuration=/app/astra-sim/examples/system/native_collectives/Ring_4chunks.json \
  --remote-memory-configuration=/app/astra-sim/examples/remote_memory/analytical/no_memory_expansion.json \
  --network-configuration=/app/astra-sim/extern/network_backend/ns-3/scratch/config/config_ring32.txt \
  --logical-topology-configuration=/root/traces/tai-trace/logical_topology.json \
  > /root/runs/ring32/ring32.log 2>&1 &
echo $!
~~~

Monitor it with:

~~~bash
pgrep -af 'AstraSimNetwork|ns3'
tail -f /root/runs/ring32/ring32.log
~~~

If only “Unable to open file” appears, check every command-line path and every path in config_ring32.txt from inside the container.

## Output files

Outputs are written under astra-sim/extern/network_backend/ns-3/scratch/output/ (or the equivalent mounted container directory).

| File | Meaning |
| --- | --- |
| fct.txt | One completed flow per line: source destination sport dport size start_ns fct_ns standalone_ns. fct_ns is observed completion; standalone_ns is the no-contention estimate. |
| flow.txt | Static flow metadata. The first line is the flow count used by the analyzer. |
| trace.txt | Node IDs selected for binary packet tracing. |
| mix.tr | Binary packet events: enqueue, dequeue, receive, and drop, preceded by trace settings. It is not text. |
| qlen.txt | Periodic queue-occupancy samples. It is not a per-packet waiting-time file. |
| pfc.txt | Priority-flow-control events; empty means none were recorded. |
| ring32.log | Simulator stdout/stderr. ASTRA completion lines look like sys[0] finished, ... cycles. |

For this configuration one cycle is 1 ns (1 GHz clock and one-cycle period). Verify the clock before converting cycles for a different system JSON.

## Analyze results

From the repository root:

~~~bash
python3 scripts/analyze_ns3_results.py \
  astra-sim/extern/network_backend/ns-3/scratch/output \
  --log /root/runs/ring32/ring32.log \
  -o results/ring32_report.md
~~~

The analyzer reports total flow count, ASTRA workload completion cycles (when --log is supplied), median/p95/maximum FCT, FCT by message size, standalone slowdown, queue occupancy, packet events and utilization, PFC events, and packet queueing duration reconstructed by matching enqueue/dequeue records in mix.tr.

The report calls interface utilization observed because it covers only nodes selected by trace.txt. It calls the maximum fct.txt end time a network-flow completion proxy. The authoritative total workload completion is the maximum ASTRA sys[...] finished cycle in the log. Packet queueing duration can have unmatched events when tracing begins or ends mid-flow.

## Reference values from the recorded run

These are sanity-check values for the exact workload, topology, and settings above.

| Metric | Value |
| --- | --- |
| ASTRA ranks | 32 |
| Completed flows | 50,176 |
| Total workload completion | 491,351,929 cycles, about 491.352 ms |
| Median FCT | 152,862 ns |
| p95 FCT | 386,410 ns |
| Maximum FCT | 5,521,517 ns |
| Median FCT/standalone | 1.338x |
| Maximum FCT/standalone | about 6.989x |
| Maximum network-flow end | 491,351,918 ns |
| Maximum sampled queue | about 326.79 KiB |
| Packet queueing duration | median 0 ns, p95 290 ns, maximum 331 ns |
| PFC events | 0 |

The 2,048,000-byte group is the main high-latency group: median FCT about 5.504 ms versus about 0.790 ms standalone (roughly 6.97x slowdown).

## Troubleshooting

- **Unable to open file:** a required input or output path is missing in the runtime environment.
- **Cannot open topology file:** verify the absolute TOPOLOGY_FILE path and that the file exists inside the container.
- **At least one NIC is alive:** use the supplied host-plus-switch topology and ensure every host has a link.
- **Long runtime:** workload execution plus qlen.txt and mix.tr I/O can be expensive. For exploratory runs, reduce tracing or set QLEN_MON_FILE to /dev/null; retain full tracing for final measurements.
- **Only a few utilization interfaces:** expand trace.txt. The recorded five-node file intentionally traces only a subset.

## Reproduction checklist

1. Confirm 32 rank trace files and rank IDs 0--31 in the communication JSON.
2. Confirm logical dimensions multiply to 32.
3. Confirm all paths in config_ring32.txt exist inside the container.
4. Confirm physical topology header 64 32 64 and host links 0--31 to switches 32--63.
5. Create the output directory.
6. Save the simulator log so completion in ASTRA cycles is available.
7. Run scripts/analyze_ns3_results.py on the completed output directory.
8. Record workload, system JSON, logical and physical topology, network config, trace-node scope, simulator version, and analyzer command with the report.

