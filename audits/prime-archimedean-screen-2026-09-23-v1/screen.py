"""Pre-claim Abel-damping screen. Mpmath diagnostics, not certificates.

The all-test undamping inequality is not inferred from any finite sample.
Below epsilon=1/2 the continued logarithmic derivative is not silently
identified with the Fourier multiplier of the physical damped form.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Callable

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from controls.davenport_heilbronn import C, F, F_xi, GUESS, f, screen  # noqa: E402

Function = Callable[[Any], Any]


def point(real: Any, imag: Any) -> Any:
    """Preserve mpmath values without narrowing them to machine floats."""
    return mp.mpc(real, imag)


def symbol(fun: Function, z: Any) -> Any:
    return 2 * mp.re(mp.diff(fun, z) / fun(z))


def order_two(z: Any) -> Any:
    return mp.exp(z * z) * (3 + 2 * mp.cosh(z))


def reciprocal_dilation(z: Any) -> Any:
    return F_xi(z) * (3 + 2 * mp.cosh(2 * z)) / (3 + 2 * mp.cosh(1))


def shifted_product(z: Any) -> Any:
    return F_xi(2 * z + mp.mpf("0.5")) * F_xi(2 * z - mp.mpf("0.5"))


def prime_powers(limit: int) -> list[tuple[int, int]]:
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    pairs: list[tuple[int, int]] = []
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for n in range(p * p, limit + 1, p):
            prime[n] = False
        n = p
        while n <= limit:
            pairs.append((n, p))
            n *= p
    return sorted(pairs)


def show(value: Any) -> str:
    return mp.nstr(value, 25)


def run(dps: int) -> dict[str, Any]:
    mp.mp.dps = dps
    gamma1 = mp.im(mp.zetazero(1))
    dh_zero = mp.findroot(f, C(*GUESS)) - mp.mpf("0.5")
    heights = [mp.mpf(0), gamma1, mp.mpf(20), mp.im(dh_zero), mp.mpf("176.702461")]
    functions: dict[str, Function] = {"zeta": F_xi, "davenport_heilbronn": F,
                                     "NS100_order_two": order_two,
                                     "NS101_reciprocal_dilation": reciprocal_dilation,
                                     "shifted_zeta_product": shifted_product}
    sampled: dict[str, Any] = {}
    for name, fun in functions.items():
        values = [symbol(fun, point(2, t)) for t in heights]
        sampled[name] = {"values": [show(v) for v in values],
                         "minimum": show(min(values)),
                         "outcome": "sampled-pass" if min(values) >= 0 else "sampled-failure"}
    dh_min = min(symbol(F, point(2, t)) for t in heights)
    tool_screen = screen(
        lambda _F, _phi: dh_min >= 0,
        "Abel-damped logarithmic derivative at epsilon=2",
        sample_domain="z=2+i*t at t=0,gamma1,20,Im(DH zero),176.702461",
        applicability="Same function expression only; original zeta gamma/pole/prime coefficients do not transfer. The full all-test undamping bound is untested.",
        observations={"min_symbol": show(dh_min)},
    )
    interior_points = {
        "davenport_heilbronn": dh_zero - mp.mpf("0.02"),
        "NS100_order_two": point(mp.acosh(mp.mpf("1.5")) - mp.mpf("0.02"), mp.pi),
        "NS101_reciprocal_dilation": point(mp.acosh(mp.mpf("1.5")) / 2 - mp.mpf("0.02"), mp.pi / 2),
        "shifted_zeta_product": C("0.23", gamma1 / 2),
    }
    interior: dict[str, Any] = {}
    for name, z in interior_points.items():
        value = symbol(functions[name], z)
        interior[name] = {"z": str(z), "continued_expression": show(value),
                          "original_zeta_same_point": show(symbol(F_xi, z)),
                          "outcome": "sampled-failure" if value < 0 else "sampled-pass",
                          "physical_multiplier_transfer": "NOT ASSERTED outside the separately justified convergence domain"}
    arithmetic: list[dict[str, Any]] = []
    pairs = prime_powers(4000)
    for limit in (1000, 4000):
        sigma = mp.mpf("2.5")
        tail = 2 * mp.power(limit, 1 - sigma) * (mp.log(limit) / (sigma - 1) + 1 / (sigma - 1) ** 2)
        rows = []
        for t in heights:
            s = point(sigma, t)
            prime_sum = mp.fsum(mp.log(p) * mp.power(n, -s) for n, p in pairs if n <= limit)
            arch_pole = 2 * mp.re(1 / s + 1 / (s - 1) + mp.digamma(s / 2) / 2 - mp.log(mp.pi) / 2)
            partial = arch_pole - 2 * mp.re(prime_sum)
            exact_expression = symbol(F_xi, point(2, t))
            error = abs(partial - exact_expression)
            rows.append({"t": show(t), "arch_pole": show(arch_pole),
                         "twice_real_prime_prefix": show(2 * mp.re(prime_sum)),
                         "partial_symbol": show(partial), "completed_expression": show(exact_expression),
                         "absolute_difference": show(error), "within_tail_diagnostic": bool(error < tail)})
        arithmetic.append({"N": limit, "sigma": "2.5", "elementary_tail_allowance": show(tail), "rows": rows})
    full_bound = screen(
        lambda _F, _phi: None,
        "Existence of C with q_epsilon-q <= C||f||^2 on every compact test",
        sample_domain="No finite sample establishes the existential, all-support bound",
        applicability="Full condition not established on any control; exact original coefficients/gamma/poles also differ",
    )
    return {"dps": dps, "heights": [show(t) for t in heights],
            "epsilon2": sampled, "DH_expression_screen": tool_screen,
            "continued_interior_checks": interior, "prime_prefix_checks": arithmetic,
            "all_test_bound_control_outcome": full_bound}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Preserve previous outputs; choose a fresh path")
    out = {"classification": "pre-claim diagnostic screen, not a numerical certificate",
           "candidate": "fixed Abel damping epsilon=2 plus an all-test, support-independent upper bound on q_epsilon-q",
           "screen_order": "Recorded proposal; function/control and prime-prefix screen before obstruction/domain audit",
           "replays": [run(dps) for dps in (30, 50)],
           "limits": "Samples check the damped expression and demonstrate that its positivity is not distinguishing. They do not refute or prove the quantified undamping bound; that is assessed using the existing NS47 theorem. Interior continuation samples are not physical-form multiplier identities.",
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "control_sha256": hashlib.sha256((ROOT / "controls/davenport_heilbronn.py").read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"epsilon2_outcomes": {k: v["outcome"] for k, v in out["replays"][1]["epsilon2"].items()},
                      "interior": out["replays"][1]["continued_interior_checks"]}, indent=2))


if __name__ == "__main__":
    main()
