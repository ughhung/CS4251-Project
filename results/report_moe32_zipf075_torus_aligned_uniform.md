# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_zipf075_torus_aligned_uniform/attempts/20261124_172909_977059/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 44,787,160 |
| Fastest rank completion (cycles) | 44,373,061 |
| Maximum exposed communication (cycles) | 43,572,978 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 44.767 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 43,935,352.594 | 43,730,221.000 | 44,148,602.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 575,952.000 | 575,624.000 | 576,840.000 | 32 |
| Wall time | 44,582,168.594 | 44,373,061.000 | 44,787,160.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 44,107,488.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 44,787,160.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 44,081,962.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 44,761,634.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 44,077,619.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 44,757,291.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 44,101,681.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 44,781,353.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 44,129,877.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 576,216.000 |
| 4 | Wall time | 44,786,461.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 44,104,351.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 576,216.000 |
| 5 | Wall time | 44,760,935.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 44,100,008.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 576,216.000 |
| 6 | Wall time | 44,756,592.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 44,124,070.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 576,216.000 |
| 7 | Wall time | 44,780,654.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 43,742,544.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 575,976.000 |
| 8 | Wall time | 44,390,216.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 43,740,669.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 575,976.000 |
| 9 | Wall time | 44,388,341.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 43,735,801.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 575,976.000 |
| 10 | Wall time | 44,383,473.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 43,737,315.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 575,976.000 |
| 11 | Wall time | 44,384,987.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 43,734,348.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 44,377,188.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 43,737,022.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 44,379,862.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 43,739,795.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 44,382,635.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 43,730,221.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 44,373,061.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 43,759,551.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 44,399,255.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 43,758,474.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,752.000 |
| 17 | Wall time | 44,398,178.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 43,758,822.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,752.000 |
| 18 | Wall time | 44,398,526.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 43,753,252.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,752.000 |
| 19 | Wall time | 44,392,956.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 43,788,903.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 575,704.000 |
| 20 | Wall time | 44,426,415.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 43,776,963.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 575,704.000 |
| 21 | Wall time | 44,414,475.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 43,782,093.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 575,704.000 |
| 22 | Wall time | 44,419,605.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 43,786,130.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 575,704.000 |
| 23 | Wall time | 44,423,642.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 44,142,580.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 575,656.000 |
| 24 | Wall time | 44,778,476.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 44,117,054.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 575,656.000 |
| 25 | Wall time | 44,752,950.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 44,112,711.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 575,656.000 |
| 26 | Wall time | 44,748,607.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 44,136,773.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 575,656.000 |
| 27 | Wall time | 44,772,669.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 44,148,602.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 44,783,250.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 44,123,076.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 44,757,724.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 44,118,733.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 44,753,381.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 44,142,795.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 44,777,443.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 6.581 us |
| Median FCT | 4.390 us |
| p95 FCT | 13.692 us |
| Maximum FCT | 330.289 us |
| Median standalone time | 3.808 us |
| Median FCT / standalone | 1.003x |
| p95 FCT / standalone | 1.616x |
| Maximum FCT / standalone | 3.712x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 3.015 us | 3.015 us | 3.015 us | 3.123 us | 0.965x |
| 433.00 B | 2,048 | 3.063 us | 3.105 us | 3.425 us | 3.139 us | 0.978x |
| 490.00 B | 2,048 | 4.092 us | 4.107 us | 4.317 us | 4.181 us | 0.979x |
| 545.00 B | 2,048 | 3.075 us | 3.102 us | 3.775 us | 3.143 us | 0.980x |
| 568.00 B | 2,560 | 5.130 us | 5.148 us | 6.840 us | 5.224 us | 0.983x |
| 632.00 B | 2,048 | 4.116 us | 4.130 us | 4.686 us | 4.187 us | 0.984x |
| 683.00 B | 2,560 | 6.186 us | 6.254 us | 8.756 us | 6.269 us | 0.988x |
| 715.00 B | 2,560 | 3.096 us | 3.124 us | 3.583 us | 3.150 us | 0.984x |
| 760.00 B | 2,048 | 5.170 us | 5.194 us | 6.978 us | 5.232 us | 0.989x |
| 860.00 B | 2,048 | 4.152 us | 4.185 us | 4.211 us | 4.196 us | 0.991x |
| 872.00 B | 2,048 | 5.190 us | 5.224 us | 9.090 us | 5.236 us | 0.993x |
| 970.00 B | 2,560 | 6.252 us | 6.294 us | 6.584 us | 6.280 us | 0.997x |
| 997.00 B | 2,560 | 3.129 us | 3.171 us | 3.184 us | 3.161 us | 0.992x |
| 1,016.00 B | 4,416 | 3.164 us | 3.246 us | 3.273 us | 3.164 us | 1.002x |
| 1.07 KiB | 2,560 | 5.246 us | 5.313 us | 5.350 us | 5.247 us | 1.001x |
| 1.10 KiB | 4,416 | 3.172 us | 3.254 us | 3.275 us | 3.168 us | 1.002x |
| 1.23 KiB | 2,048 | 4.184 us | 4.224 us | 4.339 us | 4.214 us | 0.994x |
| 1.23 KiB | 1,920 | 3.141 us | 3.223 us | 3.227 us | 3.174 us | 0.999x |
| 1.23 KiB | 2,304 | 3.182 us | 3.264 us | 3.268 us | 3.174 us | 1.004x |
| 1.24 KiB | 2,560 | 4.217 us | 4.225 us | 4.320 us | 4.214 us | 1.000x |
| 1.36 KiB | 2,560 | 5.232 us | 5.277 us | 5.368 us | 5.259 us | 0.997x |
| 1.41 KiB | 4,800 | 3.189 us | 3.271 us | 3.289 us | 3.181 us | 1.003x |
| 1.49 KiB | 2,048 | 3.193 us | 3.219 us | 3.464 us | 3.185 us | 1.002x |
| 1.54 KiB | 2,048 | 6.283 us | 6.338 us | 6.918 us | 6.307 us | 0.999x |
| 1.67 KiB | 4,224 | 3.200 us | 3.282 us | 3.332 us | 3.192 us | 1.001x |
| 1.79 KiB | 2,048 | 5.291 us | 5.327 us | 5.405 us | 5.277 us | 1.002x |
| 2.07 KiB | 4,800 | 3.254 us | 3.414 us | 3.441 us | 3.210 us | 1.015x |
| 2.15 KiB | 2,048 | 4.293 us | 4.366 us | 4.775 us | 4.253 us | 1.009x |
| 2.74 KiB | 4,608 | 3.204 us | 3.322 us | 4.578 us | 3.238 us | 1.004x |
| 2.81 KiB | 4,416 | 3.206 us | 3.314 us | 3.520 us | 3.240 us | 0.994x |
| 3.05 KiB | 2,560 | 4.262 us | 4.383 us | 4.473 us | 4.292 us | 1.005x |
| 3.45 KiB | 2,048 | 5.443 us | 5.552 us | 5.675 us | 5.349 us | 1.016x |
| 4.00 KiB | 2,560 | 6.468 us | 6.579 us | 7.048 us | 6.413 us | 1.009x |
| 4.72 KiB | 1,920 | 3.287 us | 3.328 us | 3.407 us | 3.322 us | 0.991x |
| 4.72 KiB | 2,304 | 3.287 us | 3.666 us | 3.912 us | 3.322 us | 1.013x |
| 4.81 KiB | 2,048 | 5.385 us | 5.703 us | 7.094 us | 5.406 us | 1.012x |
| 6.14 KiB | 2,048 | 4.629 us | 4.818 us | 5.712 us | 4.425 us | 1.032x |
| 8.83 KiB | 2,560 | 3.812 us | 3.863 us | 4.750 us | 3.501 us | 1.075x |
| 16.00 KiB | 28,672 | 5.729 us | 6.262 us | 11.056 us | 3.808 us | 1.426x |
| 128.00 KiB | 30,720 | 8.787 us | 24.494 us | 25.663 us | 8.616 us | 1.358x |
| 1.95 MiB | 1,536 | 92.608 us | 274.490 us | 330.289 us | 88.972 us | 1.354x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 998,489 |
| Observed queue interval | 89.200 us to 44.764 ms |
| Observed queue duration | 44.675 ms |
| Maximum sampled queue | 132.06 KiB |
| Maximum queue location | switch 50, port 1 |

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
| Trace records recognized | 103,011,440 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 44.767 ms |
| Maximum sampled packet queue | 132.25 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 203.12 KiB |
| Events | Dequ: 34,763,616, Enqu: 33,484,208, Recv: 34,763,616 |
| Bytes by event | Dequ: 17.29 GiB, Enqu: 16.07 GiB, Recv: 17.29 GiB |
| Observed interface utilization | 165 interfaces; mean 10.055%, max 24.609% |
| Matched packet queue durations | 33,374,425 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 74 ns |
| Maximum packet queue time | 5.324 us |
| Mean packet queue time | 23 ns |
| Unmatched/duplicate dequeues | 1,389,191 |
| Enqueue-key collisions | 109,783 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
