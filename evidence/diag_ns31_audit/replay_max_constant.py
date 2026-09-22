"""NS-31 diagnostic max achievable uniform 20-bin c, by column generation.
LP provides a feasible mixed state; top-eigenvalue dual provides an upper estimate.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any
import numpy as np
from scipy.optimize import linprog
sys.path[:0]=['evidence/v124/g2_schur_cancellation','evidence/diag_true_symbol']
from pencil import beta_grid,Fe_grid

def run(lam: int) -> dict[str,Any]:
    N=256; xs=np.concatenate([np.arange(.001,40,.002),np.arange(40.005,800,.005)]); hs=np.where(xs<40,.002,.005)
    beta,L=beta_grid(lam,xs); D=float(-beta.min()); F=np.array([(-1)**n*Fe_grid(n,L,xs) for n in range(N+1)])
    edges=np.linspace(-D,0,21)
    Ms=np.array([40*(F[:,s]*hs[s])@F[:,s].T for s in [(beta>=lo)&(beta<hi) for lo,hi in zip(edges[:-1],edges[1:])]])
    # Ms = 20 times MASS; each requirement is tr(Ms[b] X) >= c.
    dic=np.eye(N+1); md=np.array([np.diag(M) for M in Ms])
    for it in range(500):
        nd=md.shape[1]
        lp=linprog(np.r_[np.zeros(nd),-1],A_ub=np.column_stack([-md,np.ones(20)]),b_ub=np.zeros(20),
             A_eq=np.array([np.r_[np.ones(nd),0]]),b_eq=[1.],bounds=[(0,None)]*(nd+1),method='highs',
             options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:
            raise RuntimeError(lp.message)
        y=-lp.ineqlin.marginals; w,V=np.linalg.eigh(np.einsum('b,bij->ij',y,Ms)); v=V[:,-1]
        lower=float(lp.x[-1]); upper=float(w[-1]); gap=upper-lower
        if it%25==0 or gap<1e-6:
            print(lam,it,lower,upper,flush=True)
        if gap<1e-6 or (upper<.5 and lower>.49) or it==499:
            return {'lambda':lam,'lower':lower,'upper':upper,'dual_y':y.tolist(),
                'mixture_weights':lp.x[:-1].tolist(),'mixture_vectors':dic.T.tolist(),
                'constraint_slack':(md@lp.x[:-1]-lower).tolist(),'iterations':it}
        dic=np.column_stack([dic,v]); md=np.column_stack([md,np.array([v@M@v for M in Ms])])
    return {'lambda':lam,'lower':lower,'upper':upper,'dual_y':y.tolist(),'iterations':it}

if __name__=='__main__':
    out=[]
    for lam in (4,8):
        out.append(run(lam))
    Path('evidence/diag_ns31_audit/max_constant.json').write_text(json.dumps(out,indent=2)+'\n')
