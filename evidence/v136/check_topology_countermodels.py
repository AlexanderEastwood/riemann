"""Exact rational checks of countermodels, not arithmetic Weil numerics."""
from fractions import Fraction as F
from pathlib import Path
import json

rows=[]
for m in [2,4,16,64,256]:
    # In c_00: f=e_1, h=e_1-(1/m)sum_{j=2}^{m+1} e_j, w=f-h.
    f=[F(1)]+[F(0)]*m
    h=[F(1)]+[-F(1,m)]*m
    w=[x-y for x,y in zip(f,h)]
    n2=lambda x:sum(t*t for t in x)
    q=lambda x: -sum(x)**2
    assert sum(h)==0 and q(h)==0
    assert n2(w)==F(1,m) and q(w)==-1 and q(w)/n2(w)==-m
    # A_n=-11^T has the same dense limiting radical, exact compression
    # consistency, nonzero eigenvalue -n and strong-resolvent limit zero.
    n=m+1
    # For z=i and f=e_1 the squared resolvent error is n/(n^2+1).
    resolvent_error_squared=F(n,n*n+1)
    assert resolvent_error_squared<F(1,n)
    rows.append({'m':m,'radical_sum':str(sum(h)),
                 'approximation_error_squared':str(n2(w)),
                 'negative_form':str(q(w)),
                 'negative_rayleigh':str(q(w)/n2(w)),
                 'matrix_dimension':n,'lower_edge':-n,
                 'resolvent_error_on_e1_squared':str(resolvent_error_squared)})

result={'status':'all exact rational identities passed',
        'scope':'abstract support-consistent rank-one countermodels; not Weil matrices',
        'identities':rows,
        'positive_counterpart':'Replacing the minus sign by plus preserves the kernel and strong-resolvent limit, but makes every matrix nonnegative.',
        'interpretation':'Dense radicals and strong-resolvent collapse alone do not determine sign. Uniform semiboundedness separates the two support-consistent families.'}
Path(__file__).with_name('countermodel_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
