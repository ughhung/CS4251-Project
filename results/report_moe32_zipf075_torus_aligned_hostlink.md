# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/moe32_zipf075_torus_aligned_hostlink/attempts/20261124_204727_418370/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 29,532,253 |
| Fastest rank completion (cycles) | 29,477,126 |
| Maximum exposed communication (cycles) | 28,306,830 |
| Completed network flows | 174,272 |
| Total bytes sent | 7,845,815,040 |
| Network-flow finish proxy | 29.512 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.390% | 77.635% | 80.052% | 32 |
| Average memory utilization (%) | 62.649% | 62.313% | 63.541% | 32 |
| Average operation intensity | 8,455.642 | 8,230.790 | 8,540.486 | 32 |
| Comm time | 28,847,667.156 | 28,822,220.000 | 28,867,167.000 | 32 |
| Compute bound percentage (%) | 52.892% | 51.722% | 53.333% | 32 |
| GPU time | 1,222,768.000 | 1,210,272.000 | 1,256,512.000 | 32 |
| Total compute-communication overlap | 571,999.938 | 559,991.000 | 576,840.000 | 32 |
| Wall time | 29,498,435.219 | 29,477,126.000 | 29,532,253.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 77.635% |
| 0 | Average memory utilization | 63.541% |
| 0 | Average operation intensity | 8,230.790 |
| 0 | Comm time | 28,822,220.000 |
| 0 | Compute bound percentage | 51.722% |
| 0 | GPU time | 1,256,512.000 |
| 0 | Total compute-communication overlap | 576,840.000 |
| 0 | Wall time | 29,501,892.000 |
| 1 | Average compute utilization | 77.635% |
| 1 | Average memory utilization | 63.541% |
| 1 | Average operation intensity | 8,230.790 |
| 1 | Comm time | 28,824,971.000 |
| 1 | Compute bound percentage | 51.722% |
| 1 | GPU time | 1,256,512.000 |
| 1 | Total compute-communication overlap | 576,840.000 |
| 1 | Wall time | 29,504,643.000 |
| 2 | Average compute utilization | 77.635% |
| 2 | Average memory utilization | 63.541% |
| 2 | Average operation intensity | 8,230.790 |
| 2 | Comm time | 28,829,438.000 |
| 2 | Compute bound percentage | 51.722% |
| 2 | GPU time | 1,256,512.000 |
| 2 | Total compute-communication overlap | 576,840.000 |
| 2 | Wall time | 29,509,110.000 |
| 3 | Average compute utilization | 77.635% |
| 3 | Average memory utilization | 63.541% |
| 3 | Average operation intensity | 8,230.790 |
| 3 | Comm time | 28,828,315.000 |
| 3 | Compute bound percentage | 51.722% |
| 3 | GPU time | 1,256,512.000 |
| 3 | Total compute-communication overlap | 576,840.000 |
| 3 | Wall time | 29,507,987.000 |
| 4 | Average compute utilization | 78.853% |
| 4 | Average memory utilization | 62.922% |
| 4 | Average operation intensity | 8,386.721 |
| 4 | Comm time | 28,861,424.000 |
| 4 | Compute bound percentage | 52.535% |
| 4 | GPU time | 1,232,800.000 |
| 4 | Total compute-communication overlap | 567,618.000 |
| 4 | Wall time | 29,526,606.000 |
| 5 | Average compute utilization | 78.853% |
| 5 | Average memory utilization | 62.922% |
| 5 | Average operation intensity | 8,386.721 |
| 5 | Comm time | 28,867,127.000 |
| 5 | Compute bound percentage | 52.535% |
| 5 | GPU time | 1,232,800.000 |
| 5 | Total compute-communication overlap | 567,674.000 |
| 5 | Wall time | 29,532,253.000 |
| 6 | Average compute utilization | 78.853% |
| 6 | Average memory utilization | 62.922% |
| 6 | Average operation intensity | 8,386.721 |
| 6 | Comm time | 28,865,456.000 |
| 6 | Compute bound percentage | 52.535% |
| 6 | GPU time | 1,232,800.000 |
| 6 | Total compute-communication overlap | 567,618.000 |
| 6 | Wall time | 29,530,638.000 |
| 7 | Average compute utilization | 78.853% |
| 7 | Average memory utilization | 62.922% |
| 7 | Average operation intensity | 8,386.721 |
| 7 | Comm time | 28,859,558.000 |
| 7 | Compute bound percentage | 52.535% |
| 7 | GPU time | 1,232,800.000 |
| 7 | Total compute-communication overlap | 567,618.000 |
| 7 | Wall time | 29,524,740.000 |
| 8 | Average compute utilization | 79.334% |
| 8 | Average memory utilization | 62.678% |
| 8 | Average operation intensity | 8,448.495 |
| 8 | Comm time | 28,837,261.000 |
| 8 | Compute bound percentage | 52.854% |
| 8 | GPU time | 1,223,648.000 |
| 8 | Total compute-communication overlap | 575,976.000 |
| 8 | Wall time | 29,484,933.000 |
| 9 | Average compute utilization | 79.334% |
| 9 | Average memory utilization | 62.678% |
| 9 | Average operation intensity | 8,448.495 |
| 9 | Comm time | 28,834,203.000 |
| 9 | Compute bound percentage | 52.854% |
| 9 | GPU time | 1,223,648.000 |
| 9 | Total compute-communication overlap | 575,976.000 |
| 9 | Wall time | 29,481,875.000 |
| 10 | Average compute utilization | 79.334% |
| 10 | Average memory utilization | 62.678% |
| 10 | Average operation intensity | 8,448.495 |
| 10 | Comm time | 28,834,230.000 |
| 10 | Compute bound percentage | 52.854% |
| 10 | GPU time | 1,223,648.000 |
| 10 | Total compute-communication overlap | 575,976.000 |
| 10 | Wall time | 29,481,902.000 |
| 11 | Average compute utilization | 79.334% |
| 11 | Average memory utilization | 62.678% |
| 11 | Average operation intensity | 8,448.495 |
| 11 | Comm time | 28,837,308.000 |
| 11 | Compute bound percentage | 52.854% |
| 11 | GPU time | 1,223,648.000 |
| 11 | Total compute-communication overlap | 575,976.000 |
| 11 | Wall time | 29,484,980.000 |
| 12 | Average compute utilization | 79.600% |
| 12 | Average memory utilization | 62.542% |
| 12 | Average operation intensity | 8,482.393 |
| 12 | Comm time | 28,843,352.000 |
| 12 | Compute bound percentage | 53.033% |
| 12 | GPU time | 1,218,688.000 |
| 12 | Total compute-communication overlap | 575,848.000 |
| 12 | Wall time | 29,486,192.000 |
| 13 | Average compute utilization | 79.600% |
| 13 | Average memory utilization | 62.542% |
| 13 | Average operation intensity | 8,482.393 |
| 13 | Comm time | 28,841,400.000 |
| 13 | Compute bound percentage | 53.033% |
| 13 | GPU time | 1,218,688.000 |
| 13 | Total compute-communication overlap | 575,848.000 |
| 13 | Wall time | 29,484,240.000 |
| 14 | Average compute utilization | 79.600% |
| 14 | Average memory utilization | 62.542% |
| 14 | Average operation intensity | 8,482.393 |
| 14 | Comm time | 28,840,692.000 |
| 14 | Compute bound percentage | 53.033% |
| 14 | GPU time | 1,218,688.000 |
| 14 | Total compute-communication overlap | 575,848.000 |
| 14 | Wall time | 29,483,532.000 |
| 15 | Average compute utilization | 79.600% |
| 15 | Average memory utilization | 62.542% |
| 15 | Average operation intensity | 8,482.393 |
| 15 | Comm time | 28,843,090.000 |
| 15 | Compute bound percentage | 53.033% |
| 15 | GPU time | 1,218,688.000 |
| 15 | Total compute-communication overlap | 575,848.000 |
| 15 | Wall time | 29,485,930.000 |
| 16 | Average compute utilization | 79.773% |
| 16 | Average memory utilization | 62.455% |
| 16 | Average operation intensity | 8,504.608 |
| 16 | Comm time | 28,858,977.000 |
| 16 | Compute bound percentage | 53.147% |
| 16 | GPU time | 1,215,456.000 |
| 16 | Total compute-communication overlap | 575,752.000 |
| 16 | Wall time | 29,498,681.000 |
| 17 | Average compute utilization | 79.773% |
| 17 | Average memory utilization | 62.455% |
| 17 | Average operation intensity | 8,504.608 |
| 17 | Comm time | 28,861,849.000 |
| 17 | Compute bound percentage | 53.147% |
| 17 | GPU time | 1,215,456.000 |
| 17 | Total compute-communication overlap | 575,752.000 |
| 17 | Wall time | 29,501,553.000 |
| 18 | Average compute utilization | 79.773% |
| 18 | Average memory utilization | 62.455% |
| 18 | Average operation intensity | 8,504.608 |
| 18 | Comm time | 28,866,758.000 |
| 18 | Compute bound percentage | 53.147% |
| 18 | GPU time | 1,215,456.000 |
| 18 | Total compute-communication overlap | 575,752.000 |
| 18 | Wall time | 29,506,462.000 |
| 19 | Average compute utilization | 79.773% |
| 19 | Average memory utilization | 62.455% |
| 19 | Average operation intensity | 8,504.608 |
| 19 | Comm time | 28,865,922.000 |
| 19 | Compute bound percentage | 53.147% |
| 19 | GPU time | 1,215,456.000 |
| 19 | Total compute-communication overlap | 575,752.000 |
| 19 | Wall time | 29,505,626.000 |
| 20 | Average compute utilization | 79.890% |
| 20 | Average memory utilization | 62.395% |
| 20 | Average operation intensity | 8,520.044 |
| 20 | Comm time | 28,861,562.000 |
| 20 | Compute bound percentage | 53.224% |
| 20 | GPU time | 1,213,216.000 |
| 20 | Total compute-communication overlap | 560,711.000 |
| 20 | Wall time | 29,514,067.000 |
| 21 | Average compute utilization | 79.890% |
| 21 | Average memory utilization | 62.395% |
| 21 | Average operation intensity | 8,520.044 |
| 21 | Comm time | 28,864,705.000 |
| 21 | Compute bound percentage | 53.224% |
| 21 | GPU time | 1,213,216.000 |
| 21 | Total compute-communication overlap | 560,463.000 |
| 21 | Wall time | 29,517,458.000 |
| 22 | Average compute utilization | 79.890% |
| 22 | Average memory utilization | 62.395% |
| 22 | Average operation intensity | 8,520.044 |
| 22 | Comm time | 28,867,167.000 |
| 22 | Compute bound percentage | 53.224% |
| 22 | GPU time | 1,213,216.000 |
| 22 | Total compute-communication overlap | 560,337.000 |
| 22 | Wall time | 29,520,046.000 |
| 23 | Average compute utilization | 79.890% |
| 23 | Average memory utilization | 62.395% |
| 23 | Average operation intensity | 8,520.044 |
| 23 | Comm time | 28,865,042.000 |
| 23 | Compute bound percentage | 53.224% |
| 23 | GPU time | 1,213,216.000 |
| 23 | Total compute-communication overlap | 559,991.000 |
| 23 | Wall time | 29,518,267.000 |
| 24 | Average compute utilization | 79.983% |
| 24 | Average memory utilization | 62.348% |
| 24 | Average operation intensity | 8,531.600 |
| 24 | Comm time | 28,837,222.000 |
| 24 | Compute bound percentage | 53.287% |
| 24 | GPU time | 1,211,552.000 |
| 24 | Total compute-communication overlap | 569,318.000 |
| 24 | Wall time | 29,479,456.000 |
| 25 | Average compute utilization | 79.983% |
| 25 | Average memory utilization | 62.348% |
| 25 | Average operation intensity | 8,531.600 |
| 25 | Comm time | 28,836,046.000 |
| 25 | Compute bound percentage | 53.287% |
| 25 | GPU time | 1,211,552.000 |
| 25 | Total compute-communication overlap | 567,515.000 |
| 25 | Wall time | 29,480,083.000 |
| 26 | Average compute utilization | 79.983% |
| 26 | Average memory utilization | 62.348% |
| 26 | Average operation intensity | 8,531.600 |
| 26 | Comm time | 28,833,137.000 |
| 26 | Compute bound percentage | 53.287% |
| 26 | GPU time | 1,211,552.000 |
| 26 | Total compute-communication overlap | 567,563.000 |
| 26 | Wall time | 29,477,126.000 |
| 27 | Average compute utilization | 79.983% |
| 27 | Average memory utilization | 62.348% |
| 27 | Average operation intensity | 8,531.600 |
| 27 | Comm time | 28,833,743.000 |
| 27 | Compute bound percentage | 53.287% |
| 27 | GPU time | 1,211,552.000 |
| 27 | Total compute-communication overlap | 567,412.000 |
| 27 | Wall time | 29,477,883.000 |
| 28 | Average compute utilization | 80.052% |
| 28 | Average memory utilization | 62.313% |
| 28 | Average operation intensity | 8,540.486 |
| 28 | Comm time | 28,852,408.000 |
| 28 | Compute bound percentage | 53.333% |
| 28 | GPU time | 1,210,272.000 |
| 28 | Total compute-communication overlap | 575,624.000 |
| 28 | Wall time | 29,487,056.000 |
| 29 | Average compute utilization | 80.052% |
| 29 | Average memory utilization | 62.313% |
| 29 | Average operation intensity | 8,540.486 |
| 29 | Comm time | 28,851,080.000 |
| 29 | Compute bound percentage | 53.333% |
| 29 | GPU time | 1,210,272.000 |
| 29 | Total compute-communication overlap | 575,624.000 |
| 29 | Wall time | 29,485,728.000 |
| 30 | Average compute utilization | 80.052% |
| 30 | Average memory utilization | 62.313% |
| 30 | Average operation intensity | 8,540.486 |
| 30 | Comm time | 28,848,856.000 |
| 30 | Compute bound percentage | 53.333% |
| 30 | GPU time | 1,210,272.000 |
| 30 | Total compute-communication overlap | 575,624.000 |
| 30 | Wall time | 29,483,504.000 |
| 31 | Average compute utilization | 80.052% |
| 31 | Average memory utilization | 62.313% |
| 31 | Average operation intensity | 8,540.486 |
| 31 | Comm time | 28,850,830.000 |
| 31 | Compute bound percentage | 53.333% |
| 31 | GPU time | 1,210,272.000 |
| 31 | Total compute-communication overlap | 575,624.000 |
| 31 | Wall time | 29,485,478.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 4.016 us |
| Median FCT | 2.599 us |
| p95 FCT | 7.457 us |
| Maximum FCT | 96.902 us |
| Median standalone time | 1.812 us |
| Median FCT / standalone | 1.007x |
| p95 FCT / standalone | 2.060x |
| Maximum FCT / standalone | 3.611x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 1.019 us | 1.019 us | 1.019 us | 1.127 us | 0.904x |
| 433.00 B | 2,048 | 1.067 us | 1.088 us | 1.219 us | 1.143 us | 0.936x |
| 490.00 B | 2,048 | 2.096 us | 2.116 us | 2.250 us | 2.185 us | 0.961x |
| 545.00 B | 2,048 | 1.079 us | 1.102 us | 1.380 us | 1.147 us | 0.944x |
| 568.00 B | 2,560 | 3.134 us | 3.163 us | 3.561 us | 3.228 us | 0.973x |
| 632.00 B | 2,048 | 2.120 us | 2.127 us | 2.340 us | 2.191 us | 0.969x |
| 683.00 B | 2,560 | 4.190 us | 4.251 us | 4.736 us | 4.273 us | 0.983x |
| 715.00 B | 2,560 | 1.100 us | 1.128 us | 1.248 us | 1.154 us | 0.957x |
| 760.00 B | 2,048 | 3.174 us | 3.203 us | 3.257 us | 3.236 us | 0.982x |
| 860.00 B | 2,048 | 2.156 us | 2.199 us | 2.313 us | 2.200 us | 0.983x |
| 872.00 B | 2,048 | 3.194 us | 3.230 us | 3.291 us | 3.240 us | 0.988x |
| 970.00 B | 2,560 | 4.256 us | 4.319 us | 4.720 us | 4.284 us | 0.996x |
| 997.00 B | 2,560 | 1.133 us | 1.175 us | 1.210 us | 1.165 us | 0.978x |
| 1,016.00 B | 4,416 | 1.168 us | 1.240 us | 1.337 us | 1.168 us | 1.004x |
| 1.07 KiB | 2,560 | 3.250 us | 3.298 us | 3.373 us | 3.251 us | 1.001x |
| 1.10 KiB | 4,416 | 1.176 us | 1.248 us | 1.279 us | 1.172 us | 1.004x |
| 1.23 KiB | 2,048 | 2.188 us | 2.229 us | 2.328 us | 2.218 us | 0.991x |
| 1.23 KiB | 1,920 | 1.176 us | 1.229 us | 1.262 us | 1.178 us | 0.998x |
| 1.23 KiB | 2,304 | 1.186 us | 1.268 us | 1.288 us | 1.178 us | 1.013x |
| 1.24 KiB | 2,560 | 2.221 us | 2.229 us | 2.345 us | 2.218 us | 1.001x |
| 1.36 KiB | 2,560 | 3.236 us | 3.288 us | 3.489 us | 3.263 us | 0.995x |
| 1.41 KiB | 4,800 | 1.193 us | 1.275 us | 1.293 us | 1.185 us | 1.006x |
| 1.49 KiB | 2,048 | 1.197 us | 1.226 us | 1.370 us | 1.189 us | 1.005x |
| 1.54 KiB | 2,048 | 4.287 us | 4.368 us | 4.611 us | 4.311 us | 1.000x |
| 1.67 KiB | 4,224 | 1.199 us | 1.286 us | 1.357 us | 1.196 us | 1.001x |
| 1.79 KiB | 2,048 | 3.295 us | 3.331 us | 3.439 us | 3.281 us | 1.004x |
| 2.07 KiB | 4,800 | 1.262 us | 1.418 us | 1.445 us | 1.214 us | 1.051x |
| 2.15 KiB | 2,048 | 2.300 us | 2.370 us | 3.483 us | 2.257 us | 1.020x |
| 2.74 KiB | 4,608 | 1.276 us | 1.444 us | 2.161 us | 1.242 us | 1.027x |
| 2.81 KiB | 4,416 | 1.210 us | 1.302 us | 1.524 us | 1.244 us | 0.984x |
| 3.05 KiB | 2,560 | 2.377 us | 2.474 us | 2.537 us | 2.296 us | 1.033x |
| 3.45 KiB | 2,048 | 3.447 us | 3.565 us | 3.692 us | 3.353 us | 1.028x |
| 4.00 KiB | 2,560 | 4.513 us | 4.583 us | 5.297 us | 4.417 us | 1.018x |
| 4.72 KiB | 1,920 | 1.291 us | 1.352 us | 1.446 us | 1.326 us | 0.981x |
| 4.72 KiB | 2,304 | 1.297 us | 1.670 us | 1.916 us | 1.326 us | 1.027x |
| 4.81 KiB | 2,048 | 3.452 us | 3.663 us | 4.750 us | 3.410 us | 1.024x |
| 6.14 KiB | 2,048 | 2.597 us | 2.667 us | 3.920 us | 2.429 us | 1.049x |
| 8.83 KiB | 2,560 | 1.816 us | 1.898 us | 2.553 us | 1.505 us | 1.182x |
| 16.00 KiB | 28,672 | 3.733 us | 3.743 us | 6.544 us | 1.812 us | 1.947x |
| 128.00 KiB | 30,720 | 6.766 us | 15.182 us | 22.819 us | 6.620 us | 1.182x |
| 1.95 MiB | 1,536 | 89.178 us | 91.575 us | 96.902 us | 86.976 us | 1.029x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 868,895 |
| Observed queue interval | 32.300 us to 29.511 ms |
| Observed queue duration | 29.479 ms |
| Maximum sampled queue | 46.16 KiB |
| Maximum queue location | switch 32, port 1 |

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
| Packet trace interval | 10 ns to 29.512 ms |
| Maximum sampled packet queue | 46.76 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 154.39 KiB |
| Events | Dequ: 34,763,616, Enqu: 33,484,208, Recv: 34,763,616 |
| Bytes by event | Dequ: 17.29 GiB, Enqu: 16.07 GiB, Recv: 17.29 GiB |
| Observed interface utilization | 165 interfaces; mean 15.253%, max 37.329% |
| Matched packet queue durations | 33,398,061 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 41 ns |
| Maximum packet queue time | 1.910 us |
| Mean packet queue time | 9 ns |
| Unmatched/duplicate dequeues | 1,365,555 |
| Enqueue-key collisions | 86,147 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
