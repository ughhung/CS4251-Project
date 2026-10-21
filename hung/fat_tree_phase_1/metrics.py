import math
import os
import re
import sys

d = sys.argv[1]


def pct(vals, p):
    if not vals:
        return 0
    return vals[max(0, math.ceil(p / 100 * len(vals)) - 1)]


done, exposed = [], []
for line in open(os.path.join(d, "ns3_run.log"), errors="replace"):
    m = re.search(r"sys\[(\d+)\] finished, (\d+) cycles, exposed communication (\d+) cycles", line)
    if m:
        done.append(int(m.group(2)))
        exposed.append(int(m.group(3)))

fct, slow, nbytes = [], [], 0
for line in open(os.path.join(d, "fct.txt")):
    f = line.split()
    if len(f) < 8:
        continue
    nbytes += int(f[4])
    t, ideal = int(f[6]), int(f[7])
    fct.append(t)
    if ideal > 0:
        slow.append(t / ideal)
fct.sort()
slow.sort()

peak = 0
for line in open(os.path.join(d, "qlen.txt")):
    t = line.split()
    if len(t) < 6:
        continue
    for i in range(3, len(t) - 2, 3):
        peak = max(peak, int(t[i + 2]))

pfc = sum(1 for l in open(os.path.join(d, "pfc.txt")) if l.strip())

if not done:
    print("WARNING: no 'finished' lines in ns3_run.log - the run did not complete")
rows = [
    ("ranks that finished", len(done)),
    ("completion time (cycles, slowest rank)", max(done) if done else "n/a"),
    ("fastest rank (cycles)", min(done) if done else "n/a"),
    ("max exposed communication (cycles)", max(exposed) if exposed else "n/a"),
    ("flows", len(fct)),
    ("total bytes sent", nbytes),
    ("FCT mean (ns)", round(sum(fct) / len(fct)) if fct else "n/a"),
    ("FCT median (ns)", pct(fct, 50)),
    ("FCT p95 (ns)", pct(fct, 95)),
    ("FCT max (ns)", fct[-1] if fct else "n/a"),
    ("slowdown median (FCT / no-contention FCT)", round(pct(slow, 50), 3)),
    ("slowdown p95", round(pct(slow, 95), 3)),
    ("slowdown max", round(slow[-1], 3) if slow else "n/a"),
    ("peak queue, any port (bytes)", peak),
    ("PFC events (lines in pfc.txt)", pfc),
]
for k, v in rows:
    print(f"{k}: {v}")
