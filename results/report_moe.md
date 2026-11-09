# ASTRA-sim NS-3 Results Report

Result directory: `astra-sim/extern/network_backend/ns-3/scratch/output`

## Completion summary

| Metric | Result |
| --- | --- |
| ASTRA workload ranks with completion log | 32 |
| Total workload completion (cycles) | 592,970,125 |
| Fastest rank completion (cycles) | 592,932,800 |
| Maximum exposed communication (cycles) | 591,747,469 |
| Completed network flows | 335,360 |
| Total bytes sent | 8,175,157,248 |
| Network-flow finish proxy | 592.950 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Roofline statistics

Summary across ranks (arithmetic mean of ranks that logged each metric):

| Metric | Mean | Minimum | Maximum | Ranks reported |
| --- | --- | --- | --- | --- |
| Average compute utilization (%) | 79.379% | 79.379% | 79.379% | 32 |
| Average memory utilization (%) | 62.660% | 62.660% | 62.660% | 32 |
| Average operation intensity | 8,266.835 | 8,266.835 | 8,266.835 | 32 |
| Comm time | 592,795,572.750 | 592,777,801.000 | 592,815,126.000 | 32 |
| Compute bound percentage (%) | 52.882% | 52.882% | 52.882% | 32 |
| GPU time | 1,222,656.000 | 1,222,656.000 | 1,222,656.000 | 32 |
| Total compute-communication overlap | 1,067,657.000 | 1,067,657.000 | 1,067,657.000 | 32 |
| Wall time | 592,950,571.750 | 592,932,800.000 | 592,970,125.000 | 32 |

Per-rank values:

