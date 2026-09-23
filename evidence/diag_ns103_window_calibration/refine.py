from __future__ import annotations
import json, math
import numpy as np
import weil_window as ww
from pathlib import Path as _P
HERE = _P(__file__).resolve().parent

FMAX = 130.0
nmax = int(math.exp(2 * 4.5)) + 2
zdata, dh = ww.zeta_data(nmax), ww.dh_data(nmax)

def peak(alpha, v, lam, fmax=FMAX):
    y = np.linspace(-lam, lam, 4001)
    g = np.sin(np.outer(alpha, y + lam)).T @ v
    ts = np.linspace(0, fmax, int(fmax * 20) + 1)
    gh = np.abs(np.trapezoid(g[:, None] * np.exp(1j * np.outer(y, ts)), y, axis=0))
    return float(ts[np.argmax(gh)])

out = {}
# 1. refine lambda* for DH
out["refine"] = []
for lam in [1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
    K = int(math.ceil(2 * lam * FMAX / math.pi)) + 4
    res = ww.window_matrix(dh, lam, K)
    ev, vec = np.linalg.eigh((res["W"] + res["W"].T) / 2)
    out["refine"].append({"lambda": lam, "min_eig_over_lambda": float(ev[0] / lam),
                          "peak_freq": peak(res["alpha"], vec[:, 0], lam), "two_delta_lambda": round(2 * 0.30851718 * lam, 3)})
# 2. convergence in FMAX and panel at lambda = 2 and 4
out["convergence"] = []
for lam in [2.0, 4.0]:
    for fmax, panel in [(130.0, 0.01), (200.0, 0.01), (130.0, 0.004)]:
        K = int(math.ceil(2 * lam * fmax / math.pi)) + 4
        res = ww.window_matrix(dh, lam, K, panel=panel)
        ev = np.linalg.eigvalsh((res["W"] + res["W"].T) / 2)
        resz = ww.window_matrix(zdata, lam, K, panel=panel)
        evz = np.linalg.eigvalsh((resz["W"] + resz["W"].T) / 2)
        out["convergence"].append({"lambda": lam, "FMAX": fmax, "panel": panel, "K": K,
                                   "dh_min_over_lambda": float(ev[0] / lam), "zeta_min_over_lambda": float(evz[0] / lam),
                                   "zeta_max_over_lambda": float(evz[-1] / lam)})
# 3. resonant frequencies of the most negative directions (DH), lambda = 3, 4
out["negative_directions"] = []
for lam in [3.0, 4.0]:
    fmax = 200.0
    K = int(math.ceil(2 * lam * fmax / math.pi)) + 4
    res = ww.window_matrix(dh, lam, K)
    ev, vec = np.linalg.eigh((res["W"] + res["W"].T) / 2)
    freqs = [(float(ev[i] / lam), peak(res["alpha"], vec[:, i], lam, fmax)) for i in range(12)]
    out["negative_directions"].append({"lambda": lam, "eig_over_lambda_and_peak_freq": freqs})
# 4. zeta near-null count vs Paley-Wiener prediction
out["zeta_null"] = []
for lam in [2.0, 3.0, 4.0, 5.0]:
    K = int(math.ceil(2 * lam * FMAX / math.pi)) + 4
    res = ww.window_matrix(zdata, lam, K)
    ev = np.linalg.eigvalsh((res["W"] + res["W"].T) / 2)
    out["zeta_null"].append({"lambda": lam, "K": K, "n_below_1e-10": int((ev < 1e-10).sum()),
                             "n_below_1e-6": int((ev < 1e-6).sum()),
                             "zeros_below_FMAX_approx": round(FMAX / (2 * math.pi) * math.log(FMAX / (2 * math.pi * math.e)) + 7 / 8, 1),
                             "crossover_height_2pi_e^{2lam}": round(2 * math.pi * math.exp(2 * lam), 1)})
json.dump(out, open(HERE / "refine.json", "w"), indent=1)
print(json.dumps(out, indent=1))
