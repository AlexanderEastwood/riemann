"""Certify one theta-product slice; this is not a sign test of xi'/xi."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from flint import acb, arb, ctx


def theta_prefix(t: acb, count: int) -> acb:
    pi = acb.pi()
    v = (2*t).exp()
    return sum(((2*pi*pi*n**4*(arb(9)*t/2).exp()
                 -3*pi*n*n*(arb(5)*t/2).exp())*(-pi*n*n*v).exp()
                for n in range(1, count+1)), acb(0))


def certify(bits: int, count: int, cutoff: int) -> dict[str, object]:
    ctx.prec = bits
    pi = arb.pi()
    # For n>=count+1, n^4 exp(-pi*n^2) has decreasing successive ratios.
    ratio = arb(count+2)**4/arb(count+1)**4*(-pi*(2*count+3)).exp()
    prefix_tail = 2*pi*pi*(count+1)**4*(-pi*(count+1)**2).exp()/(1-ratio)
    geometric = 16*(-3*pi).exp()
    full_bound = 2*pi*pi*(-pi).exp()/(1-geometric)
    assert geometric < 1 and ratio < 1 and full_bound < 1
    finite_error = 2*cutoff*full_bound*prefix_tail
    tail_prefactor = 2*pi*pi/(1-geometric)
    exponent = (2*arb(cutoff)).exp()
    physical_tail = tail_prefactor**2*(9*arb(cutoff)-2*pi*exponent).exp()/(4*pi*exponent-9)
    def integrand(t: acb, analytic: bool) -> acb:
        # Every constituent is entire, so the analytic flag needs no restriction.
        return theta_prefix(t, count)**2*(40*t).cos()
    value = acb(0)
    for k in range(4*cutoff):
        value += acb.integral(integrand, arb(k)/4, arb(k+1)/4,
                              abs_tol=arb(2)**(-bits+20), rel_tol=arb(2)**(-bits+20))
    assert value.imag.contains(0)
    error = finite_error+physical_tail
    complete = value.real + arb(0, error.upper())
    assert complete < arb('-5.4319e-10')
    assert complete > arb('-5.4320e-10')
    return {'precision_bits':bits, 'theta_terms':count, 'cutoff':cutoff,
            'cosine_frequency':40, 'prefix_integral':str(value.real),
            'theta_series_error_bound':str(finite_error),
            'physical_tail_bound':str(physical_tail),
            'complete_half_line_integral':str(complete),
            'conclusion':'strictly negative; slice positivity fails, not the weighted full kernel',
            'scope':'one complete theta-product slice, not an RH counterexample'}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--terms',type=int,default=4)
    parser.add_argument('--cutoff',type=int,default=2)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = certify(args.bits,args.terms,args.cutoff)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
