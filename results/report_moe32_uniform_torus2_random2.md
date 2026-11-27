# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_uniform_torus2_random2/attempts/20261126_030556_566401/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 55,105,994 |
| Fastest rank completion (cycles) | 53,347,124 |
| Maximum exposed communication (cycles) | 53,883,210 |
| Completed network flows | 163,328 |
| Total bytes sent | 7,822,835,712 |
| Network-flow finish proxy | 55.086 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.381% | 79.381% | 79.381% | 32 |
| Average memory utilization (%) | 62.654% | 62.654% | 62.654% | 32 |
| Average operation intensity | 8,454.392 | 8,454.392 | 8,454.392 | 32 |
| Comm time | 53,470,305.062 | 52,700,284.000 | 54,459,154.000 | 32 |
| Compute bound percentage (%) | 52.886% | 52.886% | 52.886% | 32 |
| GPU time | 1,222,784.000 | 1,222,784.000 | 1,222,784.000 | 32 |
| Total compute-communication overlap | 573,907.281 | 561,820.000 | 575,944.000 | 32 |
| Wall time | 54,119,181.781 | 53,347,124.000 | 55,105,994.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.381% |
| 0 | Average memory utilization | 62.654% |
| 0 | Average operation intensity | 8,454.392 |
| 0 | Comm time | 53,037,626.000 |
| 0 | Compute bound percentage | 52.886% |
| 0 | GPU time | 1,222,784.000 |
| 0 | Total compute-communication overlap | 575,944.000 |
| 0 | Wall time | 53,684,466.000 |
| 1 | Average compute utilization | 79.381% |
| 1 | Average memory utilization | 62.654% |
| 1 | Average operation intensity | 8,454.392 |
| 1 | Comm time | 53,119,549.000 |
| 1 | Compute bound percentage | 52.886% |
| 1 | GPU time | 1,222,784.000 |
| 1 | Total compute-communication overlap | 570,792.000 |
| 1 | Wall time | 53,771,541.000 |
| 2 | Average compute utilization | 79.381% |
| 2 | Average memory utilization | 62.654% |
| 2 | Average operation intensity | 8,454.392 |
| 2 | Comm time | 53,143,048.000 |
| 2 | Compute bound percentage | 52.886% |
| 2 | GPU time | 1,222,784.000 |
| 2 | Total compute-communication overlap | 575,944.000 |
| 2 | Wall time | 53,789,888.000 |
| 3 | Average compute utilization | 79.381% |
| 3 | Average memory utilization | 62.654% |
| 3 | Average operation intensity | 8,454.392 |
| 3 | Comm time | 53,277,786.000 |
| 3 | Compute bound percentage | 52.886% |
| 3 | GPU time | 1,222,784.000 |
| 3 | Total compute-communication overlap | 575,944.000 |
| 3 | Wall time | 53,924,626.000 |
| 4 | Average compute utilization | 79.381% |
| 4 | Average memory utilization | 62.654% |
| 4 | Average operation intensity | 8,454.392 |
| 4 | Comm time | 54,459,154.000 |
| 4 | Compute bound percentage | 52.886% |
| 4 | GPU time | 1,222,784.000 |
| 4 | Total compute-communication overlap | 575,944.000 |
| 4 | Wall time | 55,105,994.000 |
| 5 | Average compute utilization | 79.381% |
| 5 | Average memory utilization | 62.654% |
| 5 | Average operation intensity | 8,454.392 |
| 5 | Comm time | 54,216,575.000 |
| 5 | Compute bound percentage | 52.886% |
| 5 | GPU time | 1,222,784.000 |
| 5 | Total compute-communication overlap | 561,820.000 |
| 5 | Wall time | 54,877,539.000 |
| 6 | Average compute utilization | 79.381% |
| 6 | Average memory utilization | 62.654% |
| 6 | Average operation intensity | 8,454.392 |
| 6 | Comm time | 54,249,738.000 |
| 6 | Compute bound percentage | 52.886% |
| 6 | GPU time | 1,222,784.000 |
| 6 | Total compute-communication overlap | 561,868.000 |
| 6 | Wall time | 54,910,654.000 |
| 7 | Average compute utilization | 79.381% |
| 7 | Average memory utilization | 62.654% |
| 7 | Average operation intensity | 8,454.392 |
| 7 | Comm time | 54,390,443.000 |
| 7 | Compute bound percentage | 52.886% |
| 7 | GPU time | 1,222,784.000 |
| 7 | Total compute-communication overlap | 575,944.000 |
| 7 | Wall time | 55,037,283.000 |
| 8 | Average compute utilization | 79.381% |
| 8 | Average memory utilization | 62.654% |
| 8 | Average operation intensity | 8,454.392 |
| 8 | Comm time | 53,029,924.000 |
| 8 | Compute bound percentage | 52.886% |
| 8 | GPU time | 1,222,784.000 |
| 8 | Total compute-communication overlap | 575,944.000 |
| 8 | Wall time | 53,676,764.000 |
| 9 | Average compute utilization | 79.381% |
| 9 | Average memory utilization | 62.654% |
| 9 | Average operation intensity | 8,454.392 |
| 9 | Comm time | 53,372,797.000 |
| 9 | Compute bound percentage | 52.886% |
| 9 | GPU time | 1,222,784.000 |
| 9 | Total compute-communication overlap | 575,944.000 |
| 9 | Wall time | 54,019,637.000 |
| 10 | Average compute utilization | 79.381% |
| 10 | Average memory utilization | 62.654% |
| 10 | Average operation intensity | 8,454.392 |
| 10 | Comm time | 53,452,033.000 |
| 10 | Compute bound percentage | 52.886% |
| 10 | GPU time | 1,222,784.000 |
| 10 | Total compute-communication overlap | 575,944.000 |
| 10 | Wall time | 54,098,873.000 |
| 11 | Average compute utilization | 79.381% |
| 11 | Average memory utilization | 62.654% |
| 11 | Average operation intensity | 8,454.392 |
| 11 | Comm time | 53,503,634.000 |
| 11 | Compute bound percentage | 52.886% |
| 11 | GPU time | 1,222,784.000 |
| 11 | Total compute-communication overlap | 575,944.000 |
| 11 | Wall time | 54,150,474.000 |
| 12 | Average compute utilization | 79.381% |
| 12 | Average memory utilization | 62.654% |
| 12 | Average operation intensity | 8,454.392 |
| 12 | Comm time | 53,907,938.000 |
| 12 | Compute bound percentage | 52.886% |
| 12 | GPU time | 1,222,784.000 |
| 12 | Total compute-communication overlap | 575,944.000 |
| 12 | Wall time | 54,554,778.000 |
| 13 | Average compute utilization | 79.381% |
| 13 | Average memory utilization | 62.654% |
| 13 | Average operation intensity | 8,454.392 |
| 13 | Comm time | 54,086,682.000 |
| 13 | Compute bound percentage | 52.886% |
| 13 | GPU time | 1,222,784.000 |
| 13 | Total compute-communication overlap | 571,578.000 |
| 13 | Wall time | 54,737,888.000 |
| 14 | Average compute utilization | 79.381% |
| 14 | Average memory utilization | 62.654% |
| 14 | Average operation intensity | 8,454.392 |
| 14 | Comm time | 54,212,107.000 |
| 14 | Compute bound percentage | 52.886% |
| 14 | GPU time | 1,222,784.000 |
| 14 | Total compute-communication overlap | 575,944.000 |
| 14 | Wall time | 54,858,947.000 |
| 15 | Average compute utilization | 79.381% |
| 15 | Average memory utilization | 62.654% |
| 15 | Average operation intensity | 8,454.392 |
| 15 | Comm time | 53,640,984.000 |
| 15 | Compute bound percentage | 52.886% |
| 15 | GPU time | 1,222,784.000 |
| 15 | Total compute-communication overlap | 575,944.000 |
| 15 | Wall time | 54,287,824.000 |
| 16 | Average compute utilization | 79.381% |
| 16 | Average memory utilization | 62.654% |
| 16 | Average operation intensity | 8,454.392 |
| 16 | Comm time | 53,006,693.000 |
| 16 | Compute bound percentage | 52.886% |
| 16 | GPU time | 1,222,784.000 |
| 16 | Total compute-communication overlap | 575,944.000 |
| 16 | Wall time | 53,653,533.000 |
| 17 | Average compute utilization | 79.381% |
| 17 | Average memory utilization | 62.654% |
| 17 | Average operation intensity | 8,454.392 |
| 17 | Comm time | 53,218,645.000 |
| 17 | Compute bound percentage | 52.886% |
| 17 | GPU time | 1,222,784.000 |
| 17 | Total compute-communication overlap | 575,169.000 |
| 17 | Wall time | 53,866,260.000 |
| 18 | Average compute utilization | 79.381% |
| 18 | Average memory utilization | 62.654% |
| 18 | Average operation intensity | 8,454.392 |
| 18 | Comm time | 53,230,728.000 |
| 18 | Compute bound percentage | 52.886% |
| 18 | GPU time | 1,222,784.000 |
| 18 | Total compute-communication overlap | 575,506.000 |
| 18 | Wall time | 53,878,006.000 |
| 19 | Average compute utilization | 79.381% |
| 19 | Average memory utilization | 62.654% |
| 19 | Average operation intensity | 8,454.392 |
| 19 | Comm time | 52,950,949.000 |
| 19 | Compute bound percentage | 52.886% |
| 19 | GPU time | 1,222,784.000 |
| 19 | Total compute-communication overlap | 575,944.000 |
| 19 | Wall time | 53,597,789.000 |
| 20 | Average compute utilization | 79.381% |
| 20 | Average memory utilization | 62.654% |
| 20 | Average operation intensity | 8,454.392 |
| 20 | Comm time | 53,273,092.000 |
| 20 | Compute bound percentage | 52.886% |
| 20 | GPU time | 1,222,784.000 |
| 20 | Total compute-communication overlap | 575,944.000 |
| 20 | Wall time | 53,919,932.000 |
| 21 | Average compute utilization | 79.381% |
| 21 | Average memory utilization | 62.654% |
| 21 | Average operation intensity | 8,454.392 |
| 21 | Comm time | 53,238,780.000 |
| 21 | Compute bound percentage | 52.886% |
| 21 | GPU time | 1,222,784.000 |
| 21 | Total compute-communication overlap | 575,944.000 |
| 21 | Wall time | 53,885,620.000 |
| 22 | Average compute utilization | 79.381% |
| 22 | Average memory utilization | 62.654% |
| 22 | Average operation intensity | 8,454.392 |
| 22 | Comm time | 52,905,422.000 |
| 22 | Compute bound percentage | 52.886% |
| 22 | GPU time | 1,222,784.000 |
| 22 | Total compute-communication overlap | 569,907.000 |
| 22 | Wall time | 53,558,299.000 |
| 23 | Average compute utilization | 79.381% |
| 23 | Average memory utilization | 62.654% |
| 23 | Average operation intensity | 8,454.392 |
| 23 | Comm time | 53,080,938.000 |
| 23 | Compute bound percentage | 52.886% |
| 23 | GPU time | 1,222,784.000 |
| 23 | Total compute-communication overlap | 575,944.000 |
| 23 | Wall time | 53,727,778.000 |
| 24 | Average compute utilization | 79.381% |
| 24 | Average memory utilization | 62.654% |
| 24 | Average operation intensity | 8,454.392 |
| 24 | Comm time | 54,148,319.000 |
| 24 | Compute bound percentage | 52.886% |
| 24 | GPU time | 1,222,784.000 |
| 24 | Total compute-communication overlap | 565,783.000 |
| 24 | Wall time | 54,805,320.000 |
| 25 | Average compute utilization | 79.381% |
| 25 | Average memory utilization | 62.654% |
| 25 | Average operation intensity | 8,454.392 |
| 25 | Comm time | 53,915,812.000 |
| 25 | Compute bound percentage | 52.886% |
| 25 | GPU time | 1,222,784.000 |
| 25 | Total compute-communication overlap | 572,991.000 |
| 25 | Wall time | 54,565,605.000 |
| 26 | Average compute utilization | 79.381% |
| 26 | Average memory utilization | 62.654% |
| 26 | Average operation intensity | 8,454.392 |
| 26 | Comm time | 53,886,771.000 |
| 26 | Compute bound percentage | 52.886% |
| 26 | GPU time | 1,222,784.000 |
| 26 | Total compute-communication overlap | 575,944.000 |
| 26 | Wall time | 54,533,611.000 |
| 27 | Average compute utilization | 79.381% |
| 27 | Average memory utilization | 62.654% |
| 27 | Average operation intensity | 8,454.392 |
| 27 | Comm time | 53,954,540.000 |
| 27 | Compute bound percentage | 52.886% |
| 27 | GPU time | 1,222,784.000 |
| 27 | Total compute-communication overlap | 575,944.000 |
| 27 | Wall time | 54,601,380.000 |
| 28 | Average compute utilization | 79.381% |
| 28 | Average memory utilization | 62.654% |
| 28 | Average operation intensity | 8,454.392 |
| 28 | Comm time | 52,730,967.000 |
| 28 | Compute bound percentage | 52.886% |
| 28 | GPU time | 1,222,784.000 |
| 28 | Total compute-communication overlap | 575,944.000 |
| 28 | Wall time | 53,377,807.000 |
| 29 | Average compute utilization | 79.381% |
| 29 | Average memory utilization | 62.654% |
| 29 | Average operation intensity | 8,454.392 |
| 29 | Comm time | 52,854,153.000 |
| 29 | Compute bound percentage | 52.886% |
| 29 | GPU time | 1,222,784.000 |
| 29 | Total compute-communication overlap | 568,851.000 |
| 29 | Wall time | 53,508,086.000 |
| 30 | Average compute utilization | 79.381% |
| 30 | Average memory utilization | 62.654% |
| 30 | Average operation intensity | 8,454.392 |
| 30 | Comm time | 52,853,651.000 |
| 30 | Compute bound percentage | 52.886% |
| 30 | GPU time | 1,222,784.000 |
| 30 | Total compute-communication overlap | 575,944.000 |
| 30 | Wall time | 53,500,491.000 |
| 31 | Average compute utilization | 79.381% |
| 31 | Average memory utilization | 62.654% |
| 31 | Average operation intensity | 8,454.392 |
| 31 | Comm time | 52,700,284.000 |
| 31 | Compute bound percentage | 52.886% |
| 31 | GPU time | 1,222,784.000 |
| 31 | Total compute-communication overlap | 575,944.000 |
| 31 | Wall time | 53,347,124.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 7.546 us |
| Median FCT | 3.425 us |
| p95 FCT | 21.596 us |
| Maximum FCT | 608.204 us |
| Median standalone time | 3.248 us |
| Median FCT / standalone | 1.011x |
| p95 FCT / standalone | 2.545x |
| Maximum FCT / standalone | 8.019x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 2.420 us | 4.430 us | 14.919 us | 2.563 us | 0.951x |
| 2.00 KiB | 88,064 | 2.656 us | 4.702 us | 22.840 us | 2.647 us | 1.011x |
| 16.00 KiB | 28,672 | 4.249 us | 6.244 us | 13.938 us | 3.248 us | 1.208x |
| 128.00 KiB | 30,720 | 15.354 us | 28.485 us | 56.262 us | 8.056 us | 2.003x |
| 1.95 MiB | 1,536 | 213.885 us | 379.150 us | 608.204 us | 88.412 us | 2.485x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 2,709,048 |
| Observed queue interval | 59.600 us to 55.081 ms |
| Observed queue duration | 55.022 ms |
| Maximum sampled queue | 711.77 KiB |
| Maximum queue location | switch 38, port 5 |

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
| Trace records recognized | 152,942,720 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 55.085 ms |
| Maximum sampled packet queue | 710.75 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 128 |
| SimSetting window | 113.28 KiB |
| Events | Dequ: 51,395,840, Enqu: 50,151,040, Recv: 51,395,840 |
| Bytes by event | Dequ: 25.51 GiB, Enqu: 24.33 GiB, Recv: 25.51 GiB |
| Observed interface utilization | 101 interfaces; mean 19.694%, max 39.567% |
| Matched packet queue durations | 49,143,854 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 1.796 us |
| Maximum packet queue time | 28.844 us |
| Mean packet queue time | 288 ns |
| Unmatched/duplicate dequeues | 2,251,986 |
| Enqueue-key collisions | 1,007,186 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
