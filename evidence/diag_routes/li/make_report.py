import json, html
from mpmath import mp, mpf, nstr, log
mp.dps = 30
A = [mpf(x) for x in json.load(open("lambda_arith.json"))["A"]]
B = [mpf(x) for x in json.load(open("lambda_arith.json"))["B"]]
Z = json.load(open("lambda_zeros_2000.json"))
W = json.load(open("lambda_windowed.json"))
try:
    Z4 = json.load(open("lambda_zeros_4000.json"))
except Exception:
    Z4 = None

rows = []
for n in range(1, 61):
    p, t = mpf(Z[str(n)][0]), mpf(Z[str(n)][1])
    c2 = p + t
    d2 = abs(A[n-1] - c2)
    cell4 = ""
    if Z4:
        p4, t4 = mpf(Z4[str(n)][0]), mpf(Z4[str(n)][1])
        cell4 = "<td>%s</td><td>%s</td>" % (nstr(p4+t4, 12), nstr(abs(A[n-1]-(p4+t4)), 2))
    rows.append("<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>%s</tr>" %
                (n, nstr(A[n-1], 20), nstr(p, 10), nstr(c2, 12), nstr(d2, 2), cell4))
hdr4 = "<th>zeros (4000)+tail</th><th>|A−C₄₀₀₀|</th>" if Z4 else ""
table = "<table><thead><tr><th>n</th><th>λ_n (exact def., route A; = route B to 1e−63)</th><th>zeros only (2000)</th><th>zeros (2000)+smooth tail (route C)</th><th>|A−C|</th>%s</tr></thead><tbody>%s</tbody></table>" % (hdr4, "".join(rows))

wrows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (n, nstr(mpf(Z[n][0])+mpf(Z[n][1]), 10), nstr(mpf(v[0])+mpf(v[1]), 10), nstr((mpf(v[0])+mpf(v[1]))/(mpf(Z[n][0])+mpf(Z[n][1])), 5)) for n, v in W.items())
wtable = "<table><thead><tr><th>n</th><th>λ_n</th><th>λ_n^{[log 16]} (2000 zeros + tail)</th><th>ratio</th></tr></thead><tbody>%s</tbody></table>" % wrows

body = open("report_body.html").read().replace("%%TABLE%%", table).replace("%%WTABLE%%", wtable)
page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Li's criterion vs the W_4 window — report</title></head>
<body style="margin:0;padding:24px 16px;background:#fff;color:#1a1a1a;font-family:Georgia,'Times New Roman',serif;font-size:16px;line-height:1.5">
<div style="max-width:680px;margin:0 auto">%s</div></body></html>""" % body
open("li-criterion-report-2026-09-21-v1.html", "w").write(page)
print("wrote", len(page), "bytes")
