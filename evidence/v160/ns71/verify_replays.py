"""Check both precisions, the independent cutoff, and the NS-69 overlap."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def fields(row: dict[str, Any]) -> dict[str, str]:
    result = {key:row[key] for key in ['energy','full_relative_gain']}
    for name, values in row['directions'].items():
        for key,value in values.items():
            result[f'{name}.{key}'] = value
    return result


def matches(left: dict[str, str], right: dict[str, str]) -> int:
    assert set(left) == set(right)
    for key,value in left.items():
        a,b = arb(value),arb(right[key])
        assert a.is_finite() and b.is_finite() and a.overlaps(b), (key,a,b)
    return len(left)


def main() -> None:
    ctx.prec = 512
    directory = Path(__file__).resolve().parent
    source_hash = hashlib.sha256((directory/'certify_preconditioner.py').read_bytes()).hexdigest()
    kernel_hash = hashlib.sha256((directory.parents[1]/'v159/ns61/certify_smoothed.py').read_bytes()).hexdigest()
    reports = [json.loads((directory/f'preconditioner-{bits}bits.json').read_text()) for bits in [256,384]]
    for bits, report in zip([256,384],reports):
        assert report['precision_bits'] == bits and report['finite_series_cutoff'] == 128
        assert report['bernoulli_order'] == 24 and report['source_sha256'] == source_hash
        assert report['kernel_source_sha256'] == kernel_hash
        assert [r['N'] for r in report['rows']] == [16,32,64,128,256]
        for row in report['rows']:
            assert all(row['gates'].values()) and arb(row['energy']) > 0
            fractions = {name:arb(v['fraction_of_full_gain']) for name,v in row['directions'].items()}
            assert all(x>0 and x<1 for x in fractions.values())
            for name in ['raw_repaired_inverse','projected_repaired_inverse']:
                assert fractions[name] > fractions['actual_correlation']
            for item in row['directions'].values():
                assert arb(item['relative_gain']) > arb(item['relative_raw_lower_gain']) > 0
                assert arb(item['old_projection_cost_factor']) > 1
    count = sum(matches(fields(a),fields(b)) for a,b in zip(reports[0]['rows'],reports[1]['rows']))
    cutoff = json.loads((directory/'preconditioner-cutoff-replay-384bits.json').read_text())
    assert cutoff['source_sha256'] == source_hash and cutoff['kernel_source_sha256'] == kernel_hash
    assert cutoff['precision_bits'] == 384 and cutoff['finite_series_cutoff'] == 256
    assert cutoff['bernoulli_order'] == 24 and [r['N'] for r in cutoff['rows']] == [256]
    assert all(cutoff['rows'][0]['gates'].values())
    cutoff_count = matches(fields(reports[1]['rows'][-1]),fields(cutoff['rows'][0]))
    previous = json.loads((directory.parent/'ns69/endpoint-384bits.json').read_text())
    earlier_count = 0
    for first,second in zip(reports[1]['rows'][:4],previous['rows']):
        assert first['N'] == second['N']
        a = {'energy':first['energy'],'full_relative_gain':first['full_relative_gain'],
             'fraction':first['directions']['actual_correlation']['fraction_of_full_gain'],
             'relative_gain':first['directions']['actual_correlation']['relative_gain']}
        b = {'energy':second['quantities']['E_N'],
             'full_relative_gain':second['quantities']['full_relative_gain'],
             'fraction':second['quantities']['actual_direction_fraction_of_gain'],
             'relative_gain':second['quantities']['actual_direction_relative_gain']}
        earlier_count += matches(a,b)
    bounds = [
        [('.2332','.2333'),('.7167','.7169'),('.8390','.8391')],
        [('.3258','.3259'),('.8580','.8581'),('.8252','.8254')],
        [('.2723','.2724'),('.9593','.9594'),('.9577','.9578')],
        [('.2946','.2948'),('.9729','.9730'),('.9781','.9782')],
        [('.3840','.3842'),('.9597','.9598'),('.9705','.9707')],
    ]
    for row, limits in zip(reports[1]['rows'],bounds):
        for name,(lower,upper) in zip(['actual_correlation','raw_repaired_inverse','projected_repaired_inverse'],limits):
            value=arb(row['directions'][name]['fraction_of_full_gain'])
            assert value>arb(lower) and value<arb(upper)
    last=reports[1]['rows'][-1]
    selected=last['directions']['projected_repaired_inverse']
    model_relative=arb(selected['numerator'])/arb(last['energy'])
    selected_ratio=arb(selected['denominator'])/arb(selected['numerator'])
    assert model_relative>arb('.7668') and model_relative<arb('.7669')
    assert selected_ratio>arb('9.4884') and selected_ratio<arb('9.4886')
    assert arb(selected['relative_gain'])>arb('.08081') and arb(selected['relative_gain'])<arb('.08083')
    assert arb(last['full_relative_gain'])>arb('.08326') and arb(last['full_relative_gain'])<arb('.08328')
    result = {'status':'PASS','precision_bits':[256,384],
              'precision_enclosure_matches':count,'doubled_cutoff_matches':cutoff_count,
              'independent_NS69_overlap_matches':earlier_count,
              'minimum_accuracy_bits':min(r['minimum_accuracy_bits'] for report in reports for r in report['rows']),
              'source_sha256':source_hash,'kernel_source_sha256':kernel_hash,
              'largest_block_open_input_values':{'N':256,'model_numerator_over_energy':model_relative.str(60),
                                                  'selected_true_model_ratio':selected_ratio.str(60)},
              'finite_prediction':'both repaired directions outperform the unmodified correlation at every tested size',
              'cofinal_estimate_obtained':False}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
