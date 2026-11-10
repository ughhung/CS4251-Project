# ASTRA-sim NS-3 Results Report

Result directory: `astra-sim/extern/network_backend/ns-3/scratch/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 491,351,929 |
| Fastest rank completion (cycles) | 491,337,251 |
| Maximum exposed communication (cycles) | 491,351,585 |
| Completed network flows | 50,176 |
| Total bytes sent | 9,525,264,384 |
| Network-flow finish proxy | 75.739 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Comm time | 491,343,045.875 | 491,337,204.000 | 491,351,882.000 | 32 |
| GPU time | 344.000 | 344.000 | 344.000 | 32 |
| Total compute-communication overlap | 297.000 | 297.000 | 297.000 | 32 |
| Wall time | 491,343,092.875 | 491,337,251.000 | 491,351,929.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Comm time | 491,346,503.000 |
| 0 | GPU time | 344.000 |
| 0 | Total compute-communication overlap | 297.000 |
| 0 | Wall time | 491,346,550.000 |
| 1 | Comm time | 491,340,566.000 |
| 1 | GPU time | 344.000 |
| 1 | Total compute-communication overlap | 297.000 |
| 1 | Wall time | 491,340,613.000 |
| 2 | Comm time | 491,337,204.000 |
| 2 | GPU time | 344.000 |
| 2 | Total compute-communication overlap | 297.000 |
| 2 | Wall time | 491,337,251.000 |
| 3 | Comm time | 491,341,730.000 |
| 3 | GPU time | 344.000 |
| 3 | Total compute-communication overlap | 297.000 |
| 3 | Wall time | 491,341,777.000 |
| 4 | Comm time | 491,338,794.000 |
| 4 | GPU time | 344.000 |
| 4 | Total compute-communication overlap | 297.000 |
| 4 | Wall time | 491,338,841.000 |
| 5 | Comm time | 491,341,153.000 |
| 5 | GPU time | 344.000 |
| 5 | Total compute-communication overlap | 297.000 |
| 5 | Wall time | 491,341,200.000 |
| 6 | Comm time | 491,346,535.000 |
| 6 | GPU time | 344.000 |
| 6 | Total compute-communication overlap | 297.000 |
| 6 | Wall time | 491,346,582.000 |
| 7 | Comm time | 491,351,882.000 |
| 7 | GPU time | 344.000 |
| 7 | Total compute-communication overlap | 297.000 |
| 7 | Wall time | 491,351,929.000 |
| 8 | Comm time | 491,346,503.000 |
| 8 | GPU time | 344.000 |
| 8 | Total compute-communication overlap | 297.000 |
| 8 | Wall time | 491,346,550.000 |
| 9 | Comm time | 491,340,566.000 |
| 9 | GPU time | 344.000 |
| 9 | Total compute-communication overlap | 297.000 |
| 9 | Wall time | 491,340,613.000 |
| 10 | Comm time | 491,337,204.000 |
| 10 | GPU time | 344.000 |
| 10 | Total compute-communication overlap | 297.000 |
| 10 | Wall time | 491,337,251.000 |
| 11 | Comm time | 491,341,730.000 |
| 11 | GPU time | 344.000 |
| 11 | Total compute-communication overlap | 297.000 |
| 11 | Wall time | 491,341,777.000 |
| 12 | Comm time | 491,338,794.000 |
| 12 | GPU time | 344.000 |
| 12 | Total compute-communication overlap | 297.000 |
| 12 | Wall time | 491,338,841.000 |
| 13 | Comm time | 491,341,153.000 |
| 13 | GPU time | 344.000 |
| 13 | Total compute-communication overlap | 297.000 |
| 13 | Wall time | 491,341,200.000 |
| 14 | Comm time | 491,346,535.000 |
| 14 | GPU time | 344.000 |
| 14 | Total compute-communication overlap | 297.000 |
| 14 | Wall time | 491,346,582.000 |
| 15 | Comm time | 491,351,882.000 |
| 15 | GPU time | 344.000 |
| 15 | Total compute-communication overlap | 297.000 |
| 15 | Wall time | 491,351,929.000 |
| 16 | Comm time | 491,346,503.000 |
| 16 | GPU time | 344.000 |
| 16 | Total compute-communication overlap | 297.000 |
| 16 | Wall time | 491,346,550.000 |
| 17 | Comm time | 491,340,566.000 |
| 17 | GPU time | 344.000 |
| 17 | Total compute-communication overlap | 297.000 |
| 17 | Wall time | 491,340,613.000 |
| 18 | Comm time | 491,337,204.000 |
| 18 | GPU time | 344.000 |
| 18 | Total compute-communication overlap | 297.000 |
| 18 | Wall time | 491,337,251.000 |
| 19 | Comm time | 491,341,730.000 |
| 19 | GPU time | 344.000 |
| 19 | Total compute-communication overlap | 297.000 |
| 19 | Wall time | 491,341,777.000 |
| 20 | Comm time | 491,338,794.000 |
| 20 | GPU time | 344.000 |
| 20 | Total compute-communication overlap | 297.000 |
| 20 | Wall time | 491,338,841.000 |
| 21 | Comm time | 491,341,153.000 |
| 21 | GPU time | 344.000 |
| 21 | Total compute-communication overlap | 297.000 |
| 21 | Wall time | 491,341,200.000 |
| 22 | Comm time | 491,346,535.000 |
| 22 | GPU time | 344.000 |
| 22 | Total compute-communication overlap | 297.000 |
| 22 | Wall time | 491,346,582.000 |
| 23 | Comm time | 491,351,882.000 |
| 23 | GPU time | 344.000 |
| 23 | Total compute-communication overlap | 297.000 |
| 23 | Wall time | 491,351,929.000 |
| 24 | Comm time | 491,346,503.000 |
| 24 | GPU time | 344.000 |
| 24 | Total compute-communication overlap | 297.000 |
| 24 | Wall time | 491,346,550.000 |
| 25 | Comm time | 491,340,566.000 |
| 25 | GPU time | 344.000 |
| 25 | Total compute-communication overlap | 297.000 |
| 25 | Wall time | 491,340,613.000 |
| 26 | Comm time | 491,337,204.000 |
| 26 | GPU time | 344.000 |
| 26 | Total compute-communication overlap | 297.000 |
| 26 | Wall time | 491,337,251.000 |
| 27 | Comm time | 491,341,730.000 |
| 27 | GPU time | 344.000 |
| 27 | Total compute-communication overlap | 297.000 |
| 27 | Wall time | 491,341,777.000 |
| 28 | Comm time | 491,338,794.000 |
| 28 | GPU time | 344.000 |
| 28 | Total compute-communication overlap | 297.000 |
| 28 | Wall time | 491,338,841.000 |
| 29 | Comm time | 491,341,153.000 |
| 29 | GPU time | 344.000 |
| 29 | Total compute-communication overlap | 297.000 |
| 29 | Wall time | 491,341,200.000 |
| 30 | Comm time | 491,346,535.000 |
| 30 | GPU time | 344.000 |
| 30 | Total compute-communication overlap | 297.000 |
| 30 | Wall time | 491,346,582.000 |
| 31 | Comm time | 491,351,882.000 |
| 31 | GPU time | 344.000 |
| 31 | Total compute-communication overlap | 297.000 |
| 31 | Wall time | 491,351,929.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 44.360 us |
| Median FCT | 32.170 us |
| p95 FCT | 114.800 us |
| Maximum FCT | 477.060 us |
| Median standalone time | 31.494 us |
| Median FCT / standalone | 0.999x |
| p95 FCT / standalone | 1.217x |
| Maximum FCT / standalone | 4.806x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 KiB | 30,720 | 31.432 us | 32.662 us | 40.744 us | 31.494 us | 1.008x |
| 116.00 KiB | 14,336 | 35.156 us | 42.667 us | 67.837 us | 35.099 us | 1.062x |
| 1,000.00 KiB | 3,584 | 76.662 us | 272.858 us | 351.045 us | 73.046 us | 1.636x |
| 1.95 MiB | 1,536 | 122.186 us | 344.952 us | 477.060 us | 115.972 us | 1.619x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,383,808 |
| Observed queue interval | 42.300 us to 75.717 ms |
| Observed queue duration | 75.675 ms |
| Maximum sampled queue | 2.00 MiB |
| Maximum queue location | switch 38, port 1 |

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
| Packet trace interval | 4.751 us to 75.734 ms |
| Maximum sampled packet queue | 2.00 MiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 192 |
| SimSetting window | 1.91 MiB |
| Events | Dequ: 41,121,792, Enqu: 39,631,872, Recv: 41,121,792 |
| Bytes by event | Dequ: 20.74 GiB, Enqu: 19.30 GiB, Recv: 20.74 GiB |
| Observed interface utilization | 165 interfaces; mean 7.128%, max 17.045% |
| Matched packet queue durations | 39,518,756 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 512 ns |
| Maximum packet queue time | 83.145 us |
| Mean packet queue time | 122 ns |
| Unmatched/duplicate dequeues | 1,603,036 |
| Enqueue-key collisions | 113,116 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
