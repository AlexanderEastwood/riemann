"""A complete local lower bound separating continuous and integer dilation spaces."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import arb, arb_mat, ctx


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    u = arb(3)/2
    ell = arb(2).log()
    logu = u.log()
    h = ell-logu
    gram = arb_mat([[1,-ell*ell/2],[-ell*ell/2,1-ell-ell*ell/2]])
    loads = arb_mat([[1/u-h*h/2],[(logu+2-ell*ell/2)/u+logu*(ell+1)/2-(ell*ell+2*ell+2)/2]])
    norm = 1/(u*u)-h*h/u+2/u-h*h/2-h-1
    assert gram.det() > 0 and norm > 0
    coefficients = gram.solve(loads,algorithm='precond')
    gap = norm-(loads.transpose()*coefficients)[0,0]
    assert gap > 0 and gap < norm
    values = {'dilation':u,'local_norm_squared':norm,'local_gram_determinant':gram.det(),
              'full_space_squared_distance_lower_bound':gap,
              'projection_coefficient_inverse_x':coefficients[0,0],
              'projection_coefficient_log_x':coefficients[1,0]}
    print(json.dumps({'classification':'certified local lower bound for the full distance of sigma_(3/2) to every integer dilation combination; not a target-tau bound',
                      'precision_bits':args.bits,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'values':{key:value.str(70) for key,value in values.items()},
                      'minimum_accuracy_bits':min(v.rel_accuracy_bits() for v in values.values()),
                      'gates':{'complete_local_integrals':True,'positive_local_gram':True,'positive_gap':True,
                               'global_bound_by_norm_restriction':True}},indent=2))


if __name__ == '__main__':
    main()
