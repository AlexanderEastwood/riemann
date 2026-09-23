"""Arb q=2 NB blocks with a proved Bernoulli/Hurwitz remainder.

The analytic tail is in gram-tail-proof.tex. No midpoint solves occur.
All inequalities concern finite blocks, not the open cofinal input.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import acb, arb, arb_mat, ctx


def ball(value: Fraction) -> arb:
    return arb(value.numerator)/value.denominator


def coefficient(j: int) -> Fraction:
    harmonic = sum((Fraction(1, k) for k in range(1, j)), Fraction(0))
    return (2*j-3-(j-1)*harmonic)/(j*(j-1))


class Kernel:
    def __init__(self, maximum: int, cutoff: int, order: int) -> None:
        self.cutoff, self.order = cutoff, order
        self.gamma = arb.const_euler()
        self.gamma1 = acb.stieltjes(1).real
        self.log2pi = (2*arb.pi()).log()
        self.kappa = self.log2pi-self.gamma
        self.k1 = (self.log2pi-self.gamma+2)/2
        self.k2 = ((1-self.gamma/2)*self.log2pi+self.log2pi**2/4
                   +arb.pi()**2/48-self.gamma**2/4-self.gamma-self.gamma1+arb(3)/2)
        self.logs = [arb(0)]+[arb(n).log() for n in range(1, maximum*cutoff+1)]
        self.harmonic, self.logfactorial, self.logharmonic = [arb(0)], [arb(0)], [arb(0)]
        for n in range(1, maximum*cutoff+1):
            self.harmonic.append(self.harmonic[-1]+arb(1)/n)
            self.logfactorial.append(self.logfactorial[-1]+self.logs[n])
            self.logharmonic.append(self.logharmonic[-1]+self.logs[n]/n)
        self.coefficients = {j: ball(coefficient(j)) for j in range(4, order+3)}
        self.bernoulli_coefficients = {
            j: [math.comb(j, k)*arb.bernoulli(j-k) for k in range(j+1)]
            for j in range(4, order+3)
        }
        a1 = 2*(order+2)*(order+1)*coefficient(order+2)-(order+1)*order*coefficient(order+1)
        a2 = -(order+2)*(order+1)*coefficient(order+2)
        sup = {j: Fraction(2*math.factorial(j), 6**j)*(1+Fraction(1, j-1))
               for j in range(order, order+3)}
        self.errors = {
            order: ball(sup[order]/(order**2*(order-1))),
            order+1: ball(abs(a1)*sup[order+1]/(order*(order+1))),
            order+2: ball(abs(a2)*sup[order+2]/((order+1)*(order+2))),
        }
        self.hurwitz: dict[tuple[int, int, int], arb] = {}
        self.bernoulli: dict[tuple[int, int, int], arb] = {}
        self.cache: dict[tuple[int, int], arb] = {}

    def bernoulli_value(self, j: int, numerator: int, denominator: int) -> arb:
        key = (j, numerator, denominator)
        if key not in self.bernoulli:
            x, result = arb(numerator)/denominator, arb(0)
            for value in reversed(self.bernoulli_coefficients[j]):
                result = result*x+value
            self.bernoulli[key] = result
        return self.bernoulli[key]

    def s2(self, numerator: int, denominator: int) -> arb:
        key = (numerator, denominator)
        if key in self.cache:
            return self.cache[key]
        total = arb(0)
        logratio = self.logs[numerator]-self.logs[denominator]
        for k in range(1, self.cutoff+1):
            invx, floorx = arb(denominator)/(k*numerator), k*numerator//denominator
            logx = self.logs[k]+logratio
            total += ((self.log2pi/2+1+logx/2)*invx
                      +(2-self.gamma)*logx-logx**2/2+2*self.gamma+self.gamma1-3
                      +((logx+2)*floorx-self.logfactorial[floorx])*invx
                      +(logx-2)*self.harmonic[floorx]-self.logharmonic[floorx])
        for j in range(4, self.order+3):
            progression = arb(0)
            for a in range(1, denominator+1):
                zkey = (j, denominator, a)
                if zkey not in self.hurwitz:
                    self.hurwitz[zkey] = arb(j).zeta(arb(self.cutoff+a)/denominator)
                residue = ((self.cutoff+a)*numerator) % denominator
                progression += self.bernoulli_value(j, residue, denominator)*self.hurwitz[zkey]
            total += self.coefficients[j]*progression/arb(numerator)**j
        inverse_ratio = arb(denominator)/numerator
        error = sum((constant*inverse_ratio**j*arb(j).zeta(self.cutoff+1)
                     for j, constant in self.errors.items()), arb(0))
        total += arb(0, error)
        self.cache[key] = total
        return total

    def gram(self, m: int, n: int) -> arb:
        if m > n:
            m, n = n, m
        divisor = math.gcd(m, n)
        logratio = arb(0) if m == n else self.logs[n]-self.logs[m]
        return ((self.k2+self.k1*logratio+logratio*logratio/4)/n
                +self.s2(n//divisor, m//divisor)/m)

    def load(self, n: int) -> arb:
        logn = self.logs[n]
        return (logn**2/2+(2-self.gamma)*logn+3-2*self.gamma-self.gamma1)/n


def sub(matrix: arb_mat, r0: int, r1: int, c0: int, c1: int) -> arb_mat:
    return arb_mat([[matrix[i, j] for j in range(c0, c1)] for i in range(r0, r1)])


def dot(first: arb_mat, second: arb_mat) -> arb:
    return (first.transpose()*second)[0, 0]


def trace(matrix: arb_mat) -> arb:
    return sum((matrix[i, i] for i in range(matrix.nrows())), arb(0))


def mobius(n: int) -> int:
    sign, divisor = 1, 2
    while divisor*divisor <= n:
        if n % divisor == 0:
            n //= divisor
            sign = -sign
            if n % divisor == 0:
                return 0
        divisor += 1
    return -sign if n > 1 else sign


def laguerre_target(size: int) -> arb:
    """k_(N,1), with the alternating Taylor remainder retained."""
    assert size >= 2
    frequency2 = (2*arb.pi()/size)**2
    total, term = arb(0), arb(2)
    for j in range(64):
        total += term if j % 2 == 0 else -term
        term = term*frequency2*(2*j+1)**2/((2*j+2)*(2*j+3)**3)
    # At and beyond j=64 the ratio is bounded by pi^2/(130*131)<1;
    # subsequent denominators increase. The first omitted term bounds
    # the alternating remainder. This is a ball, not a midpoint value.
    return total+arb(0, term)


def inspect(gram: arb_mat, loads: arb_mat, size: int, kappa: arb) -> dict[str, Any]:
    old, cross = sub(gram, 0, size, 0, size), sub(gram, 0, size, size, 2*size)
    new, oldloads = sub(gram, size, 2*size, size, 2*size), sub(loads, 0, size, 0, 1)
    c = old.solve(oldloads, algorithm="precond")
    h = sub(loads, size, 2*size, 0, 1)-cross.transpose()*c
    schur = new-cross.transpose()*old.solve(cross, algorithm="precond")
    basis, rawmap, budget = arb_mat(size, size), arb_mat(size+1, size), arb(0)
    for j, n in enumerate(range(size+1, 2*size+1)):
        basis[j, j] = rawmap[j+1, j] = 1
        rawmap[j, j] = -arb(n-1)/n
        if j:
            basis[j-1, j] = -arb(n-1)/n
        budget += kappa*(arb(n)/(n-1)).log()/n**2
    raw = rawmap.transpose()*sub(gram, size-1, 2*size, size-1, 2*size)*rawmap
    projected = basis.transpose()*schur*basis
    g = basis.transpose()*h
    energy = 2-dot(oldloads, c)
    gain = dot(g, projected.solve(g, algorithm="precond"))
    normg2 = dot(g, g)
    full, full_load = sub(gram, 0, 2*size, 0, 2*size), sub(loads, 0, 2*size, 0, 1)
    next_energy = 2-dot(full_load, full.solve(full_load, algorithm="precond"))
    assert energy > 0 and gain > 0 and next_energy > 0
    assert (gain-energy+next_energy).contains(0)
    assert (gain-dot(h, schur.solve(h, algorithm="precond"))).contains(0)
    assert trace(raw) < budget and budget < 3*kappa/(8*size**2)
    assert gain > normg2/budget
    residual = old*c-oldloads
    assert all(residual[i, 0].contains(0) for i in range(size))
    mu = [mobius(n) for n in range(1, size+1)]
    mobius_sum = sum((Fraction(value, n) for n, value in enumerate(mu, 1)), Fraction(0))
    canonical = arb_mat([[value] for value in mu])
    canonical[size-1, 0] -= size*ball(mobius_sum)
    canonical_error = 2+2*dot(oldloads, canonical)+dot(canonical, old*canonical)
    eta = ball(mobius_sum-Fraction(sum(mu), size))
    witness_pairing = size*eta-laguerre_target(size)
    witness_squared = witness_pairing*witness_pairing/size
    assert canonical_error > witness_squared and canonical_error > energy
    endpoint_a = 1-sum((c[i, 0] for i in range(size)), arb(0))/2
    endpoint_l = sum((c[m-1, 0]*(arb(m)/(2*arb.pi())).log()
                      for m in range(1, size+1)), arb(0))/2
    coefficient_mass = sum((m*abs(c[m-1, 0]) for m in range(1, size+1)), arb(0))
    leading_squared, remainder_squared = arb(0), arb(0)
    for j, n in enumerate(range(size+1, 2*size+1)):
        logn, logprevious = arb(n).log(), arb(n-1).log()
        logratio = logn-logprevious
        leading = (endpoint_a*((logn*logn-logprevious*logprevious)/2
                               +(2-arb.const_euler())*logratio)+endpoint_l*logratio)/n
        remainder = arb.pi()**2*coefficient_mass/(8*n*n*(n-1))
        assert abs(g[j, 0]-leading) < remainder
        leading_squared += leading*leading
        remainder_squared += remainder*remainder
    quantities = {
        'E_N': energy, 'E_2N': next_energy, 'gain_relative': gain/energy,
        'budget_relative': normg2/budget/energy,
        'simple_budget_relative': 8*size**2*normg2/(3*kappa*energy),
        'budget_fraction_of_gain': normg2/budget/gain,
        'projected_direction_relative': normg2**2/dot(g, projected*g)/energy,
        'raw_trace_scaled': trace(raw)*size**2, 'trace_budget_scaled': budget*size**2,
        'projected_trace_scaled': trace(projected)*size**2,
        'g_norm2_over_E_scaled': size**2*normg2/energy,
        'endpoint_log_coefficient': endpoint_a, 'endpoint_constant': endpoint_l,
        'coefficient_mass': coefficient_mass,
        'endpoint_error_budget_over_leading_norm': (remainder_squared/leading_squared).sqrt(),
        'canonical_smoothed_error_squared': canonical_error,
        'laguerre_witness_squared': witness_squared,
        'canonical_error_over_optimal_error': canonical_error/energy,
    }
    return {
        'N': size, 'quantities': {key: value.str(40) for key, value in quantities.items()},
        'minimum_accuracy_bits': min(v.rel_accuracy_bits() for v in quantities.values()),
        'gain_identity_difference': (gain-energy+next_energy).str(12),
        'gates': {'positive_errors_and_gain': True, 'complete_gain_identity': True,
                  'complete_coordinate_identity': True, 'trace_budget': True,
                  'gain_exceeds_budget_bound': True, 'solve_residual_contains_zero': True,
                  'canonical_error_exceeds_laguerre_witness': True,
                  'canonical_error_exceeds_optimum': True,
                  'all_endpoint_remainder_bounds_pass': True,
                  'endpoint_triangle_bound_is_vacuous': bool(remainder_squared > leading_squared)},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, required=True)
    parser.add_argument('--max-index', type=int, default=64)
    parser.add_argument('--cutoff', type=int, default=128)
    parser.add_argument('--order', type=int, default=24)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    started = time.monotonic()
    kernel = Kernel(args.max_index, args.cutoff, args.order)
    gram, loads = arb_mat(args.max_index, args.max_index), arb_mat(args.max_index, 1)
    for m in range(1, args.max_index+1):
        loads[m-1, 0] = kernel.load(m)
        for n in range(m, args.max_index+1):
            gram[m-1, n-1] = gram[n-1, m-1] = kernel.gram(m, n)
    print(f'Complete Gram built in {time.monotonic()-started:.2f}s', flush=True)
    rows = []
    size = 2
    while 2*size <= args.max_index:
        row = inspect(gram, loads, size, kernel.kappa)
        rows.append(row)
        print(size, row['quantities']['budget_relative'], row['minimum_accuracy_bits'], flush=True)
        size *= 2
    output = {
        'classification': 'certified finite computation, no asymptotic conclusion',
        'precision_bits': args.bits, 'max_index': args.max_index,
        'finite_series_cutoff': args.cutoff, 'bernoulli_remainder_order': args.order,
        'analytic_remainder': 'gram-tail-proof.tex, Lemma ns61-r2-tail',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'gram_1_1': gram[0, 0].str(40), 'rows': rows,
        'elapsed_seconds': time.monotonic()-started,
    }
    args.output.write_text(json.dumps(output, indent=2)+'\n')


if __name__ == '__main__':
    main()
