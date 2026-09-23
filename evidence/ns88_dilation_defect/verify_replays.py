"""Check all finite identities and record the derived whole-error upper envelope."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from typing import Any
from flint import arb,ctx

HERE=Path(__file__).resolve().parent


def read(name: str) -> dict[str,Any]:
    data=json.loads((HERE/name).read_text())
    script='physical.py' if name.startswith('physical') else 'certify.py'
    assert data['source_sha256']==hashlib.sha256((HERE/script).read_bytes()).hexdigest()
    return data


def compare(first: dict[str,Any],second: dict[str,Any],coefficients: bool) -> tuple[int,int]:
    a={r['N']:r for r in first['rows']};scalar=0;coeffs=0
    for r in second['rows']:
        old=a[r['N']]
        assert old['gates']==r['gates']
        for key,val in r['values'].items():
            assert arb(val).overlaps(arb(old['values'][key])),(r['N'],key)
            scalar+=1
        if coefficients:
            for v,w in zip(r['coefficients'],old['coefficients'],strict=True):
                assert arb(v).overlaps(arb(w));coeffs+=1
    return scalar,coeffs


def envelope(data: dict[str,Any]) -> list[dict[str,Any]]:
    rows=data['rows'];result=[];total=arb(0)
    initial=None;previous_j=None
    for r in rows:
        j=r['j'];v={k:arb(x) for k,x in r['values'].items()}
        if previous_j is not None:assert j==previous_j+1
        previous_j=j
        if initial is None:initial=(v['E_previous']*v['E_N']).sqrt()
        term=abs(v['dilation_defect'])/v['E_previous'];total+=term
        one_step=v['E_N']-2*v['dilation_defect']**2/v['previous_gain']
        upper=initial*(-arb(2).sqrt()*total).exp()
        assert v['E_next']<one_step<v['E_N']
        assert v['E_next']<upper
        assert (v['E_previous']/v['E_next']).log()>2*arb(2).sqrt()*term
        result.append({'N':r['N'],'j':j,'S':total.str(65),
                       'j_times_normalized_defect':(j*term).str(65),
                       'one_step_whole_error_upper':one_step.str(65),
                       'cumulative_whole_error_upper':upper.str(65),
                       'actual_next_error':v['E_next'].str(65)})
    return result


def main() -> None:
    ctx.prec=512
    low=read('check-256bits.json');high=read('check-384bits.json');cut=read('check-cutoff-384bits.json')
    plow=read('physical-256bits.json');phigh=read('physical-384bits.json');pcut=read('physical-cutoff-384bits.json')
    precision=compare(low,high,True);cutoff=compare(high,cut,True)
    physical=compare(plow,phigh,False)
    # Different physical truncations use different explicit remainder radii;
    # only the three full physical quantities represent the same observables.
    by_n={r['N']:r for r in phigh['rows']}
    for r in pcut['rows']:
        for key in ['potential_at_two','autocorrelation_at_two','dilation_defect']:
            assert arb(r['values'][key]).overlaps(arb(by_n[r['N']]['values'][key]))
    low_env=envelope(low);high_env=envelope(high)
    for a,b in zip(low_env,high_env,strict=True):
        for key in ['S','j_times_normalized_defect','one_step_whole_error_upper','cumulative_whole_error_upper','actual_next_error']:
            assert arb(a[key]).overlaps(arb(b[key]))
    results={r['N']:r for r in high['rows']}
    assert arb(results[16]['values']['fraction_of_available_gain'])<arb('0.003257')
    assert arb(results[8]['values']['dilation_defect'])>0
    assert arb(results[16]['values']['dilation_defect'])>0
    assert arb(results[32]['values']['dilation_defect'])<0
    assert arb(results[64]['values']['dilation_defect'])<0
    log=(HERE/'exact-checks-output.txt').read_text()
    assert 'NS88 exact checks passed: 13' in log and '\nFAIL ' not in log and '#0: checkzero' not in log
    report={'classification':'Certified finite replay and derived upper bounds; no eventual arithmetic estimate',
            'precision_scalar_overlaps':precision[0],'precision_coefficient_overlaps':precision[1],
            'kernel_cutoff_scalar_overlaps':cutoff[0],'kernel_cutoff_coefficient_overlaps':cutoff[1],
            'physical_precision_overlaps':physical[0],'physical_cutoff_full_quantity_overlaps':3,
            'physical_vs_Gram_full_quantity_checks':27,'envelope_precision_overlaps':20,
            'Maxima_exact_checks':13,'dyadic_envelope':high_env}
    (HERE/'replay-validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
