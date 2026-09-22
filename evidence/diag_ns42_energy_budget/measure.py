"""Direct Gaussian-weight NS-42 quadrature. DIAGNOSTIC, NOT A CERTIFICATE.

Independent squared-edge integration gives J_local; variance and exterior
potential are separately integrated. Identity-reconstructed J is also saved,
explicitly labelled. No interval bounds or source projection are used.
"""
from __future__ import annotations
import argparse
import json
import time
from pathlib import Path
from typing import Any
import mpmath as mp
import numpy as np
from scipy.special import roots_legendre
OUT=Path(__file__).resolve().parent

class Budget:
    def __init__(self, data: dict[str, Any], order: int, dps: int) -> None:
        mp.mp.dps=dps
        self.lam=int(data['lambda']); self.a=mp.log(self.lam)
        self.parity=str(data['parity']); self.rows=list(data['indices'])
        self.vectors=[[mp.mpf(x) for x in v['coefficients']] for v in data['vectors']]
        self.q=[mp.mpf(v['q']) for v in data['vectors']]
        self.gl=[(mp.mpf(float(x)),mp.mpf(float(w))) for x,w in zip(*roots_legendre(order))]
        self.order=order; self.dps=dps
        self.c4=4*mp.pi/mp.sqrt(3); self.sqrt_a=mp.sqrt(self.a)
        self.raw=data

    def quad_nodes(self, left: Any, right: Any) -> list[tuple[Any,Any]]:
        mid=(left+right)/2; half=(right-left)/2
        return [(mid+half*x,half*w) for x,w in self.gl]

    def h(self, x: Any) -> Any:
        x=abs(x); ex=mp.exp(2*x)
        # Terms n=1..8; this is a numerical truncation, not an enclosure.
        return self.c4*mp.exp(mp.mpf('2.5')*x)*mp.fsum(
            n*n*(2*mp.pi*n*n*ex-3)*mp.exp(-mp.pi*n*n*ex) for n in range(1,9))

    def f(self, x: Any) -> list[Any]:
        t=mp.pi*x/self.a; cosine=mp.cos(t)
        if self.parity=='even':
            modes=[1/mp.sqrt(2*self.a)]
            prev=mp.mpf(1); cur=cosine
        else:
            modes=[]; prev=mp.mpf(0); cur=mp.sin(t)
        for n in range(1,max(self.rows)+1):
            modes.append((-1)**n*cur/self.sqrt_a)
            prev,cur=cur,2*cosine*cur-prev
        return [mp.fsum(v*b for v,b in zip(vec,modes)) for vec in self.vectors]

    @staticmethod
    def rho(t: Any) -> Any:
        return mp.exp(t/2)/(2*mp.sinh(t))

    def edge(self, x: Any, y: Any) -> list[Any]:
        hx=self.h(x); hy=self.h(y)
        fx=self.f(x); fy=self.f(y)
        return [hx*hy*(a/hx-b/hy)**2 for a,b in zip(fx,fy)]

    def pole_moments(self) -> tuple[list[Any],list[Any]]:
        c=[]; s=[]
        for vec in self.vectors:
            if self.parity=='even':
                vals=[4*mp.sinh(self.a/2)/mp.sqrt(2*self.a)]
                vals.extend(mp.sinh(self.a/2)/(mp.sqrt(self.a)*((mp.pi*n/self.a)**2+mp.mpf('.25'))) for n in self.rows[1:])
                c.append(mp.fsum(v*t for v,t in zip(vec,vals))); s.append(mp.mpf(0))
            else:
                vals=[-2*(mp.pi*n/self.a)*mp.sinh(self.a/2)/(mp.sqrt(self.a)*((mp.pi*n/self.a)**2+mp.mpf('.25'))) for n in self.rows]
                s.append(mp.fsum(v*t for v,t in zip(vec,vals))); c.append(mp.mpf(0))
        return c,s

    def measure(self) -> dict[str, Any]:
        began=time.time(); integral=[mp.mpf(0) for _ in range(3)]
        norm=[mp.mpf(0) for _ in range(3)]
        for x,w in self.quad_nodes(mp.mpf(0),self.a):
            hx=self.h(x); fx=self.f(x)
            for k in range(3):
                integral[k]+=2*w*mp.cosh(x/2)*fx[k]**2/hx
                norm[k]+=2*w*fx[k]**2
        c,s=self.pole_moments(); ih=1/mp.sqrt(3)
        variance=[integral[k]/ih-(c[k]/ih)**2 for k in range(3)]
        vterm=[mp.mpf(2)/3*v for v in variance]
        pole=[2*c[k]**2-2*s[k]**2 for k in range(3)]
        arch=[mp.mpf(0) for _ in range(3)]
        for t,wt in self.quad_nodes(mp.mpf(0),2*self.a):
            for u,wu in self.quad_nodes(mp.mpf(0),self.a-t/2):
                vals=self.edge(u-t/2,u+t/2)
                for k in range(3): arch[k]+=2*wt*wu*self.rho(t)*vals[k]
        print(self.lam,self.parity,self.order,'internal continuous complete',time.time()-began,flush=True)
        primes=[mp.mpf(0) for _ in range(3)]; exterior_prime=[mp.mpf(0) for _ in range(3)]
        prime_parts=[]
        for n in range(2,16*self.lam+1):
            p=next(j for j in range(2,n+1) if n%j==0); reduced=n
            while reduced%p==0: reduced//=p
            if reduced!=1: continue
            shift=mp.log(n); weight=mp.log(p)/mp.sqrt(n)
            piece=[mp.mpf(0) for _ in range(3)]
            if n<self.lam*self.lam:
                for u,w in self.quad_nodes(mp.mpf(0),self.a-shift/2):
                    vals=self.edge(u-shift/2,u+shift/2)
                    for k in range(3): piece[k]+=2*w*weight*vals[k]
                primes=[x+y for x,y in zip(primes,piece)]
            exterior=[mp.mpf(0) for _ in range(3)]
            for x,w in self.quad_nodes(max(-self.a,self.a-shift),self.a):
                ratio=self.h(x+shift)/self.h(x); fx=self.f(x)
                for k in range(3): exterior[k]+=2*weight*w*ratio*fx[k]**2
            exterior_prime=[x+y for x,y in zip(exterior_prime,exterior)]
            prime_parts.append({'n':n,'J_local':[mp.nstr(x,35) for x in piece],'exterior':[mp.nstr(x,35) for x in exterior]})
        exterior_arch=[mp.mpf(0) for _ in range(3)]
        for x,wx in self.quad_nodes(mp.mpf(0),self.a):
            fx=self.f(x); hx=self.h(x)
            for y,wy in self.quad_nodes(self.a,mp.log(16*self.lam)):
                weight=2*wx*wy*self.h(y)*(self.rho(y-x)+self.rho(y+x))/hx
                for k in range(3): exterior_arch[k]+=weight*fx[k]**2
        local=[arch[k]+primes[k] for k in range(3)]
        exterior=[exterior_arch[k]+exterior_prime[k] for k in range(3)]
        glob=[local[k]+exterior[k] for k in range(3)]
        potential=[exterior[k]-2*ih*integral[k] for k in range(3)]
        reconstructed=[self.q[k]+vterm[k]+2*s[k]**2 for k in range(3)]
        rows=[]
        for k in range(3):
            fields={'k':k,'q_midpoint_matrix':self.q[k],'norm2_quadrature':norm[k],
                'c_moment_analytic':c[k],'s_moment_analytic':s[k],
                'variance':variance[k],'variance_term_2over3':vterm[k],
                'signed_pole_Pi':pole[k],'odd_negative_pole_magnitude':2*s[k]**2,
                'J_local_arch_direct':arch[k],'J_local_prime_direct':primes[k],
                'J_local_direct':local[k],'exterior_arch_direct':exterior_arch[k],
                'exterior_prime_direct':exterior_prime[k],'exterior_energy_direct':exterior[k],
                'J_global_direct':glob[k],'potential_integral_direct':potential[k],
                'J_global_identity_reconstructed':reconstructed[k],
                'J_local_identity_reconstructed':reconstructed[k]-exterior[k],
                'global_identity_residual':glob[k]-vterm[k]-2*s[k]**2-self.q[k],
                'local_identity_residual':local[k]+potential[k]+pole[k]-self.q[k]}
            rows.append({key:val if key=='k' else mp.nstr(val,45) for key,val in fields.items()})
        return {'lambda':self.lam,'parity':self.parity,'N':48,'order':self.order,'dps':self.dps,
            'quadrature':'tensor Gauss-Legendre with float64 nodes and weights, mpmath integrands; orders compared diagnostically',
            'truncations':{'h_terms':8,'prime_n_max':16*self.lam,'exterior_y_max':f'log({16*self.lam})'},
            'seconds':time.time()-began,'vectors':rows,'prime_parts':prime_parts}

def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument('lam',type=int); parser.add_argument('parity'); parser.add_argument('--order',type=int,default=120); parser.add_argument('--dps',type=int,default=70)
    args=parser.parse_args(); data=json.loads((OUT/f'vectors_l{args.lam}_{args.parity}.json').read_text())
    out=Budget(data,args.order,args.dps).measure()
    (OUT/f'budget_l{args.lam}_{args.parity}_g{args.order}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='prime_parts'},indent=2),flush=True)

if __name__=='__main__': main()
