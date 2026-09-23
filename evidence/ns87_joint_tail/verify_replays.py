"""Replay consistency for fixed mathematical quantities; bound endpoints may tighten."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from typing import Any
from flint import arb, ctx

HERE=Path(__file__).resolve().parent
KEYS=['E_N','full_gain','full_relative_gain','tail_energy','tail_energy_fraction',
      'tail_trace','finite_observation_gain','actual_tail_metric',
      'finite_gain_over_actual_gain','complete_Stirling_tail','universal_tail_majorant']


def records(path: Path) -> dict[tuple[int,int],dict[str,Any]]:
    data=json.loads(path.read_text())
    assert data['source_sha256']==hashlib.sha256((HERE/'certify.py').read_bytes()).hexdigest()
    return {(row['N'],entry['T']):entry for row in data['rows'] for entry in row['rows']}


def compare(first: dict[tuple[int,int],dict[str,Any]],second: dict[tuple[int,int],dict[str,Any]]) -> int:
    count=0
    for identity,item in second.items():
        assert identity in first
        assert first[identity]['gates']==item['gates']
        for key in KEYS:
            assert arb(first[identity]['values'][key]).overlaps(arb(item['values'][key])),(identity,key)
            count+=1
    return count


def main() -> None:
    ctx.prec=512
    low=records(HERE/'check-256bits.json')
    high=records(HERE/'check-384bits.json')
    cutoff=records(HERE/'check-cutoff-384bits.json')
    precision=compare(low,high)
    changed=compare(high,cutoff)
    for data in (low,high,cutoff):
        values=data[(32,4096)]['values']
        assert arb(values['safe_step_guaranteed_fraction'])>arb('0.9598')
        assert arb(values['safe_step_guaranteed_gain'])/arb(values['E_N'])>arb('0.1815')
        assert arb(data[(32,64)]['values']['finite_gain_over_actual_gain'])>arb('1.1599')
    log=(HERE/'exact-checks-output.txt').read_text()
    assert 'NS87 exact checks passed: 14' in log and '\nFAIL ' not in log and 'an error' not in log
    report={'classification':'Finite certified replay consistency; not an asymptotic estimate',
            'same_problem_precision_overlaps':precision,'same_problem_kernel_cutoff_overlaps':changed,
            'physical_potential_pairing_checks_per_precision':224,
            'additional_cutoff_potential_pairing_checks':128,
            'finite_cases_per_precision':12,'additional_cutoff_cases':4,
            'Maxima_exact_checks':14,'finite_threshold_gates':True,
            'bound_endpoint_policy':'Only fixed mathematical quantities require interval overlap. Outward-rounded tail budgets and dyadic step scalars may tighten between runs; each run separately certifies its step.'}
    (HERE/'replay-validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__': main()
