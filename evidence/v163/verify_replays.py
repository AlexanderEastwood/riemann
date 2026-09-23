"""Audit complete sampling and tail-balanced arithmetic evidence."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
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


def balanced_fields(row: dict[str, Any]) -> dict[str, str]:
    return flatten({key:row[key] for key in ['quantities','directions','span_fit_coefficients']})


def main() -> None:
    ctx.prec = 512
    folder = Path(__file__).resolve().parent
    output: dict[str, Any] = {'status':'PASS','precision_bits':[256,384],'groups':{},
                              'cofinal_arithmetic_bound':False,'independent_review':False}
    earlier = json.loads((folder.parent/'v162/ns75/divisor-384bits.json').read_text())
    old = {row['N']:row for row in earlier['rows']}
    directory = folder/'ns78'
    reports = [json.loads((directory/f'cells-{bits}bits.json').read_text()) for bits in [256,384]]
    cutoff = json.loads((directory/'cells-cutoff-replay-384bits.json').read_text())
    digest = hashlib.sha256((directory/'certify_cells.py').read_bytes()).hexdigest()
    kernel_hash = hashlib.sha256((folder.parent/'v159/ns61/certify_smoothed.py').read_bytes()).hexdigest()
    for report,bits,limit,stop,sizes in zip(reports+[cutoff],[256,384,384],[128,128,256],[65536,65536,131072],
                                          [[16,64,256],[16,64,256],[256]]):
        assert report['precision_bits'] == bits and report['kernel_series_cutoff'] == limit
        assert report['kernel_bernoulli_order'] == 24 and report['source_sha256'] == digest
        assert report['dependency_sha256'] == {'kernel':kernel_hash}
        assert [r['N'] for r in report['rows']] == sizes
        for row in report['rows']:
            assert row['reciprocal_cell_stop'] == stop and all(row['gates'].values())
            values = {key:arb(value) for key,value in row['values'].items()}
            energy = values['gram_energy']
            center = values['finite_cell_energy_with_exterior']+values['complete_main_tail']
            direct = center+arb(0,values['complete_tail_radius'])
            assert direct.contains(energy)
            assert energy.overlaps(arb(old[row['N']]['quantities']['energy']))
            assert (values['eta']**2+values['sample_prefix']+values['complete_sample_tail_upper'])/16 < energy
            assert energy < arb(21)/16*(values['eta']**2+values['sample_prefix'])
            assert values['complete_physical_energy_enclosure'].contains(energy)
            assert values['comparison_quantity_enclosure']/energy > 0
    precision = sum(matches(a['values'],b['values']) for a,b in zip(reports[0]['rows'],reports[1]['rows']))
    stable = ['gram_energy','eta','tail_slope','tail_constant','stirling_remainder_constant',
              'complete_physical_energy_enclosure','complete_sample_sum_enclosure',
              'comparison_quantity_enclosure','comparison_quantity_over_energy']
    cutoff_matches = matches({key:reports[1]['rows'][-1]['values'][key] for key in stable},
                             {key:cutoff['rows'][0]['values'][key] for key in stable})
    for row,(lo,hi),bound in zip(reports[1]['rows'],[('3.323','3.325'),('2.9002','2.9004'),('2.644','2.646')],
                               ['1.64e-6','5.20e-6','2.38e-4']):
        assert arb(lo) < arb(row['values']['comparison_quantity_over_energy']) < arb(hi)
        assert arb(row['values']['tail_radius_over_gram_energy']) < arb(bound)
    assert arb(cutoff['rows'][0]['values']['tail_radius_over_gram_energy']) < arb('4.17e-5')
    output['groups']['ns78'] = {'precision_enclosure_matches':precision,'complete_cutoff_overlap_matches':cutoff_matches,
                               'published_gram_overlap_checks':7,'complete_reconstructed_norm_contains_gram_checks':7,
                               'source_sha256':digest,'largest_complete_tail_radius_over_energy':cutoff['rows'][0]['values']['tail_radius_over_gram_energy']}
    directory = folder/'ns79'
    if not (directory/'balanced-cutoff-replay-384bits.json').exists():
        raise RuntimeError('NS79 full replay not yet complete')
    reports = [json.loads((directory/f'balanced-{bits}bits.json').read_text()) for bits in [256,384]]
    cutoff = json.loads((directory/'balanced-cutoff-replay-384bits.json').read_text())
    digest = hashlib.sha256((directory/'certify_balanced.py').read_bytes()).hexdigest()
    deps = {'kernel':folder.parent/'v159/ns61/certify_smoothed.py',
            'projection':folder.parent/'v160/ns71/certify_preconditioner.py',
            'curvature':folder.parent/'v161/ns72/certify_curvature.py'}
    for report,bits,limit,sizes in zip(reports+[cutoff],[256,384,384],[128,128,256],
                                     [[16,32,64,128,256],[16,32,64,128,256],[256]]):
        assert report['precision_bits'] == bits and report['finite_series_cutoff'] == limit
        assert report['bernoulli_order'] == 24 and report['source_sha256'] == digest
        assert [r['N'] for r in report['rows']] == sizes
        assert report['dependency_sha256'] == {key:hashlib.sha256(path.read_bytes()).hexdigest() for key,path in deps.items()}
        for row in report['rows']:
            assert all(row['gates'].values())
            span = arb(row['quantities']['three_direction_span_fraction'])
            extended = arb(row['quantities']['endpoint_augmented_span_fraction'])
            assert 0 < span < extended < 1
            assert extended > arb(old[row['N']]['quantities']['three_direction_span_fraction'])
            assert all(0 < arb(row['directions'][key]['fraction_of_full_gain']) < span
                       for key in ['balanced_divisor_cancellation','balanced_linear_defect','balanced_quadratic_defect'])
    precision = sum(matches(balanced_fields(a),balanced_fields(b)) for a,b in zip(reports[0]['rows'],reports[1]['rows']))
    cutoff_count = matches(balanced_fields(reports[1]['rows'][-1]),balanced_fields(cutoff['rows'][0]))
    overlaps = 0
    for row in reports[1]['rows']:
        earlier_row = old[row['N']]
        overlaps += matches({'energy':row['quantities']['energy'],'full':row['quantities']['full_relative_gain'],
                             'fraction':row['directions']['diagonal_curvature']['fraction_of_full_gain'],
                             'cost':row['directions']['diagonal_curvature']['true_projected_cost']},
                            {'energy':earlier_row['quantities']['energy'],'full':earlier_row['quantities']['full_relative_gain'],
                             'fraction':earlier_row['directions']['diagonal_curvature']['fraction_of_full_gain'],
                             'cost':earlier_row['directions']['diagonal_curvature']['true_projected_cost']})
    increasing = 0
    decreasing = []
    for row in reports[1]['rows']:
        for name in ['balanced_divisor_cancellation','balanced_linear_defect','balanced_quadratic_defect']:
            ratio = arb(row['directions'][name]['held_old_unit_step_error_ratio'])
            if ratio > 1:
                increasing += 1
            else:
                assert ratio < 1
                decreasing.append([row['N'],name])
        assert arb(row['quantities']['endpoint_augmented_span_fraction']) < arb(row['directions']['diagonal_curvature']['fraction_of_full_gain'])
    assert increasing == 13 and decreasing == [[128,'balanced_linear_defect'],[128,'balanced_quadratic_defect']]
    assert arb('53.07') < arb(reports[1]['rows'][-1]['directions']['balanced_divisor_cancellation']['held_old_unit_step_error_ratio']) < arb('53.09')
    for name,lo,hi in [('balanced_linear_defect','.9643','.9645'),('balanced_quadratic_defect','.9890','.9893')]:
        assert arb(lo) < arb(reports[1]['rows'][3]['directions'][name]['held_old_unit_step_error_ratio']) < arb(hi)
    lines = [line for line in (directory/'proof.tex').read_text().splitlines() if re.match(r'^\d+&\(',line)]
    assert len(lines) == 5
    for line,row in zip(lines,reports[1]['rows']):
        assert int(line.split('&')[0]) == row['N']
        values = [row['quantities']['three_direction_span_fraction'],row['quantities']['endpoint_augmented_span_fraction'],row['directions']['diagonal_curvature']['fraction_of_full_gain']]
        limits = re.findall(r'\(([.\d]+),([.\d]+)\)',line)
        assert len(limits) == 3
        for value,(lo,hi) in zip(values,limits):
            assert arb(lo) < arb(value) < arb(hi)
    output['groups']['ns79'] = {'precision_enclosure_matches':precision,'doubled_cutoff_matches':cutoff_count,
                               'published_overlap_matches':overlaps,'source_sha256':digest,'table_intervals_verified':15,'raw_unit_increases':increasing,'raw_unit_decreases':decreasing,
                               'minimum_nonzero_serialized_accuracy_bits':min(arb(v).rel_accuracy_bits()
                                  for report in reports for row in report['rows'] for v in balanced_fields(row).values() if not arb(v).is_zero())}
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
