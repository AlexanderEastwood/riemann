"""Verify NS91 finite replays and their source bindings."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name: str) -> dict[str, Any]:
    return json.loads((HERE/name).read_text())


def main() -> None:
    ctx.prec = 384
    counts = {"precision_values": 0, "precision_grouped_integrals": 0,
              "common_integrals_across_cutoffs": 0, "complete_cutoff_overlaps": 0,
              "finite_positive_numerator_cases": 0}
    for prefix in ["check", "endpoint"]:
        a, b, cut = [read(f"{prefix}-{suffix}.json") for suffix in
                     ["256bits", "384bits", "cutoff-384bits"]]
        for dataset in [a, b, cut]:
            assert dataset["source_sha256"] == digest(HERE/"check_grouping.py")
            assert dataset["input_sha256"] == digest(ROOT/dataset["input_path"])
            assert dataset["reference_sha256"] == digest(ROOT/dataset["reference_path"])
            for row in dataset["rows"]:
                assert all(row["checks"].values())
                assert arb(row["values"]["positive_lower_numerator"]) > 0
                assert arb(row["values"]["inherited_full_projected_cost"]) > 0
                assert arb(row["values"]["guaranteed_relative_gain"]) > 0
                counts["finite_positive_numerator_cases"] += 1
                if dataset["endpoint_normalized"]:
                    for scale, value in row["signed_dyadic_integrals_over_E"].items():
                        if 2**int(scale) < row["N"]:
                            assert value == "0"
        for left, right in zip(a["rows"], b["rows"]):
            assert left["N"] == right["N"]
            for field in ["values", "signed_dyadic_integrals_over_E"]:
                for key, value in left[field].items():
                    assert arb(value).overlaps(arb(right[field][key])), (prefix, field, key)
                    counts["precision_values" if field == "values" else "precision_grouped_integrals"] += 1
        left, right = b["rows"][-1], cut["rows"][0]
        assert left["N"] == right["N"] == 256
        for key in ["E_N", "alpha_E_N", "old_endpoint_shift", "complete_compensator_enclosure",
                    "complete_numerator_enclosure", "inherited_numerator", "inherited_full_projected_cost"]:
            assert arb(left["values"][key]).overlaps(arb(right["values"][key])), key
            counts["complete_cutoff_overlaps"] += 1
        for key, value in left["signed_dyadic_integrals_over_E"].items():
            assert arb(value).overlaps(arb(right["signed_dyadic_integrals_over_E"][key])), key
            counts["common_integrals_across_cutoffs"] += 1
        assert arb(right["values"]["absolute_all_dyadic_tail_bound"]) < arb(left["values"]["absolute_all_dyadic_tail_bound"])
    rows = read("endpoint-384bits.json")["rows"]
    for row, threshold in zip(rows, ["0.1793", "0.2634", "0.1867"]):
        assert arb(row["values"]["positive_lower_numerator_over_E"]) > arb(threshold)
    assert arb(rows[-1]["values"]["guaranteed_relative_gain"]) > arb("0.02821")
    assert arb(read("endpoint-cutoff-384bits.json")["rows"][0]["values"]["guaranteed_relative_gain"]) > arb("0.02822")
    assert arb(read("check-384bits.json")["rows"][-1]["values"]["guaranteed_relative_gain"]) > arb("0.00792")
    text = (HERE/"exact-checks-output.txt").read_text()
    assert "PASS: 32 exact checks" in text and "#0:" not in text
    output = {"status": "PASS", "scope": "Finite arithmetic certificates and scalar exact sanity checks; no cofinal gain proof",
              "checks": counts, "Maxima_exact_checks": 32,
              "N256_guaranteed_relative_gain_above": "0.02821",
              "new_Gram_solves": False, "independent_author_review": False,
              "source_sha256": digest(Path(__file__))}
    (HERE/"validation.json").write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
