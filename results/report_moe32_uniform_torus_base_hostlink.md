# ASTRA-sim NS-3 Results Report

Result directory: `astra-sim/extern/network_backend/ns-3/scratch/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 38,990,860 |
| Fastest rank completion (cycles) | 38,753,406 |
| Maximum exposed communication (cycles) | 37,768,076 |
| Completed network flows | 163,328 |
| Total bytes sent | 7,822,835,712 |
| Network-flow finish proxy | 38.970 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.381% | 79.381% | 79.381% | 32 |
| Average memory utilization (%) | 62.654% | 62.654% | 62.654% | 32 |
| Average operation intensity | 8,454.392 | 8,454.392 | 8,454.392 | 32 |
| Comm time | 38,174,425.781 | 38,106,566.000 | 38,344,020.000 | 32 |
| Compute bound percentage (%) | 52.886% | 52.886% | 52.886% | 32 |
| GPU time | 1,222,784.000 | 1,222,784.000 | 1,222,784.000 | 32 |
| Total compute-communication overlap | 575,944.000 | 575,944.000 | 575,944.000 | 32 |
| Wall time | 38,821,265.781 | 38,753,406.000 | 38,990,860.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.381% |
| 0 | Average memory utilization | 62.654% |
| 0 | Average operation intensity | 8,454.392 |
| 0 | Comm time | 38,283,043.000 |
| 0 | Compute bound percentage | 52.886% |
| 0 | GPU time | 1,222,784.000 |
| 0 | Total compute-communication overlap | 575,944.000 |
| 0 | Wall time | 38,929,883.000 |
| 1 | Average compute utilization | 79.381% |
| 1 | Average memory utilization | 62.654% |
| 1 | Average operation intensity | 8,454.392 |
| 1 | Comm time | 38,287,749.000 |
| 1 | Compute bound percentage | 52.886% |
| 1 | GPU time | 1,222,784.000 |
| 1 | Total compute-communication overlap | 575,944.000 |
| 1 | Wall time | 38,934,589.000 |
| 2 | Average compute utilization | 79.381% |
| 2 | Average memory utilization | 62.654% |
| 2 | Average operation intensity | 8,454.392 |
| 2 | Comm time | 38,284,986.000 |
| 2 | Compute bound percentage | 52.886% |
| 2 | GPU time | 1,222,784.000 |
| 2 | Total compute-communication overlap | 575,944.000 |
| 2 | Wall time | 38,931,826.000 |
| 3 | Average compute utilization | 79.381% |
| 3 | Average memory utilization | 62.654% |
| 3 | Average operation intensity | 8,454.392 |
| 3 | Comm time | 38,284,028.000 |
| 3 | Compute bound percentage | 52.886% |
| 3 | GPU time | 1,222,784.000 |
| 3 | Total compute-communication overlap | 575,944.000 |
| 3 | Wall time | 38,930,868.000 |
| 4 | Average compute utilization | 79.381% |
| 4 | Average memory utilization | 62.654% |
| 4 | Average operation intensity | 8,454.392 |
| 4 | Comm time | 38,331,294.000 |
| 4 | Compute bound percentage | 52.886% |
| 4 | GPU time | 1,222,784.000 |
| 4 | Total compute-communication overlap | 575,944.000 |
| 4 | Wall time | 38,978,134.000 |
| 5 | Average compute utilization | 79.381% |
| 5 | Average memory utilization | 62.654% |
| 5 | Average operation intensity | 8,454.392 |
| 5 | Comm time | 38,302,675.000 |
| 5 | Compute bound percentage | 52.886% |
| 5 | GPU time | 1,222,784.000 |
| 5 | Total compute-communication overlap | 575,944.000 |
| 5 | Wall time | 38,949,515.000 |
| 6 | Average compute utilization | 79.381% |
| 6 | Average memory utilization | 62.654% |
| 6 | Average operation intensity | 8,454.392 |
| 6 | Comm time | 38,320,653.000 |
| 6 | Compute bound percentage | 52.886% |
| 6 | GPU time | 1,222,784.000 |
| 6 | Total compute-communication overlap | 575,944.000 |
| 6 | Wall time | 38,967,493.000 |
| 7 | Average compute utilization | 79.381% |
| 7 | Average memory utilization | 62.654% |
| 7 | Average operation intensity | 8,454.392 |
| 7 | Comm time | 38,344,020.000 |
| 7 | Compute bound percentage | 52.886% |
| 7 | GPU time | 1,222,784.000 |
| 7 | Total compute-communication overlap | 575,944.000 |
| 7 | Wall time | 38,990,860.000 |
| 8 | Average compute utilization | 79.381% |
| 8 | Average memory utilization | 62.654% |
| 8 | Average operation intensity | 8,454.392 |
| 8 | Comm time | 38,109,521.000 |
| 8 | Compute bound percentage | 52.886% |
| 8 | GPU time | 1,222,784.000 |
| 8 | Total compute-communication overlap | 575,944.000 |
| 8 | Wall time | 38,756,361.000 |
| 9 | Average compute utilization | 79.381% |
| 9 | Average memory utilization | 62.654% |
| 9 | Average operation intensity | 8,454.392 |
| 9 | Comm time | 38,108,157.000 |
| 9 | Compute bound percentage | 52.886% |
| 9 | GPU time | 1,222,784.000 |
| 9 | Total compute-communication overlap | 575,944.000 |
| 9 | Wall time | 38,754,997.000 |
| 10 | Average compute utilization | 79.381% |
| 10 | Average memory utilization | 62.654% |
| 10 | Average operation intensity | 8,454.392 |
| 10 | Comm time | 38,108,709.000 |
| 10 | Compute bound percentage | 52.886% |
| 10 | GPU time | 1,222,784.000 |
| 10 | Total compute-communication overlap | 575,944.000 |
| 10 | Wall time | 38,755,549.000 |
| 11 | Average compute utilization | 79.381% |
| 11 | Average memory utilization | 62.654% |
| 11 | Average operation intensity | 8,454.392 |
| 11 | Comm time | 38,108,203.000 |
| 11 | Compute bound percentage | 52.886% |
| 11 | GPU time | 1,222,784.000 |
| 11 | Total compute-communication overlap | 575,944.000 |
| 11 | Wall time | 38,755,043.000 |
| 12 | Average compute utilization | 79.381% |
| 12 | Average memory utilization | 62.654% |
| 12 | Average operation intensity | 8,454.392 |
| 12 | Comm time | 38,108,624.000 |
| 12 | Compute bound percentage | 52.886% |
| 12 | GPU time | 1,222,784.000 |
| 12 | Total compute-communication overlap | 575,944.000 |
| 12 | Wall time | 38,755,464.000 |
| 13 | Average compute utilization | 79.381% |
| 13 | Average memory utilization | 62.654% |
| 13 | Average operation intensity | 8,454.392 |
| 13 | Comm time | 38,108,208.000 |
| 13 | Compute bound percentage | 52.886% |
| 13 | GPU time | 1,222,784.000 |
| 13 | Total compute-communication overlap | 575,944.000 |
| 13 | Wall time | 38,755,048.000 |
| 14 | Average compute utilization | 79.381% |
| 14 | Average memory utilization | 62.654% |
| 14 | Average operation intensity | 8,454.392 |
| 14 | Comm time | 38,107,405.000 |
| 14 | Compute bound percentage | 52.886% |
| 14 | GPU time | 1,222,784.000 |
| 14 | Total compute-communication overlap | 575,944.000 |
| 14 | Wall time | 38,754,245.000 |
| 15 | Average compute utilization | 79.381% |
| 15 | Average memory utilization | 62.654% |
| 15 | Average operation intensity | 8,454.392 |
| 15 | Comm time | 38,106,566.000 |
| 15 | Compute bound percentage | 52.886% |
| 15 | GPU time | 1,222,784.000 |
| 15 | Total compute-communication overlap | 575,944.000 |
| 15 | Wall time | 38,753,406.000 |
| 16 | Average compute utilization | 79.381% |
| 16 | Average memory utilization | 62.654% |
| 16 | Average operation intensity | 8,454.392 |
| 16 | Comm time | 38,127,255.000 |
| 16 | Compute bound percentage | 52.886% |
| 16 | GPU time | 1,222,784.000 |
| 16 | Total compute-communication overlap | 575,944.000 |
| 16 | Wall time | 38,774,095.000 |
| 17 | Average compute utilization | 79.381% |
| 17 | Average memory utilization | 62.654% |
| 17 | Average operation intensity | 8,454.392 |
| 17 | Comm time | 38,127,652.000 |
| 17 | Compute bound percentage | 52.886% |
| 17 | GPU time | 1,222,784.000 |
| 17 | Total compute-communication overlap | 575,944.000 |
| 17 | Wall time | 38,774,492.000 |
| 18 | Average compute utilization | 79.381% |
| 18 | Average memory utilization | 62.654% |
| 18 | Average operation intensity | 8,454.392 |
| 18 | Comm time | 38,128,279.000 |
| 18 | Compute bound percentage | 52.886% |
| 18 | GPU time | 1,222,784.000 |
| 18 | Total compute-communication overlap | 575,944.000 |
| 18 | Wall time | 38,775,119.000 |
| 19 | Average compute utilization | 79.381% |
| 19 | Average memory utilization | 62.654% |
| 19 | Average operation intensity | 8,454.392 |
| 19 | Comm time | 38,126,712.000 |
| 19 | Compute bound percentage | 52.886% |
| 19 | GPU time | 1,222,784.000 |
| 19 | Total compute-communication overlap | 575,944.000 |
| 19 | Wall time | 38,773,552.000 |
| 20 | Average compute utilization | 79.381% |
| 20 | Average memory utilization | 62.654% |
| 20 | Average operation intensity | 8,454.392 |
| 20 | Comm time | 38,130,514.000 |
| 20 | Compute bound percentage | 52.886% |
| 20 | GPU time | 1,222,784.000 |
| 20 | Total compute-communication overlap | 575,944.000 |
| 20 | Wall time | 38,777,354.000 |
| 21 | Average compute utilization | 79.381% |
| 21 | Average memory utilization | 62.654% |
| 21 | Average operation intensity | 8,454.392 |
| 21 | Comm time | 38,130,083.000 |
| 21 | Compute bound percentage | 52.886% |
| 21 | GPU time | 1,222,784.000 |
| 21 | Total compute-communication overlap | 575,944.000 |
| 21 | Wall time | 38,776,923.000 |
| 22 | Average compute utilization | 79.381% |
| 22 | Average memory utilization | 62.654% |
| 22 | Average operation intensity | 8,454.392 |
| 22 | Comm time | 38,131,314.000 |
| 22 | Compute bound percentage | 52.886% |
| 22 | GPU time | 1,222,784.000 |
| 22 | Total compute-communication overlap | 575,944.000 |
| 22 | Wall time | 38,778,154.000 |
| 23 | Average compute utilization | 79.381% |
| 23 | Average memory utilization | 62.654% |
| 23 | Average operation intensity | 8,454.392 |
| 23 | Comm time | 38,131,856.000 |
| 23 | Compute bound percentage | 52.886% |
| 23 | GPU time | 1,222,784.000 |
| 23 | Total compute-communication overlap | 575,944.000 |
| 23 | Wall time | 38,778,696.000 |
| 24 | Average compute utilization | 79.381% |
| 24 | Average memory utilization | 62.654% |
| 24 | Average operation intensity | 8,454.392 |
| 24 | Comm time | 38,163,467.000 |
| 24 | Compute bound percentage | 52.886% |
| 24 | GPU time | 1,222,784.000 |
| 24 | Total compute-communication overlap | 575,944.000 |
| 24 | Wall time | 38,810,307.000 |
| 25 | Average compute utilization | 79.381% |
| 25 | Average memory utilization | 62.654% |
| 25 | Average operation intensity | 8,454.392 |
| 25 | Comm time | 38,157,722.000 |
| 25 | Compute bound percentage | 52.886% |
| 25 | GPU time | 1,222,784.000 |
| 25 | Total compute-communication overlap | 575,944.000 |
| 25 | Wall time | 38,804,562.000 |
| 26 | Average compute utilization | 79.381% |
| 26 | Average memory utilization | 62.654% |
| 26 | Average operation intensity | 8,454.392 |
| 26 | Comm time | 38,157,523.000 |
| 26 | Compute bound percentage | 52.886% |
| 26 | GPU time | 1,222,784.000 |
| 26 | Total compute-communication overlap | 575,944.000 |
| 26 | Wall time | 38,804,363.000 |
| 27 | Average compute utilization | 79.381% |
| 27 | Average memory utilization | 62.654% |
| 27 | Average operation intensity | 8,454.392 |
| 27 | Comm time | 38,161,265.000 |
| 27 | Compute bound percentage | 52.886% |
| 27 | GPU time | 1,222,784.000 |
| 27 | Total compute-communication overlap | 575,944.000 |
| 27 | Wall time | 38,808,105.000 |
| 28 | Average compute utilization | 79.381% |
| 28 | Average memory utilization | 62.654% |
| 28 | Average operation intensity | 8,454.392 |
| 28 | Comm time | 38,153,399.000 |
| 28 | Compute bound percentage | 52.886% |
| 28 | GPU time | 1,222,784.000 |
| 28 | Total compute-communication overlap | 575,944.000 |
| 28 | Wall time | 38,800,239.000 |
| 29 | Average compute utilization | 79.381% |
| 29 | Average memory utilization | 62.654% |
| 29 | Average operation intensity | 8,454.392 |
| 29 | Comm time | 38,149,095.000 |
| 29 | Compute bound percentage | 52.886% |
| 29 | GPU time | 1,222,784.000 |
| 29 | Total compute-communication overlap | 575,944.000 |
| 29 | Wall time | 38,795,935.000 |
| 30 | Average compute utilization | 79.381% |
| 30 | Average memory utilization | 62.654% |
| 30 | Average operation intensity | 8,454.392 |
| 30 | Comm time | 38,149,887.000 |
| 30 | Compute bound percentage | 52.886% |
| 30 | GPU time | 1,222,784.000 |
| 30 | Total compute-communication overlap | 575,944.000 |
| 30 | Wall time | 38,796,727.000 |
| 31 | Average compute utilization | 79.381% |
| 31 | Average memory utilization | 62.654% |
| 31 | Average operation intensity | 8,454.392 |
| 31 | Comm time | 38,151,761.000 |
| 31 | Compute bound percentage | 52.886% |
| 31 | GPU time | 1,222,784.000 |
| 31 | Total compute-communication overlap | 575,944.000 |
| 31 | Wall time | 38,798,601.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 5.871 us |
| Median FCT | 5.039 us |
| p95 FCT | 12.178 us |
| Maximum FCT | 306.045 us |
| Median standalone time | 4.932 us |
| Median FCT / standalone | 1.018x |
| p95 FCT / standalone | 1.485x |
| Maximum FCT / standalone | 3.519x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 4.149 us | 5.039 us | 5.146 us | 4.247 us | 0.952x |
| 2.00 KiB | 88,064 | 2.255 us | 6.392 us | 6.799 us | 2.251 us | 1.024x |
| 16.00 KiB | 28,672 | 5.955 us | 7.061 us | 10.136 us | 4.932 us | 1.079x |
| 128.00 KiB | 30,720 | 8.302 us | 19.808 us | 24.666 us | 6.620 us | 1.386x |
| 1.95 MiB | 1,536 | 89.363 us | 139.710 us | 306.045 us | 86.976 us | 1.130x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,343,749 |
| Observed queue interval | 128.100 us to 38.969 ms |
| Observed queue duration | 38.841 ms |
| Maximum sampled queue | 101.97 KiB |
| Maximum queue location | switch 38, port 2 |

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
| Trace records recognized | 136,747,136 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 38.970 ms |
| Maximum sampled packet queue | 101.97 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 154.39 KiB |
| Events | Dequ: 45,997,312, Enqu: 44,752,512, Recv: 45,997,312 |
| Bytes by event | Dequ: 22.68 GiB, Enqu: 21.50 GiB, Recv: 22.68 GiB |
| Observed interface utilization | 165 interfaces; mean 15.147%, max 29.042% |
| Matched packet queue durations | 44,439,755 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 44 ns |
| Maximum packet queue time | 4.096 us |
| Mean packet queue time | 19 ns |
| Unmatched/duplicate dequeues | 1,557,557 |
| Enqueue-key collisions | 312,757 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
