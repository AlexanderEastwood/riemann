"""Replay exact dyadic obstructions to three structured lower-bound candidates.

This checks K - V from the saved interval ingredients. It does NOT certify
a negative direction for the true Weil form or its true Schur complement.
The parent assembly scripts reproduce the interval ingredients themselves.
Requires python-flint. No eigensolver or floating arithmetic enters a gate.
"""
import argparse
import hashlib
import json
from pathlib import Path

from flint import arb, arb_mat, ctx


def replay(path, bits):
    witness = json.loads(path.read_text())
    ingredients_path = path.parent / witness["ingredients"]
    raw = ingredients_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == witness["ingredients_sha256"]
    matrices = json.loads(raw)["matrices"]
    exponent = int(witness["denominator_exponent"])
    coefficients = [arb(int(x)) * arb(2) ** (-exponent)
                    for x in witness["numerators"]]
    assert all(x.is_exact() for x in coefficients)
    vector = arb_mat([[x] for x in coefficients])
    K = arb_mat([[arb(x) for x in row] for row in matrices["K"]])
    V = arb_mat([[arb(x) for x in row] for row in matrices["V"]])
    assert K.nrows() == K.ncols() == V.nrows() == V.ncols() == len(coefficients)
    norm = (vector.transpose() * vector)[0, 0]
    K_energy = (vector.transpose() * K * vector)[0, 0]
    V_energy = (vector.transpose() * V * vector)[0, 0]
    ceiling_energy = K_energy - V_energy
    assert norm > 0
    assert ceiling_energy < 0
    return {
        "status": "PASS_STRICT_NEGATIVE_CEILING",
        "outer_support_cut": witness["M"],
        "bits": bits,
        "ingredients_sha256": witness["ingredients_sha256"],
        "norm_squared": norm.str(40),
        "K_energy": K_energy.str(65),
        "V_energy": V_energy.str(65),
        "K_minus_V": ceiling_energy.str(65),
        "scope": "Obstruction to this fixed lower-bound certificate only; not a negative Weil direction.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, default=768)
    parser.add_argument("witness", nargs="*")
    args = parser.parse_args()
    ctx.prec = args.bits
    base = Path(__file__).resolve().parent
    names = args.witness or [
        "structured_ceiling_counterwitness.json",
        "structured_ceiling_counterwitness_M512.json",
        "structured_ceiling_counterwitness_M1024.json",
    ]
    paths = [Path(name) if Path(name).is_absolute() else base / name for name in names]
    print(json.dumps([replay(path, args.bits) for path in paths], indent=2))


if __name__ == "__main__":
    main()
