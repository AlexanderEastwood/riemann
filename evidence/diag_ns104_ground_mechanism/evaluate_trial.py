"""DIAGNOSTIC of a frozen finite trial, not complete eigenfunction samples.

Arb evaluates all 4097 archived coefficients. Root shifts and sample-energy
ratios are diagnostics; no omitted-zero remainder or new ground transfer
is asserted. Existing v1.43 bounds are read separately, never reinterpreted
as measured errors. Output paths must be fresh.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
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


def midpoint(value: arb) -> float:
    """Display only; never a certificate gate."""
    return float(value.mid())


def run(bits: int) -> dict[str, Any]:
    ctx.prec = bits
    coarse = load_module("ground_coarse", ROOT / "evidence/v142/certify_ground_zero.py")
    prior = coarse.load_prior()
    _data, matrices, trial, _head, _tail, provenance = prior.load_trial("even", bits)
    norm2 = sum((trial[i, 16] * trial[i, 16] for i in range(trial.nrows())), arb(0))
    coefficients = [trial[i, 16] / norm2.sqrt() for i in range(trial.nrows())]
    rho = matrices["K"][16, 16] / norm2
    length = 2 * arb(4).log()
    sample_sum = arb(0)
    rows: list[dict[str, Any]] = []
    for j in range(1, 65):
        gamma = acb.zeta_zero(j).imag
        value, slope = coarse.transform_and_derivative(gamma, coefficients, length)
        left, _ = coarse.transform_and_derivative(gamma - arb(".01"), coefficients, length)
        right, _ = coarse.transform_and_derivative(gamma + arb(".01"), coefficients, length)
        sample_sum += 2 * value * value
        shift = -value / slope if not slope.contains(0) else None
        row: dict[str, Any] = {
            "j": j, "gamma": gamma.str(85), "trial_value": value.str(85),
            "trial_derivative": slope.str(85),
            "trial_value_squared_over_rho": (value * value / rho).str(85),
            "formal_two_sided_partial_sum_over_rho": (sample_sum / rho).str(85),
            "endpoint_offset": "0.01", "left_value": left.str(85), "right_value": right.str(85),
            "endpoint_sign_change": bool((left < 0 and right > 0) or (left > 0 and right < 0)),
            "linearized_trial_shift": shift.str(85) if shift is not None else None,
            "display_only": {"gamma": midpoint(gamma), "abs_value": abs(midpoint(value)),
                             "slope": midpoint(slope), "value_over_sqrt_rho": abs(midpoint(value / rho.sqrt())),
                             "linearized_shift": midpoint(shift) if shift is not None else None},
        }
        if shift is not None and abs(midpoint(shift)) < 0.001:
            at_step, _ = coarse.transform_and_derivative(gamma + shift, coefficients, length)
            row["value_at_one_newton_step"] = at_step.str(85)
            row["sqrt_rho_over_abs_trial_slope"] = (rho.sqrt() / abs(slope)).str(85)
        rows.append(row)
        if j % 16 == 0:
            print(f"{bits} bits: {j}/64 archived trial ordinates", flush=True)
    old = json.loads((ROOT / f"evidence/v143/resolution_b{bits}.json").read_text())
    first = rows[0]["display_only"]
    return {
        "classification": "DIAGNOSTIC of finite archived trial; no complete-ground zero enumeration",
        "bits": bits, "lambda_multiplicative": 4, "logarithmic_half_width": (length / 2).str(85),
        "finite_trial_modes": len(coefficients), "normalized": True, "trial_rayleigh": rho.str(85),
        "complete_mu0": "Only 0<mu0<=rho known here; rho is not a measured eigenvalue",
        "heuristic_NS103_crossover_after_parameter_conversion": (2 * arb.pi() * 16).str(85),
        "rows": rows,
        "summary": {
            "all_64_endpoint_sign_changes": all(row["endpoint_sign_change"] for row in rows),
            "max_value_over_sqrt_rho": max(row["display_only"]["value_over_sqrt_rho"] for row in rows),
            "formal_partial_sum_over_rho": (sample_sum / rho).str(85),
            "first_linearized_trial_shift": first["linearized_shift"],
            "first_sqrt_rho_over_abs_trial_slope": rows[0].get("sqrt_rho_over_abs_trial_slope"),
            "first_shift_over_that_scale": first["value_over_sqrt_rho"],
            "existing_complete_ground_radius": old["radius"],
            "existing_complete_evaluator_constant": old["evaluator_dual_constant"],
            "existing_complete_derivative_floor": "0.0016",
        },
        "scope": "No transfer of the 64 trial signs or Newton shifts to the complete ground. No numerical eigenfunction reconstruction, zero-tail sum bound, RH assumption or new certificate. The finite partial sum is not an energy fraction unless the exact zero-side representation and nonnegative full remainder are justified.",
        "provenance": provenance,
        "dependencies": [
            {"path": str(path.relative_to(ROOT)), "sha256": sha(path)} for path in
            [ROOT / "evidence/v142/certify_ground_zero.py", ROOT / "evidence/v140/certify_ground4.py",
             ROOT / f"evidence/v143/resolution_b{bits}.json"]
        ],
        "script_sha256": sha(Path(__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, choices=(1024, 1280), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Use a fresh output path; preserve prior reports")
    out = run(args.bits)
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out["summary"], indent=2), flush=True)


if __name__ == "__main__":
    main()
