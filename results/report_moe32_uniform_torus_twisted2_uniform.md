# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_uniform_torus_twisted2_uniform/attempts/20261127_134159_646329/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 41,041,801 |
| Fastest rank completion (cycles) | 40,854,567 |
| Maximum exposed communication (cycles) | 39,819,017 |
| Completed network flows | 163,328 |
| Total bytes sent | 7,822,835,712 |
| Network-flow finish proxy | 41.021 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.381% | 79.381% | 79.381% | 32 |
| Average memory utilization (%) | 62.654% | 62.654% | 62.654% | 32 |
| Average operation intensity | 8,454.392 | 8,454.392 | 8,454.392 | 32 |
| Comm time | 40,277,833.781 | 40,207,727.000 | 40,394,961.000 | 32 |
| Compute bound percentage (%) | 52.886% | 52.886% | 52.886% | 32 |
| GPU time | 1,222,784.000 | 1,222,784.000 | 1,222,784.000 | 32 |
| Total compute-communication overlap | 575,944.000 | 575,944.000 | 575,944.000 | 32 |
| Wall time | 40,924,673.781 | 40,854,567.000 | 41,041,801.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.381% |
| 0 | Average memory utilization | 62.654% |
| 0 | Average operation intensity | 8,454.392 |
| 0 | Comm time | 40,282,702.000 |
| 0 | Compute bound percentage | 52.886% |
| 0 | GPU time | 1,222,784.000 |
| 0 | Total compute-communication overlap | 575,944.000 |
| 0 | Wall time | 40,929,542.000 |
| 1 | Average compute utilization | 79.381% |
| 1 | Average memory utilization | 62.654% |
| 1 | Average operation intensity | 8,454.392 |
| 1 | Comm time | 40,287,228.000 |
| 1 | Compute bound percentage | 52.886% |
| 1 | GPU time | 1,222,784.000 |
| 1 | Total compute-communication overlap | 575,944.000 |
| 1 | Wall time | 40,934,068.000 |
| 2 | Average compute utilization | 79.381% |
| 2 | Average memory utilization | 62.654% |
| 2 | Average operation intensity | 8,454.392 |
| 2 | Comm time | 40,285,271.000 |
| 2 | Compute bound percentage | 52.886% |
| 2 | GPU time | 1,222,784.000 |
| 2 | Total compute-communication overlap | 575,944.000 |
| 2 | Wall time | 40,932,111.000 |
| 3 | Average compute utilization | 79.381% |
| 3 | Average memory utilization | 62.654% |
| 3 | Average operation intensity | 8,454.392 |
| 3 | Comm time | 40,289,599.000 |
| 3 | Compute bound percentage | 52.886% |
| 3 | GPU time | 1,222,784.000 |
| 3 | Total compute-communication overlap | 575,944.000 |
| 3 | Wall time | 40,936,439.000 |
| 4 | Average compute utilization | 79.381% |
| 4 | Average memory utilization | 62.654% |
| 4 | Average operation intensity | 8,454.392 |
| 4 | Comm time | 40,377,073.000 |
| 4 | Compute bound percentage | 52.886% |
| 4 | GPU time | 1,222,784.000 |
| 4 | Total compute-communication overlap | 575,944.000 |
| 4 | Wall time | 41,023,913.000 |
| 5 | Average compute utilization | 79.381% |
| 5 | Average memory utilization | 62.654% |
| 5 | Average operation intensity | 8,454.392 |
| 5 | Comm time | 40,382,140.000 |
| 5 | Compute bound percentage | 52.886% |
| 5 | GPU time | 1,222,784.000 |
| 5 | Total compute-communication overlap | 575,944.000 |
| 5 | Wall time | 41,028,980.000 |
| 6 | Average compute utilization | 79.381% |
| 6 | Average memory utilization | 62.654% |
| 6 | Average operation intensity | 8,454.392 |
| 6 | Comm time | 40,373,952.000 |
| 6 | Compute bound percentage | 52.886% |
| 6 | GPU time | 1,222,784.000 |
| 6 | Total compute-communication overlap | 575,944.000 |
| 6 | Wall time | 41,020,792.000 |
| 7 | Average compute utilization | 79.381% |
| 7 | Average memory utilization | 62.654% |
| 7 | Average operation intensity | 8,454.392 |
| 7 | Comm time | 40,380,301.000 |
| 7 | Compute bound percentage | 52.886% |
| 7 | GPU time | 1,222,784.000 |
| 7 | Total compute-communication overlap | 575,944.000 |
| 7 | Wall time | 41,027,141.000 |
| 8 | Average compute utilization | 79.381% |
| 8 | Average memory utilization | 62.654% |
| 8 | Average operation intensity | 8,454.392 |
| 8 | Comm time | 40,386,263.000 |
| 8 | Compute bound percentage | 52.886% |
| 8 | GPU time | 1,222,784.000 |
| 8 | Total compute-communication overlap | 575,944.000 |
| 8 | Wall time | 41,033,103.000 |
| 9 | Average compute utilization | 79.381% |
| 9 | Average memory utilization | 62.654% |
| 9 | Average operation intensity | 8,454.392 |
| 9 | Comm time | 40,392,754.000 |
| 9 | Compute bound percentage | 52.886% |
| 9 | GPU time | 1,222,784.000 |
| 9 | Total compute-communication overlap | 575,944.000 |
| 9 | Wall time | 41,039,594.000 |
| 10 | Average compute utilization | 79.381% |
| 10 | Average memory utilization | 62.654% |
| 10 | Average operation intensity | 8,454.392 |
| 10 | Comm time | 40,389,485.000 |
| 10 | Compute bound percentage | 52.886% |
| 10 | GPU time | 1,222,784.000 |
| 10 | Total compute-communication overlap | 575,944.000 |
| 10 | Wall time | 41,036,325.000 |
| 11 | Average compute utilization | 79.381% |
| 11 | Average memory utilization | 62.654% |
| 11 | Average operation intensity | 8,454.392 |
| 11 | Comm time | 40,394,961.000 |
| 11 | Compute bound percentage | 52.886% |
| 11 | GPU time | 1,222,784.000 |
| 11 | Total compute-communication overlap | 575,944.000 |
| 11 | Wall time | 41,041,801.000 |
| 12 | Average compute utilization | 79.381% |
| 12 | Average memory utilization | 62.654% |
| 12 | Average operation intensity | 8,454.392 |
| 12 | Comm time | 40,270,531.000 |
| 12 | Compute bound percentage | 52.886% |
| 12 | GPU time | 1,222,784.000 |
| 12 | Total compute-communication overlap | 575,944.000 |
| 12 | Wall time | 40,917,371.000 |
| 13 | Average compute utilization | 79.381% |
| 13 | Average memory utilization | 62.654% |
| 13 | Average operation intensity | 8,454.392 |
| 13 | Comm time | 40,271,728.000 |
| 13 | Compute bound percentage | 52.886% |
| 13 | GPU time | 1,222,784.000 |
| 13 | Total compute-communication overlap | 575,944.000 |
| 13 | Wall time | 40,918,568.000 |
| 14 | Average compute utilization | 79.381% |
| 14 | Average memory utilization | 62.654% |
| 14 | Average operation intensity | 8,454.392 |
| 14 | Comm time | 40,265,276.000 |
| 14 | Compute bound percentage | 52.886% |
| 14 | GPU time | 1,222,784.000 |
| 14 | Total compute-communication overlap | 575,944.000 |
| 14 | Wall time | 40,912,116.000 |
| 15 | Average compute utilization | 79.381% |
| 15 | Average memory utilization | 62.654% |
| 15 | Average operation intensity | 8,454.392 |
| 15 | Comm time | 40,271,945.000 |
| 15 | Compute bound percentage | 52.886% |
| 15 | GPU time | 1,222,784.000 |
| 15 | Total compute-communication overlap | 575,944.000 |
| 15 | Wall time | 40,918,785.000 |
| 16 | Average compute utilization | 79.381% |
| 16 | Average memory utilization | 62.654% |
| 16 | Average operation intensity | 8,454.392 |
| 16 | Comm time | 40,207,727.000 |
| 16 | Compute bound percentage | 52.886% |
| 16 | GPU time | 1,222,784.000 |
| 16 | Total compute-communication overlap | 575,944.000 |
| 16 | Wall time | 40,854,567.000 |
| 17 | Average compute utilization | 79.381% |
| 17 | Average memory utilization | 62.654% |
| 17 | Average operation intensity | 8,454.392 |
| 17 | Comm time | 40,211,081.000 |
| 17 | Compute bound percentage | 52.886% |
| 17 | GPU time | 1,222,784.000 |
| 17 | Total compute-communication overlap | 575,944.000 |
| 17 | Wall time | 40,857,921.000 |
| 18 | Average compute utilization | 79.381% |
| 18 | Average memory utilization | 62.654% |
| 18 | Average operation intensity | 8,454.392 |
| 18 | Comm time | 40,212,330.000 |
| 18 | Compute bound percentage | 52.886% |
| 18 | GPU time | 1,222,784.000 |
| 18 | Total compute-communication overlap | 575,944.000 |
| 18 | Wall time | 40,859,170.000 |
| 19 | Average compute utilization | 79.381% |
| 19 | Average memory utilization | 62.654% |
| 19 | Average operation intensity | 8,454.392 |
| 19 | Comm time | 40,214,447.000 |
| 19 | Compute bound percentage | 52.886% |
| 19 | GPU time | 1,222,784.000 |
| 19 | Total compute-communication overlap | 575,944.000 |
| 19 | Wall time | 40,861,287.000 |
| 20 | Average compute utilization | 79.381% |
| 20 | Average memory utilization | 62.654% |
| 20 | Average operation intensity | 8,454.392 |
| 20 | Comm time | 40,216,682.000 |
| 20 | Compute bound percentage | 52.886% |
| 20 | GPU time | 1,222,784.000 |
| 20 | Total compute-communication overlap | 575,944.000 |
| 20 | Wall time | 40,863,522.000 |
| 21 | Average compute utilization | 79.381% |
| 21 | Average memory utilization | 62.654% |
| 21 | Average operation intensity | 8,454.392 |
| 21 | Comm time | 40,214,929.000 |
| 21 | Compute bound percentage | 52.886% |
| 21 | GPU time | 1,222,784.000 |
| 21 | Total compute-communication overlap | 575,944.000 |
| 21 | Wall time | 40,861,769.000 |
| 22 | Average compute utilization | 79.381% |
| 22 | Average memory utilization | 62.654% |
| 22 | Average operation intensity | 8,454.392 |
| 22 | Comm time | 40,216,335.000 |
| 22 | Compute bound percentage | 52.886% |
| 22 | GPU time | 1,222,784.000 |
| 22 | Total compute-communication overlap | 575,944.000 |
| 22 | Wall time | 40,863,175.000 |
| 23 | Average compute utilization | 79.381% |
| 23 | Average memory utilization | 62.654% |
| 23 | Average operation intensity | 8,454.392 |
| 23 | Comm time | 40,218,182.000 |
| 23 | Compute bound percentage | 52.886% |
| 23 | GPU time | 1,222,784.000 |
| 23 | Total compute-communication overlap | 575,944.000 |
| 23 | Wall time | 40,865,022.000 |
| 24 | Average compute utilization | 79.381% |
| 24 | Average memory utilization | 62.654% |
| 24 | Average operation intensity | 8,454.392 |
| 24 | Comm time | 40,217,307.000 |
| 24 | Compute bound percentage | 52.886% |
| 24 | GPU time | 1,222,784.000 |
| 24 | Total compute-communication overlap | 575,944.000 |
| 24 | Wall time | 40,864,147.000 |
| 25 | Average compute utilization | 79.381% |
| 25 | Average memory utilization | 62.654% |
| 25 | Average operation intensity | 8,454.392 |
| 25 | Comm time | 40,219,859.000 |
| 25 | Compute bound percentage | 52.886% |
| 25 | GPU time | 1,222,784.000 |
| 25 | Total compute-communication overlap | 575,944.000 |
| 25 | Wall time | 40,866,699.000 |
| 26 | Average compute utilization | 79.381% |
| 26 | Average memory utilization | 62.654% |
| 26 | Average operation intensity | 8,454.392 |
| 26 | Comm time | 40,218,189.000 |
| 26 | Compute bound percentage | 52.886% |
| 26 | GPU time | 1,222,784.000 |
| 26 | Total compute-communication overlap | 575,944.000 |
| 26 | Wall time | 40,865,029.000 |
| 27 | Average compute utilization | 79.381% |
| 27 | Average memory utilization | 62.654% |
| 27 | Average operation intensity | 8,454.392 |
| 27 | Comm time | 40,216,984.000 |
| 27 | Compute bound percentage | 52.886% |
| 27 | GPU time | 1,222,784.000 |
| 27 | Total compute-communication overlap | 575,944.000 |
| 27 | Wall time | 40,863,824.000 |
| 28 | Average compute utilization | 79.381% |
| 28 | Average memory utilization | 62.654% |
| 28 | Average operation intensity | 8,454.392 |
| 28 | Comm time | 40,250,986.000 |
| 28 | Compute bound percentage | 52.886% |
| 28 | GPU time | 1,222,784.000 |
| 28 | Total compute-communication overlap | 575,944.000 |
| 28 | Wall time | 40,897,826.000 |
| 29 | Average compute utilization | 79.381% |
| 29 | Average memory utilization | 62.654% |
| 29 | Average operation intensity | 8,454.392 |
| 29 | Comm time | 40,256,406.000 |
| 29 | Compute bound percentage | 52.886% |
| 29 | GPU time | 1,222,784.000 |
| 29 | Total compute-communication overlap | 575,944.000 |
| 29 | Wall time | 40,903,246.000 |
| 30 | Average compute utilization | 79.381% |
| 30 | Average memory utilization | 62.654% |
| 30 | Average operation intensity | 8,454.392 |
| 30 | Comm time | 40,248,613.000 |
| 30 | Compute bound percentage | 52.886% |
| 30 | GPU time | 1,222,784.000 |
| 30 | Total compute-communication overlap | 575,944.000 |
| 30 | Wall time | 40,895,453.000 |
| 31 | Average compute utilization | 79.381% |
| 31 | Average memory utilization | 62.654% |
| 31 | Average operation intensity | 8,454.392 |
| 31 | Comm time | 40,249,415.000 |
| 31 | Compute bound percentage | 52.886% |
| 31 | GPU time | 1,222,784.000 |
| 31 | Total compute-communication overlap | 575,944.000 |
| 31 | Wall time | 40,896,255.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 7.358 us |
| Median FCT | 6.304 us |
| p95 FCT | 11.190 us |
| Maximum FCT | 101.357 us |
| Median standalone time | 6.327 us |
| Median FCT / standalone | 1.004x |
| p95 FCT / standalone | 1.149x |
| Maximum FCT / standalone | 2.862x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 6.030 us | 7.035 us | 7.619 us | 6.243 us | 0.966x |
| 2.00 KiB | 88,064 | 5.259 us | 7.347 us | 8.082 us | 5.287 us | 1.004x |
| 16.00 KiB | 28,672 | 7.393 us | 8.632 us | 10.792 us | 6.928 us | 1.036x |
| 128.00 KiB | 30,720 | 9.114 us | 17.998 us | 26.753 us | 8.616 us | 1.171x |
| 1.95 MiB | 1,536 | 91.619 us | 95.861 us | 101.357 us | 88.972 us | 1.034x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,611,222 |
| Observed queue interval | 176.200 us to 41.019 ms |
| Observed queue duration | 40.843 ms |
| Maximum sampled queue | 52.20 KiB |
| Maximum queue location | switch 34, port 2 |

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
| Trace records recognized | 135,699,584 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 41.021 ms |
| Maximum sampled packet queue | 52.20 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 177.73 KiB |
| Events | Dequ: 45,648,128, Enqu: 44,403,328, Recv: 45,648,128 |
| Bytes by event | Dequ: 22.52 GiB, Enqu: 21.34 GiB, Recv: 22.52 GiB |
| Observed interface utilization | 165 interfaces; mean 14.291%, max 27.869% |
| Matched packet queue durations | 44,133,840 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 81 ns |
| Maximum packet queue time | 2.091 us |
| Mean packet queue time | 19 ns |
| Unmatched/duplicate dequeues | 1,514,288 |
| Enqueue-key collisions | 269,488 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
