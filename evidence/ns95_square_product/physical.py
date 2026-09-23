"""Independent complete physical-cell check of the optimized free lift."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEP = ROOT / "evidence/ns86_optimized_arithmetic"
sys.path.insert(0, str(DEP))
from certify_physical import evaluate, Kernel


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--stop", type=int, required=True)
    parser.add_argument("--sizes", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    data = json.loads(args.input.read_text())
    # evaluate(..., potential=False) never uses kernel entries. The object
    # satisfies its interface; the independent calculation uses only cells.
    kernel = Kernel(1, 128, 24)
    rows: list[dict[str, Any]] = []
    for row in data["rows"]:
        if row["N"] not in args.sizes:
            continue
        coefficients = [arb(v) for v in row["free_lift_complete_coefficients"]]
        physical = evaluate(coefficients, row["M"], args.stop, kernel, False)
        values = physical["values"]
        assert arb(values["complete_energy"]).overlaps(arb(row["values"]["free_lift_error"]))
        improvement = 1-arb(values["complete_energy"])/arb(row["values"]["E_N"])
        assert improvement > 0
        values["relative_improvement"] = improvement.str(65)
        rows.append({"N": row["N"], "values": values})
        print(json.dumps(rows[-1]), flush=True)
    assert [r["N"] for r in rows] == args.sizes
    dependencies = [DEP/"certify_physical.py", DEP/"certify_newton.py",
                    ROOT/"evidence/v159/ns61/certify_smoothed.py"]
    args.output.write_text(json.dumps({
        "classification": "independent full physical norms with analytic infinite tails",
        "precision_bits": args.bits, "cell_stop": args.stop,
        "source_sha256": digest(Path(__file__)), "input_file": args.input.name,
        "input_sha256": digest(args.input),
        "dependencies": {str(p.relative_to(ROOT)): digest(p) for p in dependencies},
        "rows": rows}, indent=2)+"\n")


if __name__ == "__main__":
    main()
