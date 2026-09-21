"""Assemble the HTML report from the computed JSON outputs (no hand-transcribed numbers)."""
import json, html
from mpmath import mp, mpf, log, euler, pi, nstr, sqrt
mp.dps = 40
C = 2 + euler - log(4*pi)

r40 = json.load(open("/tmp/nymanbeurling/dN_arb_400bits_N40.json"))
r200 = json.load(open("/tmp/nymanbeurling/dN_arb_1500bits_N200_ext.json"))
r600 = json.load(open("/tmp/nymanbeurling/dN_arb_2500bits_big_N600.json"))

def clean(s):
    return s.split(" +/-")[0].strip("[]")

rows40 = ""
for r in r40:
    N = r["N"]
    d = clean(r["d"])[:14]; d2 = clean(r["d2"])[:16]
    lg = clean(r["d2logN"])[:12] if N > 1 else "&mdash;"
    ratio = clean(r["ratio"])[:8] if N > 1 else "&mdash;"
    flag = ""
    if N > 1 and float(clean(r["ratio"])) < 1: flag = ' style="background:#fde2e2"'
    rows40 += f"<tr{flag}><td>{N}</td><td>{d}</td><td>{d2}</td><td>{lg}</td><td>{ratio}</td><td>{r['rad']}</td></tr>\n"

rows200 = ""
for (N, d2, lg, ratio, rad) in r200:
    if N <= 40: continue
    if N <= 50 or N % 10 == 0:
        flag = ' style="background:#fde2e2"' if float(ratio) < 1 else ""
        rows200 += f"<tr{flag}><td>{N}</td><td>{d2[:16]}</td><td>{lg[:12]}</td><td>{ratio[:8]}</td></tr>\n"

rows600 = ""
for (N, d2, lg, ratio, rad) in r600:
    flag = ' style="background:#fde2e2"' if float(ratio) < 1 else ""
    rows600 += f"<tr{flag}><td>{N}</td><td>{d2[:16]}</td><td>{lg[:12]}</td><td>{ratio[:8]}</td><td>{html.escape(rad.split(' +/-')[0].strip('['))}</td></tr>\n"

all_rows = [(r["N"], float(clean(r["ratio"]))) for r in r40 if r["N"] > 1] + [(N, float(ratio)) for (N, d2, lg, ratio, rad) in r200 if N > 40] + [(N, float(ratio)) for (N, d2, lg, ratio, rad) in r600 if N > 200]
below = [N for N, x in all_rows if x < 1]
def ranges(ns):
    # compress a list of N (dense for N<=50, every 10 to 200, every 20 to 600) into readable runs
    if not ns: return "none"
    out = []; start = prev = ns[0]
    for n in ns[1:]:
        step = 1 if prev <= 50 else (10 if prev <= 200 else 20)
        if n - prev <= step: prev = n; continue
        out.append(f"{start}" if start == prev else f"{start}–{prev}"); start = prev = n
    out.append(f"{start}" if start == prev else f"{start}–{prev}")
    return ", ".join(out)
below_text = ranges(below)
rmin = min(all_rows[6:], key=lambda t: t[1]); rmax = max(all_rows[6:], key=lambda t: t[1])

tpl = open("/tmp/nymanbeurling/report_template.html").read()
out = (tpl.replace("%%C%%", nstr(C, 32))
          .replace("%%SQRTC%%", nstr(sqrt(C), 12))
          .replace("%%ROWS40%%", rows40)
          .replace("%%ROWS200%%", rows200)
          .replace("%%ROWS600%%", rows600)
          .replace("%%BELOW%%", below_text)
          .replace("%%RMIN%%", f"{rmin[1]:.4f} (N = {rmin[0]})")
          .replace("%%RMAX%%", f"{rmax[1]:.4f} (N = {rmax[0]})"))
open("/tmp/nymanbeurling/nyman-beurling-report-2026-09-21-v1.html", "w").write(out)
print("wrote /tmp/nymanbeurling/nyman-beurling-report-2026-09-21-v1.html")
print("below C at N =", below)
print("range of ratio for N>=7:", rmin, rmax)
