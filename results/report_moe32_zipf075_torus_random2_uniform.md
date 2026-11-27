# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_zipf075_torus_random2_uniform/attempts/20261126_030556_566401/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 66,746,836 |
| Fastest rank completion (cycles) | 64,448,567 |
| Maximum exposed communication (cycles) | 65,514,036 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 66.726 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 65,258,628.375 | 63,768,895.000 | 66,090,252.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 575,952.000 | 575,624.000 | 576,840.000 | 32 |
| Wall time | 65,905,444.375 | 64,448,567.000 | 66,746,836.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 64,097,189.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 64,776,861.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 63,768,895.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 64,448,567.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 63,990,338.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 64,670,010.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 64,100,732.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 64,780,404.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 66,090,252.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 576,216.000 |
| 4 | Wall time | 66,746,836.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 66,025,919.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 576,216.000 |
| 5 | Wall time | 66,682,503.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 66,031,250.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 576,216.000 |
| 6 | Wall time | 66,687,834.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 66,036,979.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 576,216.000 |
| 7 | Wall time | 66,693,563.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 65,831,123.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 575,976.000 |
| 8 | Wall time | 66,478,795.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 65,873,257.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 575,976.000 |
| 9 | Wall time | 66,520,929.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 65,707,739.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 575,976.000 |
| 10 | Wall time | 66,355,411.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 65,705,741.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 575,976.000 |
| 11 | Wall time | 66,353,413.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 65,748,452.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 66,391,292.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 65,853,800.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 66,496,640.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 65,814,982.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 66,457,822.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 65,771,812.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 66,414,652.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 65,688,569.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 66,328,273.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 65,843,936.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,752.000 |
| 17 | Wall time | 66,483,640.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 65,891,307.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,752.000 |
| 18 | Wall time | 66,531,011.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 66,051,138.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,752.000 |
| 19 | Wall time | 66,690,842.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 65,017,873.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 575,704.000 |
| 20 | Wall time | 65,655,385.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 65,215,280.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 575,704.000 |
| 21 | Wall time | 65,852,792.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 65,227,827.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 575,704.000 |
| 22 | Wall time | 65,865,339.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 65,132,274.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 575,704.000 |
| 23 | Wall time | 65,769,786.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 65,224,074.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 575,656.000 |
| 24 | Wall time | 65,859,970.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 64,914,400.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 575,656.000 |
| 25 | Wall time | 65,550,296.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 65,269,923.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 575,656.000 |
| 26 | Wall time | 65,905,819.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 65,279,846.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 575,656.000 |
| 27 | Wall time | 65,915,742.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 64,246,187.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 64,880,835.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 63,954,513.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 64,589,161.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 64,442,622.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 65,077,270.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 64,427,879.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 65,062,527.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 9.898 us |
| Median FCT | 6.228 us |
| p95 FCT | 23.236 us |
| Maximum FCT | 797.422 us |
| Median standalone time | 6.264 us |
| Median FCT / standalone | 0.997x |
| p95 FCT / standalone | 2.044x |
| Maximum FCT / standalone | 8.859x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 5.025 us | 7.057 us | 17.364 us | 5.203 us | 0.970x |
| 433.00 B | 2,048 | 5.105 us | 5.143 us | 11.358 us | 4.179 us | 0.987x |
| 490.00 B | 2,048 | 6.138 us | 6.181 us | 12.809 us | 5.221 us | 0.990x |
| 545.00 B | 2,048 | 6.150 us | 6.194 us | 36.378 us | 5.223 us | 0.995x |
| 568.00 B | 2,560 | 5.130 us | 6.156 us | 17.861 us | 4.184 us | 0.991x |
| 632.00 B | 2,048 | 6.174 us | 7.214 us | 16.097 us | 4.187 us | 0.991x |
| 683.00 B | 2,560 | 6.186 us | 6.201 us | 13.573 us | 4.189 us | 0.989x |
| 715.00 B | 2,560 | 4.128 us | 5.170 us | 13.156 us | 4.190 us | 0.996x |
| 760.00 B | 2,048 | 5.394 us | 6.216 us | 7.872 us | 5.232 us | 0.988x |
| 860.00 B | 2,048 | 4.152 us | 5.190 us | 5.263 us | 4.196 us | 0.990x |
| 872.00 B | 2,048 | 6.228 us | 7.268 us | 8.924 us | 4.196 us | 0.992x |
| 970.00 B | 2,560 | 4.168 us | 6.253 us | 14.427 us | 4.200 us | 0.997x |
| 997.00 B | 2,560 | 4.232 us | 8.344 us | 8.548 us | 4.201 us | 0.995x |
| 1,016.00 B | 4,416 | 3.255 us | 7.335 us | 7.473 us | 3.164 us | 0.995x |
| 1.07 KiB | 2,560 | 4.278 us | 8.375 us | 8.684 us | 4.207 us | 0.998x |
| 1.10 KiB | 4,416 | 6.264 us | 6.305 us | 6.458 us | 6.288 us | 0.997x |
| 1.23 KiB | 2,048 | 4.284 us | 6.270 us | 6.462 us | 4.214 us | 0.997x |
| 1.23 KiB | 1,920 | 6.270 us | 7.313 us | 7.445 us | 6.294 us | 0.995x |
| 1.23 KiB | 2,304 | 6.270 us | 7.325 us | 7.485 us | 6.294 us | 0.997x |
| 1.24 KiB | 2,560 | 5.456 us | 7.313 us | 7.547 us | 5.254 us | 0.997x |
| 1.36 KiB | 2,560 | 5.232 us | 5.307 us | 5.972 us | 5.259 us | 1.001x |
| 1.41 KiB | 4,800 | 5.380 us | 7.328 us | 7.560 us | 5.261 us | 0.996x |
| 1.49 KiB | 2,048 | 6.281 us | 7.365 us | 17.014 us | 6.305 us | 1.007x |
| 1.54 KiB | 2,048 | 4.197 us | 6.324 us | 8.350 us | 3.187 us | 1.000x |
| 1.67 KiB | 4,224 | 5.245 us | 7.353 us | 7.483 us | 5.272 us | 0.998x |
| 1.79 KiB | 2,048 | 4.248 us | 7.352 us | 12.223 us | 4.237 us | 1.002x |
| 2.07 KiB | 4,800 | 4.480 us | 6.372 us | 6.700 us | 4.250 us | 0.997x |
| 2.15 KiB | 2,048 | 3.815 us | 4.342 us | 5.189 us | 3.213 us | 1.009x |
| 2.74 KiB | 4,608 | 6.422 us | 7.527 us | 19.275 us | 6.358 us | 1.009x |
| 2.81 KiB | 4,416 | 4.588 us | 8.452 us | 8.637 us | 4.280 us | 0.999x |
| 3.05 KiB | 2,560 | 5.412 us | 7.471 us | 7.551 us | 5.332 us | 1.006x |
| 3.45 KiB | 2,048 | 6.363 us | 6.486 us | 11.477 us | 5.349 us | 1.006x |
| 4.00 KiB | 2,560 | 5.343 us | 6.535 us | 31.876 us | 4.333 us | 1.024x |
| 4.72 KiB | 1,920 | 4.330 us | 6.424 us | 6.580 us | 4.362 us | 0.996x |
| 4.72 KiB | 2,304 | 4.422 us | 6.580 us | 6.973 us | 4.362 us | 1.014x |
| 4.81 KiB | 2,048 | 6.420 us | 7.646 us | 18.355 us | 5.406 us | 1.032x |
| 6.14 KiB | 2,048 | 5.644 us | 7.758 us | 24.146 us | 5.465 us | 1.026x |
| 8.83 KiB | 2,560 | 6.876 us | 7.300 us | 23.759 us | 6.621 us | 1.044x |
| 16.00 KiB | 28,672 | 6.831 us | 8.992 us | 17.771 us | 5.888 us | 1.061x |
| 128.00 KiB | 30,720 | 17.458 us | 32.261 us | 67.319 us | 10.696 us | 1.703x |
| 1.95 MiB | 1,536 | 201.679 us | 479.166 us | 797.422 us | 91.052 us | 2.503x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 3,620,511 |
| Observed queue interval | 134.100 us to 66.723 ms |
| Observed queue duration | 66.589 ms |
| Maximum sampled queue | 1.22 MiB |
| Maximum queue location | switch 33, port 2 |

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
| Trace records recognized | 209,367,344 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 66.726 ms |
| Maximum sampled packet queue | 1.22 MiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 203.12 KiB |
| Events | Dequ: 70,215,584, Enqu: 68,936,176, Recv: 70,215,584 |
| Bytes by event | Dequ: 35.00 GiB, Enqu: 33.78 GiB, Recv: 35.00 GiB |
| Observed interface utilization | 165 interfaces; mean 13.653%, max 36.359% |
| Matched packet queue durations | 67,612,076 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 2.224 us |
| Maximum packet queue time | 50.777 us |
| Mean packet queue time | 445 ns |
| Unmatched/duplicate dequeues | 2,603,508 |
| Enqueue-key collisions | 1,324,100 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
