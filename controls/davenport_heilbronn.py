"""Davenport-Heilbronn known-false analogue for screening RH proposals.

DIAGNOSTIC, NOT A CERTIFICATE. Floating point (mpmath), no interval bounds.

The Davenport-Heilbronn function f(s) (Titchmarsh, sect. 10.25) is a linear
combination of the two Dirichlet L-functions for the odd characters mod 5.
Its completion Lambda(s) is real on the critical line, satisfies the same
shape of functional equation as Riemann's xi, and its theta-type kernel
phi_f is even with double-exponential decay -- yet f has zeros with
Re s != 1/2. Any argument that establishes positivity for Riemann's kernel
using only evenness, decay and the modular completion of the kernel would
apply verbatim here and would prove a false statement.

Use: evaluate a candidate inequality or identity on F_f and phi_f before
proving it for xi. If it holds here, it cannot imply RH.

    python controls/davenport_heilbronn.py             # run the three checks
    from controls.davenport_heilbronn import phi, F     # use in your own screen
"""
from __future__ import annotations

import argparse
import json
from typing import Any, Callable

import mpmath as mp

I = mp.mpc(0, 1)


def C(re: str | float, im: str | float = 0) -> Any:
    """Complex constructor that survives mpmath's int-only stubs."""
    return mp.mpmathify(re) + mp.mpmathify(im) * I

Q = 5
# Odd character mod 5 with chi(2) = i: chi(1)=1, chi(2)=i, chi(3)=-i, chi(4)=-1.
CHI = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}


def chi(n: int) -> complex:
    return CHI[n % Q]


def kappa() -> mp.mpf:
    return (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)


def weights() -> tuple[Any, Any]:
    k = kappa()
    return (1 - I * k) / 2, (1 + I * k) / 2


def dirichlet_L(s: Any, conj: bool = False) -> Any:
    vals = [C(chi(n).real, chi(n).imag) if n else C(0) for n in range(Q)]
    if conj:
        vals = [mp.conj(v) for v in vals]
    return mp.dirichlet(s, vals)


def f(s: Any) -> Any:
    a, b = weights()
    return a * dirichlet_L(s) + b * dirichlet_L(s, conj=True)


