# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/straggler_1_5_torus_random1_uniform/attempts/20261124_200856_820521/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 45,558,377 |
| Fastest rank completion (cycles) | 43,003,489 |
| Maximum exposed communication (cycles) | 45,151,285 |
| Completed network flows | 50,176 |
| Total bytes sent | 9,525,264,384 |
| Network-flow finish proxy | 45.538 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 40.267% | 40.264% | 40.267% | 32 |
| Average memory utilization (%) | 83.379% | 83.379% | 83.382% | 32 |
| Average operation intensity | 3,183.480 | 3,182.966 | 3,183.497 | 32 |
| Comm time | 44,130,606.812 | 42,895,381.000 | 45,450,269.000 | 32 |
| Compute bound percentage (%) | 26.074% | 26.069% | 26.074% | 32 |
| GPU time | 413,456.125 | 407,092.000 | 610,744.000 | 32 |
| Total compute-communication overlap | 303,658.562 | 298,984.000 | 448,570.000 | 32 |
| Wall time | 44,240,404.375 | 43,003,489.000 | 45,558,377.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 40.264% |
| 0 | Average memory utilization | 83.382% |
| 0 | Average operation intensity | 3,182.966 |
| 0 | Comm time | 44,136,760.000 |
| 0 | Compute bound percentage | 26.069% |
| 0 | GPU time | 610,744.000 |
| 0 | Total compute-communication overlap | 448,570.000 |
| 0 | Wall time | 44,298,934.000 |
| 1 | Average compute utilization | 40.267% |
| 1 | Average memory utilization | 83.379% |
| 1 | Average operation intensity | 3,183.497 |
| 1 | Comm time | 45,045,037.000 |
| 1 | Compute bound percentage | 26.074% |
| 1 | GPU time | 407,092.000 |
| 1 | Total compute-communication overlap | 298,984.000 |
| 1 | Wall time | 45,153,145.000 |
| 2 | Average compute utilization | 40.267% |
| 2 | Average memory utilization | 83.379% |
| 2 | Average operation intensity | 3,183.497 |
| 2 | Comm time | 44,366,889.000 |
| 2 | Compute bound percentage | 26.074% |
| 2 | GPU time | 407,092.000 |
| 2 | Total compute-communication overlap | 298,984.000 |
| 2 | Wall time | 44,474,997.000 |
| 3 | Average compute utilization | 40.267% |
| 3 | Average memory utilization | 83.379% |
| 3 | Average operation intensity | 3,183.497 |
| 3 | Comm time | 43,184,075.000 |
| 3 | Compute bound percentage | 26.074% |
| 3 | GPU time | 407,092.000 |
| 3 | Total compute-communication overlap | 298,984.000 |
| 3 | Wall time | 43,292,183.000 |
| 4 | Average compute utilization | 40.267% |
| 4 | Average memory utilization | 83.379% |
| 4 | Average operation intensity | 3,183.497 |
| 4 | Comm time | 45,450,269.000 |
| 4 | Compute bound percentage | 26.074% |
| 4 | GPU time | 407,092.000 |
| 4 | Total compute-communication overlap | 298,984.000 |
| 4 | Wall time | 45,558,377.000 |
| 5 | Average compute utilization | 40.267% |
| 5 | Average memory utilization | 83.379% |
| 5 | Average operation intensity | 3,183.497 |
| 5 | Comm time | 44,585,265.000 |
| 5 | Compute bound percentage | 26.074% |
| 5 | GPU time | 407,092.000 |
| 5 | Total compute-communication overlap | 298,984.000 |
| 5 | Wall time | 44,693,373.000 |
| 6 | Average compute utilization | 40.267% |
| 6 | Average memory utilization | 83.379% |
| 6 | Average operation intensity | 3,183.497 |
| 6 | Comm time | 42,951,564.000 |
| 6 | Compute bound percentage | 26.074% |
| 6 | GPU time | 407,092.000 |
| 6 | Total compute-communication overlap | 298,984.000 |
| 6 | Wall time | 43,059,672.000 |
| 7 | Average compute utilization | 40.267% |
| 7 | Average memory utilization | 83.379% |
| 7 | Average operation intensity | 3,183.497 |
| 7 | Comm time | 43,687,929.000 |
| 7 | Compute bound percentage | 26.074% |
| 7 | GPU time | 407,092.000 |
| 7 | Total compute-communication overlap | 298,984.000 |
| 7 | Wall time | 43,796,037.000 |
| 8 | Average compute utilization | 40.267% |
| 8 | Average memory utilization | 83.379% |
| 8 | Average operation intensity | 3,183.497 |
| 8 | Comm time | 44,164,243.000 |
| 8 | Compute bound percentage | 26.074% |
| 8 | GPU time | 407,092.000 |
| 8 | Total compute-communication overlap | 298,984.000 |
| 8 | Wall time | 44,272,351.000 |
| 9 | Average compute utilization | 40.267% |
| 9 | Average memory utilization | 83.379% |
| 9 | Average operation intensity | 3,183.497 |
| 9 | Comm time | 45,034,081.000 |
| 9 | Compute bound percentage | 26.074% |
| 9 | GPU time | 407,092.000 |
| 9 | Total compute-communication overlap | 298,984.000 |
| 9 | Wall time | 45,142,189.000 |
| 10 | Average compute utilization | 40.267% |
| 10 | Average memory utilization | 83.379% |
| 10 | Average operation intensity | 3,183.497 |
| 10 | Comm time | 44,420,756.000 |
| 10 | Compute bound percentage | 26.074% |
| 10 | GPU time | 407,092.000 |
| 10 | Total compute-communication overlap | 298,984.000 |
| 10 | Wall time | 44,528,864.000 |
| 11 | Average compute utilization | 40.267% |
| 11 | Average memory utilization | 83.379% |
| 11 | Average operation intensity | 3,183.497 |
| 11 | Comm time | 43,074,542.000 |
| 11 | Compute bound percentage | 26.074% |
| 11 | GPU time | 407,092.000 |
| 11 | Total compute-communication overlap | 298,984.000 |
| 11 | Wall time | 43,182,650.000 |
| 12 | Average compute utilization | 40.267% |
| 12 | Average memory utilization | 83.379% |
| 12 | Average operation intensity | 3,183.497 |
| 12 | Comm time | 45,100,459.000 |
| 12 | Compute bound percentage | 26.074% |
| 12 | GPU time | 407,092.000 |
| 12 | Total compute-communication overlap | 298,984.000 |
| 12 | Wall time | 45,208,567.000 |
| 13 | Average compute utilization | 40.267% |
| 13 | Average memory utilization | 83.379% |
| 13 | Average operation intensity | 3,183.497 |
| 13 | Comm time | 44,551,135.000 |
| 13 | Compute bound percentage | 26.074% |
| 13 | GPU time | 407,092.000 |
| 13 | Total compute-communication overlap | 298,984.000 |
| 13 | Wall time | 44,659,243.000 |
| 14 | Average compute utilization | 40.267% |
| 14 | Average memory utilization | 83.379% |
| 14 | Average operation intensity | 3,183.497 |
| 14 | Comm time | 42,931,903.000 |
| 14 | Compute bound percentage | 26.074% |
| 14 | GPU time | 407,092.000 |
| 14 | Total compute-communication overlap | 298,984.000 |
| 14 | Wall time | 43,040,011.000 |
| 15 | Average compute utilization | 40.267% |
| 15 | Average memory utilization | 83.379% |
| 15 | Average operation intensity | 3,183.497 |
| 15 | Comm time | 43,561,476.000 |
| 15 | Compute bound percentage | 26.074% |
| 15 | GPU time | 407,092.000 |
| 15 | Total compute-communication overlap | 298,984.000 |
| 15 | Wall time | 43,669,584.000 |
| 16 | Average compute utilization | 40.267% |
| 16 | Average memory utilization | 83.379% |
| 16 | Average operation intensity | 3,183.497 |
| 16 | Comm time | 44,302,646.000 |
| 16 | Compute bound percentage | 26.074% |
| 16 | GPU time | 407,092.000 |
| 16 | Total compute-communication overlap | 298,984.000 |
| 16 | Wall time | 44,410,754.000 |
| 17 | Average compute utilization | 40.267% |
| 17 | Average memory utilization | 83.379% |
| 17 | Average operation intensity | 3,183.497 |
| 17 | Comm time | 44,600,517.000 |
| 17 | Compute bound percentage | 26.074% |
| 17 | GPU time | 407,092.000 |
| 17 | Total compute-communication overlap | 298,984.000 |
| 17 | Wall time | 44,708,625.000 |
| 18 | Average compute utilization | 40.267% |
| 18 | Average memory utilization | 83.379% |
| 18 | Average operation intensity | 3,183.497 |
| 18 | Comm time | 44,154,941.000 |
| 18 | Compute bound percentage | 26.074% |
| 18 | GPU time | 407,092.000 |
| 18 | Total compute-communication overlap | 298,984.000 |
| 18 | Wall time | 44,263,049.000 |
| 19 | Average compute utilization | 40.267% |
| 19 | Average memory utilization | 83.379% |
| 19 | Average operation intensity | 3,183.497 |
| 19 | Comm time | 43,191,068.000 |
| 19 | Compute bound percentage | 26.074% |
| 19 | GPU time | 407,092.000 |
| 19 | Total compute-communication overlap | 298,984.000 |
| 19 | Wall time | 43,299,176.000 |
| 20 | Average compute utilization | 40.267% |
| 20 | Average memory utilization | 83.379% |
| 20 | Average operation intensity | 3,183.497 |
| 20 | Comm time | 45,249,507.000 |
| 20 | Compute bound percentage | 26.074% |
| 20 | GPU time | 407,092.000 |
| 20 | Total compute-communication overlap | 298,984.000 |
| 20 | Wall time | 45,357,615.000 |
| 21 | Average compute utilization | 40.267% |
| 21 | Average memory utilization | 83.379% |
| 21 | Average operation intensity | 3,183.497 |
| 21 | Comm time | 44,627,561.000 |
| 21 | Compute bound percentage | 26.074% |
| 21 | GPU time | 407,092.000 |
| 21 | Total compute-communication overlap | 298,984.000 |
| 21 | Wall time | 44,735,669.000 |
| 22 | Average compute utilization | 40.267% |
| 22 | Average memory utilization | 83.379% |
| 22 | Average operation intensity | 3,183.497 |
| 22 | Comm time | 42,895,381.000 |
| 22 | Compute bound percentage | 26.074% |
| 22 | GPU time | 407,092.000 |
| 22 | Total compute-communication overlap | 298,984.000 |
| 22 | Wall time | 43,003,489.000 |
| 23 | Average compute utilization | 40.267% |
| 23 | Average memory utilization | 83.379% |
| 23 | Average operation intensity | 3,183.497 |
| 23 | Comm time | 43,704,178.000 |
| 23 | Compute bound percentage | 26.074% |
| 23 | GPU time | 407,092.000 |
| 23 | Total compute-communication overlap | 298,984.000 |
| 23 | Wall time | 43,812,286.000 |
| 24 | Average compute utilization | 40.267% |
| 24 | Average memory utilization | 83.379% |
| 24 | Average operation intensity | 3,183.497 |
| 24 | Comm time | 44,037,825.000 |
| 24 | Compute bound percentage | 26.074% |
| 24 | GPU time | 407,092.000 |
| 24 | Total compute-communication overlap | 298,984.000 |
| 24 | Wall time | 44,145,933.000 |
| 25 | Average compute utilization | 40.267% |
| 25 | Average memory utilization | 83.379% |
| 25 | Average operation intensity | 3,183.497 |
| 25 | Comm time | 45,036,616.000 |
| 25 | Compute bound percentage | 26.074% |
| 25 | GPU time | 407,092.000 |
| 25 | Total compute-communication overlap | 298,984.000 |
| 25 | Wall time | 45,144,724.000 |
| 26 | Average compute utilization | 40.267% |
| 26 | Average memory utilization | 83.379% |
| 26 | Average operation intensity | 3,183.497 |
| 26 | Comm time | 44,249,213.000 |
| 26 | Compute bound percentage | 26.074% |
| 26 | GPU time | 407,092.000 |
| 26 | Total compute-communication overlap | 298,984.000 |
| 26 | Wall time | 44,357,321.000 |
| 27 | Average compute utilization | 40.267% |
| 27 | Average memory utilization | 83.379% |
| 27 | Average operation intensity | 3,183.497 |
| 27 | Comm time | 43,069,096.000 |
| 27 | Compute bound percentage | 26.074% |
| 27 | GPU time | 407,092.000 |
| 27 | Total compute-communication overlap | 298,984.000 |
| 27 | Wall time | 43,177,204.000 |
| 28 | Average compute utilization | 40.267% |
| 28 | Average memory utilization | 83.379% |
| 28 | Average operation intensity | 3,183.497 |
| 28 | Comm time | 45,379,840.000 |
| 28 | Compute bound percentage | 26.074% |
| 28 | GPU time | 407,092.000 |
| 28 | Total compute-communication overlap | 298,984.000 |
| 28 | Wall time | 45,487,948.000 |
| 29 | Average compute utilization | 40.267% |
| 29 | Average memory utilization | 83.379% |
| 29 | Average operation intensity | 3,183.497 |
| 29 | Comm time | 44,657,022.000 |
| 29 | Compute bound percentage | 26.074% |
| 29 | GPU time | 407,092.000 |
| 29 | Total compute-communication overlap | 298,984.000 |
| 29 | Wall time | 44,765,130.000 |
| 30 | Average compute utilization | 40.267% |
| 30 | Average memory utilization | 83.379% |
| 30 | Average operation intensity | 3,183.497 |
| 30 | Comm time | 43,032,255.000 |
| 30 | Compute bound percentage | 26.074% |
| 30 | GPU time | 407,092.000 |
| 30 | Total compute-communication overlap | 298,984.000 |
| 30 | Wall time | 43,140,363.000 |
| 31 | Average compute utilization | 40.267% |
| 31 | Average memory utilization | 83.379% |
| 31 | Average operation intensity | 3,183.497 |
| 31 | Comm time | 43,745,369.000 |
| 31 | Compute bound percentage | 26.074% |
| 31 | GPU time | 407,092.000 |
| 31 | Total compute-communication overlap | 298,984.000 |
| 31 | Wall time | 43,853,477.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 25.310 us |
| Median FCT | 9.179 us |
| p95 FCT | 125.989 us |
| Maximum FCT | 822.551 us |
| Median standalone time | 8.099 us |
| Median FCT / standalone | 1.161x |
| p95 FCT / standalone | 2.938x |
| Maximum FCT / standalone | 9.108x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 KiB | 30,720 | 7.673 us | 11.380 us | 61.866 us | 6.574 us | 1.145x |
| 116.00 KiB | 14,336 | 14.611 us | 31.000 us | 73.763 us | 10.179 us | 1.661x |
| 1,000.00 KiB | 3,584 | 101.578 us | 220.955 us | 331.383 us | 48.126 us | 2.354x |
| 1.95 MiB | 1,536 | 228.184 us | 506.386 us | 822.551 us | 91.052 us | 2.788x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 4,235,131 |
| Observed queue interval | 5.900 us to 45.531 ms |
| Observed queue duration | 45.525 ms |
| Maximum sampled queue | 1.33 MiB |
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
| Packet trace interval | 4.751 us to 45.537 ms |
| Maximum sampled packet queue | 1.32 MiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 203.12 KiB |
| Events | Dequ: 77,311,488, Enqu: 75,821,568, Recv: 77,311,488 |
| Bytes by event | Dequ: 38.98 GiB, Enqu: 37.55 GiB, Recv: 38.98 GiB |
| Observed interface utilization | 165 interfaces; mean 22.287%, max 55.918% |
| Matched packet queue durations | 74,256,396 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 3.321 us |
| Maximum packet queue time | 55.006 us |
| Mean packet queue time | 610 ns |
| Unmatched/duplicate dequeues | 3,055,092 |
| Enqueue-key collisions | 1,565,172 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
