"""Bounded Jacobi-product admission screen; floating diagnostics, not bounds."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from types import ModuleType
from typing import Any, Callable

import mpmath as mp

COMMIT = "f32cadfb7be523a8920b19be57d40d652e39a2ef"
REVIEW = "/Users/alex/riemann-worktrees/conclusions-review"


def load_control() -> tuple[ModuleType, str]:
    source = subprocess.check_output(
        ["git", "show", f"{COMMIT}:controls/davenport_heilbronn.py"], cwd=REVIEW
    )
    module = ModuleType("pinned_davenport_heilbronn")
    exec(compile(source, "pinned_davenport_heilbronn.py", "exec"), module.__dict__)
    return module, hashlib.sha256(source).hexdigest()


def multiply(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for i, x in a.items():
        for j, y in b.items():
            result[i + j] = result.get(i + j, 0) + x * y
    return {i: x for i, x in result.items() if x}


def coefficients(count: int) -> dict[int, int]:
    result = {0: 1}
    for n in range(1, count + 1):
        result = multiply(result, {0: 1, 2 * n: -1})
        result = multiply(result, {0: 1, 2 * n - 1: 2, 4 * n - 2: 1})
    return result


def h_derivative_at_zero(coeff: dict[int, int], order: int = 1) -> Any:
    def h(t: Any) -> Any:
        return mp.exp(t / 2) * mp.fsum(
            c * mp.exp(-mp.pi * k * mp.exp(2 * t)) for k, c in coeff.items()
        )
    return mp.diff(h, mp.mpf(0), order)


def half_integral(k: int, z: Any) -> Any:
    a = (z + mp.mpf("0.5")) / 2
    v = mp.pi * k
    return mp.power(v, -a) * mp.gammainc(a, v, mp.inf) / 2


def product_transform(coeff: dict[int, int], z: Any) -> Any:
    terms = mp.fsum(
        c * (half_integral(k, z) + half_integral(k, -z))
        for k, c in coeff.items() if k > 0
    )
    return mp.mpf("0.25") + (z * z - mp.mpf("0.25")) * terms / 4


def radial(function: Callable[[Any], Any], z: Any) -> Any:
    return mp.re(mp.diff(function, z) * mp.conj(function(z)))


def serialize(value: Any) -> str:
    return str(mp.nstr(value, 35))


def direct_transform(coeff: dict[int, int], z: Any) -> tuple[Any, Any]:
    """Independent half-line quadrature, including the reflection boundary mass.

    The integration ends at t=3; its tail is reported separately, not hidden.
    """
    def density(t: Any) -> Any:
        r = mp.exp(2 * t)
        return mp.exp(t / 2) * mp.fsum(
            c * ((mp.pi * k * r) ** 2 - mp.mpf("1.5") * mp.pi * k * r)
            * mp.exp(-mp.pi * k * r)
            for k, c in coeff.items() if k > 0
        )
    intervals = [0, mp.mpf("0.25"), mp.mpf("0.5"), 1, mp.mpf("1.5"), 2, 3]
    value = h_derivative_at_zero(coeff) / 2 + 2 * mp.quad(
        lambda t: density(t) * mp.cosh(z * t), intervals
    )
    derivative = 2 * mp.quad(
        lambda t: t * density(t) * mp.sinh(z * t), intervals
    )
    return value, derivative


def quadrature_tail(coeff: dict[int, int], x: Any, *, derivative: bool) -> Any:
    """Analytic absolute tail majorant, evaluated at floating precision.

    Bound |cosh((x+iy)t)| and |sinh((x+iy)t)| by exp(|x|t).
    For the derivative use t<=exp(t) on t>=3, producing the same integral
    with x replaced by |x|+1. This is not an interval-certified number.
    """
    exponent = abs(x) + (1 if derivative else 0)
    alpha = (exponent + mp.mpf("0.5")) / 2
    start = mp.exp(6)
    return mp.fsum(
        abs(c) * (mp.pi * k) ** (-alpha)
        * (mp.gammainc(alpha + 2, mp.pi * k * start, mp.inf)
           + mp.mpf("1.5") * mp.gammainc(alpha + 1, mp.pi * k * start, mp.inf))
        for k, c in coeff.items() if k > 0
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=35)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--witness", nargs=2, metavar=("X", "Y"))
    parser.add_argument("--direct", action="store_true")
    args = parser.parse_args()
    mp.mp.dps = args.dps
    dh, source_hash = load_control()
    controls: list[dict[str, Any]] = []
    rho = mp.findroot(dh.f, dh.C(*dh.GUESS))
    dh_z = rho - mp.mpf("0.5") - mp.mpf("0.02")
    controls.append(dh.screen(
        lambda f, phi: bool(radial(f, dh_z) >= 0),
        "Actual radial-sign functional, structural control only",
        sample_domain=f"z={serialize(dh_z)}",
        applicability="Even completed transform; original Jacobi product is not assumed in this calibration.",
        observations={"radial": serialize(radial(dh.F, dh_z))},
    ))
    controls.append(dh.screen(
        lambda f, phi: None, "Exact finite Jacobi product premise",
        sample_domain="M>=1; 0<x<=1/2; y real",
        applicability="Davenport-Heilbronn has different theta coefficients, conductor and gamma factor; not this Jacobi product completion.",
        applicable=False,
    ))
    def altered(z: Any) -> Any:
        return (3 + 2 * mp.cosh(2 * z)) * dh.F_xi(z) / (3 + 2 * mp.cosh(1))
    altered_z = (mp.acosh(mp.mpf("1.5")) / 2 - mp.mpf("0.02")) + mp.j * mp.pi / 2
    controls.append({
        "name": "NS101 reciprocal mixture",
        "z": serialize(altered_z), "radial": serialize(radial(altered, altered_z)),
        "candidate_applicability": "not-applicable: different lattice frequencies; no original finite product premise",
    })
    coeff = coefficients(1)
    def candidate(z: Any) -> Any:
        return product_transform(coeff, z)
    samples: list[dict[str, str]] = []
    if args.witness:
        points = [(mp.mpf(args.witness[0]), mp.mpf(args.witness[1]))]
    else:
        points = [(mp.mpf("0.25"), mp.mpf(y)) for y in range(0, 61, 2)]
    for x, y in points:
        z = x + mp.j * y
        value = radial(candidate, z)
        samples.append({"x": serialize(x), "y": serialize(y), "radial": serialize(value),
                        "F": serialize(candidate(z)), "Fprime": serialize(mp.diff(candidate, z)),
                        "original_xi_radial": serialize(radial(dh.F_xi, z))})
        if value < 0:
            break
    verification: dict[str, Any] = {}
    if args.direct:
        last = samples[-1]
        z = mp.mpf(last["x"]) + mp.j * mp.mpf(last["y"])
        direct_f, direct_derivative = direct_transform(coeff, z)
        verification = {
            "method": "Direct density quadrature on [0,3] plus exact-formula boundary mass",
            "F": serialize(direct_f), "Fprime": serialize(direct_derivative),
            "radial": serialize(mp.re(direct_derivative * mp.conj(direct_f))),
            "difference_F": serialize(abs(direct_f - candidate(z))),
            "difference_Fprime": serialize(abs(direct_derivative - mp.diff(candidate, z))),
            "absolute_tail_majorant_F": serialize(quadrature_tail(coeff, mp.re(z), derivative=False)),
            "absolute_tail_majorant_Fprime": serialize(quadrature_tail(coeff, mp.re(z), derivative=True)),
            "tail_status": "Analytic formula evaluated at floating precision; quadrature and rounding not certified",
        }
    result = {
        "classification": "floating diagnostic, not a certificate or proof",
        "dps": args.dps, "commit": COMMIT, "control_sha256": source_hash,
        "controls": controls, "M": 1, "coefficients": coeff,
        "boundary_mass": serialize(h_derivative_at_zero(coeff) / 2),
        "candidate_samples": samples,
        "negative_found": any(mp.mpf(row["radial"]) < 0 for row in samples),
        "independent_integral_check": verification,
        "scope": "Finite-product candidate only. No negative original xi value or limiting-sign conclusion.",
    }
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"output": str(args.output), "negative_found": result["negative_found"],
                      "last_sample": samples[-1], "boundary_mass": result["boundary_mass"]}))


if __name__ == "__main__":
    main()
