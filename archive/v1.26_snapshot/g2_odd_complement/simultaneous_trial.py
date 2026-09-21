"""Complete matrix Schur verification of independently frozen finite trials.
No finite-solve convergence or positivity is used as a certificate.
"""
from posterior_trial import *
from certify_low_schur import ldl as historical_ldl

def ldl(A):
 # Multiplication encloses a square even for a zero-centered interval.
 # python-flint 0.9.0 generic **2 can return nan on such an interval.
 n=A.nrows();L=[[arb(0) for j in range(n)] for i in range(n)];D=[]
 for j in range(n):
  p=A[j,j]-sum((L[j][k]*L[j][k]*D[k] for k in range(j)),arb(0))
  if not p>0:return {'status':'FAIL_LOWER_BOUND','index':j,'pivot':p.str(65)},D
  D.append(p)
  for i in range(j+1,n):L[i][j]=(A[i,j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),arb(0)))/p
 return {'status':'PASS','pivots':len(D),'smallest_lower_pivot':min((x.lower() for x in D)).str(65)},D

def init(parity,J,bits):
 L,b,d,a=sequences(4,J,bits);c=arb(1)/10**8
 N,Mi=(512,1024) if parity=='even' else (1536,2048)
 head=list(range(0 if parity=='even' else 1,17));dh=len(head);di=N-16
 ow,X,xhash=readz(OLD/f'low_witness_{parity}_M256_b768.json.gz')
 iw,Z,ihash=readz(OLD.parent/'g2_weighted_signed'/f'weighted_witness_l4_s16_{parity}_b256.json.gz')
 report=json.loads((OLD.parent/'g2_weighted_signed'/f'weighted_tail_l4_s16_{parity}_b320.json').read_text())
 mu=arb('0.9999999999');assert report['status']=='PASS' and report['witness_sha256']==ihash and arb(report['Gershgorin_margin'])>mu
 C=arb_mat([[arb(float(x)) for x in row] for row in iw['C']]);assert all(x.is_exact() for row in C.tolist() for x in row)
 pm=prime_bound(4);RL=arb(64)/255;hh=arb(9)/16;t=2*arb.pi()*(N+1)/L;kap=pm+2/t
 if parity=='odd':kap+=arb.pi()/2+4*hh*L/(arb.pi()**2*N)
 def err(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return (1-c)*((arb(n)/L).log()-err(2*arb.pi()*n/L))-kap
 assert g(N+1)>0
 return L,b,d,a,N,Mi,head,X,Z,C,mu,g,xhash,ihash

def f_action(f,J,parity,b,d,a):
 if parity=='even':return full_action(f,J,b,d,a)
 return action(f+[arb(0)]*(J-len(f)),1,'odd',b,d,a,arb(0))

def candidate_matrix(parity='even',M=4096,steps=16,bits=768,cbits=512,normalized=False):
 begin=time.time();L,b,d,a,N,Mi,head,X,Z,C,mu,g,xhash,ihash=init(parity,65536,bits)
 assert M>=Mi;dh=len(head);di=N-16;nm=Mi-N;c=arb(1)/10**8;offset=0 if parity=='even' else 1
 dh=len(head);original=arb_mat([[int(i==j) if i<dh else -X[i-dh,j] for j in range(dh)] for i in range(257-offset)])
 if normalized:
  KM=sym(original.transpose()*block(list(range(offset,257)),list(range(offset,257)),parity,b,d)*original)
  LL=arb_mat(dh,dh);DD=[]
  for j in range(dh):
   dj=KM[j,j]-sum((LL[j,k]**2*DD[k] for k in range(j)),arb(0));assert dj>0;DD.append(dj);LL[j,j]=1
   for i in range(j+1,dh):LL[i,j]=(KM[i,j]-sum((LL[i,k]*LL[j,k]*DD[k] for k in range(j)),arb(0)))/dj
  invsqrt=arb_mat([[1/DD[i].sqrt() if i==j else 0 for j in range(dh)] for i in range(dh)])
  VV=(LL.transpose().solve(invsqrt)).mid();original=original*VV
 ctx.prec=cbits;original=original.mid();gs=[g(n) for n in range(N+1,M+1)];Ct=C.transpose();Zt=Z.transpose()
 def op(v):return action(v,17,parity,b,d,a,arb(0))
 def pre(v):
  h=v[:di];k=v[di:];z=[k[i]/gs[i] for i in range(len(k))]
  az=action([arb(0)]*di+z,17,parity,b,d,a,c)
  ztk=mv(Zt,k[:nm]);ztaz=mv(Zt,az[di:di+nm]);hh=[h[i]-ztk[i]-az[i]+ztaz[i] for i in range(di)]
  u=[x/mu for x in mv(Ct,mv(C,hh))];zu=mv(Z,u)
  graph=u+[-x for x in zu]+[arb(0)]*(M-Mi);rg=action(graph,17,parity,b,d,a,c)[di:]
  far=[z[i]-rg[i]/gs[i]-(zu[i] if i<nm else 0) for i in range(len(z))]
  return [x.mid() for x in u+far]
 stem=f'simultaneous_{parity}_M{M}_s{steps}'+('_normalized' if normalized else '')
 cols=[];hist=[];bases=[]
 for col in range(dh):
  f=[original[i,col] for i in range(257-offset)]
  bases.append([[str(t.man_exp()[0]),int(t.man_exp()[1])] for t in f])
  rhs=f_action(f,M,parity,b,d,a)[17-offset:];rhs=[x.mid() for x in rhs]
  x=[arb(0)]*len(rhs);res=rhs.copy();z=pre(res);p=z.copy();rz=dot(res,z)
  for j in range(steps):
   ap=op(p);den=dot(p,ap);assert den>0
   alpha=(rz/den).mid();x=[(xx+alpha*pp).mid() for xx,pp in zip(x,p)];res=[(rr-alpha*aa).mid() for rr,aa in zip(res,ap)]
   z=pre(res);new=dot(res,z);assert new>0
   beta=(new/rz).mid();p=[(zz+beta*pp).mid() for zz,pp in zip(z,p)];rz=new
  cols.append([[str(t.man_exp()[0]),int(t.man_exp()[1])] for t in x]);hist.append(dot(res,res).str(40))
  witness={'parity':parity,'M':M,'steps':steps,'candidate_bits':cbits,'outer_sha256':xhash,'inner_sha256':ihash,'dyadic_columns':cols,'base_columns':bases,'normalized':normalized,'recursive_residual2':hist,'scope':'Frozen finite trial only. Verification includes the complete residual matrix.'}
  (BASE/(stem+'_witness.json.gz')).write_bytes(gzip.compress(json.dumps(witness).encode()))
  print('candidate column',parity,col+1,'/',dh,'seconds',round(time.time()-begin,1),flush=True)

def dumpmat(A,digits=220):return [[A[i,j].str(digits) for j in range(A.ncols())] for i in range(A.nrows())]
def sym(A):return (A+A.transpose())/2

def verify_matrix(parity='even',M=4096,steps=16,bits=768,J=65536,normalized=False):
 begin=time.time();L,b,d,a,N,Mi,head,X,Z,C,mu,g,xhash,ihash=init(parity,J,bits)
 assert J>M>=Mi
 dh=len(head);di=N-16;nm=Mi-N;offset=0 if parity=='even' else 1;c=arb(1)/10**8
 stem=f'simultaneous_{parity}_M{M}_s{steps}'+('_normalized' if normalized else '')
 witness_raw=(BASE/(stem+'_witness.json.gz')).read_bytes();trial_hash=hashlib.sha256(witness_raw).hexdigest();w=json.loads(gzip.decompress(witness_raw))
 assert w['M']==M and w['steps']==steps and w['parity']==parity and w['outer_sha256']==xhash and w['inner_sha256']==ihash and len(w['dyadic_columns'])==dh
 fs=[];wgs=[];ks=[];zs=[];bbs=[];gs=[g(n) for n in range(N+1,J+1)];Zt=Z.transpose();rows=[offset,1,16,17,256,N,N+1,Mi,M]
 for col,raw in enumerate(w['dyadic_columns']):
  assert len(raw)==M-16
  x=[arb(n)*arb(2)**e for n,e in raw];assert all(t.is_exact() for t in x)
  if 'base_columns' in w:
   assert len(w['base_columns'][col])==257-offset
   f=[arb(n)*arb(2)**e for n,e in w['base_columns'][col]]+[arb(0)]*(M-256)
   assert all(t.is_exact() for t in f)
  else:f=[arb(int(i==col)) if i<dh else (-X[i-dh,col] if i<257-offset else arb(0)) for i in range(M+1-offset)]
  for n in range(17,M+1):f[n-offset]-=x[n-17]
  wg=f_action(f,J,parity,b,d,a);h=wg[17-offset:N+1-offset];k=wg[N+1-offset:];z=[k[i]/gs[i] for i in range(len(k))]
  dense=block(rows,list(range(offset,M+1)),parity,b,d)*arb_mat([[t] for t in f]);assert all(dense[i,0].overlaps(wg[n-offset]) for i,n in enumerate(rows))
  az=action([arb(0)]*di+z,17,parity,b,d,a,c);ztk=mv(Zt,k[:nm]);ztaz=mv(Zt,az[di:di+nm]);hh=[h[i]-ztk[i]-az[i]+ztaz[i] for i in range(di)];bb=mv(C,hh)
  fs.append(f);wgs.append(wg[:len(f)]);ks.append(k);zs.append(z);bbs.append(bb)
  print('verified column',parity,col+1,'/',dh,'seconds',round(time.time()-begin,1),flush=True)
 G=arb_mat(fs).transpose();headG=arb_mat([[G[i,j] for j in range(dh)] for i in range(dh)]);assert not headG.det().contains(0)
 WG=arb_mat(wgs).transpose();KM=sym(G.transpose()*WG)
 kM=arb_mat(ks).transpose();zM=arb_mat(zs).transpose();V=sym(kM.transpose()*zM);HM=arb_mat(bbs).transpose();HG=HM.transpose()*HM
 del ks,zs,kM,zM
 hh=arb(9)/16;pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bs=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 E=remote(G,list(range(offset,M+1)),M,J,64,parity,b,bs)/g(J+1)
 if parity=='even':
  old=json.loads((BASE/f'mixed_probe_J{J}_b{bits}.json').read_text());assert old['inner_sha256']==ihash and old['J']==J and old['bits']==bits;rho=arb(old['remote_Y_HS2_upper'])
 else:
  Gi=arb_mat([[int(i==j) if i<di else -Z[i-di,j] for j in range(di)] for i in range(Mi-16)])
  UR=remote(Gi*C.transpose(),list(range(17,Mi+1)),Mi,J,64,parity,b,bs)/g(J+1)
  rho=sum((UR[i,i] for i in range(di)),arb(0))
 ingredient={'trial_witness_sha256':trial_hash,'parity':parity,'M':M,'J':J,'steps':steps,'bits':bits,'outer_sha256':xhash,'inner_sha256':ihash,'rho':rho.str(220),'mu':mu.str(220),'matrices':{n:dumpmat(A) for n,A in [('K',KM),('V',V),('E',E),('HGram',HG),('H',HM),('head',headG)]},'scope':'All residual cross-Grams retained; remote bound covers every row beyond J.'}
 (BASE/(stem+f'_ingredients_b{bits}.json')).write_text(json.dumps(ingredient)+'\n')
 gates=[]
 for ep in range(-6,7):
  tau=arb(10)**ep;low=KM-V-E-((1+tau)*HG+(1+1/tau)*rho*E)/mu
  gate,piv=ldl(sym(low));gates.append({'tau_exponent':ep,'gate':gate})
  if gate['status']=='PASS':break
 out={'trial_witness_sha256':trial_hash,'status':'PASS_COMPLETE_HEAD' if any(t['gate']['status']=='PASS' for t in gates) else 'INCONCLUSIVE_COMPLETE_HEAD_BOUND','parity':parity,'M':M,'J':J,'steps':steps,'bits':bits,'rho':rho.str(70),'gates':gates,'K_gate':ldl(KM)[0],'seconds':time.time()-begin,'scope':'Complete one-parity head matrix certificate only if a gate passes; failure does not disprove positivity.'}
 (BASE/(stem+f'_report_b{bits}.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--normalized',action='store_true');p.add_argument('--mode',choices=['candidate','verify','both'],default='both');p.add_argument('--parity',choices=['even','odd'],default='even');p.add_argument('--M',type=int,default=4096);p.add_argument('--J',type=int,default=65536);p.add_argument('--steps',type=int,default=16);p.add_argument('--bits',type=int,default=768);s=p.parse_args()
 if s.mode in ['candidate','both']:candidate_matrix(s.parity,s.M,s.steps,s.bits,normalized=s.normalized)
 if s.mode in ['verify','both']:verify_matrix(s.parity,s.M,s.steps,s.bits,s.J,normalized=s.normalized)
