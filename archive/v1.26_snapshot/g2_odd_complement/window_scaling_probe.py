"""Growing-window diagnostics. Finite corrections are NOT complete tail uppers.
Fresh analytic far-cut bounds are independently certified at every window.
"""
from simultaneous_trial import *
import numpy as np

def asfloat(A):return np.array([[float(t.mid()) for t in row] for row in A.tolist()])
def lognorm(A):
 scale=max((abs(t).upper() for row in A.tolist() for t in row),key=lambda t:float(t.log()))
 return float(scale.log()/arb(10).log())+np.log10(np.linalg.norm(asfloat(A/scale),2))
def congruence(K):
 n=K.nrows();LL=arb_mat(n,n);DD=[]
 for j in range(n):
  dj=(K[j,j].mid()-sum((LL[j,k]**2*DD[k] for k in range(j)),arb(0))).mid();assert dj>0;DD.append(dj);LL[j,j]=1
  for i in range(j+1,n):LL[i,j]=((K[i,j].mid()-sum((LL[i,k]*LL[j,k]*DD[k] for k in range(j)),arb(0)))/dj).mid()
 VV=arb_mat(n,n)
 for j in range(n):
  for i in range(n-1,-1,-1):VV[i,j]=((1/DD[i].sqrt() if i==j else 0)-sum((LL[k,i]*VV[k,j] for k in range(i+1,n)),arb(0))).mid()
 return VV

def finite_tail_gate(T):
 try:
  cnp=np.tril(np.linalg.inv(np.linalg.cholesky(asfloat(T))))
  C=arb_mat([[arb(float(x)) for x in row] for row in cnp]);A=sym(C*T*C.transpose());n=T.nrows()
  assert all(C[i,i]>0 for i in range(n))
  margins=[A[i,i]-sum((abs(A[i,j]) for j in range(n) if j!=i),arb(0)) for i in range(n)]
  if all(t>0 for t in margins):return 'PASS_FLOAT_PROPOSAL_INTERVAL_GERSHGORIN'
 except (np.linalg.LinAlgError,AssertionError):pass
 result=ldl(T)[0];assert result['status']=='PASS',result
 return 'PASS_INTERVAL_LDL'


