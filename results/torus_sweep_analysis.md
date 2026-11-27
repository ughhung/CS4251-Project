# Which torus fits a 32-GPU training trace?

The balanced dense trace runs fastest when its collective partners occupy neighboring switches. The mixture-of-experts (MoE) traces benefit from a different property: shorter paths to a wider set of peers. Twisting the torus reduces completion time for both MoE traces, yet slightly increases it for balanced dense training. Slowing one dense rank changes the picture again. At 10× compute time on GPU 0, all five equal-delay layouts finish within 2.3% of each other.

## Experimental comparison

The sweep varies 14 physical configurations across five 32-rank traces. The reference is an 8×4 torus with one GPU per switch, 200 Gb/s links, 500 ns propagation delay per link, linear rank placement and ring collectives. Compare across topologies with the trace fixed to measure a design change. Compare each straggler with balanced dense, and Zipf MoE with uniform MoE, to measure a workload change. The dense and MoE traces perform different work. [Sweep configurations](../topologies/torus_list.txt) · [Generator](../scripts/gen_topo.py) · [Dense trace settings](../astra-sim/traces/baseline/instructions.md) · [MoE trace settings](../astra-sim/traces/moe32/README.md)

**Table 1. Workload completion in millions of simulator cycles, rounded to two decimals.** Each value comes from the report’s total workload completion across all 32 ranks. A dash means no matching report at the time of review. Coverage on November 26, 2026 was 44 of 70 pairs. The two straggler columns give the compute-time multiplier applied to GPU 0. Each report filename follows `report_<trace>_<topology>.md`; trace names in column order are `baseline`, `straggler_1_5`, `straggler`, `moe32_uniform` and `moe32_zipf075`.

| Topology | Dense | GPU 0 at 1.5× | GPU 0 at 10× | MoE uniform | MoE Zipf |
|---|---:|---:|---:|---:|---:|
| torus_base_uniform | 17.93 | 31.50 | 50.75 | 43.40 | 45.54 |
| torus_twisted_uniform | 18.54 | 30.69 | 51.43 | 37.23 | 40.35 |
| torus_aligned_uniform | 36.32 | 37.65 | 50.90 | 43.07 | 44.79 |
| torus_random1_uniform | 45.38 | 45.56 | 50.28 | — | — |
| torus_random2_uniform | 45.51 | 46.36 | 51.23 | — | 66.75 |
| torus_base_hostlink | 14.87 | 40.19 | 53.10 | 38.99 | 40.51 |
| torus_twisted_hostlink | 15.45 | 41.81 | 52.86 | 27.60 | 35.02 |
| torus_aligned_hostlink | 38.80 | 34.65 | 53.37 | — | 29.53 |
| torus_random1_hostlink | 43.26 | 44.36 | 48.27 | — | — |
| torus_random2_hostlink | 45.43 | 45.54 | 53.16 | — | — |
| torus2_base | 22.96 | 46.60 | — | — | — |
| torus2_aligned | — | — | — | — | — |
| torus2_random1 | — | — | — | — | — |
| torus2_random2 | — | — | — | — | — |

## Dense training already uses the base torus well

A ring repeatedly exchanges data between consecutive members, including the last and first. In the trace communicator order, ranks 0 through 7 form one ring, and ranks 0, 8, 16 and 24 form another. Linear placement puts the first ring on one physical row and the second on one column. The other groups repeat that pattern. Every consecutive pair is one switch hop apart, including the wraparound. This predicts low contention and little scope for a fabric shortcut to improve balanced dense training. [Dense communicators](../astra-sim/traces/baseline/dense32_validmb.json) · [Physical placement](../scripts/gen_topo.py)

