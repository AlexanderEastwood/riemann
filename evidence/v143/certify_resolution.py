#!/usr/bin/env python3
"""NS-19: replay the archived resolution budget and conditional lower-energy target.

All numerical assertions use Arb. The threshold is a conditional budget
requirement, not a claimed lower bound on the complete ground energy.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
from flint import acb, arb, ctx
from archive import COARSE_PATH, coarse


def run(bits: int) -> dict[str, Any]:
    ctx.prec = bits
    base = Path(__file__).resolve().parent
    path = base / f'discrepancy_budget_b{bits}.json'
    report = json.loads(path.read_text())
    assert report['verifier_sha256'] == coarse.sha256(base / 'certify_discrepancy_budget.py')
    rho = arb(report['rayleigh_upper_enclosure'])
    c = arb(report['complete_evaluator_dual_squared_upper'])
    d, b, epsilon = arb('0.0016'), arb('1e-67'), arb('1e-71')
    length = 2*arb(4).log()
    radius = (c*rho).sqrt()/d
    assert arb('8.75208157392882e-33') < radius < arb('8.752082e-33')
    # For l <= mu0, Delta=rho-l: q[f-Pf] <= b*Delta/(b-rho+Delta).
    # Solving C*q[f-Pf]/d^2 <= epsilon^2 gives this exact scalar threshold.
    energy_target = (d*epsilon)**2/c
    gap_threshold = energy_target*(b-rho)/(b-energy_target)
    assert arb('3.20320065e-153') < gap_threshold < arb('3.20320066e-153')
    assert arb('1.3055e-78') < gap_threshold/rho < arb('1.3056e-78')
    safe_gap = arb('3.2031e-153')
    # Rounded outward sufficient requirement using C<79921.
    safe_budget = (arb(79921)*b*safe_gap/(b-rho+safe_gap)).sqrt()/d
    assert safe_budget < epsilon
    assert (b*gap_threshold/(b-rho+gap_threshold)).overlaps(energy_target)
    ordinary_gap = (d*epsilon)**2*(b-rho)/(length-(d*epsilon)**2)
    assert arb('9.2332e-216') < ordinary_gap < arb('9.2333e-216')
    prior = coarse.load_prior()
    _, _, trial, _, _, _ = prior.load_trial('even', bits)
    norm = sum((trial[i,16]**2 for i in range(trial.nrows())), arb(0)).sqrt()
    coefficients = [trial[i,16]/norm for i in range(trial.nrows())]
    gamma = acb.zeta_zero(1).imag
    value, derivative = coarse.transform_and_derivative(gamma, coefficients, length)
    assert arb('1.0641e-40') < value < arb('1.0642e-40')
    assert arb('0.0031086') < derivative < arb('0.0031088')
    # If an energy-gap transfer ever attained the requested resolution, its
    # value error would be d*epsilon. This frozen trial is not centered to that scale.
    assert value > arb('1e33')*(d*epsilon)
    endpoint_radius = arb('8.752082e-33')
    return {
        'status':'PASS_NS19_ENCLOSURE_AND_CONDITIONAL_RESOLUTION_REQUIREMENT',
        'bits':bits, 'lambda':4,
        'radius_formula':'sqrt(C_ell*rho)/d',
        'radius':radius.str(100),
        'outward_radius_exact':'8.752082e-33',
        'left_endpoint':(gamma-endpoint_radius).lower().str(100),
        'right_endpoint':(gamma+endpoint_radius).upper().str(100),
        'symmetric_discrepancy_interval_exact':['-8.752082e-33','8.752082e-33'],
        'coarse_projection_error':(rho/b).sqrt().str(100),
        'rayleigh':rho.str(100), 'evaluator_dual_constant':c.str(100),
        'target_root_transfer_radius_exact':'1e-71',
        'target_transform_error_exact':'1.6e-74',
        'target_error_energy':energy_target.str(100),
        'rayleigh_minus_lower_bound_threshold':gap_threshold.str(100),
        'relative_gap_threshold':(gap_threshold/rho).str(100),
        'safe_sufficient_gap_exact':'3.2031e-153',
        'safe_gap_root_transfer_budget':safe_budget.str(100),
        'ordinary_norm_transfer_gap_threshold':ordinary_gap.str(100),
        'trial_transform_at_gamma':value.str(100),
        'trial_transform_derivative_at_gamma':derivative.str(100),
        'lower_bound_hypotheses':'0 <= l <= mu0 <= rho < b; simple even ground; '
                                 'even excited spectrum >= b; unit f; h=P_ground f; '
                                 '|ell(v)|^2 <= C_ell*q[v]; derivative floor d on root interval.',
        'missing_input':'A certified lower bound l sufficiently close to the COMPLETE trial Rayleigh rho. '
                        'No such lower bound is asserted. A matching trial zero is also needed for a '
                        'gamma-centered 1e-71 enclosure; the frozen trial does not supply it.',
        'direct_bound_limitation':'The direct sqrt(C_ell*rho)/d bound uses an UPPER ground-energy '
                                  'budget, not rho-l. A lower bound alone does not improve it.',
        'resolution_scope':'A floor of these stated archived scalar estimates, not an optimality '
                           'theorem for all arguments using v125/v126 data. The finite CCM '
                           'benchmark scale is below their resolution; the complete discrepancy '
                           'is not proved to have that scale. Failure of the bound, not the object.',
        'inputs':[{'path':str(path.relative_to(coarse.ROOT)), 'sha256':coarse.sha256(path)}],
        'coarse_verifier_sha256':coarse.sha256(COARSE_PATH),
        'verifier_sha256':coarse.sha256(Path(__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits', type=int, choices=(1024,1280), required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), 'Use a fresh output path.'
    result = run(args.bits)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'], args.bits, flush=True)
    for key in ['radius','rayleigh_minus_lower_bound_threshold','relative_gap_threshold',
                'ordinary_norm_transfer_gap_threshold','trial_transform_at_gamma']:
        print(key, result[key], flush=True)


if __name__ == '__main__':
    main()
