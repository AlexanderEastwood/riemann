"""Scalar replay of the complete analytic tail bound; external height is an input."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import arb, ctx


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    height = arb(3000000000000)
    logh = height.log()
    s2 = 2*(logh+1)/height
    s4 = 4*(logh/3+arb(1)/9)/(height**3)
    bound = arb(8)/3*s2**3+5*s4
    assert 0 < bound < arb('2.08e-32')
    assert arb(100).log() > 4 and 2*arb.pi() > 6
    values = {'external_verified_height_used':height,'counting_constant_A':arb(1),
              'S2_upper_bound':s2,'S4_upper_bound':s4,
              'continuous_squared_distance_upper_bound':bound}
    controls: list[dict[str, str]] = []
    for gamma in [1,10,100,1000000,3000000000000]:
        a = arb(3)/4
        c = 1-a
        g = arb(gamma)
        numerator = g*g+c*c
        denominator = g*g+a*a
        b = numerator/denominator
        d = 2*c/denominator-2*a*numerator/denominator**2
        e = 2/denominator-8*a*c/denominator**2-2*numerator/denominator**2+8*a*a*numerator/denominator**3
        distance = 2-2*b*b+2*b*d-d*d-e*e/4
        delta = 2*a-1
        budget = arb(8)/3*(delta/(g*g))**3+5*delta/g**4
        assert 0 < distance < budget
        controls.append({'hypothetical_beta':a.str(65),'hypothetical_height':g.str(65),
                         'exact_pair_squared_distance':distance.str(65),
                         'pair_budget':budget.str(65)})
    print(json.dumps({'classification':'certified scalar consequence of complete analytic zero-tail bound with external published finite-height input; not an integer error bound or new zero verification',
                      'precision_bits':args.bits,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'external_inputs':{'height':'Platt–Trudgian, Theorem 1, https://arxiv.org/pdf/2004.09765',
                                         'counting':'Hasanalizade–Shen–Wong, Corollary 1.2, https://arxiv.org/pdf/2107.06506'},
                      'values':{key:value.str(65) for key,value in values.items()},
                      'hypothetical_pair_controls':controls,
                      'gates':{'full_analytic_zero_tails':True,'positive_calibration_below_2_08e_32':True,
                               'zero_verification_is_external_input':True,'no_integer_upper_bound_claimed':True}},indent=2))


if __name__ == '__main__':
    main()
