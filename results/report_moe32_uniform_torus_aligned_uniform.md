# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_uniform_torus_aligned_uniform/attempts/20261124_172909_977059/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 43,070,866 |
| Fastest rank completion (cycles) | 43,009,713 |
| Maximum exposed communication (cycles) | 41,848,082 |
| Completed network flows | 163,328 |
| Total bytes sent | 7,822,835,712 |
| Network-flow finish proxy | 43.050 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.381% | 79.381% | 79.381% | 32 |
| Average memory utilization (%) | 62.654% | 62.654% | 62.654% | 32 |
| Average operation intensity | 8,454.392 | 8,454.392 | 8,454.392 | 32 |
| Comm time | 42,395,835.625 | 42,362,873.000 | 42,424,026.000 | 32 |
| Compute bound percentage (%) | 52.886% | 52.886% | 52.886% | 32 |
| GPU time | 1,222,784.000 | 1,222,784.000 | 1,222,784.000 | 32 |
| Total compute-communication overlap | 575,944.000 | 575,944.000 | 575,944.000 | 32 |
| Wall time | 43,042,675.625 | 43,009,713.000 | 43,070,866.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.381% |
| 0 | Average memory utilization | 62.654% |
| 0 | Average operation intensity | 8,454.392 |
| 0 | Comm time | 42,376,089.000 |
| 0 | Compute bound percentage | 52.886% |
| 0 | GPU time | 1,222,784.000 |
| 0 | Total compute-communication overlap | 575,944.000 |
| 0 | Wall time | 43,022,929.000 |
| 1 | Average compute utilization | 79.381% |
| 1 | Average memory utilization | 62.654% |
| 1 | Average operation intensity | 8,454.392 |
| 1 | Comm time | 42,400,151.000 |
| 1 | Compute bound percentage | 52.886% |
| 1 | GPU time | 1,222,784.000 |
| 1 | Total compute-communication overlap | 575,944.000 |
| 1 | Wall time | 43,046,991.000 |
| 2 | Average compute utilization | 79.381% |
| 2 | Average memory utilization | 62.654% |
| 2 | Average operation intensity | 8,454.392 |
| 2 | Comm time | 42,405,958.000 |
| 2 | Compute bound percentage | 52.886% |
| 2 | GPU time | 1,222,784.000 |
| 2 | Total compute-communication overlap | 575,944.000 |
| 2 | Wall time | 43,052,798.000 |
| 3 | Average compute utilization | 79.381% |
| 3 | Average memory utilization | 62.654% |
| 3 | Average operation intensity | 8,454.392 |
| 3 | Comm time | 42,380,432.000 |
| 3 | Compute bound percentage | 52.886% |
| 3 | GPU time | 1,222,784.000 |
| 3 | Total compute-communication overlap | 575,944.000 |
| 3 | Wall time | 43,027,272.000 |
| 4 | Average compute utilization | 79.381% |
| 4 | Average memory utilization | 62.654% |
| 4 | Average operation intensity | 8,454.392 |
| 4 | Comm time | 42,380,023.000 |
| 4 | Compute bound percentage | 52.886% |
| 4 | GPU time | 1,222,784.000 |
| 4 | Total compute-communication overlap | 575,944.000 |
| 4 | Wall time | 43,026,863.000 |
| 5 | Average compute utilization | 79.381% |
| 5 | Average memory utilization | 62.654% |
| 5 | Average operation intensity | 8,454.392 |
| 5 | Comm time | 42,404,085.000 |
| 5 | Compute bound percentage | 52.886% |
| 5 | GPU time | 1,222,784.000 |
| 5 | Total compute-communication overlap | 575,944.000 |
| 5 | Wall time | 43,050,925.000 |
| 6 | Average compute utilization | 79.381% |
| 6 | Average memory utilization | 62.654% |
| 6 | Average operation intensity | 8,454.392 |
| 6 | Comm time | 42,409,892.000 |
| 6 | Compute bound percentage | 52.886% |
| 6 | GPU time | 1,222,784.000 |
| 6 | Total compute-communication overlap | 575,944.000 |
| 6 | Wall time | 43,056,732.000 |
| 7 | Average compute utilization | 79.381% |
| 7 | Average memory utilization | 62.654% |
| 7 | Average operation intensity | 8,454.392 |
| 7 | Comm time | 42,384,366.000 |
| 7 | Compute bound percentage | 52.886% |
| 7 | GPU time | 1,222,784.000 |
| 7 | Total compute-communication overlap | 575,944.000 |
| 7 | Wall time | 43,031,206.000 |
| 8 | Average compute utilization | 79.381% |
| 8 | Average memory utilization | 62.654% |
| 8 | Average operation intensity | 8,454.392 |
| 8 | Comm time | 42,384,370.000 |
| 8 | Compute bound percentage | 52.886% |
| 8 | GPU time | 1,222,784.000 |
| 8 | Total compute-communication overlap | 575,944.000 |
| 8 | Wall time | 43,031,210.000 |
| 9 | Average compute utilization | 79.381% |
| 9 | Average memory utilization | 62.654% |
| 9 | Average operation intensity | 8,454.392 |
| 9 | Comm time | 42,408,432.000 |
| 9 | Compute bound percentage | 52.886% |
| 9 | GPU time | 1,222,784.000 |
| 9 | Total compute-communication overlap | 575,944.000 |
| 9 | Wall time | 43,055,272.000 |
| 10 | Average compute utilization | 79.381% |
| 10 | Average memory utilization | 62.654% |
| 10 | Average operation intensity | 8,454.392 |
| 10 | Comm time | 42,414,239.000 |
| 10 | Compute bound percentage | 52.886% |
| 10 | GPU time | 1,222,784.000 |
| 10 | Total compute-communication overlap | 575,944.000 |
| 10 | Wall time | 43,061,079.000 |
| 11 | Average compute utilization | 79.381% |
| 11 | Average memory utilization | 62.654% |
| 11 | Average operation intensity | 8,454.392 |
| 11 | Comm time | 42,388,713.000 |
| 11 | Compute bound percentage | 52.886% |
| 11 | GPU time | 1,222,784.000 |
| 11 | Total compute-communication overlap | 575,944.000 |
| 11 | Wall time | 43,035,553.000 |
| 12 | Average compute utilization | 79.381% |
| 12 | Average memory utilization | 62.654% |
| 12 | Average operation intensity | 8,454.392 |
| 12 | Comm time | 42,388,904.000 |
| 12 | Compute bound percentage | 52.886% |
| 12 | GPU time | 1,222,784.000 |
| 12 | Total compute-communication overlap | 575,944.000 |
| 12 | Wall time | 43,035,744.000 |
| 13 | Average compute utilization | 79.381% |
| 13 | Average memory utilization | 62.654% |
| 13 | Average operation intensity | 8,454.392 |
| 13 | Comm time | 42,412,966.000 |
| 13 | Compute bound percentage | 52.886% |
| 13 | GPU time | 1,222,784.000 |
| 13 | Total compute-communication overlap | 575,944.000 |
| 13 | Wall time | 43,059,806.000 |
| 14 | Average compute utilization | 79.381% |
| 14 | Average memory utilization | 62.654% |
| 14 | Average operation intensity | 8,454.392 |
| 14 | Comm time | 42,418,773.000 |
| 14 | Compute bound percentage | 52.886% |
| 14 | GPU time | 1,222,784.000 |
| 14 | Total compute-communication overlap | 575,944.000 |
| 14 | Wall time | 43,065,613.000 |
| 15 | Average compute utilization | 79.381% |
| 15 | Average memory utilization | 62.654% |
| 15 | Average operation intensity | 8,454.392 |
| 15 | Comm time | 42,393,247.000 |
| 15 | Compute bound percentage | 52.886% |
| 15 | GPU time | 1,222,784.000 |
| 15 | Total compute-communication overlap | 575,944.000 |
| 15 | Wall time | 43,040,087.000 |
| 16 | Average compute utilization | 79.381% |
| 16 | Average memory utilization | 62.654% |
| 16 | Average operation intensity | 8,454.392 |
| 16 | Comm time | 42,392,658.000 |
| 16 | Compute bound percentage | 52.886% |
| 16 | GPU time | 1,222,784.000 |
| 16 | Total compute-communication overlap | 575,944.000 |
| 16 | Wall time | 43,039,498.000 |
| 17 | Average compute utilization | 79.381% |
| 17 | Average memory utilization | 62.654% |
| 17 | Average operation intensity | 8,454.392 |
| 17 | Comm time | 42,416,720.000 |
| 17 | Compute bound percentage | 52.886% |
| 17 | GPU time | 1,222,784.000 |
| 17 | Total compute-communication overlap | 575,944.000 |
| 17 | Wall time | 43,063,560.000 |
| 18 | Average compute utilization | 79.381% |
| 18 | Average memory utilization | 62.654% |
| 18 | Average operation intensity | 8,454.392 |
| 18 | Comm time | 42,422,527.000 |
| 18 | Compute bound percentage | 52.886% |
| 18 | GPU time | 1,222,784.000 |
| 18 | Total compute-communication overlap | 575,944.000 |
| 18 | Wall time | 43,069,367.000 |
| 19 | Average compute utilization | 79.381% |
| 19 | Average memory utilization | 62.654% |
| 19 | Average operation intensity | 8,454.392 |
| 19 | Comm time | 42,397,001.000 |
| 19 | Compute bound percentage | 52.886% |
| 19 | GPU time | 1,222,784.000 |
| 19 | Total compute-communication overlap | 575,944.000 |
| 19 | Wall time | 43,043,841.000 |
| 20 | Average compute utilization | 79.381% |
| 20 | Average memory utilization | 62.654% |
| 20 | Average operation intensity | 8,454.392 |
| 20 | Comm time | 42,394,157.000 |
| 20 | Compute bound percentage | 52.886% |
| 20 | GPU time | 1,222,784.000 |
| 20 | Total compute-communication overlap | 575,944.000 |
| 20 | Wall time | 43,040,997.000 |
| 21 | Average compute utilization | 79.381% |
| 21 | Average memory utilization | 62.654% |
| 21 | Average operation intensity | 8,454.392 |
| 21 | Comm time | 42,418,219.000 |
| 21 | Compute bound percentage | 52.886% |
| 21 | GPU time | 1,222,784.000 |
| 21 | Total compute-communication overlap | 575,944.000 |
| 21 | Wall time | 43,065,059.000 |
| 22 | Average compute utilization | 79.381% |
| 22 | Average memory utilization | 62.654% |
| 22 | Average operation intensity | 8,454.392 |
| 22 | Comm time | 42,424,026.000 |
| 22 | Compute bound percentage | 52.886% |
| 22 | GPU time | 1,222,784.000 |
| 22 | Total compute-communication overlap | 575,944.000 |
| 22 | Wall time | 43,070,866.000 |
| 23 | Average compute utilization | 79.381% |
| 23 | Average memory utilization | 62.654% |
| 23 | Average operation intensity | 8,454.392 |
| 23 | Comm time | 42,398,500.000 |
| 23 | Compute bound percentage | 52.886% |
| 23 | GPU time | 1,222,784.000 |
| 23 | Total compute-communication overlap | 575,944.000 |
| 23 | Wall time | 43,045,340.000 |
| 24 | Average compute utilization | 79.381% |
| 24 | Average memory utilization | 62.654% |
| 24 | Average operation intensity | 8,454.392 |
| 24 | Comm time | 42,362,873.000 |
| 24 | Compute bound percentage | 52.886% |
| 24 | GPU time | 1,222,784.000 |
| 24 | Total compute-communication overlap | 575,944.000 |
| 24 | Wall time | 43,009,713.000 |
| 25 | Average compute utilization | 79.381% |
| 25 | Average memory utilization | 62.654% |
| 25 | Average operation intensity | 8,454.392 |
| 25 | Comm time | 42,386,935.000 |
| 25 | Compute bound percentage | 52.886% |
| 25 | GPU time | 1,222,784.000 |
| 25 | Total compute-communication overlap | 575,944.000 |
| 25 | Wall time | 43,033,775.000 |
| 26 | Average compute utilization | 79.381% |
| 26 | Average memory utilization | 62.654% |
| 26 | Average operation intensity | 8,454.392 |
| 26 | Comm time | 42,392,742.000 |
| 26 | Compute bound percentage | 52.886% |
| 26 | GPU time | 1,222,784.000 |
| 26 | Total compute-communication overlap | 575,944.000 |
| 26 | Wall time | 43,039,582.000 |
| 27 | Average compute utilization | 79.381% |
| 27 | Average memory utilization | 62.654% |
| 27 | Average operation intensity | 8,454.392 |
| 27 | Comm time | 42,367,216.000 |
| 27 | Compute bound percentage | 52.886% |
| 27 | GPU time | 1,222,784.000 |
| 27 | Total compute-communication overlap | 575,944.000 |
| 27 | Wall time | 43,014,056.000 |
| 28 | Average compute utilization | 79.381% |
| 28 | Average memory utilization | 62.654% |
| 28 | Average operation intensity | 8,454.392 |
| 28 | Comm time | 42,371,063.000 |
| 28 | Compute bound percentage | 52.886% |
| 28 | GPU time | 1,222,784.000 |
| 28 | Total compute-communication overlap | 575,944.000 |
| 28 | Wall time | 43,017,903.000 |
| 29 | Average compute utilization | 79.381% |
| 29 | Average memory utilization | 62.654% |
| 29 | Average operation intensity | 8,454.392 |
| 29 | Comm time | 42,395,125.000 |
| 29 | Compute bound percentage | 52.886% |
| 29 | GPU time | 1,222,784.000 |
| 29 | Total compute-communication overlap | 575,944.000 |
| 29 | Wall time | 43,041,965.000 |
| 30 | Average compute utilization | 79.381% |
| 30 | Average memory utilization | 62.654% |
| 30 | Average operation intensity | 8,454.392 |
| 30 | Comm time | 42,400,932.000 |
| 30 | Compute bound percentage | 52.886% |
| 30 | GPU time | 1,222,784.000 |
| 30 | Total compute-communication overlap | 575,944.000 |
| 30 | Wall time | 43,047,772.000 |
| 31 | Average compute utilization | 79.381% |
| 31 | Average memory utilization | 62.654% |
| 31 | Average operation intensity | 8,454.392 |
| 31 | Comm time | 42,375,406.000 |
| 31 | Compute bound percentage | 52.886% |
| 31 | GPU time | 1,222,784.000 |
| 31 | Total compute-communication overlap | 575,944.000 |
| 31 | Wall time | 43,022,246.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 6.903 us |
| Median FCT | 4.216 us |
| p95 FCT | 19.939 us |
| Maximum FCT | 330.339 us |
| Median standalone time | 3.808 us |
| Median FCT / standalone | 1.004x |
| p95 FCT / standalone | 2.187x |
| Maximum FCT / standalone | 3.713x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 3.015 us | 3.015 us | 3.015 us | 3.123 us | 0.965x |
| 2.00 KiB | 88,064 | 3.395 us | 6.302 us | 7.203 us | 3.207 us | 1.008x |
| 16.00 KiB | 28,672 | 3.800 us | 6.484 us | 11.340 us | 3.808 us | 1.156x |
| 128.00 KiB | 30,720 | 8.915 us | 24.564 us | 26.548 us | 8.616 us | 1.529x |
| 1.95 MiB | 1,536 | 98.878 us | 256.891 us | 330.339 us | 88.972 us | 1.405x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 956,290 |
| Observed queue interval | 89.200 us to 43.046 ms |
| Observed queue duration | 42.956 ms |
| Maximum sampled queue | 101.99 KiB |
| Maximum queue location | switch 61, port 1 |

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
| Trace records recognized | 103,151,744 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 43.050 ms |
| Maximum sampled packet queue | 101.97 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 203.12 KiB |
| Events | Dequ: 34,798,848, Enqu: 33,554,048, Recv: 34,798,848 |
| Bytes by event | Dequ: 17.21 GiB, Enqu: 16.03 GiB, Recv: 17.21 GiB |
| Observed interface utilization | 165 interfaces; mean 10.407%, max 24.658% |
| Matched packet queue durations | 33,438,560 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 74 ns |
| Maximum packet queue time | 4.096 us |
| Mean packet queue time | 26 ns |
| Unmatched/duplicate dequeues | 1,360,288 |
| Enqueue-key collisions | 115,488 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
