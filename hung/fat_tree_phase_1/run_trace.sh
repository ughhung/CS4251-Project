#!/bin/bash
# Usage: [LOGICAL=file] [COMM=file] bash run_trace.sh <network_config> <workload_prefix> <label> <gpus_per_leaf> [system_config]
set -e
set -o pipefail
CONFIG=$1; WORKLOAD=$2; LABEL=$3; PER_LEAF=$4
ROOT=/app/astra-sim
NS3=$ROOT/extern/network_backend/ns-3
SYSTEM=${5:-$ROOT/examples/system/native_collectives/Ring_4chunks.json}
LOGICAL=${LOGICAL:-$ROOT/examples/network/ns3/sample_16nodes_1D.json}
COMM=${COMM:-empty}
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
  --comm-group-configuration=$COMM 2>&1 | tee "$OUT/ns3_run.log"
cp $NS3/scratch/output/{fct.txt,qlen.txt,pfc.txt,mix.tr,flow.txt,trace.txt} "$OUT/"
cp "$CONFIG" "$OUT/config_used.txt"
cp "$(grep '^TOPOLOGY_FILE' "$CONFIG" | awk '{print $2}' | tr -d '\r')" "$OUT/topology_used.txt"
cp "$LOGICAL" "$OUT/logical_used.json"
cp "$SYSTEM" "$OUT/system_used.json"
if [ -f "$COMM" ]; then cp "$COMM" "$OUT/comm_groups.json"; fi
echo "workload=$WORKLOAD system=$SYSTEM logical=$LOGICAL comm=$COMM" > "$OUT/inputs.txt"
python3 /work/fattree/analyze_run.py "$OUT/fct.txt" "$OUT/qlen.txt" $PER_LEAF | tee "$OUT/analysis.txt"
echo "distinct src/dst pairs: $(awk '{print $1,$2}' "$OUT/fct.txt" | sort -u | wc -l)  flows: $(wc -l < "$OUT/fct.txt")"
grep finished "$OUT/ns3_run.log" | sed -E 's/.*sys\[([0-9]+)\] finished, ([0-9]+) cycles, exposed communication ([0-9]+) cycles.*/\1 \2 \3/' | awk '{if($2>t)t=$2; if($3>e)e=$3; n++} END{print "ranks:",n,"completion (slowest rank):",t,"max exposed comm:",e}'
