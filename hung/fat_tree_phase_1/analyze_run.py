import sys
fct_path, qlen_path, per_leaf = sys.argv[1], sys.argv[2], int(sys.argv[3])

groups = {"same-leaf": [], "cross-leaf": []}
for line in open(fct_path):
    f = line.split()
    if len(f) < 8:
        continue
    src, dst = int(f[0][4:6], 16), int(f[1][4:6], 16)
    key = "same-leaf" if src // per_leaf == dst // per_leaf else "cross-leaf"
    groups[key].append(int(f[6]))
for k, v in groups.items():
    if v:
        print(k, "flows:", len(v), "mean FCT:", sum(v) // len(v), "min:", min(v), "max:", max(v))

peak, last = {}, 0
for line in open(qlen_path):
    t = line.split()
    if len(t) < 6:
        continue
    last = max(last, int(t[1]))
    sw = int(t[2])
    q = [int(t[i + 2]) for i in range(3, len(t) - 2, 3)]
    peak[sw] = max(peak.get(sw, 0), max(q))
print("last qlen timestamp:", last)
for sw in sorted(peak):
    print("switch", sw, "peak queue:", peak[sw])
