"""Finite preconditioned trials, verified by the COMPLETE new Weil residual.
Candidate iteration is not a positivity proof. All gates include remote rows.
"""
from mixed_refinement import *

def setup(J,bits):
 L,b,d,a=sequences(4,J,bits);c=arb(1)/10**8;N=512;Mi=1024;di=496
 ow=json.loads((OLD/'structured_ceiling_counterwitness.json').read_text())
 v=arb_mat([[arb(n)/arb(2)**ow['denominator_exponent']] for n in ow['numerators']])
 sw,X,xhash=readz(OLD/'low_witness_even_M256_b768.json.gz');xv=X*v
 f=[v[i,0] if i<17 else -xv[i-17,0] for i in range(257)]
 iw,Z,ihash=readz(OLD.parent/'g2_weighted_signed/weighted_witness_l4_s16_even_b256.json.gz')
 report=json.loads((OLD.parent/'g2_weighted_signed/weighted_tail_l4_s16_even_b320.json').read_text())
 assert report['status']=='PASS' and report['witness_sha256']==ihash and arb(report['Gershgorin_margin'])>arb('0.9999999999')
 C=arb_mat([[arb(float(x)) for x in row] for row in iw['C']]);mu=arb('0.9999999999')
 pm=prime_bound(4);RL=arb(64)/255;t=2*arb.pi()*(N+1)/L;kap=pm+2/t
 def err(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return (1-c)*((arb(n)/L).log()-err(2*arb.pi()*n/L))-kap
 return L,b,d,a,f,Z,C,mu,g,xhash,ihash

def dot(x,y):return sum((u*v for u,v in zip(x,y)),arb(0))
def mv(A,x):
 y=A*arb_mat([[t] for t in x]);return [y[i,0] for i in range(y.nrows())]
def full_action(f,J,b,d,a):
 out=action(f[1:]+[arb(0)]*(J-len(f)+1),1,'even',b,d,a,arb(0))
 for n in range(1,J+1):out[n-1]+=arb(2).sqrt()*b[n]/n*f[0]
 zero=d[0]*f[0]+sum((arb(2).sqrt()*b[n]/n*f[n] for n in range(1,len(f))),arb(0))
 return [zero]+out

def candidate(M=4096,steps=16,bits=768):
 begin=time.time();L,b,d,a,f,Z,C,mu,g,xhash,ihash=setup(65536,bits)
 rhs=full_action(f,M,b,d,a)[17:];c=arb(1)/10**8;di=496
 ctx.prec=256
 rhs=[x.mid() for x in rhs];gs=[g(n) for n in range(513,M+1)];Ct=C.transpose();Zt=Z.transpose()
 def op(v):return action(v,17,'even',b,d,a,arb(0))
 def pre(v):
  h=v[:di];k=v[di:];z=[k[i]/gs[i] for i in range(len(k))]
  az=action([arb(0)]*di+z,17,'even',b,d,a,c)
  ztk=mv(Zt,k[:512]);ztaz=mv(Zt,az[di:di+512])
  head=[h[i]-ztk[i]-az[i]+ztaz[i] for i in range(di)]
  u=mv(Ct,mv(C,head));u=[x/mu for x in u];zu=mv(Z,u)
  graph=u+[-x for x in zu]+[arb(0)]*(M-1024)
  rg=action(graph,17,'even',b,d,a,c)[di:]
  far=[z[i]-rg[i]/gs[i]-(zu[i] if i<512 else 0) for i in range(len(z))]
  return [x.mid() for x in u+far]
 x=[arb(0)]*len(rhs);res=rhs.copy();z=pre(res);p=z.copy();rz=dot(res,z);history=[]
 for j in range(1,steps+1):
  ap=op(p);den=dot(p,ap);assert den>0
  alpha=(rz/den).mid();x=[(xx+alpha*pp).mid() for xx,pp in zip(x,p)]
  res=[(rr-alpha*aa).mid() for rr,aa in zip(res,ap)]
  z=pre(res);new=dot(res,z);assert new>0
  beta=(new/rz).mid();p=[(zz+beta*pp).mid() for zz,pp in zip(z,p)];rz=new
  if j in [1,2,4,8,16,32,64] or j==steps:
   history.append({'step':j,'recursive_residual2':dot(res,res).str(35),'preconditioned_residual2':rz.str(35)})
   print('candidate',M,j,round(time.time()-begin,1),history[-1],flush=True)
 witness={'M':M,'steps':steps,'candidate_bits':256,'source_precision_bits':bits,'outer_sha256':xhash,'inner_sha256':ihash,'dyadics':[[str(t.man_exp()[0]),int(t.man_exp()[1])] for t in x],'history':history,'scope':'Finite trial candidate only; recursive residual is not a certificate.'}
 path=BASE/f'posterior_witness_M{M}_s{steps}.json.gz';path.write_bytes(gzip.compress(json.dumps(witness).encode()))
 return path

def verify(M=4096,steps=16,bits=768,J=65536):
 assert J>M>=1024
 begin=time.time();L,b,d,a,f,Z,C,mu,g,xhash,ihash=setup(J,bits)
 w=json.loads(gzip.decompress((BASE/f'posterior_witness_M{M}_s{steps}.json.gz').read_bytes()));assert w['outer_sha256']==xhash and w['inner_sha256']==ihash
 assert w['M']==M and w['steps']==steps and len(w['dyadics'])==M-16
 x=[arb(n)*arb(2)**e for n,e in w['dyadics']]
 assert all(t.is_exact() for t in x) and g(513)>0
 gf=f+[arb(0)]*(M-256)
 for n in range(17,M+1):gf[n]-=x[n-17]
 wg=full_action(gf,J,b,d,a);K=dot(gf,wg[:M+1]);h=wg[17:513];k=wg[513:];gs=[g(n) for n in range(513,J+1)];z=[k[i]/gs[i] for i in range(len(k))]
 rows=[0,1,16,17,256,512,513,1024,M]
 check=block(rows,list(range(M+1)),'even',b,d)*arb_mat([[t] for t in gf])
 assert all(check[i,0].overlaps(wg[n]) for i,n in enumerate(rows))
 oldaction=full_action(f,M,b,d,a);oldK=dot(f,oldaction[:257])
 identity=oldK-2*dot(oldaction[17:],x)+dot(x,action(x,17,'even',b,d,a,arb(0)))
 assert identity.overlaps(K)
 V=dot(k,z);c=arb(1)/10**8;az=action([arb(0)]*496+z,17,'even',b,d,a,c)
 ztk=mv(Z.transpose(),k[:512]);ztaz=mv(Z.transpose(),az[496:1008]);head=[h[i]-ztk[i]-az[i]+ztaz[i] for i in range(496)];bb=mv(C,head);b2=dot(bb,bb)
 hh=arb(9)/16;pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bs=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 E=remote(arb_mat([[t] for t in gf]),list(range(M+1)),M,J,64,'even',b,bs)[0,0]/g(J+1)
 # Independently saved complete inner residual Gram, same factors, same J.
 old=json.loads((BASE/f'mixed_probe_J{J}_b{bits}.json').read_text());assert old['inner_sha256']==ihash
 assert old['J']==J and old['bits']==bits
 rho=arb(old['remote_Y_HS2_upper'])
 upper=V+E+(b2.sqrt()+(rho*E).sqrt())**2/mu
 finite_lower=K-V-b2/mu
 result={'status':'PASS_COMPLETE_DIRECTION' if K>upper else 'INCONCLUSIVE_COMPLETE_UPPER','M':M,'steps':steps,'J':J,'bits':bits,'K_new_trial':K.str(80),'residual_far_prefix':V.str(80),'residual_mixed_prefix2':b2.str(80),'remote_residual_norm2_upper':E.str(80),'complete_inverse_correction_upper':upper.str(80),'complete_S_direction_lower':(K-upper).str(80),'finite_only_optimistic_margin':finite_lower.str(80),'retained_new_residual2':dot(wg[17:M+1],wg[17:M+1]).str(50),'seconds':time.time()-begin,'scope':'The head vector is unchanged. Exact finite trial energy minus complete inverse-residual upper is a lower Schur bound; failed upper does not prove negativity.'}
 result.update({'dense_rows_checked':rows,'energy_identity_overlap':True,'old_K':oldK.str(80),'old_inverse_correction_lower':(oldK-K).str(80),'old_inverse_correction_upper':(oldK-K+upper).str(80),'relative_S_to_old_K_lower':((K-upper)/oldK).str(80)})
 (BASE/f'posterior_check_M{M}_s{steps}_J{J}_b{bits}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['candidate','verify','both'],default='both');p.add_argument('--M',type=int,default=4096);p.add_argument('--steps',type=int,default=16);p.add_argument('--bits',type=int,default=768);s=p.parse_args()
 if s.mode in ['candidate','both']:candidate(s.M,s.steps,s.bits)
 if s.mode in ['verify','both']:verify(s.M,s.steps,s.bits)
