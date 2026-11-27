# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/baseline_torus_random2_uniform/attempts/20261126_030556_566401/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 45,514,221 |
| Fastest rank completion (cycles) | 44,424,369 |
| Maximum exposed communication (cycles) | 45,107,129 |
| Completed network flows | 50,176 |
| Total bytes sent | 9,525,264,384 |
| Network-flow finish proxy | 45.494 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 40.267% | 40.267% | 40.267% | 32 |
| Average memory utilization (%) | 83.379% | 83.379% | 83.379% | 32 |
| Average operation intensity | 3,183.497 | 3,183.497 | 3,183.497 | 32 |
| Comm time | 45,077,428.500 | 44,316,261.000 | 45,406,113.000 | 32 |
| Compute bound percentage (%) | 26.074% | 26.074% | 26.074% | 32 |
| GPU time | 407,092.000 | 407,092.000 | 407,092.000 | 32 |
| Total compute-communication overlap | 298,984.000 | 298,984.000 | 298,984.000 | 32 |
| Wall time | 45,185,536.500 | 44,424,369.000 | 45,514,221.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 40.267% |
| 0 | Average memory utilization | 83.379% |
| 0 | Average operation intensity | 3,183.497 |
| 0 | Comm time | 45,000,563.000 |
| 0 | Compute bound percentage | 26.074% |
| 0 | GPU time | 407,092.000 |
| 0 | Total compute-communication overlap | 298,984.000 |
| 0 | Wall time | 45,108,671.000 |
| 1 | Average compute utilization | 40.267% |
| 1 | Average memory utilization | 83.379% |
| 1 | Average operation intensity | 3,183.497 |
| 1 | Comm time | 45,323,184.000 |
| 1 | Compute bound percentage | 26.074% |
| 1 | GPU time | 407,092.000 |
| 1 | Total compute-communication overlap | 298,984.000 |
| 1 | Wall time | 45,431,292.000 |
| 2 | Average compute utilization | 40.267% |
| 2 | Average memory utilization | 83.379% |
| 2 | Average operation intensity | 3,183.497 |
| 2 | Comm time | 44,363,080.000 |
| 2 | Compute bound percentage | 26.074% |
| 2 | GPU time | 407,092.000 |
| 2 | Total compute-communication overlap | 298,984.000 |
| 2 | Wall time | 44,471,188.000 |
| 3 | Average compute utilization | 40.267% |
| 3 | Average memory utilization | 83.379% |
| 3 | Average operation intensity | 3,183.497 |
| 3 | Comm time | 45,245,567.000 |
| 3 | Compute bound percentage | 26.074% |
| 3 | GPU time | 407,092.000 |
| 3 | Total compute-communication overlap | 298,984.000 |
| 3 | Wall time | 45,353,675.000 |
| 4 | Average compute utilization | 40.267% |
| 4 | Average memory utilization | 83.379% |
| 4 | Average operation intensity | 3,183.497 |
| 4 | Comm time | 45,047,437.000 |
| 4 | Compute bound percentage | 26.074% |
| 4 | GPU time | 407,092.000 |
| 4 | Total compute-communication overlap | 298,984.000 |
| 4 | Wall time | 45,155,545.000 |
| 5 | Average compute utilization | 40.267% |
| 5 | Average memory utilization | 83.379% |
| 5 | Average operation intensity | 3,183.497 |
| 5 | Comm time | 45,036,033.000 |
| 5 | Compute bound percentage | 26.074% |
| 5 | GPU time | 407,092.000 |
| 5 | Total compute-communication overlap | 298,984.000 |
| 5 | Wall time | 45,144,141.000 |
| 6 | Average compute utilization | 40.267% |
| 6 | Average memory utilization | 83.379% |
| 6 | Average operation intensity | 3,183.497 |
| 6 | Comm time | 45,299,095.000 |
| 6 | Compute bound percentage | 26.074% |
| 6 | GPU time | 407,092.000 |
| 6 | Total compute-communication overlap | 298,984.000 |
| 6 | Wall time | 45,407,203.000 |
| 7 | Average compute utilization | 40.267% |
| 7 | Average memory utilization | 83.379% |
| 7 | Average operation intensity | 3,183.497 |
| 7 | Comm time | 45,250,716.000 |
| 7 | Compute bound percentage | 26.074% |
| 7 | GPU time | 407,092.000 |
| 7 | Total compute-communication overlap | 298,984.000 |
| 7 | Wall time | 45,358,824.000 |
| 8 | Average compute utilization | 40.267% |
| 8 | Average memory utilization | 83.379% |
| 8 | Average operation intensity | 3,183.497 |
| 8 | Comm time | 45,129,626.000 |
| 8 | Compute bound percentage | 26.074% |
| 8 | GPU time | 407,092.000 |
| 8 | Total compute-communication overlap | 298,984.000 |
| 8 | Wall time | 45,237,734.000 |
| 9 | Average compute utilization | 40.267% |
| 9 | Average memory utilization | 83.379% |
| 9 | Average operation intensity | 3,183.497 |
| 9 | Comm time | 45,389,018.000 |
| 9 | Compute bound percentage | 26.074% |
| 9 | GPU time | 407,092.000 |
| 9 | Total compute-communication overlap | 298,984.000 |
| 9 | Wall time | 45,497,126.000 |
| 10 | Average compute utilization | 40.267% |
| 10 | Average memory utilization | 83.379% |
| 10 | Average operation intensity | 3,183.497 |
| 10 | Comm time | 44,463,973.000 |
| 10 | Compute bound percentage | 26.074% |
| 10 | GPU time | 407,092.000 |
| 10 | Total compute-communication overlap | 298,984.000 |
| 10 | Wall time | 44,572,081.000 |
| 11 | Average compute utilization | 40.267% |
| 11 | Average memory utilization | 83.379% |
| 11 | Average operation intensity | 3,183.497 |
| 11 | Comm time | 45,365,459.000 |
| 11 | Compute bound percentage | 26.074% |
| 11 | GPU time | 407,092.000 |
| 11 | Total compute-communication overlap | 298,984.000 |
| 11 | Wall time | 45,473,567.000 |
| 12 | Average compute utilization | 40.267% |
| 12 | Average memory utilization | 83.379% |
| 12 | Average operation intensity | 3,183.497 |
| 12 | Comm time | 45,134,735.000 |
| 12 | Compute bound percentage | 26.074% |
| 12 | GPU time | 407,092.000 |
| 12 | Total compute-communication overlap | 298,984.000 |
| 12 | Wall time | 45,242,843.000 |
| 13 | Average compute utilization | 40.267% |
| 13 | Average memory utilization | 83.379% |
| 13 | Average operation intensity | 3,183.497 |
| 13 | Comm time | 45,126,309.000 |
| 13 | Compute bound percentage | 26.074% |
| 13 | GPU time | 407,092.000 |
| 13 | Total compute-communication overlap | 298,984.000 |
| 13 | Wall time | 45,234,417.000 |
| 14 | Average compute utilization | 40.267% |
| 14 | Average memory utilization | 83.379% |
| 14 | Average operation intensity | 3,183.497 |
| 14 | Comm time | 45,360,055.000 |
| 14 | Compute bound percentage | 26.074% |
| 14 | GPU time | 407,092.000 |
| 14 | Total compute-communication overlap | 298,984.000 |
| 14 | Wall time | 45,468,163.000 |
| 15 | Average compute utilization | 40.267% |
| 15 | Average memory utilization | 83.379% |
| 15 | Average operation intensity | 3,183.497 |
| 15 | Comm time | 45,332,007.000 |
| 15 | Compute bound percentage | 26.074% |
| 15 | GPU time | 407,092.000 |
| 15 | Total compute-communication overlap | 298,984.000 |
| 15 | Wall time | 45,440,115.000 |
| 16 | Average compute utilization | 40.267% |
| 16 | Average memory utilization | 83.379% |
| 16 | Average operation intensity | 3,183.497 |
| 16 | Comm time | 45,035,248.000 |
| 16 | Compute bound percentage | 26.074% |
| 16 | GPU time | 407,092.000 |
| 16 | Total compute-communication overlap | 298,984.000 |
| 16 | Wall time | 45,143,356.000 |
| 17 | Average compute utilization | 40.267% |
| 17 | Average memory utilization | 83.379% |
| 17 | Average operation intensity | 3,183.497 |
| 17 | Comm time | 45,406,113.000 |
| 17 | Compute bound percentage | 26.074% |
| 17 | GPU time | 407,092.000 |
| 17 | Total compute-communication overlap | 298,984.000 |
| 17 | Wall time | 45,514,221.000 |
| 18 | Average compute utilization | 40.267% |
| 18 | Average memory utilization | 83.379% |
| 18 | Average operation intensity | 3,183.497 |
| 18 | Comm time | 44,386,579.000 |
| 18 | Compute bound percentage | 26.074% |
| 18 | GPU time | 407,092.000 |
| 18 | Total compute-communication overlap | 298,984.000 |
| 18 | Wall time | 44,494,687.000 |
| 19 | Average compute utilization | 40.267% |
| 19 | Average memory utilization | 83.379% |
| 19 | Average operation intensity | 3,183.497 |
| 19 | Comm time | 44,962,239.000 |
| 19 | Compute bound percentage | 26.074% |
| 19 | GPU time | 407,092.000 |
| 19 | Total compute-communication overlap | 298,984.000 |
| 19 | Wall time | 45,070,347.000 |
| 20 | Average compute utilization | 40.267% |
| 20 | Average memory utilization | 83.379% |
| 20 | Average operation intensity | 3,183.497 |
| 20 | Comm time | 45,175,714.000 |
| 20 | Compute bound percentage | 26.074% |
| 20 | GPU time | 407,092.000 |
| 20 | Total compute-communication overlap | 298,984.000 |
| 20 | Wall time | 45,283,822.000 |
| 21 | Average compute utilization | 40.267% |
| 21 | Average memory utilization | 83.379% |
| 21 | Average operation intensity | 3,183.497 |
| 21 | Comm time | 45,117,341.000 |
| 21 | Compute bound percentage | 26.074% |
| 21 | GPU time | 407,092.000 |
| 21 | Total compute-communication overlap | 298,984.000 |
| 21 | Wall time | 45,225,449.000 |
| 22 | Average compute utilization | 40.267% |
| 22 | Average memory utilization | 83.379% |
| 22 | Average operation intensity | 3,183.497 |
| 22 | Comm time | 45,016,788.000 |
| 22 | Compute bound percentage | 26.074% |
| 22 | GPU time | 407,092.000 |
| 22 | Total compute-communication overlap | 298,984.000 |
| 22 | Wall time | 45,124,896.000 |
| 23 | Average compute utilization | 40.267% |
| 23 | Average memory utilization | 83.379% |
| 23 | Average operation intensity | 3,183.497 |
| 23 | Comm time | 45,245,461.000 |
| 23 | Compute bound percentage | 26.074% |
| 23 | GPU time | 407,092.000 |
| 23 | Total compute-communication overlap | 298,984.000 |
| 23 | Wall time | 45,353,569.000 |
| 24 | Average compute utilization | 40.267% |
| 24 | Average memory utilization | 83.379% |
| 24 | Average operation intensity | 3,183.497 |
| 24 | Comm time | 44,889,550.000 |
| 24 | Compute bound percentage | 26.074% |
| 24 | GPU time | 407,092.000 |
| 24 | Total compute-communication overlap | 298,984.000 |
| 24 | Wall time | 44,997,658.000 |
| 25 | Average compute utilization | 40.267% |
| 25 | Average memory utilization | 83.379% |
| 25 | Average operation intensity | 3,183.497 |
| 25 | Comm time | 45,347,756.000 |
| 25 | Compute bound percentage | 26.074% |
| 25 | GPU time | 407,092.000 |
| 25 | Total compute-communication overlap | 298,984.000 |
| 25 | Wall time | 45,455,864.000 |
| 26 | Average compute utilization | 40.267% |
| 26 | Average memory utilization | 83.379% |
| 26 | Average operation intensity | 3,183.497 |
| 26 | Comm time | 44,316,261.000 |
| 26 | Compute bound percentage | 26.074% |
| 26 | GPU time | 407,092.000 |
| 26 | Total compute-communication overlap | 298,984.000 |
| 26 | Wall time | 44,424,369.000 |
| 27 | Average compute utilization | 40.267% |
| 27 | Average memory utilization | 83.379% |
| 27 | Average operation intensity | 3,183.497 |
| 27 | Comm time | 45,111,073.000 |
| 27 | Compute bound percentage | 26.074% |
| 27 | GPU time | 407,092.000 |
| 27 | Total compute-communication overlap | 298,984.000 |
| 27 | Wall time | 45,219,181.000 |
| 28 | Average compute utilization | 40.267% |
| 28 | Average memory utilization | 83.379% |
| 28 | Average operation intensity | 3,183.497 |
| 28 | Comm time | 45,256,521.000 |
| 28 | Compute bound percentage | 26.074% |
| 28 | GPU time | 407,092.000 |
| 28 | Total compute-communication overlap | 298,984.000 |
| 28 | Wall time | 45,364,629.000 |
| 29 | Average compute utilization | 40.267% |
| 29 | Average memory utilization | 83.379% |
| 29 | Average operation intensity | 3,183.497 |
| 29 | Comm time | 44,913,026.000 |
| 29 | Compute bound percentage | 26.074% |
| 29 | GPU time | 407,092.000 |
| 29 | Total compute-communication overlap | 298,984.000 |
| 29 | Wall time | 45,021,134.000 |
| 30 | Average compute utilization | 40.267% |
| 30 | Average memory utilization | 83.379% |
| 30 | Average operation intensity | 3,183.497 |
| 30 | Comm time | 45,170,682.000 |
| 30 | Compute bound percentage | 26.074% |
| 30 | GPU time | 407,092.000 |
| 30 | Total compute-communication overlap | 298,984.000 |
| 30 | Wall time | 45,278,790.000 |
| 31 | Average compute utilization | 40.267% |
| 31 | Average memory utilization | 83.379% |
| 31 | Average operation intensity | 3,183.497 |
| 31 | Comm time | 45,260,503.000 |
| 31 | Compute bound percentage | 26.074% |
| 31 | GPU time | 407,092.000 |
| 31 | Total compute-communication overlap | 298,984.000 |
| 31 | Wall time | 45,368,611.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 26.541 us |
| Median FCT | 8.757 us |
| p95 FCT | 141.743 us |
| Maximum FCT | 577.964 us |
| Median standalone time | 7.614 us |
| Median FCT / standalone | 1.171x |
| p95 FCT / standalone | 3.233x |
| Maximum FCT / standalone | 10.359x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 KiB | 30,720 | 7.073 us | 10.456 us | 48.435 us | 6.574 us | 1.135x |
| 116.00 KiB | 14,336 | 16.452 us | 39.242 us | 66.346 us | 10.179 us | 1.782x |
| 1,000.00 KiB | 3,584 | 116.790 us | 261.932 us | 498.530 us | 48.126 us | 2.718x |
| 1.95 MiB | 1,536 | 218.409 us | 424.241 us | 577.964 us | 91.052 us | 2.600x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 4,698,057 |
| Observed queue interval | 5.900 us to 45.488 ms |
| Observed queue duration | 45.482 ms |
| Maximum sampled queue | 1.43 MiB |
| Maximum queue location | switch 39, port 2 |

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
| Trace records recognized | 245,277,696 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 4.751 us to 45.493 ms |
| Maximum sampled packet queue | 1.43 MiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 203.12 KiB |
| Events | Dequ: 82,255,872, Enqu: 80,765,952, Recv: 82,255,872 |
| Bytes by event | Dequ: 41.48 GiB, Enqu: 40.04 GiB, Recv: 41.48 GiB |
| Observed interface utilization | 165 interfaces; mean 23.737%, max 50.618% |
| Matched packet queue durations | 78,803,650 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 4.190 us |
| Maximum packet queue time | 59.401 us |
| Mean packet queue time | 670 ns |
| Unmatched/duplicate dequeues | 3,452,222 |
| Enqueue-key collisions | 1,962,302 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
