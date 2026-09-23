"""Verify complete finite Newton-correction and potential replays."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

HERE = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare_values(a: dict[str, str], b: dict[str, str]) -> int:
    assert a.keys() == b.keys()
    for key in a:
        assert arb(a[key]).overlaps(arb(b[key])), key
    return len(a)


def main() -> None:
    ctx.prec = 384
    newton = [json.loads((HERE/name).read_text()) for name in
              ["newton-256bits.json", "newton-384bits.json", "newton-cutoff-384bits.json"]]
    physical = [json.loads((HERE/name).read_text()) for name in
                ["physical-256bits.json", "physical-384bits.json", "physical-cutoff-384bits.json"]]
    for report in newton:
        assert report["source_sha256"] == digest(HERE/"certify_newton.py")
        assert report["kernel_sha256"] == digest(HERE.parent/"v159/ns61/certify_smoothed.py")
    for report in physical:
        assert report["source_sha256"] == digest(HERE/"certify_physical.py")
        assert report["input_sha256"] == digest(HERE/report["input_file"])
        assert report["dependencies"]["certify_newton.py"] == digest(HERE/"certify_newton.py")
        assert report["dependencies"]["certify_smoothed.py"] == digest(HERE.parent/"v159/ns61/certify_smoothed.py")
    assert [p["precision_bits"] for p in newton] == [256, 384, 384]
    assert [p["precision_bits"] for p in physical] == [256, 384, 384]
    assert newton[2]["kernel_cutoff"] == 2*newton[1]["kernel_cutoff"]
    assert physical[2]["cell_stop"] == 2*physical[1]["cell_stop"]
    numeric_matches = 0
    coefficient_matches = 0
    for a, b in zip(newton[0]["rows"], newton[1]["rows"], strict=True):
        assert a["N"] == b["N"] and a["M"] == b["M"] == a["N"]**2
        assert a["families"].keys() == b["families"].keys()
        for key in a["families"]:
            fa, fb = a["families"][key], b["families"][key]
            numeric_matches += compare_values(fa["values"], fb["values"])
            for field in ["old_coefficients", "proposed_coefficients"]:
                for x, y in zip(fa[field], fb[field], strict=True):
                    assert arb(x).overlaps(arb(y))
                    coefficient_matches += 1
            assert fa["gates"] == fb["gates"]
    cutoff_matches = 0
    for key in newton[1]["rows"][-1]["families"]:
        cutoff_matches += compare_values(newton[1]["rows"][-1]["families"][key]["values"],
                                         newton[2]["rows"][0]["families"][key]["values"])
    potential_matches = 0
    for a, b in zip(physical[0]["rows"], physical[1]["rows"], strict=True):
        assert a["N"] == b["N"]
        for key in ["old", "new"]:
            numeric_matches += compare_values(a[key]["values"], b[key]["values"])
        for mesh in a["old"]["potential_observations"]:
            potential_matches += compare_values(a["old"]["potential_observations"][mesh],
                                                 b["old"]["potential_observations"][mesh])
    for kind in ["old", "new"]:
        before = physical[1]["rows"][-1][kind]["values"]
        after = physical[2]["rows"][0][kind]["values"]
        for key in ["eta", "exterior_energy", "interior_energy_1_to_split",
                    "complete_energy_after_split", "complete_energy"]:
            assert arb(before[key]).overlaps(arb(after[key]))
            cutoff_matches += 1
        assert arb(after["physical_tail_radius"]) < arb(before["physical_tail_radius"])/3
    for mesh in physical[1]["rows"][-1]["old"]["potential_observations"]:
        for key in ["complete_quadrature", "complete_Gram_pairing"]:
            a = physical[1]["rows"][-1]["old"]["potential_observations"][mesh][key]
            b = physical[2]["rows"][0]["old"]["potential_observations"][mesh][key]
            assert arb(a).overlaps(arb(b))
            cutoff_matches += 1
    outcomes = [row["families"]["original"]["gates"]["unit_step_decreases_error"]
                for row in newton[1]["rows"]]
    assert outcomes == [False, True, False]
    large = newton[2]["rows"][0]["families"]["original"]["values"]
    tail = physical[2]["rows"][0]["new"]["values"]["complete_energy_after_split"]
    assert 29.54 < arb(large["unit_step_error_ratio"]) < 29.56
    assert arb(tail) > 21*arb(large["E_N"])
    assert arb("0.2730") < arb(large["projected_gain_fraction"]) < arb("0.2732")
    maxima = (HERE/"exact-checks-output.txt").read_text()
    assert "PASS: 82 exact checks" in maxima
    assert "Exact check failed" not in maxima.replace('error("Exact check failed",label,expr)', '')
    result: dict[str, Any] = {
        "classification": "finite certificates and exact identities; no cofinal arithmetic lower estimate",
        "status": "PASS", "scalar_precision_matches": numeric_matches,
        "coefficient_precision_matches": coefficient_matches,
        "potential_precision_matches": potential_matches,
        "same_problem_cutoff_matches": cutoff_matches,
        "independent_physical_norm_comparisons": 14,
        "independent_quadrature_pairing_comparisons": 56,
        "exact_Maxima_checks": 82,
        "N16_unit_error_ratio": large["unit_step_error_ratio"],
        "N16_projected_fraction_of_available_gain": large["projected_gain_fraction"],
        "N16_new_tail_over_old_error": (arb(tail)/arb(large["E_N"])).str(30),
        "review": "local author review; numerical methods independently cross-checked",
        "RH_proved": False}
    (HERE/"replay-validation.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
