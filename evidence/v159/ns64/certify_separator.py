"""Complete finite local separator for the nonnegative smoothed NB cone."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

from flint import arb, arb_mat, ctx


def primitive(t: arb, first: tuple[arb, arb, arb], second: tuple[arb, arb, arb]) -> arb:
    a, b, c = first
    d, e, f = second
    logt = t.log()
    return (a*d*t+(a*e+b*d)*logt*logt/2+(a*f+c*d)*logt
            -b*e*(logt*logt+2*logt+2)/t
            -(b*f+c*e)*(logt+1)/t-c*f/t)


def polynomial(n: int, left: int) -> tuple[arb, arb, arb]:
    k = left//n
    return arb(1)/n, arb(-k), k*arb(n).log()+arb(k+1).lgamma()


def scalar(matrix: arb_mat) -> arb:
    return matrix[0, 0]


def calculate() -> dict[str, Any]:
    # t=1/x sends x>1/6 to 0<t<6; every breakpoint is an integer.
    original = arb_mat(6, 6)
    for m in range(1, 7):
        for n in range(1, 7):
            value = arb(1)/(m*n)
            for left in range(1, 6):
                first, second = polynomial(m, left), polynomial(n, left)
                value += primitive(arb(left+1), first, second)-primitive(arb(left), first, second)
            original[m-1, n-1] = value
    transform = arb_mat(6, 6)
    for n in range(1, 7):
        transform[n-1, n-1] = 1
        if n > 1:
            transform[n-2, n-1] = -arb(n-1)/n
    gram = transform.transpose()*original*transform
    beta = arb_mat([[0], [2], [arb(3)/2], [arb(2)/3], [arb(5)/6], [-arb(1)/5]])
    loads = gram*beta
    found: tuple[list[int], arb_mat, arb_mat, arb] | None = None
    for length in range(1, 7):
        for support in itertools.combinations(range(6), length):
            block = arb_mat([[gram[i, j] for j in support] for i in support])
            rhs = arb_mat([[loads[i, 0]] for i in support])
            solution = block.solve(rhs, algorithm='precond')
            if not all(solution[k, 0] > 0 for k in range(length)):
                continue
            coefficient = arb_mat(6, 1)
            for k, i in enumerate(support):
                coefficient[i, 0] = solution[k, 0]
            discrepancy = coefficient-beta
            dual = gram*discrepancy
            if not all(dual[i, 0] > 0 for i in range(6) if i not in support):
                continue
            assert all(dual[i, 0].contains(0) for i in support)
            distance2 = scalar(discrepancy.transpose()*gram*discrepancy)
            assert distance2 > 0
            assert (scalar(discrepancy.transpose()*loads)+distance2).contains(0)
            found = list(support), coefficient, dual, distance2
            break
        if found is not None:
            break
    assert found is not None
    support, coefficient, dual, distance2 = found
    e6 = arb_mat([[0], [0], [0], [0], [0], [1]])
    coordinate_dual = gram.solve(e6, algorithm='precond')
    coordinate_projection = beta+coordinate_dual/(5*coordinate_dual[5, 0])
    assert (coordinate_projection-coefficient).contains(arb_mat(6, 1))
    coordinate_distance2 = 1/(25*coordinate_dual[5, 0])
    assert coordinate_distance2 > 0
    assert (gram*coordinate_dual-e6).contains(arb_mat(6, 1))
    return {
        'classification': 'certified local nonnegative-cone distance; no signed NB or RH claim',
        'restricted_domain': 'x>1/6', 'basis': ['sigma_1']+[f'epsilon_{n}' for n in range(2, 7)],
        'gram': [[gram[i, j].str(40) for j in range(6)] for i in range(6)],
        'target_coefficients': ['0', '2', '3/2', '2/3', '5/6', '-1/5'],
        'positive_projection_support': [i+1 for i in support],
        'projection_coefficients': [coefficient[i, 0].str(40) for i in range(6)],
        'separator_coefficients': [(coefficient[i, 0]-beta[i, 0]).str(40) for i in range(6)],
        'separator_pairings': [dual[i, 0].str(40) for i in range(6)],
        'local_cone_distance_squared': distance2.str(40),
        'full_cone_distance_lower_bound': distance2.sqrt().str(40),
        'single_coordinate_distance_squared_bound': coordinate_distance2.str(40),
        'minimum_accuracy_bits': min(distance2.rel_accuracy_bits(),
            *(coefficient[i, 0].rel_accuracy_bits() for i in support),
            *(dual[i, 0].rel_accuracy_bits() for i in range(6) if i not in support)),
        'gates': {'positive_active_coefficients': True, 'strict_positive_inactive_pairings': True,
                  'active_pairings_contain_zero': True, 'separator_target_pairing_identity': True,
                  'positive_distance': True, 'coordinate_dual_identity': True,
                  'coordinate_projection_identity': True},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    result = calculate()
    result['precision_bits'] = args.bits
    result['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'precision_bits': args.bits,
                      'support': result['positive_projection_support'],
                      'distance_lower_bound': result['full_cone_distance_lower_bound'],
                      'accuracy_bits': result['minimum_accuracy_bits']}))


if __name__ == '__main__':
    main()
