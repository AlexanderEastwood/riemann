"""Energy budget of the ground state in the exact split FULL = D + T' + Hk,
and where its Fourier mass sits on the lattice.  Diagnostic; direct eigenvectors."""
import sys, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation')  # run from repo root
from flint import arb, arb_mat, ctx
from assembly_general import sequences, block
from cert import tomp
import mpmath as mp
def parts(lam,N,parity,bits):
    ctx.prec=bits; L,b,d,a=sequences(lam,N+8,bits)
    rows=list(range(0 if parity=='even' else 1,N+1)); n_=len(rows); r2=arb(2).sqrt(); sg=1 if parity=='even' else -1
    D=arb_mat(n_,n_);T=arb_mat(n_,n_);H=arb_mat(n_,n_)
    for i,n in enumerate(rows):
        for j,m in enumerate(rows):
            if n==m:
                D[i,j]=d[n]
                if n>0: H[i,j]=sg*b[n]/n
            elif n==0 or m==0: H[i,j]=r2*b[n+m]/(n+m)
            else: T[i,j]=(b[n]-b[m])/(n-m); H[i,j]=sg*(b[n]+b[m])/(n+m)
    return rows,D,T,H
def budget(lam,N,parity,bits,dps):
    rows,D,T,H=parts(lam,N,parity,bits); mp.mp.dps=dps
    Dm,Tm,Hm=tomp(D,dps),tomp(T,dps),tomp(H,dps); W=Dm+Tm+Hm
    E,Q=mp.eigsy(W); i=min(range(len(E)),key=lambda k:E[k]); v=Q[:,i]
    q=lambda M:(v.T*M*v)[0]
    eD,eT,eH,eW=q(Dm),q(Tm),q(Hm),q(W)
    mass=[abs(v[k])**2 for k in range(len(rows))]; tot=sum(mass); cum=0; m50=m90=None
    for k,mk in enumerate(mass):
        cum+=mk
        if m50 is None and cum>=tot/2: m50=rows[k]
        if m90 is None and cum>=0.9*tot: m90=rows[k]
    lowmass=sum(mk for k,mk in enumerate(mass) if rows[k]<=8)/tot
    return dict(lam=lam,par=parity,N=N,lmin=E[i],eD=eD,eT=eT,eH=eH,eW=eW,m50=m50,m90=m90,low8=lowmass,vmax=rows[max(range(len(mass)),key=lambda k:mass[k])])
print("%-4s %-5s %-4s %-11s %-11s %-11s %-11s %-11s %-5s %-5s %-5s %-6s"%("lam","par","N","lmin","v'Dv","v'T'v","v'Hk v","sum-lmin","peak","n50","n90","mass n<=8"))
for lam,N,bits,dps in ((3,256,768,260),(4,256,768,260),(6,64,2048,600),(8,64,2048,600)):
    for par in ('even','odd'):
        t=time.time(); r=budget(lam,N,par,bits,dps); mp.mp.dps=8
        print("%-4d %-5s %-4d %-11s %-11s %-11s %-11s %-11s %-5d %-5d %-5d %-6s   [%.0fs]"%(lam,par,N,mp.nstr(r['lmin'],5),mp.nstr(r['eD'],5),mp.nstr(r['eT'],5),mp.nstr(r['eH'],5),mp.nstr(r['eW']-r['lmin'],2),r['vmax'],r['m50'],r['m90'],mp.nstr(r['low8'],3),time.time()-t),flush=True)
