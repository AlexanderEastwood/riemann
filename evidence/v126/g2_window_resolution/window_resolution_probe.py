"""Cutoff/head resolution audit. Every sign here is finite dimensional."""
from window_scaling_probe import *
import mpmath as mp

def gate_scaled(A):
 V=congruence(A);assert all(V[i,i]>0 for i in range(A.nrows()))
 C=sym(V.transpose()*A*V);g=ldl(C)[0];assert g['status']=='PASS',g
 return g

def run(lam=8,head=64,cuts=(256,384,512),bits=4096,terms=256):
 start=time.time();prefix=f'resolution_l{lam}_h{head}_cuts'+('_'.join(map(str,cuts)))+f'_b{bits}_k{terms}'
 L,b,d,a=sequences(lam,max(cuts),bits,K=terms);hs=list(range(head+1));F=block(hs,hs,'even',b,d)
 print('assembled',prefix,round(time.time()-start,1),flush=True)
 forms={};data={'lambda':lam,'head':head,'cuts':list(cuts),'bits':bits,'arch_terms':terms,'certificates':[],'scope':'Nested finite Galerkin Schur forms only; no rows beyond largest cut and no complete inverse upper bound.'}
 for M in cuts:
  ts=list(range(head+1,M+1));B=block(ts,hs,'even',b,d);T=block(ts,ts,'even',b,d)
  tgate=finite_tail_gate(T);X=T.solve(B,algorithm='precond');S=sym(F-B.transpose()*X);sgate=gate_scaled(S)
  forms[M]=S
  data['certificates'].append({'cut':M,'tail_positive':tgate,'Schur_gate':sgate})
  print('Schur certified',M,round(time.time()-start,1),flush=True)
 (BASE/(prefix+'_forms.json')).write_text(json.dumps({'metadata':data,'forms':{str(M):dumpmat(S,1100) for M,S in forms.items()}})+'\n')
 data['comparisons']=[]
 for left,right in zip(cuts,cuts[1:]):
  K=forms[left];S=forms[right];V=congruence(K);Kn=sym(V.transpose()*K*V);Sn=sym(V.transpose()*S*V);dim=Kn.nrows()
  assert all(abs(Kn[i,j]-int(i==j))<arb('1e-30') for i in range(dim) for j in range(dim))
  Inv=Sn.solve(arb_mat([[int(i==j) for j in range(dim)] for i in range(dim)]),algorithm='precond')
  scale=max((abs(t).upper() for row in Inv.tolist() for t in row),key=lambda t:float(t.log()))
  with mp.workdps(200):
   num=mp.matrix([[mp.mpf((Inv[i,j]/scale).mid().str(230,radius=False)) for j in range(dim)] for i in range(dim)])
   ev,vec=mp.eigsy(num);est=1/(ev[dim-1,0]*mp.mpf(scale.mid().str(230,radius=False)))
   delta=arb(mp.nstr(est*mp.mpf('.99'),180));g=gate_scaled(sym(Sn-delta*Kn))
   z=arb_mat([[arb(mp.nstr(vec[i,dim-1],200)).mid()] for i in range(dim)])
   den=(z.transpose()*Kn*z)[0,0];assert den>0
   rq=(z.transpose()*Sn*z)[0,0]/den;assert rq>0 and rq<arb(mp.nstr(est*mp.mpf('1.01'),180))
   diagnostic=mp.nstr(est,60)
  record={'retained_cut':left,'test_cut':right,'margin_diagnostic':diagnostic,'margin_lower':delta.lower().str(90),'margin_upper':rq.upper().str(90),'lower_gate':g,'congruence_log10_condition_diagnostic':lognorm(V)+lognorm(V.inv()),'K_normalization_entrywise_error_upper':max((abs(Kn[i,j]-int(i==j)).upper() for i in range(dim) for j in range(dim))).str(20)}
  data['comparisons'].append(record)
  witness={'left':left,'right':right,'K':dumpmat(Kn,1100),'S':dumpmat(Sn,1100),'probe':dumpmat(z,1100),'delta':delta.str(300)}
  (BASE/(prefix+f'_metric_{left}_{right}.json')).write_text(json.dumps(witness)+'\n')
  print('MARGIN',json.dumps(record),flush=True)
 data['seconds']=time.time()-start;(BASE/(prefix+'_report.json')).write_text(json.dumps(data,indent=2)+'\n');return data
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--lambda-value',type=int,default=8);p.add_argument('--head',type=int,default=64);p.add_argument('--cuts',type=int,nargs='+',default=[256,384,512]);p.add_argument('--bits',type=int,default=4096);p.add_argument('--terms',type=int,default=256);s=p.parse_args();run(s.lambda_value,s.head,s.cuts,s.bits,s.terms)
