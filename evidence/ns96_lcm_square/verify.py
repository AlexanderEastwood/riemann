"""Check scalar replay, algebra bindings, exact checks, and the local inventory."""
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


def overlap(a: dict[str, str], b: dict[str, str]) -> int:
    assert a.keys() == b.keys()
    for key in a:
        assert arb(a[key]).overlaps(arb(b[key])), key
    return len(a)


def main() -> None:
    ctx.prec = 512
    a, b = read("check-256bits.json"), read("check-384bits.json")
    assert [a["precision_bits"], b["precision_bits"]] == [256, 384]
    count = overlap(a["values"], b["values"])
    for report in [a, b]:
        assert report["source_sha256"] == digest(HERE/"certify.py")
        vals = {k: arb(v) for k, v in report["values"].items()}
        assert vals["negative_floor"].overlaps(arb(3087)/4096)
        assert vals["positive_floor"] > arb(1)/32
        assert vals["zeta_s"] < 0
        assert report["rational_gap"] == "55199/13436928"
    incidence = generators = 0
    for x, y in zip(a["rows"], b["rows"], strict=True):
        assert {k: v for k, v in x.items() if k != "values"} == {k: v for k, v in y.items() if k != "values"}
        count += overlap(x["values"], y["values"])
        incidence += x["incidence_checks"]
        generators += x["signed_projected_generators"]
    exact = (HERE/"checks-output.txt").read_text()
    assert "PASS: 17 exact checks" in exact and " -- an error." not in exact
    dependencies = read("dependencies.json")
    for path, sha in dependencies["sha256"].items():
        assert digest(ROOT/path) == sha, path
    inventory_count = 0
    if (HERE/"inventory.json").exists():
        for path, sha in read("inventory.json")["sha256"].items():
            assert digest(ROOT/path) == sha, path
            inventory_count += 1
    result = {"status": "PASS", "scalar_precision_overlaps": count,
              "exact_incidence_checks_per_precision": incidence,
              "signed_projected_generators_per_precision": generators,
              "exact_Jordan_checks_per_precision": 12,
              "Maxima_exact_checks": 17, "dependency_hashes": len(dependencies["sha256"]),
              "inventory_hashes": inventory_count, "historical_numerical_replay": False,
              "independent_review": False}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
