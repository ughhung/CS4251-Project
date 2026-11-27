• I’d prioritize two runs for the torus study, plus three matched fat-tree runs if the team does not already have
  them. As of November 27, there are 50 reports for the 70 torus pairs. The biggest gap is the one the instructor
  identified in Report 2: can you predict which network change will help a workload before seeing its completion
  time, and can you show why? Filling the remaining 20 cells would do less to answer that question than testing
  one new prediction. Report 2 feedback (feedback/CN-proj/project-report-2-feedback.txt) · Final report
  expectations (feedback/CN-proj/final-report-expectations.txt)

  ## 1. Run dense and uniform MoE on a torus with --twist 2

  This is my first choice for the torus contribution. You already measured the ordinary torus (--twist 0) and a
  torus whose eight vertical wraparound links shift by four columns (--twist 4). An intermediate shift changes
  only the destination of those eight links. Keep the 8×4 grid, linear placement, 200 Gb/s rate, 500 ns host and
  fabric delays, trace files, and collective configuration fixed. The generator already supports the change.
  Google’s TPU v4 paper provides the research motivation: its authors explicitly evaluated twisted wiring with an
  all-to-all microbenchmark. Your contribution is testing whether the actual communication partners in two
  different training traces predict the benefit on your 2D fabric. Topology generator (scripts/gen_topo.py) ·
  Jouppi et al., TPU v4, §2.3 and Fig. 6

  I calculated these distances from the physical wiring and the actual communicator files. A fabric hop is one
  switch-to-switch link. Each dense ring-neighbor edge or distinct MoE expert pair gets equal weight.

   Vertical wrap            Fabric          Mean hops        Mean hops    Dense completion,          Uniform MoE
   shift                  diameter      between dense      between the             M cycles        completion, M
                                       ring neighbors          112 MoE                                    cycles
                                                          expert pairs
  ━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━
   0 columns                     6               1.00             3.43                17.93                43.40
  ───────────────  ────────────────  ─────────────────  ───────────────  ───────────────────  ───────────────────
   2 columns                     5               1.25             3.14         Proposed run         Proposed run
  ───────────────  ────────────────  ─────────────────  ───────────────  ───────────────────  ───────────────────
   4 columns                     4               1.25             2.29                18.54                37.23

  Write down the prediction before launching. For uniform MoE, I expect shift 2 to finish between shifts 0 and 4.
  For dense, I expect base to retain its advantage, with much less separation between shifts 2 and 4. The reason
  this is a useful test is that diameter improves from 5 to 4 while the dense partner distance stays exactly
  1.25. If dense also speeds up substantially, or MoE falls outside the predicted ordering, average partner
  distance is an incomplete explanation. The next quantity to examine is how many simultaneous exchanges share
  each link in each round. These distances describe available shortest paths; the simulator determines which
  paths carry traffic. Dense communicators (astra-sim/traces/baseline/dense32_validmb.json) · MoE expert pairs
  (astra-sim/traces/moe32/moe32_top1_uniform_paircoll.json)

  ## 2. Make the fat-tree comparison fair before claiming which topology to select

  For the overall project, this takes precedence if nobody on the team has matched fat-tree results. The Phase 1
  package documents 5 µs GPU-to-leaf delay, 12.5 µs leaf-to-spine delay and a 1D logical configuration. The
  reference torus uses 0.5 µs per link and a different logical configuration. Comparing those completion times
  directly mixes physical wiring, propagation delay and collective mapping. The package also already documents a
  dense run with doubled uplink bandwidth, so the first step is to recover its exact configuration and reuse any
  matching team runs. Fat-tree Phase 1 README (hung/fat_tree_phase_1/README.txt) · Torus sweep configurations
  (topologies/torus_list.txt)

  If matched results are missing, run balanced dense, uniform MoE and Zipf MoE on the two-spine fat-tree. Use the
  same trace hashes, logical topology, ring configuration, 200 Gb/s link rate, 500 ns delays and transport
  settings as the base torus. Keep the differences inherent to each physical design and report their switch and
  link counts. This gives three specific hypotheses:

   Trace             What to predict and measure on the fat-tree
  ━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Balanced dense    Four consecutive GPUs share a leaf. Ring exchanges within a leaf avoid the uplinks; cross-
                     leaf exchanges share them. Split flows by same-leaf versus cross-leaf and compare FCT
                     within the same message-size bin.
  ────────────────  ─────────────────────────────────────────────────────────────────────────────────────────────
   Uniform MoE       With linear placement, each expert exchange reaches a peer on another leaf. Four 200 Gb/s
                     GPU links can offer 800 Gb/s to a leaf with 400 Gb/s of uplink capacity. Predict uplink
                     queueing during rounds when simultaneous demand exceeds that capacity. Measure those
                     rounds.
  ────────────────  ─────────────────────────────────────────────────────────────────────────────────────────────
   Zipf MoE          Expert 0 receives 2.36× the average expert’s modeled traffic and compute. Predict that the
                     busiest destination leaf or GPU-facing port will differ from the uniform control. Identify
                     the port from the rank map and check whether it actually queues. If the extra time instead
                     appears in expert compute, report that outcome.

  The research basis is complementary. Fat-tree work explains why multipath capacity across a cut matters; Tutel
  explains why expert routing changes both communication and computation. Neither implies a universal winner. If
  the matched uniform-MoE run shows sustained uplink queues, the next targeted modification is one run doubling
  only leaf-to-spine bandwidth to 400 Gb/s. A reduction in both queueing and workload time supports the uplink-
  capacity explanation. A queue reduction with little change in completion means that queue had little influence
  on the critical path. Al-Fares et al., A Scalable, Commodity Data Center Network Architecture · Hwang et al.,
  Tutel · Project MoE trace construction (astra-sim/traces/moe32/README.md)

  ## 3. Get more evidence from the runs you already have

  • For the straggler, put compute time beside job time. On the base torus, moving GPU 0 from baseline to 10×
    adds 3.67 million GPU compute cycles, while the job grows by 32.81 million cycles. Even the fastest rank
    finishes at 49.56 million cycles, versus 17.93 million for the balanced job. That establishes that the
    perturbation reaches the other ranks. It does not establish that the remaining 29.14 million cycles are all
    network queueing. The most informative diagnostic is one affected collective: when each participant became
    ready, when its first transfer started, and when its last transfer finished. Use existing logs if they
    contain those events; otherwise instrument just the balanced and 10× base pair. I would do this before trying
    another straggler rank or multiplier. Balanced dense report (results/report_baseline_torus_base_uniform.md) ·
    10× report (results/report_straggler_torus_base_uniform.md)

  • For topology selection, make one figure that connects prediction to outcome. Plot trace-specific partner
    distance against completion for shifts 0, 2 and 4, with separate series for dense and uniform MoE. For MoE,
    also compute bytes × shortest-path hops per exchange round from the pair sizes. This matters especially for
    Zipf, where a large transfer to a hot expert counts more than a small transfer. The existing gen_topo.py
    rings helper hardcodes rank groups that differ from the dense trace’s communicator file; use the actual trace
    groups for the figure. Ring helper (scripts/gen_topo.py) · MoE pair-size generator (astra-sim/traces/moe32/
    make_moe_top1_paircoll.py)

  • For the capacity criticism, use a time window and a named link. On one representative collective, show bytes
    arriving at a leaf, uplink capacity over that interval, and the queue while the burst drains. That directly
    explains how a job can have low average utilization and still experience congestion. A numerical claim about
    supporting “5–6× more workload” would require an offered-load experiment and an explicit acceptable
    completion-time or slowdown threshold. The existing results support a burst-congestion analysis without that
    claim. Instructor’s capacity feedback (feedback/CN-proj/project-report-2-feedback.txt)

  My stopping rule: spend the next two runs on shift 2, or the next five if the matched fat-tree baselines are
  missing. Defer the remaining random-placement cells and documented stalls. The final paper will have a stronger
  answer if it can show one prediction that held, one condition where it stopped holding, and a measurement that
  explains the difference.
