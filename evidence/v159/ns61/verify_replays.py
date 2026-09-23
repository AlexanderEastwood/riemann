"""Check saved interval outputs, finite gates, and the independent tail replay."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def main() -> None:
    ctx.prec = 512
    directory = Path(__file__).resolve().parent
    source_hash = hashlib.sha256((directory/'certify_smoothed.py').read_bytes()).hexdigest()
    names = ['smoothed-64-256bits.json', 'smoothed-64-384bits.json',
             'smoothed-64-cutoff256-256bits.json']
    reports: list[dict[str, Any]] = [json.loads((directory/name).read_text()) for name in names]
    for report, bits, cutoff in zip(reports, [256, 384, 256], [128, 128, 256]):
        assert report['precision_bits'] == bits
        assert report['max_index'] == 64
        assert report['finite_series_cutoff'] == cutoff
        assert report['bernoulli_remainder_order'] == 24
        assert report['source_sha256'] == source_hash
        assert [row['N'] for row in report['rows']] == [2, 4, 8, 16, 32]
    overlap_count = 0
    for other in reports[1:]:
        for first, second in zip(reports[0]['rows'], other['rows']):
            assert first['gates'] == second['gates']
            assert all(first['gates'].values())
            assert first['quantities'].keys() == second['quantities'].keys()
            for key, value in first['quantities'].items():
                assert arb(value).overlaps(arb(second['quantities'][key])), (first['N'], key)
                overlap_count += 1
    for report in reports:
        for row in report['rows']:
            assert row['minimum_accuracy_bits'] >= 90
            assert arb(row['gain_identity_difference']).contains(0)
            if row['N'] in [16, 32]:
                assert arb(row['quantities']['budget_fraction_of_gain']) < arb(1)/50
                assert arb(row['quantities']['endpoint_error_budget_over_leading_norm']) > 2000
            ranges = {
                16: {'gain_relative': ('0.23728', '0.23729'),
                     'budget_relative': ('0.0032933', '0.0032935')},
                32: {'gain_relative': ('0.18912', '0.18914'),
                     'budget_relative': ('0.0035663', '0.0035665')},
            }
            for key, (lower, upper) in ranges.get(row['N'], {}).items():
                assert arb(row['quantities'][key]) > arb(lower)
                assert arb(row['quantities'][key]) < arb(upper)
    physical_reports: list[dict[str, Any]] = []
    for bits in [256, 384]:
        physical = json.loads((directory/f'physical-gram-{bits}bits.json').read_text())
        physical_reports.append(physical)
        assert physical['precision_bits'] == bits and len(physical['rows']) == 7
        assert all(row['strict_tail_gate'] and row['all_finite_cell_integrals_positive']
                   for row in physical['rows'])
    physical_overlap_count = 0
    for first, second in zip(physical_reports[0]['rows'], physical_reports[1]['rows']):
        assert (first['m'], first['n'], first['cutoff']) == (second['m'], second['n'], second['cutoff'])
        for key in ['physical_enclosure', 'gram_formula', 'tail_error_bound']:
            assert arb(first[key]).overlaps(arb(second[key]))
            physical_overlap_count += 1
    print(json.dumps({'status': 'PASS',
                      'physical_precision_enclosure_comparisons': physical_overlap_count, 'matching_ball_enclosures': overlap_count,
                      'precision_replay_bits': [256, 384], 'same_matrix_dimension': 64,
                      'independent_tail_cutoffs': [128, 256], 'tail_order': 24,
                      'minimum_accuracy_bits': [min(row['minimum_accuracy_bits']
                                                    for row in report['rows']) for report in reports],
                      'physical_cell_checks_per_precision': 7,
                      'source_sha256': source_hash}, indent=2))


if __name__ == '__main__':
    main()
