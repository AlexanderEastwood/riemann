"""Arb enclosures of the actual Weil Fourier coefficients at integer lambda."""
from flint import arb,acb,arb_mat,ctx
import json
from pathlib import Path
B=Path(__file__).resolve().parent

def pairs(lam):
 out=[]
 for m in range(2,lam*lam):
  for p in range(2,m+1):
   if m%p==0:
    k=m
    while k%p==0:k//=p
    if k==1:out.append((m,p))
    break
 return out

def sequences(lam,J,bits=256,K=40):
 ctx.prec=bits;path=B/f'sequences_v2_l{lam}_J{J}_b{bits}.json'
 if path.exists():
  d=json.loads(path.read_text());return arb(d['L']),*[list(map(arb,d[k])) for k in ['b','d','a']]
 L=2*arb(lam).log();pi=arb.pi();h=(L/4).sinh()**2
 pw=[(arb(m).log(),arb(p).log()/arb(m).sqrt()) for m,p in pairs(lam)]
 ks=[(2*k+arb(1)/2,arb(1)/arb(lam)**(4*k+1)) for k in range(K)]
 aK=2*K+arb(1)/2;eK=arb(1)/arb(lam)**(4*K+1)
 es=eK/(2*aK*(1-arb(1)/lam**4));ed=2*eK/(L*aK*aK*(1-arb(1)/lam**4))
 bs=[];ds=[];ars=[]
 for n in range(J+1):
  t=2*pi*n/L;z=acb(arb(1)/4,-t/2);ps=z.digamma();tri=z.polygamma(1)
  s=-ps.imag/2; a=ps.real-pi.log()+tri.real/(2*L)
  for c,e in ks:
   den=c*c+t*t;s-=e*t/den;a-=2/L*e*(c*c-t*t)/(den*den)
  s+=arb(0,es.upper());a+=arb(0,ed.upper())
  den=L*L+16*pi*pi*n*n
  b=32*L*h*n/den+(s+sum(((t*y).sin()*w for y,w in pw),arb(0)))/pi
  d=a+32*L*h*(L*L-16*pi*pi*n*n)/(den*den)-2*sum(((t*y).cos()*(1-y/L)*w for y,w in pw),arb(0))
  bs.append(b);ds.append(d);ars.append(a)
 digits=int(bits*.30103)-5
 path.write_text(json.dumps({'lambda':lam,'bits':bits,'J':J,'K':K,'L':L.str(digits),'b':[x.str(digits) for x in bs],'d':[x.str(digits) for x in ds],'a':[x.str(digits) for x in ars]},indent=2)+'\n')
 return L,bs,ds,ars

def block(rows,cols,parity,b,d,a=None,c=0):
 def e(n,m):
  same=d[n]-(c*a[n] if a is not None else 0) if n==m else (b[n]-b[m])/(n-m)
  opp=(b[n]+b[m])/(n+m)
  return same+opp if parity=='even' else same-opp
 return arb_mat([[e(n,m) for m in cols] for n in rows])

def prime_bound(lam):
 """Safe phi=exp(-x/2)+exp(-(L-x)/2) bound by every one-sided breakpoint."""
 L=2*arb(lam).log();data=pairs(lam);cuts=sorted(set([1,lam*lam]+[m for m,p in data]+[lam*lam/m for m,p in data]))
 vals=[]
 # Exact active-set decisions use rational midpoints; ratios use exact rational cuts.
 from fractions import Fraction
 cuts=sorted(set([Fraction(1),Fraction(lam*lam)]+[Fraction(m) for m,p in data]+[Fraction(lam*lam,m) for m,p in data]))
 for left,right in zip(cuts,cuts[1:]):
  mid=(left+right)/2
  for u0 in [left,right]:
   u=arb(u0.numerator)/u0.denominator;phi=(u.sqrt()+lam/u.sqrt())
   val=arb(0)
   for m,p in data:
    w=arb(p).log()/arb(m).sqrt()
    if mid*m<lam*lam:val+=w*((u*m).sqrt()+lam/(u*m).sqrt())/phi
    if mid>m:val+=w*((u/m).sqrt()+lam/(u/m).sqrt())/phi
   vals.append(val)
 best=vals[0].upper()
 for v in vals:
  u=v.upper()
  if u>best:best=u
 assert all(best>=v.upper() for v in vals)
 return best
