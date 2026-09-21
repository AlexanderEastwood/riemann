"""Actual low-head Schur certificate using the proved complete lambda4 tail metric."""
from assembly_general import *
import argparse,time,gzip,hashlib
BASE=Path(__file__).parent

def ldl(A):
 n=A.nrows();L=[[arb(0) for j in range(n)] for i in range(n)];D=[]
 for j in range(n):
  p=A[j,j]-sum((L[j][k]**2*D[k] for k in range(j)),arb(0))
  if not p>0:return {'status':'FAIL_LOWER_BOUND','index':j,'pivot':p.str(65)},D
  D.append(p)
  for i in range(j+1,n):L[i][j]=(A[i,j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),arb(0)))/p
 return {'status':'PASS','pivots':len(D),'smallest_lower_pivot':min((x.lower() for x in D)).str(65)},D

def run(M=256,J=2048,r=64,parity='even',bits=768,witness_path=None):
 begin=time.time();L,b,d,a=sequences(4,J,bits);N=16;c=arb(1)/100000000
 head=list(range(0 if parity=='even' else 1,N+1));mid=list(range(N+1,M+1));support=head+mid;nh=len(head);ns=len(support)
 F=block(head,head,parity,b,d);T=block(mid,mid,parity,b,d);B=block(mid,head,parity,b,d)
 if witness_path:
  w=json.loads(gzip.decompress(Path(witness_path).read_bytes()));Z=arb_mat([[arb(x)*arb(2)**e for x,e in row] for row in w['Z']])
 else:Z=T.solve(B,algorithm='lu').mid()
 assert all(Z[i,j].is_exact() for i in range(Z.nrows()) for j in range(Z.ncols()))
 G=arb_mat([[int(i==j) if i<nh else -Z[i-nh,j] for j in range(nh)] for i in range(ns)])
 K=F-B.transpose()*Z-Z.transpose()*B+Z.transpose()*T*Z
 R=block(list(range(N+1,J+1)),support,parity,b,d)*G
 print('solve+residual',parity,M,time.time()-begin,flush=True)
 root2=arb(2).sqrt();Sm=arb_mat(r,ns);Tm=arb_mat(r,ns)
 for col,m in enumerate(support):
  if m==0:Sm[0,col]=1;continue
  q=arb(m)/M;power=arb(1)
  for j in range(r):
   if (j%2==0)==(parity=='even'):Sm[j,col]=root2*power
   else:Tm[j,col]=root2*power*b[m]
   power*=q
 S=Sm*G;U=Tm*G
 powers=[arb(M)**k for k in range(2*r-1)];ps=[arb(k+2).zeta(arb(J+1)) for k in range(2*r-1)]
 H=arb_mat([[2*powers[j+k]*ps[j+k] if (j+k)%2==0 else 0 for k in range(r)] for j in range(r)])
 pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));h=arb(9)/16;bstar=(4*h+pp+1+arb.pi()/4)/arb.pi()
 cmr=2*sum(((arb(m)/M)**(2*r) for m in range(1,M+1)),arb(0));delta2=8*bstar**2*cmr*arb(M)**(2*r)*arb(2*r+2).zeta(arb(J+1))/(1-arb(M)/(J+1))**2
 tau=arb(1)/1000000;remote=(1+tau)*(2*bstar**2*S.transpose()*H*S+2*U.transpose()*H*U)+(1+1/tau)*delta2*(G.transpose()*G)
 RL=arb(64)/255
 def e(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return c*((arb(n)/L).log()-e(2*arb.pi()*n/L))
 assert g(17)>0
 weighted=arb_mat([[R[i,j]/(c*a[N+1+i]) for j in range(nh)] for i in range(R.nrows())])
 lower=K-R.transpose()*weighted-remote/g(J+1)
 result,pivots=ldl(lower)
 zraw=json.dumps({'N':16,'M':M,'parity':parity,'Z':[[[str(x),int(e)] for x,e in [Z[i,j].man_exp() for j in range(nh)]] for i in range(Z.nrows())]},separators=(',',':')).encode();name=f'low_witness_{parity}_M{M}_b{bits}.json.gz';(BASE/name).write_bytes(gzip.compress(zraw,mtime=0))
 out={'lambda':4,'head_cut':16,'M':M,'J':J,'r':r,'bits':bits,'parity':parity,'tail_c':'1/100000000','result':result,'pivots':[x.str(75) for x in pivots],'remote_delta2':delta2.str(55),'witness':name,'witness_sha256':hashlib.sha256(zraw).hexdigest(),'seconds':time.time()-begin,'scope':'A negative lower-bound pivot is not proof that the exact Weil form is negative.'}
 (BASE/f'low_schur_{parity}_M{M}_J{J}_r{r}_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 (BASE/f'low_matrix_{parity}_M{M}_b{bits}.json').write_text(json.dumps({'K':[[K[i,j].str(180) for j in range(nh)] for i in range(nh)],'lower':[[lower[i,j].str(180) for j in range(nh)] for i in range(nh)]})+'\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for k,v in [('M',256),('J',2048),('r',64),('bits',768)]:p.add_argument('--'+k,type=int,default=v)
 p.add_argument('--parity',default='even');p.add_argument('--witness-path');run(**vars(p.parse_args()))
