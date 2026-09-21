"""Certify the complete far-operator inverse iteration constants at lambda=4.
Analytic inputs: the manuscript's two-sided diagonal bound and commutator
norm bound, with the exact pole diagonal bounded by32h/L.
"""
from assembly_general import *
import argparse

def certify(bits=320):
 ctx.prec=bits;L=2*arb(4).log();h=arb(9)/16;c=arb(1)/10**8;RL=arb(64)/255
 P=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0))
 Bstar=(4*h+P+1+arb.pi()/4)/arb.pi()
 CR=2*arb.pi()*Bstar+32*h/L+2*P
 pm=prime_bound(4)
 out={'status':'PASS','bits':bits,'lambda':4,'c':'1/100000000','P':P.str(65),'Bstar':Bstar.str(65),'R_norm_upper':CR.str(65),'sectors':{},'scope':'Complete infinite far operators at one fixed window; no low-head or growing-window sign is asserted.'}
 for par,N,M in [('even',512,67),('odd',1536,335)]:
  t=2*arb.pi()*(N+1)/L
  E=1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
  kap=pm+2/t
  if par=='odd':kap+=arb.pi()/2+4*h*L/(arb.pi()**2*N)
  gamma=(1-c)*((arb(N+1)/L).log()-E)-kap
  ratio=1+(kap+2*(1-c)*E+CR)/gamma
  assert gamma>0 and arb(M)>ratio,(par,ratio)
  out['sectors'][par]={'N':N,'gamma':gamma.str(65),'kappa':kap.str(65),'E':E.str(65),'ratio_bound':ratio.str(65),'certified_integer_M':M,'integer_margin':(M-ratio).str(65),'contraction_factor':f'{M-1}/{M}','all_bounds_strict':True}
 Path(__file__).with_name(f'far_inverse_contraction_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--bits',type=int,default=320);certify(**vars(p.parse_args()))
