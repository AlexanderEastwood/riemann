"""Exact finite rational witness against a two-sided energy norm contraction."""
import numpy as np,json
from pathlib import Path
from scipy.linalg import eigh
from weighted_pilot import seq
from assembly_general import sequences,block
from flint import arb,arb_mat,ctx
base=Path(__file__).parent
L,b,d,a=seq(4,256);ns=np.arange(17,257);diff=ns[:,None]-ns
B=np.divide(b[ns,None]-b[ns],diff,out=np.zeros(diff.shape),where=diff!=0);np.fill_diagonal(B,d[ns]);B+=(b[ns,None]+b[ns])/(ns[:,None]+ns)
ww=np.sqrt(a[ns]);_,v=eigh(B/ww[:,None]/ww[None,:],subset_by_index=[239,239]);c=v[:,0]/ww
nums=np.rint(c*2**40).astype('int64').tolist();ctx.prec=256
LL,bb,dd,aa=sequences(4,256,256);A=block(list(ns),list(ns),'even',bb,dd);V=arb_mat([[arb(x)/2**40] for x in nums])
energy=(V.transpose()*A*V)[0,0];arch=sum((aa[int(n)]*(arb(x)/2**40)**2 for n,x in zip(ns,nums)),arb(0));difference=energy-2*arch
assert difference>arb('0.0525')
out={'status':'PASS','lambda':4,'N':16,'M':256,'parity':'even','coefficient_denominator':2**40,'coefficient_numerators':nums,'energy':energy.str(55),'arch_energy':arch.str(55),'energy_minus_2arch':difference.str(55),'ratio':(energy/arch).str(55),'claim':'An exact finite rational vector has W energy >2 times its exact archimedean diagonal energy. Thus the signed weighted remainder has norm >1; no negative Weil direction is exhibited.','independent_double_sequence_max_differences':{k:float(np.max(abs(x-np.array(list(map(float,y)))))) for k,x,y in [('b',b,bb),('d',d,dd),('a',a,aa)]}}
(base/'weighted_norm_counterexample.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='coefficient_numerators'})
