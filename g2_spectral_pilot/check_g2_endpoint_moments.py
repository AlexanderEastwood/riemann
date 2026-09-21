#!/usr/bin/env python3
"""Independent exact polynomial Mellin integration of the Galerkin source.

The moment formula is exact for the finite Legendre polynomial. Its evaluation
and comparison to the genuine PSWF remain non-certified numerical calculations.
The omitted smooth repair has an explicit reported endpoint-error upper formula.
"""
import json
from pathlib import Path
import mpmath as mp
from check_g2_spectral import repaired_source


def main():
    _,_,meta,hc=repaired_source('3',70,140,return_coefficients=True)
    lam=mp.mpf(3); length=2*mp.log(lam); size=len(hc)
    d=[]
    for r in range(size):
        d.append(mp.fsum(hc[k]*(-1)**(k-r)*mp.factorial(2*k+2*r)
            /(2**(2*k)*mp.factorial(k-r)*mp.factorial(k+r)*mp.factorial(2*r))
            for k in range(r,size)))
    mmax=int(mp.floor(lam**2))
    b=[mp.fsum(mp.mpf(m)**(2*r) for m in range(1,mmax+1))/lam**(4*r+mp.mpf('.5'))
       for r in range(size)]
    def coeff(n):
        t=2*mp.pi*n/length
        aa=mp.sqrt(lam)*mp.fsum(mp.exp((-mp.mpf('.5')-1j*t)*mp.log(m))
                               for m in range(1,mmax+1))
        return mp.re(mp.fsum(d[r]*(aa-b[r])/(2*r+mp.mpf('.5')+1j*t)
                            for r in range(size)))/mp.sqrt(length)
    endpoint=mp.mpf(meta['B_physical']); hzero=mp.mpf(meta['h_at_zero_before_repair'])
    radius=mp.mpf('.75'); C=mp.mpf(meta['bump_moment_ratio'])
    # |psi|<=1+C radius^2; at most floor(radius*lambda) nonzero summands;
    # integral_{1/lambda}^radius sqrt(u) du/u <=2 sqrt(radius).
    l1=2*mp.sqrt(radius)*int(mp.floor(radius*lam))*(1+C*radius**2)
    sample_ns={8,16,32,64,128,256,512,1024,2048,4096}
    samples=[]; low=[]; total=mp.mpf(0)
    for n in range(4097):
        c=coeff(n)
        if n<=32: low.append(mp.nstr(c,70))
        total += c if n==0 else 2*c
        if n in sample_ns:
            value=total/mp.sqrt(length)
            row=dict(N=n,polynomial_endpoint=mp.nstr(value,35),
                relative_error_against_repaired_physical_endpoint=mp.nstr(abs(value-endpoint)/abs(endpoint),25),
                omitted_repair_endpoint_bound_formula_value=mp.nstr(abs(hzero)*(2*n+1)*l1/length,25),
                omitted_repair_relative_bound_formula_value=mp.nstr(abs(hzero)*(2*n+1)*l1/(length*abs(endpoint)),25))
            samples.append(row); print(json.dumps(row),flush=True)
    inp=json.loads(Path(__file__).with_name('g2_spectral_mp_checks.json').read_text())
    ref=inp['rows'][-1]['coefficient_vector_N32']
    diff=max(abs(mp.mpf(low[n])-mp.mpf(ref[32+n])) for n in range(33))
    # Bound the smooth repair's coefficient by |hzero|*||E psi||_1/sqrt(L).
    cbound=abs(hzero)*l1/mp.sqrt(length)
    out=dict(status='Non-certified finite-Galerkin evaluation. No N=4096 Weil matrix assembled.',
        source=meta,
        identity='c_n=L^(-1/2) Re sum_r d_r [sqrt(lambda) sum_(m<=lambda²) m^(-1/2-it_n) - lambda^(-4r-1/2) sum_(m<=lambda²) m^(2r)]/(2r+1/2+it_n)',
        source_polynomial='h_circle(v)=sum_r d_r (v/lambda)^(2r)',
        explicit_L1_bound_for_Epsi=mp.nstr(l1,25),
        low_coefficient_max_difference_from_repaired_quadrature=mp.nstr(diff,30),
        omitted_repair_coefficient_bound_formula_value=mp.nstr(cbound,30),
        positive_coefficients_N32=low,endpoint_rows=samples)
    Path(__file__).with_name('g2_endpoint_moment_checks.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':
    main()