def Lambda(s: Any) -> Any:
    """Completed function: even about s = 1/2 (checked by `check_evenness`)."""
    return mp.power(mp.mpf(Q) / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * f(s)


def F(z: Any) -> Any:
    """Analogue of F(z) = xi(1/2+z)/2 in evidence/ns100_reassessment/argument.tex."""
    return Lambda(mp.mpf(1) / 2 + z)


def theta_twisted(y: Any, conj: bool = False, terms: int | None = None) -> Any:
    """theta_chi(y) = sum_{n>=1} n chi(n) exp(-pi n^2 y / q)  (odd character, weight 3/2)."""
    if terms is None:
        terms = int(mp.sqrt(Q * (mp.mp.dps + 6) * mp.log(10) / (mp.pi * y))) + 3
    total = mp.mpc(0)
    for n in range(1, terms + 1):
        c = chi(n)
        if c == 0:
            continue
        cc = C(c.real, -c.imag if conj else c.imag)
        total += n * cc * mp.exp(-mp.pi * n * n * y / Q)
    return total


def phi(t: Any) -> Any:
    """Even theta-type kernel with F(z) = int_R phi(t) e^{zt} dt.

    Lambda(s) = int_0^inf theta_f(y) y^{(s+1)/2} dy/y with s = 1/2 + z and
    y = e^{2t} gives phi(t) = 2 e^{3t/2} theta_f(e^{2t}).
    """
    a, b = weights()
    y = mp.exp(2 * t)
    th = a * theta_twisted(y) + b * theta_twisted(y, conj=True)
    val = 2 * mp.exp(3 * t / 2) * th
    assert abs(mp.im(val)) < mp.mpf(10) ** (-mp.mp.dps + 5), "phi is not real"
    return mp.re(val)


def check_evenness(points=(-1.5, -0.7, -0.2, 0.3, 1.1)) -> dict:
    """phi(-t) == phi(t) and Lambda(s) == Lambda(1-s): the modular/functional-equation input."""
    rows = []
    for t in points:
        t = mp.mpf(t)
        rows.append({"t": float(t), "phi(t)": mp.nstr(phi(t), 20),
                     "phi(-t)": mp.nstr(phi(-t), 20),
                     "abs_diff": mp.nstr(abs(phi(t) - phi(-t)), 5)})
    s_pts = [C('0.3', '7.1'), C('0.9', '40.2'), C('1.6', '85.7')]
    fe = [{"s": str(s), "abs(Lambda(s)-Lambda(1-s))": mp.nstr(abs(Lambda(s) - Lambda(1 - s)), 5),
           "abs(Lambda(s))": mp.nstr(abs(Lambda(s)), 5)} for s in s_pts]
    return {"phi_even": rows, "functional_equation": fe}


GUESS = ("0.808517", "85.699348")


def check_offline_zero(guess: Any = None) -> dict:
    """Locate a zero of f with Re s != 1/2 by Newton from a literature-neighbourhood guess.

    Reported values (Spira 1994; Bombieri-Hejhal 1995) place a zero near
    0.8085 + 85.699 i. This is a floating-point root, validated by residual
    and by a winding-number count on a small box; it is not a certificate.
    """
    rho = mp.findroot(f, C(*GUESS) if guess is None else guess)
    # winding number of f around a box of half-width 0.05 centred at rho
    h = mp.mpf("0.05")
    corners = [rho + h * c for c in (C(1, 1), C(-1, 1), C(-1, -1), C(1, -1))]
    total = mp.mpc(0)
    for a, b in zip(corners, corners[1:] + corners[:1]):
        total += mp.quad(lambda u: mp.diff(f, u) / f(u), [a, b])
    winding = total / (2 * I * mp.pi)
    return {"rho": str(rho), "re_rho_minus_half": mp.nstr(mp.re(rho) - mp.mpf(1) / 2, 8),
            "abs_f(rho)": mp.nstr(abs(f(rho)), 5), "winding_number_box_0.05": mp.nstr(winding, 8)}


def check_lagarias_failure(rho: Any = None) -> dict:
    """Re(F'(z) conj F(z)) < 0 somewhere in Re z > 0.

    For xi this quantity is positive throughout Re z > 0 iff RH (Lagarias 1999),
    and equals 8 * int p sinh(2xp) A_p(y) dp in NS100's formula (1). Here the same
    weighted theta integral takes both signs, so no identity using only the
    kernel's evenness, decay and modular completion can force its sign.
    """
    if rho is None:
        rho = mp.findroot(f, C(*GUESS))
    z0 = rho - mp.mpf(1) / 2  # zero of F in Re z > 0
    samples = []
    for dz in (C("0.02"), C("-0.02"), C(0, "0.02"), C(0, "-0.02")):
        z = z0 + dz
        val = mp.re(mp.diff(F, z) * mp.conj(F(z)))
        samples.append({"z": str(z), "Re(F' conj F)": mp.nstr(val, 8)})
    negative = [s for s in samples if mp.mpf(s["Re(F' conj F)"]) < 0]
    return {"z0": str(z0), "samples": samples, "negative_found": bool(negative)}


def screen(candidate: Callable[[Callable, Callable], bool], name: str = "candidate") -> dict:
    """Run a caller-supplied predicate candidate(F, phi) on the Davenport-Heilbronn pair.

    Returns {"holds_on_known_false_analogue": bool}. True means the candidate
    cannot imply RH as stated.
    """
    return {"name": name, "holds_on_known_false_analogue": bool(candidate(F, phi))}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=30)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    mp.mp.dps = args.dps
    out = {"classification": "diagnostic control, floating point, not a certificate",
           "evenness": check_evenness()}
    z = check_offline_zero()
    out["offline_zero"] = z
    out["lagarias_failure"] = check_lagarias_failure(mp.mpmathify(z["rho"]))
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(text + "\n")


if __name__ == "__main__":
    main()
