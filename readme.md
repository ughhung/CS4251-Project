``` ROOT=/app/astra-sim
  NS3=$ROOT/extern/network_backend/ns-3
  TRACE_DIR=$ROOT/traces/tai-trace
  SYSTEM=$ROOT/examples/system/native_collectives/Ring_4chunks_roofline.json

  sed 's/"roofline-enabled": 0/"roofline-enabled": 1/' \
    "$ROOT/examples/system/native_collectives/Ring_4chunks.json" > "$SYSTEM"
  grep '"roofline-enabled"' "$SYSTEM"

  Then use the copied file as --system-configuration for every trace and topology. For example, the dense run on the 32-rank ring:

  cd "$NS3/build/scratch"
  ./ns3.42-AstraSimNetwork-default \
    --workload-configuration="$TRACE_DIR/dense32_validmb" \
    --comm-group-configuration="$TRACE_DIR/dense32_validmb.json" \
    --system-configuration="$SYSTEM" \
    --remote-memory-configuration="$ROOT/examples/remote_memory/analytical/no_memory_expansion.json" \
    --network-configuration="$NS3/scratch/config/config_ring32.txt" \
    --logical-topology-configuration="$TRACE_DIR/logical_topology.json"```
    