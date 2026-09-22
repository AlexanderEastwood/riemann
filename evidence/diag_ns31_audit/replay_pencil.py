"""NS-31 diagnostic precision-floor replay at existing lambda=6,8 N=96.
Reuses the original quadrature to isolate arithmetic precision, not quadrature error.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any
import numpy as np
import mpmath as mp
from flint import ctx
sys.path[:0]=['evidence/v124/g2_schur_cancellation','evidence/diag_true_symbol']
from assembly_general import sequences,block
from pencil import beta_grid,Fe_grid
from cert import tomp

def run(lam: int) -> None:
    N=96; rows=list(range(N+1)); xs=np.concatenate([np.arange(.001,40,.002),np.arange(40.005,4000,.01)])
    hs=np.where(xs<40,.002,.01); beta,L=beta_grid(lam,xs)
    F=np.array([(-1)**n*Fe_grid(n,L,xs) for n in rows]); Wm=2*(F*(np.maximum(-beta,0)*hs))@F.T
    ctx.prec=2048; _,b,d,_=sequences(lam,N+8,2048); Wb=block(rows,rows,'even',b,d)
    out=[]
    for dps in (120,180):
        W=tomp(Wb,dps); B=W+mp.matrix(Wm.tolist()); C=mp.cholesky(B); Ci=C**-1
        M=Ci*W*Ci.T; M=(M+M.T)/2
        nu=sorted(mp.eigsy(M,eigvals_only=True)); threshold=mp.mpf('1e-30'); count=sum(x<threshold for x in nu)
        row={'lambda':lam,'N':N,'dps':dps,'nu':[mp.nstr(x,24) for x in nu],
             'counts':{s:sum(x<mp.mpf(s) for x in nu) for s in ('1e-8','1e-16','1e-30')},
             'threshold_neighbors':[mp.nstr(nu[count-1],14),mp.nstr(nu[count],14)]}
        out.append(row); print(json.dumps({k:v for k,v in row.items() if k!='nu'}),'first',row['nu'][:10],flush=True)
    Path(f'evidence/diag_ns31_audit/pencil_l{lam}.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    for s in sys.argv[1:] or ['6','8']:
        run(int(s))
