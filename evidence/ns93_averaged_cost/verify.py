"""Replay bindings and compare finite cost identities at both precisions."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from typing import Any
from flint import arb, ctx
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]


def read(name: str) -> dict[str, Any]:
    return json.loads((HERE/name).read_text())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ctx.prec=384
    files=['cost-256bits.json','cost-384bits.json','cost-sieve-replay.json']
    data=[read(n) for n in files]
    counts={'precision_overlaps':0,'sieve_overlaps':0,'independent_NS92_overlaps':0}
    for d in data:
        assert d['source_sha256']==digest(HERE/'check_cost.py')
        assert d['mobius_source_sha256']==digest(ROOT/'evidence/ns92_arithmetic_cost/certify_cost.py')
        for row in d['rows']:
            v={k:arb(x) for k,x in row['values'].items()}
            assert (v['diagonal']+v['signed_off_diagonal']).overlaps(v['signed_square_cost'])
            assert v['diagonal']<v['proved_diagonal_upper']
            if row['N']>=2048:
                assert v['absolute_product_majorant']>v['proved_absolute_lower_for_N_ge_2048']
    for left,right,key in [(data[0],data[1],'precision_overlaps'),(data[1],data[2],'sieve_overlaps')]:
        for group in ['rows','blocks']:
            for a,b in zip(left[group],right[group],strict=True):
                for name,value in a['values'].items():
                    assert arb(value).overlaps(arb(b['values'][name])),name
                    counts[key]+=1
    prior=json.loads((ROOT/'evidence/ns92_arithmetic_cost/cost-384bits.json').read_text())
    lookup={r['N']:r for r in data[1]['rows']}
    for r in prior['rows']:
        assert arb(r['values']['weighted_Mobius_tail_square_sum']).overlaps(arb(lookup[r['N']]['values']['signed_square_cost']))
        counts['independent_NS92_overlaps']+=1
    exact=(HERE/'checks-output.txt').read_text()
    geometry=(ROOT/'evidence/ns94_circle_inversion/checks-output.txt').read_text()
    assert 'PASS: 8 exact checks' in exact and ' -- an error.' not in exact
    assert 'PASS: 23 exact checks' in geometry and ' -- an error.' not in geometry
    out={'status':'PASS','scope':'Finite identities, complete analytic inequality audited by author only; no cofinal gain',
         'checks':counts,'arithmetic_Maxima_checks':8,'geometry_Maxima_checks':23,
         'direct_quadratic_sizes':[16,32,64],'no_physical_cutoff':True,
         'no_new_Gram_solve':True,'source_sha256':digest(Path(__file__))}
    (HERE/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
