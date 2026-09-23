"""Numerical illustration only: floating point canonical cancellation scan."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys
import time
from typing import Any

import numpy as np
from scipy.special import gammaln

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'v160' / 'ns67'))
from certify_cells import mobius_sieve, sigma_one_norm
from flint import ctx


def moments(h: np.ndarray, power: int) -> np.ndarray:
    value, term = np.zeros_like(h), h ** (power + 1)
    factorial = 1
    for k in range(12):
        if k:
            factorial *= k
        value += ((-1) ** k) * term / (factorial * (k + power + 1))
        term *= h
    return value


def scan(n: int, factor: int) -> dict[str, Any]:
    started = time.monotonic()
    cutoff = n * factor
    mu = mobius_sieve(n)
    beta = n * math.fsum(mu[k] / k for k in range(1, n + 1))
    coeff = np.array(mu[1:], dtype=float)
    coeff[-1] -= beta
    indices = np.arange(1, n + 1, dtype=float)
    leading_a = 1 + (sum(mu[1:]) - beta) / 2
    leading_b = float(np.dot(coeff, np.log(2 * np.pi / indices)) / 2)
    mass = float(np.dot(indices, np.abs(coeff)))
    divisor = np.zeros(cutoff + 1, dtype=np.int32)
    for k in range(1, n + 1):
        if mu[k]:
            divisor[k::k] += mu[k]
    cumulative = np.cumsum(divisor, dtype=np.int64)
    carry = np.longdouble(0)
    finite = np.longdouble(0)
    sigma_cross = np.longdouble(0)
    tau_cross = np.longdouble(0)
    checkpoint_energies = []
    boundaries = sorted(set([n] + [n * 2**k for k in range(1, factor.bit_length())
                                       if n * 2**k < cutoff] + [cutoff]))
    for low, high in zip(boundaries, boundaries[1:]):
        for start in range(low, high, 131072):
            end = min(high, start + 131072)
            j = np.arange(start, end, dtype=np.float64)
            floor = np.arange(start, end, dtype=np.int64) // n
            slope = 1 - cumulative[start:end] + beta * floor
            h = np.log1p(1 / j)
            increments = slope * h
            values = np.cumsum(increments, dtype=np.longdouble)
            values += carry
            carry = values[-1]
            values -= increments
            value = values.astype(np.float64)
            i0, i1, i2 = 1 / (j + 1), moments(h, 1), moments(h, 2)
            cells = (value * value * i0 + 2 * value * slope * i1 + slope * slope * i2) / j
            finite += np.sum(cells, dtype=np.longdouble)
            logj = np.log(j)
            sigma = j / n - floor * np.log(j / n) + gammaln(floor + 1)
            sig_cells = (value * sigma * i0 + (slope * sigma - value * floor) * i1
                         - slope * floor * i2 + (j / n) *
                         (value * (h - i0) + slope * (h*h/2 - i1))) / j
            sigma_cross += np.sum(sig_cells, dtype=np.longdouble)
            tau_cross += np.sum((value * logj * i0 + (value + slope * logj) * i1
                                 + slope * i2) / j, dtype=np.longdouble)
        checkpoint_energies.append({'T': high, 'energy': float(finite)})
    t = float(cutoff)
    v = leading_a * math.log(t) + leading_b
    model2 = (v*v + 2*leading_a*v + 2*leading_a**2) / t
    remainder = mass / (6 * math.sqrt(3*t**3))
    tail_error = 2*math.sqrt(model2)*remainder + remainder**2
    sigma_v = math.log(2*math.pi*t/n) / 2
    sigma_cross += (v*sigma_v + v/2 + leading_a*sigma_v + leading_a) / t
    tau_cross += (v*math.log(t) + v + leading_a*math.log(t) + 2*leading_a) / t
    total = float(finite) + model2
    w = beta - sum(mu[1:])
    # Fixed complete Gram value is a diagnostic midpoint, never a certificate.
    sigma_norm2 = float(sigma_one_norm().mid())
    boundary2 = w*w*sigma_norm2/n
    together2 = total + 2*w*float(sigma_cross) + boundary2
    return {'N': n, 'T': cutoff, 'seconds': round(time.monotonic()-started, 3),
            'full_energy_center': total, 'analytic_tail_error_allowance': tail_error,
            'finite_energy': float(finite), 'tail_model_energy': model2,
            'boundary_energy': boundary2, 'target_plus_integral_energy': together2,
            'triangle_ratio': (math.sqrt(max(together2, 0)) + math.sqrt(boundary2))/math.sqrt(total),
            'N_eta': w, 'scaled_eta': w/math.sqrt(n), 'leading_a': leading_a,
            'leading_b': leading_b, 'coefficient_mass': mass,
            'cross_sigma': float(sigma_cross), 'cross_tau': float(tau_cross),
            'checkpoint_energies': checkpoint_energies}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--sizes', type=int, nargs='+', required=True)
    parser.add_argument('--factor', type=int, default=256)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 128
    rows = []
    for n in args.sizes:
        row = scan(n, args.factor)
        rows.append(row)
        print(json.dumps({key: row[key] for key in ['N','seconds','full_energy_center',
                          'analytic_tail_error_allowance','triangle_ratio']}), flush=True)
    args.output.write_text(json.dumps({'classification': 'numerical illustration only, not a certificate',
                                      'rows': rows},indent=2)+'\n')


if __name__ == '__main__':
    main()
