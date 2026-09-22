"""Independent mpmath adaptive quadrature of two lambda=4 entries; diagnostic only.
Finite integral uses exact digamma and sinc transforms. Tail expands inverse powers,
retains all prime/continuum oscillations, and integrates powers via incomplete gamma.
No grid quadrature helpers are imported. Tail order/cutoff replay is not a certificate.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any
import mpmath as mp
from flint import ctx
sys.path.insert(0,'evidence/v124/g2_schur_cancellation')
from assembly_general import sequences, block
mp.mp.dps=40
L=2*mp.log(4)
PW=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13)]

def beta(x: Any) -> Any:
    c=mp.mpf('.5')+1j*x
    return mp.re(mp.digamma(mp.mpf('1.25')+1j*x/2))-mp.log(mp.pi)-2*sum(mp.log(p)/mp.sqrt(m)*mp.cos(x*mp.log(m)) for m,p in PW)+2*mp.re((mp.exp(c*L)-1)/c)

def transform(n: int, x: Any, odd: bool) -> Any:
    if n==0:
        return mp.sqrt(L/(2*mp.pi))*mp.sinc(x*L/2)
    w=2*mp.pi*n/L
    return mp.sqrt(2/L)*L/2/mp.sqrt(2*mp.pi)*(mp.sinc((w-x)*L/2)+(-1 if odd else 1)*mp.sinc((w+x)*L/2))

def moment(p: int, freq: Any, X: int, logterm: bool=False) -> Any:
    if abs(freq)<mp.mpf('1e-35'):
        val=mp.mpf(X)**(1-p)/(p-1)
        return val*(mp.log(X)+1/mp.mpf(p-1)) if logterm else val
    def f(q: Any) -> Any:
        return (-1j*freq)**(q-1)*mp.gammainc(1-q,-1j*freq*X)
    return -mp.diff(f,p) if logterm else f(p)

def tail(n: int, m: int, odd: bool, X: int, order: int) -> Any:
    # After applying (-1)^(n+m), 2 F_n F_m = (4 c_n c_m/pi)*sin²(xL/2)
    # times x²/((x²-w_n²)(x²-w_m²)), or w_n*w_m/den for odd.
    wn=2*mp.pi*n/L; wm=2*mp.pi*m/L
    cn=mp.sqrt((1 if n==0 else 2)/L); cm=mp.sqrt((1 if m==0 else 2)/L)
    base={}
    for k in range(order//2):
        p=(4 if odd else 2)+2*k
        base[p]=sum(wn**(2*j)*wm**(2*(k-j)) for j in range(k+1))*(wn*wm if odd else 1)
    # Re psi(5/4+ix/2)-log pi = log x + sum a_p*x^-p.
    a={0:-mp.log(2*mp.pi)}; z0=mp.mpf('1.25'); q=-2j*z0
    for p in range(1,order+1):
        value=(-1)**(p+1)*q**p/p
        value+=1j*(-q)**(p-1)
        for k in range(1,p//2+1):
            value-=mp.bernoulli(2*k)/(2*k)*(2/1j)**(2*k)*(-1)**(p-2*k)*mp.binomial(p-1,p-2*k)*q**(p-2*k)
        a[p]=mp.re(value)
    terms=[(p,mp.mpf(0),v) for p,v in a.items()]
    for value,prime in PW:
        for sign in (-1,1):
            terms.append((0,sign*mp.log(value),-mp.log(prime)/mp.sqrt(value)))
    # 2 Re[(4 exp(ixL)-1)/(.5+ix)].
    for k in range(order//2):
        fac=(-mp.mpf('.25'))**k
        terms.extend([(2+2*k,L,2*fac),(2+2*k,-L,2*fac),(2+2*k,mp.mpf(0),-fac),
                      (1+2*k,L,-4j*fac),(1+2*k,-L,4j*fac)])
    result=mp.mpc(0)
    cache: dict[Any,Any]={}
    def mom(p: int, f: Any, logterm: bool=False) -> Any:
        key=(p,str(f),logterm)
        if key not in cache:
            cache[key]=moment(p,f,X,logterm)
        return cache[key]
    for bp,bv in base.items():
        if bp>order:
            continue
        for sf,sv in [(mp.mpf(0),mp.mpf('.5')),(L,-mp.mpf('.25')),(-L,-mp.mpf('.25'))]:
            result+=bv*sv*mom(bp,sf,True)
            for ap,af,av in terms:
                if bp+ap<=order:
                    result+=bv*sv*av*mom(bp+ap,sf+af)
    return mp.re(result)*4*cn*cm/mp.pi

def run() -> None:
    ctx.prec=512
    _,b,d,_=sequences(4,16,512)
    out=[]
    for odd,n,m in [(False,0,1),(True,1,2)]:
        W=block([n],[m],'odd' if odd else 'even',b,d)[0,0]
        ref=mp.mpf(W.mid().str(45,radius=False))
        def fun(x: Any) -> Any:
            return 2*beta(x)*transform(n,x,odd)*transform(m,x,odd)*(-1)**(n+m)
        low=mp.mpf(0)
        for cutoff in (64,128):
            start=0 if cutoff==64 else 64
            low+=mp.fsum(mp.quadgl(fun,[k,k+2],maxdegree=6) for k in range(start,cutoff,2))
            for order in (12,18):
                high=tail(n,m,odd,cutoff,order)
                row={'parity':'odd' if odd else 'even','n':n,'m':m,'cutoff':cutoff,'tail_order':order,
                     'reference':str(ref),'signed_finite':str(low),'unsigned_finite':str(-low),
                     'tail':str(high),'total':str(low+high),'error':str(low+high-ref)}
                out.append(row); print(json.dumps(row),flush=True)
    Path('evidence/diag_ns31_audit/identity.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    run()
