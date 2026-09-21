#!/usr/bin/env python3
"""Independent principal-minor and exact-norm replay of the NS-5 gates.

This uses Arb's determinant implementation rather than certify_ground4.inertia
for the new shifted gates, and exact Fraction arithmetic for selected physical
column norms. The archived complete residual enclosures remain inherited inputs.
"""
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path

from flint import arb_mat, ctx

import certify_ground4 as certificate


BASE = Path(__file__).resolve().parent


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    result = {
        "scope": "Independent Arb principal determinants and exact Fraction "
                 "physical norms; archived complete residual bounds are reused.",
        "certificate_source_sha256": sha256(BASE / "certify_ground4.py"),
        "checker_source_sha256": sha256(Path(__file__)),
        "shift": "1e-73",
        "checks": [],
    }
    for bits in (1024, 1280):
        ctx.prec = bits
        for parity, kappa in (("even", "62629/100000"), ("odd", "428/1000")):
            data, matrices, G, V, Z, provenance = certificate.load_trial(parity, bits)
            certificate.replay_prior_gates(parity, data, matrices, bits)
            K = certificate.sym(matrices["K"])
            Hh, Ht = V.transpose() * V, Z.transpose() * Z
            H = Hh + Ht
            delta, shift = certificate.A("1.7940e-8"), certificate.A("1e-73")
            lower = certificate.sym(
                certificate.A(kappa) * K - shift * (
                    Hh + 2 / (1 - shift / delta) * (Ht + K / delta)
                )
            )

            # Distinct implementation from the bespoke signed LDL algorithm.
            minor_signs = []
            for n in range(1, K.nrows() + 1):
                minor = arb_mat([[lower[i, j] for j in range(n)]
                                 for i in range(n)]).det()
                expected_positive = parity == "odd" or n < K.nrows()
                assert (minor > 0) if expected_positive else (minor < 0)
                minor_signs.append(1 if expected_positive else -1)

            # Independently reconstruct the actual finite column with rationals.
            witness_path = certificate.ROOT / provenance["witness"]
            witness = json.loads(gzip.decompress(witness_path.read_bytes()))
            column = 16 if parity == "even" else 15
            offset = 0 if parity == "even" else 1
            coefficients = [certificate.dyadic_fraction(x)
                            for x in witness["base_columns"][column]]
            coefficients += [Fraction(0)] * (4096 - 256)
            for i, dyadic in enumerate(witness["dyadic_columns"][column]):
                coefficients[17 - offset + i] -= certificate.dyadic_fraction(dyadic)
            norm_squared = sum((x * x for x in coefficients), Fraction(0))
            assert H[column, column].contains(certificate.A(norm_squared))
            rayleigh = K[column, column] / certificate.A(norm_squared)
            upper = "2.454e-75" if parity == "even" else "1e-70"
            assert rayleigh < certificate.A(upper)
            norm_record = f"{norm_squared.numerator}/{norm_squared.denominator}"
            check = {
                "precision_bits": bits,
                "parity": parity,
                "leading_principal_minor_signs": minor_signs,
                "prior_small_gates_replayed": True,
                "trial_column": column,
                "exact_fraction_norm_enclosed": True,
                "exact_fraction_norm_sha256": hashlib.sha256(
                    norm_record.encode("ascii")).hexdigest(),
                "trial_rayleigh": rayleigh.str(70),
                "proved_trial_upper": upper,
                "provenance": provenance,
            }
            result["checks"].append(check)
            print(bits, parity, "principal minors", minor_signs,
                  "exact norm enclosed; Rayleigh", rayleigh.str(30), flush=True)
    result["status"] = "PASS_INDEPENDENT_CHECKS"
    output = BASE / "independent_checks.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(result["status"], flush=True)
    return result


if __name__ == "__main__":
    run()
