#!/usr/bin/env python3
"""
Generate / check ASTRA-sim ns-3 topology files for the 32-GPU study.

File format written (ASTRA-sim ns-3 backend style):
    <total_nodes> <num_switches> <num_links>
    <switch node ids ...>
    <src> <dst> <rate> <delay> <error_rate>      (one line per link)
!! Format is from memory: diff the header and a few link lines against your
!! existing torus/fat-tree files before running, and match them if they differ.

Node numbering:
    GPUs = 0..31
    torus switches start at 32; id = 32 + y*W + x
        1 GPU/switch : 4 rows x 8 columns = 32 switches (your current torus)
        2 GPUs/switch: 4 rows x 4 columns = 16 switches (comparable to fat-tree)
    fat-tree leaves = 32..39, spines = 40..(40+S-1)

Examples
    # torus, all links 500 ns (uniform baseline)
    gen_topo.py torus --host-delay-ns 500 --fabric-delay-ns 500 -o torus_uniform.txt
    # torus, GPU<->switch link ~0 (the switch is the GPU's own router)
    gen_topo.py torus --host-delay-ns 1 --fabric-delay-ns 500 -o torus_hostlink.txt
    # 2 GPUs per switch (4x4 grid of 16 switches), real short cable to each GPU
    gen_topo.py torus --gpus-per-switch 2 --host-delay-ns 100 --fabric-delay-ns 500 -o torus2.txt
    # T1 twisted (use on the 4x8 grid)    T2 placements
    gen_topo.py torus --twist 4 ...
    gen_topo.py torus --placement aligned ...   |   --placement random --seed 1
    # fat-tree 2:1 (2 spines); F1 non-blocking = --spines 4; F2 = --placement dp-local
    gen_topo.py fattree --host-delay-ns 100 --fabric-delay-ns 500 -o fattree.txt
    # check a file (counts, degrees, hop stats)  /  distance between group partners
    gen_topo.py check FILE
    gen_topo.py rings FILE
"""
import argparse, collections, random

N_GPU = 32


def fmt_delay(ns):
    return f"{ns / 1e6:.6f}ms"          # 500 ns -> 0.000500ms


def write(path, n_nodes, switches, links):
    with open(path, "w") as f:
        f.write(f"{n_nodes} {len(switches)} {len(links)}\n")
        f.write(" ".join(map(str, switches)) + "\n")
        for a, b, rate, delay in links:
            f.write(f"{a} {b} {rate} {delay} 0\n")


