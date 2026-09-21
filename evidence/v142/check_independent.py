#!/usr/bin/env python3
"""Second implementation of inertia and the centered Fourier evaluation.

Uses leading principal determinants (not the signed LDL routine) and the
termwise sinc formula (not the partial-fraction formula). Same inherited
complete-tail inputs: this is an implementation check, not an external audit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from flint import acb, arb, arb_mat, ctx
import certify_ground_zero as certificate


def sinc_and_derivative(t: arb) -> tuple[arb, arb]:
    assert not t.contains(0)
    return t.sin()/t, (t*t.cos()-t.sin())/(t*t)


def direct_transform(z: arb, coefficients: list[arb], length: arb) -> tuple[arb, arb]:
    a = length/2
    value, derivative = sinc_and_derivative(a*z)
    value *= length.sqrt()*coefficients[0]
    derivative *= a*length.sqrt()*coefficients[0]
    for n, coefficient in enumerate(coefficients[1:], 1):
        omega = 2*arb.pi()*n/length
        vminus, dminus = sinc_and_derivative(a*(z-omega))
        vplus, dplus = sinc_and_derivative(a*(z+omega))
        factor = (length/2).sqrt()*((-1)**n)*coefficient
        value += factor*(vminus+vplus)
        derivative += a*factor*(dminus+dplus)
    return value, derivative


def run() -> dict[str, Any]:
    checks = []
    prior = certificate.load_prior()
    for bits in (1024, 1280):
        ctx.prec = bits
        data, matrices, trial, head, tail, provenance = prior.load_trial('even', bits)
        prior.replay_prior_gates('even', data, matrices, bits)
        energy = prior.sym(matrices['K'])
        hh, ht = head.transpose()*head, tail.transpose()*tail
        delta, separator = arb('1.7940e-8'), arb('1e-67')
        lower = prior.sym(arb(62629)/100000*energy - separator*(
            hh + 2/(1-separator/delta)*(ht+energy/delta)))
        determinant_signs = []
        previous_sign, negative = 1, 0
        for n in range(1, 18):
            determinant = arb_mat([[lower[i, j] for j in range(n)] for i in range(n)]).det()
            assert determinant > 0 or determinant < 0
            sign = 1 if determinant > 0 else -1
            negative += int(sign != previous_sign)
            previous_sign = sign
            determinant_signs.append(sign)
        assert negative == 1
        norm_squared = sum((trial[i, 16]*trial[i, 16] for i in range(trial.nrows())), arb(0))
        assert norm_squared.overlaps((hh+ht)[16, 16])
        rayleigh = energy[16, 16]/norm_squared
        assert 0 < rayleigh < separator
        coefficients = [trial[i, 16]/norm_squared.sqrt() for i in range(trial.nrows())]
        length = 2*arb(4).log()
        error = (length*rayleigh/separator).sqrt()
        derivative_error = (length**3*rayleigh/(12*separator)).sqrt()
        gamma = acb.zeta_zero(1).imag
        left, right = gamma-arb(1)/10, gamma+arb(1)/10
        left_value, _ = direct_transform(left, coefficients, length)
        right_value, _ = direct_transform(right, coefficients, length)
        assert left_value+error < 0 and right_value-error > 0
        comparisons = []
        for z in (left, gamma, right):
            direct, direct_derivative = direct_transform(z, coefficients, length)
            partial, partial_derivative = certificate.transform_and_derivative(z, coefficients, length)
            assert direct.overlaps(partial) and direct_derivative.overlaps(partial_derivative)
            comparisons.append({'point': z.str(60), 'value_overlap': True, 'derivative_overlap': True})
        slope_bounds = []
        for j in range(32):
            lo, hi = left+arb(j)/160, left+arb(j+1)/160
            _, slope = direct_transform(lo.union(hi), coefficients, length)
            margin = slope-derivative_error
            assert margin > 0
            slope_bounds.append(margin.lower().str(70))
        checks.append({
            'precision_bits': bits, 'principal_determinant_signs': determinant_signs,
            'negative_index': negative, 'trial_norm_independent_sum_overlaps': True,
            'termwise_left_upper': (left_value+error).upper().str(70),
            'termwise_right_lower': (right_value-error).lower().str(70),
            'formula_comparisons': comparisons,
            'termwise_derivative_32_lower_bounds': slope_bounds,
            'provenance': provenance,
        })
        print(bits, 'PASS determinant inertia and direct termwise zero gates', flush=True)

    # Reparse the delivered intervals, not just values held in memory.
    reports = [json.loads((certificate.BASE/f'ground_zero_b{b}.json').read_text()) for b in (1024, 1280)]
    keys = ['trial_norm_squared', 'trial_rayleigh', 'projection_error_upper',
            'nonunitary_transform_error_upper', 'nonunitary_derivative_error_upper',
            'gamma_1', 'trial_left_value', 'trial_right_value']
    for key in keys:
        assert arb(reports[0][key]).overlaps(arb(reports[1][key]))
    for report in reports:
        assert report['verifier_sha256'] == certificate.sha256(Path(certificate.__file__))
        assert arb(report['projected_ground_left_upper']) < 0
        assert arb(report['projected_ground_right_lower']) > 0
        for interval in report['derivative_subintervals']:
            assert arb(interval['trial_derivative']) - arb(report['nonunitary_derivative_error_upper']) > 0
            assert arb(interval['projected_ground_derivative_lower']) > arb('0.0016')
        for dependency in report['dependencies']:
            assert certificate.sha256(certificate.ROOT/dependency['path']) == dependency['sha256']
    return {
        'status': 'PASS_SECOND_IMPLEMENTATION_AND_SAVED_INTERVALS',
        'scope': 'Implementation cross-check by the same agent; no new external or independent-agent audit.',
        'checks': checks, 'cross_precision_overlapping_keys': keys,
        'serialized_intervals_retain_all_sign_gates': True,
        'all_dependency_hashes_match': True,
        'checker_sha256': certificate.sha256(Path(__file__)),
        'verifier_sha256': certificate.sha256(Path(certificate.__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), 'Use a fresh output path.'
    result = run()
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(result['status'])


if __name__ == '__main__':
    main()
