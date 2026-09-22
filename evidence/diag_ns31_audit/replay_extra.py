"""NS-31 diagnostic checks: independent tail values and c=.5 infeasibility rays."""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any
import numpy as np
import mpmath as mp
from flint import ctx
sys.path[:0]=['evidence/v124/g2_schur_cancellation','evidence/diag_true_symbol','evidence/diag_ns31_audit']
from assembly_general import sequences,block,pairs
from pencil import beta_grid,Fe_grid
from replay_lp import solve

def run() -> None:
    mp.mp.dps=50
    out: dict[str,Any]={'tail':[],'infeasible_half':[]}
    for lam,xi in [(6,'152359.72500188358'),(8,'130060.42500058559')]:
        x=mp.mpf(xi); L=2*mp.log(lam); c=mp.mpf('.5')+1j*x
        beta=mp.re(mp.digamma(mp.mpf('1.25')+1j*x/2))-mp.log(mp.pi)-2*sum(mp.log(p)/mp.sqrt(m)*mp.cos(x*mp.log(m)) for m,p in pairs(lam))+2*mp.re((mp.exp(c*L)-1)/c)
        out['tail'].append({'lambda':lam,'xi':xi,'beta_mpmath':mp.nstr(beta,40)})
    L=2*mp.log(4)
    out['pole_transfer_constant_mode']=mp.nstr(2/L*mp.quad(lambda t:(L-t)*mp.exp(-t/2),[0,L]),40)
    for lam in (3,4,6,8):
        N=256; xs=np.concatenate([np.arange(.001,40,.002),np.arange(40.005,800,.005)]); hs=np.where(xs<40,.002,.005)
        beta,Lf=beta_grid(lam,xs); D=float(-beta.min()); rows=list(range(N+1))
        F=np.array([(-1)**n*Fe_grid(n,Lf,xs) for n in rows]); edges=np.linspace(-D,0,21)
        Ms=[2*(F[:,s]*hs[s])@F[:,s].T/(D/20) for s in [(beta>=lo)&(beta<hi) for lo,hi in zip(edges[:-1],edges[1:])]]
        bits=2048 if lam>=6 else 1024; ctx.prec=bits; _,b,d,_=sequences(lam,N+8,bits); Wb=block(rows,rows,'even',b,d)
        W=np.array([[float(Wb[i,j].mid()) for j in rows] for i in rows]); W=(W+W.T)/2
        r=np.full(20,.5/D); ans=solve(W,Ms,r,[0,.01,.1]); y=np.array(ans['y']); y/=sum(y)
        gap=float(y@r-np.linalg.eigvalsh(sum(yb*M for yb,M in zip(y,Ms)))[-1])
        out['infeasible_half'].append({'lambda':lam,'normalized_y':y.tolist(),'infeasibility_gap':gap})
        print(lam,'c=.5 infeasibility gap',gap,flush=True)
    print(json.dumps(out,indent=2),flush=True)
    Path('evidence/diag_ns31_audit/extra.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    run()
