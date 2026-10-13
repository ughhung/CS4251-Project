import sys
from collections import defaultdict

fct_path, per_leaf, dp_span = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
rows = defaultdict(list)
for line in open(fct_path):
    f = line.split()
    if len(f) < 8:
        continue
    src, dst = int(f[0][4:6], 16), int(f[1][4:6], 16)
    kind = "same-leaf" if src // per_leaf == dst // per_leaf else "cross-leaf"
    group = "DP" if src // dp_span == dst // dp_span else "TP"
    rows[(group, int(f[4]), kind)].append(int(f[6]))

print("group size_bytes kind flows mean_FCT min_FCT max_FCT")
for (group, size, kind), v in sorted(rows.items()):
    print(group, size, kind, len(v), sum(v) // len(v), min(v), max(v))
