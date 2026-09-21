"""Self-similarity test in u = xi*L/(2 pi): ground mass per lattice cell, and beta_a at fixed u, across lambda."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
from beta_true import make_beta_true
cells=[(0,0.5),(0.5,1.5),(1.5,2.5),(2.5,3.5),(3.5,4.5),(4.5,6.5),(6.5,10.5)]
us=[0.25,0.5,0.75,1.0,1.25,1.5,2.0,2.5,3.0,4.0]
rows_mass=[]; rows_beta=[]
for lam in (3,4,6,8):
    N=120; bits=2048 if lam>=6 else 1024; dps=300 if lam>=6 else 220
    ctx.prec=bits; Lq,b,d,a=sequences(lam,N+8,bits); rows=list(range(N+1)); mp.mp.dps=dps
    E,Q=mp.eigsy(tomp(block(rows,rows,'even',b,d),dps)); i=min(range(len(E)),key=lambda k:E[k])
    v=np.array([float(Q[k,i]) for k in range(N+1)]); L=2*math.log(lam); nmax=int(np.max(np.nonzero(np.abs(v)>1e-13)))+1
    def Ff(xi):
        out=v[0]/np.sqrt(L)*2*np.sin(xi*L/2)/xi
        for n in range(1,nmax):
            w=2*np.pi*n/L; out+=((-1)**n)*v[n]*np.sqrt(2/L)*(np.sin((w-xi)*L/2)/(w-xi)+np.sin((w+xi)*L/2)/(w+xi))
        return out/np.sqrt(2*np.pi)
    h=0.002; xs=np.arange(h/2,60,h); f2=Ff(xs)**2; u=xs*L/(2*np.pi)
    rows_mass.append((lam,[2*np.sum(f2[(u>=a_)&(u<b_)])*h for a_,b_ in cells]))
    beta,_=make_beta_true(lam); mp.mp.dps=15
    rows_beta.append((lam,[float(beta(uu*2*np.pi/L)) for uu in us], [abs(v[k]) for k in range(6)]))
print("GROUND MASS per lattice cell (u = xi L/2pi):")
print("%-4s "%"lam"+" ".join("%-10s"%("[%g,%g)"%c) for c in cells))
for lam,m in rows_mass: print("%-4d "%lam+" ".join("%-10.4f"%x for x in m))
print("\nSYMBOL beta_a at fixed u = xi L/2pi:")
print("%-4s "%"lam"+" ".join("%-8s"%("u=%g"%uu) for uu in us))
for lam,bv,vv in rows_beta: print("%-4d "%lam+" ".join("%-8.3f"%x for x in bv))
print("\nGROUND coefficients |v_0..v_5| (lattice modes):")
for lam,bv,vv in rows_beta: print("%-4d "%lam+" ".join("%-8.4f"%x for x in vv))
