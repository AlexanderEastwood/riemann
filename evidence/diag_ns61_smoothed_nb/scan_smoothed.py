"""Numerical illustration only: truncated Ehm q=2 Gram, no enclosures.

The cutoff and precision must both be varied. All projections retain the
complete old/new Gram. No finite result establishes an asymptotic bound.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path
from typing import Any

import mpmath as mp


class Kernel:
    def __init__(self, maximum: int, cutoff: int) -> None:
        self.cutoff = cutoff
        self.gamma = mp.euler
        self.gamma1 = mp.stieltjes(1)
        self.log2pi = mp.log(2*mp.pi)
        self.kappa = self.log2pi-self.gamma
        self.k1 = (self.log2pi-self.gamma+2)/2
        self.k2 = ((1-self.gamma/2)*self.log2pi+self.log2pi**2/4
                   +mp.pi**2/48-self.gamma**2/4-self.gamma-self.gamma1+mp.mpf(3)/2)
        self.logs = [mp.mpf(0)]+[mp.log(n) for n in range(1, maximum*cutoff+1)]
        self.harmonic = [mp.mpf(0)]
        self.logfactorial = [mp.mpf(0)]
        self.logharmonic = [mp.mpf(0)]
        for n in range(1, maximum*cutoff+1):
            self.harmonic.append(self.harmonic[-1]+mp.mpf(1)/n)
            self.logfactorial.append(self.logfactorial[-1]+self.logs[n])
            self.logharmonic.append(self.logharmonic[-1]+self.logs[n]/n)
        self.cache: dict[tuple[int, int], Any] = {}

    def s2(self, numerator: int, denominator: int) -> Any:
        key = (numerator, denominator)
        if key in self.cache:
            return self.cache[key]
        total = mp.mpf(0)
        logratio = self.logs[numerator]-self.logs[denominator]
        for k in range(1, self.cutoff+1):
            invx = mp.mpf(denominator)/(k*numerator)
            floorx = k*numerator//denominator
            logx = self.logs[k]+logratio
            r2 = ((self.log2pi/2+1+logx/2)*invx
                  +(2-self.gamma)*logx-logx**2/2+2*self.gamma+self.gamma1-3
                  +((logx+2)*floorx-self.logfactorial[floorx])*invx
                  +(logx-2)*self.harmonic[floorx]-self.logharmonic[floorx])
            total += r2
        self.cache[key] = total
        return total

    def gram(self, m: int, n: int) -> Any:
        if m > n:
            m, n = n, m
        divisor = math.gcd(m, n)
        logratio = self.logs[n]-self.logs[m]
        return ((self.k2+self.k1*logratio+logratio**2/4)/n
                +self.s2(n//divisor, m//divisor)/m)

    def load(self, n: int) -> Any:
        logn = self.logs[n]
        return (logn**2/2+(2-self.gamma)*logn+3-2*self.gamma-self.gamma1)/n


def dot(a: Any, b: Any) -> Any:
    return (a.T*b)[0]


def inspect(gram: Any, loads: Any, size: int, kappa: Any) -> dict[str, Any]:
    old = gram[:size, :size]
    cross = gram[:size, size:2*size]
    new = gram[size:2*size, size:2*size]
    oldloads = loads[:size, :]
    c = mp.lu_solve(old, oldloads)
    inverse_cross = old**-1*cross
    h = loads[size:2*size, :]-cross.T*c
    schur = new-cross.T*inverse_cross
    basis = mp.eye(size)
    rawmap = mp.matrix(size+1, size)
    budget = mp.mpf(0)
    for j, n in enumerate(range(size+1, 2*size+1)):
        rawmap[j+1, j] = 1
        rawmap[j, j] = -mp.mpf(n-1)/n
        if j:
            basis[j-1, j] = -mp.mpf(n-1)/n
        budget += kappa*mp.log(mp.mpf(n)/(n-1))/n**2
    raw = rawmap.T*gram[size-1:2*size, size-1:2*size]*rawmap
    projected = basis.T*schur*basis
    g = basis.T*h
    energy = 2-dot(oldloads, c)
    gain = dot(g, mp.lu_solve(projected, g))
    normg2 = dot(g, g)
    nextloads = loads[:2*size, :]
    nextenergy = 2-dot(nextloads, mp.lu_solve(gram[:2*size, :2*size], nextloads))
    coefficients_mass = sum(m*abs(c[m-1]) for m in range(1, size+1))
    a = 1-sum(c)/2
    d = sum(c[m-1]*mp.log(m/(2*mp.pi)) for m in range(1, size+1))/2
    quantities = {
        'E_N': energy, 'E_2N': nextenergy, 'gain_relative': gain/energy,
        'gain_identity_defect': abs(gain-energy+nextenergy),
        'budget_relative': normg2/budget/energy,
        'simple_budget_relative': 8*size**2*normg2/(3*kappa*energy),
        'budget_fraction_of_gain': normg2/budget/gain,
        'projected_direction_relative': normg2**2/dot(g, projected*g)/energy,
        'raw_trace_scaled': sum(raw[i, i] for i in range(size))*size**2,
        'trace_budget_scaled': budget*size**2,
        'projected_trace_scaled': sum(projected[i, i] for i in range(size))*size**2,
        'g_norm2_over_E_scaled': size**2*normg2/energy,
        'endpoint_log_coefficient': a, 'endpoint_constant': d,
        'coefficient_mass': coefficients_mass,
    }
    return {'N': size, **{key: mp.nstr(value, 30) for key, value in quantities.items()}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-index', type=int, default=32)
    parser.add_argument('--cutoff', type=int, default=512)
    parser.add_argument('--digits', type=int, default=60)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.digits
    started = time.monotonic()
    kernel = Kernel(args.max_index, args.cutoff)
    gram = mp.matrix(args.max_index)
    for m in range(1, args.max_index+1):
        for n in range(m, args.max_index+1):
            gram[m-1, n-1] = gram[n-1, m-1] = kernel.gram(m, n)
    loads = mp.matrix([kernel.load(n) for n in range(1, args.max_index+1)])
    rows = []
    size = 2
    while 2*size <= args.max_index:
        row = inspect(gram, loads, size, kernel.kappa)
        rows.append(row)
        print(json.dumps(row), flush=True)
        size *= 2
    output = {
        'classification': 'numerical illustration, not a certificate',
        'source': 'https://arxiv.org/html/2405.06349v1, Theorem 2.1, q=2',
        'tail': 'S2 series truncated without an enclosure; compare cutoff replays',
        'max_index': args.max_index, 'cutoff': args.cutoff, 'decimal_digits': args.digits,
        'gram_1_1': mp.nstr(gram[0, 0], 30), 'rows': rows,
        'elapsed_seconds': time.monotonic()-started,
    }
    args.output.write_text(json.dumps(output, indent=2)+'\n')


if __name__ == '__main__':
    main()
