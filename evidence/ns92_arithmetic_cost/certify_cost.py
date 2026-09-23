"""Complete NS61-based scalar upper budgets for the NS73 selected cost.

The finite budgets are unconditional; no uniform-in-N bound is asserted.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mobius(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    prime = [True] * (limit + 1)
    mu[0] = 0
    for p in range(2, limit + 1):
        if prime[p]:
            for k in range(p, limit + 1, p):
                prime[k] = False
                mu[k] *= -1
            for k in range(p * p, limit + 1, p * p):
                mu[k] = 0
    return mu


def run(n: int, mu: list[int]) -> dict[str, Any]:
    kappa = (2 * arb.pi()).log() - arb.const_euler()
    alpha = arb(2).log()
    tail, l1, l2, vector2 = arb(0), arb(0), arb(0), arb(0)
    trace = arb(0)
    for k in range(2*n, n, -1):
        tail -= mu[k] * (arb(2*n)/k).log()/k
        # T(x) equals this suffix for k-1 <= x < k.
        l1 += 2 * abs(tail) / (arb(k).sqrt() + arb(k-1).sqrt())
        l2 += tail**2
        vector2 += (k*tail)**2
        trace += (arb(k)/(k-1)).log()/k**2
    upper = kappa*l1**2
    variance_upper = kappa*alpha*l2
    old_trace_upper = kappa*trace*vector2
    assert upper > 0 and variance_upper > 0
    assert upper < variance_upper
    return {"N": n, "values": {k:v.str(65) for k,v in {
        "weighted_Mobius_tail_square_sum": l2,
        "complete_cost_upper": upper,
        "L2_cost_upper": variance_upper,
        "NS61_trace_cost_upper": old_trace_upper,
        "endpoint_old_coefficient": -n*tail,
    }.items()}}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--bits',type=int,required=True)
    p.add_argument('--sizes',type=int,nargs='+',default=[16,64,256,1024,4096,16384,65536])
    p.add_argument('--cutoff-replay',action='store_true')
    p.add_argument('--output',type=Path,required=True)
    args = p.parse_args()
    ctx.prec = args.bits
    mu = mobius(2*max(args.sizes))
    suffix = 'cutoff-384bits' if args.cutoff_replay else f'{args.bits}bits'
    source = ROOT/f'evidence/ns91_joint_abel/endpoint-{suffix}.json'
    prior = {r['N']:r for r in json.loads(source.read_text())['rows']}
    rows = []
    for n in args.sizes:
        row = run(n,mu)
        if n in prior:
            old = prior[n]['values']
            upper = arb(row['values']['complete_cost_upper'])
            true_cost = arb(old['inherited_full_projected_cost'])
            lower = arb(old['positive_lower_numerator'])
            energy = arb(old['E_N'])
            step = arb(1)/512
            step_gain = (2*step*lower-step**2*upper)/energy
            assert step_gain > 0
            assert true_cost < upper
            row['finite_gain'] = {
                'lower_relative_gain': (lower**2/(upper*energy)).str(65),
                'rational_step': '1/512',
                'rational_step_lower_relative_gain':step_gain.str(65),
                'upper_over_true_projected_cost':(upper/true_cost).str(65),
                'inherited_true_cost_for_validation_only':true_cost.str(65),
                'inherited_numerator_for_validation_only':arb(old['inherited_numerator']).str(65),
                'inherited_lower_numerator':lower.str(65),
                'inherited_energy':energy.str(65),
            }
        rows.append(row)
        print(json.dumps(row),flush=True)
    args.output.write_text(json.dumps({
        'classification':'Certified finite scalar cost upper budgets; no cofinal cost or gain estimate',
        'precision_bits':args.bits,'cutoff_replay':args.cutoff_replay,
        'source_sha256':digest(Path(__file__)),
        'input_path':str(source.relative_to(ROOT)),'input_sha256':digest(source),
        'cost_uses_Gram_inverse':False,'rows':rows,
    },indent=2)+'\n')


if __name__ == '__main__':
    main()