The placement called `aligned` was intended to keep collective partners close. Its mapping assumes four consecutive ranks form a group and maps those ranks onto a column. With the trace's actual groups, partners such as ranks 0 and 8 move from adjacent switches to switches two hops apart. Both runs send exactly 9,525,264,384 completed-flow bytes. Under the changed placement, p95 flow completion time rises from 47.05 to 100.40 µs, the maximum sampled queue rises from 1.11 to 739.57 KiB, and the workload takes 2.03× as long. Both random placements take about 2.53× as long as base. The controlled change and these measurements support using the communicator file to place ranks for this workload. [Base dense](report_baseline_torus_base_uniform.md) · [Aligned dense](report_baseline_torus_aligned_uniform.md) · [Random seed 1](report_baseline_torus_random1_uniform.md) · [Random seed 2](report_baseline_torus_random2_uniform.md)

## MoE benefits from shortening paths between expert peers

In the MoE trace each rank meets seven expert-parallel peers in seven pairwise rounds. A physical row optimized for consecutive ring partners need not bring all seven peers close. The twist moves the far end of each of the eight vertical wraparound links by four columns while preserving link count, rate and placement. Twisted tori have a precedent in the 3D TPU v4 system. Here the prediction can be tested directly on the project's 2D graph: shortening paths for the trace's expert pairs should reduce the cost of their exchanges. [MoE trace construction](../astra-sim/traces/moe32/README.md) · [Topology generator](../scripts/gen_topo.py) · [Jouppi et al., TPU v4](https://arxiv.org/abs/2304.01433)

Counting each of the 112 distinct two-rank communicators once, the mean shortest switch-to-switch distance falls from 3.43 to 2.29 hops. The fabric diameter falls from six hops to four. These are graph calculations with equal weight per pair. Actual routed paths and byte-weighted traffic could differ. On equal-delay links, twisting reduces completion time by 14.2% for uniform MoE and 11.4% for Zipf. Their p95 flow completion times fall from 11.90 to 11.10 µs and from 12.47 to 11.66 µs, respectively. Zipf’s maximum sampled queue barely changes (50.20 versus 50.61 KiB). Shorter available paths and faster flow completion support a locality explanation, while the peak queue alone would miss the improvement. The same twist makes balanced dense 3.4% slower. [Expert pairs](../astra-sim/traces/moe32/moe32_top1_uniform_paircoll.json) · [Uniform base](report_moe32_uniform_torus_base_uniform.md) · [Uniform twisted](report_moe32_uniform_torus_twisted_uniform.md) · [Zipf base](report_moe32_zipf075_torus_base_uniform.md) · [Zipf twisted](report_moe32_zipf075_torus_twisted_uniform.md)

The Zipf trace tests expert imbalance. It preserves the pair schedule, total modeled remote expert bytes and total expert operations, while assigning the busiest expert 2.36× the mean traffic and compute work. Completion takes 4.9% longer than uniform MoE on the base fabric and 8.4% longer on the twisted fabric at equal delay. Skew affects both incoming traffic and computation at the hot expert. The two contributions cannot be separated with this control. [MoE workload definition](../astra-sim/traces/moe32/README.md) · [GShard, motivation for studying expert imbalance](https://arxiv.org/abs/2006.16668)

## GPU 0 is the straggler in both dense variants

A byte comparison of all 32 rank files against dense baseline found that only `dense32_validmb.0.et` changes in either variant. Applying the trace generator’s compute-node scaling to baseline rank 0 reproduces all 344 changed nodes in each file. The factor is 1.5 for `straggler_1_5` and 10 for `straggler`. The generator scales operation count and tensor size together to model a longer compute time. The simulated network sees the same dense byte volume, but a different schedule of arrivals at collectives. [Trace generator](../astra-sim/traces/straggler/make_straggler.py) · [GPU 0 at 1.5×](../astra-sim/traces/straggler_1_5/dense32_validmb.0.et) · [GPU 0 at 10×](../astra-sim/traces/straggler/dense32_validmb.0.et)

**Table 2. Measured rank GPU time, network behavior and job completion on the base equal-delay torus.** GPU time is the logged compute metric for an individual rank. Completion includes the time the workload spends waiting for communication. All three runs send 9,525,264,384 completed-flow bytes. [Dense](report_baseline_torus_base_uniform.md) · [GPU 0 at 1.5×](report_straggler_1_5_torus_base_uniform.md) · [GPU 0 at 10×](report_straggler_torus_base_uniform.md)

| Trace | Rank 0 GPU cycles | Rank 1 GPU cycles | p95 flow slowdown vs. standalone | Max sampled queue (KiB) | Completion (M cycles) |
|---|---:|---:|---:|---:|---:|
| Dense | 407,092 | 407,092 | 1.022× | 1.11 | 17.93 |
| GPU 0 at 1.5× | 610,744 | 407,092 | 3.183× | 396.59 | 31.50 |
| GPU 0 at 10× | 4,073,040 | 407,092 | 4.104× | 791.16 | 50.75 |

In the 10× trace, the fastest rank finishes at 49.56 million cycles, far later than the balanced job's 17.93 million. Changing one rank’s compute changes when its peers can complete dependent collectives. The flow slowdown and queue measurements show a network timing effect as well. Isolating how much time is lost waiting for a participant versus waiting in queues would require per-collective timing. Placement still matters at 1.5×, where base takes 31.50 million cycles and random seed 2 takes 46.36 million. At 10× the equal-delay layouts span only 50.28–51.43 million cycles. For that trace, changing placement offers little leverage in the tested configurations. [Base, GPU 0 at 10×](report_straggler_torus_base_uniform.md) · [Random seed 2, GPU 0 at 1.5×](report_straggler_1_5_torus_random2_uniform.md)

## Endpoint latency, switch sharing and limits on interpretation

Reducing only GPU-to-switch propagation delay from 500 ns to 1 ns on base wiring cuts completion by 17.1% for dense, 10.2% for uniform MoE and 11.0% for Zipf. With GPU 0 at 1.5× and 10× compute time, completion instead increases by 27.6% and 4.6%. The mechanism behind that reversal remains open. With 1 ns host links, the twist still improves both MoE workloads against their matching base, by 29.2% for uniform and 13.6% for Zipf. Placement can help Zipf further in this regime: the aligned run finishes in 29.53 million cycles versus 35.02 million for twisted. Its uniform-MoE counterpart has no report, limiting the comparison. [Host-link definitions](../topologies/torus_list.txt) · [Base, GPU 0 at 1.5×](report_straggler_1_5_torus_base_hostlink.md) · [Twisted uniform MoE](report_moe32_uniform_torus_twisted_hostlink.md) · [Twisted Zipf](report_moe32_zipf075_torus_twisted_hostlink.md) · [Aligned Zipf](report_moe32_zipf075_torus_aligned_hostlink.md)

The two-GPU-per-switch experiment tests whether local switch sharing can reduce fabric traversal. It also changes the grid to 4×4, the host-link delay to 100 ns, the logical dimensions and the collective configuration. Its two completed base runs take 22.96 million cycles for dense and 46.60 million for GPU 0 at 1.5×. These measurements describe the combined configuration. Isolating the contribution of switch sharing would require additional controls. [Configuration sets](../topologies/torus_list.txt) · [Two GPUs per switch, dense](report_baseline_torus2_base.md) · [Two GPUs per switch, GPU 0 at 1.5×](report_straggler_1_5_torus2_base.md)

The proposal asked when a targeted network change helps a particular training workload. The sweep answers that question most directly where one change can be tied to the partners in the trace. Preserve one-hop ring neighbors for balanced dense training, and consider shortcuts where expert exchanges span several switch hops. A separate capacity claim would require an offered-load experiment with a defined completion-time or queueing target. Average utilization over a whole iteration can coexist with large queues during bursts and cannot establish how many more jobs the fabric will support. [Report 2 feedback](../feedback/CN-proj/project-report-2-feedback.txt)
