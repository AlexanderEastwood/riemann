"""Finite-support K positivity for the complete lambda4 quadratic form."""
from assembly_general import *
import argparse,gzip,hashlib
BASE=Path(__file__).parent

def positive_ldl(A):
 n=A.nrows();ls=[[arb(0) for _ in range(n)] for _ in range(n)];ps=[]
 for j in range(n):
  p=A[j,j]-sum((ls[j][k]**2*ps[k] for k in range(j)),arb(0));assert p>0,(j,p)
  ps.append(p)
  for i in range(j+1,n):ls[i][j]=(A[i,j]-sum((ls[i][k]*ls[j][k]*ps[k] for k in range(j)),arb(0)))/p
 return ps

def run(bits=768):
 L,b,d,a=sequences(4,256,bits);report={'bits':bits,'lambda':4,'head_cut':16,'solve_cut':256,'results':[],'scope':'K_X is the exact complete-operator finite-support form; alpha=0 for these two frozen solves and for X0. This does not prove the infinite Schur complement positive or any uniform growing-window sign.'}
 for parity in ['even','odd']:
  head=list(range(0 if parity=='even' else 1,17));mid=list(range(17,257));nh=len(head)
  F=block(head,head,parity,b,d);T=block(mid,mid,parity,b,d);B=block(mid,head,parity,b,d)
  witness=BASE/f'finite_K_X_{parity}.json.gz'
  if witness.exists():
   w=json.loads(gzip.decompress(witness.read_bytes()));X=arb_mat([[arb(v)*arb(2)**e for v,e in row] for row in w['X']])
  else:
   X=T.solve(B,algorithm='lu').mid();w={'lambda':4,'parity':parity,'head_cut':16,'support_cut':256,'X':[[[str(v),int(e)] for v,e in [X[i,j].man_exp() for j in range(nh)]] for i in range(X.nrows())]};witness.write_bytes(gzip.compress(json.dumps(w,separators=(',',':')).encode(),mtime=0))
  K=F-B.transpose()*X-X.transpose()*B+X.transpose()*T*X
  for name,A in [('zero',F),('frozen_finite_solve',K)]:
   piv=positive_ldl(A)
   report['results'].append({'parity':parity,'X':name,'status':'PASS_STRICT_POSITIVE','pivot_count':len(piv),'smallest_lower_pivot':min(x.lower() for x in piv).str(65),'witness_sha256':hashlib.sha256(gzip.decompress(witness.read_bytes())).hexdigest() if name!='zero' else None})
 (BASE/f'finite_K_certificate_b{bits}.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--bits',type=int,default=768);run(**vars(p.parse_args()))
