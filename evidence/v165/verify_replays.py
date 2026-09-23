"""Validate source identity, exact cutoffs, and scalar full-tail enclosures."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from flint import arb, ctx
from ns82.certify_tail import cutoff


def main() -> None:
    ctx.prec = 512
    root = Path(__file__).resolve().parent
    digest = hashlib.sha256((root/'ns82/certify_tail.py').read_bytes()).hexdigest()
    reports = [json.loads((root/f'ns82/tail-{bits}bits.json').read_text()) for bits in [256,384]]
    for report,bits in zip(reports,[256,384]):
        assert report['precision_bits'] == bits and report['source_sha256'] == digest
        assert [r['total_atoms'] for r in report['rows']] == [16,64,256,512]
        for row in report['rows']:
            m,c,squares = cutoff(row['total_atoms'])
            assert row['cutoff'] == m and m**3 >= 16*c*squares/27
            assert row['comparator_assembled'] is False
            v = {key:arb(value) for key,value in row['values'].items()}
            assert 0 < v['relative_remainder_squared_upper_bound'] < arb(1)/4
            assert 1 < v['projected_condition_upper_bound'] < 9
            assert v['ten_step_gain_fraction_lower_bound'] > arb('.9884')
    matches = 0
    for low,high in zip(reports[0]['rows'],reports[1]['rows']):
        assert low['cutoff'] == high['cutoff']
        assert low['values'].keys() == high['values'].keys()
        for key,value in low['values'].items():
            assert arb(value).overlaps(arb(high['values'][key]))
            matches += 1
    assert reports[1]['rows'][-1]['cutoff'] == 8435244
    print(json.dumps({'status':'PASS','precision_bits':[256,384],'precision_enclosure_matches':matches,
                      'source_sha256':digest,'exact_cutoffs_rechecked':4,'comparator_assembled':False,
                      'cutoff_replay':'not applicable: all discarded remainder is bounded analytically; scalar certificates only',
                      'cofinal_error_decay':False,'independent_review':False},indent=2))

if __name__ == '__main__':
    main()
