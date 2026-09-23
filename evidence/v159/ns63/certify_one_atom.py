"""Certified finite changing-norm control; one atom, no RH conclusion."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path
from typing import Any

from flint import acb, arb, ctx


def inspect(order: int, cutoff: int) -> dict[str, Any]:
    zeta0 = arb(1)/2
    zeta0 = zeta0.zeta()
    norm_squared = arb(math.comb(2*order, order))
    pi = arb.pi()

    def integrand(t: acb, analytic: bool) -> acb:
        # The integrand is meromorphic; its poles return nonfinite balls.
        # No conjugation or nonanalytic absolute-value operation is used.
        s = acb(arb(1)/2)+acb(0, 1)*t
        return ((1-s.zeta()/zeta0)*(1-(1-s).zeta()/zeta0)
                /(pi*norm_squared*(s*(1-s))**(order+1)))

    tolerance = arb(2)**-120
    interior = acb.integral(integrand, 0, cutoff, abs_tol=tolerance,
                           rel_tol=tolerance, eval_limit=200000, depth_limit=40)
    assert interior.is_finite() and interior.imag.contains(0)
    a = arb(cutoff)
    tail = (2*a**(-2*order-1)/(2*order+1)
            +32*a**(-2*order+1)/(zeta0*zeta0*(2*order-1)))/(pi*norm_squared)
    relative_error = interior.real+arb(0, tail)
    absolute_error = relative_error*norm_squared
    d0 = (arb.const_euler()+pi/2+(8*pi).log())/2
    leading = d0*d0/(4*(2*order-1))
    assert relative_error > 0 and relative_error < 1
    return {'order': order, 'cutoff': cutoff,
            'relative_squared_error': relative_error.str(35),
            'absolute_squared_error': absolute_error.str(35),
            'target_norm_squared': str(math.comb(2*order, order)),
            'leading_relative_asymptotic': leading.str(35),
            'relative_tail_bound': tail.str(20),
            'relative_accuracy_bits': relative_error.rel_accuracy_bits(),
            'gates': {'finite_analytic_integral': True, 'imaginary_part_contains_zero': True,
                      'positive_error_below_target_norm': True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    started = time.monotonic()
    rows = []
    for order, cutoff in [(4, 32), (16, 8), (64, 4)]:
        row = inspect(order, cutoff)
        rows.append(row)
        print(order, row['relative_squared_error'], flush=True)
    result = {'classification': 'certified finite control, not RH evidence',
              'precision_bits': args.bits, 'one_atom_index': 1,
              'fixed_coefficient': '-1/zeta(1/2)', 'quadrature_tolerance_bits': 120,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'elapsed_seconds': time.monotonic()-started, 'rows': rows}
    args.output.write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
