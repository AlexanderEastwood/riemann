"""Independent positive-cell q=2 integral checks, including the whole tail."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

from certify_smoothed import Kernel


def primitive(t: arb, first: tuple[arb, arb, arb], second: tuple[arb, arb, arb]) -> arb:
    a, b, c = first
    d, e, f = second
    logt = t.log()
    return (a*d*t+(a*e+b*d)*logt*logt/2+(a*f+c*d)*logt
            -b*e*(logt*logt+2*logt+2)/t
            -(b*f+c*e)*(logt+1)/t-c*f/t)


def check_pair(kernel: Kernel, m: int, n: int, cutoff: int) -> dict[str, Any]:
    assert cutoff >= max(m, n)
    points = sorted(set(range(m, cutoff+1, m)) | set(range(n, cutoff+1, n)) | {cutoff})
    integral = arb(min(m, n))/(m*n)
    logs = [arb(0)]+[arb(k).log() for k in range(1, cutoff+1)]
    factorial_logs = [arb(0)]
    for k in range(1, cutoff+1):
        factorial_logs.append(factorial_logs[-1]+logs[k])
    for left, right in zip(points, points[1:]):
        km, kn = left//m, left//n
        first = (arb(1)/m, arb(-km), km*logs[m]+factorial_logs[km])
        second = (arb(1)/n, arb(-kn), kn*logs[n]+factorial_logs[kn])
        cell = primitive(arb(right), first, second)-primitive(arb(left), first, second)
        assert cell > 0, (m, n, left, right)
        integral += cell
    t = arb(cutoff)
    lm, ln = (2*arb.pi()*t/m).log()/2, (2*arb.pi()*t/n).log()/2
    tail_main = (lm*ln+(lm+ln)/2+arb(1)/2)/t
    tail_error = 3*(m*(ln/2+arb(1)/8)+n*(lm/2+arb(1)/8))/t**2+3*m*n/t**3
    enclosure = integral+tail_main+arb(0, tail_error)
    exact_gram = kernel.gram(m, n)
    # Stronger than overlap: the entire Gram ball is strictly inside the
    # independent interval centered at the positive-cell integral plus tail.
    discrepancy = exact_gram-integral-tail_main
    assert abs(discrepancy) < tail_error
    return {'m': m, 'n': n, 'cells': len(points)-1, 'cutoff': cutoff,
            'physical_enclosure': enclosure.str(20), 'gram_formula': exact_gram.str(30),
            'tail_error_bound': tail_error.str(15), 'strict_tail_gate': True,
            'all_finite_cell_integrals_positive': True}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, required=True)
    parser.add_argument('--cutoff', type=int, default=16384)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    kernel = Kernel(16, 128, 24)
    pairs = [(1, 1), (1, 2), (2, 3), (3, 8), (7, 8), (5, 11), (8, 16)]
    rows = [check_pair(kernel, m, n, args.cutoff) for m, n in pairs]
    result = {'classification': 'certified finite convention checks, not an asymptotic result',
              'precision_bits': args.bits, 'tail_lemma': 'gram-tail-proof.tex, physical check paragraph',
              'rows': rows}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'positive_cell_checks': len(rows), 'precision_bits': args.bits}))


if __name__ == '__main__':
    main()
