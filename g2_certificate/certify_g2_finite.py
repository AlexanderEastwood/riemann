#!/usr/bin/env python3
"""Arb interval certificate for the exact finite Weil matrix lambda=3,N=64.

Requires python-flint==0.9.0 and g2_finite_candidate.json. Does not require
mpmath, source quadrature, a zeta zero list, or an RH assumption. All pass/fail
conditions compare rigorous Arb enclosures; no approximate solve is used.
"""
import hashlib,json,time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,acb,arb_mat,fmpq,ctx

BASE=Path(__file__).resolve().parent
ctx.prec=512


def exact_decimal(s):
    f=Fraction(s)
    return arb(fmpq(f.numerator,f.denominator))


def eye(n):
    return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])


def ldl_certificate(matrix,label):
    """All positive interval pivots imply positivity of the exact symmetric input."""
    n=matrix.nrows(); lower=[[arb(0) for _ in range(n)] for _ in range(n)]
    pivots=[]
    for j in range(n):
        pivot=matrix[j,j]-sum((lower[j][k]**2*pivots[k] for k in range(j)),arb(0))
        if not pivot>0:
            raise ArithmeticError(f'{label}: pivot {j} not certified positive: {pivot}')
        pivots.append(pivot); lower[j][j]=arb(1)
        for i in range(j+1,n):
            lower[i][j]=(matrix[i,j]-sum((lower[i][k]*lower[j][k]*pivots[k] for k in range(j)),arb(0)))/pivot
    print(f'{label}: {n} strictly positive interval pivots',flush=True)
    return [p.str(50) for p in pivots]


def assemble():
    L=2*arb(3).log(); pi=arb.pi(); nmax=64; ii=acb(0,1)
    primes=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
    pdat=[(arb(m).log(),arb(p).log()/arb(m).sqrt()) for m,p in primes]
    bs=[]; ds=[]; integrals=[]
    tol=exact_decimal('1e-120')
    for n in range(nmax+1):
        t=2*pi*n/L
        # sinh(y)/y = sinc(i*y). Both rewritten integrands extend at zero.
        def fb(y,analytic):
            return t/2*(y/2).exp()*(t*y).sinc()/(ii*y).sinc()
        def fd(y,analytic):
            return (y/2).exp()/(ii*y).sinc()*(-t*t*y/2*(t*y/2).sinc()**2
                +(-y/4).exp()*(ii*y/4).sinc()/2-(t*y).cos()/L)
        bi=acb(0) if n==0 else acb.integral(fb,0,L,abs_tol=tol,rel_tol=tol,eval_limit=1000000)
        di=acb.integral(fd,0,L,abs_tol=tol,rel_tol=tol,eval_limit=1000000)
        if not (bi.is_finite() and di.is_finite()): raise ArithmeticError('Non-finite integral')
        if not (bi.imag.contains(0) and di.imag.contains(0)): raise ArithmeticError('Unexpected complex integral')
        denom=L*L+16*pi*pi*n*n
        pointb=32*L*(L/4).sinh()**2*n/denom
        b=pointb+(bi.real+sum(((t*y).sin()*v for y,v in pdat),arb(0)))/pi
        pole=32*L*(L/4).sinh()**2*(L*L-16*pi*pi*n*n)/denom**2
        prime=2*sum(((t*y).cos()*(1-y/L)*v for y,v in pdat),arb(0))
        arch=di.real+(4*pi).log()+arb.const_euler()+(L/2).tanh().log()
        bs.append(b); ds.append(pole-prime-arch)
        integrals.append(dict(n=n,sine_integral=bi.real.str(140),diagonal_integral=di.real.str(140)))
        if n%16==0:print(f'Certified archimedean integrals through n={n}',flush=True)
    def entry(n,m):
        if n==m:return ds[abs(n)]
        bn=bs[abs(n)] if n>=0 else -bs[abs(n)]
        bm=bs[abs(m)] if m>=0 else -bs[abs(m)]
        return (bn-bm)/(n-m)
    we=arb_mat(nmax+1,nmax+1); wo=arb_mat(nmax,nmax); root2=arb(2).sqrt()
    for n in range(nmax+1):
        for m in range(nmax+1):
            if n==m==0:we[n,m]=entry(0,0)
            elif n==0 or m==0:we[n,m]=root2*entry(n,m)
            else:we[n,m]=entry(n,m)+entry(n,-m)
    for n in range(1,nmax+1):
        for m in range(1,nmax+1):wo[n-1,m-1]=entry(n,m)-entry(n,-m)
    return L,we,wo,integrals


