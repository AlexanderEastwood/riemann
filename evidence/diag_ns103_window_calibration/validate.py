"""Validate the explicit-formula pipeline against actual zeros (zeta and Davenport-Heilbronn)."""
from __future__ import annotations

import json
import sys

import mpmath as mp
import numpy as np

import weil_window as ww
from pathlib import Path as _P
HERE = _P(__file__).resolve().parent

mp.mp.dps = 20
out: dict = {}

# 1. closed-form sine cross-correlations vs numeric
rows = []
for (j, k, x) in [(3, 3, 0.7), (4, 2, 1.3), (5, 1, 2.9), (7, 7, 3.4), (6, 3, 0.4)]:
    rows.append({"j": j, "k": k, "x": x, "closed": ww.S_closed(2.0, j, k, x), "numeric": ww.S_numeric(2.0, j, k, x)})
out["sine_closed_form"] = rows

# 2. zeta explicit formula: modulated Gaussian h(x) = exp(-x^2/(2 s^2)) cos(w x)
def make_h(s, w):
    return lambda x: mp.exp(-x * x / (2 * s * s)) * mp.cos(w * x)

def hhat_line(s, w, t):  # hhat(1/2 + i t) for that h
    return mp.sqrt(2 * mp.pi) * s / 2 * (mp.exp(-s * s * (t - w) ** 2 / 2) + mp.exp(-s * s * (t + w) ** 2 / 2))

zdata = ww.zeta_data(5000)
zeros = [mp.im(mp.zetazero(k)) for k in range(1, 41)]
out["zeta_checks"] = []
for (s, w) in [(1.0, 20.0), (0.7, 30.0)]:
    rhs = ww.weil_generic(zdata, make_h(s, w), 8.0)
    zero_side = sum(2 * hhat_line(s, w, g) for g in zeros)
    out["zeta_checks"].append({"sigma": s, "omega": w, "zero_side": mp.nstr(zero_side, 12),
                               "explicit_rhs": mp.nstr(rhs["total"], 12),
                               "pole": mp.nstr(rhs["pole"], 8), "prime": mp.nstr(rhs["prime"], 8), "arch": mp.nstr(rhs["arch"], 8),
                               "abs_diff": mp.nstr(abs(zero_side - rhs["total"]), 3)})

# 3. Davenport-Heilbronn: zeros on the line up to height 60, argument-principle count, explicit formula
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from controls.davenport_heilbronn import Lambda as LamDH  # noqa: E402

def Z(t):
    return mp.re(LamDH(mp.mpf(1) / 2 + 1j * t))

ts = np.linspace(0.05, 60.0, 6001)
vals = np.array([float(Z(mp.mpf(t))) for t in ts])
sign_changes = np.where(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0]
line_zeros = [float(mp.findroot(Z, (ts[i], ts[i + 1]), solver="bisect")) for i in sign_changes]

def winding(box):
    (x0, x1, y0, y1) = box
    pts = []
    n = 1500
    for (p, q_) in [((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0)), ((x0, y0), (x1, y0))]:
        for u in np.linspace(0, 1, n, endpoint=False):
            pts.append(complex(p[0] + (q_[0] - p[0]) * u, p[1] + (q_[1] - p[1]) * u))
    ph = np.unwrap([float(mp.arg(LamDH(mp.mpc(z)))) for z in pts] + [float(mp.arg(LamDH(mp.mpc(pts[0]))))])
    return (ph[-1] - ph[0]) / (2 * np.pi)

wind = winding((-0.5, 1.5, 0.05, 60.0))
out["dh_zero_count"] = {"line_zeros_below_60": len(line_zeros), "winding_box": float(wind),
                        "first_line_zeros": [round(z, 6) for z in line_zeros[:6]]}

dh = ww.dh_data(5000)
out["dh_lambda_sample"] = {str(n): float(dh.lam[n]) for n in (2, 3, 4, 5, 6, 8, 9, 10, 12, 16)}
out["dh_checks"] = []
for (s, w) in [(1.0, 25.0), (0.8, 35.0)]:
    rhs = ww.weil_generic(dh, make_h(s, w), 8.0)
    zero_side = sum(2 * hhat_line(s, w, g) for g in line_zeros)
    out["dh_checks"].append({"sigma": s, "omega": w, "zero_side": mp.nstr(zero_side, 12),
                             "explicit_rhs": mp.nstr(rhs["total"], 12),
                             "prime": mp.nstr(rhs["prime"], 8), "arch": mp.nstr(rhs["arch"], 8),
                             "abs_diff": mp.nstr(abs(zero_side - rhs["total"]), 3)})

# 4. end-to-end: sine-basis matrix entry vs generic functional on h = g_j x-corr g_k (zeta, lambda = 1.5)
lam = 1.5
res = ww.window_matrix(zdata, lam, 12)
def h_pair(j, k):
    def h(x):
        xf = float(x)
        return mp.mpf(ww.S_numeric(lam, j, k, abs(xf), 4001)) / 2 if True else 0
    return h
# S_numeric returns h(x)+h(-x); the functional only uses h(x)+h(-x) and h(0), so feed the even part.
pairs = [(2, 2), (3, 1), (5, 3), (4, 4)]
out["sine_vs_generic_zeta"] = []
for (j, k) in pairs:
    gen = ww.weil_generic(zdata, h_pair(j, k), 2 * lam)
    out["sine_vs_generic_zeta"].append({"j": j, "k": k, "matrix": float(res["W"][j - 1, k - 1]), "generic": float(gen["total"])})

json.dump(out, open(HERE / "validation.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
