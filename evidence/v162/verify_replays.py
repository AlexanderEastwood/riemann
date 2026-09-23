"""Audit v162 source hashes, complete finite replays, table enclosures and scope."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any

from flint import arb, ctx


def flatten(value: Any, prefix: str = '') -> dict[str, str]:
    if isinstance(value, str):
        return {prefix:value}
    if isinstance(value, list):
        return {key:item for i,entry in enumerate(value) for key,item in flatten(entry,f'{prefix}.{i}').items()}
    return {key:item for name,entry in value.items() for key,item in flatten(entry,f'{prefix}.{name}').items()}


def matches(left: dict[str, str], right: dict[str, str]) -> int:
    assert set(left) == set(right)
    for key,value in left.items():
        a,b = arb(value),arb(right[key])
        assert a.is_finite() and b.is_finite() and a.overlaps(b), (key,a,b)
    return len(left)


def fields(row: dict[str, Any]) -> dict[str, str]:
    return flatten({key:row[key] for key in ['quantities','directions','span_fit_coefficients']})


def main() -> None:
    ctx.prec = 512
    folder = Path(__file__).resolve().parent
    deps = {'kernel':folder.parent/'v159/ns61/certify_smoothed.py',
            'projection':folder.parent/'v160/ns71/certify_preconditioner.py',
            'curvature':folder.parent/'v161/ns72/certify_curvature.py'}
    output: dict[str, Any] = {'status':'PASS','precision_bits':[256,384],'groups':{},
                              'cofinal_arithmetic_bound':False,'independent_review':False}
    directory = folder/'ns75'
    reports = [json.loads((directory/f'divisor-{bits}bits.json').read_text()) for bits in [256,384]]
    cutoff = json.loads((directory/'divisor-cutoff-replay-384bits.json').read_text())
    digest = hashlib.sha256((directory/'certify_divisor.py').read_bytes()).hexdigest()
    for report,bits,limit,sizes in zip(reports+[cutoff],[256,384,384],[128,128,256],
                                     [[16,32,64,128,256],[16,32,64,128,256],[256]]):
        assert report['precision_bits'] == bits and report['finite_series_cutoff'] == limit
        assert report['bernoulli_order'] == 24 and report['source_sha256'] == digest
        assert [r['N'] for r in report['rows']] == sizes
        assert set(report['dependency_sha256']) == set(deps)
        for key,value in report['dependency_sha256'].items():
            assert value == hashlib.sha256(deps[key].read_bytes()).hexdigest()
        for row in report['rows']:
            assert all(row['gates'].values())
    precision = sum(matches(fields(a),fields(b)) for a,b in zip(reports[0]['rows'],reports[1]['rows']))
    cutoff_count = matches(fields(reports[1]['rows'][-1]),fields(cutoff['rows'][0]))
    earlier = json.loads((folder.parent/'v161/ns72/curvature-384bits.json').read_text())
    overlap = 0
    names = ['raw_divisor_cancellation','linear_log_defect','quadratic_log_defect']
    for row,old in zip(reports[1]['rows'],earlier['rows']):
        assert row['N'] == old['N']
        new = row['directions']['diagonal_curvature']
        previous = old['directions']['diagonal_curvature']
        overlap += matches({'energy':row['quantities']['energy'],'full':row['quantities']['full_relative_gain'],
                            'fraction':new['fraction_of_full_gain'],'cost':new['true_projected_cost']},
                           {'energy':old['quantities']['energy'],'full':old['quantities']['full_relative_gain'],
                            'fraction':previous['fraction_of_full_gain'],'cost':previous['true_projected_cost']})
        span = arb(row['quantities']['three_direction_span_fraction'])
        assert 0 < span < arb(new['fraction_of_full_gain']) < 1
        for name in names:
            data = row['directions'][name]
            assert 0 < arb(data['fraction_of_full_gain']) < span
            assert arb(data['held_old_unit_step_error_ratio']) > 1
        assert 0 < arb(row['quantities']['curvature_energy_fraction_in_span']) < 1
    lines = [line for line in (directory/'proof.tex').read_text().splitlines() if re.match(r'^\d+&\(',line)]
    assert len(lines) == 5
    for line,row in zip(lines,reports[1]['rows']):
        assert int(line.split('&')[0]) == row['N']
        values = [row['directions']['raw_divisor_cancellation']['fraction_of_full_gain'],
                  row['quantities']['three_direction_span_fraction'],row['directions']['diagonal_curvature']['fraction_of_full_gain']]
        limits = re.findall(r'\(([.\d]+),([.\d]+)\)',line)
        assert len(limits) == 3
        for value,(lo,hi) in zip(values,limits):
            assert arb(lo) < arb(value) < arb(hi)
    last = reports[1]['rows'][-1]['directions']['raw_divisor_cancellation']
    assert arb(last['numerator']) < 0
    assert arb('1495.54') < arb(last['held_old_unit_step_error_ratio']) < arb('1495.55')
    output['groups']['ns75'] = {'precision_enclosure_matches':precision,'doubled_cutoff_matches':cutoff_count,
                               'NS72_overlap_matches':overlap,'source_sha256':digest,
                               'table_intervals_verified':15,'all_fifteen_held_old_unit_steps_increase_error':True,
                               'minimum_nonzero_serialized_accuracy_bits':min(arb(v).rel_accuracy_bits()
                                   for report in reports for row in report['rows'] for v in fields(row).values() if not arb(v).is_zero())}
    for task,stem,script in [('ns76','local-gap','certify_local_gap.py'),('ns77','tail','certify_tail.py')]:
        directory = folder/task
        pair = [json.loads((directory/f'{stem}-{bits}bits.json').read_text()) for bits in [256,384]]
        digest = hashlib.sha256((directory/script).read_bytes()).hexdigest()
        for report,bits in zip(pair,[256,384]):
            assert report['precision_bits'] == bits and report['source_sha256'] == digest
            assert all(report['gates'].values())
        left = flatten({key:pair[0][key] for key in ['values','hypothetical_pair_controls'] if key in pair[0]})
        right = flatten({key:pair[1][key] for key in ['values','hypothetical_pair_controls'] if key in pair[1]})
        count = matches(left,right)
        if task == 'ns76':
            gap = arb(pair[1]['values']['full_space_squared_distance_lower_bound'])
            assert arb('.00111713') < gap < arb('.00111714')
        else:
            bound = arb(pair[1]['values']['continuous_squared_distance_upper_bound'])
            assert 0 < bound < arb('2.08e-32')
            assert pair[0]['external_inputs'] == pair[1]['external_inputs']
            for report in pair:
                for control in report['hypothetical_pair_controls']:
                    assert 0 < arb(control['exact_pair_squared_distance']) < arb(control['pair_budget'])
        output['groups'][task] = {'precision_enclosure_matches':count,'source_sha256':digest,
                                 'minimum_nonzero_serialized_accuracy_bits':min(arb(v).rel_accuracy_bits()
                                      for values in [left,right] for v in values.values() if not arb(v).is_zero()),
                                 'cutoff_replay':'not applicable: complete elementary finite expressions; zero tail handled analytically in NS77'}
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
