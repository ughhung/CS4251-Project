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
| Network-flow finish proxy | 491.352 ms |

The network-flow finish proxy is `max(start_ns + fct_ns)` and is not a substitute for ASTRA-sim's per-rank workload completion metric.

## Flow-completion metrics

| Metric | Value |
| --- | --- |
| Mean FCT | 313.170 us |
| Median FCT | 152.862 us |
| p95 FCT | 386.410 us |
| Maximum FCT | 5.522 ms |
| Median standalone time | 114.192 us |
| Median FCT / standalone | 1.338x |
| p95 FCT / standalone | 1.346x |
| Maximum FCT / standalone | 6.989x |

## FCT by message size

| Size | Flows | Median FCT | p95 FCT | Max FCT | Median standalone | Mean slowdown |
| --- | --- | --- | --- | --- | --- | --- |
| 32.00 KiB | 30,720 | 152.862 us | 153.581 us | 168.786 us | 114.192 us | 1.339x |
| 116.00 KiB | 14,336 | 71.872 us | 136.734 us | 137.985 us | 70.798 us | 1.017x |
| 1,000.00 KiB | 3,584 | 386.052 us | 453.422 us | 454.192 us | 374.368 us | 1.032x |
| 1.95 MiB | 1,536 | 5.504 ms | 5.511 ms | 5.522 ms | 790.017 us | 6.969x |

## Queue metrics

| Metric | Result |
| --- | --- |
| Queue records | 121,119,772 |
| Observed queue interval | 10.700 us to 491.296 ms |
| Observed queue duration | 491.286 ms |
| Maximum sampled queue | 326.79 KiB |
| Maximum queue location | switch 35, port 3 |

The queue interval is the time span covered by non-empty queue records; it is not per-flow queueing duration.

## PFC and flow inputs

| Metric | Result |
| --- | --- |
| PFC events | 0 |
| Static flows declared | 0 |
| Trace nodes listed | 5 |

## Packet trace

| Metric | Result |
| --- | --- |
| Trace records recognized | 7,449,600 |
| Invalid/unrecognized records | 0 |
| Trace format recognized | yes |
| Packet trace interval | 12 ns to 491.347 ms |
| Maximum sampled packet queue | 0.00 B |
| Maximum packet size | 1.01 KiB |
| SimSetting interface entries | 128 |
| SimSetting window | 566.89 KiB |
| Events | Dequ: 2,979,840, Enqu: 1,489,920, Recv: 2,979,840 |
| Bytes by event | Dequ: 1.50 GiB, Enqu: 68.20 MiB, Recv: 1.50 GiB |
| Observed interface utilization | 5 interfaces; mean 21.016%, max 21.016% |
| Matched packet queue durations | 1,489,856 |
| Median packet queue time | 0 ns |
| p95 packet queue time | 290 ns |
| Maximum packet queue time | 331 ns |
| Mean packet queue time | 73 ns |
| Unmatched/duplicate dequeues | 1,489,984 |
| Enqueue-key collisions | 64 |

This packet-trace parser reads the NS-3 `TraceFormat` binary records. Interface utilization is computed from Dequ bytes over the trace interval and is limited to interfaces included in `trace.txt`; it is not a whole-network utilization measure unless all relevant nodes were traced.

## Scaling

This report describes one result directory. Supply separate 8-, 16-, and 32-rank result directories to compare scaling; rank count cannot be inferred reliably from the network output alone.
