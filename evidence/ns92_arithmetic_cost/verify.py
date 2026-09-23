"""Verify NS92 finite replays, exact arithmetic, and dependency bindings."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from flint import arb, ctx
from certify_cost import ROOT, digest, mobius

HERE=Path(__file__).resolve().parent


def read(name: str) -> dict[str, Any]:
    return json.loads((HERE/name).read_text())


def main() -> None:
    ctx.prec=384
    base,high,cut=[read(f'cost-{s}.json') for s in ['256bits','384bits','cutoff-384bits']]
    counts={'scalar_precision_overlaps':0,'scalar_cutoff_invariants':0,
            'physical_precision_overlaps':0,'physical_cutoff_overlaps':0}
    for dataset in [base,high,cut]:
        assert dataset['source_sha256']==digest(HERE/'certify_cost.py')
        assert dataset['input_sha256']==digest(ROOT/dataset['input_path'])
        for row in dataset['rows']:
            u=arb(row['values']['complete_cost_upper'])
            assert arb('0.00098')<u<arb('0.00220')
            if 'finite_gain' in row:
                assert arb(row['finite_gain']['rational_step_lower_relative_gain'])>0
    for a,b in zip(base['rows'],high['rows']):
        assert a['N']==b['N']
        for field in ['values','finite_gain']:
            for k,v in a.get(field,{}).items():
                if k=='rational_step':
                    assert v==b[field][k]=='1/512'
                    continue
                assert arb(v).overlaps(arb(b[field][k])),(a['N'],k)
                counts['scalar_precision_overlaps']+=1
    a=next(r for r in high['rows'] if r['N']==256);b=cut['rows'][0]
    assert b['N']==256
    for k,v in a['values'].items():
        assert arb(v).overlaps(arb(b['values'][k]))
        counts['scalar_cutoff_invariants']+=1
    for k in ['inherited_true_cost_for_validation_only','inherited_numerator_for_validation_only','inherited_energy']:
        assert arb(a['finite_gain'][k]).overlaps(arb(b['finite_gain'][k]))
        counts['scalar_cutoff_invariants']+=1
    assert arb(a['finite_gain']['lower_relative_gain'])>arb('0.000464')
    assert arb(a['finite_gain']['rational_step_lower_relative_gain'])>arb('0.000443')
    physical=[read(f'physical-{s}.json') for s in ['256bits','384bits','cutoff-384bits']]
    for dataset in physical:
        assert dataset['source_sha256']==digest(HERE/'physical_step.py')
        for p,h in dataset['dependencies'].items():
            assert digest(ROOT/p)==h,p
        v=dataset['values']
        assert arb(v['complete_endpoint_direction_cost'])<arb(v['scalar_cost_upper'])
        assert arb(v['rational_step_actual_gain'])>arb(v['rational_step_lower_gain'])>0
        assert arb(v['larger_rational_step_actual_relative_gain'])>arb('0.0157')
    for left,right,name in [(physical[0],physical[1],'physical_precision_overlaps'),
                            (physical[1],physical[2],'physical_cutoff_overlaps')]:
        for k,v in left['values'].items():
            if k=='rational_step_lower_gain' and name=='physical_cutoff_overlaps':
                continue  # NS91 finite lower bounds change with its cutoff.
            assert arb(v).overlaps(arb(right['values'][k])),k
            counts[name]+=1
    mu=mobius(2*max(r['N'] for r in high['rows']))
    totals=[0]*len(mu)
    for d in range(1,len(mu)):
        for n in range(d,len(mu),d):
            totals[n]+=mu[d]
    assert totals[1]==1 and all(x==0 for x in totals[2:])
    exact=(HERE/'exact-checks-output.txt').read_text()
    assert 'PASS: 16 exact checks' in exact and '#0:' not in exact
    output={'status':'PASS','classification':'Finite bound and step validation; no uniform arithmetic estimate',
            'checks':counts,'Maxima_exact_checks':16,'integer_Mobius_convolution_checks':len(mu)-1,
            'N256_budget_step_relative_gain_above':'0.000443',
            'N256_physical_step_relative_gain_above':'0.0157',
            'new_Gram_solves':False,'independent_author_review':False,
            'source_sha256':digest(Path(__file__))}
    (HERE/'validation.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':
    main()
