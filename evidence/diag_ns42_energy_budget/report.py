"""Render the NS-42 diagnostic report; no inferential conclusions."""
from __future__ import annotations
import hashlib
import html
import json
from pathlib import Path
from typing import Any
import mpmath as mp
OUT=Path(__file__).resolve().parent
mp.mp.dps=70

def fmt(value: str) -> str:
    return f'{float(value):.9e}'

def table(headers: list[str], rows: list[list[str]]) -> str:
    th=''.join(f'<th style="text-align:right;padding:7px 5px;border-bottom:2px solid #59665b;">{html.escape(h)}</th>' for h in headers)
    body=''.join('<tr>'+''.join(f'<td style="padding:6px 5px;text-align:right;border-bottom:1px solid #d8dfd8;white-space:nowrap;">{html.escape(v)}</td>' for v in row)+'</tr>' for row in rows)
    return f'<div style="overflow-x:auto;"><table style="border-collapse:collapse;width:100%;font-size:11px;font-variant-numeric:tabular-nums;"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'

def main() -> None:
    rows_global=[]; rows_local=[]; rows_parts=[]; markdown=[]; checks=[]; datafiles=[]
    maximum_residual=mp.mpf(0); maximum_norm_error=mp.mpf(0); maximum_order_change=mp.mpf(0)
    for lam in (3,4):
        for parity in ('even','odd'):
            path=OUT/f'budget_l{lam}_{parity}_g144.json'; data=json.loads(path.read_text()); datafiles.append(path.name)
            low=json.loads((OUT/f'budget_l{lam}_{parity}_g96.json').read_text())
            for v,vlo in zip(data['vectors'],low['vectors']):
                label=f'{lam}/{parity[0]}/{v["k"]}'
                rows_global.append([label]+[fmt(v[key]) for key in ('J_global_direct','variance_term_2over3','odd_negative_pole_magnitude','q_midpoint_matrix')])
                rows_local.append([label]+[fmt(v[key]) for key in ('J_local_direct','potential_integral_direct','signed_pole_Pi')])
                rows_parts.append([label]+[fmt(v[key]) for key in ('J_local_arch_direct','J_local_prime_direct','exterior_energy_direct')])
                markdown.append('| '+label+' | '+' | '.join(fmt(v[key]) for key in ('J_global_direct','variance_term_2over3','odd_negative_pole_magnitude','J_local_direct','potential_integral_direct','signed_pole_Pi','q_midpoint_matrix'))+' |')
                changes={key:mp.mpf(v[key])-mp.mpf(vlo[key]) for key in ('J_global_direct','J_local_direct','variance_term_2over3','potential_integral_direct')}
                maximum_residual=max(maximum_residual,abs(mp.mpf(v['global_identity_residual'])))
                maximum_norm_error=max(maximum_norm_error,abs(mp.mpf(v['norm2_quadrature'])-1))
                maximum_order_change=max(maximum_order_change,*[abs(delta)/(1+abs(mp.mpf(v[key]))) for key,delta in changes.items()])
                checks.append({'lambda':lam,'parity':parity,'k':v['k'],'g144_minus_g96':{key:mp.nstr(val,30) for key,val in changes.items()},'global_identity_residual_g144':v['global_identity_residual'],'norm2_error_g144':mp.nstr(mp.mpf(v['norm2_quadrature'])-1,30)})
    checks_summary={'maximum_absolute_identity_residual':mp.nstr(maximum_residual,30),'maximum_absolute_norm_error':mp.nstr(maximum_norm_error,30),'maximum_scaled_order_change':mp.nstr(maximum_order_change,30),'rows':checks}
    (OUT/'checks.json').write_text(json.dumps(checks_summary,indent=2)+'\n')
    scope='First three generalized pencil directions k=0,1,2 at each existing λ=3,4; N=48 gives 49 even modes and 48 odd modes. All vectors have ordinary L² norm one. The even vectors are raw and are not asserted to be orthogonal to the actual source. Odd vectors have odd parity and hence no even-source constraint.'
    basis='Set a=log λ. The physical coordinates are e₀(x)=1/√(2a), eₙ(x)=(-1)ⁿ cos(nπx/a)/√a in the even sector, and eₙ(x)=(-1)ⁿ sin(nπx/a)/√a in the odd sector, on (-a,a), extended by zero. The (-1)ⁿ factors are retained from the block() matrix convention. These are the first three eigenvectors of Wv=ν(W+W⁻)v, rather than the first three ordinary eigenvectors of W.'
    definitions='Use the unnormalized Gaussian weight h of eq:v150-weight, g=f/h inside the window and g=0 outside, c=cosh(x/2), s=sinh(x/2), Iₕ=1/√3 and dν=c h dx/Iₕ. J denotes the full squared-edge energy of eq:v150-global-energy; Jₐ denotes the same energy restricted to edges whose two endpoints are inside the window. E=∫(Tₐ/h)|f|² is the exterior edge contribution, so J=Jₐ+E. V=(2/3)Varν(g). The signed potential entry is R=∫rₐ|f|², with rₐ=(Tₐ−2Iₕc)/h. It is not ∫(rₐ)₋|f|². Π=2|∫cf|²−2|∫sf|²; S=2|∫sf|² is the nonnegative odd negative-pole magnitude. The identities are q=J−V−S and q=Jₐ+R+Π.'
    method='The pencil uses the original float W⁻ grid (0.001≤ξ<4000 with steps 0.002 and 0.01) and 1024-bit Arb W converted to midpoint mpmath arithmetic at 150 decimal digits. That defines the frozen diagnostic vectors; it is not an accuracy certificate for the pencil. Each vector is saved with 130 significant digits. Matrix q and pencil residuals are computed internally before decimal export; their printed residuals are not claims about exact arithmetic on the exported decimals.'
    quadrature='Jₐ is measured directly from nonnegative squared-edge integrands, with continuous and prime parts saved separately. E and ∫c|f|²/h are independently integrated; the two pole moments are evaluated by analytic Fourier-basis formulas. Gauss–Legendre orders 96 and 144 use float64 nodes and weights with mpmath integrands at 70 and 90 decimal digits respectively. The Gaussian sum is numerically truncated at n=8, exterior prime sums at n=16λ, and exterior continuous integration at y=log(16λ); no truncation enclosure is claimed. The report displays the order-144 run. Both raw runs, all per-prime contributions, norms and residuals are archived.'
    limits=f'The largest order-144 absolute residual in J−V−S−q is {float(maximum_residual):.6e}; the largest quadrature norm error is {float(maximum_norm_error):.6e}. The largest change from order 96 to 144, divided by 1+the magnitude of the order-144 value, is {float(maximum_order_change):.6e} across J, Jₐ, V and R. These are diagnostic comparisons, not error bounds. The independent integrations do not resolve the tiny matrix q values. JSON fields named identity_reconstructed add q to the separately measured subtractive terms and are expressly not independent measurements of J.'
    intro='<p style="color:#854011;font-weight:bold;letter-spacing:.03em;">DIAGNOSTIC, NOT A CERTIFICATE.</p><h1 style="font-size:30px;line-height:1.1;margin:14px 0;">NS-42 · Transformed energy budgets</h1><p style="color:#657065;">22 September 2026 · version 1 · first three directions, both parities</p>'
    def para(text: str) -> str:
        return f'<p style="margin:16px 0;">{html.escape(text)}</p>'
    body=intro+para(scope)+para(basis)+para(definitions)+para(method)+para(quadrature)
    body+='<h2 style="font-size:21px;margin-top:28px;">Global identity: q = J − V − S</h2>'+table(['λ/parity/k','J, direct','V, direct','S, analytic','q, midpoint W'],rows_global)
    body+='<h2 style="font-size:21px;margin-top:28px;">Local identity: q = Jₐ + R + Π</h2>'+table(['λ/parity/k','Jₐ, direct','R, signed potential','Π, signed pole'],rows_local)
    body+='<h2 style="font-size:21px;margin-top:28px;">Direct edge components</h2>'+table(['λ/parity/k','Jₐ continuous','Jₐ primes','E exterior'],rows_parts)+para(limits)
    body+='<h2 style="font-size:21px;margin-top:28px;">Record and replay</h2>'+para('freeze.py reproduces the fixed pencil directions; measure.py evaluates the budgets for a specified window, parity, order and decimal precision; report.py formats these saved outputs. The base v1.50 manuscript was actually built: 246 pages, zero undefined or duplicate references. Python diagnostics: zero errors and warnings. No manuscript, research-map, certificate or version-number change is part of NS-42.')
    links=' '.join(f'<a style="color:#285c45;" href="{name}">{name}</a>' for name in datafiles)
    body+=f'<p style="font-size:12px;word-break:break-all;">{links}</p>'+para('Numerical illustrations only. No all-window, admissibility, bound, G2 or RH inference is made from this table.')
    document='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NS-42 transformed energy budgets · 2026-09-22 v1</title></head><body style="margin:0;background:#f3f5ef;color:#253026;font-family:Georgia,serif;line-height:1.6;"><main style="max-width:680px;margin:30px auto;padding:30px 24px;background:#fff;">'+body+'</main></body></html>\n'
    (OUT/'ns42-energy-budgets-2026-09-22-v1.html').write_text(document)
    md='DIAGNOSTIC, NOT A CERTIFICATE.\n\n# NS-42 transformed energy budgets\n\n'+scope+'\n\n'+basis+'\n\n'+definitions+'\n\n'+method+'\n\n'+quadrature+'\n\n| λ/parity/k | J global | V=2/3 Var | S odd pole | J local | R potential | Pi pole | q midpoint W |\n|---|---:|---:|---:|---:|---:|---:|---:|\n'+'\n'.join(markdown)+'\n\n'+limits+'\n\n## Replay\n\n```sh\n.venv/bin/python evidence/diag_ns42_energy_budget/freeze.py\n.venv/bin/python evidence/diag_ns42_energy_budget/measure.py 3 even --order 96 --dps 70\n.venv/bin/python evidence/diag_ns42_energy_budget/measure.py 3 even --order 144 --dps 90\n# Repeat the two measure calls for 3 odd, 4 even, 4 odd.\n.venv/bin/python evidence/diag_ns42_energy_budget/report.py\n```\n\nThe original assembly may regenerate its sequence caches; they are not a separate certificate. The frozen vectors and all eight measurement outputs are archived here. Ordinary norm checks, per-prime terms and internal matrix residuals are saved. The HTML report is the delivered document.\n\nValidation: actual base-v1.50 build 246 pages, zero undefined/duplicate references; Python diagnostics zero errors/warnings. No manuscript or map edits. Nothing in this diagnostic is cited as a bound.\n'
    (OUT/'results.md').write_text(md)

if __name__=='__main__': main()
