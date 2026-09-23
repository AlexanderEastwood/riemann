"""Per-zero detection window for DH, and the reach of zeta's near-null space vs the Paley-Wiener crossover."""
from __future__ import annotations
import json, math
from typing import Any
import numpy as np
import weil_window as ww
from pathlib import Path as _P
HERE = _P(__file__).resolve().parent

nmax = int(math.exp(2 * 4.0)) + 2
zdata, dh = ww.zeta_data(nmax), ww.dh_data(nmax)
ZEROS = {"85.70": 0.308517, "176.70": 0.224258, "114.16": 0.150830, "166.48": 0.074356}

def peaks(alpha, vecs, lam, fmax):
    y = np.linspace(-lam, lam, 3001)
    G = np.sin(np.outer(alpha, y + lam)).T @ vecs          # y x m
    ts = np.linspace(0, fmax, int(fmax * 10) + 1)
    E = np.exp(1j * np.outer(ts, y)) * (y[1] - y[0])       # t x y
    gh = np.abs(E @ G)                                     # t x m
    return ts[np.argmax(gh, axis=0)]

out: dict[str, Any] = {"per_zero_detection": [], "zeta_null_reach": []}
FMAX = 200.0
first: dict[str, float] = {}
for lam in np.arange(1.4, 4.01, 0.1):
    lam = round(float(lam), 2)
    K = int(math.ceil(2 * lam * FMAX / math.pi)) + 4
    res = ww.window_matrix(dh, lam, K)
    ev, vec = np.linalg.eigh((res["W"] + res["W"].T) / 2)
    neg = np.where(ev < -1e-9 * lam)[0]
    row: dict[str, Any] = {"lambda": lam, "half_log_T_over_2pi": {T: round(0.5 * math.log(float(T) / (2 * math.pi)), 3) for T in ZEROS}}
    if len(neg):
        pk = peaks(res["alpha"], vec[:, neg], lam, FMAX)
        for T in ZEROS:
            sel = [i for i, p in zip(neg, pk) if abs(p - float(T)) < 4]
            if sel:
                row[T] = float(min(ev[sel]) / lam)
                first.setdefault(T, lam)
    out["per_zero_detection"].append(row)
out["first_detection_window"] = {T: {"lambda_star": first.get(T), "delta": ZEROS[T],
                                     "one_over_2delta": round(1 / (2 * ZEROS[T]), 2),
                                     "half_log_T_over_2pi": round(0.5 * math.log(float(T) / (2 * math.pi)), 2)} for T in ZEROS}

for lam in [1.5, 2.0, 2.5]:
    fmax = 400.0
    K = int(math.ceil(2 * lam * fmax / math.pi)) + 4
    res = ww.window_matrix(zdata, lam, K)
    ev, vec = np.linalg.eigh((res["W"] + res["W"].T) / 2)
    null = np.where(ev < 1e-9)[0]
    pk = peaks(res["alpha"], vec[:, null], lam, fmax) if len(null) else np.array([])
    out["zeta_null_reach"].append({"lambda": lam, "K": K, "n_null": int(len(null)),
                                   "max_peak_freq_of_null": float(pk.max()) if len(pk) else None,
                                   "null_peak_freq_percentiles_50_90_99": [float(np.percentile(pk, q)) for q in (50, 90, 99)] if len(pk) else None,
                                   "crossover_2pi_e^{2lam}": round(2 * math.pi * math.exp(2 * lam), 1),
                                   "min_eig_over_lambda": float(ev[0] / lam)})
json.dump(out, open(HERE / "law.json", "w"), indent=1)
print(json.dumps(out["first_detection_window"], indent=1))
print(json.dumps(out["zeta_null_reach"], indent=1))
for r in out["per_zero_detection"]:
    print(r["lambda"], {k: round(v, 4) for k, v in r.items() if k in ZEROS})
