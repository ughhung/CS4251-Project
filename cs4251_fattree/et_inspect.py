import argparse
import collections
import glob
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("--pb", required=True, help="folder holding et_def_pb2.py")
ap.add_argument("--prefix", required=True, help="trace path without .N.et")
ap.add_argument("--nodes", type=int, nargs="*", default=[], help="node ids to look up")
args = ap.parse_args()
sys.path.insert(0, args.pb)
import et_def_pb2 as pb


def varint(buf, pos):
    r, s = 0, 0
    while True:
        b = buf[pos]
        pos += 1
        r |= (b & 0x7F) << s
        if not b & 0x80:
            return r, pos
        s += 7


def read_et(path):
    buf = open(path, "rb").read()
    size, pos = varint(buf, 0)  # first message: global metadata
    pos += size
    nodes = []
    while pos < len(buf):
        size, pos = varint(buf, pos)
        n = pb.Node()
        n.ParseFromString(buf[pos:pos + size])
        pos += size
        nodes.append(n)
    return nodes


def tname(n):
    return pb.NodeType.Name(n.type)


def attrs(n):
    out = []
    for a in n.attr:
        vals = [f"{fd.name}={v}" for fd, v in a.ListFields() if fd.name not in ("name", "doc_string")]
        out.append(f"{a.name}: {' '.join(vals)}")
    return out


files = glob.glob(args.prefix + ".*.et")
ranks = sorted(int(f[len(args.prefix) + 1:-3]) for f in files)
print("rank files found:", len(ranks))
all_nodes = {r: read_et(f"{args.prefix}.{r}.et") for r in ranks}

print("\n== node counts and types (rank 0) ==")
c = collections.Counter(tname(n) for n in all_nodes[ranks[0]])
print("nodes in rank 0:", len(all_nodes[ranks[0]]), dict(c))
sizes = [len(v) for v in all_nodes.values()]
print("nodes per rank: min", min(sizes), "max", max(sizes))

print("\n== structure checks over all ranks ==")
tot = collections.Counter()
examples = collections.defaultdict(list)
for r, nodes in all_nodes.items():
    ids = [n.id for n in nodes]
    pos = {}
    for i, n in enumerate(nodes):
        if n.id in pos:
            tot["duplicate ids"] += 1
        pos[n.id] = i
    indeg = {}
    children = collections.defaultdict(list)
    for i, n in enumerate(nodes):
        deps = set(n.data_deps) | set(n.ctrl_deps)
        indeg[n.id] = 0
        for d in deps:
            if d not in pos:
                tot["deps on a missing id"] += 1
                if len(examples["missing"]) < 3:
                    examples["missing"].append((r, n.id, d))
                continue
            indeg[n.id] += 1
            children[d].append(n.id)
            if pos[d] > i:
                tot["deps appearing LATER in the file"] += 1
                if len(examples["forward"]) < 3:
                    examples["forward"].append((r, n.id, d))
    for i in range(1, len(ids)):
        if ids[i] < ids[i - 1]:
            tot["places where id goes down in file order"] += 1
    q = [k for k, v in indeg.items() if v == 0]
    seen = 0
    while q:
        k = q.pop()
        seen += 1
        for ch in children[k]:
            indeg[ch] -= 1
            if indeg[ch] == 0:
                q.append(ch)
    if seen != len(nodes):
        tot["nodes stuck in a dependency cycle"] += len(nodes) - seen
    for n in nodes:
        if n.type == pb.COMP_NODE and n.duration_micros == 0:
            nops = [a for a in n.attr if a.name == "num_ops"]
            if not nops or nops[0].int64_val == 0:
                tot["compute nodes with zero duration and zero ops"] += 1
    mx = max((len(set(n.data_deps) | set(n.ctrl_deps)) for n in nodes), default=0)
    tot["max deps on one node (largest over ranks)"] = max(tot["max deps on one node (largest over ranks)"], mx)
    mc = max((len(v) for v in children.values()), default=0)
    tot["max dependents of one node (largest over ranks)"] = max(tot["max dependents of one node (largest over ranks)"], mc)
for k, v in tot.items():
    print(f"  {k}: {v}")
if not tot:
    print("  (nothing flagged)")
for k, v in examples.items():
    print(f"  examples of '{k}' (rank, node, dependency):", v)

for nid in args.nodes:
    print(f"\n== node {nid} ==")
    found = [r for r, nodes in all_nodes.items() if any(n.id == nid for n in nodes)]
    print("present in ranks:", found)
    for r in found[:2]:
        nodes = all_nodes[r]
        byid = {n.id: n for n in nodes}
        n = byid[nid]
        print(f"  rank {r}: type={tname(n)} name={n.name!r}")
        print("    attrs:", attrs(n))
        print("    depends on:", [(d, byid[d].name if d in byid else "MISSING") for d in list(n.data_deps) + list(n.ctrl_deps)])
        kids = [m for m in nodes if nid in m.data_deps or nid in m.ctrl_deps]
        print("    nodes that depend on it:", [(m.id, tname(m), m.name) for m in kids][:8])
