"""Cross-check saved Arb enclosures and the two finite gates used in the text."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def main() -> None:
    ctx.prec = 512
    directory = Path(__file__).resolve().parent
    source_hash = hashlib.sha256((directory/'nb_certify.py').read_bytes()).hexdigest()
    reports: list[dict[str, Any]] = [
        json.loads((directory/f'nb-blocks-{bits}bits.json').read_text())
        for bits in [256,384]
    ]
    overlap_count = 0
    for report,bits in zip(reports,[256,384]):
        assert report['precision_bits'] == bits
        assert report['max_index'] == 512
        assert report['source_sha256'] == source_hash
        assert report['adjacent_norm_validation']['strict_lower_and_upper_gates']
    rows_a,rows_b = reports[0]['rows'],reports[1]['rows']
    assert [row['N'] for row in rows_a] == [4,8,16,32,64,128,256]
    assert [row['N'] for row in rows_b] == [row['N'] for row in rows_a]
    table_ranges = {
        128:{'gain_relative':('.14752','.14753'),
             'raw_trace_relative':('.0003503','.0003505'),
             'difference_budget_relative':('.0004286','.0004289'),
             'difference_direction_relative':('.08380','.08381')},
        256:{'gain_relative':('.10289','.10290'),
             'raw_trace_relative':('.0002135','.0002137'),
             'difference_budget_relative':('.0001328','.0001331'),
             'difference_direction_relative':('.05955','.05956')},
    }
    for first,second in zip(rows_a,rows_b):
        assert first['gates'] == second['gates']
        assert first['quantities'].keys() == second['quantities'].keys()
        for key,value in first['quantities'].items():
            assert arb(value).overlaps(arb(second['quantities'][key])),(first['N'],key)
            overlap_count += 1
        for row in [first,second]:
            assert row['minimum_accuracy_bits'] >= 80
            assert row['solve_residuals_contain_zero']
            assert arb(row['gain_identity_difference']).contains(0)
            assert arb(row['difference_gain_identity_difference']).contains(0)
            assert row['gates']['exact_gain_exceeds_raw_bound']
            assert row['gates']['exact_gain_exceeds_projected_bound']
            if row['N'] in [128,256]:
                assert row['gates']['raw_bound_below_one_400th_of_gain']
                for key,(lower,upper) in table_ranges[row['N']].items():
                    value=arb(row['quantities'][key])
                    assert value > arb(lower) and value < arb(upper),(row['N'],key)
            if row['N'] == 256:
                assert row['gates']['difference_budget_bound_below_raw_trace_bound']
    print(json.dumps({'status':'PASS','matching_ball_enclosures':overlap_count,
                      'same_finite_problem_at_bits':[256,384],
                      'table_intervals_checked_at_both_precisions':True,
                      'source_sha256':source_hash},indent=2))


if __name__=='__main__':
    main()