def main():
    started=time.time(); path=BASE/'g2_finite_candidate.json'
    source=json.loads(path.read_text())
    assert source['N']==64 and source['lambda_exact']=='3'
    co=[exact_decimal(x) for x in source['positive_coefficients']]
    assert len(co)==65
    norm=(co[0]**2+2*sum((x*x for x in co[1:]),arb(0))).sqrt()
    u=arb_mat([[co[0]/norm]]+[[arb(2).sqrt()*x/norm] for x in co[1:]])
    L,we,wo,integrals=assemble()
    alpha=(u.transpose()*we*u)[0,0]
    # Stable Householder: v=u+e_0, H u=-e_0; columns 1..64 span u-perp.
    v=arb_mat(u); v[0,0]+=1
    denominator=(v.transpose()*v)[0,0]
    assert denominator>1
    house=eye(65)-2*v*v.transpose()/denominator
    basis=arb_mat([[house[i,j] for j in range(1,65)] for i in range(65)])
    C=basis.transpose()*we*basis
    r=basis.transpose()*we*u
    A=C-alpha*eye(64)
    gamma=exact_decimal('1e-34')
    even_pivots=ldl_certificate(A-gamma*eye(64),'even complement minus alpha minus gamma')
    odd_pivots=ldl_certificate(wo-(alpha+gamma)*eye(64),'odd block minus alpha minus gamma')
    z=A.solve(r,algorithm='lu')
    q=(z.transpose()*z)[0,0].sqrt()
    energy=(z.transpose()*r)[0,0]
    lower=alpha-energy
    sine=q/(1+q*q).sqrt()
    checks=dict(complement_gap_at_least_1e_minus34=True,
        schur_tangent_below_0_000216=bool(q<exact_decimal('0.000216')),
        ground_lower_bound_above_3_64e_minus38=bool(lower>exact_decimal('3.64e-38')),
        rayleigh_upper_bound_below_5_32e_minus38=bool(alpha<exact_decimal('5.32e-38')))
    if not all(checks.values()):raise ArithmeticError(f'Final inequality failed: {checks}')
    row=dict(status='PASS: rigorous Arb enclosures for exact finite matrix and explicitly frozen rational candidate.',
        scope='Not a true-PSWF approximation certificate, infinite Fourier-complement theorem, continuum positivity theorem, G2 closure or RH proof.',
        lambda_exact=3,N=64,dimension=129,precision_bits=ctx.prec,python_flint_version=flint.__version__,
        flint_version=str(getattr(flint,'__FLINT_VERSION__','unknown')),
        candidate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        matrix_definition='Correct CCM logarithmic diagonal and all prime powers 2,3,4,5,7,8,9; exact L=2log(3).',
        integration_absolute_and_relative_tolerance='1e-120',
        first_slot_linear=True,
        alpha=alpha.str(65),complement_gap_certified_lower='1e-34',
        q=q.str(65),sin_angle_bound=sine.str(65),schur_energy=energy.str(65),
        ground_eigenvalue_lower_bound=lower.str(65),checks=checks,
        source_norm=norm.str(65),candidate_endpoint=((co[0]+2*sum(co[1:],arb(0)))/L.sqrt()).str(65),
        even_complement_pivots=even_pivots,odd_block_pivots=odd_pivots,
        elapsed_seconds=round(time.time()-started,3))
    (BASE/'g2_finite_certificate.json').write_text(json.dumps(row,indent=2)+'\n')
    (BASE/'g2_finite_matrix_intervals.json').write_text(json.dumps(dict(
        status='Certified entrywise enclosures from Arb; decimal export includes radii.',
        even_matrix=[[we[i,j].str(140) for j in range(65)] for i in range(65)],
        odd_matrix=[[wo[i,j].str(140) for j in range(64)] for i in range(64)],
        integrals=integrals),indent=2)+'\n')
    print(json.dumps({k:v for k,v in row.items() if not k.endswith('pivots')},indent=2),flush=True)


if __name__=='__main__':main()