def torus_positions(placement, W, H, gps, seed):
    """rank -> (x, y) grid position of the switch its GPU plugs into.
    Assumes TP groups = 4 consecutive ranks and DP groups = ranks with equal (rank mod 4)
    -- verify against the communicator file."""
    if placement == "linear":                    # fill the grid in rank order, gps GPUs per switch
        return [((r // gps) % W, (r // gps) // W) for r in range(N_GPU)]
    if placement == "aligned":                   # TP group -> a column (ring of 4), DP group -> a row (ring)
        return [((r // 4) // gps, r % 4) for r in range(N_GPU)]
    if placement == "random":
        cells = [(x, y) for y in range(H) for x in range(W) for _ in range(gps)]
        random.Random(seed).shuffle(cells)
        return cells
    raise SystemExit(f"unknown torus placement {placement}")


def make_torus(a):
    gps = a.gpus_per_switch
    if gps not in (1, 2):
        raise SystemExit("--gpus-per-switch must be 1 or 2")
    W, H = (8, 4) if gps == 1 else (4, 4)
    n_sw = W * H
    sw = lambda x, y: N_GPU + y * W + x
    host = (a.rate, fmt_delay(a.host_delay_ns))
    fab = (a.rate, fmt_delay(a.fabric_delay_ns))
    links = []
    for r, (x, y) in enumerate(torus_positions(a.placement, W, H, gps, a.seed)):
        links.append((r, sw(x, y), *host))
    for y in range(H):
        for x in range(W):
            links.append((sw(x, y), sw((x + 1) % W, y), *fab))            # horizontal (+ wraparound)
            if y + 1 < H:
                links.append((sw(x, y), sw(x, y + 1), *fab))              # vertical
            else:                                                         # vertical wraparound, twisted by a.twist columns
                links.append((sw(x, y), sw((x + a.twist) % W, 0), *fab))
    write(a.out, N_GPU + n_sw, list(range(N_GPU, N_GPU + n_sw)), links)


def make_fattree(a):
    leaves, per_leaf, S = 8, 4, a.spines
    leaf0, spine0 = N_GPU, N_GPU + leaves
    host = (a.rate, fmt_delay(a.host_delay_ns))
    fab = (a.rate, fmt_delay(a.fabric_delay_ns))
    if a.placement == "linear":                  # leaf l hosts ranks 4l..4l+3 (TP group inside a leaf)
        gpus = [[per_leaf * l + i for i in range(per_leaf)] for l in range(leaves)]
    elif a.placement == "dp-local":              # leaf l hosts 4 ranks of ONE DP group (rank mod 4 equal)
        gpus = [[(l // 2) + 4 * (4 * (l % 2) + i) for i in range(per_leaf)] for l in range(leaves)]
    else:
        raise SystemExit(f"unknown fat-tree placement {a.placement}")
    links = []
    for l in range(leaves):
        for g in gpus[l]:
            links.append((g, leaf0 + l, *host))
    for l in range(leaves):
        for s in range(S):
            links.append((leaf0 + l, spine0 + s, *fab))
    write(a.out, N_GPU + leaves + S, list(range(leaf0, spine0 + S)), links)


def load(path):
    with open(path) as f:
        n, nsw, nl = map(int, f.readline().split())
        sws = set(map(int, f.readline().split()))
        rows = [l.split() for l in f if l.strip()]
    return n, nsw, nl, sws, rows


def bfs(adj, s):
    d, q = {s: 0}, collections.deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1; q.append(v)
    return d


def check(path):
    n, nsw, nl, sws, rows = load(path)
    adj, deg, seen, delays = collections.defaultdict(set), collections.Counter(), set(), collections.Counter()
    assert len(rows) == nl, f"header says {nl} links, file has {len(rows)}"
    assert len(sws) == nsw and n == N_GPU + nsw
    for a, b, rate, delay, err in rows:
        a, b = int(a), int(b)
        key = (min(a, b), max(a, b))
        assert key not in seen, f"duplicate link {key}"
        seen.add(key)
        adj[a].add(b); adj[b].add(a); deg[a] += 1; deg[b] += 1
        delays[(("host" if (a < N_GPU or b < N_GPU) else "fabric"), rate, delay)] += 1
    tot = cnt = dm = 0
    for s in range(N_GPU):
        d = bfs(adj, s)
        for t in range(N_GPU):
            if t != s:
                assert t in d, "graph is disconnected"
                tot += d[t]; cnt += 1; dm = max(dm, d[t])
    print(f"{path}: nodes={n} switches={nsw} links={nl}")
    print(f"  GPU degree: {sorted(set(deg[g] for g in range(N_GPU)))}   switch degree: {sorted(set(deg[s] for s in sws))}")
    print(f"  GPU-to-GPU hops: avg={tot / cnt:.2f}  diameter={dm}")
    for k, v in sorted(delays.items()):
        print(f"  {v:3d} {k[0]} links  rate={k[1]} delay={k[2]}")


def rings(path):
    """Average / max number of switch-to-switch (fabric) hops between ring neighbours of each group."""
    _, _, _, _, rows = load(path)
    adj = collections.defaultdict(set)
    for a, b, *_ in rows:
        adj[int(a)].add(int(b)); adj[int(b)].add(int(a))
    tp = [[4 * g + i for i in range(4)] for g in range(8)]
    dp = [[j + 4 * k for k in range(8)] for j in range(4)]
    for name, groups in (("TP groups (4)", tp), ("DP groups (8)", dp)):
        hs = []
        for g in groups:
            for i, r in enumerate(g):
                nxt = g[(i + 1) % len(g)]
                hs.append(max(bfs(adj, r)[nxt] - 2, 0))      # subtract the 2 GPU links
        print(f"  {name}: partner-to-partner fabric hops avg={sum(hs) / len(hs):.2f} max={max(hs)}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("torus", "fattree"):
        q = sub.add_parser(name)
        q.add_argument("-o", "--out", required=True)
        q.add_argument("--rate", default="200Gbps")
        q.add_argument("--host-delay-ns", type=float, default=500)
        q.add_argument("--fabric-delay-ns", type=float, default=500)
        q.add_argument("--placement", default="linear")
        if name == "torus":
            q.add_argument("--gpus-per-switch", type=int, default=1, help="1 = 4x8 grid (32 switches); 2 = 4x4 grid (16 switches)")
            q.add_argument("--twist", type=int, default=0, help="column shift applied to the vertical wraparound (T1 uses 4 on the 4x8 grid)")
            q.add_argument("--seed", type=int, default=0)
        else:
            q.add_argument("--spines", type=int, default=2, help="2 = 2:1 oversubscribed; 4 = non-blocking (F1)")
    for name in ("check", "rings"):
        c = sub.add_parser(name); c.add_argument("path")
    a = p.parse_args()
    if a.cmd == "torus": make_torus(a)
    elif a.cmd == "fattree": make_fattree(a)
    elif a.cmd == "check": check(a.path)
    else: rings(a.path)


if __name__ == "__main__":
    main()