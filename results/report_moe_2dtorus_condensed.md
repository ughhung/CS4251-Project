# ASTRA-sim NS-3 Results Report

Result directory: `astra-sim/extern/network_backend/ns-3/scratch/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 337,426,939 |
| Fastest rank completion (cycles) | 337,299,048 |
| Maximum exposed communication (cycles) | 336,204,283 |
| Completed network flows | 335,360 |
| Total bytes sent | 8,175,157,248 |
| Network-flow finish proxy | 337.406 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.379% | 79.379% | 79.379% | 32 |
| Average memory utilization (%) | 62.660% | 62.660% | 62.660% | 32 |
| Average operation intensity | 8,266.835 | 8,266.835 | 8,266.835 | 32 |
| Comm time | 337,218,996.750 | 337,144,049.000 | 337,271,940.000 | 32 |
| Compute bound percentage (%) | 52.882% | 52.882% | 52.882% | 32 |
| GPU time | 1,222,656.000 | 1,222,656.000 | 1,222,656.000 | 32 |
| Total compute-communication overlap | 1,067,657.000 | 1,067,657.000 | 1,067,657.000 | 32 |
| Wall time | 337,373,995.750 | 337,299,048.000 | 337,426,939.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.379% |
| 0 | Average memory utilization | 62.660% |
| 0 | Average operation intensity | 8,266.835 |
| 0 | Comm time | 337,144,049.000 |
| 0 | Compute bound percentage | 52.882% |
| 0 | GPU time | 1,222,656.000 |
| 0 | Total compute-communication overlap | 1,067,657.000 |
| 0 | Wall time | 337,299,048.000 |
| 1 | Average compute utilization | 79.379% |
| 1 | Average memory utilization | 62.660% |
| 1 | Average operation intensity | 8,266.835 |
| 1 | Comm time | 337,144,049.000 |
| 1 | Compute bound percentage | 52.882% |
| 1 | GPU time | 1,222,656.000 |
| 1 | Total compute-communication overlap | 1,067,657.000 |
| 1 | Wall time | 337,299,048.000 |
| 2 | Average compute utilization | 79.379% |
| 2 | Average memory utilization | 62.660% |
| 2 | Average operation intensity | 8,266.835 |
| 2 | Comm time | 337,144,049.000 |
| 2 | Compute bound percentage | 52.882% |
| 2 | GPU time | 1,222,656.000 |
| 2 | Total compute-communication overlap | 1,067,657.000 |
| 2 | Wall time | 337,299,048.000 |
| 3 | Average compute utilization | 79.379% |
| 3 | Average memory utilization | 62.660% |
| 3 | Average operation intensity | 8,266.835 |
| 3 | Comm time | 337,144,049.000 |
| 3 | Compute bound percentage | 52.882% |
| 3 | GPU time | 1,222,656.000 |
| 3 | Total compute-communication overlap | 1,067,657.000 |
| 3 | Wall time | 337,299,048.000 |
| 4 | Average compute utilization | 79.379% |
| 4 | Average memory utilization | 62.660% |
| 4 | Average operation intensity | 8,266.835 |
| 4 | Comm time | 337,174,081.000 |
| 4 | Compute bound percentage | 52.882% |
| 4 | GPU time | 1,222,656.000 |
| 4 | Total compute-communication overlap | 1,067,657.000 |
| 4 | Wall time | 337,329,080.000 |
| 5 | Average compute utilization | 79.379% |
| 5 | Average memory utilization | 62.660% |
| 5 | Average operation intensity | 8,266.835 |
| 5 | Comm time | 337,174,081.000 |
| 5 | Compute bound percentage | 52.882% |
| 5 | GPU time | 1,222,656.000 |
| 5 | Total compute-communication overlap | 1,067,657.000 |
| 5 | Wall time | 337,329,080.000 |
| 6 | Average compute utilization | 79.379% |
| 6 | Average memory utilization | 62.660% |
| 6 | Average operation intensity | 8,266.835 |
| 6 | Comm time | 337,174,081.000 |
| 6 | Compute bound percentage | 52.882% |
| 6 | GPU time | 1,222,656.000 |
| 6 | Total compute-communication overlap | 1,067,657.000 |
| 6 | Wall time | 337,329,080.000 |
| 7 | Average compute utilization | 79.379% |
| 7 | Average memory utilization | 62.660% |
| 7 | Average operation intensity | 8,266.835 |
| 7 | Comm time | 337,174,081.000 |
| 7 | Compute bound percentage | 52.882% |
| 7 | GPU time | 1,222,656.000 |
| 7 | Total compute-communication overlap | 1,067,657.000 |
| 7 | Wall time | 337,329,080.000 |
| 8 | Average compute utilization | 79.379% |
| 8 | Average memory utilization | 62.660% |
| 8 | Average operation intensity | 8,266.835 |
| 8 | Comm time | 337,210,480.000 |
| 8 | Compute bound percentage | 52.882% |
| 8 | GPU time | 1,222,656.000 |
| 8 | Total compute-communication overlap | 1,067,657.000 |
| 8 | Wall time | 337,365,479.000 |
| 9 | Average compute utilization | 79.379% |
| 9 | Average memory utilization | 62.660% |
| 9 | Average operation intensity | 8,266.835 |
| 9 | Comm time | 337,210,480.000 |
| 9 | Compute bound percentage | 52.882% |
| 9 | GPU time | 1,222,656.000 |
| 9 | Total compute-communication overlap | 1,067,657.000 |
| 9 | Wall time | 337,365,479.000 |
| 10 | Average compute utilization | 79.379% |
| 10 | Average memory utilization | 62.660% |
| 10 | Average operation intensity | 8,266.835 |
| 10 | Comm time | 337,210,480.000 |
| 10 | Compute bound percentage | 52.882% |
| 10 | GPU time | 1,222,656.000 |
| 10 | Total compute-communication overlap | 1,067,657.000 |
| 10 | Wall time | 337,365,479.000 |
| 11 | Average compute utilization | 79.379% |
| 11 | Average memory utilization | 62.660% |
| 11 | Average operation intensity | 8,266.835 |
| 11 | Comm time | 337,210,480.000 |
| 11 | Compute bound percentage | 52.882% |
| 11 | GPU time | 1,222,656.000 |
| 11 | Total compute-communication overlap | 1,067,657.000 |
| 11 | Wall time | 337,365,479.000 |
| 12 | Average compute utilization | 79.379% |
| 12 | Average memory utilization | 62.660% |
| 12 | Average operation intensity | 8,266.835 |
| 12 | Comm time | 337,240,512.000 |
| 12 | Compute bound percentage | 52.882% |
| 12 | GPU time | 1,222,656.000 |
| 12 | Total compute-communication overlap | 1,067,657.000 |
| 12 | Wall time | 337,395,511.000 |
| 13 | Average compute utilization | 79.379% |
| 13 | Average memory utilization | 62.660% |
| 13 | Average operation intensity | 8,266.835 |
| 13 | Comm time | 337,240,512.000 |
| 13 | Compute bound percentage | 52.882% |
| 13 | GPU time | 1,222,656.000 |
| 13 | Total compute-communication overlap | 1,067,657.000 |
| 13 | Wall time | 337,395,511.000 |
| 14 | Average compute utilization | 79.379% |
| 14 | Average memory utilization | 62.660% |
| 14 | Average operation intensity | 8,266.835 |
| 14 | Comm time | 337,240,512.000 |
| 14 | Compute bound percentage | 52.882% |
| 14 | GPU time | 1,222,656.000 |
| 14 | Total compute-communication overlap | 1,067,657.000 |
| 14 | Wall time | 337,395,511.000 |
| 15 | Average compute utilization | 79.379% |
| 15 | Average memory utilization | 62.660% |
| 15 | Average operation intensity | 8,266.835 |
| 15 | Comm time | 337,240,512.000 |
| 15 | Compute bound percentage | 52.882% |
| 15 | GPU time | 1,222,656.000 |
| 15 | Total compute-communication overlap | 1,067,657.000 |
| 15 | Wall time | 337,395,511.000 |
| 16 | Average compute utilization | 79.379% |
| 16 | Average memory utilization | 62.660% |
| 16 | Average operation intensity | 8,266.835 |
| 16 | Comm time | 337,219,486.000 |
| 16 | Compute bound percentage | 52.882% |
| 16 | GPU time | 1,222,656.000 |
| 16 | Total compute-communication overlap | 1,067,657.000 |
| 16 | Wall time | 337,374,485.000 |
| 17 | Average compute utilization | 79.379% |
| 17 | Average memory utilization | 62.660% |
| 17 | Average operation intensity | 8,266.835 |
| 17 | Comm time | 337,219,486.000 |
| 17 | Compute bound percentage | 52.882% |
| 17 | GPU time | 1,222,656.000 |
| 17 | Total compute-communication overlap | 1,067,657.000 |
| 17 | Wall time | 337,374,485.000 |
| 18 | Average compute utilization | 79.379% |
| 18 | Average memory utilization | 62.660% |
| 18 | Average operation intensity | 8,266.835 |
| 18 | Comm time | 337,219,486.000 |
| 18 | Compute bound percentage | 52.882% |
| 18 | GPU time | 1,222,656.000 |
| 18 | Total compute-communication overlap | 1,067,657.000 |
| 18 | Wall time | 337,374,485.000 |
| 19 | Average compute utilization | 79.379% |
| 19 | Average memory utilization | 62.660% |
| 19 | Average operation intensity | 8,266.835 |
| 19 | Comm time | 337,219,486.000 |
| 19 | Compute bound percentage | 52.882% |
| 19 | GPU time | 1,222,656.000 |
| 19 | Total compute-communication overlap | 1,067,657.000 |
| 19 | Wall time | 337,374,485.000 |
| 20 | Average compute utilization | 79.379% |
| 20 | Average memory utilization | 62.660% |
| 20 | Average operation intensity | 8,266.835 |
| 20 | Comm time | 337,249,518.000 |
| 20 | Compute bound percentage | 52.882% |
| 20 | GPU time | 1,222,656.000 |
| 20 | Total compute-communication overlap | 1,067,657.000 |
| 20 | Wall time | 337,404,517.000 |
| 21 | Average compute utilization | 79.379% |
| 21 | Average memory utilization | 62.660% |
| 21 | Average operation intensity | 8,266.835 |
| 21 | Comm time | 337,249,518.000 |
| 21 | Compute bound percentage | 52.882% |
| 21 | GPU time | 1,222,656.000 |
| 21 | Total compute-communication overlap | 1,067,657.000 |
| 21 | Wall time | 337,404,517.000 |
| 22 | Average compute utilization | 79.379% |
| 22 | Average memory utilization | 62.660% |
| 22 | Average operation intensity | 8,266.835 |
| 22 | Comm time | 337,249,518.000 |
| 22 | Compute bound percentage | 52.882% |
| 22 | GPU time | 1,222,656.000 |
| 22 | Total compute-communication overlap | 1,067,657.000 |
| 22 | Wall time | 337,404,517.000 |
| 23 | Average compute utilization | 79.379% |
| 23 | Average memory utilization | 62.660% |
| 23 | Average operation intensity | 8,266.835 |
| 23 | Comm time | 337,249,518.000 |
| 23 | Compute bound percentage | 52.882% |
| 23 | GPU time | 1,222,656.000 |
| 23 | Total compute-communication overlap | 1,067,657.000 |
| 23 | Wall time | 337,404,517.000 |
| 24 | Average compute utilization | 79.379% |
| 24 | Average memory utilization | 62.660% |
| 24 | Average operation intensity | 8,266.835 |
| 24 | Comm time | 337,241,908.000 |
| 24 | Compute bound percentage | 52.882% |
| 24 | GPU time | 1,222,656.000 |
| 24 | Total compute-communication overlap | 1,067,657.000 |
| 24 | Wall time | 337,396,907.000 |
| 25 | Average compute utilization | 79.379% |
| 25 | Average memory utilization | 62.660% |
| 25 | Average operation intensity | 8,266.835 |
| 25 | Comm time | 337,241,908.000 |
| 25 | Compute bound percentage | 52.882% |
| 25 | GPU time | 1,222,656.000 |
| 25 | Total compute-communication overlap | 1,067,657.000 |
| 25 | Wall time | 337,396,907.000 |
| 26 | Average compute utilization | 79.379% |
| 26 | Average memory utilization | 62.660% |
| 26 | Average operation intensity | 8,266.835 |
| 26 | Comm time | 337,241,908.000 |
| 26 | Compute bound percentage | 52.882% |
| 26 | GPU time | 1,222,656.000 |
| 26 | Total compute-communication overlap | 1,067,657.000 |
| 26 | Wall time | 337,396,907.000 |
| 27 | Average compute utilization | 79.379% |
| 27 | Average memory utilization | 62.660% |
| 27 | Average operation intensity | 8,266.835 |
| 27 | Comm time | 337,241,908.000 |
| 27 | Compute bound percentage | 52.882% |
| 27 | GPU time | 1,222,656.000 |
| 27 | Total compute-communication overlap | 1,067,657.000 |
| 27 | Wall time | 337,396,907.000 |
| 28 | Average compute utilization | 79.379% |
| 28 | Average memory utilization | 62.660% |
| 28 | Average operation intensity | 8,266.835 |
| 28 | Comm time | 337,271,940.000 |
| 28 | Compute bound percentage | 52.882% |
| 28 | GPU time | 1,222,656.000 |
| 28 | Total compute-communication overlap | 1,067,657.000 |
| 28 | Wall time | 337,426,939.000 |
| 29 | Average compute utilization | 79.379% |
| 29 | Average memory utilization | 62.660% |
| 29 | Average operation intensity | 8,266.835 |
| 29 | Comm time | 337,271,940.000 |
| 29 | Compute bound percentage | 52.882% |
| 29 | GPU time | 1,222,656.000 |
| 29 | Total compute-communication overlap | 1,067,657.000 |
| 29 | Wall time | 337,426,939.000 |
| 30 | Average compute utilization | 79.379% |
| 30 | Average memory utilization | 62.660% |
| 30 | Average operation intensity | 8,266.835 |
| 30 | Comm time | 337,271,940.000 |
| 30 | Compute bound percentage | 52.882% |
| 30 | GPU time | 1,222,656.000 |
| 30 | Total compute-communication overlap | 1,067,657.000 |
| 30 | Wall time | 337,426,939.000 |
| 31 | Average compute utilization | 79.379% |
| 31 | Average memory utilization | 62.660% |
| 31 | Average operation intensity | 8,266.835 |
| 31 | Comm time | 337,271,940.000 |
| 31 | Compute bound percentage | 52.882% |
| 31 | GPU time | 1,222,656.000 |
| 31 | Total compute-communication overlap | 1,067,657.000 |
| 31 | Wall time | 337,426,939.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 32.148 us |
| Median FCT | 30.173 us |
| p95 FCT | 35.463 us |
| Maximum FCT | 346.604 us |
| Median standalone time | 30.207 us |
| Median FCT / standalone | 0.999x |
| p95 FCT / standalone | 0.999x |
| Maximum FCT / standalone | 2.989x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 30.015 us | 30.015 us | 30.046 us | 30.123 us | 0.996x |
| 2.00 KiB | 260,096 | 30.173 us | 30.173 us | 75.374 us | 30.207 us | 0.999x |
| 16.00 KiB | 28,672 | 30.761 us | 30.789 us | 31.380 us | 30.808 us | 0.999x |
| 128.00 KiB | 30,720 | 35.463 us | 39.020 us | 51.575 us | 35.616 us | 1.014x |
| 1.95 MiB | 1,536 | 332.063 us | 336.682 us | 346.604 us | 115.972 us | 2.868x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,758,220 |
| Observed queue interval | 845.800 us to 337.386 ms |
| Observed queue duration | 336.541 ms |
| Maximum sampled queue | 2.25 MiB |
| Maximum queue location | switch 32, port 5 |

The queue interval is the time span covered by non-empty queue records; it is not per-flow queueing duration.

## PFC and flow inputs

| Metric | Result |
| --- | --- |
| PFC events | 0 |
| Static flows declared | 0 |
| Trace nodes listed | 13 |

## Packet trace

| Metric | Result |
| --- | --- |
| Trace records recognized | 108,420,992 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 337.401 ms |
| Maximum sampled packet queue | 2.25 MiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 88 |
| SimSetting window | 1.20 MiB |
| Events | Dequ: 36,582,144, Enqu: 35,256,704, Recv: 36,582,144 |
| Bytes by event | Dequ: 17.85 GiB, Enqu: 16.61 GiB, Recv: 17.85 GiB |
| Observed interface utilization | 61 interfaces; mean 3.725%, max 11.111% |
| Matched packet queue durations | 35,223,927 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 68.392 us |
| Maximum packet queue time | 93.363 us |
| Mean packet queue time | 6.296 us |
| Unmatched/duplicate dequeues | 1,358,217 |
| Enqueue-key collisions | 32,777 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
