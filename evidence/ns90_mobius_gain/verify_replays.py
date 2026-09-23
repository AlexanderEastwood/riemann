"""Check the fresh numerator decomposition against the archived full Gram."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name: str) -> dict[str, Any]:
    return json.loads((HERE/name).read_text())


def main() -> None:
    ctx.prec = 384
    a, b, cut = [read(name) for name in ["check-256bits.json", "check-384bits.json",
                                        "check-cutoff-384bits.json"]]
    counts = {"precision_scalar_overlaps": 0, "cutoff_complete_overlaps": 0,
              "archived_Gram_numerator_overlaps": 0, "negative_triangle_bounds": 0,
              "wrong_sign_if_finite_divisor_sum_omitted": 0}
    slopes = {}
    for data in [a, b, cut]:
        assert data["source_sha256"] == digest(HERE/"certify.py")
        assert data["sieve_sha256"] == digest(ROOT/"evidence/v160/ns67/certify_cells.py")
        assert data["input_sha256"] == digest(ROOT/data["input"])
        assert data["reference_sha256"] == digest(ROOT/data["reference"])
        original = json.loads((ROOT/data["input"]).read_text())
        for row in data["rows"]:
            v = {k: arb(s) for k, s in row["values"].items()}
            assert all(row["gates"].values())
            assert v["complete_numerator"] > 0
            assert v["inherited_projected_cost"] > 0
            assert v["complete_numerator"].overlaps(v["inherited_numerator"])
            counts["archived_Gram_numerator_overlaps"] += 1
            assert v["triangle_lower_numerator"] < 0
            counts["negative_triangle_bounds"] += 1
            assert v["omit_divisor_forcing_numerator"] < 0
            counts["wrong_sign_if_finite_divisor_sum_omitted"] += 1
            source = next(r for r in original["rows"] if r["N"] == row["N"])
            u = 1-sum((arb(s) for s in source["optimal_coefficients"]), arb(0))/2
            assert not u.contains(0)
            slopes[str(row["N"])] = u.str(60)
    for left, right in zip(a["rows"], b["rows"]):
        assert left["N"] == right["N"]
        for key, value in left["values"].items():
            assert arb(value).overlaps(arb(right["values"][key])), key
            counts["precision_scalar_overlaps"] += 1
    last, doubled = b["rows"][-1]["values"], cut["rows"][0]["values"]
    for key in ["E_N", "log2_times_energy", "complete_compensator", "complete_numerator",
                "inherited_numerator", "inherited_projected_cost", "numerator_over_E_N",
                "compensator_over_E_N"]:
        assert arb(last[key]).overlaps(arb(doubled[key])), key
        counts["cutoff_complete_overlaps"] += 1
    assert arb(doubled["tail_radius"]) < arb(last["tail_radius"])
    assert arb(last["triangle_lower_over_E_N"]) < -186
    assert arb(doubled["triangle_lower_over_E_N"]) < -226
    assert arb(b["rows"][0]["values"]["triangle_lower_over_E_N"]) < -828
    maxima = (HERE/"exact-checks-output.txt").read_text()
    assert "PASS: 15 exact checks" in maxima and "#0:" not in maxima
    output = {"status": "PASS", "checks": counts, "Maxima_exact_checks": 15,
              "nonzero_actual_residual_tail_slopes": slopes,
              "cutoff_dependent_summands_not_compared_as_invariants": True,
              "cofinal_lower_gain_proved": False, "new_Gram_solves_performed": False,
              "source_sha256": digest(Path(__file__))}
    (HERE/"replay-validation.json").write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
