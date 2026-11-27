# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_uniform_torus_twisted_uniform/attempts/20261124_172909_977059/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 37,231,206 |
| Fastest rank completion (cycles) | 37,167,122 |
| Maximum exposed communication (cycles) | 36,008,422 |
| Completed network flows | 163,328 |
| Total bytes sent | 7,822,835,712 |
| Network-flow finish proxy | 37.211 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.381% | 79.381% | 79.381% | 32 |
| Average memory utilization (%) | 62.654% | 62.654% | 62.654% | 32 |
| Average operation intensity | 8,454.392 | 8,454.392 | 8,454.392 | 32 |
| Comm time | 36,555,131.062 | 36,520,282.000 | 36,584,366.000 | 32 |
| Compute bound percentage (%) | 52.886% | 52.886% | 52.886% | 32 |
| GPU time | 1,222,784.000 | 1,222,784.000 | 1,222,784.000 | 32 |
| Total compute-communication overlap | 575,944.000 | 575,944.000 | 575,944.000 | 32 |
| Wall time | 37,201,971.062 | 37,167,122.000 | 37,231,206.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.381% |
| 0 | Average memory utilization | 62.654% |
| 0 | Average operation intensity | 8,454.392 |
| 0 | Comm time | 36,525,647.000 |
| 0 | Compute bound percentage | 52.886% |
| 0 | GPU time | 1,222,784.000 |
| 0 | Total compute-communication overlap | 575,944.000 |
| 0 | Wall time | 37,172,487.000 |
| 1 | Average compute utilization | 79.381% |
| 1 | Average memory utilization | 62.654% |
| 1 | Average operation intensity | 8,454.392 |
| 1 | Comm time | 36,528,503.000 |
| 1 | Compute bound percentage | 52.886% |
| 1 | GPU time | 1,222,784.000 |
| 1 | Total compute-communication overlap | 575,944.000 |
| 1 | Wall time | 37,175,343.000 |
| 2 | Average compute utilization | 79.381% |
| 2 | Average memory utilization | 62.654% |
| 2 | Average operation intensity | 8,454.392 |
| 2 | Comm time | 36,530,251.000 |
| 2 | Compute bound percentage | 52.886% |
| 2 | GPU time | 1,222,784.000 |
| 2 | Total compute-communication overlap | 575,944.000 |
| 2 | Wall time | 37,177,091.000 |
| 3 | Average compute utilization | 79.381% |
| 3 | Average memory utilization | 62.654% |
| 3 | Average operation intensity | 8,454.392 |
| 3 | Comm time | 36,520,282.000 |
| 3 | Compute bound percentage | 52.886% |
| 3 | GPU time | 1,222,784.000 |
| 3 | Total compute-communication overlap | 575,944.000 |
| 3 | Wall time | 37,167,122.000 |
| 4 | Average compute utilization | 79.381% |
| 4 | Average memory utilization | 62.654% |
| 4 | Average operation intensity | 8,454.392 |
| 4 | Comm time | 36,564,242.000 |
| 4 | Compute bound percentage | 52.886% |
| 4 | GPU time | 1,222,784.000 |
| 4 | Total compute-communication overlap | 575,944.000 |
| 4 | Wall time | 37,211,082.000 |
| 5 | Average compute utilization | 79.381% |
| 5 | Average memory utilization | 62.654% |
| 5 | Average operation intensity | 8,454.392 |
| 5 | Comm time | 36,563,146.000 |
| 5 | Compute bound percentage | 52.886% |
| 5 | GPU time | 1,222,784.000 |
| 5 | Total compute-communication overlap | 575,944.000 |
| 5 | Wall time | 37,209,986.000 |
| 6 | Average compute utilization | 79.381% |
| 6 | Average memory utilization | 62.654% |
| 6 | Average operation intensity | 8,454.392 |
| 6 | Comm time | 36,563,739.000 |
| 6 | Compute bound percentage | 52.886% |
| 6 | GPU time | 1,222,784.000 |
| 6 | Total compute-communication overlap | 575,944.000 |
| 6 | Wall time | 37,210,579.000 |
| 7 | Average compute utilization | 79.381% |
| 7 | Average memory utilization | 62.654% |
| 7 | Average operation intensity | 8,454.392 |
| 7 | Comm time | 36,556,947.000 |
| 7 | Compute bound percentage | 52.886% |
| 7 | GPU time | 1,222,784.000 |
| 7 | Total compute-communication overlap | 575,944.000 |
| 7 | Wall time | 37,203,787.000 |
| 8 | Average compute utilization | 79.381% |
| 8 | Average memory utilization | 62.654% |
| 8 | Average operation intensity | 8,454.392 |
| 8 | Comm time | 36,552,493.000 |
| 8 | Compute bound percentage | 52.886% |
| 8 | GPU time | 1,222,784.000 |
| 8 | Total compute-communication overlap | 575,944.000 |
| 8 | Wall time | 37,199,333.000 |
| 9 | Average compute utilization | 79.381% |
| 9 | Average memory utilization | 62.654% |
| 9 | Average operation intensity | 8,454.392 |
| 9 | Comm time | 36,541,941.000 |
| 9 | Compute bound percentage | 52.886% |
| 9 | GPU time | 1,222,784.000 |
| 9 | Total compute-communication overlap | 575,944.000 |
| 9 | Wall time | 37,188,781.000 |
| 10 | Average compute utilization | 79.381% |
| 10 | Average memory utilization | 62.654% |
| 10 | Average operation intensity | 8,454.392 |
| 10 | Comm time | 36,544,027.000 |
| 10 | Compute bound percentage | 52.886% |
| 10 | GPU time | 1,222,784.000 |
| 10 | Total compute-communication overlap | 575,944.000 |
| 10 | Wall time | 37,190,867.000 |
| 11 | Average compute utilization | 79.381% |
| 11 | Average memory utilization | 62.654% |
| 11 | Average operation intensity | 8,454.392 |
| 11 | Comm time | 36,546,279.000 |
| 11 | Compute bound percentage | 52.886% |
| 11 | GPU time | 1,222,784.000 |
| 11 | Total compute-communication overlap | 575,944.000 |
| 11 | Wall time | 37,193,119.000 |
| 12 | Average compute utilization | 79.381% |
| 12 | Average memory utilization | 62.654% |
| 12 | Average operation intensity | 8,454.392 |
| 12 | Comm time | 36,564,352.000 |
| 12 | Compute bound percentage | 52.886% |
| 12 | GPU time | 1,222,784.000 |
| 12 | Total compute-communication overlap | 575,944.000 |
| 12 | Wall time | 37,211,192.000 |
| 13 | Average compute utilization | 79.381% |
| 13 | Average memory utilization | 62.654% |
| 13 | Average operation intensity | 8,454.392 |
| 13 | Comm time | 36,565,314.000 |
| 13 | Compute bound percentage | 52.886% |
| 13 | GPU time | 1,222,784.000 |
| 13 | Total compute-communication overlap | 575,944.000 |
| 13 | Wall time | 37,212,154.000 |
| 14 | Average compute utilization | 79.381% |
| 14 | Average memory utilization | 62.654% |
| 14 | Average operation intensity | 8,454.392 |
| 14 | Comm time | 36,568,882.000 |
| 14 | Compute bound percentage | 52.886% |
| 14 | GPU time | 1,222,784.000 |
| 14 | Total compute-communication overlap | 575,944.000 |
| 14 | Wall time | 37,215,722.000 |
| 15 | Average compute utilization | 79.381% |
| 15 | Average memory utilization | 62.654% |
| 15 | Average operation intensity | 8,454.392 |
| 15 | Comm time | 36,565,613.000 |
| 15 | Compute bound percentage | 52.886% |
| 15 | GPU time | 1,222,784.000 |
| 15 | Total compute-communication overlap | 575,944.000 |
| 15 | Wall time | 37,212,453.000 |
| 16 | Average compute utilization | 79.381% |
| 16 | Average memory utilization | 62.654% |
| 16 | Average operation intensity | 8,454.392 |
| 16 | Comm time | 36,565,073.000 |
| 16 | Compute bound percentage | 52.886% |
| 16 | GPU time | 1,222,784.000 |
| 16 | Total compute-communication overlap | 575,944.000 |
| 16 | Wall time | 37,211,913.000 |
| 17 | Average compute utilization | 79.381% |
| 17 | Average memory utilization | 62.654% |
| 17 | Average operation intensity | 8,454.392 |
| 17 | Comm time | 36,569,692.000 |
| 17 | Compute bound percentage | 52.886% |
| 17 | GPU time | 1,222,784.000 |
| 17 | Total compute-communication overlap | 575,944.000 |
| 17 | Wall time | 37,216,532.000 |
| 18 | Average compute utilization | 79.381% |
| 18 | Average memory utilization | 62.654% |
| 18 | Average operation intensity | 8,454.392 |
| 18 | Comm time | 36,574,351.000 |
| 18 | Compute bound percentage | 52.886% |
| 18 | GPU time | 1,222,784.000 |
| 18 | Total compute-communication overlap | 575,944.000 |
| 18 | Wall time | 37,221,191.000 |
| 19 | Average compute utilization | 79.381% |
| 19 | Average memory utilization | 62.654% |
| 19 | Average operation intensity | 8,454.392 |
| 19 | Comm time | 36,560,740.000 |
| 19 | Compute bound percentage | 52.886% |
| 19 | GPU time | 1,222,784.000 |
| 19 | Total compute-communication overlap | 575,944.000 |
| 19 | Wall time | 37,207,580.000 |
| 20 | Average compute utilization | 79.381% |
| 20 | Average memory utilization | 62.654% |
| 20 | Average operation intensity | 8,454.392 |
| 20 | Comm time | 36,584,366.000 |
| 20 | Compute bound percentage | 52.886% |
| 20 | GPU time | 1,222,784.000 |
| 20 | Total compute-communication overlap | 575,944.000 |
| 20 | Wall time | 37,231,206.000 |
| 21 | Average compute utilization | 79.381% |
| 21 | Average memory utilization | 62.654% |
| 21 | Average operation intensity | 8,454.392 |
| 21 | Comm time | 36,581,200.000 |
| 21 | Compute bound percentage | 52.886% |
| 21 | GPU time | 1,222,784.000 |
| 21 | Total compute-communication overlap | 575,944.000 |
| 21 | Wall time | 37,228,040.000 |
| 22 | Average compute utilization | 79.381% |
| 22 | Average memory utilization | 62.654% |
| 22 | Average operation intensity | 8,454.392 |
| 22 | Comm time | 36,576,251.000 |
| 22 | Compute bound percentage | 52.886% |
| 22 | GPU time | 1,222,784.000 |
| 22 | Total compute-communication overlap | 575,944.000 |
| 22 | Wall time | 37,223,091.000 |
| 23 | Average compute utilization | 79.381% |
| 23 | Average memory utilization | 62.654% |
| 23 | Average operation intensity | 8,454.392 |
| 23 | Comm time | 36,582,051.000 |
| 23 | Compute bound percentage | 52.886% |
| 23 | GPU time | 1,222,784.000 |
| 23 | Total compute-communication overlap | 575,944.000 |
| 23 | Wall time | 37,228,891.000 |
| 24 | Average compute utilization | 79.381% |
| 24 | Average memory utilization | 62.654% |
| 24 | Average operation intensity | 8,454.392 |
| 24 | Comm time | 36,530,391.000 |
| 24 | Compute bound percentage | 52.886% |
| 24 | GPU time | 1,222,784.000 |
| 24 | Total compute-communication overlap | 575,944.000 |
| 24 | Wall time | 37,177,231.000 |
| 25 | Average compute utilization | 79.381% |
| 25 | Average memory utilization | 62.654% |
| 25 | Average operation intensity | 8,454.392 |
| 25 | Comm time | 36,531,957.000 |
| 25 | Compute bound percentage | 52.886% |
| 25 | GPU time | 1,222,784.000 |
| 25 | Total compute-communication overlap | 575,944.000 |
| 25 | Wall time | 37,178,797.000 |
| 26 | Average compute utilization | 79.381% |
| 26 | Average memory utilization | 62.654% |
| 26 | Average operation intensity | 8,454.392 |
| 26 | Comm time | 36,535,837.000 |
| 26 | Compute bound percentage | 52.886% |
| 26 | GPU time | 1,222,784.000 |
| 26 | Total compute-communication overlap | 575,944.000 |
| 26 | Wall time | 37,182,677.000 |
| 27 | Average compute utilization | 79.381% |
| 27 | Average memory utilization | 62.654% |
| 27 | Average operation intensity | 8,454.392 |
| 27 | Comm time | 36,527,436.000 |
| 27 | Compute bound percentage | 52.886% |
| 27 | GPU time | 1,222,784.000 |
| 27 | Total compute-communication overlap | 575,944.000 |
| 27 | Wall time | 37,174,276.000 |
| 28 | Average compute utilization | 79.381% |
| 28 | Average memory utilization | 62.654% |
| 28 | Average operation intensity | 8,454.392 |
| 28 | Comm time | 36,559,937.000 |
| 28 | Compute bound percentage | 52.886% |
| 28 | GPU time | 1,222,784.000 |
| 28 | Total compute-communication overlap | 575,944.000 |
| 28 | Wall time | 37,206,777.000 |
| 29 | Average compute utilization | 79.381% |
| 29 | Average memory utilization | 62.654% |
| 29 | Average operation intensity | 8,454.392 |
| 29 | Comm time | 36,564,124.000 |
| 29 | Compute bound percentage | 52.886% |
| 29 | GPU time | 1,222,784.000 |
| 29 | Total compute-communication overlap | 575,944.000 |
| 29 | Wall time | 37,210,964.000 |
| 30 | Average compute utilization | 79.381% |
| 30 | Average memory utilization | 62.654% |
| 30 | Average operation intensity | 8,454.392 |
| 30 | Comm time | 36,566,364.000 |
| 30 | Compute bound percentage | 52.886% |
| 30 | GPU time | 1,222,784.000 |
| 30 | Total compute-communication overlap | 575,944.000 |
| 30 | Wall time | 37,213,204.000 |
| 31 | Average compute utilization | 79.381% |
| 31 | Average memory utilization | 62.654% |
| 31 | Average operation intensity | 8,454.392 |
| 31 | Comm time | 36,552,766.000 |
| 31 | Compute bound percentage | 52.886% |
| 31 | GPU time | 1,222,784.000 |
| 31 | Total compute-communication overlap | 575,944.000 |
| 31 | Wall time | 37,199,606.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 6.720 us |
| Median FCT | 5.321 us |
| p95 FCT | 11.097 us |
| Maximum FCT | 99.194 us |
| Median standalone time | 5.287 us |
| Median FCT / standalone | 1.003x |
| p95 FCT / standalone | 1.133x |
| Maximum FCT / standalone | 2.852x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 5.214 us | 6.030 us | 6.356 us | 5.203 us | 0.966x |
| 2.00 KiB | 88,064 | 4.216 us | 6.302 us | 6.891 us | 4.247 us | 1.005x |
| 16.00 KiB | 28,672 | 6.890 us | 7.464 us | 10.227 us | 5.888 us | 1.023x |
| 128.00 KiB | 30,720 | 9.148 us | 17.012 us | 26.662 us | 8.616 us | 1.153x |
| 1.95 MiB | 1,536 | 91.327 us | 94.702 us | 99.194 us | 88.972 us | 1.030x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,469,280 |
| Observed queue interval | 148.100 us to 37.207 ms |
| Observed queue duration | 37.059 ms |
| Maximum sampled queue | 50.39 KiB |
| Maximum queue location | switch 50, port 4 |

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
| Trace records recognized | 131,804,288 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 37.210 ms |
| Maximum sampled packet queue | 50.39 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 152.34 KiB |
| Events | Dequ: 44,349,696, Enqu: 43,104,896, Recv: 44,349,696 |
| Bytes by event | Dequ: 21.94 GiB, Enqu: 20.76 GiB, Recv: 21.94 GiB |
| Observed interface utilization | 165 interfaces; mean 15.348%, max 28.527% |
| Matched packet queue durations | 42,872,822 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 74 ns |
| Maximum packet queue time | 2.019 us |
| Mean packet queue time | 18 ns |
| Unmatched/duplicate dequeues | 1,476,874 |
| Enqueue-key collisions | 232,074 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
