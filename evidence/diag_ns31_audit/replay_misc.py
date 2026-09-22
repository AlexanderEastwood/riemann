"""NS-31 diagnostic spot checks of concentration, tail and displayed tables."""
from __future__ import annotations
import json
import math
import sys
from pathlib import Path
from typing import Any
import numpy as np
sys.path[:0]=['evidence/v124/g2_schur_cancellation','evidence/diag_true_symbol']
from pencil import beta_grid,Fe_grid

def run() -> None:
    out: dict[str,Any]={}
    for lam in (3,4,6,8):
        xs=np.concatenate([np.arange(.001,40,.002),np.arange(40.005,800,.005)])
        hs=np.where(xs<40,.002,.005); beta,L=beta_grid(lam,xs); D=float(-beta.min())
        edges=np.linspace(-D,0,21); mb=np.array([np.sum(hs[(beta>=lo)&(beta<hi)])/800 for lo,hi in zip(edges[:-1],edges[1:])])
        fe=np.linspace(-D,0,201); fm=np.array([np.sum(hs[(beta>=lo)&(beta<hi)])/800 for lo,hi in zip(fe[:-1],fe[1:])])
        sel=beta<0; bv=beta[sel]; weights=hs[sel]/800; order=np.argsort(bv); bv=bv[order]; weights=weights[order]
        right=np.searchsorted(bv,bv+D/20,side='right'); cum=np.r_[0,np.cumsum(weights)]
        mass=cum[right]-cum[np.arange(len(bv))]; top=int(np.argmax(mass))
        out[str(lam)]={'D':D,'histogram20_peak':float(max(mb)/(D/20)), 'histogram200_peak':float(max(fm)/(D/200)),
            'max_fixed_bin':float(max(mb)), 'sliding_concentration':float(max(mass)),
            'sliding_left':float(bv[top]), 'sliding_right':float(bv[top]+D/20)}
        if lam==4:
            rho=np.abs(xs*L/(2*math.pi)-np.rint(xs*L/(2*math.pi))); ring=np.minimum((rho*80).astype(int),39)
            rmin=np.array([min(beta[ring==k]) for k in range(40)])
            old=np.minimum.accumulate(rmin[::-1])[::-1]; correct=np.minimum.accumulate(rmin)
            F=np.array([Fe_grid(n,L,xs) for n in range(257)])
            T=np.eye(257)-2*(F*hs)@F.T
            def eta(g: Any) -> float:
                M=2*(F*(g[ring]*hs))@F.T-D*T
                return max(0.,-float(np.linalg.eigvalsh(M)[0]))
            out[str(lam)]['comb']={'old_profile':old.tolist(),'correct_centered_profile':correct.tolist(),
                'old_negative_weight_min':float(min(old[:-1]-old[1:])), 'old_eta':eta(old),'correct_eta':eta(correct)}
        print(lam,json.dumps(out[str(lam)]),flush=True)
    for lam in (4,6,8):
        best=(float('inf'),0.)
        for start in range(40000,1000000,40000):
            xs=np.arange(start+.025,start+40000,.05); b,_=beta_grid(lam,xs); i=int(np.argmin(b))
            if b[i]<best[0]: best=(float(b[i]),float(xs[i]))
        out[str(lam)]['tail_beyond40000']={'minimum_sample':best[0],'frequency':best[1]}
        print('TAIL',lam,best,flush=True)
    Path('evidence/diag_ns31_audit/misc.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    run()
