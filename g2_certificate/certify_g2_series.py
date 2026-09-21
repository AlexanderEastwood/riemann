#!/usr/bin/env python3
"""Second certificate: analytic arch series and a rational full-space complement.

No numerical integration or Householder coordinates. Uses explicit geometric
tail bounds and rigorous Arb digamma/trigamma enclosures, then interval LDL/LU.
"""
import hashlib,json,time
from pathlib import Path
from flint import arb,acb,arb_mat,ctx
from certify_g2_finite import exact_decimal,eye,ldl_certificate

BASE=Path(__file__).resolve().parent
ctx.prec=768


def main():
    start=time.time(); L=2*arb(3).log(); pi=arb.pi(); nmax=64; K=128
    pdat=[(arb(m).log(),arb(p).log()/arb(m).sqrt()) for m,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]]
    bs=[]; ds=[]; entries=[]
    aK=2*K+arb(1)/2
    expK=arb(1)/arb(3)**(4*K+1)
    tailS=expK/(2*aK*(1-arb(1)/81))
    tailD=2*expK/(L*aK*aK*(1-arb(1)/81))
    for n in range(nmax+1):
        t=2*pi*n/L; z=acb(arb(1)/4,-t/2)
        ps=z.digamma(); trig=z.polygamma(1)
        s=arb(0) if n==0 else -ps.imag/2
        d=pi.log()-ps.real-trig.real/(2*L)
        for k in range(K):
            a=2*k+arb(1)/2; e=arb(1)/arb(3)**(4*k+1); den=a*a+t*t
            if n:s-=e*t/den
            d+=2/L*e*(a*a-t*t)/(den*den)
        if n:s+=arb(0,tailS.upper())
        d+=arb(0,tailD.upper())
        denom=L*L+16*pi*pi*n*n
        b=32*L*(L/4).sinh()**2*n/denom+(s+sum(((t*y).sin()*v for y,v in pdat),arb(0)))/pi
        pole=32*L*(L/4).sinh()**2*(L*L-16*pi*pi*n*n)/denom**2
        prime=2*sum(((t*y).cos()*(1-y/L)*v for y,v in pdat),arb(0))
        bs.append(b); ds.append(pole-prime-d)
        entries.append(dict(n=n,sine_integral=s.str(140),complete_arch_diagonal=d.str(140)))
    def entry(n,m):
        if n==m:return ds[abs(n)]
        bn=bs[abs(n)] if n>=0 else -bs[abs(n)]
        bm=bs[abs(m)] if m>=0 else -bs[abs(m)]
        return (bn-bm)/(n-m)
    W=arb_mat([[entry(n,m) for m in range(-64,65)] for n in range(-64,65)])
    path=BASE/'g2_finite_candidate.json'; source=json.loads(path.read_text())
    co=[exact_decimal(s) for s in source['positive_coefficients']]
    v=arb_mat([[co[abs(n)]] for n in range(-64,65)]); s=(v.transpose()*v)[0,0]
    alpha=(v.transpose()*W*v)[0,0]/s
    # Q_j=e_j-(v_j/v_k)e_k is an EXACT rational basis of v-perp.
    k=64; indices=[i for i in range(129) if i!=k]
    Q=arb_mat(129,128)
    for j,i in enumerate(indices):Q[i,j]=1; Q[k,j]=-v[i,0]/v[k,0]
    G=Q.transpose()*Q
    H=Q.transpose()*(W-alpha*eye(129))*Q
    b=Q.transpose()*W*v
    gamma=exact_decimal('1e-34')
    pivots=ldl_certificate(H-gamma*G,'rational full-space complement minus gamma Gram')
    z=H.solve(b,algorithm='lu')
    q=(z.transpose()*G*z)[0,0]/s; q=q.sqrt()
    energy=(b.transpose()*z)[0,0]/s; lower=alpha-energy
    print('Independent Schur values:',alpha.str(35),q.str(35),energy.str(35),lower.str(35),flush=True)
    assert q<exact_decimal('.000216')
    assert lower>exact_decimal('3.64e-38')
    assert alpha<exact_decimal('5.32e-38')
    # Entrywise independent overlap check with the quadrature/Householder run.
    reference=json.loads((BASE/'g2_finite_matrix_intervals.json').read_text())
    comparisons=0; root2=arb(2).sqrt()
    for n in range(65):
        for m in range(65):
            value=entry(0,0) if n==m==0 else root2*entry(n,m) if n==0 or m==0 else entry(n,m)+entry(n,-m)
            assert value.overlaps(arb(reference['even_matrix'][n][m]))
            comparisons+=1
    for n in range(1,65):
        for m in range(1,65):
            assert (entry(n,m)-entry(n,-m)).overlaps(arb(reference['odd_matrix'][n-1][m-1]))
            comparisons+=1
    result=dict(status='PASS: independent rigorous series/rational-complement certificate.',
        scope='Exact finite matrix, frozen rational candidate only; not true-PSWF or infinite-dimensional certification.',
        lambda_exact=3,N=64,dimension=129,precision_bits=ctx.prec,series_terms=K,
        candidate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        sine_integral_tail_bound=tailS.str(70),arch_diagonal_tail_bound=tailD.str(70),
        alpha=alpha.str(65),q=q.str(65),schur_energy=energy.str(65),ground_lower=lower.str(65),
        complement_gap_certified_lower='1e-34',strictly_positive_pivots=len(pivots),
        independent_matrix_entry_overlaps=comparisons,
        checks=dict(q_below_0_000216=True,ground_above_3_64e_minus38=True,alpha_below_5_32e_minus38=True),
        pivots=pivots,elapsed_seconds=round(time.time()-start,3))
    (BASE/'g2_finite_series_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    (BASE/'g2_finite_series_intervals.json').write_text(json.dumps(dict(
        status='Certified special-function series enclosures with explicit tail radii.',rows=entries),indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='pivots'},indent=2),flush=True)


if __name__=='__main__':main()
