"""The race at the first zero: depth/width of beta_a's lobe near gamma_1 (and gamma_2)
vs the ground state's Fourier mass and negative-level energy there, lambda = 3,4,6,8."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
from beta_true import make_beta_true
G=[14.134725,21.022040]
print("%-4s %-7s %-8s | %-9s %-7s %-7s %-8s | %-10s %-10s %-11s | %-10s"%("lam","L","eps_N","lobe@g1","depth","width","w*L/2pi","mass|x-g1|<1","mass lobe","E_neg lobe","mass xi>10"))
for lam in (3,4,6,8):
    t=time.time(); N=120; bits=2048 if lam>=6 else 1024; dps=300 if lam>=6 else 220
    ctx.prec=bits; Lq,b,d,a=sequences(lam,N+8,bits); rows=list(range(N+1)); mp.mp.dps=dps
    E,Q=mp.eigsy(tomp(block(rows,rows,'even',b,d),dps)); i=min(range(len(E)),key=lambda k:E[k]); eps=float(E[i])
    v=np.array([float(Q[k,i]) for k in range(N+1)]); L=2*math.log(lam); nmax=int(np.max(np.nonzero(np.abs(v)>1e-13)))+1
    def Ff(xi):
        out=v[0]/np.sqrt(L)*2*np.sin(xi*L/2)/xi
        for n in range(1,nmax):
            w=2*np.pi*n/L; out+=((-1)**n)*v[n]*np.sqrt(2/L)*(np.sin((w-xi)*L/2)/(w-xi)+np.sin((w+xi)*L/2)/(w+xi))
        return out/np.sqrt(2*np.pi)
    beta,_=make_beta_true(lam); mp.mp.dps=15
    h=0.002; xs=np.arange(10+h/2,30,h); bv=np.array([float(beta(x)) for x in xs]); f2=Ff(xs)**2
    # lobe containing/nearest gamma_1
    g=G[0]; j=int(np.argmin(np.abs(xs-g))); neg=bv<0
    # walk to the negative interval nearest gamma_1
    k=j
    if not neg[k]:
        left=k; right=k
        while left>0 and not neg[left]: left-=1
        while right<len(xs)-1 and not neg[right]: right+=1
        k=left if (j-left)<=(right-j) else right
    lo=k; hi=k
    while lo>0 and neg[lo-1]: lo-=1
    while hi<len(xs)-1 and neg[hi+1]: hi+=1
    depth=float(np.min(bv[lo:hi+1])); width=(hi-lo+1)*h; center=xs[lo:hi+1][np.argmin(bv[lo:hi+1])]
    mass_near=2*np.sum(f2[np.abs(xs-g)<1])*h; mass_lobe=2*np.sum(f2[lo:hi+1])*h; e_lobe=2*np.sum(bv[lo:hi+1]*f2[lo:hi+1])*h
    xs2=np.arange(10+h/2,400,h); mass_hi=2*np.sum(Ff(xs2)**2)*h
    print("%-4d %-7.4f %-8.1e | %-9.3f %-7.3f %-7.3f %-8.3f | %-10.2e %-10.2e %-11.2e | %-10.2e   [%.0fs]"%(lam,L,eps,center,depth,width,width*L/(2*math.pi),mass_near,mass_lobe,e_lobe,mass_hi,time.time()-t),flush=True)
