# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/torus_sweep_20261124_134236_443048/moe32_zipf075_torus_base_hostlink/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 40,512,361 |
| Fastest rank completion (cycles) | 40,309,159 |
| Maximum exposed communication (cycles) | 39,299,145 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 40.492 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 39,742,585.625 | 39,662,160.000 | 39,874,849.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 575,952.000 | 575,624.000 | 576,840.000 | 32 |
| Wall time | 40,389,401.625 | 40,309,159.000 | 40,512,361.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 39,764,286.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 40,443,958.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 39,763,139.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 40,442,811.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 39,753,121.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 40,432,793.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 39,758,432.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 40,438,104.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 39,802,949.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 576,216.000 |
| 4 | Wall time | 40,459,533.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 39,805,226.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 576,216.000 |
| 5 | Wall time | 40,461,810.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 39,807,534.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 576,216.000 |
| 6 | Wall time | 40,464,118.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 39,802,277.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 576,216.000 |
| 7 | Wall time | 40,458,861.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 39,664,935.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 575,976.000 |
| 8 | Wall time | 40,312,607.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 39,665,080.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 575,976.000 |
| 9 | Wall time | 40,312,752.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 39,664,574.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 575,976.000 |
| 10 | Wall time | 40,312,246.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 39,662,160.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 575,976.000 |
| 11 | Wall time | 40,309,832.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 39,674,420.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 40,317,260.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 39,674,307.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 40,317,147.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 39,674,308.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 40,317,148.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 39,674,608.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 40,317,448.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 39,808,067.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 40,447,771.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 39,809,480.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,752.000 |
| 17 | Wall time | 40,449,184.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 39,821,098.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,752.000 |
| 18 | Wall time | 40,460,802.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 39,826,809.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,752.000 |
| 19 | Wall time | 40,466,513.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 39,874,117.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 575,704.000 |
| 20 | Wall time | 40,511,629.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 39,874,849.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 575,704.000 |
| 21 | Wall time | 40,512,361.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 39,862,359.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 575,704.000 |
| 22 | Wall time | 40,499,871.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 39,870,495.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 575,704.000 |
| 23 | Wall time | 40,508,007.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 39,673,263.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 575,656.000 |
| 24 | Wall time | 40,309,159.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 39,674,309.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 575,656.000 |
| 25 | Wall time | 40,310,205.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 39,674,471.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 575,656.000 |
| 26 | Wall time | 40,310,367.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 39,674,275.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 575,656.000 |
| 27 | Wall time | 40,310,171.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 39,678,391.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 40,313,039.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 39,675,869.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 40,310,517.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 39,676,661.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 40,311,309.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 39,676,871.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 40,311,519.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 5.801 us |
| Median FCT | 5.039 us |
| p95 FCT | 12.370 us |
| Maximum FCT | 312.933 us |
| Median standalone time | 4.932 us |
| Median FCT / standalone | 1.007x |
| p95 FCT / standalone | 1.623x |
| Maximum FCT / standalone | 3.598x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 4.149 us | 5.039 us | 5.146 us | 4.247 us | 0.952x |
| 433.00 B | 2,048 | 4.130 us | 4.204 us | 4.708 us | 4.263 us | 0.971x |
| 490.00 B | 2,048 | 1.073 us | 1.087 us | 1.330 us | 1.145 us | 0.939x |
| 545.00 B | 2,048 | 5.179 us | 5.253 us | 6.411 us | 5.307 us | 0.978x |
| 568.00 B | 2,560 | 5.186 us | 5.252 us | 9.038 us | 5.308 us | 0.980x |
| 632.00 B | 2,048 | 1.091 us | 1.100 us | 1.263 us | 1.151 us | 0.951x |
| 683.00 B | 2,560 | 2.128 us | 2.151 us | 2.269 us | 2.193 us | 0.972x |
| 715.00 B | 2,560 | 4.196 us | 4.257 us | 4.820 us | 4.274 us | 0.984x |
| 760.00 B | 2,048 | 6.276 us | 6.313 us | 6.639 us | 6.356 us | 0.988x |
| 860.00 B | 2,048 | 1.118 us | 1.134 us | 1.236 us | 1.160 us | 0.966x |
| 872.00 B | 2,048 | 6.308 us | 6.342 us | 9.674 us | 6.360 us | 0.993x |
| 970.00 B | 2,560 | 2.172 us | 2.210 us | 2.440 us | 2.204 us | 0.988x |
| 997.00 B | 2,560 | 5.305 us | 5.347 us | 6.587 us | 5.325 us | 0.998x |
| 1,016.00 B | 4,416 | 1.217 us | 3.318 us | 3.344 us | 1.168 us | 1.020x |
| 1.07 KiB | 2,560 | 5.310 us | 5.351 us | 6.161 us | 5.331 us | 0.998x |
| 1.10 KiB | 4,416 | 1.221 us | 3.330 us | 3.465 us | 1.172 us | 1.022x |
| 1.23 KiB | 2,048 | 1.145 us | 1.186 us | 1.287 us | 1.178 us | 0.981x |
| 1.23 KiB | 1,920 | 1.220 us | 3.313 us | 3.317 us | 1.178 us | 1.011x |
| 1.23 KiB | 2,304 | 1.258 us | 3.354 us | 3.386 us | 1.178 us | 1.029x |
| 1.24 KiB | 2,560 | 1.178 us | 1.186 us | 1.232 us | 1.178 us | 0.997x |
| 1.36 KiB | 2,560 | 5.322 us | 5.397 us | 6.493 us | 5.343 us | 0.999x |
| 1.41 KiB | 4,800 | 1.234 us | 3.353 us | 3.412 us | 1.185 us | 1.021x |
| 1.49 KiB | 2,048 | 4.285 us | 4.391 us | 4.844 us | 4.309 us | 1.000x |
| 1.54 KiB | 2,048 | 2.201 us | 2.251 us | 2.526 us | 2.231 us | 0.994x |
| 1.67 KiB | 4,224 | 1.232 us | 3.341 us | 3.422 us | 1.196 us | 1.018x |
| 1.79 KiB | 2,048 | 6.383 us | 6.470 us | 6.581 us | 6.401 us | 1.000x |
| 2.07 KiB | 4,800 | 1.344 us | 3.490 us | 3.512 us | 1.214 us | 1.064x |
| 2.15 KiB | 2,048 | 1.254 us | 1.333 us | 1.839 us | 1.217 us | 1.034x |
| 2.74 KiB | 4,608 | 5.385 us | 5.544 us | 6.371 us | 5.402 us | 1.005x |
| 2.81 KiB | 4,416 | 1.210 us | 3.300 us | 3.610 us | 1.244 us | 0.993x |
| 3.05 KiB | 2,560 | 1.330 us | 1.402 us | 1.693 us | 1.256 us | 1.057x |
| 3.45 KiB | 2,048 | 6.489 us | 6.626 us | 7.010 us | 6.473 us | 1.005x |
| 4.00 KiB | 2,560 | 2.388 us | 2.500 us | 2.767 us | 2.337 us | 1.024x |
| 4.72 KiB | 1,920 | 1.322 us | 3.485 us | 3.623 us | 1.326 us | 1.001x |
| 4.72 KiB | 2,304 | 1.455 us | 3.705 us | 3.934 us | 1.326 us | 1.065x |
| 4.81 KiB | 2,048 | 5.538 us | 5.854 us | 6.821 us | 5.490 us | 1.016x |
| 6.14 KiB | 2,048 | 1.590 us | 1.804 us | 2.408 us | 1.389 us | 1.125x |
| 8.83 KiB | 2,560 | 4.800 us | 5.355 us | 6.359 us | 4.625 us | 1.050x |
| 16.00 KiB | 28,672 | 5.977 us | 7.252 us | 10.095 us | 4.932 us | 1.094x |
| 128.00 KiB | 30,720 | 8.843 us | 19.765 us | 24.692 us | 6.620 us | 1.419x |
| 1.95 MiB | 1,536 | 91.136 us | 222.893 us | 312.933 us | 86.976 us | 1.228x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,400,348 |
| Observed queue interval | 128.100 us to 40.489 ms |
| Observed queue duration | 40.361 ms |
| Maximum sampled queue | 91.17 KiB |
| Maximum queue location | switch 57, port 3 |

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
| Packet trace interval | 10 ns to 40.492 ms |
| Maximum sampled packet queue | 91.12 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 154.39 KiB |
| Events | Dequ: 45,933,152, Enqu: 44,653,744, Recv: 45,933,152 |
| Bytes by event | Dequ: 22.79 GiB, Enqu: 21.57 GiB, Recv: 22.79 GiB |
| Observed interface utilization | 165 interfaces; mean 14.648%, max 28.972% |
| Matched packet queue durations | 44,329,366 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 52 ns |
| Maximum packet queue time | 3.689 us |
| Mean packet queue time | 23 ns |
| Unmatched/duplicate dequeues | 1,603,786 |
| Enqueue-key collisions | 324,378 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
