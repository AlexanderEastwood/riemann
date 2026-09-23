"""Independent complete physical P_N(2) and residual autocorrelation checks."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any
from flint import arb,ctx

HERE=Path(__file__).resolve().parent


def evaluate(c: list[arb], stop: int) -> dict[str,str]:
    n=len(c);assert stop>2*n
    logs=[arb(0)]+[arb(k).log() for k in range(1,stop+1)]
    eta=sum((x/j for j,x in enumerate(c,1)),arb(0))
    delta=[arb(0) for _ in range(stop+1)];delta[1]=arb(1)
    for j,x in enumerate(c,1):
        for m in range(j,stop+1,j):delta[m]+=x
    b1,z1,b2,z2=arb(0),arb(0),arb(0),arb(0)
    a1,a2=-eta,-eta/2
    correlation=eta**2/2;potential=arb(0)
    for k in range(1,stop):
        l,r=logs[k],logs[k+1]
        b1+=delta[k];z1-=delta[k]*l
        if k%2==0:
            b2+=delta[k//2];z2-=delta[k//2]*l
        i0=arb(1)/(k*(k+1))
        i1=(l+1)/k-(r+1)/(k+1)
        i2=(l*l+2*l+2)/k-(r*r+2*r+2)/(k+1)
        correlation+=a1*a2+(a1*b2+a2*b1)*(r*r-l*l)/2
        correlation+=(a1*z2+a2*z1)*(r-l)+b1*b2*i2+(b1*z2+b2*z1)*i1+z1*z2*i0
        if k>=2:
            potential+=a1*((r*r-l*l)/2-logs[2]*(r-l))
            potential+=b1*(i2-logs[2]*i1)+z1*(i1-logs[2]*i0)
    slope=1-sum(c,arb(0))/2
    constant=sum((x*(logs[j]-(2*arb.pi()).log()) for j,x in enumerate(c,1)),arb(0))/2
    rem=sum((j*abs(x) for j,x in enumerate(c,1)),arb(0))/6
    q=slope*logs[stop]+constant;q2=q-slope*logs[2]
    main1=(q*q+2*slope*q+2*slope*slope)/stop
    main2=(q2*q2+2*slope*q2+2*slope*slope)/stop
    error=rem**2/(3*arb(stop)**3)
    crad=2*(main1*error).sqrt()+(main2*error).sqrt()+2*error
    correlation+=(q*q2+slope*(q+q2)+2*slope*slope)/stop+arb(0,crad)
    l=logs[stop]-logs[2]
    prad=rem*(l/2+arb(1)/4)/arb(stop)**2
    potential+=(q*l+q+slope*l+2*slope)/stop+arb(0,prad)
    vals={'potential_at_two':potential,'autocorrelation_at_two':correlation,
          'dilation_defect':potential-correlation,'correlation_tail_radius':crad,'potential_tail_radius':prad}
    return {k:v.str(65) for k,v in vals.items()}


def main() -> None:
    p=argparse.ArgumentParser();p.add_argument('--bits',type=int,required=True)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--stop',type=int,default=65536)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args();ctx.prec=a.bits
    source=json.loads(a.input.read_text());rows:list[dict[str,Any]]=[]
    for row in source['rows']:
        vals=evaluate([arb(x) for x in row['coefficients']],a.stop)
        for key in ['potential_at_two','autocorrelation_at_two','dilation_defect']:
            assert arb(vals[key]).overlaps(arb(row['values'][key])),(row['N'],key)
        assert not arb(vals['dilation_defect']).contains(0)
        rows.append({'N':row['N'],'values':vals,'gates':{'complete_physical_vs_Gram':True,'physical_defect_nonzero':True}})
        print(json.dumps({'N':row['N'],'bits':a.bits,'T':a.stop,'physical_defect':vals['dilation_defect']}),flush=True)
    a.output.write_text(json.dumps({'classification':'Certified complete physical identity checks; no cofinal lower bound',
        'precision_bits':a.bits,'physical_stop':a.stop,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),'rows':rows},indent=2)+'\n')


if __name__=='__main__':main()
