"""NS-31 diagnostic only: replay archived dual optimization, save all primal slacks.
Run from repository root. No certificate; constraints remain 20 grid bins.
"""
from __future__ import annotations
import json
import math
import sys
import time
from pathlib import Path
from typing import Any
import numpy as np
from scipy.optimize import minimize, linprog
from flint import ctx
sys.path[:0] = ['evidence/v124/g2_schur_cancellation', 'evidence/diag_true_symbol']
from assembly_general import sequences, block
from pencil import beta_grid, Fe_grid
OUT = Path('evidence/diag_ns31_audit')

def solve(W: Any, Ms: Any, r: Any, starts: list[float]) -> dict[str, Any]:
    def negphi(y: Any) -> tuple[Any, Any]:
        A = W - sum(yb*M for yb, M in zip(y, Ms))
        w, V = np.linalg.eigh(A)
        v = V[:, 0]
        return -(w[0]+y@r), -(r-np.array([v@M@v for M in Ms]))
    best: Any = None
    for start in starts:
        res = minimize(negphi, np.full(len(r), start), jac=True, method='L-BFGS-B',
                       bounds=[(0,None)]*len(r), options={'maxiter':3000,'ftol':1e-15,'gtol':1e-12})
        if best is None or res.fun < best.fun:
            best = res
    A = W - sum(yb*M for yb, M in zip(best.x, Ms))
    w, V = np.linalg.eigh(A)
    v = V[:, 0]
    masses = np.array([v@M@v for M in Ms])
    return {'dual':float(-best.fun), 'energy':float(v@W@v), 'min_ratio':float(np.min(masses/r)),
            'slack':(masses-r).tolist(), 'masses':masses.tolist(), 'required':r.tolist(),
            'y':best.x.tolist(), 'v':v.tolist(), 'success':bool(best.success), 'message':str(best.message)}

def run(lam: int) -> None:
    N=256; XI=800.; nb=20
    xs=np.concatenate([np.arange(.001,40,.002),np.arange(40.005,XI,.005)])
    hs=np.where(xs<40,.002,.005)
    beta,L=beta_grid(lam,xs); D=float(-beta.min())
    ctx.prec=2048 if lam>=6 else 1024
    _,b,d,_=sequences(lam,N+8,ctx.prec); rows=list(range(N+1))
    Wb=block(rows,rows,'even',b,d)
    W=np.array([[float(Wb[i,j].mid()) for j in rows] for i in rows]); W=(W+W.T)/2
    Fs=np.array([(-1)**n*Fe_grid(n,L,xs) for n in rows])
    edges=np.linspace(-D,0,nb+1)
    sels=[(beta>=lo)&(beta<hi) for lo,hi in zip(edges[:-1],edges[1:])]
    Ms=[2*(Fs[:,s]*hs[s])@Fs[:,s].T for s in sels]
    mb=np.array([np.sum(hs[s]) for s in sels])/XI
    payload: dict[str,Any]={'lambda':lam,'N':N,'D':D,'mb':mb.tolist(),'uniform':{},'weighted':{}}
    for c in (.01,.03,.05,.1,.2,.3):
        item=solve(W,[M/(D/nb) for M in Ms],np.full(nb,c/D),[0,.01,.1])
        payload['uniform'][str(c)]=item
        print(lam,'uniform',c,'dual',item['dual'],'energy',item['energy'],'min ratio',item['min_ratio'],'slack',min(item['slack']),flush=True)
    for c in (.1,.2,.5,1.,2.,4.):
        item=solve(W,Ms,c*mb,[0,.01,.1,1.])
        payload['weighted'][str(c)]=item
        print(lam,'weighted',c,'dual',item['dual'],'energy',item['energy'],'min ratio',item['min_ratio'],'slack',min(item['slack']),flush=True)
    if lam==3:
        raw=json.loads(Path('evidence/v124/g2_source_certificate/source_polynomial_intervals.json').read_text())['projected_positive_coefficients']
        u=np.zeros(N+1); u[:len(raw)]=[float(s.strip('[]').split('+/-')[0]) for s in raw]
        u[1:]*=math.sqrt(2); u/=np.linalg.norm(u)
        wu=W@u; Eu=float(u@wu); residual=float(np.linalg.norm(wu))
        v=np.array(payload['weighted']['1.0']['v']); ov=float(v@u)
        g=(v-ov*u)/math.sqrt(1-ov**2)
        gm=np.array([g@M@g for M in Ms])
        lower=(np.maximum(np.sqrt(np.array([v@M@v for M in Ms]))-abs(ov)*np.sqrt(np.maximum(np.array([u@M@u for M in Ms]),0)),0)**2)/(1-ov**2)
        P=np.linalg.qr(np.column_stack([u,np.eye(N+1)]))[0][:,1:]
        proj=solve(P.T@W@P,[P.T@M@P for M in Ms],mb,[0,.01,.1,1.])
        vp=P@np.array(proj['v']); proj['v']=vp.tolist()
        # A slightly stronger requirement supplies a feasible c'=1 witness despite optimizer noise.
        strong=solve(P.T@W@P,[P.T@M@P for M in Ms],1.001*mb,[0,.01,.1,1.])
        vs=P@np.array(strong['v']); strong['v']=vs.tolist()
        strong['ratio_at_one']=float(min((vs@M@vs)/m for M,m in zip(Ms,mb)))
        payload['projection']={'overlap':ov,'source_energy':Eu,'source_residual':residual,
            'projected_energy':float(g@W@g),'projected_ratio':float(min(gm/mb)),
            'bin_triangle_lower_ratio':float(min(lower/mb)), 'projected_slack':(gm-mb).tolist(),
            'energy_bound':float((float(v@W@v)+(2*abs(ov)+ov**2)*residual)/(1-ov**2)),
            'optimized':proj,'stronger_feasible_witness':strong}
        print('PROJECTION',json.dumps({k:v for k,v in payload['projection'].items() if k not in ('optimized','stronger_feasible_witness')}),flush=True)
        print('PROJECTED STRONG WITNESS',strong['energy'],strong['ratio_at_one'],flush=True)
    (OUT/f'lp_l{lam}.json').write_text(json.dumps(payload,indent=2)+'\n')

if __name__=='__main__':
    for value in sys.argv[1:] or ['3','4','6','8']:
        run(int(value))
