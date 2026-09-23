"""Independent full physical upper bounds for exact rational trial vectors."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx


def evaluate(strings: list[str], stop: int) -> dict[str, str]:
    rational_coefficients = [Fraction(s) for s in strings]
    assert sum((c/n for n,c in enumerate(rational_coefficients,1)),Fraction(0)) == 0
    coefficients = [arb(c.numerator)/c.denominator for c in rational_coefficients]
    assert stop > len(coefficients)
    logs = [arb(0)]+[arb(m).log() for m in range(1,stop+1)]
    defects = [arb(0) for _ in range(stop)]
    defects[1] = arb(1)
    for n,c in enumerate(coefficients,1):
        for m in range(n,stop,n):
            defects[m] += c
    running, weighted, head = arb(0), arb(0), arb(0)
    for m in range(1,stop):
        a,b = logs[m],logs[m+1]
        running += defects[m]
        weighted += defects[m]*a
        i0 = arb(1)/(m*(m+1))
        i1 = (a+1)/m-(b+1)/(m+1)
        i2 = (a*a+2*a+2)/m-(b*b+2*b+2)/(m+1)
        cell = running**2*i2-2*running*weighted*i1+weighted**2*i0
        assert not cell < 0
        head += cell
    u = 1-sum(coefficients,arb(0))/2
    v = sum((c*(logs[n]-(2*arb.pi()).log()) for n,c in enumerate(coefficients,1)),arb(0))/2
    d = sum((n*abs(c) for n,c in enumerate(coefficients,1)),arb(0))/6
    q = u*logs[stop]+v
    main_tail = (q*q+2*u*q+2*u*u)/stop
    remainder = d*d/(3*arb(stop)**3)
    radius = 2*(main_tail*remainder).sqrt()+remainder
    upper = head+main_tail+radius
    enclosure = head+main_tail+arb(0,radius)
    return {k:x.str(65) for k,x in {
        "head_energy":head,"main_tail":main_tail,"tail_radius":radius,
        "complete_energy_enclosure":enclosure,"complete_upper_certificate":upper,
        "tail_slope":u,"tail_constant":v,"remainder_constant":d}.items()}


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--bits",type=int,required=True)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--stop",type=int,default=262144)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    source=json.loads(args.input.read_text());rows:list[dict[str,Any]]=[]
    for row in source["rows"]:
        values=evaluate(row["rational_coefficients"],args.stop)
        gram=arb(row["values"]["explicit_trial_error"])
        assert arb(values["complete_energy_enclosure"]).overlaps(gram)
        assert gram < arb(values["complete_upper_certificate"])
        rows.append({"N":row["N"],"values":values})
        print(json.dumps({"N":row["N"],"upper":values["complete_upper_certificate"],
                          "tail_radius":values["tail_radius"]}),flush=True)
    args.output.write_text(json.dumps({"classification":"Complete physical upper certificates; exact rational zero exterior, signed interior and full remote tail retained",
        "precision_bits":args.bits,"physical_stop":args.stop,
        "input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "rows":rows},indent=2)+"\n")


if __name__ == "__main__":
    main()
