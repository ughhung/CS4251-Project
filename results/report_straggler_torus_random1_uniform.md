# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/straggler_torus_random1_uniform/attempts/20261124_200856_820521/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 50,280,553 |
| Fastest rank completion (cycles) | 48,071,599 |
| Maximum exposed communication (cycles) | 49,873,461 |
| Completed network flows | 50,176 |
| Total bytes sent | 9,525,264,384 |
| Network-flow finish proxy | 50.260 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 40.267% | 40.261% | 40.267% | 32 |
| Average memory utilization (%) | 83.379% | 83.379% | 83.384% | 32 |
| Average operation intensity | 3,183.455 | 3,182.148 | 3,183.497 | 32 |
| Comm time | 48,995,169.094 | 47,963,491.000 | 50,172,445.000 | 32 |
| Compute bound percentage (%) | 26.074% | 26.069% | 26.074% | 32 |
| GPU time | 521,652.875 | 407,092.000 | 4,073,040.000 | 32 |
| Total compute-communication overlap | 376,901.500 | 298,984.000 | 2,792,344.000 | 32 |
| Wall time | 49,139,920.469 | 48,071,599.000 | 50,280,553.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 40.261% |
| 0 | Average memory utilization | 83.384% |
| 0 | Average operation intensity | 3,182.148 |
| 0 | Comm time | 48,829,078.000 |
| 0 | Compute bound percentage | 26.069% |
| 0 | GPU time | 4,073,040.000 |
| 0 | Total compute-communication overlap | 2,792,344.000 |
| 0 | Wall time | 50,109,774.000 |
| 1 | Average compute utilization | 40.267% |
| 1 | Average memory utilization | 83.379% |
| 1 | Average operation intensity | 3,183.497 |
| 1 | Comm time | 49,965,713.000 |
| 1 | Compute bound percentage | 26.074% |
| 1 | GPU time | 407,092.000 |
| 1 | Total compute-communication overlap | 298,984.000 |
| 1 | Wall time | 50,073,821.000 |
| 2 | Average compute utilization | 40.267% |
| 2 | Average memory utilization | 83.379% |
| 2 | Average operation intensity | 3,183.497 |
| 2 | Comm time | 49,710,222.000 |
| 2 | Compute bound percentage | 26.074% |
| 2 | GPU time | 407,092.000 |
| 2 | Total compute-communication overlap | 298,984.000 |
| 2 | Wall time | 49,818,330.000 |
| 3 | Average compute utilization | 40.267% |
| 3 | Average memory utilization | 83.379% |
| 3 | Average operation intensity | 3,183.497 |
| 3 | Comm time | 48,285,222.000 |
| 3 | Compute bound percentage | 26.074% |
| 3 | GPU time | 407,092.000 |
| 3 | Total compute-communication overlap | 298,984.000 |
| 3 | Wall time | 48,393,330.000 |
| 4 | Average compute utilization | 40.267% |
| 4 | Average memory utilization | 83.379% |
| 4 | Average operation intensity | 3,183.497 |
| 4 | Comm time | 49,672,418.000 |
| 4 | Compute bound percentage | 26.074% |
| 4 | GPU time | 407,092.000 |
| 4 | Total compute-communication overlap | 298,984.000 |
| 4 | Wall time | 49,780,526.000 |
| 5 | Average compute utilization | 40.267% |
| 5 | Average memory utilization | 83.379% |
| 5 | Average operation intensity | 3,183.497 |
| 5 | Comm time | 48,484,991.000 |
| 5 | Compute bound percentage | 26.074% |
| 5 | GPU time | 407,092.000 |
| 5 | Total compute-communication overlap | 298,984.000 |
| 5 | Wall time | 48,593,099.000 |
| 6 | Average compute utilization | 40.267% |
| 6 | Average memory utilization | 83.379% |
| 6 | Average operation intensity | 3,183.497 |
| 6 | Comm time | 48,161,551.000 |
| 6 | Compute bound percentage | 26.074% |
| 6 | GPU time | 407,092.000 |
| 6 | Total compute-communication overlap | 298,984.000 |
| 6 | Wall time | 48,269,659.000 |
| 7 | Average compute utilization | 40.267% |
| 7 | Average memory utilization | 83.379% |
| 7 | Average operation intensity | 3,183.497 |
| 7 | Comm time | 48,179,612.000 |
| 7 | Compute bound percentage | 26.074% |
| 7 | GPU time | 407,092.000 |
| 7 | Total compute-communication overlap | 298,984.000 |
| 7 | Wall time | 48,287,720.000 |
| 8 | Average compute utilization | 40.267% |
| 8 | Average memory utilization | 83.379% |
| 8 | Average operation intensity | 3,183.497 |
| 8 | Comm time | 49,957,895.000 |
| 8 | Compute bound percentage | 26.074% |
| 8 | GPU time | 407,092.000 |
| 8 | Total compute-communication overlap | 298,984.000 |
| 8 | Wall time | 50,066,003.000 |
| 9 | Average compute utilization | 40.267% |
| 9 | Average memory utilization | 83.379% |
| 9 | Average operation intensity | 3,183.497 |
| 9 | Comm time | 50,105,699.000 |
| 9 | Compute bound percentage | 26.074% |
| 9 | GPU time | 407,092.000 |
| 9 | Total compute-communication overlap | 298,984.000 |
| 9 | Wall time | 50,213,807.000 |
| 10 | Average compute utilization | 40.267% |
| 10 | Average memory utilization | 83.379% |
| 10 | Average operation intensity | 3,183.497 |
| 10 | Comm time | 49,347,184.000 |
| 10 | Compute bound percentage | 26.074% |
| 10 | GPU time | 407,092.000 |
| 10 | Total compute-communication overlap | 298,984.000 |
| 10 | Wall time | 49,455,292.000 |
| 11 | Average compute utilization | 40.267% |
| 11 | Average memory utilization | 83.379% |
| 11 | Average operation intensity | 3,183.497 |
| 11 | Comm time | 48,354,963.000 |
| 11 | Compute bound percentage | 26.074% |
| 11 | GPU time | 407,092.000 |
| 11 | Total compute-communication overlap | 298,984.000 |
| 11 | Wall time | 48,463,071.000 |
| 12 | Average compute utilization | 40.267% |
| 12 | Average memory utilization | 83.379% |
| 12 | Average operation intensity | 3,183.497 |
| 12 | Comm time | 49,767,059.000 |
| 12 | Compute bound percentage | 26.074% |
| 12 | GPU time | 407,092.000 |
| 12 | Total compute-communication overlap | 298,984.000 |
| 12 | Wall time | 49,875,167.000 |
| 13 | Average compute utilization | 40.267% |
| 13 | Average memory utilization | 83.379% |
| 13 | Average operation intensity | 3,183.497 |
| 13 | Comm time | 48,527,550.000 |
| 13 | Compute bound percentage | 26.074% |
| 13 | GPU time | 407,092.000 |
| 13 | Total compute-communication overlap | 298,984.000 |
| 13 | Wall time | 48,635,658.000 |
| 14 | Average compute utilization | 40.267% |
| 14 | Average memory utilization | 83.379% |
| 14 | Average operation intensity | 3,183.497 |
| 14 | Comm time | 48,107,664.000 |
| 14 | Compute bound percentage | 26.074% |
| 14 | GPU time | 407,092.000 |
| 14 | Total compute-communication overlap | 298,984.000 |
| 14 | Wall time | 48,215,772.000 |
| 15 | Average compute utilization | 40.267% |
| 15 | Average memory utilization | 83.379% |
| 15 | Average operation intensity | 3,183.497 |
| 15 | Comm time | 48,426,930.000 |
| 15 | Compute bound percentage | 26.074% |
| 15 | GPU time | 407,092.000 |
| 15 | Total compute-communication overlap | 298,984.000 |
| 15 | Wall time | 48,535,038.000 |
| 16 | Average compute utilization | 40.267% |
| 16 | Average memory utilization | 83.379% |
| 16 | Average operation intensity | 3,183.497 |
| 16 | Comm time | 50,025,970.000 |
| 16 | Compute bound percentage | 26.074% |
| 16 | GPU time | 407,092.000 |
| 16 | Total compute-communication overlap | 298,984.000 |
| 16 | Wall time | 50,134,078.000 |
| 17 | Average compute utilization | 40.267% |
| 17 | Average memory utilization | 83.379% |
| 17 | Average operation intensity | 3,183.497 |
| 17 | Comm time | 50,172,445.000 |
| 17 | Compute bound percentage | 26.074% |
| 17 | GPU time | 407,092.000 |
| 17 | Total compute-communication overlap | 298,984.000 |
| 17 | Wall time | 50,280,553.000 |
| 18 | Average compute utilization | 40.267% |
| 18 | Average memory utilization | 83.379% |
| 18 | Average operation intensity | 3,183.497 |
| 18 | Comm time | 49,520,882.000 |
| 18 | Compute bound percentage | 26.074% |
| 18 | GPU time | 407,092.000 |
| 18 | Total compute-communication overlap | 298,984.000 |
| 18 | Wall time | 49,628,990.000 |
| 19 | Average compute utilization | 40.267% |
| 19 | Average memory utilization | 83.379% |
| 19 | Average operation intensity | 3,183.497 |
| 19 | Comm time | 48,135,785.000 |
| 19 | Compute bound percentage | 26.074% |
| 19 | GPU time | 407,092.000 |
| 19 | Total compute-communication overlap | 298,984.000 |
| 19 | Wall time | 48,243,893.000 |
| 20 | Average compute utilization | 40.267% |
| 20 | Average memory utilization | 83.379% |
| 20 | Average operation intensity | 3,183.497 |
| 20 | Comm time | 49,828,244.000 |
| 20 | Compute bound percentage | 26.074% |
| 20 | GPU time | 407,092.000 |
| 20 | Total compute-communication overlap | 298,984.000 |
| 20 | Wall time | 49,936,352.000 |
| 21 | Average compute utilization | 40.267% |
| 21 | Average memory utilization | 83.379% |
| 21 | Average operation intensity | 3,183.497 |
| 21 | Comm time | 48,092,511.000 |
| 21 | Compute bound percentage | 26.074% |
| 21 | GPU time | 407,092.000 |
| 21 | Total compute-communication overlap | 298,984.000 |
| 21 | Wall time | 48,200,619.000 |
| 22 | Average compute utilization | 40.267% |
| 22 | Average memory utilization | 83.379% |
| 22 | Average operation intensity | 3,183.497 |
| 22 | Comm time | 48,049,696.000 |
| 22 | Compute bound percentage | 26.074% |
| 22 | GPU time | 407,092.000 |
| 22 | Total compute-communication overlap | 298,984.000 |
| 22 | Wall time | 48,157,804.000 |
| 23 | Average compute utilization | 40.267% |
| 23 | Average memory utilization | 83.379% |
| 23 | Average operation intensity | 3,183.497 |
| 23 | Comm time | 48,809,802.000 |
| 23 | Compute bound percentage | 26.074% |
| 23 | GPU time | 407,092.000 |
| 23 | Total compute-communication overlap | 298,984.000 |
| 23 | Wall time | 48,917,910.000 |
| 24 | Average compute utilization | 40.267% |
| 24 | Average memory utilization | 83.379% |
| 24 | Average operation intensity | 3,183.497 |
| 24 | Comm time | 49,610,186.000 |
| 24 | Compute bound percentage | 26.074% |
| 24 | GPU time | 407,092.000 |
| 24 | Total compute-communication overlap | 298,984.000 |
| 24 | Wall time | 49,718,294.000 |
| 25 | Average compute utilization | 40.267% |
| 25 | Average memory utilization | 83.379% |
| 25 | Average operation intensity | 3,183.497 |
| 25 | Comm time | 49,976,934.000 |
| 25 | Compute bound percentage | 26.074% |
| 25 | GPU time | 407,092.000 |
| 25 | Total compute-communication overlap | 298,984.000 |
| 25 | Wall time | 50,085,042.000 |
| 26 | Average compute utilization | 40.267% |
| 26 | Average memory utilization | 83.379% |
| 26 | Average operation intensity | 3,183.497 |
| 26 | Comm time | 49,639,482.000 |
| 26 | Compute bound percentage | 26.074% |
| 26 | GPU time | 407,092.000 |
| 26 | Total compute-communication overlap | 298,984.000 |
| 26 | Wall time | 49,747,590.000 |
| 27 | Average compute utilization | 40.267% |
| 27 | Average memory utilization | 83.379% |
| 27 | Average operation intensity | 3,183.497 |
| 27 | Comm time | 48,111,215.000 |
| 27 | Compute bound percentage | 26.074% |
| 27 | GPU time | 407,092.000 |
| 27 | Total compute-communication overlap | 298,984.000 |
| 27 | Wall time | 48,219,323.000 |
| 28 | Average compute utilization | 40.267% |
| 28 | Average memory utilization | 83.379% |
| 28 | Average operation intensity | 3,183.497 |
| 28 | Comm time | 49,597,000.000 |
| 28 | Compute bound percentage | 26.074% |
| 28 | GPU time | 407,092.000 |
| 28 | Total compute-communication overlap | 298,984.000 |
| 28 | Wall time | 49,705,108.000 |
| 29 | Average compute utilization | 40.267% |
| 29 | Average memory utilization | 83.379% |
| 29 | Average operation intensity | 3,183.497 |
| 29 | Comm time | 48,298,870.000 |
| 29 | Compute bound percentage | 26.074% |
| 29 | GPU time | 407,092.000 |
| 29 | Total compute-communication overlap | 298,984.000 |
| 29 | Wall time | 48,406,978.000 |
| 30 | Average compute utilization | 40.267% |
| 30 | Average memory utilization | 83.379% |
| 30 | Average operation intensity | 3,183.497 |
| 30 | Comm time | 47,963,491.000 |
| 30 | Compute bound percentage | 26.074% |
| 30 | GPU time | 407,092.000 |
| 30 | Total compute-communication overlap | 298,984.000 |
| 30 | Wall time | 48,071,599.000 |
| 31 | Average compute utilization | 40.267% |
| 31 | Average memory utilization | 83.379% |
| 31 | Average operation intensity | 3,183.497 |
| 31 | Comm time | 48,129,147.000 |
| 31 | Compute bound percentage | 26.074% |
| 31 | GPU time | 407,092.000 |
| 31 | Total compute-communication overlap | 298,984.000 |
| 31 | Wall time | 48,237,255.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 26.245 us |
| Median FCT | 9.152 us |
| p95 FCT | 134.064 us |
| Maximum FCT | 801.108 us |
| Median standalone time | 8.099 us |
| Median FCT / standalone | 1.149x |
| p95 FCT / standalone | 3.246x |
| Maximum FCT / standalone | 9.916x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 KiB | 30,720 | 7.651 us | 11.308 us | 44.390 us | 6.574 us | 1.143x |
| 116.00 KiB | 14,336 | 14.092 us | 34.316 us | 55.284 us | 10.179 us | 1.710x |
| 1,000.00 KiB | 3,584 | 102.174 us | 252.526 us | 487.548 us | 48.126 us | 2.513x |
| 1.95 MiB | 1,536 | 249.017 us | 499.216 us | 801.108 us | 91.052 us | 2.888x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 4,128,769 |
| Observed queue interval | 5.900 us to 50.256 ms |
| Observed queue duration | 50.250 ms |
| Maximum sampled queue | 1.22 MiB |
| Maximum queue location | switch 32, port 4 |

The queue interval is the time span covered by non-empty queue records; it is not per-flow queueing duration.

## PFC and flow inputs

| Metric | Result |
| --- | --- |
| PFC events | 0 |
| Static flows declared | 0 |
| Trace nodes listed | 37 |

## Packet trace

| Metric | Result |
| --- | --- |
| Trace records recognized | 230,444,544 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 4.751 us to 50.260 ms |
| Maximum sampled packet queue | 1.22 MiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 203.12 KiB |
| Events | Dequ: 77,311,488, Enqu: 75,821,568, Recv: 77,311,488 |
| Bytes by event | Dequ: 38.98 GiB, Enqu: 37.55 GiB, Recv: 38.98 GiB |
| Observed interface utilization | 165 interfaces; mean 20.193%, max 50.664% |
| Matched packet queue durations | 74,335,630 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 3.302 us |
| Maximum packet queue time | 50.672 us |
| Mean packet queue time | 642 ns |
| Unmatched/duplicate dequeues | 2,975,858 |
| Enqueue-key collisions | 1,485,938 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
