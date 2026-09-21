"""Diagnostic: how much of W^-[0,0] and W^-[0,1] lies beyond the pencil grid (xi > 4000), lambda = 4, 8.
Coarse grid to 2e5 (the negative set of beta_a can extend to ~ 2 pi exp(sup r_a)).  Run from the repo root."""
import sys, math
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np
from pencil import beta_grid, Fe_grid
for lam in (4,8):
    xs=np.arange(4000.025,2e5,0.05); h=0.05
    beta,L=beta_grid(lam,xs); neg=np.maximum(-beta,0.0)
    F0=Fe_grid(0,L,xs); F1=Fe_grid(1,L,xs)
    t00=2*np.sum(neg*F0*F0)*h; t01=-2*np.sum(neg*F0*F1)*h   # (-1)^{0+1} sign to block() basis
    xs2=np.concatenate([np.arange(0.001,40,0.002),np.arange(40.005,4000,0.01)]); h2=np.where(xs2<40,0.002,0.01)
    b2,_=beta_grid(lam,xs2); n2=np.maximum(-b2,0.0); G0=Fe_grid(0,L,xs2); G1=Fe_grid(1,L,xs2)
    m00=2*np.sum(n2*G0*G0*h2); m01=-2*np.sum(n2*G0*G1*h2)
    print(f"lambda={lam}: negative measure in [4000,2e5] = {2*np.sum(beta<0)*h:.1f}, last beta<0 at {xs[beta<0].max() if np.any(beta<0) else 0:.0f}; "
          f"W^-[0,0]: main {m00:.6f} + beyond-grid {t00:.2e} ({t00/m00:.1e} rel);  W^-[0,1]: main {m01:.6f} + {t01:.2e} ({abs(t01/m01):.1e} rel)")
