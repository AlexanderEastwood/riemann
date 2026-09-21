"""Fresh outward certificate for shifted scalar-tail cutoff thresholds."""
import json
from pathlib import Path
from assembly_general import arb,ctx,prime_bound
ctx.prec=256
rows=[]
for lam in (5,6,8):
    L=2*arb(lam).log();P=prime_bound(lam);h=(L/4).sinh()**2
    RL=arb(1)/lam/(1-arb(1)/lam**4)
    assert arb(1)>=arb(1)/4+RL
    for parity in ('even','odd'):
        for ds in ('0','0.001','1','3','8'):
            shift=arb(ds)
            def g(N):
                t=2*arb.pi()*(N+1)/L
                E=1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
                kap=P+2/t
                if parity=='odd':kap+=arb.pi()/2+4*h*L/(arb.pi()**2*N)
                return (arb(N+1)/L).log()-E-kap+shift
            lo=hi=1
            while not g(hi)>0:hi*=2
            while lo<hi:
                mid=(lo+hi)//2
                if g(mid)>0:hi=mid
                elif g(mid)<0:lo=mid+1
                else:raise ArithmeticError('Indeterminate threshold')
            assert g(lo)>0
            if lo>1:assert g(lo-1)<0
            rows.append({'lambda':lam,'parity':parity,'shift_exact':ds,'first_N_at_least_one':lo,'positive_gate':g(lo).str(55),'preceding_negative_gate':g(lo-1).str(55) if lo>1 else None})
Path(__file__).with_name('cutoff_thresholds.json').write_text(json.dumps({'bits':256,'c':0,'scope':'Minimal remote scalar-gate cutoff only; not a complete-form certificate','thresholds':rows},indent=2)+'\n')
print(json.dumps(rows,indent=2))
