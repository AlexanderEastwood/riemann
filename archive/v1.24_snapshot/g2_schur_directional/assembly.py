"""Exact lambda=3 Weil sequences; Arb enclosures and reusable parity blocks.

Fixed first-slot-linear convention; unshifted normalized Fourier basis.
All three places retained, including the separately defined arch diagonal.
"""
import json
from pathlib import Path
from flint import arb, acb, arb_mat, ctx

BASE=Path(__file__).resolve().parent


def assemble_sequences(nmax,bits=768,K=128,cache=True):
    ctx.prec=bits
    path=BASE/f'weil_sequences_n{nmax}_b{bits}_k{K}.json'
    if cache and path.exists():
        d=json.loads(path.read_text())
        return arb(d['L']),[arb(x) for x in d['b']],[arb(x) for x in d['d']]
    L=2*arb(3).log();pi=arb.pi();h=arb(1)/3
    pdat=[(arb(m).log(),arb(p).log()/arb(m).sqrt())
          for m,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]]
    # The full-length m=9 shift is identically zero, hence omitted exactly.
    ks=[(2*k+arb(1)/2,arb(1)/arb(3)**(4*k+1)) for k in range(K)]
    aK=2*K+arb(1)/2;eK=arb(1)/arb(3)**(4*K+1)
    tailS=eK/(2*aK*(1-arb(1)/81))
    tailD=2*eK/(L*aK*aK*(1-arb(1)/81))
    bs=[];ds=[]
    for n in range(nmax+1):
        t=2*pi*n/L;z=acb(arb(1)/4,-t/2)
        psi=z.digamma();trig=z.polygamma(1)
        s=arb(0) if n==0 else -psi.imag/2
        d=pi.log()-psi.real-trig.real/(2*L)
        for a,e in ks:
            den=a*a+t*t
            if n:s-=e*t/den
            d+=2/L*e*(a*a-t*t)/(den*den)
        if n:s+=arb(0,tailS.upper())
        d+=arb(0,tailD.upper())
        den=L*L+16*pi*pi*n*n
        b=32*L*h*n/den+(s+sum(((t*y).sin()*v for y,v in pdat),arb(0)))/pi
        pole=32*L*h*(L*L-16*pi*pi*n*n)/(den*den)
        prime=2*sum(((t*y).cos()*(1-y/L)*v for y,v in pdat),arb(0))
        bs.append(b);ds.append(pole-prime-d)
    if cache:
        digits=int(bits*0.30103)-8
        data=dict(lambda_exact=3,nmax=nmax,bits=bits,K=K,
                  scope='Arb enclosures of exact all-index Weil sequences; no spectral claim.',
                  L=L.str(digits),b=[x.str(digits) for x in bs],d=[x.str(digits) for x in ds],
                  tailS=tailS.str(40),tailD=tailD.str(40))
        path.write_text(json.dumps(data,indent=2)+'\n')
    return L,bs,ds


def parity_entry(n,m,parity,b,d):
    """Even indices 0,1,...; odd indices 1,2,... ."""
    if parity not in ('even','odd'):raise ValueError(parity)
    if n==m==0:return d[0]
    if n==0 or m==0:
        assert parity=='even'
        j=n+m
        return arb(2).sqrt()*b[j]/j
    same=d[n] if n==m else (b[n]-b[m])/(n-m)
    opposite=(b[n]+b[m])/(n+m)
    return same+opposite if parity=='even' else same-opposite


def parity_block(rows,cols,parity,b,d):
    return arb_mat([[parity_entry(n,m,parity,b,d) for m in cols] for n in rows])
