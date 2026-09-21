"""Certified finite-compression CCM benchmark at the EXISTING lambda=3 window.

Arb assembles the matrix; acb_mat.eig isolates eigenpairs. Midpoint root finding
only proposes brackets, accepted exclusively by interval signs and derivatives.
This is not a certificate for complete-ground zero locations or convergence.
"""
from __future__ import annotations

import argparse
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import time
from typing import Any

from flint import acb, acb_mat, arb, ctx
import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
ASSEMBLY = ROOT / "evidence/v124/g2_schur_cancellation/assembly_general.py"
PUBLISHED = ["1.6e-34", "2.1e-31", "1.5e-29", "8.3e-27", "1.3e-25", "1.2e-23", "7.5e-22", "6.6e-21"]
N = 120
K = 128


def load_assembly(cache: Path) -> Any:
    spec = importlib.util.spec_from_file_location("original_assembly", ASSEMBLY)
    assert spec is not None and spec.loader is not None
    module: Any = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.B = cache
    return module


def rational(z: arb, v: list[arb], omega: list[arb]) -> arb:
    return v[0] / z + arb(2).sqrt() * sum(
        (v[n] * z / (z*z - omega[n]*omega[n]) for n in range(1, len(v))), arb(0)
    )


def derivative(z: arb, v: list[arb], omega: list[arb]) -> arb:
    return -v[0] / (z*z) - arb(2).sqrt() * sum(
        (v[n] * (z*z + omega[n]*omega[n]) / (z*z - omega[n]*omega[n])**2
         for n in range(1, len(v))), arb(0)
    )


def centered_transform(z: arb, length: arb, v: list[arb]) -> arb:
    """Direct termwise integral; the (-1)^n translation is mandatory."""
    value = 2*v[0]/length.sqrt() * (z*length/2).sin()/z
    for n in range(1, len(v)):
        w = 2*arb.pi()*n/length
        value += (2/length).sqrt()*((-1)**n)*v[n]*(
            ((w-z)*length/2).sin()/(w-z) + ((w+z)*length/2).sin()/(w+z)
        )
    return value


def mp_proposal(gamma: arb, length: arb, v: list[arb]) -> str:
    """An uncertified proposal; never used as an acceptance test."""
    length_mp = mp.mpf(length.mid().str(190, radius=False))
    vector = [mp.mpf(x.mid().str(190, radius=False)) for x in v]
    omega = [2*mp.pi*n/length_mp for n in range(len(v))]
    def fun(z: Any) -> Any:
        return vector[0]/z + mp.sqrt(2)*sum(
            vector[n]*z/(z*z-omega[n]**2) for n in range(1, len(v))
        )
    g = mp.mpf(gamma.mid().str(190, radius=False))
    root = mp.findroot(fun, (g-mp.mpf("0.001"),g+mp.mpf("0.001")), tol=mp.mpf("1e-165"))
    return mp.nstr(root, 160)


def run(bits: int) -> dict[str, Any]:
    ctx.prec = bits
    mp.mp.dps = 190
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="ns2-assembly-") as folder:
        asm = load_assembly(Path(folder))
        length, b, d, _ = asm.sequences(3, N, bits, K)
        even = asm.block(list(range(N+1)), list(range(N+1)), "even", b, d)
        odd = asm.block(list(range(1,N+1)), list(range(1,N+1)), "odd", b, d)
    eigenvalues, eigenvectors = acb_mat(even).eig(right=True, algorithm="rump")
    ground_index = min(range(len(eigenvalues)), key=lambda k: float(eigenvalues[k].real.mid()))
    ground = eigenvalues[ground_index]
    assert ground.imag.contains(0)
    assert all(ground.real < e.real for k,e in enumerate(eigenvalues) if k != ground_index)
    odd_values = acb_mat(odd).eig(algorithm="rump")
    assert all(ground.real < e.real for e in odd_values)
    v = [(eigenvectors[k,ground_index]/eigenvectors[0,ground_index]).real for k in range(N+1)]
    assert v[0].contains(1)
    v[0] = arb(1)
    omega = [2*arb.pi()*n/length for n in range(N+1)]
    identity_checks = []
    for z in map(arb, ["0.7", "6.2", "13.1", "23.3"]):
        direct = centered_transform(z, length, v)
        partial_fractions = 2/length.sqrt()*(z*length/2).sin()*rational(z,v,omega)
        delta = direct - partial_fractions
        assert delta.contains(0)
        identity_checks.append({"z":str(z),"difference":delta.str(12)})
    roots = []
    for k, published in enumerate(PUBLISHED,1):
        gamma = acb.zeta_zero(k).imag
        center = mp_proposal(gamma,length,v)
        bracket = arb(center,"1e-110")
        left = arb(center)-arb("1e-110")
        right = arb(center)+arb("1e-110")
        fleft, fright = rational(left,v,omega), rational(right,v,omega)
        deriv = derivative(bracket,v,omega)
        assert fleft*fright < 0
        assert not deriv.contains(0)
        assert not (bracket*length/2).sin().contains(0)
        discrepancy = bracket-gamma
        pub = Decimal(published)
        exponent = pub.as_tuple().exponent
        assert isinstance(exponent, int)
        half_unit = Decimal(10)**exponent / 2
        assert discrepancy > arb(str(pub-half_unit))
        assert discrepancy < arb(str(pub+half_unit))
        roots.append({"zeta_index":k,"published_rounded_discrepancy":published,
                      "center_decimal":center,"radius_decimal":"1e-110",
                      "root_bracket":bracket.str(145, more=True),"zeta_ordinate":gamma.str(145),
                      "discrepancy":discrepancy.str(100),
                      "left_sign":1 if fleft>0 else -1,"right_sign":1 if fright>0 else -1,
                      "derivative":deriv.str(15),"matches_published_rounding":True})
    lattice = {str(k):((length/2).sqrt()*((-1)**k)*v[k]).str(45) for k in range(1,9)}
    assert all(not arb(value).contains(0) for value in lattice.values())
    return {"classification":"certified computation for a finite compression only",
            "lambda":3,"N":N,"K":K,"bits":bits,"L":length.str(145),
            "source":"https://arxiv.org/html/2511.22755v1#S6",
            "figure":"https://arxiv.org/html/2511.22755v1/lambda3.svg",
            "assembly_sha256":hashlib.sha256(ASSEMBLY.read_bytes()).hexdigest(),
            "ground":ground.real.str(120),"simple_even_global_finite_ground":True,
            "normalized_unshifted_even_coefficients":[x.str(145) for x in v],
            "transform_identity_checks":identity_checks,"roots":roots,
            "transform_at_first_eight_lattice_points":lattice,
            "scope":"Unique local roots near the first eight zeta ordinates; no claim of complete-ground transfer, exhaustive root enumeration, cofinal convergence, G2 or RH.",
            "elapsed_seconds":round(time.monotonic()-start,3)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits",type=int,choices=[768,1024],required=True)
    args = parser.parse_args()
    result = run(args.bits)
    target = OUT/f"ccm_lambda3_N120_b{args.bits}.json"
    target.write_text(json.dumps(result,indent=2)+"\n")
    print(target.name,"all interval gates passed",result["elapsed_seconds"],"s",flush=True)
    for row in result["roots"]:
        print(row["zeta_index"],row["discrepancy"],flush=True)

if __name__ == "__main__":
    main()
