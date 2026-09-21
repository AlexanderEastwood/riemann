#!/usr/bin/env python3
"""Exact rational checks of abstract obstructions; no arithmetic-window test."""
from fractions import Fraction as F
import json
from pathlib import Path


def multiply(A, B):
    return [[sum((x*y for x,y in zip(row,col)),F(0))
             for col in zip(*B)] for row in A]


def transpose(A):
    return [list(c) for c in zip(*A)]


def main():
    I = [[F(i==j) for j in range(4)] for i in range(4)]
    U = [I[0],I[2],I[1],I[3]]
    assert multiply(transpose(U),U) == I
    cases=[]
    for R in (2,17,1000):
        for epsilon in (F(0),F(1,16)):
            M=[[F(0),F(0),F(0),epsilon],
               [F(0),F(1),F(0),F(0)],
               [F(0),F(0),-F(R),F(0)],
               [epsilon,F(0),F(0),F(2)]]
            N=multiply(multiply(transpose(U),M),U)
            # Physical space is span(e0,e1,e3); source is e0.
            # Both the source and its complete action epsilon*e3 are fixed.
            assert [r[0] for r in N] == [r[0] for r in M]
            assert N[1][1] == -R and M[1][1] == 1
            assert multiply(multiply(U,N),transpose(U)) == M
            cases.append({'negative_depth':R,'source_residual':str(epsilon),
                          'unrotated_test_energy':'1',
                          'rotated_test_energy':str(N[1][1]),
                          'complete_source_column_preserved':True,
                          'exact_unitary_equivalence':True})
    # Dimensionless area a|E|/pi = 1/[2(D+1)].
    positive=[]
    for D in (F(1),F(100),F(10**12)):
        area=1/(2*(D+1))
        floor=1-(D+1)*area
        assert floor == F(1,2)
        positive.append({'negative_depth':str(D),'a_times_area_over_pi':str(area),
                         'location_independent_floor':str(floor)})
    # Analytic probe proof uses only this exact rational enclosure for pi.
    assert 6*F(22,7)**2 < 100
    report={'scope':'Exact abstract finite-dimensional and mass-cap checks; not a Weil computation',
            'arithmetic':'fractions.Fraction (exact; no precision replay needed)',
            'protected_head_models':cases,'location_blind_positive_models':positive,
            'probe_rational_gate':'6*(22/7)^2 < 100',
            'all_exact_checks_passed':True}
    out=Path(__file__).with_name('exact_model_results.json')
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('6 protected-source models, 3 location-blind positive models, rational probe gate: all exact checks passed')


if __name__ == '__main__':
    main()
