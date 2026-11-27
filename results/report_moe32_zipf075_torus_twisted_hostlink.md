# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_zipf075_torus_twisted_hostlink/attempts/20261124_204727_418370/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 35,017,861 |
| Fastest rank completion (cycles) | 34,819,508 |
| Maximum exposed communication (cycles) | 33,761,349 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 34.997 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 34,228,117.625 | 34,166,666.000 | 34,338,189.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 574,598.625 | 569,963.000 | 576,840.000 | 32 |
| Wall time | 34,876,287.000 | 34,819,508.000 | 35,017,861.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 34,335,517.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 35,015,189.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 34,338,189.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 35,017,861.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 34,337,353.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 35,017,025.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 34,326,066.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 35,005,738.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 34,275,503.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 576,216.000 |
| 4 | Wall time | 34,932,087.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 34,281,642.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 576,216.000 |
| 5 | Wall time | 34,938,226.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 34,282,441.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 576,216.000 |
| 6 | Wall time | 34,939,025.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 34,282,185.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 576,216.000 |
| 7 | Wall time | 34,938,769.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 34,171,120.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 573,378.000 |
| 8 | Wall time | 34,821,390.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 34,171,343.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 573,335.000 |
| 9 | Wall time | 34,821,656.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 34,170,754.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 573,459.000 |
| 10 | Wall time | 34,820,943.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 34,166,666.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 570,806.000 |
| 11 | Wall time | 34,819,508.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 34,200,819.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 34,843,659.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 34,201,136.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 34,843,976.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 34,200,632.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 34,843,472.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 34,199,579.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 34,842,419.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 34,199,940.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 34,839,644.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 34,198,962.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,534.000 |
| 17 | Wall time | 34,838,884.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 34,199,677.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,403.000 |
| 18 | Wall time | 34,839,730.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 34,198,058.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,363.000 |
| 19 | Wall time | 34,838,151.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 34,218,519.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 572,796.000 |
| 20 | Wall time | 34,858,939.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 34,215,008.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 572,724.000 |
| 21 | Wall time | 34,855,500.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 34,214,584.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 572,911.000 |
| 22 | Wall time | 34,854,889.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 34,212,047.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 571,983.000 |
| 23 | Wall time | 34,853,280.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 34,203,453.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 571,756.000 |
| 24 | Wall time | 34,843,249.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 34,205,763.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 571,797.000 |
| 25 | Wall time | 34,845,518.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 34,204,884.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 569,963.000 |
| 26 | Wall time | 34,846,473.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 34,201,860.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 572,084.000 |
| 27 | Wall time | 34,841,328.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 34,221,564.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 34,856,212.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 34,222,700.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 34,857,348.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 34,224,311.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 34,858,959.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 34,217,489.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 34,852,137.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 4.775 us |
| Median FCT | 3.279 us |
| p95 FCT | 10.039 us |
| Maximum FCT | 330.435 us |
| Median standalone time | 3.258 us |
| Median FCT / standalone | 1.004x |
| p95 FCT / standalone | 1.343x |
| Maximum FCT / standalone | 3.727x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 3.099 us | 4.034 us | 4.138 us | 3.207 us | 0.942x |
| 433.00 B | 2,048 | 4.130 us | 4.182 us | 4.461 us | 4.263 us | 0.971x |
| 490.00 B | 2,048 | 1.073 us | 1.096 us | 1.305 us | 1.145 us | 0.940x |
| 545.00 B | 2,048 | 3.129 us | 3.190 us | 3.462 us | 3.227 us | 0.973x |
| 568.00 B | 2,560 | 3.134 us | 3.191 us | 3.489 us | 3.228 us | 0.974x |
| 632.00 B | 2,048 | 1.091 us | 1.120 us | 1.411 us | 1.151 us | 0.953x |
| 683.00 B | 2,560 | 2.128 us | 2.163 us | 2.453 us | 2.193 us | 0.973x |
| 715.00 B | 2,560 | 4.196 us | 4.235 us | 4.437 us | 4.274 us | 0.983x |
| 760.00 B | 2,048 | 2.140 us | 2.167 us | 2.260 us | 2.196 us | 0.976x |
| 860.00 B | 2,048 | 1.118 us | 1.152 us | 1.237 us | 1.160 us | 0.969x |
| 872.00 B | 2,048 | 2.156 us | 2.192 us | 2.517 us | 2.200 us | 0.983x |
| 970.00 B | 2,560 | 2.172 us | 2.212 us | 2.462 us | 2.204 us | 0.989x |
| 997.00 B | 2,560 | 3.219 us | 3.261 us | 3.394 us | 3.245 us | 0.994x |
| 1,016.00 B | 4,416 | 1.217 us | 3.317 us | 3.400 us | 1.168 us | 1.017x |
| 1.07 KiB | 2,560 | 3.250 us | 3.269 us | 3.418 us | 3.251 us | 0.999x |
| 1.10 KiB | 4,416 | 1.221 us | 3.326 us | 3.365 us | 1.172 us | 1.019x |
| 1.23 KiB | 2,048 | 3.231 us | 3.272 us | 3.360 us | 3.258 us | 0.995x |
| 1.23 KiB | 1,920 | 1.219 us | 3.313 us | 3.321 us | 1.178 us | 1.010x |
| 1.23 KiB | 2,304 | 1.258 us | 3.354 us | 3.386 us | 1.178 us | 1.027x |
| 1.24 KiB | 2,560 | 1.180 us | 1.208 us | 1.265 us | 1.178 us | 1.001x |
| 1.36 KiB | 2,560 | 1.188 us | 1.210 us | 1.356 us | 1.183 us | 1.002x |
| 1.41 KiB | 4,800 | 1.234 us | 3.351 us | 3.388 us | 1.185 us | 1.018x |
| 1.49 KiB | 2,048 | 4.285 us | 4.363 us | 4.606 us | 4.309 us | 0.998x |
| 1.54 KiB | 2,048 | 2.242 us | 2.254 us | 2.387 us | 2.231 us | 0.999x |
| 1.67 KiB | 4,224 | 1.221 us | 3.351 us | 3.422 us | 1.196 us | 1.017x |
| 1.79 KiB | 2,048 | 2.252 us | 2.296 us | 2.410 us | 2.241 us | 1.002x |
| 2.07 KiB | 4,800 | 1.344 us | 3.490 us | 3.531 us | 1.214 us | 1.062x |
| 2.15 KiB | 2,048 | 1.254 us | 1.344 us | 1.800 us | 1.217 us | 1.032x |
| 2.74 KiB | 4,608 | 1.308 us | 3.441 us | 4.278 us | 1.242 us | 1.024x |
| 2.81 KiB | 4,416 | 1.210 us | 3.310 us | 3.610 us | 1.244 us | 0.992x |
| 3.05 KiB | 2,560 | 3.307 us | 3.430 us | 3.613 us | 3.336 us | 0.998x |
| 3.45 KiB | 2,048 | 2.404 us | 2.510 us | 2.555 us | 2.313 us | 1.034x |
| 4.00 KiB | 2,560 | 2.453 us | 2.552 us | 2.987 us | 2.337 us | 1.036x |
| 4.72 KiB | 1,920 | 1.299 us | 3.428 us | 3.789 us | 1.326 us | 0.993x |
| 4.72 KiB | 2,304 | 1.414 us | 3.691 us | 4.002 us | 1.326 us | 1.055x |
| 4.81 KiB | 2,048 | 3.452 us | 3.741 us | 4.855 us | 3.410 us | 1.024x |
| 6.14 KiB | 2,048 | 1.590 us | 1.787 us | 2.614 us | 1.389 us | 1.116x |
| 8.83 KiB | 2,560 | 4.616 us | 5.099 us | 6.191 us | 4.625 us | 1.025x |
| 16.00 KiB | 28,672 | 4.894 us | 5.635 us | 8.189 us | 3.892 us | 1.060x |
| 128.00 KiB | 30,720 | 7.639 us | 17.411 us | 24.666 us | 6.620 us | 1.289x |
| 1.95 MiB | 1,536 | 89.398 us | 131.570 us | 330.435 us | 86.976 us | 1.133x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,267,385 |
| Observed queue interval | 91.800 us to 34.997 ms |
| Observed queue duration | 34.905 ms |
| Maximum sampled queue | 101.88 KiB |
| Maximum queue location | switch 61, port 3 |

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
| Packet trace interval | 10 ns to 34.997 ms |
| Maximum sampled packet queue | 101.97 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 103.61 KiB |
| Events | Dequ: 44,387,936, Enqu: 43,108,528, Recv: 44,387,936 |
| Bytes by event | Dequ: 22.06 GiB, Enqu: 20.84 GiB, Recv: 22.06 GiB |
| Observed interface utilization | 165 interfaces; mean 16.408%, max 31.478% |
| Matched packet queue durations | 42,838,021 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 42 ns |
| Maximum packet queue time | 4.096 us |
| Mean packet queue time | 18 ns |
| Unmatched/duplicate dequeues | 1,549,915 |
| Enqueue-key collisions | 270,507 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
