# ASTRA-sim NS-3 Results Report

Result directory: `/Users/anon/Documents/fall26/CS6250-CN/project/astra-sim/runs/torus_sweep/straggler_1_5_torus2_aligned/attempts/20261126_030556_566401/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 32,336,392 |
| Fastest rank completion (cycles) | 32,164,609 |
| Maximum exposed communication (cycles) | 31,929,300 |
| Completed network flows | 50,176 |
| Total bytes sent | 9,525,264,384 |
| Network-flow finish proxy | 32.316 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 40.267% | 40.264% | 40.267% | 32 |
| Average memory utilization (%) | 83.379% | 83.379% | 83.382% | 32 |
| Average operation intensity | 3,183.480 | 3,182.966 | 3,183.497 | 32 |
| Comm time | 32,123,222.406 | 32,026,491.000 | 32,228,284.000 | 32 |
| Compute bound percentage (%) | 26.074% | 26.069% | 26.074% | 32 |
| GPU time | 413,456.125 | 407,092.000 | 610,744.000 | 32 |
| Total compute-communication overlap | 303,658.562 | 298,984.000 | 448,570.000 | 32 |
| Wall time | 32,233,019.969 | 32,164,609.000 | 32,336,392.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 40.264% |
| 0 | Average memory utilization | 83.382% |
| 0 | Average operation intensity | 3,182.966 |
| 0 | Comm time | 32,026,491.000 |
| 0 | Compute bound percentage | 26.069% |
| 0 | GPU time | 610,744.000 |
| 0 | Total compute-communication overlap | 448,570.000 |
| 0 | Wall time | 32,188,665.000 |
| 1 | Average compute utilization | 40.267% |
| 1 | Average memory utilization | 83.379% |
| 1 | Average operation intensity | 3,183.497 |
| 1 | Comm time | 32,211,798.000 |
| 1 | Compute bound percentage | 26.074% |
| 1 | GPU time | 407,092.000 |
| 1 | Total compute-communication overlap | 298,984.000 |
| 1 | Wall time | 32,319,906.000 |
| 2 | Average compute utilization | 40.267% |
| 2 | Average memory utilization | 83.379% |
| 2 | Average operation intensity | 3,183.497 |
| 2 | Comm time | 32,133,193.000 |
| 2 | Compute bound percentage | 26.074% |
| 2 | GPU time | 407,092.000 |
| 2 | Total compute-communication overlap | 298,984.000 |
| 2 | Wall time | 32,241,301.000 |
| 3 | Average compute utilization | 40.267% |
| 3 | Average memory utilization | 83.379% |
| 3 | Average operation intensity | 3,183.497 |
| 3 | Comm time | 32,090,192.000 |
| 3 | Compute bound percentage | 26.074% |
| 3 | GPU time | 407,092.000 |
| 3 | Total compute-communication overlap | 298,984.000 |
| 3 | Wall time | 32,198,300.000 |
| 4 | Average compute utilization | 40.267% |
| 4 | Average memory utilization | 83.379% |
| 4 | Average operation intensity | 3,183.497 |
| 4 | Comm time | 32,056,501.000 |
| 4 | Compute bound percentage | 26.074% |
| 4 | GPU time | 407,092.000 |
| 4 | Total compute-communication overlap | 298,984.000 |
| 4 | Wall time | 32,164,609.000 |
| 5 | Average compute utilization | 40.267% |
| 5 | Average memory utilization | 83.379% |
| 5 | Average operation intensity | 3,183.497 |
| 5 | Comm time | 32,207,301.000 |
| 5 | Compute bound percentage | 26.074% |
| 5 | GPU time | 407,092.000 |
| 5 | Total compute-communication overlap | 298,984.000 |
| 5 | Wall time | 32,315,409.000 |
| 6 | Average compute utilization | 40.267% |
| 6 | Average memory utilization | 83.379% |
| 6 | Average operation intensity | 3,183.497 |
| 6 | Comm time | 32,106,987.000 |
| 6 | Compute bound percentage | 26.074% |
| 6 | GPU time | 407,092.000 |
| 6 | Total compute-communication overlap | 298,984.000 |
| 6 | Wall time | 32,215,095.000 |
| 7 | Average compute utilization | 40.267% |
| 7 | Average memory utilization | 83.379% |
| 7 | Average operation intensity | 3,183.497 |
| 7 | Comm time | 32,083,479.000 |
| 7 | Compute bound percentage | 26.074% |
| 7 | GPU time | 407,092.000 |
| 7 | Total compute-communication overlap | 298,984.000 |
| 7 | Wall time | 32,191,587.000 |
| 8 | Average compute utilization | 40.267% |
| 8 | Average memory utilization | 83.379% |
| 8 | Average operation intensity | 3,183.497 |
| 8 | Comm time | 32,086,942.000 |
| 8 | Compute bound percentage | 26.074% |
| 8 | GPU time | 407,092.000 |
| 8 | Total compute-communication overlap | 298,984.000 |
| 8 | Wall time | 32,195,050.000 |
| 9 | Average compute utilization | 40.267% |
| 9 | Average memory utilization | 83.379% |
| 9 | Average operation intensity | 3,183.497 |
| 9 | Comm time | 32,177,165.000 |
| 9 | Compute bound percentage | 26.074% |
| 9 | GPU time | 407,092.000 |
| 9 | Total compute-communication overlap | 298,984.000 |
| 9 | Wall time | 32,285,273.000 |
| 10 | Average compute utilization | 40.267% |
| 10 | Average memory utilization | 83.379% |
| 10 | Average operation intensity | 3,183.497 |
| 10 | Comm time | 32,096,411.000 |
| 10 | Compute bound percentage | 26.074% |
| 10 | GPU time | 407,092.000 |
| 10 | Total compute-communication overlap | 298,984.000 |
| 10 | Wall time | 32,204,519.000 |
| 11 | Average compute utilization | 40.267% |
| 11 | Average memory utilization | 83.379% |
| 11 | Average operation intensity | 3,183.497 |
| 11 | Comm time | 32,100,429.000 |
| 11 | Compute bound percentage | 26.074% |
| 11 | GPU time | 407,092.000 |
| 11 | Total compute-communication overlap | 298,984.000 |
| 11 | Wall time | 32,208,537.000 |
| 12 | Average compute utilization | 40.267% |
| 12 | Average memory utilization | 83.379% |
| 12 | Average operation intensity | 3,183.497 |
| 12 | Comm time | 32,077,536.000 |
| 12 | Compute bound percentage | 26.074% |
| 12 | GPU time | 407,092.000 |
| 12 | Total compute-communication overlap | 298,984.000 |
| 12 | Wall time | 32,185,644.000 |
| 13 | Average compute utilization | 40.267% |
| 13 | Average memory utilization | 83.379% |
| 13 | Average operation intensity | 3,183.497 |
| 13 | Comm time | 32,174,131.000 |
| 13 | Compute bound percentage | 26.074% |
| 13 | GPU time | 407,092.000 |
| 13 | Total compute-communication overlap | 298,984.000 |
| 13 | Wall time | 32,282,239.000 |
| 14 | Average compute utilization | 40.267% |
| 14 | Average memory utilization | 83.379% |
| 14 | Average operation intensity | 3,183.497 |
| 14 | Comm time | 32,069,230.000 |
| 14 | Compute bound percentage | 26.074% |
| 14 | GPU time | 407,092.000 |
| 14 | Total compute-communication overlap | 298,984.000 |
| 14 | Wall time | 32,177,338.000 |
| 15 | Average compute utilization | 40.267% |
| 15 | Average memory utilization | 83.379% |
| 15 | Average operation intensity | 3,183.497 |
| 15 | Comm time | 32,110,261.000 |
| 15 | Compute bound percentage | 26.074% |
| 15 | GPU time | 407,092.000 |
| 15 | Total compute-communication overlap | 298,984.000 |
| 15 | Wall time | 32,218,369.000 |
| 16 | Average compute utilization | 40.267% |
| 16 | Average memory utilization | 83.379% |
| 16 | Average operation intensity | 3,183.497 |
| 16 | Comm time | 32,115,119.000 |
| 16 | Compute bound percentage | 26.074% |
| 16 | GPU time | 407,092.000 |
| 16 | Total compute-communication overlap | 298,984.000 |
| 16 | Wall time | 32,223,227.000 |
| 17 | Average compute utilization | 40.267% |
| 17 | Average memory utilization | 83.379% |
| 17 | Average operation intensity | 3,183.497 |
| 17 | Comm time | 32,228,284.000 |
| 17 | Compute bound percentage | 26.074% |
| 17 | GPU time | 407,092.000 |
| 17 | Total compute-communication overlap | 298,984.000 |
| 17 | Wall time | 32,336,392.000 |
| 18 | Average compute utilization | 40.267% |
| 18 | Average memory utilization | 83.379% |
| 18 | Average operation intensity | 3,183.497 |
| 18 | Comm time | 32,098,234.000 |
| 18 | Compute bound percentage | 26.074% |
| 18 | GPU time | 407,092.000 |
| 18 | Total compute-communication overlap | 298,984.000 |
| 18 | Wall time | 32,206,342.000 |
| 19 | Average compute utilization | 40.267% |
| 19 | Average memory utilization | 83.379% |
| 19 | Average operation intensity | 3,183.497 |
| 19 | Comm time | 32,123,857.000 |
| 19 | Compute bound percentage | 26.074% |
| 19 | GPU time | 407,092.000 |
| 19 | Total compute-communication overlap | 298,984.000 |
| 19 | Wall time | 32,231,965.000 |
| 20 | Average compute utilization | 40.267% |
| 20 | Average memory utilization | 83.379% |
| 20 | Average operation intensity | 3,183.497 |
| 20 | Comm time | 32,101,671.000 |
| 20 | Compute bound percentage | 26.074% |
| 20 | GPU time | 407,092.000 |
| 20 | Total compute-communication overlap | 298,984.000 |
| 20 | Wall time | 32,209,779.000 |
| 21 | Average compute utilization | 40.267% |
| 21 | Average memory utilization | 83.379% |
| 21 | Average operation intensity | 3,183.497 |
| 21 | Comm time | 32,207,429.000 |
| 21 | Compute bound percentage | 26.074% |
| 21 | GPU time | 407,092.000 |
| 21 | Total compute-communication overlap | 298,984.000 |
| 21 | Wall time | 32,315,537.000 |
| 22 | Average compute utilization | 40.267% |
| 22 | Average memory utilization | 83.379% |
| 22 | Average operation intensity | 3,183.497 |
| 22 | Comm time | 32,092,050.000 |
| 22 | Compute bound percentage | 26.074% |
| 22 | GPU time | 407,092.000 |
| 22 | Total compute-communication overlap | 298,984.000 |
| 22 | Wall time | 32,200,158.000 |
| 23 | Average compute utilization | 40.267% |
| 23 | Average memory utilization | 83.379% |
| 23 | Average operation intensity | 3,183.497 |
| 23 | Comm time | 32,126,112.000 |
| 23 | Compute bound percentage | 26.074% |
| 23 | GPU time | 407,092.000 |
| 23 | Total compute-communication overlap | 298,984.000 |
| 23 | Wall time | 32,234,220.000 |
| 24 | Average compute utilization | 40.267% |
| 24 | Average memory utilization | 83.379% |
| 24 | Average operation intensity | 3,183.497 |
| 24 | Comm time | 32,089,428.000 |
| 24 | Compute bound percentage | 26.074% |
| 24 | GPU time | 407,092.000 |
| 24 | Total compute-communication overlap | 298,984.000 |
| 24 | Wall time | 32,197,536.000 |
| 25 | Average compute utilization | 40.267% |
| 25 | Average memory utilization | 83.379% |
| 25 | Average operation intensity | 3,183.497 |
| 25 | Comm time | 32,226,840.000 |
| 25 | Compute bound percentage | 26.074% |
| 25 | GPU time | 407,092.000 |
| 25 | Total compute-communication overlap | 298,984.000 |
| 25 | Wall time | 32,334,948.000 |
| 26 | Average compute utilization | 40.267% |
| 26 | Average memory utilization | 83.379% |
| 26 | Average operation intensity | 3,183.497 |
| 26 | Comm time | 32,110,597.000 |
| 26 | Compute bound percentage | 26.074% |
| 26 | GPU time | 407,092.000 |
| 26 | Total compute-communication overlap | 298,984.000 |
| 26 | Wall time | 32,218,705.000 |
| 27 | Average compute utilization | 40.267% |
| 27 | Average memory utilization | 83.379% |
| 27 | Average operation intensity | 3,183.497 |
| 27 | Comm time | 32,123,864.000 |
| 27 | Compute bound percentage | 26.074% |
| 27 | GPU time | 407,092.000 |
| 27 | Total compute-communication overlap | 298,984.000 |
| 27 | Wall time | 32,231,972.000 |
| 28 | Average compute utilization | 40.267% |
| 28 | Average memory utilization | 83.379% |
| 28 | Average operation intensity | 3,183.497 |
| 28 | Comm time | 32,082,215.000 |
| 28 | Compute bound percentage | 26.074% |
| 28 | GPU time | 407,092.000 |
| 28 | Total compute-communication overlap | 298,984.000 |
| 28 | Wall time | 32,190,323.000 |
| 29 | Average compute utilization | 40.267% |
| 29 | Average memory utilization | 83.379% |
| 29 | Average operation intensity | 3,183.497 |
| 29 | Comm time | 32,208,661.000 |
| 29 | Compute bound percentage | 26.074% |
| 29 | GPU time | 407,092.000 |
| 29 | Total compute-communication overlap | 298,984.000 |
| 29 | Wall time | 32,316,769.000 |
| 30 | Average compute utilization | 40.267% |
| 30 | Average memory utilization | 83.379% |
| 30 | Average operation intensity | 3,183.497 |
| 30 | Comm time | 32,108,470.000 |
| 30 | Compute bound percentage | 26.074% |
| 30 | GPU time | 407,092.000 |
| 30 | Total compute-communication overlap | 298,984.000 |
| 30 | Wall time | 32,216,578.000 |
| 31 | Average compute utilization | 40.267% |
| 31 | Average memory utilization | 83.379% |
| 31 | Average operation intensity | 3,183.497 |
| 31 | Comm time | 32,092,239.000 |
| 31 | Compute bound percentage | 26.074% |
| 31 | GPU time | 407,092.000 |
| 31 | Total compute-communication overlap | 298,984.000 |
| 31 | Wall time | 32,200,347.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 17.831 us |
| Median FCT | 4.135 us |
| p95 FCT | 89.566 us |
| Maximum FCT | 284.711 us |
| Median standalone time | 2.894 us |
| Median FCT / standalone | 1.429x |
| p95 FCT / standalone | 3.160x |
| Maximum FCT / standalone | 6.240x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 KiB | 30,720 | 3.782 us | 6.375 us | 14.993 us | 2.894 us | 1.358x |
| 116.00 KiB | 14,336 | 10.753 us | 32.476 us | 40.552 us | 6.499 us | 2.068x |
| 1,000.00 KiB | 3,584 | 83.744 us | 131.888 us | 173.558 us | 44.446 us | 1.975x |
| 1.95 MiB | 1,536 | 166.963 us | 234.345 us | 284.711 us | 87.372 us | 1.987x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 3,365,252 |
| Observed queue interval | 4.900 us to 32.315 ms |
| Observed queue duration | 32.310 ms |
| Maximum sampled queue | 270.13 KiB |
| Maximum queue location | switch 34, port 5 |

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
| Trace records recognized | 121,875,456 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 4.751 us to 32.316 ms |
| Maximum sampled packet queue | 269.12 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 128 |
| SimSetting window | 113.28 KiB |
| Events | Dequ: 41,121,792, Enqu: 39,631,872, Recv: 41,121,792 |
| Bytes by event | Dequ: 20.74 GiB, Enqu: 19.30 GiB, Recv: 20.74 GiB |
| Observed interface utilization | 101 interfaces; mean 27.292%, max 43.069% |
| Matched packet queue durations | 39,550,274 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 1.587 us |
| Maximum packet queue time | 10.943 us |
| Mean packet queue time | 345 ns |
| Unmatched/duplicate dequeues | 1,571,518 |
| Enqueue-key collisions | 81,598 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
