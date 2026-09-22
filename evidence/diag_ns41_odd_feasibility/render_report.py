"""Render the versioned NS-41 diagnostic report from the frozen data."""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

OUT = Path(__file__).resolve().parent
TABLE = 'border-collapse:collapse;width:100%;font-size:13px;margin:14px 0 24px;'
CELL = 'padding:6px 7px;border-bottom:1px solid #ddd;text-align:right;vertical-align:top;'
HEAD = 'padding:6px 7px;border-bottom:2px solid #555;text-align:right;vertical-align:top;'


def table(headers: list[str], rows: list[list[str]]) -> str:
    top = ''.join(f'<th style="{HEAD}">{html.escape(x)}</th>' for x in headers)
    body = ''.join('<tr>' + ''.join(f'<td style="{CELL}">{html.escape(x)}</td>' for x in row) + '</tr>' for row in rows)
    return f'<table style="{TABLE}"><thead><tr>{top}</tr></thead><tbody>{body}</tbody></table>'


def number(value: float | str, digits: int = 10) -> str:
    return f'{float(value):.{digits}g}'


def slacks(screen: dict[str, Any]) -> str:
    rows = [[str(i), number(required, 13), number(mass, 13), number(slack, 13), number(ratio, 10)]
            for i, (required, mass, slack, ratio) in enumerate(zip(
                screen['required'], screen['masses'], screen['slacks'], screen['ratios']))]
    return table(['Bin', 'Required m_b', 'Measured μ_b', 'Slack μ_b−m_b', 'μ_b/m_b'], rows)


