"""Freeze NS-42 N=48 generalized pencil vectors. DIAGNOSTIC, NOT A CERTIFICATE."""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any
import mpmath as mp
import numpy as np
from flint import ctx
ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT/'evidence/v124/g2_schur_cancellation'), str(ROOT/'evidence/diag_true_symbol')]
from assembly_general import block, sequences
from cert import tomp
from pencil import beta_grid, Fe_grid
from pencil_odd import Fo_grid
OUT = Path(__file__).resolve().parent

def run(lam: int, n: int = 48, dps: int = 150) -> None:
    mp.mp.dps = dps
    xs = np.concatenate([np.arange(.001,40,.002), np.arange(40.005,4000,.01)])
    hs = np.where(xs<40,.002,.01)
    beta, length = beta_grid(lam, xs)
    ctx.prec = 1024
    _, b, d, _ = sequences(lam, n+8, 1024)
    for parity in ('even','odd'):
        rows = list(range(n+1)) if parity=='even' else list(range(1,n+1))
        fe = Fe_grid if parity=='even' else Fo_grid
        f = np.array([(-1)**j*fe(j,length,xs) for j in rows])
        wm = 2*(f*(np.maximum(-beta,0)*hs))@f.T
        w = tomp(block(rows,rows,parity,b,d), dps)
        wp = w + mp.matrix(wm.tolist())
        chol = mp.cholesky(wp); ci = chol**-1
        middle = ci*w*ci.T; middle=(middle+middle.T)/2
        nu, u = mp.eigsy(middle)
        data: dict[str, Any] = {'lambda':lam,'N':n,'parity':parity,'dps':dps,'bits':1024,'indices':rows,
            'Wminus_scope':'original float grid xi=.001..4000, steps .002/.01, no tail charge',
            'basis':'e0=1/sqrt(2a); en=(-1)^n/sqrt(a) cos(n*pi*x/a) even or sin(n*pi*x/a) odd; zero outside (-a,a)',
            'vectors':[]}
        for k in range(3):
            vec = ci.T*u[:,k]; vec /= mp.norm(vec)
            if vec[0]<0: vec=-vec
            q = (vec.T*w*vec)[0]; qp=(vec.T*wp*vec)[0]
            residual = mp.norm(w*vec-nu[k]*wp*vec)
            data['vectors'].append({'k':k,'nu':mp.nstr(nu[k],100),'q':mp.nstr(q,100),'qplus':mp.nstr(qp,100),
                'pencil_residual':mp.nstr(residual,12),'norm2':mp.nstr((vec.T*vec)[0],100),
                'coefficients':[mp.nstr(v,130) for v in vec]})
        path=OUT/f'vectors_l{lam}_{parity}.json'; path.write_text(json.dumps(data,indent=2)+'\n')
        print(lam,parity,[(v['k'],mp.nstr(mp.mpf(v['q']),12),mp.nstr(mp.mpf(v['nu']),12)) for v in data['vectors']],flush=True)

if __name__=='__main__':
    for arg in sys.argv[1:] or ['3','4']:
        run(int(arg))
