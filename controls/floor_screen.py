"""Floor screen: evaluate a WEIL-FLOOR candidate on zeta and on Davenport-Heilbronn across windows.

DIAGNOSTIC, NOT A CERTIFICATE. Floating point. Uses the plain explicit-formula
Weil form restricted to tests supported in [-lambda, lambda] (NS-103 machinery
in evidence/diag_ns103_window_calibration/weil_window.py), not the manuscript's
semilocal form. A candidate that passes here has only survived a screen.

Why this exists. The v1.36 target is a uniform floor q[f] >= -C ||f||^2 with
one C for every window. For zeta that is the open input; for the
Davenport-Heilbronn function the plain form has NO floor (its minimum per unit
norm falls without bound as the window grows, NS-103). So any chain of
inequalities that would prove a floor must contain a step that FAILS on the
Davenport-Heilbronn object. This tool evaluates each step of a candidate chain
on both objects and reports where it fails, before anyone attempts a proof.

Built-in candidates:
  plain      the claim "q >= -C ||f||^2" itself; reports min eig / lambda.
  abel       the PR #58 shape: damp every prime weight by n^{-eps}; the chain is
             (i) q_eps >= 0 and (ii) q_eps - q <= C ||f||^2 uniformly in lambda.
             Reports min eig(q_eps)/lambda and max eig(q_eps - q)/lambda.
  custom     module:function returning {"name": matrix, ...} built from
             (data, lam, K, ww); every matrix gets min and max eig / lambda.

    .venv/bin/python controls/floor_screen.py --candidate plain --C 1
    .venv/bin/python controls/floor_screen.py --candidate abel --eps 2 --C 1
    .venv/bin/python controls/floor_screen.py --candidate custom --custom mymod:build
"""
from __future__ import annotations

import argparse
import importlib
import json
import math
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any, Callable

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evidence/diag_ns103_window_calibration"))
import weil_window as ww  # noqa: E402

DEFAULT_LAMS = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
FMAX = 130.0


def basis_size(lam: float, fmax: float = FMAX) -> int:
    return int(math.ceil(2 * lam * fmax / math.pi)) + 4


def damped(data: ww.Completed, eps: float) -> ww.Completed:
    """Multiply every prime-side weight Lambda_D(n) by n^{-eps} (Abel damping in log scale)."""
    n = np.arange(len(data.lam), dtype=float)
    n[0] = 1.0
    return replace(data, name=f"{data.name}[abel eps={eps}]", lam=data.lam * n ** (-eps))


def eig_range(M: np.ndarray, lam: float) -> tuple[float, float]:
    ev = np.linalg.eigvalsh((M + M.T) / 2)
    return float(ev[0] / lam), float(ev[-1] / lam)


def screen(candidate: str, lams: list[float], C: float, eps: float,
           custom: Callable[..., dict[str, np.ndarray]] | None) -> dict[str, Any]:
    nmax = int(math.exp(2 * max(lams))) + 2
    objects = {"zeta": ww.zeta_data(nmax), "davenport-heilbronn": ww.dh_data(nmax)}
    rows: list[dict[str, Any]] = []
    for lam in lams:
        K = basis_size(lam)
        row: dict[str, Any] = {"lambda": lam, "K": K}
        for name, data in objects.items():
            base = ww.window_matrix(data, lam, K)
            entry: dict[str, Any] = {}
            if candidate == "plain":
                lo, hi = eig_range(base["W"], lam)
                entry = {"min_eig_over_lambda": lo, "floor_holds_with_C": lo >= -C}
            elif candidate == "abel":
                damp = ww.window_matrix(damped(data, eps), lam, K)
                lo_eps, _ = eig_range(damp["W"], lam)
                diff = damp["W"] - base["W"]           # = P - P_eps (prime side only)
                _, hi_diff = eig_range(diff, lam)
                entry = {"step_i_min_eig_q_eps_over_lambda": lo_eps, "step_i_holds": lo_eps >= 0,
                         "step_ii_max_eig_diff_over_lambda": hi_diff, "step_ii_holds_with_C": hi_diff <= C}
            else:
                assert custom is not None
                for mname, M in custom(data, lam, K, ww).items():
                    lo, hi = eig_range(M, lam)
                    entry[mname] = {"min_over_lambda": lo, "max_over_lambda": hi}
            row[name] = entry
        rows.append(row)
        print(json.dumps(row), file=sys.stderr, flush=True)
    return {"classification": "diagnostic floor screen on the plain window-restricted Weil form; not a certificate",
            "candidate": candidate, "C": C, "eps": eps if candidate == "abel" else None,
            "FMAX": FMAX, "rows": rows, "verdict": verdict(candidate, rows, C)}


