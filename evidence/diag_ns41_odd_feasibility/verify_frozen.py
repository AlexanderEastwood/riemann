"""DIAGNOSTIC, NOT A CERTIFICATE: direct-transform replay of frozen NS-41 vectors.

This replay does not assemble bin matrices or rerun optimization. It evaluates
the saved decimal vector's odd transform directly, uses scipy's digamma rather
than the proposal helper's asymptotic expansion, and prints all twenty slacks.
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
from typing import Any

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS', '1')
import numpy as np
from scipy.special import digamma

OUT = Path(__file__).resolve().parent


def prime_powers(lam: int) -> list[tuple[int, int]]:
    """Return m=p^k<lambda^2 without using the archived assembly helper."""
    pairs: list[tuple[int, int]] = []
    for p in range(2, lam * lam):
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            continue
        power = p
        while power < lam * lam:
            pairs.append((power, p))
            power *= p
    return sorted(pairs)


def beta_direct(lam: int, xs: Any) -> Any:
    """Correct shifted-digamma symbol with strict prime-power endpoint."""
    length = 2 * math.log(lam)
    value = np.real(digamma(1.25 + .5j * xs)) - math.log(math.pi)
    for m, p in prime_powers(lam):
        value -= 2 * math.log(p) / math.sqrt(m) * np.cos(xs * math.log(m))
    z = .5 + 1j * xs
    value += 2 * np.real(np.expm1(z * length) / z)
    return value


def replay(payload: dict[str, Any], refinement: int, improved: dict[str, Any] | None = None) -> dict[str, Any]:
    """Two-sided transform mass by direct sample sums, no M_b product."""
    lam = payload['lambda']
    length = 2 * math.log(lam)
    decimal = payload['pure_search']['best']['vector_decimal'] if improved is None else improved['vector_decimal']
    vector = np.array([float(x) for x in decimal])
    vector /= np.linalg.norm(vector)
    xs0 = np.concatenate([np.arange(.001, 40., .002), np.arange(40.005, 800., .005)])
    hs0 = np.where(xs0 < 40, .002, .005)
    offsets = (np.arange(refinement) + .5) / refinement - .5
    xs = (xs0[:, None] + hs0[:, None] * offsets).ravel()
    hs = np.repeat(hs0 / refinement, refinement)
    edges = np.array(payload['edges'])
    masses = np.zeros(20)
    required = np.zeros(20)
    indices = np.arange(1, 257)
    omega = 2 * math.pi * indices / length
    coefficients = vector * (-1.) ** indices * math.sqrt(2 / length) / math.sqrt(2 * math.pi)
    for first in range(0, len(xs), 4096):
        sample, weight = xs[first:first+4096], hs[first:first+4096]
        minus = omega[:, None] - sample[None, :]
        plus = omega[:, None] + sample[None, :]
        # None of the prescribed grid centers is an exact pole. The stable
        # sinc fallback handles a removable zero if a future replay hits one.
        left = np.divide(np.sin(minus * length / 2), minus,
                         out=np.full_like(minus, length / 2), where=minus != 0)
        right = np.divide(np.sin(plus * length / 2), plus,
                          out=np.full_like(plus, length / 2), where=plus != 0)
        transform = coefficients @ (left - right)
        beta = beta_direct(lam, sample)
        bin_index = np.searchsorted(edges, beta, side='right') - 1
        bin_index = np.maximum(bin_index, 0)  # deepest bin extends downward
        for b in range(20):
            selected = (beta < 0) & (bin_index == b)
            masses[b] += float(np.sum(2 * weight[selected] * transform[selected] ** 2))
            required[b] += float(weight[selected].sum()) / 800
    slacks = masses - required
    saved = (payload['pure_search']['best']['screen'] if refinement == 1 else payload['pure_grid2']) if improved is None else improved['screens'][refinement - 1]
    return {'lambda': lam, 'refinement': refinement, 'witness': 'interior' if improved is None else 'improved', 'required': required.tolist(),
            'masses': masses.tolist(), 'slacks': slacks.tolist(), 'ratios': (masses / required).tolist(),
            'min_ratio': float(min(masses / required)), 'min_slack': float(min(slacks)),
            'all_slacks_positive': bool(np.all(slacks > 0)),
            'maximum_mass_difference_from_matrix_screen': float(max(abs(masses - saved['masses']))),
            'maximum_reference_difference': float(max(abs(required - saved['required'])))}


def main() -> None:
    rows = []
    for lam in (3, 4, 6, 8):
        payload = json.loads((OUT / f'lambda{lam}.json').read_text())
        candidates: list[dict[str, Any] | None] = [None]
        improved_path = OUT / f'lambda{lam}-improved.json'
        if improved_path.exists():
            candidates.append(json.loads(improved_path.read_text()))
        for candidate in candidates:
            for refinement in (1, 2):
                row = replay(payload, refinement, candidate)
                rows.append(row)
                print('FROZEN DIRECT REPLAY', lam, row['witness'], refinement, 'min_ratio', row['min_ratio'],
                      'mass matrix difference', row['maximum_mass_difference_from_matrix_screen'], flush=True)
                print('bin required mass slack ratio', flush=True)
                for i, values in enumerate(zip(row['required'], row['masses'], row['slacks'], row['ratios'])):
                    print(i, *(f'{v:.17g}' for v in values), flush=True)
    (OUT / 'frozen-replay.json').write_text(json.dumps({'status': 'DIAGNOSTIC, NOT A CERTIFICATE',
        'arithmetic': 'numpy/scipy float64, direct transform sample sums; not an enclosure', 'checks': rows}, indent=2) + '\n')


if __name__ == '__main__':
    main()
