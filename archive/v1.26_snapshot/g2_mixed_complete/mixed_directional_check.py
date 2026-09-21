"""Rigorous one-direction lower test for the complete first-polynomial bound.

This tests a sufficient upper-bound method, not Weil positivity.
"""
from mixed_refinement import *

def check(J=65536,bits=768):
 begin=time.time();L,b,d,a=sequences(4,J,bits);N=512;Mi=1024;c=arb(1)/10**8
 data=json.loads((BASE/f'mixed_vectors_J{J}_b{bits}.json').read_text())
 bb=arb_mat([[arb(x)] for x in data['b1']]);bn=(bb.transpose()*bb)[0,0].sqrt()
 # A frozen exact dyadic vector: no dependence on interval sign guesses.
 qb=(bb/bn).mid()
 witness_path=BASE/f'mixed_directional_witness_J{J}.json'
 if witness_path.exists():qnums=json.loads(witness_path.read_text())['numerators']
 else:qnums=[int((qb[i,0]*arb(2)**160).floor().unique_fmpz()) for i in range(qb.nrows())]
 q=arb_mat([[arb(n)/arb(2)**160] for n in qnums])
 assert all(q[i,0].is_exact() for i in range(q.nrows()))
 qnorm=(q.transpose()*q)[0,0].sqrt()
 w,Z,whash=readz(OLD.parent/'g2_weighted_signed/weighted_witness_l4_s16_even_b256.json.gz')
 C=arb_mat([[arb(float(x)) for x in row] for row in w['C']]);di=496
 Gi=arb_mat([[int(i==j) if i<di else -Z[i-di,j] for j in range(di)] for i in range(1008)])
 source=Gi*C.transpose()*q
 zlist=[source[i,0] for i in range(source.nrows())]+[arb(0)]*(J-Mi)
 az=action(zlist,17,'even',b,d,a,c)
 pm=prime_bound(4);RL=arb(64)/255;t=2*arb.pi()*(N+1)/L;kap=pm+2/t
 def err(t):return 1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
 def g(n):return (1-c)*((arb(n)/L).log()-err(2*arb.pi()*n/L))-kap
 gs=[g(n) for n in range(N+1,J+1)]
 fy=[az[n-17] for n in range(N+1,J+1)];dz=[fy[i]/gs[i] for i in range(len(fy))]
 udz=action(dz,N+1,'even',b,d,a,c)
 eta=sum((dz[i]*(udz[i]-gs[i]*dz[i]) for i in range(len(dz))),arb(0))
 assert eta>0
 hh=arb(9)/16;pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bs=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 rho=remote(source,list(range(17,Mi+1)),Mi,J,64,'even',b,bs)[0,0]/g(J+1)
 p=json.loads((BASE/f'mixed_probe_J{J}_b{bits}.json').read_text())
 E=arb(p['remote_y_norm2_upper']);AP=arb(p['AP']);V=arb(p['V']);K=arb(p['K'])
 tj=2*arb.pi()*(J+1)/L;rup=pm+2/tj+arb.pi()/2+hh*L**3/(12*arb.pi()**4*J**3)
 nu=(kap+2*(1-c)*err(tj)+rup)/g(J+1)
 assert nu<20
 errbound=((nu*eta*E).sqrt()+(nu*AP*rho).sqrt())/20+(rho*E).sqrt()
 proj=(q.transpose()*bb)[0,0]
 lower=(proj-errbound)/qnorm
 mixedlo=lower**2 if lower>0 else arb(0)
 # Minimize v-a/m-2 sqrt(a nu)x/m+(1-nu/m)x^2 over x>=0.
 # This controls every possible remote input, even without its norm bound.
 farlo=V-AP/(20-nu)
 mu=arb('0.9999999999');total=farlo+mixedlo/mu
 metric_upper=mu*qnorm**2+(eta.sqrt()+(nu*rho).sqrt())**2/20
 improved_mixed_lower=(proj-errbound)**2/metric_upper if proj>errbound else arb(0)
 improved_total_lower=farlo+improved_mixed_lower
 out={'status':'COMPLETE_FIRST_POLYNOMIAL_SCALAR_MU_FAILURE' if total>K else 'INCONCLUSIVE_LOWER_TEST','J':J,'bits':bits,'eta_direction':eta.str(80),'rho_direction':rho.str(80),'tail_pairing_error_upper':errbound.str(80),'projection':proj.str(80),'qnorm':qnorm.str(80),'complete_mixed_energy_lower':(mixedlo/mu).str(80),'complete_far_energy_lower':farlo.str(80),'complete_total_lower':total.str(80),'K':K.str(80),'excess_lower':(total-K).str(80),'seconds':time.time()-begin,'scope':'Failure, if certified, is of Q1 with scalar mu head bound. It is not a negative Weil direction, true inverse failure, or failure of the strengthened matrix head metric.'}
 out.update({'strengthened_metric_quadratic_upper':metric_upper.str(80),'strengthened_mixed_energy_lower':improved_mixed_lower.str(80),'strengthened_total_lower':improved_total_lower.str(80),'strengthened_excess_lower':(improved_total_lower-K).str(80),'strengthened_status':'COMPLETE_FIRST_POLYNOMIAL_UPDATED_MU_HEAD_FAILURE' if improved_total_lower>K else 'INCONCLUSIVE','scope':'These gates reject first-polynomial majorants with the saved mu head certificate, including its exact positive update. They do not reject higher degree, a stronger initial head certificate, the true inverse, or Weil positivity.'})
 (BASE/f'mixed_directional_J{J}_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 (BASE/f'mixed_directional_witness_J{J}.json').write_text(json.dumps({'denominator_exponent':160,'numerators':qnums})+'\n')
 print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--J',type=int,default=65536);p.add_argument('--bits',type=int,default=768);check(**vars(p.parse_args()))
