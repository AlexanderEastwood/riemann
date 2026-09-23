"""Exact finite identity checks and Arb scalar replay; no optimized error run."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
from typing import Any
from flint import arb, ctx

HERE = Path(__file__).resolve().parent


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def jordan_exact(n: int, power: int) -> int:
    """Divisor recursion, independent of the product formula in the proof."""
    return n**power - sum(jordan_exact(d, power) for d in divisors(n)[:-1])


def grouped(vector: list[int]) -> dict[int, int]:
    answer: dict[int, int] = {}
    for i, x in enumerate(vector, 1):
        for j, y in enumerate(vector, 1):
            k = lcm(i, j)
            answer[k] = answer.get(k, 0) + x * y
    return answer


def finite_checks(n: int) -> dict[str, Any]:
    vector = [(-1)**i * (i % 3 + 1) for i in range(1, n + 1)]
    q = grouped(vector)
    incidence_count = 0
    for m in range(1, 3*n*n + 1):
        assert sum(v for k, v in q.items() if m % k == 0) == sum(
            vector[i-1] for i in range(1, n+1) if m % i == 0
        )**2
        incidence_count += 1
    for power in [1, 2, 3]:
        direct = sum((Fraction(v, k**power) for k, v in q.items()), Fraction(0))
        factored = sum((jordan_exact(d, power) * sum(
            (Fraction(vector[i-1], i**power) for i in range(d, n+1, d)), Fraction(0)
        )**2 for d in range(1, n+1)), Fraction(0))
        assert direct == factored > 0
    # Every new LCM basis vector is realized with either sign by a PSD
    # rank-one square plus old terms. Test coefficients, not a mocked Gram.
    new_indices = sorted(k for k in q if k > n)
    for k in new_indices:
        i, j = next((i, j) for i in range(1, n+1) for j in range(i+1, n+1) if lcm(i, j) == k)
        for sign in [-1, 1]:
            pair = [int(d == i) + sign*int(d == j) for d in range(1, n+1)]
            pair_q = grouped(pair)
            assert {ell: value for ell, value in pair_q.items() if ell > n and value} == {k: 2*sign}
    s = arb(4)/7
    direct_ball = sum((arb(v) / arb(k)**s for k, v in q.items()), arb(0))
    jordan: dict[int, arb] = {}
    for d in range(1, n+1):
        jordan[d] = arb(d)**s - sum((jordan[e] for e in divisors(d)[:-1]), arb(0))
        assert jordan[d] > 0
    factored_ball = sum((jordan[d]*sum(
        (arb(vector[i-1])/arb(i)**s for i in range(d, n+1, d)), arb(0)
    )**2 for d in range(1, n+1)), arb(0))
    assert direct_ball.overlaps(factored_ball) and direct_ball > 0
    # Direct double-sum reciprocal-LCM definition, independent grouping.
    matrix_ball = sum((arb(vector[i-1]*vector[j-1]) * arb(gcd(i,j))**s
                       / (arb(i)**s*arb(j)**s)
                       for i in range(1, n+1) for j in range(1, n+1)), arb(0))
    assert matrix_ball.overlaps(direct_ball)
    return {"N": n, "vector": vector, "q": {str(k): v for k, v in sorted(q.items())},
            "incidence_checks": incidence_count, "exact_Jordan_powers": [1, 2, 3],
            "signed_projected_generators": 2*len(new_indices),
            "values": {"Q": str(direct_ball), "Jordan_Q": str(factored_ball), "matrix_Q": str(matrix_ball)}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    s = arb(4)/7
    ell = arb(2).log()
    norm = 1/(1-s)**2 + 1/(2*s-1)
    floor = 1/(s**4*norm)
    kappa = 1-ell-ell**2/2-ell**4/8
    x = Fraction(25, 36)
    rational_gap = 1-x-x*x/2-x**4/8-Fraction(1, 32)
    assert rational_gap == Fraction(55199, 13436928) > 0
    assert floor.contains(arb(3087)/4096)
    assert kappa > arb(1)/32 and ell < arb(25)/36 and s.zeta() < 0
    values = {"s": s, "zeta_s": s.zeta(), "evaluator_norm_squared": norm,
              "negative_floor": floor, "positive_floor": kappa, "log2": ell,
              "positive_floor_minus_1_32": kappa-arb(1)/32}
    out = {"classification": "Exact finite algebra and certified scalar constants only; no finite optimization or cofinal estimate",
           "precision_bits": args.bits, "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "values": {k: str(v) for k, v in values.items()},
           "rational_gap": str(rational_gap), "rows": [finite_checks(n) for n in [3, 4, 8, 12]],
           "cutoff_status": "Not applicable: no truncated physical or Gram integral used"}
    args.output.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"bits": args.bits, "status": "PASS", "positive_floor": str(kappa)}))


if __name__ == "__main__":
    main()
