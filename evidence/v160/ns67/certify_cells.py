"""Complete canonical q=2 norm from signed physical cells and analytic tails.

All numbers used as evidence are Arb balls. The elementary tail proof and
all mixed terms are in proof.tex. No midpoint quadrature or solve occurs.
"""
from __future__ import annotations

import argparse
from array import array
from fractions import Fraction
import hashlib
import json
import time
from pathlib import Path
from typing import Any

from flint import arb, ctx


def mobius_sieve(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    mu[0] = 0
    primes = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if not primes[p]:
            continue
        for k in range(p, limit + 1, p):
            primes[k] = False
            mu[k] *= -1
        square = p * p
        for k in range(square, limit + 1, square):
            mu[k] = 0
    return mu


def rational(value: Fraction) -> arb:
    return arb(value.numerator) / value.denominator


def coefficients(size: int, mu: list[int]) -> tuple[Fraction, list[Fraction]]:
    beta = size * sum((Fraction(mu[n], n) for n in range(1, size + 1)), Fraction())
    coeff = [Fraction(v) for v in mu[:size + 1]]
    coeff[size] -= beta
    assert sum((coeff[n] / n for n in range(1, size + 1)), Fraction()) == 0
    return beta, coeff


def truncated_divisors(size: int, cutoff: int, mu: list[int]) -> array:
    values = array('i', [0]) * (cutoff + 1)
    for n in range(1, size + 1):
        if mu[n]:
            for k in range(n, cutoff + 1, n):
                values[k] += mu[n]
    return values


def display(value: arb) -> str:
    return value.str(70)


def complete_tail(size: int, cutoff: int, coeff: list[Fraction]) -> dict[str, arb]:
    log2pi = (2 * arb.pi()).log()
    leading_a = 1 + rational(sum(coeff[1:], Fraction())) / 2
    leading_b = sum((rational(coeff[n]) * (log2pi - arb(n).log()) / 2
                     for n in range(1, size + 1)), arb(0))
    mass = sum((n * abs(coeff[n]) for n in range(1, size + 1)), Fraction())
    t = arb(cutoff)
    logt = t.log()
    endpoint = leading_a * logt + leading_b
    model2 = (endpoint * endpoint + 2 * leading_a * endpoint + 2 * leading_a * leading_a) / t
    # |A(z)-log(2*pi*z)/2| <= 1/(6*z), z >= 1.
    remainder_norm = rational(mass) / (6 * (3 * t * t * t).sqrt())
    sigma_endpoint = (log2pi + logt - arb(size).log()) / 2
    sigma_model2 = (sigma_endpoint * sigma_endpoint + sigma_endpoint + arb(1) / 2) / t
    sigma_remainder_norm = arb(size) / (6 * (3 * t * t * t).sqrt())
    tau_tail2 = (logt * logt + 2 * logt + 2) / t
    cross_sigma = (endpoint * sigma_endpoint + endpoint / 2
                   + leading_a * sigma_endpoint + leading_a) / t
    cross_tau = (endpoint * logt + endpoint + leading_a * logt + 2 * leading_a) / t
    energy_error = 2 * model2.sqrt() * remainder_norm + remainder_norm * remainder_norm
    sigma_error = (model2.sqrt() * sigma_remainder_norm
                   + sigma_model2.sqrt() * remainder_norm
                   + remainder_norm * sigma_remainder_norm)
    tau_error = tau_tail2.sqrt() * remainder_norm
    return {
        'leading_a': leading_a, 'leading_b': leading_b,
        'coefficient_mass': rational(mass),
        'model_energy': model2, 'remainder_norm_bound': remainder_norm,
        'energy_error_bound': energy_error,
        'energy': model2 + arb(0, energy_error),
        'cross_sigma': cross_sigma + arb(0, sigma_error),
        'cross_tau': cross_tau + arb(0, tau_error),
    }


def cell_moments(j: int) -> tuple[arb, arb, arb, arb]:
    h = (arb(j + 1) / j).log()
    decay = arb(j) / (j + 1)
    i0 = arb(1) / (j + 1)
    i1 = 1 - (1 + h) * decay
    i2 = 2 - (h * h + 2 * h + 2) * decay
    return h, i0, i1, i2


def certify(size: int, cutoff: int) -> dict[str, Any]:
    assert size >= 1 and cutoff > size
    started = time.monotonic()
    mu = mobius_sieve(size)
    beta_exact, coeff = coefficients(size, mu)
    beta = rational(beta_exact)
    divisors = truncated_divisors(size, cutoff, mu)
    # sum_{j<=N} sum_{n|j,n<=N} mu(n) = 1, including N=1.
    running_divisors = sum(divisors[1:size + 1])
    assert running_divisors == 1
    value = arb(0)
    energy, cross_sigma, cross_tau = arb(0), arb(0), arb(0)
    logn = arb(size).log()
    factorial_logs = [arb(0)]
    for k in range(1, cutoff // size + 1):
        factorial_logs.append(factorial_logs[-1] + arb(k).log())
    physical_spot_checks = []
    requested_spots = {size, size + 1, 2 * size, 3 * size, cutoff - 1}
    checkpoints = []
    next_checkpoint = 2 * size
    for j in range(size, cutoff):
        slope = 1 - running_divisors + beta * (j // size)
        h, i0, i1, i2 = cell_moments(j)
        cell = (value * value * i0 + 2 * value * slope * i1 + slope * slope * i2) / j
        energy += cell
        logj = arb(j).log()
        k = j // size
        sigma_at_j = arb(j) / size - k * (logj - logn) + factorial_logs[k]
        cross_sigma += (value * sigma_at_j * i0
                        + (slope * sigma_at_j - value * k) * i1
                        - slope * k * i2
                        + (arb(j) / size) * (value * (h - i0)
                                            + slope * (h * h / 2 - i1))) / j
        cross_tau += (value * logj * i0 + (value + slope * logj) * i1 + slope * i2) / j
        if j in requested_spots:
            direct = logj
            for n in range(1, size + 1):
                if not coeff[n]:
                    continue
                z, kn = arb(j) / n, j // n
                acell = z - kn * z.log() + arb(kn + 1).lgamma()
                direct += rational(coeff[n]) * acell
            assert (direct - value).contains(0), (size, j, direct, value)
            physical_spot_checks.append(j)
        value += slope * h
        running_divisors += divisors[j + 1]
        if j + 1 == next_checkpoint:
            checkpoints.append({'cutoff': j + 1, 'partial_energy': display(energy)})
            next_checkpoint *= 2
    tail = complete_tail(size, cutoff, coeff)
    full_energy = energy + tail['energy']
    full_sigma = cross_sigma + tail['cross_sigma']
    full_tau = cross_tau + tail['cross_tau']
    assert full_energy > 0
    eta_n = beta - sum(mu[1:])  # N*eta_N, the Abel boundary amplitude.
    # sigma_1 norm is an independent complete physical integral plus tail.
    # It is enclosed separately below, and is not inferred from this error.
    sigma_norm2 = sigma_one_norm()
    boundary2 = eta_n * eta_n * sigma_norm2 / size
    target_plus_integral2 = full_energy + 2 * eta_n * full_sigma + boundary2
    integral2 = target_plus_integral2 + 2 - 2 * (full_tau + eta_n * target_load(size))
    triangle_ratio = (target_plus_integral2.sqrt() + boundary2.sqrt()) / full_energy.sqrt()
    k_target = laguerre_target(size)
    centered_amplitude = eta_n - k_target
    centered_boundary2 = centered_amplitude * centered_amplitude * sigma_norm2 / size
    centered_together2 = full_energy + 2 * centered_amplitude * full_sigma + centered_boundary2
    centered_ratio = (centered_together2.sqrt() + centered_boundary2.sqrt()) / full_energy.sqrt()
    conditioning_constant = 1 + 2 * sigma_norm2.sqrt()
    witness2 = centered_amplitude * centered_amplitude / size
    assert full_energy > witness2
    assert centered_ratio < conditioning_constant
    fields = {
        'finite_energy': energy, 'full_energy': full_energy,
        'cross_sigma': full_sigma, 'cross_tau': full_tau,
        'boundary_energy': boundary2,
        'target_plus_integral_energy': target_plus_integral2,
        'integral_energy': integral2,
        'whole_term_triangle_ratio': triangle_ratio,
        'scaled_eta': eta_n / arb(size).sqrt(),
        'cutoff_value': value,
        'laguerre_target': k_target,
        'centered_boundary_energy': centered_boundary2,
        'centered_target_plus_integral_energy': centered_together2,
        'centered_triangle_ratio': centered_ratio,
        'conditioning_constant': conditioning_constant,
        'localized_witness_squared': witness2,
    }
    assert all(v.is_finite() for v in fields.values())
    return {
        'N': size, 'cutoff': cutoff, 'cells': cutoff - size,
        'seconds': round(time.monotonic() - started, 3),
        'physical_spot_checks': physical_spot_checks,
        'exact_tail_coefficient_cancellation': True,
        'gates': {'full_energy_positive': True, 'full_energy_above_localized_witness': True,
                  'centered_ratio_below_uniform_constant': True, 'all_fields_finite': True},
        'balls': {key: display(v) for key, v in fields.items()},
        'tail': {key: display(v) for key, v in tail.items()},
        'checkpoints': checkpoints,
    }


def laguerre_target(n: int) -> arb:
    """Complete k_(N,1) Taylor series with the alternating tail retained."""
    frequency2 = (2 * arb.pi() / n) ** 2
    total, term = arb(0), arb(2)
    for j in range(64):
        total += term if j % 2 == 0 else -term
        term = term * frequency2 * (2*j+1)**2 / ((2*j+2) * (2*j+3)**3)
    assert frequency2 / (130 * 131) < 1
    return total + arb(0, term)


def target_load(n: int) -> arb:
    from flint import acb
    v, gamma, gamma1 = arb(n).log(), arb.const_euler(), acb.stieltjes(1).real
    return (v * v / 2 + (2 - gamma) * v + 3 - 2 * gamma - gamma1) / n


def sigma_one_norm() -> arb:
    # Imported complete Bernoulli/Hurwitz formula, independently validated in v159.
    import sys
    previous = Path(__file__).resolve().parents[2] / 'v159' / 'ns61'
    sys.path.insert(0, str(previous))
    from certify_smoothed import Kernel
    return Kernel(1, 128, 24).gram(1, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, required=True)
    parser.add_argument('--sizes', type=int, nargs='+', required=True)
    parser.add_argument('--factor', type=int, default=0,
                        help='Use factor*N; zero uses max(N*N, 64*N).')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    rows = []
    for size in args.sizes:
        cutoff = args.factor * size if args.factor else max(size * size, 64 * size)
        row = certify(size, cutoff)
        rows.append(row)
        print(json.dumps({'N': size, 'bits': args.bits, 'seconds': row['seconds'],
                          'full_energy': row['balls']['full_energy'],
                          'triangle_ratio': row['balls']['whole_term_triangle_ratio']}), flush=True)
    result = {
        'classification': 'certified finite full-domain norms, not an asymptotic bound',
        'precision_bits': args.bits,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'inherited_kernel_sha256': hashlib.sha256(
            Path(__file__).resolve().parents[2].joinpath('v159/ns61/certify_smoothed.py').read_bytes()).hexdigest(),
        'rows': rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