def verdict(candidate: str, rows: list[dict[str, Any]], C: float) -> str:
    dh = [r["davenport-heilbronn"] for r in rows]
    zt = [r["zeta"] for r in rows]
    if candidate == "plain":
        bad = [r["lambda"] for r in rows if not r["davenport-heilbronn"]["floor_holds_with_C"]]
        zbad = [r["lambda"] for r in rows if not r["zeta"]["floor_holds_with_C"]]
        s = (f"Davenport-Heilbronn violates the floor -C from lambda = {bad[0]} on" if bad
             else "Davenport-Heilbronn satisfies the floor on every scanned window: widen the scan; the plain form has no floor there")
        return s + ("; zeta holds on every scanned window (as it must if RH)" if not zbad else f"; zeta violates at {zbad}: pipeline error")
    if candidate == "abel":
        def fails(entries: list[dict[str, Any]], key: str) -> list[float]:
            return [r["lambda"] for r, e in zip(rows, entries) if not e[key]]
        i_dh, ii_dh = fails(dh, "step_i_holds"), fails(dh, "step_ii_holds_with_C")
        i_z, ii_z = fails(zt, "step_i_holds"), fails(zt, "step_ii_holds_with_C")
        grow = dh[-1]["step_ii_max_eig_diff_over_lambda"] / max(dh[0]["step_ii_max_eig_diff_over_lambda"], 1e-300)
        if not i_dh and not ii_dh:
            return ("BOTH steps hold on Davenport-Heilbronn on the scanned windows, which would prove a false floor: "
                    "the chain has a step that fails at larger windows or a hypothesis the control violates; name it or stop")
        parts = []
        parts.append(f"step (i) q_eps >= 0 fails on zeta at lambda {i_z}" if i_z else "step (i) holds on zeta")
        parts.append(f"and on Davenport-Heilbronn at {i_dh}" if i_dh else "and holds on Davenport-Heilbronn")
        parts.append(f"; step (ii) <= C fails on zeta at {ii_z}" if ii_z else "; step (ii) holds on zeta")
        parts.append(f"and on Davenport-Heilbronn at {ii_dh}, growing by a factor {grow:.3g} across the scan" if ii_dh else "and holds on Davenport-Heilbronn")
        if ii_z and ii_dh:
            parts.append("; no uniform C on either object: the damping cannot be removed at constant cost (NS47/PR58)")
        if (i_z or ii_z) and not (i_dh or ii_dh):
            parts.append("; the chain fails on zeta but not on the control: it is not a floor argument for zeta")
        return " ".join(parts)
    return "custom candidate: read the per-matrix ranges; a step that holds on Davenport-Heilbronn cannot carry a floor proof by itself"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--candidate", choices=("plain", "abel", "custom"), required=True)
    parser.add_argument("--C", type=float, default=1.0, help="claimed uniform floor / bound constant per unit norm")
    parser.add_argument("--eps", type=float, default=2.0, help="abel damping exponent")
    parser.add_argument("--custom", default=None, help="module:function for --candidate custom")
    parser.add_argument("--lams", type=float, nargs="*", default=DEFAULT_LAMS)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    fn = None
    if args.candidate == "custom":
        modname, fname = args.custom.split(":")
        fn = getattr(importlib.import_module(modname), fname)
    out = screen(args.candidate, args.lams, args.C, args.eps, fn)
    text = json.dumps(out, indent=1)
    print(text)
    if args.output:
        Path(args.output).write_text(text + "\n")


if __name__ == "__main__":
    main()
