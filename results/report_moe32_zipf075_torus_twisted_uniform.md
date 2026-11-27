# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_zipf075_torus_twisted_uniform/attempts/20261124_172909_977059/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 40,345,279 |
| Fastest rank completion (cycles) | 40,137,194 |
| Maximum exposed communication (cycles) | 39,112,479 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 40.325 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 39,559,570.688 | 39,489,522.000 | 39,688,695.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 575,952.000 | 575,624.000 | 576,840.000 | 32 |
| Wall time | 40,206,386.688 | 40,137,194.000 | 40,345,279.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 39,492,297.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 40,171,969.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 39,495,150.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 40,174,822.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 39,501,432.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 40,181,104.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 39,504,328.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 40,184,000.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 39,677,071.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 576,216.000 |
| 4 | Wall time | 40,333,655.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 39,682,262.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 576,216.000 |
| 5 | Wall time | 40,338,846.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 39,683,134.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 576,216.000 |
| 6 | Wall time | 40,339,718.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 39,688,695.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 576,216.000 |
| 7 | Wall time | 40,345,279.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 39,492,414.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 575,976.000 |
| 8 | Wall time | 40,140,086.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 39,489,522.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 575,976.000 |
| 9 | Wall time | 40,137,194.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 39,493,117.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 575,976.000 |
| 10 | Wall time | 40,140,789.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 39,495,152.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 575,976.000 |
| 11 | Wall time | 40,142,824.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 39,556,689.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 40,199,529.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 39,548,351.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 40,191,191.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 39,547,900.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 40,190,740.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 39,547,400.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 40,190,240.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 39,562,203.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 40,201,907.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 39,556,449.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,752.000 |
| 17 | Wall time | 40,196,153.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 39,558,785.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,752.000 |
| 18 | Wall time | 40,198,489.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 39,554,547.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,752.000 |
| 19 | Wall time | 40,194,251.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 39,670,918.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 575,704.000 |
| 20 | Wall time | 40,308,430.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 39,667,067.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 575,704.000 |
| 21 | Wall time | 40,304,579.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 39,673,273.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 575,704.000 |
| 22 | Wall time | 40,310,785.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 39,664,955.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 575,704.000 |
| 23 | Wall time | 40,302,467.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 39,509,521.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 575,656.000 |
| 24 | Wall time | 40,145,417.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 39,511,393.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 575,656.000 |
| 25 | Wall time | 40,147,289.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 39,510,311.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 575,656.000 |
| 26 | Wall time | 40,146,207.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 39,507,754.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 575,656.000 |
| 27 | Wall time | 40,143,650.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 39,516,343.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 40,150,991.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 39,520,902.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 40,155,550.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 39,512,669.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 40,147,317.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 39,514,258.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 40,148,906.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 6.672 us |
| Median FCT | 5.262 us |
| p95 FCT | 11.655 us |
| Maximum FCT | 102.902 us |
| Median standalone time | 5.254 us |
| Median FCT / standalone | 0.999x |
| p95 FCT / standalone | 1.192x |
| Maximum FCT / standalone | 2.853x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 5.214 us | 6.030 us | 6.356 us | 5.203 us | 0.966x |
| 433.00 B | 2,048 | 6.126 us | 6.178 us | 6.534 us | 6.259 us | 0.980x |
| 490.00 B | 2,048 | 3.069 us | 3.085 us | 3.238 us | 3.141 us | 0.978x |
| 545.00 B | 2,048 | 5.125 us | 5.161 us | 5.297 us | 5.223 us | 0.982x |
| 568.00 B | 2,560 | 5.130 us | 5.162 us | 5.567 us | 5.224 us | 0.983x |
| 632.00 B | 2,048 | 3.087 us | 3.097 us | 3.453 us | 3.147 us | 0.982x |
| 683.00 B | 2,560 | 4.124 us | 4.150 us | 4.448 us | 4.189 us | 0.985x |
| 715.00 B | 2,560 | 6.192 us | 6.232 us | 6.618 us | 6.270 us | 0.989x |
| 760.00 B | 2,048 | 4.136 us | 4.148 us | 4.434 us | 4.192 us | 0.987x |
| 860.00 B | 2,048 | 3.114 us | 3.132 us | 3.222 us | 3.156 us | 0.988x |
| 872.00 B | 2,048 | 4.152 us | 4.171 us | 4.272 us | 4.196 us | 0.990x |
| 970.00 B | 2,560 | 4.168 us | 4.192 us | 4.501 us | 4.200 us | 0.993x |
| 997.00 B | 2,560 | 5.215 us | 5.242 us | 5.390 us | 5.241 us | 0.996x |
| 1,016.00 B | 4,416 | 3.195 us | 5.299 us | 5.361 us | 3.164 us | 1.003x |
| 1.07 KiB | 2,560 | 5.220 us | 5.295 us | 5.422 us | 5.247 us | 0.998x |
| 1.10 KiB | 4,416 | 3.203 us | 5.303 us | 5.344 us | 3.168 us | 1.004x |
| 1.23 KiB | 2,048 | 5.227 us | 5.268 us | 5.338 us | 5.254 us | 0.996x |
| 1.23 KiB | 1,920 | 3.184 us | 5.301 us | 5.313 us | 3.174 us | 1.001x |
| 1.23 KiB | 2,304 | 3.223 us | 5.340 us | 5.354 us | 3.174 us | 1.008x |
| 1.24 KiB | 2,560 | 3.174 us | 3.182 us | 3.247 us | 3.174 us | 0.996x |
| 1.36 KiB | 2,560 | 3.184 us | 3.201 us | 3.295 us | 3.179 us | 1.000x |
| 1.41 KiB | 4,800 | 3.229 us | 5.316 us | 5.367 us | 3.181 us | 1.005x |
| 1.49 KiB | 2,048 | 6.281 us | 6.346 us | 6.784 us | 6.305 us | 0.999x |
| 1.54 KiB | 2,048 | 4.238 us | 4.243 us | 4.511 us | 4.227 us | 0.999x |
| 1.67 KiB | 4,224 | 3.210 us | 5.327 us | 5.418 us | 3.192 us | 1.004x |
| 1.79 KiB | 2,048 | 4.248 us | 4.292 us | 4.339 us | 4.237 us | 1.001x |
| 2.07 KiB | 4,800 | 3.326 us | 5.426 us | 5.527 us | 3.210 us | 1.017x |
| 2.15 KiB | 2,048 | 3.250 us | 3.277 us | 3.537 us | 3.213 us | 1.007x |
| 2.74 KiB | 4,608 | 3.300 us | 5.386 us | 5.834 us | 3.238 us | 1.008x |
| 2.81 KiB | 4,416 | 3.206 us | 5.292 us | 5.624 us | 3.240 us | 0.995x |
| 3.05 KiB | 2,560 | 5.303 us | 5.451 us | 5.497 us | 5.332 us | 1.000x |
| 3.45 KiB | 2,048 | 4.400 us | 4.453 us | 4.685 us | 4.309 us | 1.015x |
| 4.00 KiB | 2,560 | 4.449 us | 4.504 us | 4.967 us | 4.333 us | 1.016x |
| 4.72 KiB | 1,920 | 3.287 us | 5.399 us | 5.510 us | 3.322 us | 0.994x |
| 4.72 KiB | 2,304 | 3.379 us | 5.535 us | 6.010 us | 3.322 us | 1.017x |
| 4.81 KiB | 2,048 | 5.423 us | 5.581 us | 6.374 us | 5.406 us | 1.011x |
| 6.14 KiB | 2,048 | 3.586 us | 3.702 us | 4.343 us | 3.385 us | 1.042x |
| 8.83 KiB | 2,560 | 6.620 us | 7.001 us | 7.868 us | 6.621 us | 1.018x |
| 16.00 KiB | 28,672 | 6.890 us | 7.619 us | 11.332 us | 5.888 us | 1.035x |
| 128.00 KiB | 30,720 | 9.457 us | 19.996 us | 26.662 us | 8.616 us | 1.217x |
| 1.95 MiB | 1,536 | 91.301 us | 95.526 us | 102.902 us | 88.972 us | 1.031x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,524,474 |
| Observed queue interval | 148.100 us to 40.320 ms |
| Observed queue duration | 40.172 ms |
| Maximum sampled queue | 50.61 KiB |
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
| Trace records recognized | 131,884,400 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 40.324 ms |
| Maximum sampled packet queue | 50.01 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 152.34 KiB |
| Events | Dequ: 44,387,936, Enqu: 43,108,528, Recv: 44,387,936 |
| Bytes by event | Dequ: 22.06 GiB, Enqu: 20.84 GiB, Recv: 22.06 GiB |
| Observed interface utilization | 165 interfaces; mean 14.240%, max 27.320% |
| Matched packet queue durations | 42,882,401 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 76 ns |
| Maximum packet queue time | 2.043 us |
| Mean packet queue time | 18 ns |
| Unmatched/duplicate dequeues | 1,505,535 |
| Enqueue-key collisions | 226,127 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
