#!/usr/bin/env python3
"""Rigorous infinite PSWF / repaired source / finite projection certificate.

Requires python-flint==0.9.0. Input rational coefficients are not assumed accurate.
Run without -O; assertions are strict interval verification gates.
"""
import json,hashlib,math
from pathlib import Path
from fractions import Fraction
import flint
from flint import arb,acb,fmpq,ctx
ctx.prec=768
BASE=Path(__file__).resolve().parent
PREV=BASE.parent/'g2_certificate'
def exact(s):
 f=Fraction(s);return arb(fmpq(f.numerator,f.denominator))
def upper(x):return abs(x).upper()
def norm(v):return sum((x*x for x in v),arb(0)).sqrt()
def dump(x):return x.str(60)
def positive(x):assert x>0;return x

def main():
 inp=BASE/'pswf_rational_input.json'; data=json.loads(inp.read_text());M=data['even_dimension']
 lam=arb(3); L=2*lam.log(); c=18*arb.pi(); c2=c*c
 def a(l):return arb(l+1)/arb((2*l+1)*(2*l+3)).sqrt() if l>=0 else arb(0)
 diag=[arb(2*k*(2*k+1))+c2*(a(2*k)**2+a(2*k-1)**2) for k in range(M)]
 off=[c2*a(2*k)*a(2*k+1) for k in range(M)]
 tailbase=arb(2*M*(2*M+1))
 def count(x,subtract):
  # LDL of finite tridiagonal Schur upper/lower bounding matrices.
  correction=off[-1]**2/positive(tailbase-x) if subtract else arb(0)
  pivots=[]; negative=0
  for k in range(M):
   p=diag[k]-x-(off[k-1]**2/pivots[-1] if k else 0)-(correction if k==M-1 else 0)
   assert p>0 or p<0, f'Unresolved inertia pivot {k}'
   negative+=int(p<0);pivots.append(p)
  return negative
 rows=[]; polys=[]; deltas=[]; uniforms=[]
 for row in data['rows']:
  xi=exact(row['xi']); v=[exact(x) for x in row['coefficients']]; vn=norm(v);v=[x/vn for x in v]
  expect=row['mode']//2
  counts=[]
  for x,n in [(xi-1,expect),(xi+1,expect+1)]:
   pair=[count(x,False),count(x,True)];assert pair==[n,n];counts.append(pair)
  residual=[]
  for k in range(M):
   residual.append((diag[k]-xi)*v[k]+(off[k-1]*v[k-1] if k else 0)+(off[k]*v[k+1] if k<M-1 else 0))
  residual.append(off[-1]*v[-1]) # full infinite residual includes omitted link
  eps=norm(residual).upper();assert eps<exact('1e-30')
  delta=(arb(2).sqrt()*eps).upper() # distance of all other eigenvalues from xi is >=1
  unif=(2*eps+(1+upper(xi)+c2)*delta).upper()
  poly=[v[k]*(arb(4*k+1)/2).sqrt()/lam.sqrt() for k in range(M)]
  center=sum((poly[k]*exact(Fraction((-1)**k*math.comb(2*k,k),4**k)) for k in range(M)),arb(0))
  assert center>unif/lam.sqrt() # exact true sign is positive at zero
  rows.append(dict(mode=row['mode'],xi=dump(xi),inertia_at_xi_minus_and_plus_one=counts,
   full_infinite_residual_bound=dump(eps),angular_L2_error_bound=dump(delta),angular_uniform_error_bound=dump(unif),physical_center_approx=dump(center),omitted_link=dump(residual[-1])))
  polys.append(poly);deltas.append(delta);uniforms.append((unif/lam.sqrt()).upper())
 print('Mode bounds',rows,flush=True)
 p0,p4=polys; d0,d4=deltas;u0,u4=uniforms
 # Physical modal integrals = 2 lambda times constant Legendre coefficient.
 a0=-2*lam*p4[0];a4=2*lam*p0[0]
 da0=(2*lam).sqrt()*d4;da4=(2*lam).sqrt()*d0
 hsup0=sum(map(upper,p0),arb(0));hsup4=sum(map(upper,p4),arb(0))
 eta=((upper(a0)+da0)*u0+da0*hsup0+(upper(a4)+da4)*u4+da4*hsup4).upper()
 hc=[a0*p0[k]+a4*p4[k] for k in range(M)]
 z=sum((hc[k]*exact(Fraction((-1)**k*math.comb(2*k,k),4**k)) for k in range(M)),arb(0))
 # Exact smooth bump: C=I0/I2. I0<=b and I2>=b^3/128 give |psi|<=129.
 bump=arb(129)
 repaired=(eta+(upper(z)+eta)*bump).upper()
 source_norm_error=(lam**3*L).sqrt()*repaired
 print('Raw/repaired source uniform bounds',dump(eta),dump(repaired),'center',dump(z),flush=True)
 # Convert the finite polynomial to monomials using exact factorial coefficients.
 mon=[]
 for r in range(M):
  value=arb(0)
  for k in range(r,M):
   frac=Fraction((-1)**(k-r)*math.factorial(2*k+2*r),2**(2*k)*math.factorial(k-r)*math.factorial(k+r)*math.factorial(2*r))
   value+=hc[k]*exact(frac)
  mon.append(value)
 bs=[sum((arb(m)**(2*r) for m in range(1,10)),arb(0))/lam**(4*r)/lam.sqrt() for r in range(M)]
 co=[]
 for n in range(65):
  t=2*arb.pi()*n/L
  aa=lam.sqrt()*sum(((-acb(arb(1)/2,t)*arb(m).log()).exp() for m in range(1,10)),acb(0))
  val=sum((mon[r]*(aa-bs[r])/acb(arb(2*r)+arb(1)/2,t) for r in range(M)),acb(0)).real/L.sqrt()
  co.append(val)
 oldpath=PREV/'g2_finite_candidate.json'; old=json.loads(oldpath.read_text()); frozen=[exact(x) for x in old['positive_coefficients']]
 assert hashlib.sha256(oldpath.read_bytes()).hexdigest()=='6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e'
 poly_diff=norm([co[0]-frozen[0]]+[(co[k]-frozen[k])*arb(2).sqrt() for k in range(1,65)]).upper()
 err=(source_norm_error+poly_diff).upper()
 frozen_norm=norm([frozen[0]]+[arb(2).sqrt()*x for x in frozen[1:]])
 assert frozen_norm>err
 projector_error=(err/(frozen_norm-err)).upper()
 oldcertpath=PREV/'g2_finite_series_certificate.json'
 oldcert=json.loads(oldcertpath.read_text())
 assert oldcert['candidate_sha256']==hashlib.sha256(oldpath.read_bytes()).hexdigest()
 assert oldcert['lambda_exact']==3 and oldcert['N']==64 and oldcert['dimension']==129
 assert oldcert['status'].startswith('PASS') and all(oldcert['checks'].values())
 q=arb(oldcert['q']); assert q>0 and q<exact('.000216')
 sinbound=(q/(1+q*q).sqrt()+projector_error).upper()
 assert sinbound<exact('.000216')
 # Direct finite-polynomial endpoint, no smoothing or equal-coefficient substitute.
 def legendre_value(x):
  prev=arb(1);cur=x;v=hc[0]
  for degree in range(2,2*M-1):
   new=((2*degree-1)*x*cur-(degree-1)*prev)/degree
   if degree%2==0:v+=hc[degree//2]*new
   prev,cur=cur,new
  return v
 Bhat=(lam.sqrt()*sum(hc,arb(0))+sum((legendre_value(arb(m)/9) for m in range(1,9)),arb(0))/lam.sqrt())/2
 Berr=(lam.sqrt()*eta+8/lam.sqrt()*repaired)/2
 B=Bhat+arb(0,Berr.upper());assert B>0
 projected=(co[0]+2*sum(co[1:],arb(0)))/L.sqrt()
 projected_error=(arb(129)/L).sqrt()*source_norm_error
 projected+=arb(0,projected_error.upper())
 relative=abs(projected-B)/B
 assert relative>exact('1.374') and relative<exact('1.375')
 assert err<exact('2.60e-36')
 assert projector_error<exact('4e-36')
 assert B>exact('5.58669e-19') and B<exact('5.58670e-19')
 result=dict(status='PASS: infinite PSWF/source certification and exact projected-source ground-angle transfer at lambda=3,N=64.',
  scope='Fixed parameters only; no growing-window bound, omitted Fourier positivity, endpoint recovery, graph/full-strip transfer, G2 closure or RH proof.',
  precision_bits=ctx.prec,python_flint_version=flint.__version__,flint_version=str(flint.__FLINT_VERSION__),
  input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),prior_weil_certificate_sha256=hashlib.sha256(oldcertpath.read_bytes()).hexdigest(),frozen_candidate_sha256=hashlib.sha256(oldpath.read_bytes()).hexdigest(),
  modes=rows,raw_source_uniform_error=dump(eta),raw_source_center_approx=dump(z),bump_sup_bound='129',
  repaired_source_vs_raw_polynomial_uniform_error=dump(repaired),
  finite_polynomial_coefficients_vs_frozen_norm=dump(poly_diff),
  exact_repaired_source_projection_vs_frozen_norm_bound=dump(err),
  normalized_projector_distance_bound=dump(projector_error),
  true_projected_source_ground_angle_sine_bound=dump(sinbound),
  physical_endpoint=dump(B),projected_endpoint=dump(projected),relative_physical_endpoint_error=dump(relative),
  checks=dict(full_infinite_spectral_counts=True,full_residual_includes_tail=True,positive_true_modal_centers=True,
  exact_source_coefficient_error_below_2_60e_minus36=True,normalized_projector_distance_below_4e_minus36=True,true_projected_source_angle_below_0_000216=True,
  physical_endpoint_positive=True,relative_endpoint_error_between_1_374_and_1_375=True))
 (BASE/'pswf_source_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
 (BASE/'source_polynomial_intervals.json').write_text(json.dumps(dict(legendre_coefficients=[dump(x) for x in hc],projected_positive_coefficients=[dump(x) for x in co]),indent=2)+'\n')
 print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
