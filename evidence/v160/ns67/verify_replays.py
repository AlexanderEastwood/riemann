"""Check two precisions, independent Gram values, and doubled physical cutoffs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def compare(first: dict[str, Any], second: dict[str, Any], keys: list[str]) -> int:
    count = 0
    for key in keys:
        assert arb(first[key]).overlaps(arb(second[key])), (key, first[key], second[key])
        count += 1
    return count


def main() -> None:
    ctx.prec = 512
    directory = Path(__file__).resolve().parent
    source_hash = hashlib.sha256((directory/'certify_cells.py').read_bytes()).hexdigest()
    gram_hash = hashlib.sha256((directory/'check_gram.py').read_bytes()).hexdigest()
    kernel_hash = hashlib.sha256(directory.parents[1].joinpath('v159/ns61/certify_smoothed.py').read_bytes()).hexdigest()
    reports = [json.loads((directory/f'cells-{bits}bits.json').read_text()) for bits in [256,384]]
    for bits, report in zip([256,384],reports):
        assert report['precision_bits'] == bits and report['source_sha256'] == source_hash
        assert report['inherited_kernel_sha256'] == kernel_hash
        assert [r['N'] for r in report['rows']] == [8,16,64,512,4096]
        for row in report['rows']:
            assert all(row['gates'].values()) and row['exact_tail_coefficient_cancellation']
            assert len(row['physical_spot_checks']) == 5
            balls = {key: arb(v) for key,v in row['balls'].items()}
            assert balls['full_energy'] > 0
            assert balls['full_energy'] > balls['localized_witness_squared']
            assert balls['centered_triangle_ratio'] < balls['conditioning_constant']
            assert balls['conditioning_constant'] < arb('4.617')
            assert balls['centered_triangle_ratio'] >= 1
    precision_matches = 0
    for first,second in zip(reports[0]['rows'],reports[1]['rows']):
        assert first['N'] == second['N'] and first['cutoff'] == second['cutoff']
        precision_matches += compare(first['balls'],second['balls'],list(first['balls']))
        precision_matches += compare(first['tail'],second['tail'],list(first['tail']))
        for a,b in zip(first['checkpoints'],second['checkpoints']):
            assert a['cutoff'] == b['cutoff']
            assert arb(a['partial_energy']).overlaps(arb(b['partial_energy']))
            precision_matches += 1
    cutoff = json.loads((directory/'cells-cutoff-replay-384bits.json').read_text())
    assert cutoff['source_sha256'] == source_hash and cutoff['precision_bits'] == 384
    by_n = {r['N']:r for r in reports[1]['rows']}
    cutoff_matches = 0
    invariant_keys = ['full_energy','cross_sigma','cross_tau','boundary_energy',
                      'target_plus_integral_energy','integral_energy','whole_term_triangle_ratio',
                      'scaled_eta','laguerre_target','centered_boundary_energy',
                      'centered_target_plus_integral_energy','centered_triangle_ratio',
                      'conditioning_constant','localized_witness_squared']
    for row in cutoff['rows']:
        base = by_n[row['N']]
        assert row['cutoff'] == 2*base['cutoff']
        cutoff_matches += compare(base['balls'],row['balls'],invariant_keys)
        assert arb(row['tail']['energy_error_bound']) < arb(base['tail']['energy_error_bound'])
    gram_reports = [json.loads((directory/f'gram-check-{bits}bits.json').read_text()) for bits in [256,384]]
    gram_matches = 0
    minimum_bits = []
    for bits,report in zip([256,384],gram_reports):
        assert report['precision_bits'] == bits and report['source_sha256'] == gram_hash
        assert report['inherited_kernel_sha256'] == kernel_hash
        for row in report['rows']:
            assert row['all_three_gram_balls_inside_physical_enclosures']
            minimum_bits.append(row['minimum_accuracy_bits'])
            for key,value in row['balls'].items():
                assert arb(by_n[row['N']]['balls'][key]).contains(arb(value))
    for first,second in zip(gram_reports[0]['rows'],gram_reports[1]['rows']):
        gram_matches += compare(first['balls'],second['balls'],list(first['balls']))
    result = {'status':'PASS','precision_bits':[256,384],
              'physical_precision_enclosure_matches':precision_matches,
              'doubled_cutoff_enclosure_matches':cutoff_matches,
              'independent_gram_precision_matches':gram_matches,
              'independent_gram_minimum_accuracy_bits':min(minimum_bits),
              'physical_spot_checks_per_precision':25,
              'uniform_centered_conditioning_bound':'1+2*norm(sigma_1) < 4.617',
              'source_sha256':source_hash,'inherited_kernel_sha256':kernel_hash}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
