#!/bin/bash
# Usage: bash run_case.sh <network_config> <collective_folder> <results_label> <gpus_per_leaf>
set -e
set -o pipefail
CONFIG=$1; COLL=$2; LABEL=$3; PER_LEAF=$4
ROOT=/app/astra-sim
NS3=$ROOT/extern/network_backend/ns-3
WORKLOAD=$ROOT/examples/workload/microbenchmarks/$COLL/16npus_1MB/$COLL
SYSTEM=$ROOT/examples/system/native_collectives/Ring_4chunks.json
LOGICAL=$ROOT/examples/network/ns3/sample_16nodes_1D.json
MEMORY=$ROOT/examples/remote_memory/analytical/no_memory_expansion.json
OUT=/work/results/$LABEL
mkdir -p "$OUT"
cd "$NS3/build/scratch"
./ns3.42-AstraSimNetwork-default \
  --workload-configuration=$WORKLOAD \
  --system-configuration=$SYSTEM \
  --network-configuration=$CONFIG \
  --remote-memory-configuration=$MEMORY \
  --logical-topology-configuration=$LOGICAL \
  --comm-group-configuration=empty 2>&1 | tee "$OUT/ns3_run.log"
cp $NS3/scratch/output/{fct.txt,qlen.txt,pfc.txt,mix.tr,flow.txt,trace.txt} "$OUT/"
cp "$CONFIG" "$OUT/config_used.txt"
cp "$(grep '^TOPOLOGY_FILE' "$CONFIG" | awk '{print $2}' | tr -d '\r')" "$OUT/topology_used.txt"
echo "workload=$WORKLOAD system=$SYSTEM logical=$LOGICAL" > "$OUT/inputs.txt"
python3 /work/fattree/analyze_run.py "$OUT/fct.txt" "$OUT/qlen.txt" $PER_LEAF | tee "$OUT/analysis.txt"
echo "distinct src/dst pairs: $(awk '{print $1,$2}' "$OUT/fct.txt" | sort -u | wc -l)  flows: $(wc -l < "$OUT/fct.txt")"
grep finished "$OUT/ns3_run.log" | sed 's/.*sys\[[0-9]*\] finished, \([0-9]*\) cycles.*/\1/' | sort -n | awk 'NR==1{lo=$1} {hi=$1; n++} END{print "ranks:", n, "fastest:", lo, "slowest (= completion time):", hi}'
