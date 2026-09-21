"""Directional mixed inverse diagnostic, with exact frozen inputs and Arb actions.

Finite-prefix mixed values are explicitly NOT complete-tail certificates.
"""
from refine_inverse import *
from structured_low_schur import readz
import hashlib

def run(J=65536,bits=768,degree=1):
 begin=time.time();L,b,d,a=sequences(4,J,bits);N=512;Mi=1024;M=256;c=arb(1)/10**8
 def stamp(s):print(s,round(time.time()-begin,2),flush=True)
 w=json.loads((OLD/'structured_ceiling_counterwitness.json').read_text())
 v=arb_mat([[arb(x)/arb(2)**w['denominator_exponent']] for x in w['numerators']])
 sw,X,xhash=readz(OLD/'low_witness_even_M256_b768.json.gz')
 xv=X*v;f=[v[i,0] if i<17 else -xv[i-17,0] for i in range(M+1)]
 fv=arb_mat([[x] for x in f]);K=(fv.transpose()*block(list(range(M+1)),list(range(M+1)),'even',b,d)*fv)[0,0]
 # Complete W f on retained rows, using finite support of f.
 wf=action(f[1:]+[arb(0)]*(J-M),1,'even',b,d,a,arb(0))
 for n in range(1,J+1):wf[n-1]+=arb(2).sqrt()*b[n]/n*f[0]
 dense=block(list(range(17,42)),list(range(M+1)),'even',b,d)*fv
 assert all(wf[16+i].overlaps(dense[i,0]) for i in range(25))
 h=arb_mat([[wf[n-1]] for n in range(17,N+1)]);k=wf[N:]
 stamp('source action')
 iw,Z,ihash=readz(OLD.parent/'g2_weighted_signed/weighted_witness_l4_s16_even_b256.json.gz')
 report=json.loads((OLD.parent/'g2_weighted_signed/weighted_tail_l4_s16_even_b320.json').read_text())
 assert report['status']=='PASS' and report['witness_sha256']==ihash
 assert arb(report['Gershgorin_margin'])>arb('0.9999999999')
 C=arb_mat([[arb(float(x)) for x in row] for row in iw['C']])
 assert all(C[i,j].is_exact() for i in range(C.nrows()) for j in range(C.ncols()))
 di=N-16;ins=list(range(17,Mi+1))
 Gi=arb_mat([[int(i==j) if i<di else -Z[i-di,j] for j in range(di)] for i in range(len(ins))])
 ks=arb_mat([[k[i]] for i in range(Mi-N)])
 base=C*(h-Z.transpose()*ks)
 pm=prime_bound(4);RL=arb(64)/255;t=2*arb.pi()*(N+1)/L;kap=pm+2/t
 def err(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return (1-c)*((arb(n)/L).log()-err(2*arb.pi()*n/L))-kap
 gs=[g(n) for n in range(N+1,J+1)]
 z=[k[i]/gs[i] for i in range(len(k))]
 uz=action(z,N+1,'even',b,d,a,c)
 q=[z[i]-(uz[i]-gs[i]*z[i])/(20*gs[i]) for i in range(len(z))]
 V=sum((k[i]*z[i] for i in range(len(k))),arb(0))
 AP=sum((z[i]*(uz[i]-gs[i]*z[i]) for i in range(len(k))),arb(0))
 def pair_R(w):
  aw=action([arb(0)]*di+w,17,'even',b,d,a,c)
  av=arb_mat([[aw[i]] for i in range(Mi-16)])
  return C*Gi.transpose()*av
 b0=base-pair_R(z);b1=base-pair_R(q)
 e0=(b0.transpose()*b0)[0,0];e1=(b1.transpose()*b1)[0,0]
 stamp('finite mixed vectors')
 hh=arb(9)/16;pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bs=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 Uk=remote(fv,list(range(M+1)),M,J,64,'even',b,bs)[0,0]/g(J+1)
 Gc=Gi*C.transpose();URc=remote(Gc,ins,Mi,J,64,'even',b,bs)/g(J+1)
 rho=sum((URc[i,i] for i in range(di)),arb(0))
 stamp('remote input and residual Grams')
 mu=arb(9999999999)/10000000000
 # The old complete inner certificate gives Y*Y <= C K_Z C* - mu I.
 inner_trial=Gc.transpose()*block(ins,ins,'even',b,d,a,c)*Gc
 Ytrace=sum((inner_trial[i,i]-mu for i in range(di)),arb(0))
 assert Ytrace>0
 rows=[sum((abs(inner_trial[i,j]-(mu if i==j else 0)).upper() for j in range(di)),arb(0)).upper() for i in range(di)]
 Ynorm=rows[0]
 for row in rows[1:]:
  if row>Ynorm:Ynorm=row
 Ybound=Ynorm if Ynorm<Ytrace else Ytrace
 stamp('complete Y metric trace bound')
 tj=2*arb.pi()*(J+1)/L
 rup=pm+2/tj+arb.pi()/2+hh*L**3/(12*arb.pi()**4*J**3)
 nu=(kap+2*(1-c)*err(tj)+rup)/g(J+1)
 # Y=PY+QY, y=p+q. These bounds include both omitted input and output.
 assert nu<20
 mixed_error=(rho*Uk).sqrt()+((19*Ybound*nu*Uk).sqrt()+(rho*nu*AP).sqrt())/20
 mixed_upper=(e1.sqrt()+mixed_error)**2/mu
 low=AP.sqrt()-(nu*Uk).sqrt();aplo=low*low if low>0 else arb(0)
 complete_far_upper=V+Uk-aplo/20
 out={'status':'FINITE_PREFIX_DIAGNOSTIC_NOT_COMPLETE_MIXED_BOUND','J':J,'bits':bits,'K':K.str(80),'V':V.str(80),'AP':AP.str(80),'finite_first_far':(V-AP/20).str(80),'mixed_diag_prefix_squared':e0.str(80),'mixed_first_prefix_squared':e1.str(80),'remote_y_norm2_upper':Uk.str(80),'remote_Y_HS2_upper':rho.str(80),'finite_first_total':(V-AP/20+e1/mu).str(80),'base_norm2':(base.transpose()*base)[0,0].str(80),'outer_sha256':xhash,'inner_sha256':ihash,'seconds':time.time()-begin,'scope':'Q1 prefix has additional output beyond J; omitted k and mixed correlations are not zero.'}
 (BASE/f'mixed_probe_J{J}_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 # Vector checkpoint permits later certified directional lower bounds.
 data={'b0':[x[0].str(220) for x in b0.tolist()],'b1':[x[0].str(220) for x in b1.tolist()]}
 (BASE/f'mixed_vectors_J{J}_b{bits}.json').write_text(json.dumps(data)+'\n')
 out.update({'complete_Y_HS2_upper':Ytrace.str(80),'complete_Y_operator_norm2_upper':Ybound.str(80),'remote_H_norm_upper':nu.str(80),'complete_mixed_error_norm_upper':mixed_error.str(80),'complete_mixed_energy_upper':mixed_upper.str(80),'complete_far_energy_upper':complete_far_upper.str(80),'complete_structured_energy_upper':(complete_far_upper+mixed_upper).str(80),'status':'COMPLETE_DIRECTIONAL_UPPER_BOUND_INCONCLUSIVE'})
 trials=[{'degree':1,'finite_far':(V-AP/20).str(50),'finite_mixed_squared':e1.str(50),'finite_total':(V-AP/20+e1/mu).str(50)}]
 for order in range(2,degree+1):
  uq=action(q,N+1,'even',b,d,a,c)
  q=[z[i]/20+q[i]-uq[i]/(20*gs[i]) for i in range(len(q))]
  if order==degree or order in [2,4,8,16,32,64]:
   be=base-pair_R(q);en=(be.transpose()*be)[0,0];far=sum((k[i]*q[i] for i in range(len(k))),arb(0))
   trials.append({'degree':order,'finite_far':far.str(50),'finite_mixed_squared':en.str(50),'finite_total':(far+en/mu).str(50)})
   stamp('finite polynomial degree '+str(order))
 out['higher_polynomial_finite_diagnostics']=trials
 out['seconds']=time.time()-begin
 (BASE/f'mixed_probe_J{J}_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--J',type=int,default=65536);p.add_argument('--bits',type=int,default=768);p.add_argument('--degree',type=int,default=1);run(**vars(p.parse_args()))
