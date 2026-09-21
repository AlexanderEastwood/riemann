"""Reproducible Arb experiments for the complete lambda=4 tail inverse.
Finite-prefix experiments are not certificates of the complete Schur sign.
"""
import sys, json, gzip, time, argparse
from pathlib import Path
BASE=Path(__file__).resolve().parent
OLD=BASE/'recovered/g2_low_schur'
if not OLD.exists():OLD=BASE.parent/'g2_low_schur'
sys.path.insert(0,str(OLD))
from assembly_general import *
from flint import arb_poly
from structured_low_schur import remote

def constants(bits=320):
 ctx.prec=bits; L=2*arb(4).log(); h=arb(9)/16; c=arb(1)/10**8
 pm=prime_bound(4); RL=arb(64)/255
 def err(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 out={'bits':bits,'status':'PASS','sectors':{}}
 for par,N,m in [('even',512,20),('odd',1536,90)]:
  t=2*arb.pi()*(N+1)/L; E=err(t); kap=pm+2/t
  pole=h*L**3/(12*arb.pi()**4*N**3)
  if par=='odd':kap+=arb.pi()/2+4*h*L/(arb.pi()**2*N)
  upper=pm+2/t+(arb.pi()/2+pole if par=='even' else 0)
  g=(1-c)*((arb(N+1)/L).log()-E)-kap
  ratio=1+(kap+2*(1-c)*E+upper)/g
  assert g>0 and ratio<m
  out['sectors'][par]={'N':N,'m':m,'ratio':ratio.str(70),'g':g.str(70),'remainder_upper':upper.str(70),'positive_pole_tail_upper':pole.str(70)}
 (BASE/f'parity_inverse_constants_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)

def action(z,start,parity,b,d,a,c):
 """Exact finite compression applied by four Arb polynomial products."""
 size=len(z); bz=[b[start+i]*z[i] for i in range(size)]
 zp=arb_poly(z); bp=arb_poly(bz)
 ker=arb_poly([arb(1)/k if k else arb(0) for k in range(1-size,size)])
 cz=zp*ker; cb=bp*ker
 han=arb_poly([arb(1)/(2*start+k) for k in range(2*size-1)])
 hz=arb_poly(z[::-1])*han; hb=arb_poly(bz[::-1])*han
 sign=1 if parity=='even' else -1
 return [(d[start+i]-c*a[start+i])*z[i]+b[start+i]*cz[size-1+i]-cb[size-1+i]+sign*(b[start+i]*hz[size-1+i]+hb[size-1+i]) for i in range(size)]

def probe(J=4096,bits=768):
 begin=time.time(); L,b,d,a=sequences(4,J,bits); N=512; M=256; c=arb(1)/10**8
 w=json.loads((OLD/'structured_ceiling_counterwitness.json').read_text())
 v=arb_mat([[arb(x)/arb(2)**w['denominator_exponent']] for x in w['numerators']])
 sw=json.loads(gzip.decompress((OLD/'low_witness_even_M256_b768.json.gz').read_bytes()))
 X=arb_mat([[arb(x)*arb(2)**e for x,e in row] for row in sw['Z']])
 xv=X*v; f=arb_mat([[v[i,0] if i<17 else -xv[i-17,0]] for i in range(M+1)])
 wf=block(list(range(M+1)),list(range(M+1)),'even',b,d)*f
 K=(f.transpose()*wf)[0,0]
 k=block(list(range(N+1,J+1)),list(range(M+1)),'even',b,d)*f
 pm=prime_bound(4); RL=arb(64)/255; t=2*arb.pi()*(N+1)/L; kap=pm+2/t
 def err(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return (1-c)*((arb(n)/L).log()-err(2*arb.pi()*n/L))-kap
 gs=[g(n) for n in range(N+1,J+1)]; z=[k[i,0]/gs[i] for i in range(k.nrows())]
 uz=action(z,N+1,'even',b,d,a,c)
 # Independent dense check of the polynomial multiplication indexing.
 zz=arb_mat([[z[i]] for i in range(25)])
 check=block(list(range(N+1,N+26)),list(range(N+1,N+26)),'even',b,d,a,c)*zz
 fast=action(z[:25],N+1,'even',b,d,a,c)
 assert all(check[i,0].overlaps(fast[i]) for i in range(25))
 V=sum((k[i,0]*z[i] for i in range(k.nrows())),arb(0))
 AP=sum((z[i]*(uz[i]-gs[i]*z[i]) for i in range(k.nrows())),arb(0))
 assert AP>0
 hh=arb(9)/16; pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bs=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 Uk=remote(f,list(range(M+1)),M,J,64,'even',b,bs)[0,0]/g(J+1)
 tj=2*arb.pi()*(J+1)/L
 rup=pm+2/tj+arb.pi()/2+hh*L**3/(12*arb.pi()**4*J**3)
 nu=(kap+2*(1-c)*err(tj)+rup)/g(J+1)
 # PSD reverse triangle with a smaller remote compression bound.
 lo=AP.sqrt()-(nu*Uk).sqrt()
 AP_lower=lo*lo if lo>0 else arb(0)
 far_upper=V+Uk-AP_lower/20
 if J==65536:
  assert K>arb('6.469e-20') and far_upper<arb('5.758e-20') and V>K
 out={'status':'PASS_SINGLE_DIRECTION_FAR_GATE' if J==65536 else 'PREFIX_AND_REMOTE_BOUNDS_ONLY','bits':bits,'J':J,'K':K.str(70),'V':V.str(70),'A_prefix':AP.str(70),'remote_norm2_upper':Uk.str(70),'remote_H_norm_upper':nu.str(70),'A_complete_lower':AP_lower.str(70),'first_m20_far_upper':far_upper.str(70),'strict_head_margin':(K-far_upper).str(70),'finite_prefix_first_m20':(V-AP/20).str(70),'first_polynomial_unconditional_lower':(V*V/(V+AP)).str(70),'seconds':time.time()-begin,'scope':'One frozen even head direction only. Not a Schur sign or matrix certificate.'}
 (BASE/f'inverse_probe_J{J}_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['constants','probe'],default='constants');p.add_argument('--bits',type=int,default=320);p.add_argument('--J',type=int,default=4096);s=p.parse_args()
 constants(s.bits) if s.mode=='constants' else probe(s.J,s.bits)
