import argparse
p = argparse.ArgumentParser()
p.add_argument("--gpus", type=int, default=16)
p.add_argument("--leaves", type=int, default=4)
p.add_argument("--spines", type=int, default=2)
p.add_argument("--host-bw", default="200Gbps")
p.add_argument("--uplink-bw", default="200Gbps")
p.add_argument("--host-lat", default="0.005ms")
p.add_argument("--uplink-lat", default="0.0125ms")
a = p.parse_args()
per_leaf = a.gpus // a.leaves
leaf0 = a.gpus
spine0 = leaf0 + a.leaves
total = a.gpus + a.leaves + a.spines
links = []
for g in range(a.gpus):
    links.append((g, leaf0 + g // per_leaf, a.host_bw, a.host_lat))
for l in range(a.leaves):
    for s in range(a.spines):
        links.append((leaf0 + l, spine0 + s, a.uplink_bw, a.uplink_lat))
print(total, a.leaves + a.spines, len(links))
print(" ".join(str(x) for x in range(leaf0, total)))
for x, y, bw, lat in links:
    print(x, y, bw, lat, 0)
