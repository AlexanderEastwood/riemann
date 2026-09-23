"""Validate finite conditioning certificates and complete scalar tail bounds."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def main() -> None:
    ctx.prec = 512
    folder = Path(__file__).resolve().parent
    directory = folder/'ns81'
    reports = [json.loads((directory/f'conditioning-{bits}bits.json').read_text()) for bits in [256,384]]
    digest = hashlib.sha256((directory/'certify_conditioning.py').read_bytes()).hexdigest()
    matches = 0
    for report,bits in zip(reports,[256,384]):
        assert report['precision_bits'] == bits and report['source_sha256'] == digest
        assert [r['N'] for r in report['rows']] == [16,64,256]
        for row in report['rows']:
            n = row['N']
            assert row['prefix_cells_evaluated'] == n and row['largest_sample_integer'] == n+1
            assert row['sufficient_comparator_cell_stop'] == 2**16*(n+1)**6
            assert row['large_comparator_assembled'] is False and all(row['gates'].values())
            v = {key:arb(value) for key,value in row['values'].items()}
            assert all(value.is_finite() for value in v.values())
            assert 0 < v['certified_inverse_trace'] < v['coefficient_bound_C_N']
            assert v['certified_prefix_eigenvalue_lower_bound_from_trace'] > v['prefix_eigenvalue_lower_bound'] > 0
            assert (16*v['ordinary_gram_eigenvalue_lower_bound']).overlaps(v['prefix_eigenvalue_lower_bound'])
            assert 0 < v['tail_relative_to_prefix_upper_bound'] < v['universal_relative_tail_upper_bound'] < 1
    for low,high in zip(reports[0]['rows'],reports[1]['rows']):
        assert set(low['values']) == set(high['values'])
        for key,value in low['values'].items():
            assert arb(value).overlaps(arb(high['values'][key])),key
            matches += 1
    last = reports[1]['rows'][-1]['values']
    assert arb(last['ordinary_gram_eigenvalue_lower_bound']) > arb('4.91e-14')
    assert arb(last['tail_relative_to_prefix_upper_bound']) < arb('.01925')
    result: dict[str, Any] = {'status':'PASS','precision_bits':[256,384],
                              'precision_enclosure_matches':matches,'source_sha256':digest,
                              'prefix_matrices_tested':[16,64,256],'complete_scalar_tail_bounds_tested':[16,64,256],
                              'enormous_comparators_assembled':False,
                              'cutoff_replay':'not applicable: all small prefix cells evaluated; infinite tail bounded by a complete analytic inequality',
                              'minimum_serialized_accuracy_bits':min(arb(v).rel_accuracy_bits() for report in reports for row in report['rows'] for v in row['values'].values()),
                              'cofinal_error_decay':False,'independent_review':False}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
