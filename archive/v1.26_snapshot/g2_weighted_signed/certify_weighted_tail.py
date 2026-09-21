"""One-sided verified-solve certificate on a literal Fourier tail. No RH input."""
from assembly_general import *
import numpy as np,time,argparse
from scipy.linalg import cholesky,solve_triangular
from threadpoolctl import threadpool_limits

def certify(lam=4,start=16,N=512,M=1024,J=4096,r=48,parity='even',bits=256,cstr='0.00000001',witness_path=None):
 begin=time.time();L,b,d,a=sequences(lam,J,bits);c=arb(cstr)
 head=list(range(start+1,N+1));mid=list(range(N+1,M+1));support=head+mid;nh=len(head);ns=len(support)
 mat=lambda rr,cc:block(rr,cc,parity,b,d,a,c)
 F=mat(head,head);T=mat(mid,mid);B=mat(mid,head)
 loaded=None
 if witness_path:
  import gzip
  loaded=json.loads(gzip.decompress(Path(witness_path).read_bytes()))
  Z=arb_mat([[arb(x)*arb(2)**e for x,e in row] for row in loaded['Z']])
 else:Z=T.solve(B,algorithm='lu').mid()
 assert Z.nrows()==len(mid) and Z.ncols()==nh
 assert all(Z[i,j].is_exact() for i in range(Z.nrows()) for j in range(Z.ncols()))
 print('solved',parity,time.time()-begin,flush=True)
 G=arb_mat([[int(i==j) if i<nh else -Z[i-nh,j] for j in range(nh)] for i in range(ns)])
 K=F-B.transpose()*Z-Z.transpose()*B+Z.transpose()*T*Z
 R=mat(list(range(N+1,J+1)),support)*G
 print('residual',time.time()-begin,flush=True)
 root2=arb(2).sqrt();Sm=arb_mat(r,ns);Tm=arb_mat(r,ns)
 for col,m in enumerate(support):
  q=arb(m)/M;power=arb(1)
  for j in range(r):
   if (j%2==0)==(parity=='even'):Sm[j,col]=root2*power
   else:Tm[j,col]=root2*power*b[m]
   power*=q
 S=Sm*G;U=Tm*G
 ps=[arb(k+2).zeta(arb(J+1)) for k in range(2*r-1)];powers=[arb(M)**k for k in range(2*r-1)]
 H=arb_mat([[2*powers[j+k]*ps[j+k] if (j+k)%2==0 else 0 for k in range(r)] for j in range(r)])
 P=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(lam)),arb(0));h=(L/4).sinh()**2;bstar=(4*h+P+1+arb.pi()/4)/arb.pi()
 cmr=2*sum(((arb(m)/M)**(2*r) for m in range(1,M+1)),arb(0));delta2=8*bstar**2*cmr*arb(M)**(2*r)*arb(2*r+2).zeta(arb(J+1))/(1-arb(M)/(J+1))**2
 tau=arb(1)/10**6;remote=(1+tau)*(2*bstar**2*S.transpose()*H*S+2*U.transpose()*H*U)+(1+1/tau)*delta2*(G.transpose()*G)
 prime=prime_bound(lam);RL=arb(1)/lam/(1-arb(1)/lam**4);CL=arb(1)
 assert CL>=arb(1)/4+RL;tstar=2*arb.pi()*(N+1)/L
 kappa=prime+2*CL/tstar
 if parity=='odd':kappa+=arb.pi()/2+4*h*L/(arb.pi()**2*N)
 def error(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return (1-c)*((arb(n)/L).log()-error(2*arb.pi()*n/L))-kappa
 gamma=g(N+1);assert gamma>0,str(gamma)
 arch_floor=(arb(start+1)/L).log()-error(2*arb.pi()*(start+1)/L)
 assert arch_floor>0
 gs=[g(n) for n in range(N+1,J+1)];weighted=arb_mat([[R[i,j]/gs[i] for j in range(nh)] for i in range(R.nrows())])
 lower=K-R.transpose()*weighted-remote/g(J+1)
 print('lower formed',time.time()-begin,flush=True)
 # Freeze the computed inverse Cholesky as an exact dyadic witness; its origin has no proof role.
 f=np.array([[float(lower[i,j].mid()) for j in range(nh)] for i in range(nh)])
 with threadpool_limits(2):
  try:
   if loaded:C=np.array(loaded['C'])
   else:ch=cholesky(f,lower=True);C=solve_triangular(ch,np.eye(nh),lower=True)
  except Exception as ex:
   out={'status':'NO CERTIFICATE','why':str(ex),'min_numeric':float(np.linalg.eigvalsh(f)[0])};print(out,flush=True);return out
 A=arb_mat([[arb(float(v)) for v in row] for row in C]);assert all(A[i,j].is_exact() for i in range(nh) for j in range(nh))
 Y=A*lower*A.transpose();margins=[Y[i,i]-sum((abs(Y[i,j]) for j in range(nh) if j!=i),arb(0)) for i in range(nh)];margin=margins[0].lower()
 for v in margins:
  if v.lower()<margin:margin=v.lower()
 assert all(A[i,i]!=0 for i in range(nh))
 assert all(A[i,j]==0 for i in range(nh) for j in range(i+1,nh))
 ok=all(v>0 for v in margins)
 import gzip,hashlib
 witness={'Z':[[[str(x),int(e)] for x,e in [Z[i,j].man_exp() for j in range(Z.ncols())]] for i in range(Z.nrows())],'C':[[float(x) for x in row] for row in C]}
 name=f'weighted_witness_l{lam}_s{start}_{parity}_b{bits}.json.gz';raw=json.dumps(witness,separators=(',',':')).encode();(Path(__file__).parent/name).write_bytes(gzip.compress(raw,mtime=0))
 out={'status':'PASS' if ok else 'NO CERTIFICATE','lambda':lam,'literal_tail_start':start,'N':N,'M':M,'J':J,'r':r,'bits':bits,'c':cstr,'parity':parity,'head_dimension':nh,'prime_bound':prime.str(40),'remote_gamma':gamma.str(40),'arch_diagonal_floor':arch_floor.str(40),'all_Gershgorin_rows_positive':ok,'Gershgorin_margin':margin.str(40),'delta2':delta2.str(40),'witness':name,'witness_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.time()-begin,'claim':'W restricted to |n|>start in selected parity >= c times the exact positive archimedean diagonal; fixed window only.'}
 (Path(__file__).parent/f'weighted_tail_l{lam}_s{start}_{parity}_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True);return out
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for k,v in [('lam',4),('start',16),('N',512),('M',1024),('J',4096),('r',48),('bits',256)]:p.add_argument('--'+k,type=int,default=v)
 p.add_argument('--parity',default='even');p.add_argument('--cstr',default='0.00000001');p.add_argument('--witness-path');certify(**vars(p.parse_args()))
