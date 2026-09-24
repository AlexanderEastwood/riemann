"""DIAGNOSTIC: transform of the frozen archived even lambda=4 trial on a height grid.

Arb evaluates all 4097 archived coefficients (via the v1.42 loader, as in NS104).
This samples a finite trial, not the complete ground; no zero-tail bound, no new
certificate, no G2 or RH statement. Output paths must be fresh.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from types import ModuleType
from typing import Any

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(bits: int, tmax: float, step: float, nzeros: int) -> dict[str, Any]:
    ctx.prec = bits
    coarse = load_module("ground_coarse", ROOT / "evidence/v142/certify_ground_zero.py")
    prior = coarse.load_prior()
    _data, matrices, trial, _head, _tail, provenance = prior.load_trial("even", bits)
    norm2 = sum((trial[i, 16] * trial[i, 16] for i in range(trial.nrows())), arb(0))
    coefficients = [trial[i, 16] / norm2.sqrt() for i in range(trial.nrows())]
    rho = matrices["K"][16, 16] / norm2
    length = 2 * arb(4).log()
    crossover = 2 * arb.pi() * 16  # NS104-corrected: 2 pi e^{2 log 4} = 32 pi

    npts = int(round(tmax / step))
    ts, vals, rads = [], [], []
    for i in range(npts):
        t = arb(i + 1) * arb(step)  # the evaluator divides by t, so the grid starts at one step
        v, _ = coarse.transform_and_derivative(t, coefficients, length)
        ts.append(float(t.mid())); vals.append(float(v.mid())); rads.append(float(v.rad()))
        if i % 2000 == 0:
            print(f"{bits} bits: {i}/{npts}", flush=True)

    # sign changes on the grid (midpoints of straddling cells); the interval radius is checked
    changes = []
    for i in range(npts - 1):
        if vals[i] == 0.0 or vals[i + 1] == 0.0:
            continue
        if (vals[i] < 0) != (vals[i + 1] < 0):
            # require both endpoint intervals to exclude zero at this precision
            if abs(vals[i]) > rads[i] and abs(vals[i + 1]) > rads[i + 1]:
                changes.append(0.5 * (ts[i] + ts[i + 1]))
    zeros = [float(acb.zeta_zero(j).imag.mid()) for j in range(1, nzeros + 1)]

    def nearest_zero(x: float) -> tuple[int, float]:
        j = min(range(len(zeros)), key=lambda k: abs(zeros[k] - x))
        return j + 1, x - zeros[j]

    matched = []
    for c in changes:
        j, d = nearest_zero(c)
        matched.append({"sign_change_height": round(c, 3), "nearest_ordinate_index": j,
                        "offset_from_ordinate": round(d, 3), "within_0.05": abs(d) <= 0.05 + step / 2})

    # band envelopes
    bands = []
    width = 20.0
    for b in range(int(tmax / width)):
        lo, hi = b * width, (b + 1) * width
        idx = [i for i in range(npts) if lo <= ts[i] < hi]
        mx = max(abs(vals[i]) for i in idx)
        bands.append({"band": [lo, hi], "max_abs_F": mx, "log10": round(math.log10(mx), 3) if mx > 0 else None,
                      "max_interval_radius": max(rads[i] for i in idx)})
    below = max(abs(vals[i]) for i in range(npts) if ts[i] < float(crossover.mid()))
    above = max(abs(vals[i]) for i in range(npts) if ts[i] >= float(crossover.mid()))
    above130 = max(abs(vals[i]) for i in range(npts) if ts[i] >= 130.0)
    plateau = [abs(vals[i]) for i in range(npts) if ts[i] >= 200.0]
    sqrt_rho = float(rho.sqrt().mid())

    counts = []
    for T in (50.0, 100.0, 100.53, 150.0, 200.0, 300.0, 400.0):
        counts.append({"T": T, "sign_changes_of_F_below_T": sum(1 for c in changes if c < T),
                       "N_zeta(T)": sum(1 for z in zeros if z < T),
                       "changes_within_0.05_of_an_ordinate": sum(1 for m in matched if m["sign_change_height"] < T and m["within_0.05"])})

    return {
        "classification": "DIAGNOSTIC of the frozen finite archived trial; not the complete ground; not a certificate",
        "bits": bits, "grid_step": step, "t_max": tmax, "points": npts,
        "lambda_multiplicative": 4, "logarithmic_half_width": (length / 2).str(30),
        "crossover_32pi": crossover.str(30), "trial_rayleigh_rho": rho.str(30), "sqrt_rho": sqrt_rho,
        "envelope_bands": bands,
        "max_abs_F_below_crossover": below, "max_abs_F_above_crossover": above, "max_abs_F_above_130": above130,
        "ratio_above_over_below": above / below,
        "plateau_above_200": {"max": max(plateau), "median": sorted(plateau)[len(plateau) // 2],
                              "max_over_sqrt_rho": max(plateau) / sqrt_rho, "median_over_sqrt_rho": sorted(plateau)[len(plateau) // 2] / sqrt_rho},
        "counts": counts,
        "sign_changes": matched,
        "unmatched_below_100": [m for m in matched if m["sign_change_height"] < 100 and not m["within_0.05"]],
        "grid": {"t": ts, "F_mid": vals, "F_rad": rads},
        "provenance": provenance,
        "dependencies": [{"path": str(p.relative_to(ROOT)), "sha256": sha(p)} for p in
                         [ROOT / "evidence/v142/certify_ground_zero.py", ROOT / "evidence/v140/certify_ground4.py"]],
        "script_sha256": sha(Path(__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, choices=(1024, 1280), required=True)
    parser.add_argument("--tmax", type=float, default=400.0)
    parser.add_argument("--step", type=float, default=0.05)
    parser.add_argument("--nzeros", type=int, default=210)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Use a fresh output path; preserve prior reports")
    out = run(args.bits, args.tmax, args.step, args.nzeros)
    args.output.write_text(json.dumps(out, indent=1) + "\n")
    summary = {k: out[k] for k in ("max_abs_F_below_crossover", "max_abs_F_above_crossover", "max_abs_F_above_130",
                                   "ratio_above_over_below", "plateau_above_200", "counts", "unmatched_below_100")}
    summary["bands"] = [(b["band"], b["log10"]) for b in out["envelope_bands"]]
    print(json.dumps(summary, indent=1), flush=True)


if __name__ == "__main__":
    main()
