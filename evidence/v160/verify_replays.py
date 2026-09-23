"""Verify complete finite NS-68--70 replays and displayed outward intervals."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare(left: dict[str, Any], right: dict[str, Any]) -> int:
    assert set(left) == set(right)
    for key in left:
        a, b = arb(left[key]), arb(right[key])
        assert a.is_finite() and b.is_finite() and a.overlaps(b), (key, a, b)
    return len(left)


def inside(value: str, lower: str, upper: str) -> None:
    ball = arb(value)
    assert ball > arb(lower) and ball < arb(upper), (value, lower, upper)


def main() -> None:
    ctx.prec = 512
    root = Path(__file__).resolve().parent
    kernel_hash = sha(root.parent/'v159/ns61/certify_smoothed.py')
    specifications = [
        ('ns68','renewal','certify_renewal.py','balls',[16,64,512,4096,65536,1048576]),
        ('ns69','endpoint','certify_endpoint.py','quantities',[16,32,64,128]),
        ('ns70','background','certify_background.py','balls',[256,1024,4096]),
    ]
    output: dict[str, Any] = {'status':'PASS','precision_bits':[256,384],'groups':{}}
    for name, prefix, source, field, sizes in specifications:
        directory = root/name
        reports = [json.loads((directory/f'{prefix}-{bits}bits.json').read_text()) for bits in [256,384]]
        for bits, report in zip([256,384],reports):
            assert report['precision_bits'] == bits
            assert report['source_sha256'] == sha(directory/source)
            if name == 'ns68':
                assert report['sibling_source_sha256'] == sha(root/'ns67/certify_cells.py')
                assert report['maximum_mobius_index'] == 2*max(sizes)
            else:
                assert report['kernel_source_sha256'] == kernel_hash
                assert report['finite_series_cutoff'] == 128 and report['bernoulli_order'] == 24
            assert [row.get('N',row.get('n')) for row in report['rows']] == sizes
            for row in report['rows']:
                assert row['gates'] and all(row['gates'].values())
                if name == 'ns68':
                    b = row[field]
                    assert arb(b['renewal_residual']).contains(0)
                    assert arb(b['energy_ratio']) > arb(b['weighted_lower_factor'])
                    assert arb(b['energy_ratio']) < arb(b['weighted_upper_factor'])
        matches = 0
        for first, second in zip(reports[0]['rows'],reports[1]['rows']):
            matches += compare(first[field],second[field])
            if name == 'ns69':
                assert len(first['samples']) == len(second['samples']) == 5
                for a,b in zip(first['samples'],second['samples']):
                    assert a['index'] == b['index']
                    matches += compare({k:v for k,v in a.items() if k != 'index'},
                                       {k:v for k,v in b.items() if k != 'index'})
        if name == 'ns68':
            for a,b in zip(reports[0]['constants'],reports[1]['constants']):
                assert a['theta'] == b['theta']
                matches += compare({k:v for k,v in a.items() if k != 'theta'},
                                   {k:v for k,v in b.items() if k != 'theta'})
                inside(a['kernel_mass'],'0','1')
            inside(reports[1]['constants'][1]['kernel_mass'],'.8027641','.8027642')
            inside(reports[1]['constants'][1]['power_transfer_constant'],'3.58508','3.58509')
        if name == 'ns70':
            matches += compare(reports[0]['constants'],reports[1]['constants'])
            assert all(arb(v)>0 for v in reports[1]['constants'].values())
        cutoff_matches = 0
        if name != 'ns68':
            replay = json.loads((directory/f'{prefix}-cutoff-replay-384bits.json').read_text())
            assert replay['source_sha256'] == sha(directory/source)
            assert replay['kernel_source_sha256'] == kernel_hash
            assert replay['precision_bits'] == 384 and replay['finite_series_cutoff'] == 256
            assert replay['bernoulli_order'] == 24
            by_size = {r.get('N',r.get('n')):r for r in reports[1]['rows']}
            for row in replay['rows']:
                base = by_size[row.get('N',row.get('n'))]
                assert all(row['gates'].values())
                cutoff_matches += compare(base[field],row[field])
                if name == 'ns69':
                    for a,b in zip(base['samples'],row['samples']):
                        assert a['index'] == b['index']
                        cutoff_matches += compare({k:v for k,v in a.items() if k != 'index'},
                                                  {k:v for k,v in b.items() if k != 'index'})
            if name == 'ns70':
                cutoff_matches += compare(reports[1]['constants'],replay['constants'])
        output['groups'][name] = {'precision_enclosure_matches':matches,
                                  'doubled_cutoff_matches':cutoff_matches,
                                  'source_sha256':sha(directory/source)}
        if name != 'ns68':
            output['groups'][name]['minimum_recorded_accuracy_bits'] = min(
                r['minimum_accuracy_bits'] for report in reports for r in report['rows'])
        if name == 'ns69':
            intervals = [
                [('.6074','.6076'),('.8477','.8479'),('.1204','.1205'),('.2332','.2333')],
                [('.9250','.9252'),('.7982','.7983'),('.2036','.2037'),('.3258','.3259')],
                [('2.0203','2.0205'),('.5966','.5968'),('.0806','.0807'),('.2723','.2724')],
                [('3.1748','3.1750'),('.4592','.4594'),('.0330','.0331'),('.2946','.2948')],
            ]
            keys = ['remainder_over_leading','leading_actual_cosine',
                    'two_moment_fraction_of_gain','actual_direction_fraction_of_gain']
            for row, bounds in zip(reports[1]['rows'],intervals):
                for key,(lower,upper) in zip(keys,bounds):
                    inside(row[field][key],lower,upper)
                inside(row[field]['improved_budget_over_actual_remainder'],'216','541')
                inside(row['samples'][-1]['relative_remainder'],'0','.017')
            inside(reports[1]['rows'][2][field]['endpoint_log_coefficient'],'-.000554','-.000553')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
