"""Structured inverse bound on the actual lambda=4 low-head Schur residual.
All arithmetic entering a sign decision is Arb; frozen witnesses are dyadic.
"""
from assembly_general import *
from certify_low_schur import ldl
import gzip,hashlib,time,argparse
BASE=Path(__file__).parent
OLD=BASE/'evidence/g2_weighted_signed'
if not OLD.exists():OLD=BASE.parent/'g2_weighted_signed'

def readz(path):
 raw=gzip.decompress(path.read_bytes());w=json.loads(raw)
 return w,arb_mat([[arb(x)*arb(2)**e for x,e in row] for row in w['Z']]),hashlib.sha256(raw).hexdigest()

def remote(G,support,M,J,r,parity,b,bstar):
 ns=len(support);nh=G.ncols();root2=arb(2).sqrt();Sm=arb_mat(r,ns);Tm=arb_mat(r,ns)
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
 cmr=2*sum(((arb(m)/M)**(2*r) for m in range(1,M+1)),arb(0));delta2=8*bstar**2*cmr*arb(M)**(2*r)*arb(2*r+2).zeta(arb(J+1))/(1-arb(M)/(J+1))**2
 tau=arb(1)/1000000
 return (1+tau)*(2*bstar**2*S.transpose()*H*S+2*U.transpose()*H*U)+(1+1/tau)*delta2*(G.transpose()*G)

def run(parity='even',M=256,J=4096,r=64,bits=768,tau_exp=0):
 begin=time.time();L,b,d,a=sequences(4,J,bits);c=arb(1)/10**8;N=512 if parity=='even' else 1536;Mi=1024 if parity=='even' else 2048
 assert J>max(M,Mi)
 outer=list(range(0 if parity=='even' else 1,17));mid=list(range(17,M+1));supp=outer+mid;dh=len(outer)
 F=block(outer,outer,parity,b,d);B=block(mid,outer,parity,b,d);T=block(mid,mid,parity,b,d)
 X=T.solve(B,algorithm='lu').mid();G=arb_mat([[int(i==j) if i<dh else -X[i-dh,j] for j in range(dh)] for i in range(len(supp))])
 K=F-B.transpose()*X-X.transpose()*B+X.transpose()*T*X
 Ro=block(list(range(17,J+1)),supp,parity,b,d)*G
 h=arb_mat([[Ro[i,j] for j in range(dh)] for i in range(N-16)])
 k=arb_mat([[Ro[i,j] for j in range(dh)] for i in range(N-16,Ro.nrows())])
 print('outer',time.time()-begin,flush=True)
 w,Z,whash=readz(OLD/f'weighted_witness_l4_s16_{parity}_b256.json.gz')
 C=arb_mat([[arb(float(x)) for x in row] for row in w['C']]);assert all(C[i,j].is_exact() for i in range(C.nrows()) for j in range(C.ncols()))
 ih=list(range(17,N+1));ims=list(range(N+1,Mi+1));ins=ih+ims;di=len(ih)
 Gi=arb_mat([[int(i==j) if i<di else -Z[i-di,j] for j in range(di)] for i in range(len(ins))])
 Ri=block(list(range(N+1,J+1)),ins,parity,b,d,a,c)*Gi
 print('inner residual',time.time()-begin,flush=True)
 prime=prime_bound(4);RL=arb(64)/255;tstar=2*arb.pi()*(N+1)/L;hh=arb(9)/16
 kap=prime+2/tstar
 if parity=='odd':kap+=arb.pi()/2+4*hh*L/(arb.pi()**2*N)
 def error(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return (1-c)*((arb(n)/L).log()-error(2*arb.pi()*n/L))-kap
 assert g(N+1)>0
 Wk=arb_mat([[k[i,j]/g(N+1+i) for j in range(dh)] for i in range(k.nrows())])
 ks=arb_mat([[k[i,j] for j in range(dh)] for i in range(Mi-N)])
 H=h-Z.transpose()*ks-Ri.transpose()*Wk
 CH=C*H;V=k.transpose()*Wk
 pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bstar=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 Uk=remote(G,supp,M,J,r,parity,b,bstar)/g(J+1)
 # Trace bounds the norm of the positive remote Gram after congruence.
 Gc=Gi*C.transpose();URc=remote(Gc,ins,Mi,J,r,parity,b,bstar)/g(J+1)
 rho=sum((URc[i,i] for i in range(di)),arb(0)).upper()
 tau=arb(1)/10**tau_exp;mu=arb(9999999999)/10000000000
 report=json.loads((OLD/f'weighted_tail_l4_s16_{parity}_b320.json').read_text())
 assert report['status']=='PASS' and arb(report['Gershgorin_margin'])>mu and report['witness_sha256']==whash
 CHGram=CH.transpose()*CH
 ingredients={'K':K,'V':V,'Uk':Uk,'CHGram':CHGram}
 (BASE/f'structured_{parity}_M{M}_J{J}_ingredients.json').write_text(json.dumps({'rho':rho.str(190),'mu':mu.str(190),'matrices':{key:[[val[i,j].str(190) for j in range(dh)] for i in range(dh)] for key,val in ingredients.items()}})+'\n')
 lower=K-V-Uk-((1+tau)*CHGram+(1+1/tau)*rho*Uk)/mu
 result,piv=ldl(lower)
 out={'lambda':4,'parity':parity,'outer_head_cut':16,'M':M,'inner_N':N,'inner_M':Mi,'J':J,'r':r,'bits':bits,'tau_exp':tau_exp,'inner_mu':mu.str(35),'rho_trace_upper':rho.str(55),'result':result,'pivots':[x.str(60) for x in piv],'seconds':time.time()-begin,'inner_witness_sha256':whash,'scope':'Failed lower-bound sign gates do not prove a negative Weil direction.'}
 stem=f'structured_{parity}_M{M}_J{J}_r{r}_b{bits}_t{tau_exp}'
 (BASE/(stem+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 (BASE/(stem+'_matrix.json')).write_text(json.dumps({'K':[[K[i,j].str(190) for j in range(dh)] for i in range(dh)],'lower':[[lower[i,j].str(190) for j in range(dh)] for i in range(dh)]})+'\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--parity',default='even')
 for k,v in [('M',256),('J',4096),('r',64),('bits',768),('tau-exp',0)]:p.add_argument('--'+k,type=int,default=v)
 run(**vars(p.parse_args()))
