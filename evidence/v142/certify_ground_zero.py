#!/usr/bin/env python3
"""Complete lambda=4 local zero via an even spectral separator and energy.

All acceptance tests use Arb intervals. The complete v125/v126 residual
assemblies are inherited enclosures; only their small final gates are replayed.
No new window, finite eigensolve, residual assembly or midpoint solve is used.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from types import ModuleType
from typing import Any

from flint import acb, arb, ctx

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_prior() -> ModuleType:
    path = ROOT / 'evidence/v140/certify_ground4.py'
    spec = importlib.util.spec_from_file_location('archived_ground4', path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def transform_and_derivative(z: arb, coefficients: list[arb], length: arb) -> tuple[arb, arb]:
    """Nonunitary centered transform of UNshifted cosine coefficients.

    The (-1)^n centering phase cancels the same phase in the sine numerator.
    All queried intervals avoid zero and every removable lattice pole.
    """
    assert not z.contains(0)
    rational = coefficients[0] / z
    derivative = -coefficients[0] / (z*z)
    sqrt_two = arb(2).sqrt()
    for n, coefficient in enumerate(coefficients[1:], 1):
        omega = 2 * arb.pi() * n / length
        denominator = z*z - omega*omega
        assert not denominator.contains(0)
        rational += sqrt_two * coefficient * z / denominator
        derivative -= sqrt_two * coefficient * (z*z + omega*omega) / (denominator*denominator)
    phase = z * length / 2
    value = 2 * phase.sin() * rational / length.sqrt()
    slope = (length * phase.cos() * rational + 2 * phase.sin() * derivative) / length.sqrt()
    return value, slope


def run(bits: int) -> dict[str, Any]:
    assert bits in (1024, 1280)
    ctx.prec = bits
    prior = load_prior()
    data, matrices, trial, head, tail, provenance = prior.load_trial('even', bits)
    inherited_gate = prior.replay_prior_gates('even', data, matrices, bits)
    energy = prior.sym(matrices['K'])
    assert prior.inertia(energy)['negative'] == 0
    head_gram = head.transpose() * head
    tail_gram = tail.transpose() * tail
    norm_gram = head_gram + tail_gram
    delta, separator, kappa = arb('1.7940e-8'), arb('1e-67'), arb(62629)/100000
    assert 0 < separator < delta
    lower = prior.sym(kappa * energy - separator * (
        head_gram + 2 / (1 - separator / delta) * (tail_gram + energy / delta)
    ))
    gate = prior.inertia(lower)
    assert gate['status'] == 'CERTIFIED'
    assert gate['negative'] == 1 and gate['positive'] == 16
    column = 16
    norm_squared = norm_gram[column, column]
    rayleigh = energy[column, column] / norm_squared
    assert 0 < rayleigh < arb('2.454e-75') < separator
    coefficients = [trial[i, column] / norm_squared.sqrt() for i in range(trial.nrows())]
    assert len(coefficients) == 4097

    # Nonnegative complete operator + even spectral theorem:
    # h=P_ground f != 0 and ||f-h|| <= sqrt(q[f]/separator).
    length = 2 * arb(4).log()
    projection_error = (rayleigh / separator).sqrt()
    value_error = length.sqrt() * projection_error
    derivative_error = (length**3 / 12).sqrt() * projection_error
    assert value_error < arb('0.000260824')
    assert derivative_error < arb('0.000208757')
    gamma = acb.zeta_zero(1).imag
    radius = arb(1)/10
    left, right = gamma - radius, gamma + radius
    left_value, _ = transform_and_derivative(left, coefficients, length)
    right_value, _ = transform_and_derivative(right, coefficients, length)
    assert left_value + value_error < 0
    assert right_value - value_error > 0

    subintervals = []
    for j in range(8):
        lo = left + 2*radius*j/8
        hi = left + 2*radius*(j+1)/8
        interval = lo.union(hi)
        _, derivative = transform_and_derivative(interval, coefficients, length)
        ground_lower = derivative - derivative_error
        assert ground_lower > arb('0.0016')
        subintervals.append({
            'left': lo.str(100), 'right': hi.str(100),
            'trial_derivative': derivative.str(100, more=True),
            'projected_ground_derivative_lower': ground_lower.lower().str(100),
        })

    # Show the precise weakness of using the old global separator unchanged.
    baseline_error = (length * rayleigh / arb('1e-73')).sqrt()
    baseline_fails = bool(left_value + baseline_error > 0 and right_value - baseline_error < 0)
    assert baseline_fails
    ground_report = ROOT / f'evidence/v140/ground4_b{bits}_shift1e-73.json'
    assert json.loads(ground_report.read_text())['status'] == 'PASS_COMPLETE_SIMPLE_EVEN_GROUND'
    dependencies = [ROOT / provenance['ingredients'], ROOT / provenance['witness'],
                    ROOT / 'evidence/v140/certify_ground4.py', ground_report]
    dependencies += [ROOT / item['path'] for item in inherited_gate['dependencies']]
    return {
        'status': 'PASS_COMPLETE_GROUND_LOCAL_SIMPLE_ZERO',
        'precision_bits': bits, 'lambda': 4, 'head_last_mode': 16,
        'trial_last_mode': 4096, 'inherited_residual_row_cut': 65536,
        'scope': 'A unique simple local zero of the COMPLETE ground transform in '
                 '(gamma_1-1/10,gamma_1+1/10). No ordering of earlier zeros, '
                 'sign of discrepancy, high-accuracy CCM transfer, cofinal convergence, G2 or RH.',
        'new_computation': 'Shifted even Schur inertia, exact-trial ordinary norm, '
                           'spectral-energy projection bound, transform endpoint/derivative gates.',
        'inherited_inputs': 'Complete v125/v126 infinite-tail residual enclosures at '
                            '768/896 bits; their small even final gate is replayed. '
                            'v140 simple-even theorem is retained. No fresh full residual assembly.',
        'separator': '1e-67', 'ordinary_tail_floor': '1.7940e-8',
        'shifted_lower_inertia': gate, 'prior_complete_even_gate': inherited_gate,
        'trial_column_zero_based': column, 'trial_norm_squared': norm_squared.str(100),
        'trial_rayleigh': rayleigh.str(100),
        'projection_error_upper': projection_error.str(100),
        'nonunitary_transform_error_upper': value_error.str(100),
        'nonunitary_derivative_error_upper': derivative_error.str(100),
        'gamma_1': gamma.str(100), 'root_radius_exact': '1/10',
        'root_interval_description': '(gamma_1-1/10, gamma_1+1/10)',
        'left_endpoint': left.str(100), 'right_endpoint': right.str(100),
        'trial_left_value': left_value.str(100), 'trial_right_value': right_value.str(100),
        'projected_ground_left_upper': (left_value+value_error).upper().str(100),
        'projected_ground_right_lower': (right_value-value_error).lower().str(100),
        'derivative_subintervals': subintervals,
        'baseline_global_separator': '1e-73',
        'baseline_transform_error_upper': baseline_error.str(100),
        'baseline_sign_gate_fails': baseline_fails,
        'provenance': provenance,
        'dependencies': [{'path': str(path.relative_to(ROOT)), 'sha256': sha256(path)}
                         for path in dependencies],
        'verifier_sha256': sha256(Path(__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits', type=int, required=True, choices=(1024, 1280))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), 'Use a fresh output path to preserve prior evidence.'
    result = run(args.bits)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'], args.bits)
    for key in ('projection_error_upper', 'nonunitary_transform_error_upper',
                'projected_ground_left_upper', 'projected_ground_right_lower'):
        print(key, result[key])


if __name__ == '__main__':
    main()
