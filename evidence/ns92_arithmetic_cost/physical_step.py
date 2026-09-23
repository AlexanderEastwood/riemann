"""Independently integrate the complete NS92 endpoint-only step, including tail."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
from flint import arb, ctx
from certify_cost import ROOT, digest, mobius


def parameters(c: list[arb], alpha: arb, log_t: arb) -> tuple[arb, arb, arb]:
    u = alpha-sum(c,arb(0))/2
    v = sum((z*(arb(k)/(2*arb.pi())).log() for k,z in enumerate(c,1)),arb(0))/2
    bound = sum((k*abs(z) for k,z in enumerate(c,1)),arb(0))/6
    return u,u*log_t+v,bound


def evaluate(old: dict[str, Any], scalar: dict[str, Any], stop: int) -> dict[str, str]:
    n = old['N']
    c = [arb(z) for z in old['optimal_coefficients']]+[arb(0)]*n
    mu = mobius(2*n)
    e = [arb(0)]*n+[-mu[k]*(arb(2*n)/k).log() for k in range(n+1,2*n+1)]
    e[n-1] = -n*sum((z/k for k,z in enumerate(e,1) if k!=n),arb(0))
    assert sum((z/k for k,z in enumerate(e,1)),arb(0)).contains(0)
    f = [-z for z in e]  # alpha=0, -sum f*a = the trial direction F.
    logs = [arb(0)]+[arb(k).log() for k in range(1,stop+1)]
    dr,df = [arb(0) for _ in range(stop)],[arb(0) for _ in range(stop)]
    dr[1] = arb(1)
    for k in range(1,2*n+1):
        for m in range(k,stop,k):
            dr[m] += c[k-1]
            df[m] += f[k-1]
    eta = sum((z/k for k,z in enumerate(c,1)),arb(0))
    # The direction's eta is exactly zero by its defining coefficient rule.
    ar,br,af,bf = arb(0),arb(0),arb(0),arb(0)
    er,ef,cross = eta**2,arb(0),arb(0)  # whole exterior 0<t<1.
    for m in range(1,stop):
        lo,hi = logs[m],logs[m+1]
        ar += dr[m];br += dr[m]*lo
        af += df[m];bf += df[m]*lo
        h,h2 = hi-lo,(hi*hi-lo*lo)/2
        i0 = arb(1)/(m*(m+1))
        i1 = (lo+1)/m-(hi+1)/(m+1)
        i2 = (lo*lo+2*lo+2)/m-(hi*hi+2*hi+2)/(m+1)
        er += eta**2-2*eta*(ar*h2-br*h)+ar**2*i2-2*ar*br*i1+br**2*i0
        if m<n:
            assert af.contains(0) and bf.contains(0)
            continue
        ef += af**2*i2-2*af*bf*i1+bf**2*i0
        cross += -eta*(af*h2-bf*h)+ar*af*i2-(ar*bf+af*br)*i1+br*bf*i0
    ur,qr,bb_r = parameters(c,arb(1),logs[stop])
    uf,qf,bb_f = parameters(f,arb(0),logs[stop])
    mr,mf = (qr**2+2*ur*qr+2*ur**2)/stop,(qf**2+2*uf*qf+2*uf**2)/stop
    rr,rf = bb_r**2/(3*arb(stop)**3),bb_f**2/(3*arb(stop)**3)
    er += mr+arb(0,2*(mr*rr).sqrt()+rr)
    ef += mf+arb(0,2*(mf*rf).sqrt()+rf)
    cross += (qr*qf+ur*qf+uf*qr+2*ur*uf)/stop+arb(0,(mr*rf).sqrt()+(mf*rr).sqrt()+(rr*rf).sqrt())
    energy = arb(old['values']['E_N'])
    upper = arb(scalar['values']['complete_cost_upper'])
    lower = arb(scalar['finite_gain']['inherited_lower_numerator'])
    step = arb(1)/512
    lower_gain = 2*step*lower-step**2*upper
    actual_gain = 2*step*cross-step**2*ef
    assert er.overlaps(energy)
    assert cross.overlaps(arb(scalar['finite_gain']['inherited_numerator_for_validation_only']))
    assert ef > 0 and ef < upper
    assert actual_gain > lower_gain and actual_gain > 0
    assert (cross/8-ef/256)/energy > arb('0.015')
    assert er-actual_gain > 0 and er-actual_gain < er
    return {k:v.str(65) for k,v in {
        'old_energy':er,'complete_endpoint_direction_cost':ef,
        'complete_gain_numerator':cross,'scalar_cost_upper':upper,
        'rational_step_lower_gain':lower_gain,
        'rational_step_actual_gain':actual_gain,
        'rational_step_actual_relative_gain':actual_gain/energy,
        'new_complete_error':er-actual_gain,
        'larger_rational_step_actual_relative_gain':(cross/8-ef/256)/energy,
        'larger_rational_step_new_error':er-cross/8+ef/256,
    }.items()}


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--bits',type=int,required=True)
    p.add_argument('--stop',type=int,default=262144)
    p.add_argument('--cutoff-replay',action='store_true')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    suffix='cutoff-384bits' if args.cutoff_replay else f'{args.bits}bits'
    inp=ROOT/f'evidence/ns89_upper_normalization/check-{suffix}.json'
    scalar=Path(__file__).parent/f'cost-{suffix}.json'
    old=next(r for r in json.loads(inp.read_text())['rows'] if r['N']==256)
    cost=next(r for r in json.loads(scalar.read_text())['rows'] if r['N']==256)
    values=evaluate(old,cost,args.stop)
    output={'classification':'Certified full physical validation of a fixed rational endpoint-only step; no uniform estimate',
            'precision_bits':args.bits,'N':256,'physical_cutoff':args.stop,'step':'1/512','larger_physical_step':'1/16','values':values,
            'source_sha256':digest(Path(__file__)),
            'dependencies':{str(p.relative_to(ROOT)):digest(p) for p in [inp,scalar,Path(__file__).parent/'certify_cost.py']}}
    args.output.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
