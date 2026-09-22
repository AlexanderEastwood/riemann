#!/usr/bin/env python3
"""Numerical illustration: deep NS-22 samples and explicit zero-prefix counts.

Counts are sufficient for this specified Gaussian/desmoothed evaluation at
these samples, not universal counts for the sharp conditionally convergent sum.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import mpmath as mp
from flint import acb, ctx

from verify_identity import ROOT, US, dec, gaussian_parts, make_beta_true, prime_powers

OUT = Path(__file__).resolve().parent
COMB = ROOT / 'evidence/diag_comb_minorant/comb_minorant_l3_4_6_8.json'
REFERENCE = 1200
EPSILON = '.025'
TAIL_TOL = '2e-7'


def sample_points() -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for lam in (3, 4, 6, 8):
        for u in US:
            result.append({'lambda': lam, 'kind': 'low_lattice', 'u_input': u})
    records = json.loads(COMB.read_text())
    for record in records:
        lam = record['lambda']
        if lam not in (4, 8):
            continue
        for rank, (depth, xi) in enumerate(record['lobes'][:5], 1):
            result.append({'lambda': lam, 'kind': 'archived_grid_trough',
                           'trough_rank': rank, 'xi_input': str(xi),
                           'archived_depth': str(depth)})
        for row in record['D1']:
            if row[0] in (8, 16):
                result.append({'lambda': lam, 'kind': 'binding_centroid',
                               'J_levels_in_diagnostic': row[0], 'xi_input': str(row[4])})
    return result


def paired_term(gamma: Any, xi: Any, length: Any, eps: Any) -> Any:
    def term(y: Any) -> Any:
        return (mp.sin(length * y) / y if y else length) * mp.exp(-eps * eps * y * y / 2)
    return 2 * (term(gamma + xi) + term(xi - gamma))


def run(bits: int, dps: int) -> dict[str, Any]:
    ctx.prec = bits
    balls = acb.zeta_zeros(1, REFERENCE + 1)
    height = (balls[-2].imag + balls[-1].imag) / 2
    count = height.zeta_nzeros()
    assert count == REFERENCE
    assert all(z.real == 0.5 for z in balls)
    mp.mp.dps = dps
    gammas = [mp.mpf(z.imag.mid().str(dps + 5, radius=False)) for z in balls[:-1]]
    powers = prime_powers(256)
    eps = mp.mpf(EPSILON)
    rows: list[dict[str, Any]] = []
    for sample in sample_points():
        lam = sample['lambda']
        length = 2 * mp.log(lam)
        if 'u_input' in sample:
            xi = 2 * mp.pi * mp.mpf(sample['u_input']) / length
        else:
            xi = mp.mpf(sample['xi_input'])
        u = xi * length / (2 * mp.pi)
        # Empty zero list obtains independently computed pole, trivial and
        # desmoothing terms. The zero series is accumulated by ordinate below.
        parts = gaussian_parts(lam, mp.nstr(u, dps), eps, [], powers)
        base = parts['sum_without_left_contour']
        terms = [paired_term(g, xi, length, eps) for g in gammas]
        partials = [mp.mpf(0)]
        for term in terms:
            partials.append(partials[-1] + term)
        tail_abs = [mp.mpf(0)] * (REFERENCE + 1)
        for index in range(REFERENCE - 1, -1, -1):
            tail_abs[index] = tail_abs[index + 1] + abs(terms[index])
        sufficient = next(n for n in range(REFERENCE + 1) if tail_abs[n] < mp.mpf(TAIL_TOL))
        beta, _ = make_beta_true(lam)
        direct = beta(xi)
        full_error = abs(base + partials[-1] - direct)
        count_error = abs(base + partials[sufficient] - direct)
        assert full_error < mp.mpf('1e-6') and count_error < mp.mpf('1e-6')
        archived_error = (abs(direct + mp.mpf(sample['archived_depth']))
                          if 'archived_depth' in sample else None)
        if archived_error is not None:
            assert archived_error < mp.mpf('1e-6')
        sharp400 = 2 * mp.fsum(mp.sin((g + xi) * length) / (g + xi)
                               + mp.sin((g - xi) * length) / (g - xi) for g in gammas[:400])
        sharp_trivial = -2 * mp.re(mp.fsum(mp.exp((-2 * n - mp.mpf('.5') + 1j * xi) * length)
                                     / (2 * n + mp.mpf('.5') - 1j * xi) for n in range(1, 60)))
        endpoint = parts['endpoint']
        row = {**sample, 'xi': dec(xi), 'u': dec(u), 'direct_beta': dec(direct),
               'reference_zero_sum': dec(partials[-1]),
               'reference_total': dec(base + partials[-1]), 'reference_error': dec(full_error),
               'zero_count_sufficient': sufficient,
               'positive_zero_height_sufficient': dec(gammas[sufficient - 1]),
               'finite_absolute_remainder_to_1200': dec(tail_abs[sufficient]),
               'error_at_sufficient_count': dec(count_error),
               '1000_to_1200_difference': dec(abs(partials[1000] - partials[1200])),
               'gaussian_400_error': dec(abs(base + partials[400] - direct)),
               'sharp_400_error_with_endpoint_and_trivial': dec(abs(sharp400 + sharp_trivial + endpoint - direct)),
               'reconstructed_full_sharp_zero_contribution': dec(direct - endpoint - sharp_trivial),
               'trivial_sharp': dec(sharp_trivial),
               'archived_grid_value_error': dec(archived_error) if archived_error is not None else None,
               'parts_excluding_zeros': {key: dec(value) for key, value in parts.items() if key not in ('zeros', 'xi')}}
        rows.append(row)
    counts: list[dict[str, Any]] = []
    for lam in (3, 4, 6, 8):
        for kind in ('low_lattice', 'deep_and_centroids'):
            selected = [r for r in rows if r['lambda'] == lam and
                        (r['kind'] == 'low_lattice' if kind == 'low_lattice' else r['kind'] != 'low_lattice')]
            if not selected:
                continue
            counts.append({'lambda': lam, 'sample_group': kind, 'sample_count': len(selected),
                           'sufficient_positive_zero_count': max(r['zero_count_sufficient'] for r in selected),
                           'max_reference_error': dec(max(mp.mpf(r['reference_error']) for r in selected)),
                           'max_error_at_pointwise_sufficient_counts': dec(max(mp.mpf(r['error_at_sufficient_count']) for r in selected))})
    return {'classification': 'NUMERICAL ILLUSTRATION ONLY, NOT AN INTERVAL CERTIFICATE',
            'bits_zero_input': bits, 'mpmath_dps': dps, 'epsilon': EPSILON,
            'summation': 'Gaussian Perron residues exp(epsilon^2 (rho-s)^2 / 2), ordinate order, conjugate pairs; exact desmoothing back to n<x',
            'positive_zeros_in_reference': REFERENCE, 'N_at_reference_height': count.str(10),
            'reference_height': height.str(40),
            'count_rule': 'first prefix with sum of absolute omitted real paired contributions through 1200 < 2e-7; empirical sufficient count, not a sharp-sum or interval tail certificate',
            'cutoff_stability': 'compare 1000 and 1200 positive zeros',
            'archived_source_sha256': hashlib.sha256(COMB.read_bytes()).hexdigest(),
            'counts_by_window': counts, 'rows': rows}


def main() -> None:
    for bits, dps in ((192, 45), (256, 65)):
        result = run(bits, dps)
        path = OUT / f'deep_b{bits}.json'
        path.write_text(json.dumps(result, indent=2) + '\n')
        print(path.name, json.dumps(result['counts_by_window']), flush=True)


if __name__ == '__main__':
    main()
