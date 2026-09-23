"""Verify all precision/cutoff enclosures and overlap with published NS71."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def fields(row: dict[str, Any]) -> dict[str, str]:
    result = dict(row['quantities'])
    for name, values in row['directions'].items():
        result.update({f'{name}.{key}': value for key, value in values.items()})
    return result


def matches(left: dict[str, str], right: dict[str, str]) -> int:
    assert set(left) == set(right)
    for key, value in left.items():
        a, b = arb(value), arb(right[key])
        assert a.is_finite() and b.is_finite() and a.overlaps(b), (key, a, b)
    return len(left)


def main() -> None:
    ctx.prec = 512
    folder = Path(__file__).resolve().parent
    hashes = {
        'source_sha256': folder/'certify_curvature.py',
        'kernel_source_sha256': folder.parents[1]/'v159/ns61/certify_smoothed.py',
        'projection_source_sha256': folder.parents[1]/'v160/ns71/certify_preconditioner.py',
    }
    reports = [json.loads((folder/f'curvature-{bits}bits.json').read_text()) for bits in [256, 384]]
    cutoff = json.loads((folder/'curvature-cutoff-replay-384bits.json').read_text())
    for report, bits, limit, sizes in zip(reports+[cutoff], [256, 384, 384], [128, 128, 256],
                                         [[16,32,64,128,256], [16,32,64,128,256], [256]]):
        assert report['precision_bits'] == bits and report['finite_series_cutoff'] == limit
        assert report['bernoulli_order'] == 24 and [r['N'] for r in report['rows']] == sizes
        for key, path in hashes.items():
            assert report[key] == hashlib.sha256(path.read_bytes()).hexdigest()
        for row in report['rows']:
            assert all(row['gates'].values())
            q = {k: arb(v) for k, v in row['quantities'].items()}
            assert q['energy'] > 0 and q['A'] > 0 and q['B'] > 0
            assert 2*q['local_curvature_sum'] < q['bending_energy'] < 6*q['local_curvature_sum']
            assert q['bending_energy']/(4*q['B']) < q['model_numerator'] < 84*q['bending_energy']/q['A']
            fractions = {k: arb(v['fraction_of_full_gain']) for k, v in row['directions'].items()}
            assert all(0 < x < 1 for x in fractions.values())
            assert fractions['diagonal_curvature'] > fractions['spline_curvature'] > fractions['repaired_model']
            for item in row['directions'].values():
                assert arb(item['relative_gain']) > arb(item['raw_lower_relative_gain']) > 0
    precision = sum(matches(fields(a), fields(b)) for a, b in zip(reports[0]['rows'], reports[1]['rows']))
    cutoff_count = matches(fields(reports[1]['rows'][-1]), fields(cutoff['rows'][0]))
    previous = json.loads((folder.parents[1]/'v160/ns71/preconditioner-384bits.json').read_text())
    inherited = 0
    for a, b in zip(reports[1]['rows'], previous['rows']):
        assert a['N'] == b['N']
        old = b['directions']['projected_repaired_inverse']
        new = a['directions']['repaired_model']
        inherited += matches(
            {'energy': a['quantities']['energy'], 'full': a['quantities']['full_relative_gain'],
             'numerator': new['numerator'], 'cost': new['true_projected_cost'], 'fraction': new['fraction_of_full_gain']},
            {'energy': b['energy'], 'full': b['full_relative_gain'],
             'numerator': old['numerator'], 'cost': old['denominator'], 'fraction': old['fraction_of_full_gain']})
    bounds = [('.9308','.9310'),('.9040','.9041'),('.9783','.9785'),('.9852','.9854'),('.9763','.9764')]
    for row, (lo, hi) in zip(reports[1]['rows'], bounds):
        assert arb(lo) < arb(row['directions']['diagonal_curvature']['fraction_of_full_gain']) < arb(hi)
    result = {'status':'PASS', 'precision_enclosure_matches':precision, 'doubled_cutoff_matches':cutoff_count,
              'published_NS71_overlap_matches':inherited,
              'minimum_accuracy_bits':min(r['minimum_accuracy_bits'] for p in reports for r in p['rows']),
              'finite_prediction':'both curvature directions outperform the repaired model at each tested size; diagonal best',
              'cofinal_arithmetic_bound':False}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
