#!/usr/bin/env python3
"""Second scalar-duality and saved dyadic-coverage check; no external audit."""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any
from flint import arb, arb_mat, ctx
from archive import coarse
import certify_discrepancy_budget as budget


def check(bits: int) -> dict[str, Any]:
    ctx.prec=bits
    base=Path(__file__).parent
    report=json.loads((base/f'discrepancy_budget_b{bits}.json').read_text())
    assert report['verifier_sha256']==coarse.sha256(Path(budget.__file__))
    kappa=arb(62629)/100000
    theta=(1-kappa).sqrt()
    matrix=arb_mat([[1,-theta],[-theta,1]])
    assert matrix.det()>0 and matrix.det().overlaps(kappa)
    vector=arb_mat([[arb(report['head_evaluator_dual_squared']).sqrt()],
                    [arb(report['tail_evaluator_dual_squared_upper']).sqrt()]])
    dual=(vector.transpose()*matrix.solve(vector))[0,0]
    assert dual.overlaps(arb(report['complete_evaluator_dual_squared_upper']))
    radius=(arb(report['rayleigh_upper_enclosure'])*dual).sqrt()/arb('0.0016')
    assert radius<arb('9e-33')
    prior=coarse.load_prior()
    _,_,trial,_,_,_=prior.load_trial('even',bits)
    norm=sum((trial[i,16]*trial[i,16] for i in range(trial.nrows())),arb(0)).sqrt()
    coefficients=[trial[i,16]/norm for i in range(trial.nrows())]
    length=2*arb(4).log()
    gamma=arb(report['gamma_1'])
    top=gamma-arb(1)/10
    exclusion=report['first_positive_zero_exclusion']
    error=arb(exclusion['combined_projection_and_finite_omission_error'])
    segments: list[tuple[Fraction,Fraction]]=[]
    for item in exclusion['accepted_subintervals']:
        depth=item['depth']
        denominator=2**depth
        # Floating value only proposes the integer grid address; interval
        # comparisons below validate it, and Fraction proves exact coverage.
        numerator=round(float((arb(item['left'])/top).mid())*denominator)
        left,right=top*numerator/denominator,top*(numerator+1)/denominator
        assert arb(item['left']).overlaps(left) and arb(item['right']).overlaps(right)
        assert arb(item['projected_ground_transform_upper'])<0
        value=budget.truncated_transform(left.union(right),coefficients[:65],length)+error
        assert value<0
        segments.append((Fraction(numerator,denominator),Fraction(numerator+1,denominator)))
    segments.sort()
    assert segments[0][0]==0 and segments[-1][1]==1
    assert all(a[1]==b[0] for a,b in zip(segments,segments[1:]))
    for dependency in report['inherited_dependencies']:
        assert coarse.sha256(coarse.ROOT/dependency['path'])==dependency['sha256']
    finite=json.loads((base/f'finite_lambda4_N120_b{bits}.json').read_text())
    finite_discrepancy=arb(finite['signed_finite_discrepancy'])
    assert arb('2.9250e-71')<finite_discrepancy<arb('2.9251e-71')
    assert finite['verifier_sha256']==coarse.sha256(base/'certify_finite_lambda4.py')
    assert report['fixes_sign'] is False and report['fixes_magnitude_within_factor_10'] is False
    resolution_path=base/f'resolution_b{bits}.json'
    resolution=json.loads(resolution_path.read_text())
    assert resolution['verifier_sha256']==coarse.sha256(base/'certify_resolution.py')
    assert resolution['inputs'][0]['sha256']==coarse.sha256(base/f'discrepancy_budget_b{bits}.json')
    rho=arb(report['rayleigh_upper_enclosure'])
    b,d,epsilon=arb('1e-67'),arb('0.0016'),arb('1e-71')
    # Independent rearrangement: s(b-rho)/(Cb-s), rather than the
    # energy-target substitution used by certify_resolution.py.
    square=(d*epsilon)**2
    threshold=square*(b-rho)/(dual*b-square)
    assert threshold.overlaps(arb(resolution['rayleigh_minus_lower_bound_threshold']))
    gap=arb(resolution['safe_sufficient_gap_exact'])
    lower=rho-gap
    error_energy=(rho-lower)/(1-lower/b)
    assert (dual*error_energy).sqrt()/d<epsilon
    assert arb(resolution['radius'])<arb('8.752082e-33')
    assert arb('1.0641e-40')<arb(resolution['trial_transform_at_gamma'])<arb('1.0642e-40')
    return {'bits':bits,'dual_comparison_matrix_positive':True,
            'dual_solve_agrees':True,'complete_root_radius_below_9e_33':True,
            'dyadic_coverage_exact':True,'negative_subintervals_recomputed':len(segments),
            'finite_only_discrepancy_positive':True,'resolution_threshold_algebra_checked':True,'complete_discrepancy_sign_unresolved':True}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    assert not args.output.exists()
    checks=[check(bits) for bits in (1024,1280)]
    base=Path(__file__).parent
    reports=[json.loads((base/f'discrepancy_budget_b{bits}.json').read_text()) for bits in (1024,1280)]
    keys=['head_evaluator_dual_squared','complete_tail_evaluator_norm_squared',
          'tail_evaluator_dual_squared_upper','complete_evaluator_dual_squared_upper',
          'rayleigh_upper_enclosure','projected_ground_value_budget','zero_displacement_budget']
    assert all(arb(reports[0][key]).overlaps(arb(reports[1][key])) for key in keys)
    finite=[json.loads((base/f'finite_lambda4_N120_b{bits}.json').read_text()) for bits in (1024,1280)]
    assert arb(finite[0]['signed_finite_discrepancy']).overlaps(arb(finite[1]['signed_finite_discrepancy']))
    resolution_reports=[json.loads((base/f'resolution_b{bits}.json').read_text()) for bits in (1024,1280)]
    resolution_keys=['radius','target_error_energy','rayleigh_minus_lower_bound_threshold',
                     'relative_gap_threshold','ordinary_norm_transfer_gap_threshold','trial_transform_at_gamma']
    assert all(arb(resolution_reports[0][key]).overlaps(arb(resolution_reports[1][key])) for key in resolution_keys)
    result={'status':'PASS_SECOND_IMPLEMENTATION_NS19; NO_COMPLETE_SIGN_CLAIM',
            'checks':checks,'cross_precision_overlap_keys':keys,'resolution_overlap_keys':resolution_keys,
            'checker_sha256':coarse.sha256(Path(__file__)),
            'scope':'Same-agent implementation check of the absolute complete bound and finite benchmark. '
                    'No claim that the finite discrepancy transfers to the complete ground.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__':
    main()
