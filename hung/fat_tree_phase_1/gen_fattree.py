#!/usr/bin/env python3
"""
Generate a 2-tier fat-tree (leaf-spine) topology file for ASTRA-sim's ns-3 backend.

File format (from the ASTRA-sim ns-3 docs):
  line 1: <total nodes> <number of switches> <number of links>
  line 2: <switch node IDs, space separated>
  line 3+: <nodeA> <nodeB> <bandwidth> <latency> <last field>
Node IDs: GPUs are 0..G-1, then leaf (ToR) switches, then spine switches.

The last field is copied as "0" like the official example. Its meaning is not
confirmed in the docs, so confirm it in the ns-3 config parser before relying on it.

Example (default, 16 GPUs, 4 leaf switches, 2 spines, 2:1 oversubscribed):
  python3 gen_fattree.py > fattree_16.txt
"""
import argparse


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--gpus", type=int, default=16)
    p.add_argument("--leaves", type=int, default=4, help="number of leaf/ToR switches")
    p.add_argument("--spines", type=int, default=2, help="number of spine switches")
    p.add_argument("--host-bw", default="200Gbps", help="GPU-to-leaf link speed")
    p.add_argument("--uplink-bw", default="200Gbps", help="leaf-to-spine link speed")
    p.add_argument("--host-lat", default="0.005ms")
    p.add_argument("--uplink-lat", default="0.0125ms")
    a = p.parse_args()

    if a.gpus % a.leaves:
        raise SystemExit("gpus must divide evenly across leaves")
    per_leaf = a.gpus // a.leaves

    leaf0 = a.gpus
    spine0 = leaf0 + a.leaves
    total = a.gpus + a.leaves + a.spines
    switches = list(range(leaf0, total))

    links = []
    for g in range(a.gpus):  # each GPU to its leaf
        links.append((g, leaf0 + g // per_leaf, a.host_bw, a.host_lat))
    for l in range(a.leaves):  # every leaf to every spine
        for s in range(a.spines):
            links.append((leaf0 + l, spine0 + s, a.uplink_bw, a.uplink_lat))

    print(total, len(switches), len(links))
    print(" ".join(map(str, switches)))
    for x, y, bw, lat in links:
        print(x, y, bw, lat, 0)


if __name__ == "__main__":
    main()
