"""Check paired trial diagnostics and their source bindings; no new theorem."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare(left: Any, right: Any, location: str = "root") -> int:
    """Compare every common serialized Arb enclosure, skipping provenance."""
    if isinstance(left, dict) and isinstance(right, dict):
        return sum(compare(left[key], right[key], f"{location}.{key}")
                   for key in left.keys() & right.keys()
                   if key not in {"provenance", "dependencies"})
    if isinstance(left, list) and isinstance(right, list):
        assert len(left) == len(right), location
        return sum(compare(a, b, f"{location}[{i}]")
                   for i, (a, b) in enumerate(zip(left, right)))
    if isinstance(left, str) and left.startswith("[") and "+/-" in left:
        assert arb(left).overlaps(arb(right)), location
        return 1
    return 0


def validate() -> dict[str, Any]:
    ctx.prec = 1400
    reports = [json.loads((HERE / f"trial-{bits}bits.json").read_text())
               for bits in (1024, 1280)]
    for report in reports:
        assert report["script_sha256"] == sha(HERE / "evaluate_trial.py")
        assert report["finite_trial_modes"] == 4097
        for dependency in report["dependencies"]:
            assert sha(ROOT / dependency["path"]) == dependency["sha256"]
        provenance = report["provenance"]
        assert sha(ROOT / provenance["witness"]) == provenance["witness_sha256"]
        assert sha(ROOT / provenance["ingredients"]) == provenance["ingredient_sha256"]
        assert [row["j"] for row in report["rows"]] == list(range(1, 65))
        for row in report["rows"]:
            left, right = arb(row["left_value"]), arb(row["right_value"])
            assert (left < 0 and right > 0) or (left > 0 and right < 0)
            assert row["endpoint_sign_change"]
            assert not arb(row["trial_derivative"]).contains(0)
            assert not arb(row["trial_value"]).contains(0)
    assert reports[0]["provenance"]["witness_sha256"] == reports[1]["provenance"]["witness_sha256"]
    overlap_count = compare(*reports)
    rho = arb(reports[1]["trial_rayleigh"])
    length = 2 * arb(4).log()
    norm_error = (rho / arb("1e-67")).sqrt()
    derivative_error = (length ** 3 / 12).sqrt() * norm_error
    first = reports[1]["rows"][0]
    scale_ratio = arb(first["sqrt_rho_over_abs_trial_slope"]) / abs(arb(first["linearized_trial_shift"]))
    report = {
        "classification": "DIAGNOSTIC consistency and provenance checks, not a historical certificate replay",
        "paired_arb_fields_overlapping": overlap_count,
        "both_reports": {"64_sign_changes": True, "64_values_exclude_zero": True,
                         "64_slopes_exclude_zero": True, "all_dependency_hashes_match": True},
        "same_exact_witness": True,
        "inherited_ingredient_precisions": [r["provenance"]["ingredient_precision_bits"] for r in reports],
        "ordinary_projection_error": norm_error.str(40),
        "ordinary_transform_error": (length.sqrt() * norm_error).str(40),
        "ordinary_derivative_error": derivative_error.str(40),
        "derivative_allowance_exceeds_gamma2_slope": bool(derivative_error > abs(arb(reports[1]["rows"][1]["trial_derivative"]))),
        "first_sqrt_rho_scale_divided_by_linearized_shift": scale_ratio.str(40),
        "scope": "No omitted-zero tail, unique-root enclosure or new complete-ground transfer. Saved intervals agree; this does not validate every historical computation.",
    }
    return report


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2))
