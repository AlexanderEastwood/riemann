"""Verify saved local cone-separator enclosures at two precisions."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def main() -> None:
    ctx.prec = 512
    directory = Path(__file__).resolve().parent
    source_hash = hashlib.sha256((directory/'certify_separator.py').read_bytes()).hexdigest()
    reports: list[dict[str, Any]] = [json.loads((directory/f'separator-{bits}bits.json').read_text())
                                    for bits in [256, 384]]
    for report, bits in zip(reports, [256, 384]):
        assert report['source_sha256'] == source_hash and report['precision_bits'] == bits
        assert report['positive_projection_support'] == [1, 2, 3, 4, 5]
        assert all(report['gates'].values()) and report['minimum_accuracy_bits'] >= 220
        value = arb(report['full_cone_distance_lower_bound'])
        assert value > arb('0.00228323766118601628')
        assert value < arb('0.00228323766118601629')
        assert all(arb(c) > 0 for c in report['projection_coefficients'][:5])
        assert arb(report['projection_coefficients'][5]).is_zero()
        assert all(arb(c).contains(0) for c in report['separator_pairings'][:5])
        assert arb(report['separator_pairings'][5]) > 0
        assert arb(report['local_cone_distance_squared']).overlaps(
            arb(report['single_coordinate_distance_squared_bound']))
    matches = 0
    for first, second in zip(reports[0]['gram'], reports[1]['gram']):
        for a, b in zip(first, second):
            assert arb(a).overlaps(arb(b))
            matches += 1
    for key in ['projection_coefficients', 'separator_coefficients', 'separator_pairings']:
        for a, b in zip(reports[0][key], reports[1][key]):
            assert arb(a).overlaps(arb(b))
            matches += 1
    for key in ['local_cone_distance_squared', 'full_cone_distance_lower_bound',
                'single_coordinate_distance_squared_bound']:
        assert arb(reports[0][key]).overlaps(arb(reports[1][key]))
        matches += 1
    print(json.dumps({'status': 'PASS', 'matching_ball_enclosures': matches,
                      'precision_bits': [256, 384],
                      'minimum_accuracy_bits': [r['minimum_accuracy_bits'] for r in reports],
                      'all_five_coefficient_signs_strict': True,
                      'local_equality_full_space_lower_bound_only': True,
                      'source_sha256': source_hash}, indent=2))


if __name__ == '__main__':
    main()