def far_cuts(lam,bits=320):
 ctx.prec=bits;L=2*arb(lam).log();h=arb(lam-1)**2/(4*lam);RL=arb(lam)**3/(arb(lam)**4-1);P=prime_bound(lam);c=arb(1)/10**8
 def err(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def gamma(N,parity):
  t=2*arb.pi()*(N+1)/L;k=P+2/t
  if parity=='odd':k+=arb.pi()/2+4*h*L/(arb.pi()**2*N)
  return (1-c)*((arb(N+1)/L).log()-err(t))-k
 out={'lambda':lam,'bits':bits,'prime_schur_upper':P.str(65),'sectors':{}}
 for par in ['even','odd']:
  lo=1;hi=2
  while not gamma(hi,par)>0:lo=hi;hi*=2
  while hi-lo>1:
   mid=(lo+hi)//2
   if gamma(mid,par)>0:hi=mid
   else:lo=mid
  assert gamma(hi,par)>0 and gamma(hi-1,par)<0
  out['sectors'][par]={'first_positive_N':hi,'gamma_at_N':gamma(hi,par).str(55),'gamma_at_previous':gamma(hi-1,par).str(55)}
 return out

def finite_probe(lam,parity='even',ret=256,omit=384,bits=2048):
 start=time.time();L,b,d,a=sequences(lam,omit,bits,K=192);H=lam*lam;offset=0 if parity=='even' else 1;hs=list(range(offset,H+1));nh=len(hs)
 assert H<ret<omit
 def solve(M):
  tail=list(range(H+1,M+1));F=block(hs,hs,parity,b,d);B=block(tail,hs,parity,b,d);T=block(tail,tail,parity,b,d)
  finite_tail_gate(T)
  X=T.solve(B,algorithm='precond');S=sym(F-B.transpose()*X);return S
 K=solve(ret);Somit=solve(omit);V=congruence(K);Kn=sym(V.transpose()*K*V);Un=sym(V.transpose()*(K-Somit)*V);lower=sym(Kn-Un)
 kg=ldl(Kn)[0];sg=ldl(lower)[0]
 if kg['status']!='PASS' or sg['status']!='PASS':
  print('INCONCLUSIVE_METRIC',lam,kg,sg,'Kdev',max((abs(Kn[i,j]-int(i==j)).upper() for i in range(nh) for j in range(nh))).str(15),'lognormV',lognorm(V),flush=True)
 assert kg['status']=='PASS' and sg['status']=='PASS'
 assert all(abs(Kn[i,j]-int(i==j))<arb('1e-20') for i in range(nh) for j in range(nh))
 kn=asfloat(Kn);un=asfloat(Un);lo=asfloat(lower);kk=np.linalg.eigvalsh(kn);uu=np.linalg.eigvalsh(un);ll=np.linalg.eigvalsh(lo)
 C=np.linalg.cholesky(kn);ci=np.linalg.inv(C);theta=np.linalg.eigvalsh(ci@un@ci.T)
 margin=1-float(theta[-1]);margin_note='double precision diagnostic';trace_lower=None;relative_gate=None;rayleigh_upper=None
 if margin < 1e-12:
  import mpmath as mp
  invlower=lower.solve(arb_mat(np.eye(nh,dtype=int).tolist()),algorithm='precond')
  trace=sum((invlower[i,i] for i in range(nh)),arb(0))
  kmax=arb(1)+nh*arb('1e-20') # certified from the entrywise normalization gate
  trace_lower=(1/(trace*kmax)).lower().str(40)
  print('TRACE_MARGIN_LOWER',lam,trace_lower,flush=True)
  scale=max((abs(t).upper() for row in invlower.tolist() for t in row),key=lambda t:float(t.log()))
  with mp.workdps(100):
   mm=mp.matrix([[mp.mpf((invlower[i,j]/scale).mid().str(120,radius=False)) for j in range(nh)] for i in range(nh)])
   evals,evecs=mp.eigsy(mm);largest=evals[nh-1,0]
   # Kn is interval-certified entrywise within 1e-20 of I: this ordinary
   # lower-matrix estimate agrees with its generalized margin to relative
   # error at most nh*1e-20, apart from numerical midpoint calculation.
   est=1/(largest*mp.mpf(scale.mid().str(120,radius=False)))
   margin=float(est);delta=arb(mp.nstr(est*mp.mpf('0.99'),80))
   relative_gate=ldl(sym(lower-delta*Kn))[0]
   assert relative_gate['status']=='PASS',relative_gate
   relative_gate['certified_delta']=delta.str(50)
   vv=arb_mat([[arb(mp.nstr(evecs[i,nh-1],100)).mid()] for i in range(nh)])
   rq=(vv.transpose()*lower*vv)[0,0]/(vv.transpose()*Kn*vv)[0,0]
   assert rq>0 and rq<arb(mp.nstr(est*mp.mpf('1.01'),80)),rq
   rayleigh_upper=rq.upper().str(60)
   payload={'bits':bits,'lambda':lam,'K_normalized':dumpmat(Kn),'Schur_normalized':dumpmat(lower),'probe':dumpmat(vv),'delta':delta.str(120)}
   (BASE/f'window_scaling_l{lam}_metric_witness_b{bits}.json').write_text(json.dumps(payload)+'\n')
  margin_note='100-digit inverse eigenvalue diagnostic; Kn differs from I entrywise by <1e-20; 99-percent threshold interval-certified'
 condlog=lognorm(V)+lognorm(V.inv());kmnlog=-2*lognorm(V);umaxlog=lognorm(K-Somit)
 out={'lambda':lam,'parity':parity,'head_cut':H,'head_dimension':nh,'retained_cut':ret,'omitted_test_cut':omit,'bits':bits,'arch_series_terms':192,'finite_head_sign_interval_certified':True,'complete_inverse_upper_available_in_this_probe':False,'finite_tail_sign_certified':True,'dimensionless_generalized_margin_FINITE':margin,'margin_evaluation':margin_note,'finite_trace_inverse_margin_lower':trace_lower,'finite_relative_margin_gate':relative_gate,'finite_relative_margin_rayleigh_upper':rayleigh_upper,'lambda_min_K_normalized_FINITE':float(kk[0]),'lambda_min_lower_over_lambda_min_K_FINITE':float(ll[0]/kk[0]) if margin_note.startswith('double') else None,'norm_U_over_lambda_min_K_FINITE':float(max(abs(uu))/kk[0]),'log10_condition_V_diagnostic':condlog,'log10_lambda_min_K_raw_diagnostic':kmnlog,'log10_norm_U_raw_diagnostic':umaxlog,'per_direction_relative_corrections_FINITE':[float(x) for x in theta],'worst_direction_headroom_FINITE':1/(1-margin),'reference_first_column_headroom_FINITE':float(Kn[0,0].mid()/Un[0,0].mid()),'best_direction_reporting_threshold':1e-14,'best_resolved_direction_headroom_FINITE':1/min(float(x) for x in theta if x>1e-14),'seconds':time.time()-start,'scope':'Finite Galerkin correction Kret-Somit only. It omits every mode beyond omitted_test_cut and is not the complete residual majorant. Diagnostics do not certify a cofinal-family error.'}
 (BASE/f'window_scaling_l{lam}_{parity}_r{ret}_o{omit}_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--lambda-value',type=int);p.add_argument('--parity',default='even');p.add_argument('--bits',type=int,default=4096);s=p.parse_args()
 if s.lambda_value:finite_probe(s.lambda_value,s.parity,bits=s.bits)
 else:
  report=[far_cuts(lam) for lam in [3,4,5,6,8]]
  (BASE/'window_scaling_far_cuts_b320.json').write_text(json.dumps(report,indent=2)+'\n')
  print(json.dumps(report,indent=2),flush=True)
  for lam in [3,4,5,6,8]:finite_probe(lam,bits=s.bits)
