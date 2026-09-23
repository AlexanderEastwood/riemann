"""Check the two interval replays of the finite one-atom control."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def main() -> None:
    ctx.prec = 512
    directory = Path(__file__).resolve().parent
    source_hash = hashlib.sha256((directory/'certify_one_atom.py').read_bytes()).hexdigest()
    reports: list[dict[str, Any]] = [json.loads((directory/f'one-atom-{bits}bits.json').read_text())
                                    for bits in [256, 384]]
    matches = 0
    keys = ['relative_squared_error', 'absolute_squared_error',
            'leading_relative_asymptotic', 'relative_tail_bound']
    for report, bits in zip(reports, [256, 384]):
        assert report['precision_bits'] == bits
        assert report['source_sha256'] == source_hash
        assert [row['order'] for row in report['rows']] == [4, 16, 64]
        for row in report['rows']:
            assert all(row['gates'].values()) and row['relative_accuracy_bits'] >= 30
            if row['order'] == 64:
                value = arb(row['relative_squared_error'])
                assert value > arb('0.0138756') and value < arb('0.0138757')
                assert arb(row['absolute_squared_error']) > arb(10)**35
    for a, b in zip(reports[0]['rows'], reports[1]['rows']):
        for key in keys:
            assert arb(a[key]).overlaps(arb(b[key])), (a['order'], key)
            matches += 1
    anchors = [json.loads((directory/f'q2-anchor-{bits}bits.json').read_text())
               for bits in [256, 384]]
    for anchor, bits in zip(anchors, [256, 384]):
        assert anchor['precision_bits'] == bits and anchor['strict_containment_gate']
        assert anchor['independent_quadrature']['order'] == 1
        assert anchor['independent_quadrature']['cutoff'] == 64
        reference = arb(anchor['q2_gram_value'])
        assert reference > arb('0.45312316') and reference < arb('0.45312317')
        assert arb(anchor['independent_quadrature']['relative_squared_error']).contains(reference)
    assert arb(anchors[0]['q2_gram_value']).overlaps(arb(anchors[1]['q2_gram_value']))
    print(json.dumps({'status': 'PASS', 'matching_ball_enclosures': matches,
                      'independent_q2_anchor_checks': 2,
                      'q2_anchor_is_coarse_full_tail_normalization_check': True,
                      'precision_bits': [256, 384], 'orders': [4, 16, 64],
                      'one_atom_index': 1, 'full_analytic_tail_included': True,
                      'source_sha256': source_hash}, indent=2))


if __name__ == '__main__':
    main()
