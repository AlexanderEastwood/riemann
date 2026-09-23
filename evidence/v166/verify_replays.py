"""Check finite zero-subset constants without converting them to finite error bounds."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from flint import arb,ctx


def main() -> None:
    ctx.prec = 512
    root = Path(__file__).resolve().parent
    digest = hashlib.sha256((root/'ns83/certify_constants.py').read_bytes()).hexdigest()
    reports = [json.loads((root/f'ns83/constants-{bits}bits.json').read_text()) for bits in [256,384]]
    for report,bits in zip(reports,[256,384]):
        assert report['precision_bits'] == bits and report['source_sha256'] == digest
        assert report['asymptotic_onset_N0'] is None and not report['error_upper_bound'] and not report['RH_proved']
        assert report['multiplicity_weights_used'] == 1 and report['both_conjugates_counted']
        assert [r['positive_zero_index'] for r in report['rows']] == list(range(1,11))
        last = arb(0)
        totals = {q:arb(0) for q in [1,2,3]}
        for row in report['rows']:
            height = arb(row['ordinate'])
            assert arb(row['real_part']) == arb(1)/2 and height > last
            for q in [1,2,3]:
                weight = arb(row['pair_weights'][f'pair_weight_q{q}'])
                assert weight > 0 and weight.overlaps(2/(height*height+arb(1)/4)**q)
                totals[q] += weight
            last = height
        for q in [1,2,3]:
            assert totals[q].overlaps(arb(report['partial_constants'][f'q{q}']))
        assert arb(report['partial_constants']['q2']) > arb('0.000072332433')
        assert [r['multiplicity'] for r in report['hilbert_blocks']] == list(range(1,9))
        assert all(int(r['inverse_top_left']) == r['multiplicity']**2 and r['equals_m_squared'] for r in report['hilbert_blocks'])
    matches = 0
    for low,high in zip(reports[0]['rows'],reports[1]['rows']):
        assert arb(low['ordinate']).overlaps(arb(high['ordinate']))
        matches += 1
        for key in low['pair_weights']:
            assert arb(low['pair_weights'][key]).overlaps(arb(high['pair_weights'][key]))
            matches += 1
    for key in reports[0]['partial_constants']:
        assert arb(reports[0]['partial_constants'][key]).overlaps(arb(reports[1]['partial_constants'][key]))
        matches += 1
    print(json.dumps({'status':'PASS','precision_bits':[256,384],'precision_enclosure_matches':matches,
                      'exact_hilbert_blocks_checked':8,'source_sha256':digest,
                      'critical_zeros_used':20,'finite_zero_subset_only':True,
                      'cutoff_replay':'not applicable: omitted zero weights are nonnegative and the subset constant is only a lower bound',
                      'finite_N_error_bound':False,'asymptotic_onset_N0':None,'independent_review':False},indent=2))

if __name__ == '__main__':
    main()
