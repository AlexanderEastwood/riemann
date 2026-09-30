"""Diagnostic for exact two-prime boundary ordering, not a Weil certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from types import ModuleType
from typing import Any

import mpmath as mp

BASE = "ccebc6524cf8adf5e83143ad00daa55b190737bd"
ROOT = Path(__file__).resolve().parents[2]


def number(value: Any) -> str:
    return str(mp.nstr(value, 35))


def outside_overlap(left: Any, right: Any, half_width: Any, window: Any) -> Any:
    """Normalized intersection length outside (-window,window)."""
    lo = max(left - half_width, right - half_width)
    hi = min(left + half_width, right + half_width)
    if hi <= lo:
        return mp.mpf(0)
    inside = max(mp.mpf(0), min(hi, window) - max(lo, -window))
    return (hi - lo - inside) / (2 * half_width)


def rayleigh(matrix: Any, values: list[int]) -> Any:
    vector = mp.matrix(values)
    return (vector.T * matrix * vector)[0] / (vector.T * vector)[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.dps
    source = subprocess.check_output(
        ["git", "show", f"{BASE}:controls/davenport_heilbronn.py"], cwd=ROOT
    )
    control = ModuleType("pinned_control")
    exec(compile(source, "pinned_control.py", "exec"), control.__dict__)
    dh = control.screen(
        lambda function, kernel: None,
        "One-sided boundary ordering for exact Euler denominators",
        sample_domain="Every window and pair of distinct primes; screen p=2,q=3",
        applicability="Literal original Euler-denominator operators are not hypotheses supplied by this completed-function control.",
        applicable=False,
    )
    ell_p, ell_q = mp.log(2), mp.log(3)
    radius_p, radius_q = 1 / mp.sqrt(2), 1 / mp.sqrt(3)
    window, half_width = mp.mpf(2), mp.mpf(1) / 100
    x = mp.mpf(3) / 2
    y = x + ell_q - ell_p
    centers = [x, y, -x, -y]
    mixed = mp.matrix(4)
    paths = []
    for i, ci in enumerate(centers):
        for j, cj in enumerate(centers):
            value = mp.mpf(0)
            for sp in (-1, 1):
                for sq in (-1, 1):
                    overlap = outside_overlap(ci + sp * ell_p, cj + sq * ell_q, half_width, window)
                    value += radius_p * radius_q * overlap
                    if overlap > mp.mpf("1e-30"):
                        paths.append({"i": i, "j": j, "p_sign": sp, "q_sign": sq, "overlap": number(overlap)})
            mixed[i, j] = value
    defect = (mixed + mixed.T) / 2
    directions = {"even_same_sign": [1, 1, 1, 1],
                  "even_opposite_sign": [1, -1, 1, -1],
                  "odd_same_sign": [1, 1, -1, -1],
                  "odd_opposite_sign": [1, -1, -1, 1]}
    energies = {name: number(rayleigh(defect, vector)) for name, vector in directions.items()}
    result = {
        "classification": "Diagnostic, not an interval certificate or complete Weil computation",
        "reviewed_commit": BASE, "dps": args.dps,
        "control_sha256": hashlib.sha256(source).hexdigest(), "Davenport_Heilbronn": dh,
        "NS100_NS101": "not-applicable: exact Euler-denominator hypotheses absent",
        "NS57": "not used: finite coefficient alteration loses the exact identities being retained",
        "p": 2, "q": 3, "window_half_width": "2", "packet_half_width": "1/100",
        "packet_centers": [number(v) for v in centers], "nonzero_exterior_paths": paths,
        "mixed_matrix": [[number(mixed[i, j]) for j in range(4)] for i in range(4)],
        "symmetric_defect": [[number(defect[i, j]) for j in range(4)] for i in range(4)],
        "rayleigh_values": energies,
        "predicted_absolute_value": number(1 / (2 * mp.sqrt(6))),
        "both_orderings_fail_diagnostically": bool(mp.mpf(energies["even_same_sign"]) > 0 and mp.mpf(energies["even_opposite_sign"]) < 0),
        "scope": "The boundary defect alone is tested. No claim about indefiniteness of the compressed product, the complete Weil form, or API."
    }
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"dps": args.dps, "rayleigh_values": energies, "output": str(args.output)}))


if __name__ == "__main__":
    main()
