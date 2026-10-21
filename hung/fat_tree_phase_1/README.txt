FAT-TREE PHASE 1 PACKAGE
=======================
The scripts and topology for the 32-GPU two-tier fat-tree (leaf-spine) used in Phase 1,
so a teammate can rebuild it and run jobs on it.

DESIGN
  32 GPUs (nodes 0-31), 8 leaf switches (32-39), 2 spine switches (40-41).
  4 GPUs under each leaf; every leaf links to both spines.
  48 links: 32 GPU-to-leaf and 16 leaf-to-spine, all 200 Gbps.
  Delay: GPU-to-leaf 0.005 ms, leaf-to-spine 0.0125 ms (the 0.0125 ms came from the
  simulator docs' example; it is a design choice, not a measurement).
  Each leaf: 800 Gbps down, 400 Gbps up = 2:1 oversubscribed.
  Rank i runs on node i.

FILES
  gen_fattree.py    writes the topology file from a few numbers
  fattree_32.txt    the generated topology (50 lines, header "42 10 48")
  run_trace.sh      runs a job and saves the results to /work/results/<name>/
  analyze_run.py    splits flows into same-leaf / cross-leaf and prints peak queue per switch
  metrics.py        prints the 15 comparison numbers from a results folder (works for any topology)
  port_peaks.py     lists the switch ports with the longest queues, and what each faces
  fct_by_size.py    groups flows by size and kind. Dense trace only (assumes DP groups of 8)
  SHA256SUMS        fingerprints to check the files arrived unchanged

ASSUMES
  Docker container, ASTRA-sim repo at /app/astra-sim (commit 4ce9ecfe746a3ee5fe47559a11d91644d641fa7f),
  ns-3 backend already built, and a shared folder at /work. Put these files in /work/fattree/.
  If your paths differ, edit the variables at the top of run_trace.sh.

REBUILD STEPS (inside the container)
  1. mkdir -p /work/fattree, copy all files there, then:
       cd /work/fattree && sha256sum -c SHA256SUMS
  2. Regenerate the topology and compare:
       python3 gen_fattree.py --gpus 32 --leaves 8 --spines 2 > /tmp/check.txt
       diff /tmp/check.txt fattree_32.txt && echo same
  3. Network config = the stock config with ONE line changed:
       cp /app/astra-sim/extern/network_backend/ns-3/scratch/config/config_clos.txt /work/fattree/config_fattree32.txt
       sed -i 's#^TOPOLOGY_FILE .*#TOPOLOGY_FILE /work/fattree/fattree_32.txt#' /work/fattree/config_fattree32.txt
       diff /app/astra-sim/extern/network_backend/ns-3/scratch/config/config_clos.txt /work/fattree/config_fattree32.txt
     (diff must show exactly one changed line)
  4. Logical topology (the stock 16-node file with 16 changed to 32):
       sed 's/16/32/' /app/astra-sim/examples/network/ns3/sample_16nodes_1D.json > /work/fattree/logical_32nodes_1D.json
  5. This simulator version has no "build.sh -r". It needs a file missing from a fresh clone:
       echo 0 > /app/astra-sim/extern/network_backend/ns-3/scratch/output/flow.txt
  6. Run a job (replace the paths; each trace has its own groups .json):
       LOGICAL=/work/fattree/logical_32nodes_1D.json COMM=<groups>.json \
         bash /work/fattree/run_trace.sh /work/fattree/config_fattree32.txt <trace prefix without .N.et> <results name> 4
     The simulator overwrites its output folder on every run. run_trace.sh copies the results out. Run ONE simulation at a time.
  7. Measure:
       python3 /work/fattree/metrics.py /work/results/<results name>
  Variant with doubled leaf-to-spine speed (the capacity-vs-structure test):
       python3 gen_fattree.py --gpus 32 --leaves 8 --spines 2 --uplink-bw 400Gbps > fattree_32_up400.txt
     then repeat step 3 with that file.

REPRODUCIBILITY CHECK
  Dense trace dense32_validmb on this fat-tree: slowest rank = 111512144 cycles,
  50176 flows, 9525264384 bytes. With 400 Gbps uplinks: 107753058 cycles.
  Same inputs gave byte-identical results on a rerun (tested once, one machine).

NOT VERIFIED
  - the fifth field on each link line (copied as 0 from the stock topology file)
  - what CC_MODE 12 is (stock config; keep it identical across topologies)
  - how the simulator picks between the two spines
  - port-to-link mapping in port_peaks.py (assumes port p = the node's p-th link in the topology file)
  - the scripts were written from copies of what ran in the container and tested on stand-in data