def main() -> None:
    payloads = {lam: json.loads((OUT / f'lambda{lam}.json').read_text()) for lam in (3, 4, 6, 8)}
    selected: dict[int, Any] = {}
    rows, initial, dual_rows, precision = [], [], [], []
    for lam, data in payloads.items():
        path = OUT / f'lambda{lam}-improved.json'
        candidate = json.loads(path.read_text()) if path.exists() else None
        if candidate is not None and candidate['all_grid_constraints_pass_at_one']:
            selected[lam] = candidate
        else:
            selected[lam] = {'screens': [data['pure_search']['best']['screen'], data['pure_grid2']],
                             'energy_rechecks': data['energy_rechecks'], 'vector_decimal': data['pure_search']['best']['vector_decimal']}
        state = selected[lam]
        rows.append([str(lam), number(state['energy_rechecks'][-1]['normalized_energy_midpoint'], 12),
                     number(state['screens'][0]['min_ratio']), number(state['screens'][1]['min_ratio']),
                     number(min(s['min_slack'] for s in state['screens']))])
        initial.append([str(lam), str(data['pure_search']['best']['rank']),
                        number(data['energy_rechecks'][-1]['normalized_energy_midpoint'], 12),
                        number(data['pure_search']['best']['screen']['min_ratio']), number(data['pure_grid2']['min_ratio'])])
        dual = data['dual_grid1']
        dual_rows.append([str(lam), number(dual['value_float']),
                          number(dual['spectral_term_float']), number(dual['linear_term_float']),
                          number(dual['minimizing_eigenvector_screen']['min_ratio'])])
        rechecks = state['energy_rechecks']
        precision.append([str(lam), '/'.join(str(x['bits']) for x in rechecks),
                          '/'.join(str(x['decimal_digits']) for x in rechecks),
                          str(rechecks[0]['normalized_energy_midpoint'] == rechecks[1]['normalized_energy_midpoint'])])
    replay = json.loads((OUT / 'frozen-replay.json').read_text())
    maximum_error = max(row['maximum_mass_difference_from_matrix_screen'] for row in replay['checks'])
    assert all(row['all_slacks_positive'] for row in replay['checks'])
    parts = ['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">',
        '<title>NS-41 odd-sector weighted-bin measurements — 2026-09-22 v2</title>',
        '<body style="margin:0;background:#f5f3ee;color:#222;font-family:Georgia,serif;line-height:1.55;">',
        '<main style="max-width:680px;margin:36px auto;padding:36px;background:white;">',
        '<p style="font:700 12px Arial,sans-serif;letter-spacing:1px;color:#8d2a19;">DIAGNOSTIC, NOT A CERTIFICATE</p>',
        '<h1 style="font-size:28px;line-height:1.2;margin:12px 0;">NS-41: odd-sector weighted-bin feasibility</h1>',
        '<p style="color:#555;">2026-09-22 · version 2 · Codex · baseline a0e916a, manuscript v1.50</p>',
        '<p>Pure odd states pass all twenty weighted bins at c′=1 at each of the existing windows λ=3,4,6,8. Every primal energy belongs to a fixed saved feasible vector, rechecked at two arithmetic precisions. These are numerical feasibility measurements, not minimum energies, complete-space bounds, or all-Borel statements.</p>',
        '<h2 style="font-size:21px;margin-top:30px;">Feasible pure witnesses</h2>',
        table(['λ', 'Fixed-vector q', 'Min ratio, grid 1', 'Min ratio, grid 2', 'Smallest slack'], rows),
        '<p>The table uses the improved witness at λ=3,6,8 and the interior witness at λ=4. All constraints are checked after normalizing the exact saved decimal coefficient vector. The λ=4 witness is already below the double-precision energy scale; no float energy minimization was applied there. No equality between a primal and a dual value is asserted.</p>',
        '<h2 style="font-size:21px;margin-top:30px;">The finite problem and directions of the numbers</h2>',
        '<p>Let L=2 log λ. The 256-dimensional odd head has the orthonormal basis e_n(x)=(-1)^n√(2/L) sin(2πnx/L), n=1,…,256, on (-L/2,L/2), extended by zero. The Fourier transform uses 1/√(2π). The prescribed source is even, so every odd vector is source-orthogonal by parity; no approximate source or projection is used.</p>',
        '<p>For bin b, M_b=2 Σ_{j∈b} h_j F(ξ_j)F(ξ_j)ᵀ is a mass matrix. The requirement is vᵀM_bv/‖v‖² ≥ m_b, where m_b=Σ_{j∈b}h_j/800. These are mass constraints, not level-density constraints. The factor two in M_b accounts for negative frequencies; m_b is normalized one-sided level measure. Every slack is μ_b−m_b. A positive slack passes that numerical grid inequality.</p>',
        '<p>Grid 1 repeats the historical centers .001,.003,… below 40 and 40.005,40.010,… below 800, with widths .002 and .005. Their interval weights total 799.995. This grid leaves a .0025 gap immediately above 40 and stops .0025 below 800; its denominator remains 800. Grid 2 bisects the same weighted intervals. No tail is included or estimated. For each λ, twenty edges are frozen at equal spacings between the original sampled minimum of β and zero. The first bin extends downward so new lower samples stay counted; zero is excluded.</p>',
        '<p>The energy q is evaluated from the untruncated-symbol finite odd block assembled by the archived Arb routine, using its midpoints. It is not the truncated grid integral of β|Fv|². In exact arithmetic a feasible state’s energy is an upper bound for the optimum over this same finite-bin problem. Here the slacks and energy evaluations are unenclosed diagnostics, so no certified numerical upper bound is claimed. Passing two finite grids does not establish the continuum-bin inequalities, all-Borel WLH, or cofinal uniformity.</p>',
        '<h2 style="font-size:21px;margin-top:30px;">Separate dual measurements</h2>',
        '<p>For y_b≥0, the exact expression d(y)=λ_min(W−Σ_b y_bM_b)+Σ_b y_bm_b is a lower bound on the grid-1 mixed-state minimum, and hence on its pure-state minimum. The numbers below are float approximations to that expression, without error enclosures. The two terms can cancel at the floating-point scale. A negative float dual value is not a negative Weil direction. The optimizing matrix’s lowest eigenvector is not assumed feasible and is not used as a primal witness.</p>',
        table(['λ', 'Float dual d', 'Spectral term', 'Linear term', 'Eigenvector min ratio'], dual_rows),
        '<p>All multipliers and every constraint slack of these eigenvectors are archived separately from the primal witnesses. A dual lower value does not establish existence or an upper energy bound; no primal-dual equality is claimed.</p>',
        '<h2 style="font-size:21px;margin-top:30px;">Every selected primal constraint</h2>']
    for lam, state in selected.items():
        for screen in state['screens']:
            parts.append(f'<details style="margin:12px 0;"><summary style="font-weight:bold;cursor:pointer;">λ={lam}, selected pure witness, grid {screen["refinement"]}</summary>{slacks(screen)}</details>')
    parts.append('<h2 style="font-size:21px;margin-top:30px;">Every dual eigenvector constraint, separately</h2>')
    for lam, data in payloads.items():
        screen = data['dual_grid1']['minimizing_eigenvector_screen']
        parts.append(f'<details style="margin:12px 0;"><summary style="font-weight:bold;cursor:pointer;">λ={lam}, dual minimizing eigenvector, grid 1 — not used as an upper witness</summary>{slacks(screen)}</details>')
    parts.extend(['<h2 style="font-size:21px;margin-top:30px;">Replays and preserved proposals</h2>',
        '<p>The original interior witnesses are retained; subsequent local energy searches impose all forty grid-1/grid-2 inequalities at c′=1.03. Only explicitly passing states enter the selected primal table. Failed intermediate searches are optimization records, not infeasibility results.</p>',
        table(['λ', 'Initial search rank', 'Initial fixed q', 'Grid 1 min ratio', 'Grid 2 min ratio'], initial),
        table(['λ', 'Assembly bits', 'Arithmetic digits', '60-digit strings agree'], precision),
        f'<p>A separate replay evaluates the saved vectors’ Fourier transforms directly, without mass matrices or optimization, and uses scipy digamma rather than the proposal helper’s asymptotic branch. All fourteen vector/grid replays pass. The largest mass difference from the matrix screen is {maximum_error:.4g}. Precision agreement and grid stability are not error enclosures.</p>',
        '<p>Files: <a href="measure.py">proposal and dual measurements</a>; <a href="refine_energy.py">feasible energy improvement</a>; <a href="verify_frozen.py">direct frozen-vector replay</a>; <a href="frozen-replay.json">all replay numbers</a>; <a href="inventory.json">artifact and source hashes</a>. Each lambda*.json saves its full vector, bin edges, masses, requirements, all slacks, dual multipliers, and precision rechecks. Text outputs print each constraint individually.</p>',
        '<p>A bounded independent read-only review of the scripts, saved data and v1 report found no MAJOR or MINOR issue. Version 2 clarifies the opening phrase to “Every primal energy”; version 1 remains preserved. See <a href="peer-review.txt">the peer-review record</a>.</p>',
        '<p>Validation: Python diagnostics report zero errors and zero warnings. The unchanged v1.50 manuscript was built: 246 pages, zero undefined or duplicate references. No manuscript, map, other diagnostic, window, or tail metric was changed. No G2 or RH claim is made.</p>',
        '</main></body></html>'])
    (OUT / 'odd-weighted-bin-measurements-2026-09-22-v2.html').write_text('\n'.join(parts) + '\n')
    text = '''DIAGNOSTIC, NOT A CERTIFICATE.

NS-41 measures odd-sector finite-head weighted-bin feasibility at c'=1 on the existing windows lambda=3,4,6,8. The 256 odd sine modes are automatically orthogonal to the even source. All reported upper witnesses are pure states with each of twenty constraints checked individually on two grids; no mixed/pure equality or energy optimum is claimed.

The user-facing report is [the versioned HTML report](odd-weighted-bin-measurements-2026-09-22-v2.html). Its tables specify each number's scope and direction and print all selected primal and separate dual-eigenvector slacks.

Run from the repository root with the existing virtual environment:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python evidence/diag_ns41_odd_feasibility/measure.py 3 4 6 8
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python evidence/diag_ns41_odd_feasibility/refine_energy.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python evidence/diag_ns41_odd_feasibility/verify_frozen.py
.venv/bin/python evidence/diag_ns41_odd_feasibility/render_report.py
```

`measure.py` saves interior pure witnesses and a separately labelled float dual. `refine_energy.py` performs a local feasible pure-state improvement at lambda=3,6,8 with all forty grid constraints. Lambda=4 is already below the float energy scale, so no float energy minimization is performed there. Fixed saved vector energies are re-evaluated at 80/120 decimal digits with separate 1024/1280 or 2048/2304-bit assemblies. All are midpoint diagnostics, not ball enclosures.

`verify_frozen.py` evaluates every saved witness directly on both grids without assembling M_b or rerunning the optimizer, and evaluates beta using scipy digamma. The first bin is extended below the original sampled minimum; other edges are frozen. The reference normalization is 800; the deliberately gapped grid covers total interval weight 799.995. No tail completion or tail metric is performed.

No all-Borel WLH, continuum-bin feasibility, cofinal uniformity, positivity, G2 or RH claim follows. The unchanged manuscript build is 246 pages with zero undefined/duplicate references. The inventory records hashes; it is not a certificate.
'''
    (OUT / 'results.md').write_text(text)


if __name__ == '__main__':
    main()
