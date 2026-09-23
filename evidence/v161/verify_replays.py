"""Verify template and same-Gram controls, including inherited overlaps."""
from __future__ import annotations

from fractions import Fraction
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


def fields(row: dict[str, Any]) -> dict[str, str]:
    return flatten({key:row[key] for key in ['quantities','directions','span_fit_coefficients','families'] if key in row})


def matches(left: dict[str, str], right: dict[str, str]) -> int:
    assert set(left) == set(right)
    for key,value in left.items():
        a,b = arb(value),arb(right[key])
        assert a.is_finite() and b.is_finite() and a.overlaps(b), (key,a,b)
    return len(left)


def main() -> None:
    ctx.prec = 512
    folder = Path(__file__).resolve().parent
    deps = {'kernel':folder.parent/'v159/ns61/certify_smoothed.py',
            'projection':folder.parent/'v160/ns71/certify_preconditioner.py',
            'sieve':folder.parent/'v160/ns67/certify_cells.py',
            'curvature':folder/'ns72/certify_curvature.py'}
    earlier = json.loads((folder/'ns72/curvature-384bits.json').read_text())
    table_counts: dict[str, int] = {}
    for task, stem, names in [
        ('ns72','curvature',['repaired_model','spline_curvature','diagonal_curvature']),
        ('ns73','mobius',['sharp_mobius','linear_log_taper','quadratic_log_taper','span'])]:
        report = json.loads((folder/task/f'{stem}-384bits.json').read_text())
        lines = [line for line in (folder/task/'proof.tex').read_text().splitlines() if re.match(r'^\d+&\(',line)]
        assert len(lines) == len(report['rows'])
        count = 0
        for line,row in zip(lines,report['rows']):
            assert int(line.split('&')[0]) == row['N']
            limits = re.findall(r'\(([.\d]+),([.\d]+)\)',line)
            assert len(limits) == len(names)
            for name,(lo,hi) in zip(names,limits):
                value = arb(row['quantities']['three_direction_span_fraction'] if name == 'span'
                            else row['directions'][name]['fraction_of_full_gain'])
                assert arb(lo) < value < arb(hi)
                count += 1
        table_counts[task] = count
    assert all(arb('.0619') < arb(r['quantities']['certified_numerator_lower_fraction']) < arb('.0626')
               for r in earlier['rows'])
    output: dict[str, Any] = {'status':'PASS','precision_bits':[256,384],'groups':{},'cofinal_arithmetic_bound':False}
    output['manuscript_table_intervals_verified'] = table_counts
    for task,stem,script in [('ns73','mobius','certify_mobius.py'),('ns74','deformation','certify_deformation.py')]:
        directory = folder/task
        reports = [json.loads((directory/f'{stem}-{bits}bits.json').read_text()) for bits in [256,384]]
        cutoff = json.loads((directory/f'{stem}-cutoff-replay-384bits.json').read_text())
        source_hash = hashlib.sha256((directory/script).read_bytes()).hexdigest()
        for report,bits,limit,sizes in zip(reports+[cutoff],[256,384,384],[128,128,256],
                                           [[16,32,64,128,256],[16,32,64,128,256],[256]]):
            assert report['precision_bits'] == bits and report['finite_series_cutoff'] == limit
            assert report['bernoulli_order'] == 24 and report['source_sha256'] == source_hash
            assert [r['N'] for r in report['rows']] == sizes
            assert set(report['dependency_sha256']) == (set(deps) if task == 'ns73' else set(deps)-{'sieve'})
            for key,digest in report['dependency_sha256'].items():
                assert digest == hashlib.sha256(deps[key].read_bytes()).hexdigest()
            for row in report['rows']:
                assert all(row['gates'].values())
                assert all(arb(v).is_finite() for v in fields(row).values())
        precision = sum(matches(fields(a),fields(b)) for a,b in zip(reports[0]['rows'],reports[1]['rows']))
        cutoff_count = matches(fields(reports[1]['rows'][-1]),fields(cutoff['rows'][0]))
        overlap = 0
        for row,old in zip(reports[1]['rows'],earlier['rows']):
            assert row['N'] == old['N']
            previous = old['directions']['diagonal_curvature']
            if task == 'ns73':
                new = row['directions']['diagonal_curvature']
                overlap += matches({'energy':row['quantities']['energy'],'full':row['quantities']['full_relative_gain'],
                                    'fraction':new['fraction_of_full_gain'],'cost':new['true_projected_cost']},
                                   {'energy':old['quantities']['energy'],'full':old['quantities']['full_relative_gain'],
                                    'fraction':previous['fraction_of_full_gain'],'cost':previous['true_projected_cost']})
                span = arb(row['quantities']['three_direction_span_fraction'])
                assert 0 < span < arb(new['fraction_of_full_gain']) < 1
                assert all(span > arb(row['directions'][name]['fraction_of_full_gain']) > 0
                           for name in ['sharp_mobius','linear_log_taper','quadratic_log_taper'])
                assert 0 < arb(row['quantities']['curvature_energy_fraction_in_span']) < 1
            else:
                original = row['families']['original']
                overlap += matches({'energy':original['energy'],'full':original['full_relative_gain'],
                                    'fraction':original['curvature_fraction_of_full_gain'],'cost':original['curvature_true_cost']},
                                   {'energy':old['quantities']['energy'],'full':old['quantities']['full_relative_gain'],
                                    'fraction':previous['fraction_of_full_gain'],'cost':previous['true_projected_cost']})
                for denominator in [1000000,10000000000]:
                    data = row['families'][f'beta_half_plus_1_over_{denominator}']
                    exact = Fraction(32*denominator**3*(denominator-2)**2,(denominator+2)**6)
                    expected = arb(exact.numerator)/exact.denominator
                    assert expected > 0 and expected.overlaps(arb(data['positive_floor']))
                    assert arb(data['energy']) > arb(data['next_energy']) > expected
                    assert arb('.9') < arb(data['curvature_fraction_of_full_gain']) < 1
                    assert abs(arb(data['curvature_fraction_of_full_gain'])-arb(original['curvature_fraction_of_full_gain'])) < arb('.00001')
        output['groups'][task] = {'precision_enclosure_matches':precision,'doubled_cutoff_matches':cutoff_count,
                                 'NS72_overlap_matches':overlap,'source_sha256':source_hash,
                                 'minimum_nonzero_serialized_accuracy_bits':min(arb(v).rel_accuracy_bits()
                                     for report in reports for row in report['rows'] for v in fields(row).values() if not arb(v).is_zero())}
        if task == 'ns73':
            last = reports[1]['rows'][-1]
            assert arb('.8366') < arb(last['quantities']['three_direction_span_fraction']) < arb('.8367')
            output['groups'][task]['conclusion'] = 'curvature exceeds even the optimized three-template span at all five sizes; no asymptotic exclusion'
        else:
            last = reports[1]['rows'][-1]['families']['beta_half_plus_1_over_1000000']
            assert arb(last['floor_fraction_of_energy']) > arb('.69')
            for key,lo,hi in [('energy','.00004614','.00004615'),('positive_floor','.00003199','.00003200'),
                              ('curvature_fraction_of_full_gain','.9763','.9764'),('curvature_relative_gain','.02491','.02493')]:
                assert arb(lo) < arb(last[key]) < arb(hi)
            assert arb(last['floor_fraction_of_energy']) > arb('.6934')
            output['groups'][task]['largest_block_altered_family'] = last
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
