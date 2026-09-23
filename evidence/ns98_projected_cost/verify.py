"""Verify finite NS98 replay overlaps and prior-cost agreement."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(name: str) -> dict[str, Any]:
    return json.loads((HERE/name).read_text())


def main() -> None:
    ctx.prec = 512
    low = read("cost-256bits.json")
    high = read("cost-384bits.json")
    cutoff = read("cost-cutoff-384bits.json")
    prior = json.loads((ROOT/"evidence/v161/ns73/mobius-384bits.json").read_text())
    prior_rows = {row["N"]: row for row in prior["rows"]}
    source_hash = hashlib.sha256((HERE/"certify_cost.py").read_bytes()).hexdigest()
    kernel_hash = hashlib.sha256((ROOT/"evidence/v159/ns61/certify_smoothed.py").read_bytes()).hexdigest()
    precision_checks = cutoff_checks = prior_checks = 0
    for report in [low, high, cutoff]:
        assert report["source_sha256"] == source_hash
        assert report["kernel_sha256"] == kernel_hash
        for row in report["rows"]:
            assert all(row["gates"].values())
            assert row["minimum_accuracy_bits"] >= 90
            assert row["off_diagonal_sign"] == "negative"
    for left, right, replay in zip(low["rows"], high["rows"], cutoff["rows"], strict=True):
        assert left["N"] == right["N"] == replay["N"]
        for key, value in left["values"].items():
            assert arb(value).overlaps(arb(right["values"][key]))
            precision_checks += 1
            assert arb(right["values"][key]).overlaps(arb(replay["values"][key]))
            cutoff_checks += 1
        previous = prior_rows[left["N"]]["directions"]["linear_log_taper"]["true_projected_cost"]
        assert arb(right["values"]["projected_cost"]).overlaps(arb(previous))
        prior_checks += 1
    print(json.dumps({"classification": "Finite replay validation, not a cofinal estimate",
                      "precision_overlaps": precision_checks, "cutoff_overlaps": cutoff_checks,
                      "NS73_cost_overlaps": prior_checks, "source_bindings": 2}, indent=2))


if __name__ == "__main__":
    main()
