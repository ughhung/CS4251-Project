import sys
from collections import defaultdict

qlen_path, topo_path = sys.argv[1], sys.argv[2]
rows = open(topo_path).read().split("\n")
total, nsw, nlinks = map(int, rows[0].split()[:3])
ngpu = total - nsw

nbrs = defaultdict(list)
for line in rows[2:2 + nlinks]:
    f = line.split()
    if len(f) < 2:
        continue
    a, b = int(f[0]), int(f[1])
    nbrs[a].append(b)
    nbrs[b].append(a)


def name(n):
    return ("GPU %d" % n) if n < ngpu else ("switch %d" % n)


peak = defaultdict(int)
busy = defaultdict(int)
for line in open(qlen_path):
    t = line.split()
    if len(t) < 6:
        continue
    sw = int(t[2])
    for i in range(3, len(t) - 2, 3):
        p, q = int(t[i + 1]), int(t[i + 2])
        peak[(sw, p)] = max(peak[(sw, p)], q)
        if q > 0:
            busy[(sw, p)] += 1


def peer(sw, p):
    lst = nbrs.get(sw, [])
    return name(lst[p - 1]) if 1 <= p <= len(lst) else "?"


print("Top ports by peak queue (bytes)")
for (sw, p), v in sorted(peak.items(), key=lambda kv: -kv[1])[:12]:
    print("switch %d port %d -> %s: peak %d, samples with queue>0: %d" % (sw, p, peer(sw, p), v, busy[(sw, p)]))

to_gpu = [v for (sw, p), v in peak.items() if peer(sw, p).startswith("GPU")]
to_sw = [v for (sw, p), v in peak.items() if peer(sw, p).startswith("switch")]
print("max peak on ports facing a GPU:", max(to_gpu) if to_gpu else "none")
print("max peak on ports facing a switch:", max(to_sw) if to_sw else "none")
