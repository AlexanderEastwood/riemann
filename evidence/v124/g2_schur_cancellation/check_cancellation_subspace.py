"""Audit uniqueness of cancellation using the actual lambda3 even Fourier form.
Eigenvectors only propose exact dyadic witnesses. All assertions use Arb.
"""
from assembly_general import *
import mpmath as mp,argparse,hashlib
BASE=Path(__file__).parent

def positive2(A):
 return A[0,0]>0 and A[0,0]*A[1,1]-A[0,1]**2>0

def run(bits=768):
 L,b,d,a=sequences(3,64,bits);idx=list(range(65));W=block(idx,idx,'even',b,d)
 pi=arb.pi();h=(L/4).sinh()**2
 pp=[(arb(m).log(),arb(p).log()/arb(m).sqrt()) for m,p in pairs(3)]
 bp=[];dp=[];bt=[];dt=[]
 for n in idx:
  t=2*pi*n/L;den=L*L+16*pi*pi*n*n
  bp.append(32*L*h*n/den);dp.append(32*L*h*(L*L-16*pi*pi*n*n)/(den*den))
  bt.append(sum(((t*y).sin()*w for y,w in pp),arb(0))/pi)
  dt.append(-2*sum(((t*y).cos()*(1-y/L)*w for y,w in pp),arb(0)))
 ba=[b[n]-bp[n]-bt[n] for n in idx]
 Arch=block(idx,idx,'even',ba,a);Pole=block(idx,idx,'even',bp,dp);Prime=block(idx,idx,'even',bt,dt)
 assert all((W[i,j]-Arch[i,j]-Pole[i,j]-Prime[i,j]).contains(0) for i in idx for j in idx)
 path=BASE/'cancellation_two_mode_witness.json'
 if path.exists():w=json.loads(path.read_text());nums=w['numerators'];den_exp=w['denominator_exponent']
 else:
  mp.mp.dps=110;wm=mp.matrix([[mp.mpf(W[i,j].mid().str(112,radius=False)) for j in idx] for i in idx]);E,V=mp.eigsy(wm)
  print('Eigenvalue proposals',[mp.nstr(E[k],30) for k in range(5)],flush=True)
  den_exp=300;nums=[[str(int(mp.nint(V[i,j]*mp.mpf(2)**den_exp))) for j in range(2)] for i in idx]
  w={'lambda':3,'N':64,'parity':'even','denominator_exponent':den_exp,'numerators':nums,'scope':'Exact dyadic two-dimensional trial subspace, not asserted to be invariant or an exact eigenspace.'};path.write_text(json.dumps(w,indent=2)+'\n')
 V=arb_mat([[arb(n)*arb(2)**(-den_exp) for n in row] for row in nums]);G=V.transpose()*V
 Q=V.transpose()*W*V;QA=V.transpose()*Arch*V;QP=V.transpose()*Pole*V;QT=V.transpose()*Prime*V
 out={'bits':bits,'lambda':3,'N':64,'parity':'even','witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'matrices':{name:[[A[i,j].str(90) for j in range(2)] for i in range(2)] for name,A in [('Gram',G),('Weil',Q),('Arch',QA),('Pole',QP),('Prime',QT)]}}
 print(json.dumps(out,indent=2),flush=True)
 assert positive2(G)
 for threshold in ['1e-10','1e-15','1e-20','1e-25','1e-30']:
  eps=arb(threshold);out['absolute_Weil_bound_'+threshold]=positive2(eps*G-Q) and positive2(eps*G+Q)
 for threshold in ['0.001','0.01','0.02','0.04']:
  c=arb(threshold);out['Arch_lower_'+threshold]=positive2(QA-c*G)
 candidate=json.loads((BASE/'g2_finite_candidate.json').read_text())
 assert hashlib.sha256((BASE/'g2_finite_candidate.json').read_bytes()).hexdigest()=='6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e'
 coeff=candidate['positive_coefficients'];cv=arb_mat([[arb(t)*(arb(2).sqrt() if i else 1)] for i,t in enumerate(coeff)])
 cnorm=(cv.transpose()*cv)[0,0]
 out['frozen_source_energies']={name:((cv.transpose()*A*cv)[0,0]/cnorm).str(75) for name,A in [('Weil',W),('Arch',Arch),('Pole',Pole),('Prime',Prime),('Nonprime',Arch+Pole)]}
 proj=V.transpose()*cv;x=arb_mat([[-proj[1,0]],[proj[0,0]]]);norm2=(x.transpose()*G*x)[0,0];assert norm2>0
 energies={name:(x.transpose()*A*x)[0,0]/norm2 for name,A in [('Weil',Q),('Arch',QA),('Pole',QP),('Prime',QT),('Nonprime',QA+QP)]}
 # The exact algebraic construction x=(-<v1,c>,<v0,c>) makes Vx orthogonal to c.
 normbounds={}
 for name,A in [('Weil',W),('Prime',Prime),('Nonprime',Arch+Pole)]:
  rows=[sum((abs(A[i,j]) for j in idx),arb(0)) for i in idx]
  bound=rows[0].upper()
  for y in rows:
   if y.upper()>bound:bound=y.upper()
  assert all(bound>=y.upper() for y in rows)
  normbounds[name]=bound
 # Previously certified rank-one projector distance to the exact P64 repaired source.
 prior=json.loads((BASE/'pswf_source_certificate.json').read_text())
 assert prior['frozen_candidate_sha256']==hashlib.sha256((BASE/'g2_finite_candidate.json').read_bytes()).hexdigest()
 delta=arb('4e-36');assert arb(prior['normalized_projector_distance_bound'])<delta
 # Orthogonal projection and renormalization move the unit vector by <2delta.
 # For a bounded selfadjoint matrix H, unit-vector quadratic values change by <=4delta||H||.
 final_weil=abs(energies['Weil'])+4*delta*normbounds['Weil']
 final_weil_lower=energies['Weil']-4*delta*normbounds['Weil']
 final_nonprime=energies['Nonprime']-4*delta*normbounds['Nonprime']
 final_prime=energies['Prime']+4*delta*normbounds['Prime']
 assert final_weil_lower>0 and final_weil<arb('3e-31') and final_nonprime>arb('0.4') and final_prime<arb('-0.4')
 out['source_orthogonal_witness']={'candidate_energies':{k:v.str(75) for k,v in energies.items()},'finite_operator_norm_upper':{k:v.str(50) for k,v in normbounds.items()},'exact_source_transfer':{'uses_prior_projector_bound':'4e-36','Weil_lower':final_weil_lower.str(75),'absolute_Weil_upper':final_weil.str(75),'Nonprime_lower':final_nonprime.str(75),'Prime_upper':final_prime.str(75),'all_strict_gates':True},'scope':'Existence of a unit even Fourier polynomial in E64 exactly orthogonal to the literal repaired source p3, by projection to its exact normalized P64 vector. Full quadratic forms equal their finite-support matrix values. No infinite-operator residual or invariant-subspace assertion.'}
 (BASE/f'cancellation_subspace_b{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out['source_orthogonal_witness'],indent=2),flush=True)
 print({k:v for k,v in out.items() if isinstance(v,bool)},flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--bits',type=int,default=768);run(**vars(p.parse_args()))
