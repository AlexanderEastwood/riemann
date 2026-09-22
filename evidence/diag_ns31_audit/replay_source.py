"""NS-31 diagnostic source normalization and projected feasible density matrix.
Uses high precision only to avoid float cancellation; still not a certificate.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any
import mpmath as mp
import numpy as np
from flint import ctx
sys.path[:0]=['evidence/v124/g2_schur_cancellation','evidence/diag_true_symbol']
from assembly_general import sequences,block
from cert import tomp
from pencil import beta_grid,Fe_grid
OUT=Path('evidence/diag_ns31_audit')

def q(v: Any,W: Any) -> Any:
    return (v.T*W*v)[0]

def run() -> None:
    mp.mp.dps=120; ctx.prec=1024
    data=json.loads(Path('evidence/v124/g2_source_certificate/source_polynomial_intervals.json').read_text())
    co=mp.matrix([mp.mpf(s.strip('[]').split('+/-')[0]) for s in data['projected_positive_coefficients']])
    u=mp.matrix([co[k]*(mp.sqrt(2) if k else 1) for k in range(65)]); u/=mp.norm(u)
    raw=co/mp.norm(co)
    _,b,d,_=sequences(3,264,1024); W64=tomp(block(list(range(65)),list(range(65)),'even',b,d),120)
    e,V=mp.eigsy(W64); ground=V[:,0]
    out: dict[str,Any]={'correct_sine':mp.nstr(mp.sqrt(1-(ground.T*u)[0]**2),20),
       'uncorrected_sine':mp.nstr(mp.sqrt(1-(ground.T*raw)[0]**2),20),
       'source_ground_overlap':mp.nstr(abs((ground.T*u)[0]),24),
       'source_energy_64':mp.nstr(q(u,W64),24)}
    N=256; W=tomp(block(list(range(N+1)),list(range(N+1)),'even',b,d),120)
    um=mp.matrix([u[k] if k<65 else mp.mpf(0) for k in range(N+1)])
    out['source_residual_256']=mp.nstr(mp.norm(W*um),24)
    payload=json.loads((OUT/'lp_l3.json').read_text())
    xs=np.concatenate([np.arange(.001,40,.002),np.arange(40.005,800,.005)])
    hs=np.where(xs<40,.002,.005); beta,L=beta_grid(3,xs); D=float(-beta.min())
    Fs=np.array([(-1)**n*Fe_grid(n,L,xs) for n in range(N+1)])
    edges=np.linspace(-D,0,21); sels=[(beta>=lo)&(beta<hi) for lo,hi in zip(edges[:-1],edges[1:])]
    Ms=[2*(Fs[:,s]*hs[s])@Fs[:,s].T for s in sels]
    mb=np.array([np.sum(hs[s]) for s in sels])/800
    uv=np.array([float(x) for x in um]); source_mass=np.array([uv@M@uv for M in Ms])
    states=[]
    for c in ('1.0','4.0'):
        v=mp.matrix(payload['weighted'][c]['v']); v/=mp.norm(v)
        overlap=(um.T*v)[0]; g=(v-overlap*um)/mp.sqrt(1-overlap**2)
        vf=np.array([float(x) for x in v]); gf=np.array([float(x) for x in g])
        mass=np.array([vf@M@vf for M in Ms]); gm=np.array([gf@M@gf for M in Ms])
        density_lower=(np.maximum(np.sqrt(mass)-float(abs(overlap))*np.sqrt(np.maximum(source_mass,0)),0)**2)/float(1-overlap**2)
        energy_bound=(q(v,W)+(2*abs(overlap)+overlap**2)*mp.norm(W*um))/(1-overlap**2)
        state={'c_raw':c,'source_overlap':mp.nstr(overlap,20),'raw_energy':mp.nstr(q(v,W),24),
               'projected_energy':mp.nstr(q(g,W),24),'energy_projection_upper':mp.nstr(energy_bound,24),
               'min_ratio':float(min(gm/mb)),'density_lower_ratio':float(min(density_lower/mb)),
               'density_lower_mass':density_lower.tolist(),'slack':(gm-mb).tolist(), 'v':[mp.nstr(x,30) for x in g]}
        states.append(state)
    alpha=mp.mpf('0.000001')
    mixed_lower=(1-float(alpha))*np.array(states[0]['density_lower_mass'])+float(alpha)*np.array(states[1]['density_lower_mass'])
    mixed_energy=(1-alpha)*mp.mpf(states[0]['projected_energy'])+alpha*mp.mpf(states[1]['projected_energy'])
    candidates=[]
    g0=mp.matrix(states[0]['v']); g4=mp.matrix(states[1]['v'])
    for eps in ('1e-7','1e-6','1e-5'):
        for sign in (-1,1):
            h=g0+sign*mp.mpf(eps)*g4; h/=mp.norm(h)
            hf=np.array([float(x) for x in h]); hm=np.array([hf@M@hf for M in Ms])
            candidates.append({'epsilon':str(sign*mp.mpf(eps)),'energy':mp.nstr(q(h,W),24),
                'min_ratio':float(min(hm/mb)), 'slack':(hm-mb).tolist(),
                'source_overlap':mp.nstr(abs((h.T*um)[0]),12),'v':[mp.nstr(x,30) for x in h]})
    feasible=[v for v in candidates if v['min_ratio']>1.0000001]
    out['pure_repair_trials']=[{k:v for k,v in row.items() if k!='v'} for row in candidates]
    out['feasible_projected_pure']=min(feasible,key=lambda v:float(v['energy']))
    out['projected_states']=states
    out['feasible_projected_mixture']={'weight_second':str(alpha),'energy':mp.nstr(mixed_energy,24),
         'density_triangle_min_ratio':float(min(mixed_lower/mb)),'density_triangle_slack':(mixed_lower-mb).tolist()}
    print(json.dumps({k:v for k,v in out.items() if k!='projected_states'},indent=2),flush=True)
    for s in states:
        print(json.dumps({k:v for k,v in s.items() if k not in ('v','slack','density_lower_mass')},indent=2),flush=True)
    (OUT/'source_projection.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    run()
