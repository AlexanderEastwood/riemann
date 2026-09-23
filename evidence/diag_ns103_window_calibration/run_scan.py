"""Min eigenvalue of the window-restricted Weil form vs lambda, zeta and Davenport-Heilbronn."""
from __future__ import annotations

import json
import math
import sys
import time

import numpy as np

import weil_window as ww
from pathlib import Path as _P
HERE = _P(__file__).resolve().parent

FMAX = 130.0          # top basis frequency alpha_K (covers the 85.7 and 114.2 off-line heights)
lams = [float(v) for v in sys.argv[1:]] or [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
nmax = int(math.exp(2 * max(lams))) + 2
t0 = time.time()
zdata = ww.zeta_data(nmax)
dh = ww.dh_data(nmax)
print(f"coefficients ready in {time.time()-t0:.1f}s, nmax={nmax}", file=sys.stderr)


def peak_frequency(alpha, v, lam):
    """Dominant |ghat(1/2+it)| of g = sum v_j g_j on a t-grid (numeric)."""
    y = np.linspace(-lam, lam, 4001)
    g = np.sin(np.outer(alpha, y + lam)).T @ v
    ts = np.linspace(0, FMAX, 2601)
    gh = np.abs(np.trapezoid(g[:, None] * np.exp(1j * np.outer(y, ts)), y, axis=0))
    return float(ts[np.argmax(gh)]), float(gh.max() ** 2 / np.trapezoid(g * g, y))


rows = []
for lam in lams:
    K = int(math.ceil(2 * lam * FMAX / math.pi)) + 4
    row = {"lambda": lam, "K": K}
    for data in (zdata, dh):
        t1 = time.time()
        res = ww.window_matrix(data, lam, K)
        W = res["W"]
        evals, evecs = np.linalg.eigh((W + W.T) / 2)
        i = int(np.argmin(evals))
        freq, conc = peak_frequency(res["alpha"], evecs[:, i], lam)
        row[data.name] = {"min_eig_over_lambda": float(evals[i] / lam),
                          "n_negative": int((evals < 0).sum()),
                          "min_eigvec_peak_freq": freq,
                          "seconds": round(time.time() - t1, 1)}
    rows.append(row)
    print(json.dumps(row), file=sys.stderr)

json.dump(rows, open(HERE / "scan.json", "w"), indent=1)
