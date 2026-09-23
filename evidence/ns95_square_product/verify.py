"""Verify complete-cost replays, bindings and exact product constraints."""
from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any
from flint import arb, ctx
from certify import product_data

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name: str) -> dict[str, Any]:
    return json.loads((HERE/name).read_text())


def overlaps(left: dict[str, str], right: dict[str, str]) -> int:
    assert left.keys() == right.keys()
    for k, v in left.items():
        assert arb(v).overlaps(arb(right[k])), k
    return len(left)


def main() -> None:
    ctx.prec = 384
    data = [read(n) for n in ["check-256bits.json", "check-384bits.json", "check-cutoff-384bits.json"]]
    physical = [read(n) for n in ["physical-256bits.json", "physical-384bits.json", "physical-cutoff-384bits.json"]]
    assert [d["precision_bits"] for d in data] == [256, 384, 384]
    assert [d["kernel_cutoff"] for d in data] == [128, 128, 256]
    assert [d["precision_bits"] for d in physical] == [256, 384, 384]
    assert [d["cell_stop"] for d in physical] == [65536, 65536, 131072]
    counts = {"scalar_precision_overlaps": 0, "coefficient_precision_overlaps": 0,
              "scalar_cutoff_overlaps": 0, "coefficient_cutoff_overlaps": 0,
              "physical_precision_overlaps": 0, "physical_cutoff_overlaps": 0,
              "complete_physical_Gram_overlaps": 0, "NS86_scalar_overlaps": 0,
              "exact_large_prime_fiber_checks": 0}
    for report in data:
        assert report["source_sha256"] == digest(HERE/"certify.py")
        assert report["kernel_sha256"] == digest(ROOT/"evidence/v159/ns61/certify_smoothed.py")
        for row in report["rows"]:
            assert all(row["gates"].values())
    for report in physical:
        assert report["source_sha256"] == digest(HERE/"physical.py")
        assert report["input_sha256"] == digest(HERE/report["input_file"])
        for path, value in report["dependencies"].items():
            assert digest(ROOT/path) == value
        lookup = {r["N"]: r for r in read(report["input_file"])["rows"]}
        for row in report["rows"]:
            assert arb(row["values"]["complete_energy"]).overlaps(arb(lookup[row["N"]]["values"]["free_lift_error"]))
            assert arb(row["values"]["relative_improvement"]) > 0
            counts["complete_physical_Gram_overlaps"] += 1
    for a, b in zip(data[0]["rows"], data[1]["rows"], strict=True):
        assert a["N"] == b["N"]
        counts["scalar_precision_overlaps"] += overlaps(a["values"], b["values"])
        for field in ["free_lift_complete_coefficients", "free_lift_parameters"]:
            for x, y in zip(a[field], b[field], strict=True):
                assert arb(x).overlaps(arb(y))
                counts["coefficient_precision_overlaps"] += 1
    a, b = data[1]["rows"][-1], data[2]["rows"][0]
    assert a["N"] == b["N"] == 16
    counts["scalar_cutoff_overlaps"] += overlaps(a["values"], b["values"])
    for field in ["free_lift_complete_coefficients", "free_lift_parameters"]:
        for x, y in zip(a[field], b[field], strict=True):
            assert arb(x).overlaps(arb(y))
            counts["coefficient_cutoff_overlaps"] += 1
    for a, b in zip(physical[0]["rows"], physical[1]["rows"], strict=True):
        counts["physical_precision_overlaps"] += overlaps(a["values"], b["values"])
    a, b = physical[1]["rows"][-1]["values"], physical[2]["rows"][0]["values"]
    for key in a:
        if key != "physical_tail_radius":
            assert arb(a[key]).overlaps(arb(b[key])), key
            counts["physical_cutoff_overlaps"] += 1
    assert arb(b["physical_tail_radius"]) < arb(a["physical_tail_radius"])/3

    prior = json.loads((ROOT/"evidence/ns86_optimized_arithmetic/newton-384bits.json").read_text())
    for a, b in zip(data[1]["rows"], prior["rows"], strict=True):
        assert a["N"] == b["N"]
        old = b["families"]["original"]["values"]
        for newkey, oldkey in [("E_N", "E_N"), ("E_N_squared", "E_N_squared"),
                               ("full_gain_relative", "full_gain_relative"),
                               ("NS86_projected_gain_fraction", "projected_gain_fraction")]:
            assert arb(a["values"][newkey]).overlaps(arb(old[oldkey]))
            counts["NS86_scalar_overlaps"] += 1
        n = a["N"]
        products, matrix, pivots = product_data(n)
        assert a["product_seeds"] == products
        assert a["lift_basis_seeds"] == [products[j] for j in pivots]
        assert a["free_lift_rank"] == len(pivots)
        primes = [p for p in range(n+1, n*n+1) if all(p % d for d in range(2, isqrt(p)+1))]
        assert a["prime_pair"] == [primes[0], primes[-1]]
        for p in primes:
            for m in range(1, n*n//p+1):
                expected = [int(m % d == 0) for d in products]
                assert matrix[m*p-n-1] == expected
                counts["exact_large_prime_fiber_checks"] += 1
        v = {k: arb(s) for k, s in a["values"].items()}
        assert v["product_pairing_minor"] < 0
        assert v["free_lift_gain_fraction"] > arb("0.9974")
        assert v["missing_gain_fraction"] > v["prime_constraint_loss_fraction"] > 0
    final = {k: arb(v) for k, v in data[2]["rows"][0]["values"].items()}
    assert arb("0.99827") < final["free_lift_gain_fraction"] < arb("0.99828")
    assert final["free_lift_gain_relative"] > arb("0.55636")
    exact = (HERE/"checks-output.txt").read_text()
    assert "PASS: 18 exact checks" in exact and " -- an error." not in exact
    out = {"status": "PASS", "classification": "finite certificates and scoped analytic restrictions; no cofinal gain bound",
           "checks": counts, "Maxima_exact_checks": 18,
           "source_sha256": digest(Path(__file__)), "independent_review": False}
    (HERE/"validation.json").write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
