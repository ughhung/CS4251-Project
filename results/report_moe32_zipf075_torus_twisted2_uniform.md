# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_zipf075_torus_twisted2_uniform/attempts/20261127_134159_646329/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 44,425,264 |
| Fastest rank completion (cycles) | 44,240,404 |
| Maximum exposed communication (cycles) | 43,168,752 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 44.405 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 43,680,533.531 | 43,604,508.000 | 43,745,592.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 575,952.000 | 575,624.000 | 576,840.000 | 32 |
| Wall time | 44,327,349.531 | 44,240,404.000 | 44,425,264.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 43,745,592.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 44,425,264.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 43,726,855.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 44,406,527.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 43,733,886.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 44,413,558.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 43,738,763.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 44,418,435.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 43,648,897.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 576,216.000 |
| 4 | Wall time | 44,305,481.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 43,654,978.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 576,216.000 |
| 5 | Wall time | 44,311,562.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 43,658,366.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 576,216.000 |
| 6 | Wall time | 44,314,950.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 43,646,415.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 576,216.000 |
| 7 | Wall time | 44,302,999.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 43,646,876.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 575,976.000 |
| 8 | Wall time | 44,294,548.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 43,649,822.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 575,976.000 |
| 9 | Wall time | 44,297,494.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 43,650,409.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 575,976.000 |
| 10 | Wall time | 44,298,081.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 43,637,868.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 575,976.000 |
| 11 | Wall time | 44,285,540.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 43,627,953.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 44,270,793.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 43,623,534.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 44,266,374.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 43,621,166.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 44,264,006.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 43,624,733.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 44,267,573.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 43,721,851.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 44,361,555.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 43,723,868.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,752.000 |
| 17 | Wall time | 44,363,572.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 43,714,331.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,752.000 |
| 18 | Wall time | 44,354,035.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 43,713,803.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,752.000 |
| 19 | Wall time | 44,353,507.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 43,735,528.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 575,704.000 |
| 20 | Wall time | 44,373,040.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 43,722,541.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 575,704.000 |
| 21 | Wall time | 44,360,053.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 43,720,994.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 575,704.000 |
| 22 | Wall time | 44,358,506.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 43,727,223.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 575,704.000 |
| 23 | Wall time | 44,364,735.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 43,607,762.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 575,656.000 |
| 24 | Wall time | 44,243,658.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 43,604,508.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 575,656.000 |
| 25 | Wall time | 44,240,404.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 43,607,591.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 575,656.000 |
| 26 | Wall time | 44,243,487.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 43,609,350.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 575,656.000 |
| 27 | Wall time | 44,245,246.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 43,738,082.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 44,372,730.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 43,725,445.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 44,360,093.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 43,728,933.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 44,363,581.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 43,739,150.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 44,373,798.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 7.296 us |
| Median FCT | 6.228 us |
| p95 FCT | 11.852 us |
| Maximum FCT | 103.852 us |
| Median standalone time | 6.276 us |
| Median FCT / standalone | 1.001x |
| p95 FCT / standalone | 1.202x |
| Maximum FCT / standalone | 2.856x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 6.030 us | 7.035 us | 7.619 us | 6.243 us | 0.966x |
| 433.00 B | 2,048 | 6.126 us | 6.169 us | 6.633 us | 6.259 us | 0.980x |
| 490.00 B | 2,048 | 3.069 us | 3.070 us | 3.233 us | 3.141 us | 0.978x |
| 545.00 B | 2,048 | 7.175 us | 7.228 us | 7.828 us | 7.303 us | 0.984x |
| 568.00 B | 2,560 | 7.182 us | 7.230 us | 7.651 us | 7.304 us | 0.984x |
| 632.00 B | 2,048 | 3.087 us | 3.094 us | 3.234 us | 3.147 us | 0.982x |
| 683.00 B | 2,560 | 4.124 us | 4.145 us | 4.261 us | 4.189 us | 0.985x |
| 715.00 B | 2,560 | 6.192 us | 6.236 us | 6.861 us | 6.270 us | 0.989x |
| 760.00 B | 2,048 | 6.204 us | 6.216 us | 6.293 us | 6.272 us | 0.990x |
| 860.00 B | 2,048 | 3.114 us | 3.132 us | 3.206 us | 3.156 us | 0.987x |
| 872.00 B | 2,048 | 6.228 us | 6.251 us | 6.306 us | 6.276 us | 0.993x |
| 970.00 B | 2,560 | 4.168 us | 4.188 us | 4.393 us | 4.200 us | 0.993x |
| 997.00 B | 2,560 | 7.301 us | 7.337 us | 7.872 us | 7.321 us | 0.998x |
| 1,016.00 B | 4,416 | 3.195 us | 5.299 us | 5.340 us | 3.164 us | 1.003x |
| 1.07 KiB | 2,560 | 7.306 us | 7.342 us | 7.920 us | 7.327 us | 0.998x |
| 1.10 KiB | 4,416 | 3.209 us | 5.303 us | 5.344 us | 3.168 us | 1.004x |
| 1.23 KiB | 2,048 | 5.227 us | 5.260 us | 5.385 us | 5.254 us | 0.996x |
| 1.23 KiB | 1,920 | 3.184 us | 5.301 us | 5.313 us | 3.174 us | 1.001x |
| 1.23 KiB | 2,304 | 3.223 us | 5.342 us | 5.369 us | 3.174 us | 1.008x |
| 1.24 KiB | 2,560 | 3.174 us | 3.182 us | 3.253 us | 3.174 us | 0.997x |
| 1.36 KiB | 2,560 | 5.232 us | 5.273 us | 5.628 us | 5.259 us | 0.997x |
| 1.41 KiB | 4,800 | 3.226 us | 5.316 us | 5.379 us | 3.181 us | 1.005x |
| 1.49 KiB | 2,048 | 6.281 us | 6.353 us | 6.810 us | 6.305 us | 0.999x |
| 1.54 KiB | 2,048 | 4.238 us | 4.243 us | 4.362 us | 4.227 us | 0.999x |
| 1.67 KiB | 4,224 | 3.202 us | 5.327 us | 5.422 us | 3.192 us | 1.003x |
| 1.79 KiB | 2,048 | 6.334 us | 6.381 us | 6.674 us | 6.317 us | 1.002x |
| 2.07 KiB | 4,800 | 3.323 us | 5.426 us | 5.527 us | 3.210 us | 1.017x |
| 2.15 KiB | 2,048 | 3.250 us | 3.323 us | 3.523 us | 3.213 us | 1.008x |
| 2.74 KiB | 4,608 | 5.386 us | 7.472 us | 8.248 us | 5.318 us | 1.004x |
| 2.81 KiB | 4,416 | 3.206 us | 5.294 us | 5.606 us | 3.240 us | 0.996x |
| 3.05 KiB | 2,560 | 5.303 us | 5.412 us | 5.572 us | 5.332 us | 0.999x |
| 3.45 KiB | 2,048 | 6.445 us | 6.548 us | 6.710 us | 6.389 us | 1.007x |
| 4.00 KiB | 2,560 | 4.449 us | 4.500 us | 4.790 us | 4.333 us | 1.018x |
| 4.72 KiB | 1,920 | 3.287 us | 5.379 us | 5.518 us | 3.322 us | 0.993x |
| 4.72 KiB | 2,304 | 3.369 us | 5.562 us | 6.002 us | 3.322 us | 1.016x |
| 4.81 KiB | 2,048 | 7.569 us | 7.819 us | 8.527 us | 7.486 us | 1.013x |
| 6.14 KiB | 2,048 | 3.586 us | 3.599 us | 4.177 us | 3.385 us | 1.039x |
| 8.83 KiB | 2,560 | 6.835 us | 7.330 us | 8.126 us | 6.621 us | 1.034x |
| 16.00 KiB | 28,672 | 7.490 us | 8.786 us | 12.046 us | 6.928 us | 1.046x |
| 128.00 KiB | 30,720 | 9.472 us | 20.910 us | 26.677 us | 8.616 us | 1.232x |
| 1.95 MiB | 1,536 | 91.495 us | 96.600 us | 103.852 us | 88.972 us | 1.034x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,577,804 |
| Observed queue interval | 176.200 us to 44.402 ms |
| Observed queue duration | 44.225 ms |
| Maximum sampled queue | 62.54 KiB |
| Maximum queue location | switch 60, port 4 |

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
| Trace records recognized | 135,589,232 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 44.405 ms |
| Maximum sampled packet queue | 62.54 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 177.73 KiB |
| Events | Dequ: 45,622,880, Enqu: 44,343,472, Recv: 45,622,880 |
| Bytes by event | Dequ: 22.64 GiB, Enqu: 21.42 GiB, Recv: 22.64 GiB |
| Observed interface utilization | 165 interfaces; mean 13.270%, max 26.649% |
| Matched packet queue durations | 44,086,251 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 80 ns |
| Maximum packet queue time | 2.556 us |
| Mean packet queue time | 19 ns |
| Unmatched/duplicate dequeues | 1,536,629 |
| Enqueue-key collisions | 257,221 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