| Rank | Metric | Value |
| --- | --- | --- |
| 0 | Average compute utilization | 79.379% |
| 0 | Average memory utilization | 62.660% |
| 0 | Average operation intensity | 8,266.835 |
| 0 | Comm time | 592,777,801.000 |
| 0 | Compute bound percentage | 52.882% |
| 0 | GPU time | 1,222,656.000 |
| 0 | Total compute-communication overlap | 1,067,657.000 |
| 0 | Wall time | 592,932,800.000 |
| 1 | Average compute utilization | 79.379% |
| 1 | Average memory utilization | 62.660% |
| 1 | Average operation intensity | 8,266.835 |
| 1 | Comm time | 592,815,126.000 |
| 1 | Compute bound percentage | 52.882% |
| 1 | GPU time | 1,222,656.000 |
| 1 | Total compute-communication overlap | 1,067,657.000 |
| 1 | Wall time | 592,970,125.000 |
| 2 | Average compute utilization | 79.379% |
| 2 | Average memory utilization | 62.660% |
| 2 | Average operation intensity | 8,266.835 |
| 2 | Comm time | 592,797,865.000 |
| 2 | Compute bound percentage | 52.882% |
| 2 | GPU time | 1,222,656.000 |
| 2 | Total compute-communication overlap | 1,067,657.000 |
| 2 | Wall time | 592,952,864.000 |
| 3 | Average compute utilization | 79.379% |
| 3 | Average memory utilization | 62.660% |
| 3 | Average operation intensity | 8,266.835 |
| 3 | Comm time | 592,791,499.000 |
| 3 | Compute bound percentage | 52.882% |
| 3 | GPU time | 1,222,656.000 |
| 3 | Total compute-communication overlap | 1,067,657.000 |
| 3 | Wall time | 592,946,498.000 |
| 4 | Average compute utilization | 79.379% |
| 4 | Average memory utilization | 62.660% |
| 4 | Average operation intensity | 8,266.835 |
| 4 | Comm time | 592,777,801.000 |
| 4 | Compute bound percentage | 52.882% |
| 4 | GPU time | 1,222,656.000 |
| 4 | Total compute-communication overlap | 1,067,657.000 |
| 4 | Wall time | 592,932,800.000 |
| 5 | Average compute utilization | 79.379% |
| 5 | Average memory utilization | 62.660% |
| 5 | Average operation intensity | 8,266.835 |
| 5 | Comm time | 592,815,126.000 |
| 5 | Compute bound percentage | 52.882% |
| 5 | GPU time | 1,222,656.000 |
| 5 | Total compute-communication overlap | 1,067,657.000 |
| 5 | Wall time | 592,970,125.000 |
| 6 | Average compute utilization | 79.379% |
| 6 | Average memory utilization | 62.660% |
| 6 | Average operation intensity | 8,266.835 |
| 6 | Comm time | 592,797,865.000 |
| 6 | Compute bound percentage | 52.882% |
| 6 | GPU time | 1,222,656.000 |
| 6 | Total compute-communication overlap | 1,067,657.000 |
| 6 | Wall time | 592,952,864.000 |
| 7 | Average compute utilization | 79.379% |
| 7 | Average memory utilization | 62.660% |
| 7 | Average operation intensity | 8,266.835 |
| 7 | Comm time | 592,791,499.000 |
| 7 | Compute bound percentage | 52.882% |
| 7 | GPU time | 1,222,656.000 |
| 7 | Total compute-communication overlap | 1,067,657.000 |
| 7 | Wall time | 592,946,498.000 |
| 8 | Average compute utilization | 79.379% |
| 8 | Average memory utilization | 62.660% |
| 8 | Average operation intensity | 8,266.835 |
| 8 | Comm time | 592,777,801.000 |
| 8 | Compute bound percentage | 52.882% |
| 8 | GPU time | 1,222,656.000 |
| 8 | Total compute-communication overlap | 1,067,657.000 |
| 8 | Wall time | 592,932,800.000 |
| 9 | Average compute utilization | 79.379% |
| 9 | Average memory utilization | 62.660% |
| 9 | Average operation intensity | 8,266.835 |
| 9 | Comm time | 592,815,126.000 |
| 9 | Compute bound percentage | 52.882% |
| 9 | GPU time | 1,222,656.000 |
| 9 | Total compute-communication overlap | 1,067,657.000 |
| 9 | Wall time | 592,970,125.000 |
| 10 | Average compute utilization | 79.379% |
| 10 | Average memory utilization | 62.660% |
| 10 | Average operation intensity | 8,266.835 |
| 10 | Comm time | 592,797,865.000 |
| 10 | Compute bound percentage | 52.882% |
| 10 | GPU time | 1,222,656.000 |
| 10 | Total compute-communication overlap | 1,067,657.000 |
| 10 | Wall time | 592,952,864.000 |
| 11 | Average compute utilization | 79.379% |
| 11 | Average memory utilization | 62.660% |
| 11 | Average operation intensity | 8,266.835 |
| 11 | Comm time | 592,791,499.000 |
| 11 | Compute bound percentage | 52.882% |
| 11 | GPU time | 1,222,656.000 |
| 11 | Total compute-communication overlap | 1,067,657.000 |
| 11 | Wall time | 592,946,498.000 |
| 12 | Average compute utilization | 79.379% |
| 12 | Average memory utilization | 62.660% |
| 12 | Average operation intensity | 8,266.835 |
| 12 | Comm time | 592,777,801.000 |
| 12 | Compute bound percentage | 52.882% |
| 12 | GPU time | 1,222,656.000 |
| 12 | Total compute-communication overlap | 1,067,657.000 |
| 12 | Wall time | 592,932,800.000 |
| 13 | Average compute utilization | 79.379% |
| 13 | Average memory utilization | 62.660% |
| 13 | Average operation intensity | 8,266.835 |
| 13 | Comm time | 592,815,126.000 |
| 13 | Compute bound percentage | 52.882% |
| 13 | GPU time | 1,222,656.000 |
| 13 | Total compute-communication overlap | 1,067,657.000 |
| 13 | Wall time | 592,970,125.000 |
| 14 | Average compute utilization | 79.379% |
| 14 | Average memory utilization | 62.660% |
| 14 | Average operation intensity | 8,266.835 |
| 14 | Comm time | 592,797,865.000 |
| 14 | Compute bound percentage | 52.882% |
| 14 | GPU time | 1,222,656.000 |
| 14 | Total compute-communication overlap | 1,067,657.000 |
| 14 | Wall time | 592,952,864.000 |
| 15 | Average compute utilization | 79.379% |
| 15 | Average memory utilization | 62.660% |
| 15 | Average operation intensity | 8,266.835 |
| 15 | Comm time | 592,791,499.000 |
| 15 | Compute bound percentage | 52.882% |
| 15 | GPU time | 1,222,656.000 |
| 15 | Total compute-communication overlap | 1,067,657.000 |
| 15 | Wall time | 592,946,498.000 |
| 16 | Average compute utilization | 79.379% |
| 16 | Average memory utilization | 62.660% |
| 16 | Average operation intensity | 8,266.835 |
| 16 | Comm time | 592,777,801.000 |
| 16 | Compute bound percentage | 52.882% |
| 16 | GPU time | 1,222,656.000 |
| 16 | Total compute-communication overlap | 1,067,657.000 |
| 16 | Wall time | 592,932,800.000 |
| 17 | Average compute utilization | 79.379% |
| 17 | Average memory utilization | 62.660% |
| 17 | Average operation intensity | 8,266.835 |
| 17 | Comm time | 592,815,126.000 |
| 17 | Compute bound percentage | 52.882% |
| 17 | GPU time | 1,222,656.000 |
| 17 | Total compute-communication overlap | 1,067,657.000 |
| 17 | Wall time | 592,970,125.000 |
| 18 | Average compute utilization | 79.379% |
| 18 | Average memory utilization | 62.660% |
| 18 | Average operation intensity | 8,266.835 |
| 18 | Comm time | 592,797,865.000 |
| 18 | Compute bound percentage | 52.882% |
| 18 | GPU time | 1,222,656.000 |
| 18 | Total compute-communication overlap | 1,067,657.000 |
| 18 | Wall time | 592,952,864.000 |
| 19 | Average compute utilization | 79.379% |
| 19 | Average memory utilization | 62.660% |
| 19 | Average operation intensity | 8,266.835 |
| 19 | Comm time | 592,791,499.000 |
| 19 | Compute bound percentage | 52.882% |
| 19 | GPU time | 1,222,656.000 |
| 19 | Total compute-communication overlap | 1,067,657.000 |
| 19 | Wall time | 592,946,498.000 |
| 20 | Average compute utilization | 79.379% |
| 20 | Average memory utilization | 62.660% |
| 20 | Average operation intensity | 8,266.835 |
| 20 | Comm time | 592,777,801.000 |
| 20 | Compute bound percentage | 52.882% |
| 20 | GPU time | 1,222,656.000 |
| 20 | Total compute-communication overlap | 1,067,657.000 |
| 20 | Wall time | 592,932,800.000 |
| 21 | Average compute utilization | 79.379% |
| 21 | Average memory utilization | 62.660% |
| 21 | Average operation intensity | 8,266.835 |
| 21 | Comm time | 592,815,126.000 |
| 21 | Compute bound percentage | 52.882% |
| 21 | GPU time | 1,222,656.000 |
| 21 | Total compute-communication overlap | 1,067,657.000 |
| 21 | Wall time | 592,970,125.000 |
| 22 | Average compute utilization | 79.379% |
| 22 | Average memory utilization | 62.660% |
| 22 | Average operation intensity | 8,266.835 |
| 22 | Comm time | 592,797,865.000 |
| 22 | Compute bound percentage | 52.882% |
| 22 | GPU time | 1,222,656.000 |
| 22 | Total compute-communication overlap | 1,067,657.000 |
| 22 | Wall time | 592,952,864.000 |
| 23 | Average compute utilization | 79.379% |
| 23 | Average memory utilization | 62.660% |
| 23 | Average operation intensity | 8,266.835 |
| 23 | Comm time | 592,791,499.000 |
| 23 | Compute bound percentage | 52.882% |
| 23 | GPU time | 1,222,656.000 |
| 23 | Total compute-communication overlap | 1,067,657.000 |
| 23 | Wall time | 592,946,498.000 |
| 24 | Average compute utilization | 79.379% |
| 24 | Average memory utilization | 62.660% |
| 24 | Average operation intensity | 8,266.835 |
| 24 | Comm time | 592,777,801.000 |
| 24 | Compute bound percentage | 52.882% |
| 24 | GPU time | 1,222,656.000 |
| 24 | Total compute-communication overlap | 1,067,657.000 |
| 24 | Wall time | 592,932,800.000 |
| 25 | Average compute utilization | 79.379% |
| 25 | Average memory utilization | 62.660% |
| 25 | Average operation intensity | 8,266.835 |
| 25 | Comm time | 592,815,126.000 |
| 25 | Compute bound percentage | 52.882% |
| 25 | GPU time | 1,222,656.000 |
| 25 | Total compute-communication overlap | 1,067,657.000 |
| 25 | Wall time | 592,970,125.000 |
| 26 | Average compute utilization | 79.379% |
| 26 | Average memory utilization | 62.660% |
| 26 | Average operation intensity | 8,266.835 |
| 26 | Comm time | 592,797,865.000 |
| 26 | Compute bound percentage | 52.882% |
| 26 | GPU time | 1,222,656.000 |
| 26 | Total compute-communication overlap | 1,067,657.000 |
| 26 | Wall time | 592,952,864.000 |
| 27 | Average compute utilization | 79.379% |
| 27 | Average memory utilization | 62.660% |
| 27 | Average operation intensity | 8,266.835 |
| 27 | Comm time | 592,791,499.000 |
| 27 | Compute bound percentage | 52.882% |
| 27 | GPU time | 1,222,656.000 |
| 27 | Total compute-communication overlap | 1,067,657.000 |
| 27 | Wall time | 592,946,498.000 |
| 28 | Average compute utilization | 79.379% |
| 28 | Average memory utilization | 62.660% |
| 28 | Average operation intensity | 8,266.835 |
| 28 | Comm time | 592,777,801.000 |
| 28 | Compute bound percentage | 52.882% |
| 28 | GPU time | 1,222,656.000 |
| 28 | Total compute-communication overlap | 1,067,657.000 |
| 28 | Wall time | 592,932,800.000 |
| 29 | Average compute utilization | 79.379% |
| 29 | Average memory utilization | 62.660% |
| 29 | Average operation intensity | 8,266.835 |
| 29 | Comm time | 592,815,126.000 |
| 29 | Compute bound percentage | 52.882% |
| 29 | GPU time | 1,222,656.000 |
| 29 | Total compute-communication overlap | 1,067,657.000 |
| 29 | Wall time | 592,970,125.000 |
| 30 | Average compute utilization | 79.379% |
| 30 | Average memory utilization | 62.660% |
| 30 | Average operation intensity | 8,266.835 |
| 30 | Comm time | 592,797,865.000 |
| 30 | Compute bound percentage | 52.882% |
| 30 | GPU time | 1,222,656.000 |
| 30 | Total compute-communication overlap | 1,067,657.000 |
| 30 | Wall time | 592,952,864.000 |
| 31 | Average compute utilization | 79.379% |
| 31 | Average memory utilization | 62.660% |
| 31 | Average operation intensity | 8,266.835 |
| 31 | Comm time | 592,791,499.000 |
| 31 | Compute bound percentage | 52.882% |
| 31 | GPU time | 1,222,656.000 |
| 31 | Total compute-communication overlap | 1,067,657.000 |
| 31 | Wall time | 592,946,498.000 |

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 56.535 us |
| Median FCT | 60.302 us |
| p95 FCT | 60.890 us |
| Maximum FCT | 147.934 us |
| Median standalone time | 60.327 us |
| Median FCT / standalone | 1.000x |
| p95 FCT / standalone | 1.000x |
| Maximum FCT / standalone | 1.168x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 B | 14,336 | 60.030 us | 60.030 us | 60.055 us | 60.243 us | 0.996x |
| 2.00 KiB | 260,096 | 60.302 us | 60.302 us | 60.418 us | 60.327 us | 1.000x |
| 16.00 KiB | 28,672 | 60.890 us | 60.890 us | 61.881 us | 60.928 us | 1.000x |
| 128.00 KiB | 30,720 | 35.641 us | 55.829 us | 56.685 us | 35.616 us | 0.999x |
| 1.95 MiB | 1,536 | 119.863 us | 142.051 us | 147.934 us | 115.972 us | 1.034x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 1,290,848 |
| Observed queue interval | 1.687 ms to 592.929 ms |
| Observed queue duration | 591.242 ms |
| Maximum sampled queue | 88.77 KiB |
| Maximum queue location | switch 34, port 2 |

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
| Trace records recognized | 151,717,760 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 10 ns to 592.950 ms |
| Maximum sampled packet queue | 89.05 KiB |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 128 |
| SimSetting window | 4.31 MiB |
| Events | Dequ: 51,014,400, Enqu: 49,688,960, Recv: 51,014,400 |
| Bytes by event | Dequ: 24.41 GiB, Enqu: 23.17 GiB, Recv: 24.41 GiB |
| Observed interface utilization | 101 interfaces; mean 1.750%, max 2.483% |
| Matched packet queue durations | 49,525,051 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 80 ns |
| Maximum packet queue time | 3.572 us |
| Mean packet queue time | 47 ns |
| Unmatched/duplicate dequeues | 1,489,349 |
| Enqueue-key collisions | 163,909 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
