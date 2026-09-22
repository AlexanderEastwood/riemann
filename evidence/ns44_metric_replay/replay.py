"""Fresh dyadic counterwitnesses to the existing lambda=5, Q16, 1e-8 D metric.

Proposal uses binary64 only. Verification rebuilds every coefficient in Arb,
checks strict interval gates at 320/448 bits, and independently expands signed
Fourier indices. This is new evidence, not recovery of absent v1.27 originals.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
import numpy as np
from scipy.linalg import eigh
from flint import arb, arb_mat, ctx

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "evidence/v124/g2_schur_cancellation"))
import assembly_general as assembly

OUT = Path(__file__).resolve().parent
ROWS = list(range(17, 129))
SHIFT_DENOMINATOR = 100_000_000
FREEZE_BITS = 60


def fresh_sequences(bits: int) -> tuple[Any, Any, Any, Any]:
    """Force a fresh analytic Arb assembly, bypassing all preexisting caches."""
    with tempfile.TemporaryDirectory(prefix="ns44-coeff-") as scratch:
        previous = assembly.B
        try:
            assembly.B = Path(scratch)
            length, bs, ds, diagonal = assembly.sequences(5, 128, bits, K=96)
            return length, bs, ds, diagonal
        finally:
            assembly.B = previous


def propose() -> None:
    """Freeze common-denominator dyadics; no proposal number proves a gate."""
    _, bs, ds, diagonal = fresh_sequences(192)
    metric = np.array([float(diagonal[n].mid()) for n in ROWS])
    records: dict[str, Any] = {}
    for parity in ("even", "odd"):
        ball_matrix = assembly.block(ROWS, ROWS, parity, bs, ds)
        midpoint = np.array([[float(ball_matrix[i,j].mid()) for j in range(len(ROWS))]
                             for i in range(len(ROWS))])
        scaled = midpoint / np.sqrt(metric[:,None] * metric[None,:])
        _, vectors = eigh(scaled)
        vector = vectors[:,0] / np.sqrt(metric)
        vector /= np.linalg.norm(vector)
        integers = [int(round(float(x) * 2**FREEZE_BITS)) for x in vector]
        records[parity] = {"indices": ROWS, "numerators": integers,
                           "denominator_power_of_two": FREEZE_BITS}
    path = OUT / "witnesses.json"
    if path.exists():
        raise RuntimeError("Frozen witnesses already exist; use --verify to replay them")
    path.write_text(json.dumps({"lambda": 5, "tail_start": 16,
        "shift": "1/100000000", "classification": "exact dyadic proposals; not sign evidence by themselves",
        "parities": records}, indent=2)+"\n")


def signed_pairing(integers: list[int], exponent: int, parity: str,
                   bs: Any, ds: Any) -> Any:
    """Separate signed-index quadratic assembly with explicit +/- n coordinates."""
    sign = 1 if parity == "even" else -1
    indices = ROWS + [-n for n in ROWS]
    positive = [arb(x) / (arb(2)**exponent * arb(2).sqrt()) for x in integers]
    coordinates = positive + [sign*x for x in positive]
    total = arb(0)
    for i,n in enumerate(indices):
        total += coordinates[i]**2 * ds[abs(n)]
        bn = bs[abs(n)] if n > 0 else -bs[abs(n)]
        for j in range(i):
            m = indices[j]
            bm = bs[abs(m)] if m > 0 else -bs[abs(m)]
            total += 2*coordinates[i]*coordinates[j]*(bn-bm)/(n-m)
    return total


def verify() -> None:
    """No midpoint solve/eigenvalue enters this complete finite-support proof."""
    if not __debug__:
        raise RuntimeError("Do not disable the interval proof gates with Python -O.")
    witness_path = OUT / "witnesses.json"
    document = json.loads(witness_path.read_text())
    assert document["lambda"] == 5 and document["tail_start"] == 16
    assert document["shift"] == "1/100000000"
    assert set(document["parities"]) == {"even", "odd"}
    results: list[dict[str, Any]] = []
    for bits in (320, 448):
        _, bs, ds, diagonal = fresh_sequences(bits)
        assert all(diagonal[n] > 0 for n in ROWS)
        for parity, record in document["parities"].items():
            assert record["indices"] == ROWS
            integers = record["numerators"]
            exponent = record["denominator_power_of_two"]
            vector = arb_mat([[arb(n) / arb(2)**exponent] for n in integers])
            w = assembly.block(ROWS, ROWS, parity, bs, ds)
            numerator = (vector.transpose()*w*vector)[0,0]
            denominator = sum((vector[i,0]**2*diagonal[n] for i,n in enumerate(ROWS)),arb(0))
            norm2 = sum((vector[i,0]**2 for i in range(len(ROWS))),arb(0))
            shifted = numerator-denominator/SHIFT_DENOMINATOR
            signed = signed_pairing(integers, exponent, parity, bs, ds)
            agreement = numerator-signed
            ratio = numerator/denominator
            assert norm2 > 0 and denominator > 0
            assert numerator > 0, "Unexpected nonpositive Weil numerator; investigate before any claim"
            assert shifted < 0 and ratio < arb(1)/SHIFT_DENOMINATOR
            assert signed > 0 and signed-denominator/SHIFT_DENOMINATOR < 0
            assert agreement.contains(0)
            digits = int(bits*.30103)-10
            item = {"bits":bits,"parity":parity,"norm2":norm2.str(digits),
                "Weil_numerator":numerator.str(digits),"D_denominator":denominator.str(digits),
                "ratio_q_over_D":ratio.str(digits),"q_minus_1e8_inverse_D":shifted.str(digits),
                "signed_index_numerator":signed.str(digits),"assembly_difference":agreement.str(digits),
                "gates":{"norm_positive":True,"D_positive":True,"q_positive":True,
                         "shifted_q_strictly_negative":True,"signed_shifted_q_strictly_negative":True,
                         "assemblies_overlap":True}}
            results.append(item)
            print(bits,parity,"q/D",ratio.str(14),"q-1e-8D",shifted.str(14),flush=True)
    sources = ["evidence/v124/g2_schur_cancellation/assembly_general.py",
               "evidence/ns44_metric_replay/replay.py"]
    out = {"classification":"CERTIFIED COMPUTATION: strict interval gates at two precisions",
           "scope":"lambda=5, both parity tails 17..128; failure of the stipulated 1e-8 D lower comparison only",
           "not_original_recovery":True,"witness_sha256":hashlib.sha256(witness_path.read_bytes()).hexdigest(),
           "source_sha256":{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
           "analytic_series_terms":96,"fresh_assembly":True,"results":results}
    (OUT/"certificate.json").write_text(json.dumps(out,indent=2)+"\n")


def main() -> None:
    if not __debug__:
        raise RuntimeError("Do not disable the interval proof gates with Python -O.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--propose", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.propose:
        propose()
    if args.verify:
        verify()
    if not args.propose and not args.verify:
        parser.error("choose --propose and/or --verify")


if __name__ == "__main__":
    main()
