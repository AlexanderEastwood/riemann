"""Arb finite checks of the complete first-annulus forcing and renewal energies.

No finite table establishes the open square-root-plus-epsilon estimate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, ctx

SIBLING = Path(__file__).resolve().parents[1] / 'ns67'
sys.path.insert(0, str(SIBLING))
from certify_cells import mobius_sieve


def primitive(t: arb, logt: arb, a: arb, b: int, c: arb) -> arb:
    return (a*a*t+a*b*logt*logt+2*a*c*logt
            -b*b*(logt*logt+2*logt+2)/t-2*b*c*(logt+1)/t-c*c/t)


def run(sizes: list[int]) -> dict[str, Any]:
    maximum = 2*max(sizes)
    started = time.monotonic()
    mu = mobius_sieve(maximum)
    v = arb(2).log()
    needed = set(sizes) | {2*n for n in sizes}
    records: dict[int, dict[str, Any]] = {}
    m_top, m_low = 0, 0
    s_top, s_low, l_top, l_low = arb(0), arb(0), arb(0), arb(0)
    eta_energy, forcing_energy, p_integral = arb(0), arb(0), arb(0)
    for j in range(1, maximum+1):
        t, logj = arb(j), arb(j).log()
        if mu[j]:
            m_top += mu[j]
            s_top += arb(mu[j])/j
            l_top += mu[j]*logj
        if j % 2 == 0 and mu[j//2]:
            m_low += mu[j//2]
            s_low += arb(mu[j//2])/(j//2)
            l_low += mu[j//2]*arb(j//2).log()
        if j in needed:
            records[j] = {'M':m_top,'s':s_top,'L':l_top,'p':j*s_top-m_top,
                          'eta_energy':eta_energy,'forcing_half_energy':forcing_energy,
                          'p_integral':p_integral}
        if j == maximum:
            break
        next_t, next_log = arb(j+1), arb(j+1).log()
        h = next_log-logj
        eta_energy += s_top*s_top-2*s_top*m_top*h+arb(m_top*m_top)/(j*(j+1))
        # On t in [j,j+1], f(t/2) = a*t+b*log(t)+c.
        a, b, c = v*s_low/2, m_top-m_low, -(l_top-l_low)
        forcing_energy += primitive(next_t,next_log,a,b,c)-primitive(t,logj,a,b,c)
        p_integral += s_top-m_top*h
    theta = arb(1)/2
    factor = (-theta*v).exp()
    q = (1-v)*factor+(1-factor)/theta
    assert q > 0 and q < 1
    rows = []
    for n in sizes:
        first, second = records[n], records[2*n]
        p_n, p_2n = first['p'], second['p']
        full_forcing = n*first['s']*v+(second['M']-first['M'])*arb(2*n).log()-(second['L']-first['L'])
        interval = second['p_integral']-first['p_integral']
        residual = full_forcing-p_2n+(1-v)*p_n+interval
        assert residual.contains(0)
        ee, ge = first['eta_energy'], first['forcing_half_energy']
        assert ee > 0 and ge > 0
        ratio = ge/ee
        assert ratio > (1-q)*(1-q) and ratio < (1+q)*(1+q)
        balls = {'p':p_n,'forcing':full_forcing,'p_scaled':p_n/arb(n).sqrt(),
                 'forcing_scaled':full_forcing/arb(n).sqrt(),
                 'eta_energy':ee,'forcing_half_energy':ge,'energy_ratio':ratio,
                 'renewal_integral':interval,'renewal_residual':residual,
                 'weighted_lower_factor':(1-q)*(1-q),
                 'weighted_upper_factor':(1+q)*(1+q)}
        assert all(value.is_finite() for value in balls.values())
        rows.append({'N':n,'balls':{key:value.str(70) for key,value in balls.items()},
                     'gates':{'complete_renewal_identity':True,'critical_energy_comparison':True,
                              'all_fields_finite':True}})
    constants=[]
    for numerator,denominator in [(1,4),(1,2),(3,4),(1,1)]:
        th=arb(numerator)/denominator
        damping=(-th*v).exp()
        mass=(1-v)*damping+(1-damping)/th
        transfer=damping/(1-mass)
        assert mass>0 and mass<1
        constants.append({'theta':f'{numerator}/{denominator}','kernel_mass':mass.str(70),
                          'power_transfer_constant':transfer.str(70)})
    return {'classification':'certified finite identities and constants, not a cofinal growth bound',
            'precision_bits':ctx.prec,'maximum_mobius_index':maximum,
            'seconds':round(time.monotonic()-started,3),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'sibling_source_sha256':hashlib.sha256((SIBLING/'certify_cells.py').read_bytes()).hexdigest(),
            'rows':rows,'constants':constants}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--bits',required=True,type=int)
    parser.add_argument('--sizes',required=True,nargs='+',type=int)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    ctx.prec=args.bits
    report=run(args.sizes)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'PASS','precision_bits':args.bits,
                      'sizes':args.sizes,'seconds':report['seconds'],
                      'critical_weight_constants':report['constants'][1]}))


if __name__=='__main__':
    main()
