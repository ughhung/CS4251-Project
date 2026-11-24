# ASTRA-sim NS-3 Results Report

Result directory: `work/results/fattree32_moe_top1_roofline_d005`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 394,266,033 |
| Fastest rank completion (cycles) | 393,957,487 |
| Maximum exposed communication (cycles) | 393,043,377 |
| Completed network flows | 335,360 |
| Total bytes sent | 8,175,157,248 |
| Network-flow finish proxy | 394.246 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.379% | 79.379% | 79.379% | 32 |
| Average memory utilization (%) | 62.660% | 62.660% | 62.660% | 32 |
| Average operation intensity | 8,266.835 | 8,266.835 | 8,266.835 | 32 |
| Comm time | 393,945,122.906 | 393,802,488.000 | 394,111,034.000 | 32 |
| Compute bound percentage (%) | 52.882% | 52.882% | 52.882% | 32 |
| GPU time | 1,222,656.000 | 1,222,656.000 | 1,222,656.000 | 32 |
| Total compute-communication overlap | 1,067,657.000 | 1,067,657.000 | 1,067,657.000 | 32 |
| Wall time | 394,100,121.906 | 393,957,487.000 | 394,266,033.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.379% |
| 0 | Average memory utilization | 62.660% |
| 0 | Average operation intensity | 8,266.835 |
| 0 | Comm time | 393,844,936.000 |
| 0 | Compute bound percentage | 52.882% |
| 0 | GPU time | 1,222,656.000 |
| 0 | Total compute-communication overlap | 1,067,657.000 |
| 0 | Wall time | 393,999,935.000 |
| 1 | Average compute utilization | 79.379% |
| 1 | Average memory utilization | 62.660% |
| 1 | Average operation intensity | 8,266.835 |
| 1 | Comm time | 393,802,488.000 |
| 1 | Compute bound percentage | 52.882% |
| 1 | GPU time | 1,222,656.000 |
| 1 | Total compute-communication overlap | 1,067,657.000 |
| 1 | Wall time | 393,957,487.000 |
| 2 | Average compute utilization | 79.379% |
| 2 | Average memory utilization | 62.660% |
| 2 | Average operation intensity | 8,266.835 |
| 2 | Comm time | 393,831,934.000 |
| 2 | Compute bound percentage | 52.882% |
| 2 | GPU time | 1,222,656.000 |
| 2 | Total compute-communication overlap | 1,067,657.000 |
| 2 | Wall time | 393,986,933.000 |
| 3 | Average compute utilization | 79.379% |
| 3 | Average memory utilization | 62.660% |
| 3 | Average operation intensity | 8,266.835 |
| 3 | Comm time | 393,856,744.000 |
| 3 | Compute bound percentage | 52.882% |
| 3 | GPU time | 1,222,656.000 |
| 3 | Total compute-communication overlap | 1,067,657.000 |
| 3 | Wall time | 394,011,743.000 |
| 4 | Average compute utilization | 79.379% |
| 4 | Average memory utilization | 62.660% |
| 4 | Average operation intensity | 8,266.835 |
| 4 | Comm time | 393,877,473.000 |
| 4 | Compute bound percentage | 52.882% |
| 4 | GPU time | 1,222,656.000 |
| 4 | Total compute-communication overlap | 1,067,657.000 |
| 4 | Wall time | 394,032,472.000 |
| 5 | Average compute utilization | 79.379% |
| 5 | Average memory utilization | 62.660% |
| 5 | Average operation intensity | 8,266.835 |
| 5 | Comm time | 393,843,300.000 |
| 5 | Compute bound percentage | 52.882% |
| 5 | GPU time | 1,222,656.000 |
| 5 | Total compute-communication overlap | 1,067,657.000 |
| 5 | Wall time | 393,998,299.000 |
| 6 | Average compute utilization | 79.379% |
| 6 | Average memory utilization | 62.660% |
| 6 | Average operation intensity | 8,266.835 |
| 6 | Comm time | 393,833,474.000 |
| 6 | Compute bound percentage | 52.882% |
| 6 | GPU time | 1,222,656.000 |
| 6 | Total compute-communication overlap | 1,067,657.000 |
| 6 | Wall time | 393,988,473.000 |
| 7 | Average compute utilization | 79.379% |
| 7 | Average memory utilization | 62.660% |
| 7 | Average operation intensity | 8,266.835 |
| 7 | Comm time | 393,850,784.000 |
| 7 | Compute bound percentage | 52.882% |
| 7 | GPU time | 1,222,656.000 |
| 7 | Total compute-communication overlap | 1,067,657.000 |
| 7 | Wall time | 394,005,783.000 |
| 8 | Average compute utilization | 79.379% |
| 8 | Average memory utilization | 62.660% |
| 8 | Average operation intensity | 8,266.835 |
| 8 | Comm time | 393,921,728.000 |
| 8 | Compute bound percentage | 52.882% |
| 8 | GPU time | 1,222,656.000 |
| 8 | Total compute-communication overlap | 1,067,657.000 |
| 8 | Wall time | 394,076,727.000 |
| 9 | Average compute utilization | 79.379% |
| 9 | Average memory utilization | 62.660% |
| 9 | Average operation intensity | 8,266.835 |
| 9 | Comm time | 393,875,414.000 |
| 9 | Compute bound percentage | 52.882% |
| 9 | GPU time | 1,222,656.000 |
| 9 | Total compute-communication overlap | 1,067,657.000 |
| 9 | Wall time | 394,030,413.000 |
| 10 | Average compute utilization | 79.379% |
| 10 | Average memory utilization | 62.660% |
| 10 | Average operation intensity | 8,266.835 |
| 10 | Comm time | 393,880,597.000 |
| 10 | Compute bound percentage | 52.882% |
| 10 | GPU time | 1,222,656.000 |
| 10 | Total compute-communication overlap | 1,067,657.000 |
| 10 | Wall time | 394,035,596.000 |
| 11 | Average compute utilization | 79.379% |
| 11 | Average memory utilization | 62.660% |
| 11 | Average operation intensity | 8,266.835 |
| 11 | Comm time | 393,908,528.000 |
| 11 | Compute bound percentage | 52.882% |
| 11 | GPU time | 1,222,656.000 |
| 11 | Total compute-communication overlap | 1,067,657.000 |
| 11 | Wall time | 394,063,527.000 |
| 12 | Average compute utilization | 79.379% |
| 12 | Average memory utilization | 62.660% |
| 12 | Average operation intensity | 8,266.835 |
| 12 | Comm time | 393,942,300.000 |
| 12 | Compute bound percentage | 52.882% |
| 12 | GPU time | 1,222,656.000 |
| 12 | Total compute-communication overlap | 1,067,657.000 |
| 12 | Wall time | 394,097,299.000 |
| 13 | Average compute utilization | 79.379% |
| 13 | Average memory utilization | 62.660% |
| 13 | Average operation intensity | 8,266.835 |
| 13 | Comm time | 393,915,137.000 |
| 13 | Compute bound percentage | 52.882% |
| 13 | GPU time | 1,222,656.000 |
| 13 | Total compute-communication overlap | 1,067,657.000 |
| 13 | Wall time | 394,070,136.000 |
| 14 | Average compute utilization | 79.379% |
| 14 | Average memory utilization | 62.660% |
| 14 | Average operation intensity | 8,266.835 |
| 14 | Comm time | 393,905,164.000 |
| 14 | Compute bound percentage | 52.882% |
| 14 | GPU time | 1,222,656.000 |
| 14 | Total compute-communication overlap | 1,067,657.000 |
| 14 | Wall time | 394,060,163.000 |
| 15 | Average compute utilization | 79.379% |
| 15 | Average memory utilization | 62.660% |
| 15 | Average operation intensity | 8,266.835 |
| 15 | Comm time | 393,917,333.000 |
| 15 | Compute bound percentage | 52.882% |
| 15 | GPU time | 1,222,656.000 |
| 15 | Total compute-communication overlap | 1,067,657.000 |
| 15 | Wall time | 394,072,332.000 |
| 16 | Average compute utilization | 79.379% |
| 16 | Average memory utilization | 62.660% |
| 16 | Average operation intensity | 8,266.835 |
| 16 | Comm time | 394,080,163.000 |
| 16 | Compute bound percentage | 52.882% |
| 16 | GPU time | 1,222,656.000 |
| 16 | Total compute-communication overlap | 1,067,657.000 |
| 16 | Wall time | 394,235,162.000 |
| 17 | Average compute utilization | 79.379% |
| 17 | Average memory utilization | 62.660% |
| 17 | Average operation intensity | 8,266.835 |
| 17 | Comm time | 394,111,034.000 |
| 17 | Compute bound percentage | 52.882% |
| 17 | GPU time | 1,222,656.000 |
| 17 | Total compute-communication overlap | 1,067,657.000 |
| 17 | Wall time | 394,266,033.000 |
| 18 | Average compute utilization | 79.379% |
| 18 | Average memory utilization | 62.660% |
| 18 | Average operation intensity | 8,266.835 |
| 18 | Comm time | 394,071,024.000 |
| 18 | Compute bound percentage | 52.882% |
| 18 | GPU time | 1,222,656.000 |
| 18 | Total compute-communication overlap | 1,067,657.000 |
| 18 | Wall time | 394,226,023.000 |
| 19 | Average compute utilization | 79.379% |
| 19 | Average memory utilization | 62.660% |
| 19 | Average operation intensity | 8,266.835 |
| 19 | Comm time | 394,049,374.000 |
| 19 | Compute bound percentage | 52.882% |
| 19 | GPU time | 1,222,656.000 |
| 19 | Total compute-communication overlap | 1,067,657.000 |
| 19 | Wall time | 394,204,373.000 |
| 20 | Average compute utilization | 79.379% |
| 20 | Average memory utilization | 62.660% |
| 20 | Average operation intensity | 8,266.835 |
| 20 | Comm time | 394,013,753.000 |
| 20 | Compute bound percentage | 52.882% |
| 20 | GPU time | 1,222,656.000 |
| 20 | Total compute-communication overlap | 1,067,657.000 |
| 20 | Wall time | 394,168,752.000 |
| 21 | Average compute utilization | 79.379% |
| 21 | Average memory utilization | 62.660% |
| 21 | Average operation intensity | 8,266.835 |
| 21 | Comm time | 394,028,101.000 |
| 21 | Compute bound percentage | 52.882% |
| 21 | GPU time | 1,222,656.000 |
| 21 | Total compute-communication overlap | 1,067,657.000 |
| 21 | Wall time | 394,183,100.000 |
| 22 | Average compute utilization | 79.379% |
| 22 | Average memory utilization | 62.660% |
| 22 | Average operation intensity | 8,266.835 |
| 22 | Comm time | 393,997,503.000 |
| 22 | Compute bound percentage | 52.882% |
| 22 | GPU time | 1,222,656.000 |
| 22 | Total compute-communication overlap | 1,067,657.000 |
| 22 | Wall time | 394,152,502.000 |
| 23 | Average compute utilization | 79.379% |
| 23 | Average memory utilization | 62.660% |
| 23 | Average operation intensity | 8,266.835 |
| 23 | Comm time | 393,984,307.000 |
| 23 | Compute bound percentage | 52.882% |
| 23 | GPU time | 1,222,656.000 |
| 23 | Total compute-communication overlap | 1,067,657.000 |
| 23 | Wall time | 394,139,306.000 |
| 24 | Average compute utilization | 79.379% |
| 24 | Average memory utilization | 62.660% |
| 24 | Average operation intensity | 8,266.835 |
| 24 | Comm time | 393,972,864.000 |
| 24 | Compute bound percentage | 52.882% |
| 24 | GPU time | 1,222,656.000 |
| 24 | Total compute-communication overlap | 1,067,657.000 |
| 24 | Wall time | 394,127,863.000 |
| 25 | Average compute utilization | 79.379% |
| 25 | Average memory utilization | 62.660% |
| 25 | Average operation intensity | 8,266.835 |
| 25 | Comm time | 393,985,900.000 |
| 25 | Compute bound percentage | 52.882% |
| 25 | GPU time | 1,222,656.000 |
| 25 | Total compute-communication overlap | 1,067,657.000 |
| 25 | Wall time | 394,140,899.000 |
| 26 | Average compute utilization | 79.379% |
| 26 | Average memory utilization | 62.660% |
| 26 | Average operation intensity | 8,266.835 |
| 26 | Comm time | 393,939,537.000 |
| 26 | Compute bound percentage | 52.882% |
| 26 | GPU time | 1,222,656.000 |
| 26 | Total compute-communication overlap | 1,067,657.000 |
| 26 | Wall time | 394,094,536.000 |
| 27 | Average compute utilization | 79.379% |
| 27 | Average memory utilization | 62.660% |
| 27 | Average operation intensity | 8,266.835 |
| 27 | Comm time | 393,964,244.000 |
| 27 | Compute bound percentage | 52.882% |
| 27 | GPU time | 1,222,656.000 |
| 27 | Total compute-communication overlap | 1,067,657.000 |
| 27 | Wall time | 394,119,243.000 |
| 28 | Average compute utilization | 79.379% |
| 28 | Average memory utilization | 62.660% |
| 28 | Average operation intensity | 8,266.835 |
| 28 | Comm time | 393,992,625.000 |
| 28 | Compute bound percentage | 52.882% |
| 28 | GPU time | 1,222,656.000 |
| 28 | Total compute-communication overlap | 1,067,657.000 |
| 28 | Wall time | 394,147,624.000 |
| 29 | Average compute utilization | 79.379% |
| 29 | Average memory utilization | 62.660% |
| 29 | Average operation intensity | 8,266.835 |
| 29 | Comm time | 394,020,594.000 |
| 29 | Compute bound percentage | 52.882% |
| 29 | GPU time | 1,222,656.000 |
| 29 | Total compute-communication overlap | 1,067,657.000 |
| 29 | Wall time | 394,175,593.000 |
| 30 | Average compute utilization | 79.379% |
| 30 | Average memory utilization | 62.660% |
| 30 | Average operation intensity | 8,266.835 |
| 30 | Comm time | 394,035,516.000 |
| 30 | Compute bound percentage | 52.882% |
| 30 | GPU time | 1,222,656.000 |
| 30 | Total compute-communication overlap | 1,067,657.000 |
| 30 | Wall time | 394,190,515.000 |
| 31 | Average compute utilization | 79.379% |
| 31 | Average memory utilization | 62.660% |
| 31 | Average operation intensity | 8,266.835 |
| 31 | Comm time | 393,990,060.000 |
| 31 | Compute bound percentage | 52.882% |
| 31 | GPU time | 1,222,656.000 |
| 31 | Total compute-communication overlap | 1,067,657.000 |
| 31 | Wall time | 394,145,059.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 37.509 us |
| Median FCT | 40.216 us |
| p95 FCT | 40.804 us |
| Maximum FCT | 126.245 us |
| Median standalone time | 40.247 us |
| Median FCT / standalone | 0.999x |
| p95 FCT / standalone | 1.008x |
| Maximum FCT / standalone | 1.624x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 40.020 us | 40.020 us | 40.144 us | 40.163 us | 0.996x |
| 2.00 KiB | 260,096 | 40.216 us | 40.216 us | 41.331 us | 40.247 us | 0.999x |
| 16.00 KiB | 28,672 | 40.804 us | 41.381 us | 45.476 us | 40.848 us | 1.001x |
| 128.00 KiB | 30,720 | 25.612 us | 31.963 us | 41.541 us | 25.576 us | 1.042x |
| 1.95 MiB | 1,536 | 108.462 us | 115.884 us | 126.245 us | 105.932 us | 1.037x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 749,396 |
| Observed queue interval | 1.126 ms to 394.227 ms |
| Observed queue duration | 393.101 ms |
| Maximum sampled queue | 73.20 KiB |
| Maximum queue location | switch 33, port 2 |

The queue interval is the time span covered by non-empty queue records; it is not per-flow queueing duration.

## PFC and flow inputs

| Metric | Result |
| --- | --- |
| PFC events | 0 |
| Static flows declared | 0 |
| Trace nodes listed | 5 |

## Packet trace

| Metric | Result |
| --- | --- |
| Trace records recognized | 6,627,200 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 394.002 ms |
| Maximum sampled packet queue | 0.00 B |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 96 |
| SimSetting window | 980.47 KiB |
| Events | Dequ: 2,650,880, Enqu: 1,325,440, Recv: 2,650,880 |
| Bytes by event | Dequ: 1.29 GiB, Enqu: 60.67 MiB, Recv: 1.29 GiB |
| Observed interface utilization | 5 interfaces; mean 2.820%, max 2.820% |
| Matched packet queue durations | 1,324,819 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 35 ns |
| Maximum packet queue time | 40 ns |
| Mean packet queue time | 7 ns |
| Unmatched/duplicate dequeues | 1,326,061 |
| Enqueue-key collisions | 621 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.