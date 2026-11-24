# ASTRA-sim NS-3 Results Report

Result directory: `astra-sim/extern/network_backend/ns-3/scratch/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 45,543,995 |
| Fastest rank completion (cycles) | 45,285,356 |
| Maximum exposed communication (cycles) | 44,325,307 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 45.524 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 44,724,790.531 | 44,630,765.000 | 44,901,155.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 575,952.000 | 575,624.000 | 576,840.000 | 32 |
| Wall time | 45,371,606.531 | 45,285,356.000 | 45,543,995.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 44,635,138.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 45,314,810.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 44,636,991.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 45,316,663.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 44,633,921.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 45,313,593.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 44,630,765.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 45,310,437.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 44,655,558.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 576,216.000 |
| 4 | Wall time | 45,312,142.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 44,647,464.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 576,216.000 |
| 5 | Wall time | 45,304,048.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 44,651,279.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 576,216.000 |
| 6 | Wall time | 45,307,863.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 44,653,826.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 576,216.000 |
| 7 | Wall time | 45,310,410.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 44,854,789.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 575,976.000 |
| 8 | Wall time | 45,502,461.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 44,858,323.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 575,976.000 |
| 9 | Wall time | 45,505,995.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 44,838,695.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 575,976.000 |
| 10 | Wall time | 45,486,367.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 44,845,801.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 575,976.000 |
| 11 | Wall time | 45,493,473.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 44,888,447.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 45,531,287.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 44,889,854.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 45,532,694.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 44,889,567.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 45,532,407.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 44,901,155.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 45,543,995.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 44,712,608.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 45,352,312.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 44,716,408.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,752.000 |
| 17 | Wall time | 45,356,112.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 44,718,484.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,752.000 |
| 18 | Wall time | 45,358,188.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 44,713,396.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,752.000 |
| 19 | Wall time | 45,353,100.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 44,735,747.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 575,704.000 |
| 20 | Wall time | 45,373,259.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 44,739,077.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 575,704.000 |
| 21 | Wall time | 45,376,589.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 44,738,075.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 575,704.000 |
| 22 | Wall time | 45,375,587.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 44,728,883.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 575,704.000 |
| 23 | Wall time | 45,366,395.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 44,657,348.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 575,656.000 |
| 24 | Wall time | 45,293,244.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 44,658,914.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 575,656.000 |
| 25 | Wall time | 45,294,810.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 44,649,460.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 575,656.000 |
| 26 | Wall time | 45,285,356.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 44,652,729.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 575,656.000 |
| 27 | Wall time | 45,288,625.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 44,664,623.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 45,299,271.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 44,668,567.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 45,303,215.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 44,662,119.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 45,296,767.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 44,665,286.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 45,299,934.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 7.499 us |
| Median FCT | 7.035 us |
| p95 FCT | 12.467 us |
| Maximum FCT | 128.914 us |
| Median standalone time | 6.928 us |
| Median FCT / standalone | 1.001x |
| p95 FCT / standalone | 1.230x |
| Maximum FCT / standalone | 2.872x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 6.522 us | 7.035 us | 7.514 us | 6.243 us | 0.966x |
| 433.00 B | 2,048 | 6.126 us | 6.182 us | 6.510 us | 6.259 us | 0.980x |
| 490.00 B | 2,048 | 3.069 us | 3.070 us | 3.385 us | 3.141 us | 0.978x |
| 545.00 B | 2,048 | 7.175 us | 7.212 us | 7.710 us | 7.303 us | 0.983x |
| 568.00 B | 2,560 | 7.182 us | 7.221 us | 7.623 us | 7.304 us | 0.984x |
| 632.00 B | 2,048 | 3.087 us | 3.094 us | 3.415 us | 3.147 us | 0.982x |
| 683.00 B | 2,560 | 4.124 us | 4.138 us | 4.497 us | 4.189 us | 0.985x |
| 715.00 B | 2,560 | 6.192 us | 6.244 us | 7.000 us | 6.270 us | 0.989x |
| 760.00 B | 2,048 | 8.272 us | 8.302 us | 8.711 us | 8.352 us | 0.991x |
| 860.00 B | 2,048 | 3.114 us | 3.130 us | 3.219 us | 3.156 us | 0.987x |
| 872.00 B | 2,048 | 8.304 us | 8.340 us | 8.542 us | 8.356 us | 0.994x |
| 970.00 B | 2,560 | 4.168 us | 4.199 us | 4.329 us | 4.200 us | 0.994x |
| 997.00 B | 2,560 | 7.301 us | 7.343 us | 7.499 us | 7.321 us | 0.998x |
| 1,016.00 B | 4,416 | 3.187 us | 5.291 us | 5.378 us | 3.164 us | 1.002x |
| 1.07 KiB | 2,560 | 7.306 us | 7.350 us | 7.909 us | 7.327 us | 0.998x |
| 1.10 KiB | 4,416 | 3.199 us | 5.299 us | 5.344 us | 3.168 us | 1.002x |
| 1.23 KiB | 2,048 | 3.174 us | 3.182 us | 3.242 us | 3.174 us | 0.996x |
| 1.23 KiB | 1,920 | 3.182 us | 5.299 us | 5.342 us | 3.174 us | 0.999x |
| 1.23 KiB | 2,304 | 3.223 us | 5.311 us | 5.354 us | 3.174 us | 1.005x |
| 1.24 KiB | 2,560 | 3.174 us | 3.182 us | 3.228 us | 3.174 us | 0.997x |
| 1.36 KiB | 2,560 | 7.318 us | 7.389 us | 7.950 us | 7.339 us | 0.999x |
| 1.41 KiB | 4,800 | 3.220 us | 5.316 us | 5.375 us | 3.181 us | 1.004x |
| 1.49 KiB | 2,048 | 6.281 us | 6.365 us | 6.792 us | 6.305 us | 1.000x |
| 1.54 KiB | 2,048 | 4.197 us | 4.243 us | 4.421 us | 4.227 us | 0.996x |
| 1.67 KiB | 4,224 | 3.200 us | 5.317 us | 5.418 us | 3.192 us | 1.001x |
| 1.79 KiB | 2,048 | 8.379 us | 8.471 us | 8.583 us | 8.397 us | 1.001x |
| 2.07 KiB | 4,800 | 3.322 us | 5.422 us | 5.508 us | 3.210 us | 1.014x |
| 2.15 KiB | 2,048 | 3.250 us | 3.329 us | 3.496 us | 3.213 us | 1.009x |
| 2.74 KiB | 4,608 | 7.378 us | 7.540 us | 8.282 us | 7.398 us | 1.003x |
| 2.81 KiB | 4,416 | 3.206 us | 5.292 us | 5.606 us | 3.240 us | 0.995x |
| 3.05 KiB | 2,560 | 3.326 us | 3.346 us | 3.456 us | 3.252 us | 1.014x |
| 3.45 KiB | 2,048 | 8.490 us | 8.631 us | 8.807 us | 8.469 us | 1.005x |
| 4.00 KiB | 2,560 | 4.421 us | 4.483 us | 4.911 us | 4.333 us | 1.013x |
| 4.72 KiB | 1,920 | 3.287 us | 5.392 us | 5.535 us | 3.322 us | 0.994x |
| 4.72 KiB | 2,304 | 3.359 us | 5.527 us | 5.930 us | 3.322 us | 1.013x |
| 4.81 KiB | 2,048 | 7.543 us | 7.812 us | 8.609 us | 7.486 us | 1.013x |
| 6.14 KiB | 2,048 | 3.586 us | 3.609 us | 4.291 us | 3.385 us | 1.041x |
| 8.83 KiB | 2,560 | 6.771 us | 7.292 us | 8.536 us | 6.621 us | 1.030x |
| 16.00 KiB | 28,672 | 7.943 us | 9.005 us | 11.856 us | 6.928 us | 1.053x |
| 128.00 KiB | 30,720 | 9.460 us | 20.906 us | 26.691 us | 8.616 us | 1.246x |
| 1.95 MiB | 1,536 | 91.572 us | 98.382 us | 128.914 us | 88.972 us | 1.039x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,612,762 |
| Observed queue interval | 184.200 us to 45.520 ms |
| Observed queue duration | 45.336 ms |
| Maximum sampled queue | 50.20 KiB |
| Maximum queue location | switch 42, port 3 |

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
| Trace records recognized | 136,520,048 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 45.523 ms |
| Maximum sampled packet queue | 50.20 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 203.12 KiB |
| Events | Dequ: 45,933,152, Enqu: 44,653,744, Recv: 45,933,152 |
| Bytes by event | Dequ: 22.79 GiB, Enqu: 21.57 GiB, Recv: 22.79 GiB |
| Observed interface utilization | 165 interfaces; mean 13.029%, max 25.770% |
| Matched packet queue durations | 44,376,385 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 84 ns |
| Maximum packet queue time | 2.043 us |
| Mean packet queue time | 19 ns |
| Unmatched/duplicate dequeues | 1,556,767 |
| Enqueue-key collisions | 277,359 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
