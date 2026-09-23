"""Numerical illustration only: projected NB block gain budgets, not a certificate."""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import cho_factor, cho_solve, eigh

Array = NDArray[np.float64]


def build_float(max_index: int) -> tuple[Array, Array]:
    """Replay the archived Vasyunin formula with vectorized finite sums."""
    values: list[Array] = [np.zeros(1), np.zeros(1)]
    for denominator in range(2, max_index + 1):
        integers = np.arange(1, denominator, dtype=np.int64)
        cotangents = 1.0 / np.tan(np.pi * integers / denominator)
        residues = (integers[:, None] * integers[None, :]) % denominator
        row = np.zeros(denominator)
        row[1:] = (residues / denominator) @ cotangents
        values.append(row)
    kappa = math.log(2 * math.pi) - float(np.euler_gamma)
    gram = np.empty((max_index, max_index))
    for m in range(1, max_index + 1):
        for n in range(m, max_index + 1):
            divisor = math.gcd(m, n)
            h, k = m // divisor, n // divisor
            v = values[k][h % k] + values[h][k % h]
            value = (
                kappa / 2 * (1 / m + 1 / n)
                + (n - m) / (2 * m * n) * math.log(m / n)
                - math.pi * divisor / (2 * m * n) * v
            )
            gram[m - 1, n - 1] = value
            gram[n - 1, m - 1] = value
    indices = np.arange(1, max_index + 1, dtype=np.float64)
    loads = (np.log(indices) + 1 - np.euler_gamma) / indices
    return gram, loads


def quotient(h: Array, schur: Array, direction: Array) -> float:
    denominator = float(direction @ schur @ direction)
    return float(direction @ h) ** 2 / denominator


def inspect_block(gram: Array, loads: Array, size: int) -> dict[str, Any]:
    old, cross, new = gram[:size, :size], gram[:size, size:2*size], gram[size:2*size, size:2*size]
    factor = cho_factor(old, lower=True)
    coeff = cho_solve(factor, loads[:size])
    h = loads[size:2*size] - cross.T @ coeff
    schur = new - cross.T @ cho_solve(factor, cross)
    schur = (schur + schur.T) / 2
    values, vectors = eigh(schur)
    if float(values[0]) <= 0:
        raise ArithmeticError(f"Unresolved positive definiteness in floating scan at N={size}")
    energy = 1 - float(loads[:size] @ coeff)
    exact_direction = cho_solve(cho_factor(schur, lower=True), h)
    gain = float(h @ exact_direction)
    weights = (vectors.T @ h) ** 2
    raw_trace = float(np.trace(new))
    residual_trace = float(np.trace(schur))
    norm_h2 = float(h @ h)
    full_coeff = cho_solve(cho_factor(gram[:2*size, :2*size], lower=True), loads[:2*size])
    next_energy = 1 - float(loads[:2*size] @ full_coeff)
    diagonal_direction = h / np.diag(schur)
    difference_map = np.eye(size)
    for j in range(1, size):
        n = size + j + 1
        difference_map[j-1, j] = -(n-1)/n
    differences = difference_map.T @ h
    difference_schur = difference_map.T @ schur @ difference_map
    harmonic = np.cumsum(1/np.arange(1, 2*size, dtype=np.float64))
    difference_budget = float(sum(harmonic[n-2]/n**2 for n in range(size+1, 2*size+1)))
    difference_trace = float(np.trace(difference_schur))
    difference_norm2 = float(differences @ differences)
    return {
        "N": size, "M": 2*size, "E_N": energy, "E_M": next_energy,
        "gain": gain, "gain_relative": gain/energy,
        "gain_vs_separate_solve_error": gain-(energy-next_energy),
        "h_norm2": norm_h2, "raw_trace": raw_trace, "residual_trace": residual_trace,
        "schur_min": float(values[0]), "schur_max": float(values[-1]),
        "raw_trace_gain_relative": norm_h2/raw_trace/energy,
        "residual_trace_gain_relative": norm_h2/residual_trace/energy,
        "spectral_norm_gain_relative": norm_h2/float(values[-1])/energy,
        "h_direction_gain_relative": quotient(h, schur, h)/energy,
        "diagonal_direction_gain_relative": quotient(h, schur, diagonal_direction)/energy,
        "difference_budget": difference_budget,
        "difference_projected_trace": difference_trace,
        "difference_budget_relative": difference_norm2/difference_budget/energy,
        "difference_trace_relative": difference_norm2/difference_trace/energy,
        "difference_direction_relative": quotient(differences, difference_schur, differences)/energy,
        "difference_gain_identity_error": quotient(h, schur, exact_direction)-float(differences @ cho_solve(cho_factor(difference_schur, lower=True), differences)),
        "smallest_quarter_gain_share": float(np.sum(weights[:max(1,size//4)]/values[:max(1,size//4)]))/gain,
        "largest_quarter_gain_share": float(np.sum(weights[-max(1,size//4):]/values[-max(1,size//4):]))/gain,
        "j_times_raw_trace_relative": math.log2(size)*norm_h2/raw_trace/energy,
        "h": h.tolist(), "schur_diagonal": np.diag(schur).tolist(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-index", type=int, default=512)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    gram, loads = build_float(args.max_index)
    rows: list[dict[str, Any]] = []
    size = 4
    while 2*size <= args.max_index:
        row = inspect_block(gram, loads, size)
        rows.append(row)
        print({key: row[key] for key in ["N", "E_N", "gain_relative", "raw_trace_gain_relative", "residual_trace_gain_relative", "h_direction_gain_relative", "diagonal_direction_gain_relative"]}, flush=True)
        size *= 2
    result = {"classification": "numerical illustration, not a certificate", "max_index":args.max_index,
              "elapsed_seconds":time.monotonic()-start,"rows":rows}
    args.output.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
