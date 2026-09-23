"""Worked example of the control screen (diagnostic, not a certificate).

Candidate: "Re(F'(z) conj F(z)) >= 0 on a small sample in Re z > 0".
For xi this is a Lagarias-criterion sample and is expected to hold under RH.
For the Davenport-Heilbronn pair it fails. A candidate that held on BOTH
would be useless as an RH mechanism; this one at least discriminates.

    .venv/bin/python controls/example_screen.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from controls.davenport_heilbronn import C, F, F_xi, GUESS, f  # noqa: E402


def sample_min(Fun, z0) -> mp.mpf:
    vals = []
    for dz in (C("0.02"), C("-0.02"), C(0, "0.02"), C(0, "-0.02")):
        z = z0 + dz
        vals.append(mp.re(mp.diff(Fun, z) * mp.conj(Fun(z))))
    return min(vals)


def main() -> None:
    mp.mp.dps = 20
    rho = mp.findroot(f, C(*GUESS))
    z0 = rho - mp.mpf(1) / 2
    out = {
        "candidate": "Re(F' conj F) >= 0 at four points around z0, Re z0 > 0",
        "z0": str(z0),
        "xi": {"min_sample": mp.nstr(sample_min(F_xi, z0), 6)},
        "davenport_heilbronn": {"min_sample": mp.nstr(sample_min(F, z0), 6)},
    }
    out["xi"]["holds"] = mp.mpf(out["xi"]["min_sample"]) >= 0
    out["davenport_heilbronn"]["holds"] = mp.mpf(out["davenport_heilbronn"]["min_sample"]) >= 0
    out["verdict"] = ("discriminates: fails on the known-false analogue"
                      if out["xi"]["holds"] and not out["davenport_heilbronn"]["holds"]
                      else "does not discriminate or fails on xi; stop or add a hypothesis")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
