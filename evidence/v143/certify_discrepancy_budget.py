#!/usr/bin/env python3
"""Complete lambda=4 evaluator budget; requested sign/factor-ten gate is unresolved.

Uses the archived complete Schur comparison and tail floor without a new
metric. New acceptance gates use Arb at 1024/1280 bits. A symmetric complete
root enclosure is not a signed discrepancy certificate.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
from flint import acb, arb, arb_mat, ctx
from archive import COARSE_PATH, coarse


def truncated_transform(t: arb, coefficients: list[arb], length: arb) -> arb:
    """Direct centered cosine integrals, valid also at removable poles and zero."""
    a = length/2
    value = length.sqrt()*coefficients[0]*(a*t).sinc()
    for n, coefficient in enumerate(coefficients[1:], 1):
        omega = 2*arb.pi()*n/length
        value += (length/2).sqrt()*((-1)**n)*coefficient*(
            (a*(t-omega)).sinc()+(a*(t+omega)).sinc())
    return value


def exclude_earlier(coefficients: list[arb], length: arb, gamma: arb,
                    projection_error: arb) -> dict[str, Any]:
    cut = 64
    omitted_norm = sum((x*x for x in coefficients[cut+1:]), arb(0)).sqrt()
    error = length.sqrt()*(projection_error+omitted_norm)
    stack = [(arb(0), gamma-arb(1)/10, 0)]
    accepted: list[dict[str, Any]] = []
    while stack:
        left, right, depth = stack.pop()
        upper = truncated_transform(left.union(right), coefficients[:cut+1], length)+error
        if upper < 0:
            accepted.append({'left':left.str(90),'right':right.str(90),
                             'projected_ground_transform_upper':upper.upper().str(90),
                             'depth':depth})
        else:
            assert depth < 20, 'Earlier-zero exclusion inconclusive at maximum depth.'
            middle = (left+right)/2
            stack.extend([(left,middle,depth+1),(middle,right,depth+1)])
    return {'status':'PASS_NO_NONNEGATIVE_VALUE_BEFORE_LOCAL_INTERVAL',
            'covered_interval':'[0,gamma_1-1/10]', 'finite_evaluation_cut':cut,
            'omitted_finite_trial_norm':omitted_norm.str(100),
            'combined_projection_and_finite_omission_error':error.str(100),
            'accepted_subintervals':accepted}


def run(bits: int) -> dict[str, Any]:
    ctx.prec = bits
    old = coarse.run(bits)
    prior = coarse.load_prior()
    data, matrices, trial, _, _, provenance = prior.load_trial('even',bits)
    prior.replay_prior_gates('even',data,matrices,bits)
    energy = prior.sym(matrices['K'])
    assert prior.inertia(energy)['negative'] == 0
    length, gamma = 2*arb(4).log(), acb.zeta_zero(1).imag
    row = arb_mat([[coarse.transform_and_derivative(
        gamma,[trial[i,j] for i in range(trial.nrows())],length)[0]
        for j in range(17)]])
    # Certified solve, not a midpoint inverse or midpoint acceptance gate.
    head_dual_squared = (row*energy.solve(row.transpose()))[0,0]
    factor = 2*(gamma*length/2).sin()/length.sqrt()
    head_evaluator = [factor/gamma]+[
        arb(2).sqrt()*factor*gamma/(gamma*gamma-(2*arb.pi()*n/length)**2)
        for n in range(1,17)]
    # Parseval for the complete cosine evaluator, not a finite tail sum.
    full_evaluator_squared = length/2+(gamma*length).sin()/(2*gamma)
    tail_evaluator_squared = full_evaluator_squared-sum((x*x for x in head_evaluator),arb(0))
    delta, kappa = arb('1.7940e-8'),arb(62629)/100000
    tail_dual_squared = tail_evaluator_squared/delta
    assert head_dual_squared > 0 and tail_dual_squared > 0
    dual_squared = (head_dual_squared+tail_dual_squared+
                    2*((1-kappa)*head_dual_squared*tail_dual_squared).sqrt())/kappa
    norm_squared = sum((trial[i,16]*trial[i,16] for i in range(trial.nrows())),arb(0))
    rayleigh = energy[16,16]/norm_squared
    value_budget = (rayleigh*dual_squared).sqrt()
    slope_floor = arb('0.0016')
    root_budget = value_budget/slope_floor
    assert root_budget < arb('9e-33')
    # Even dropping the nonnegative tail term does not rescue THIS energy budget.
    head_only_budget = (rayleigh*head_dual_squared/kappa).sqrt()/slope_floor
    target_scale = arb('3e-71')  # diagnostic planning scale, never a complete-root bound
    assert root_budget > arb('1e38')*target_scale
    assert head_only_budget > arb('1e35')*target_scale
    coefficients = [trial[i,16]/norm_squared.sqrt() for i in range(trial.nrows())]
    earlier = exclude_earlier(coefficients,length,gamma,arb(old['projection_error_upper']))
    assert all(arb(item['projected_ground_transform_upper'])<0
               for item in earlier['accepted_subintervals'])
    return {
        'status':'PASS_COMPLETE_ABSOLUTE_BOUND; REQUESTED_SIGN_AND_FACTOR_TEN_UNRESOLVED',
        'bits':bits,'lambda':4,'root_name':'z_1(4): first positive complete-ground transform zero',
        'signed_discrepancy_interval_exact':['-9e-33','9e-33'],
        'fixes_sign':False,'fixes_magnitude_within_factor_10':False,
        'gamma_1':gamma.str(110),
        'head_evaluator_dual_squared':head_dual_squared.str(100),
        'complete_tail_evaluator_norm_squared':tail_evaluator_squared.str(100),
        'tail_evaluator_dual_squared_upper':tail_dual_squared.str(100),
        'complete_evaluator_dual_squared_upper':dual_squared.str(100),
        'rayleigh_upper_enclosure':rayleigh.str(100),
        'projected_ground_value_budget':value_budget.str(100),
        'coarse_local_derivative_lower_exact':'0.0016',
        'zero_displacement_budget':root_budget.str(100),
        'head_only_zero_budget_in_same_comparison':head_only_budget.str(100),
        'diagnostic_target_scale_only':'3e-71',
        'budget_over_diagnostic_scale':(root_budget/target_scale).str(60),
        'head_only_budget_over_diagnostic_scale':(head_only_budget/target_scale).str(60),
        'first_positive_zero_exclusion':earlier,
        'scope':'Full tail covered by inherited Schur/residual inequalities and Parseval. '
                'This is a new absolute complete-ground bound, not the requested signed magnitude certificate. '
                'The symmetric uncertainty cannot be treated as a nonzero lower discrepancy bound. '
                'No new tail metric, new window, G2 or RH claim.',
        'provenance':provenance,'inherited_dependencies':old['dependencies'],
        'coarse_verifier_sha256':coarse.sha256(COARSE_PATH),
        'verifier_sha256':coarse.sha256(Path(__file__)),
    }


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits',type=int,choices=(1024,1280),required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    assert not args.output.exists(), 'Use a fresh output path.'
    result=run(args.bits)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],args.bits,flush=True)
    print('root budget',result['zero_displacement_budget'],flush=True)
    print('earlier-zero intervals',len(result['first_positive_zero_exclusion']['accepted_subintervals']),flush=True)


if __name__=='__main__':
    main()
