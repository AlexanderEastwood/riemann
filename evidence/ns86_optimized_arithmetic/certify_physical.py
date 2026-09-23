"""Independent physical norms and complete arithmetic-potential checks.

Input coefficients remain interval enclosures. Every infinite tail is bounded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
KERNEL_PATH = HERE.parent / "v159/ns61/certify_smoothed.py"
sys.path.insert(0, str(KERNEL_PATH.parent))
from certify_smoothed import Kernel
from certify_newton import defects


def evaluate(coefficients: list[arb], split: int, stop: int, kernel: Kernel,
             potential: bool) -> dict[str, Any]:
    n = len(coefficients)
    assert stop > max(n, split)
    logs = [arb(0)] + [arb(k).log() for k in range(1, stop + 1)]
    eta = sum((c / k for k, c in enumerate(coefficients, 1)), arb(0))
    total = sum(coefficients, arb(0))
    slope = 1 - total / 2
    constant = sum((c * (logs[k] - (2 * arb.pi()).log())
                    for k, c in enumerate(coefficients, 1)), arb(0)) / 2
    remainder = sum((k * abs(c) for k, c in enumerate(coefficients, 1)), arb(0)) / 6
    delta = defects(coefficients, stop - 1)
    running, logarithmic = arb(0), arb(0)
    interior, remote = arb(0), arb(0)
    # Three complete-cell linear integrals: r/t^2, r log(t)/t^2, and r/t.
    j0, j1 = [arb(0)], [arb(0)]
    first_moment = -eta
    for m in range(1, stop):
        a, b = logs[m], logs[m + 1]
        running += delta[m]
        logarithmic += delta[m] * a
        weight = arb(1) / (m * (m + 1))
        i1 = (a + 1) / m - (b + 1) / (m + 1)
        i2 = (a*a + 2*a + 2) / m - (b*b + 2*b + 2) / (m + 1)
        cell = eta**2 + running**2 * i2 + logarithmic**2 * weight
        cell -= eta * running * (b*b - a*a)
        cell += 2 * eta * logarithmic * (b-a) - 2 * running * logarithmic * i1
        assert not cell < 0
        if m < split:
            interior += cell
        else:
            remote += cell
        if potential:
            j0.append(-eta*(b-a) + running*i1 - logarithmic*weight)
            j1.append(-eta*(b*b-a*a)/2 + running*i2 - logarithmic*i1)
            first_moment += -eta + running*(b*b-a*a)/2 - logarithmic*(b-a)
    q = slope * logs[stop] + constant
    main_tail = (q*q + 2*slope*q + 2*slope*slope) / stop
    remainder_energy = remainder**2 / (3 * arb(stop)**3)
    radius = 2 * (main_tail * remainder_energy).sqrt() + remainder_energy
    remote += main_tail + arb(0, radius)
    energy = eta**2 + interior + remote
    assert energy > 0 and interior > 0 and remote > 0
    values = {"eta": eta, "exterior_energy": eta**2,
              "interior_energy_1_to_split": interior,
              "complete_energy_after_split": remote,
              "complete_energy": energy, "physical_tail_radius": radius,
              "tail_slope": slope, "tail_constant": constant,
              "Stirling_remainder_constant": remainder}
    observations: dict[str, Any] = {}
    if potential:
        # P(t)=int_t^infinity log(u/t) r(u) du/u^2, A(t)=int_t^infinity r(u) du/u^2.
        # Coupled tail errors are bounded separately; no cancellation of radii is assumed.
        a_tail = (q+slope)/stop + arb(0, remainder/(2*arb(stop)**2))
        log_moment_tail = ((q+slope)*logs[stop] + q + 2*slope)/stop
        log_moment_tail += arb(0, remainder*(logs[stop]/2+arb(1)/4)/arb(stop)**2)
        acc0, acc1 = arb(0), arb(0)
        samples = [arb(0) for _ in range(stop + 1)]
        for m in range(stop - 1, 0, -1):
            acc0 += j0[m]
            acc1 += j1[m]
            samples[m] = acc1 - logs[m] * acc0
        values["P_at_one"] = samples[1] + log_moment_tail
        values["P_at_one_minus_energy"] = values["P_at_one"] - energy
        assert values["P_at_one"].overlaps(energy)
        for mesh in [1, 2, 4, 8, 16, 32, 64, 256]:
            if stop % mesh:
                continue
            k = stop // mesh
            logk = logs[k]
            # The shared tail log-moment cancels exactly before interval evaluation.
            boundary_coefficient = k*(1-logk) + arb(k+1).lgamma()
            finite_quadrature = first_moment / mesh - sum(
                (samples[j] for j in range(mesh, stop + 1, mesh)), arb(0))
            finite_quadrature += boundary_coefficient * a_tail
            harmonic = sum((arb(1)/j for j in range(1, k+1)), arb(0))
            log_harmonic = sum((logs[j]/j for j in range(1, k+1)), arb(0))
            b = slope * logs[mesh] + 2*slope + constant
            main_quadrature_tail = (slope*(-kernel.gamma1-logk*logk/2+log_harmonic)
                                    + b*(harmonic-kernel.gamma-logk))/mesh
            complete_quadrature = finite_quadrature + main_quadrature_tail
            complete_quadrature += arb(0, remainder/(4*arb(stop)**2))
            direct = kernel.load(mesh) - sum(
                (c*kernel.gram(j, mesh) for j, c in enumerate(coefficients, 1)), arb(0))
            assert complete_quadrature.overlaps(direct), (n, mesh, finite_quadrature,
                                                         main_quadrature_tail, direct,
                                                         complete_quadrature)
            if mesh <= n:
                assert direct.contains(0)
            assert abs(direct-finite_quadrature) < 2*(energy/stop).sqrt()
            physical_tail_energy = main_tail + arb(0, radius)
            sharper_tail_bound = (physical_tail_energy/stop).sqrt() * (
                arb(1)/arb(2).sqrt() + arb(mesh)/(3*stop))
            assert abs(direct-finite_quadrature) < sharper_tail_bound
            observations[str(mesh)] = {
                "finite_quadrature": finite_quadrature.str(65),
                "analytic_main_tail": main_quadrature_tail.str(65),
                "complete_quadrature": complete_quadrature.str(65),
                "complete_Gram_pairing": direct.str(65),
                "universal_tail_bound": (2*(energy/stop).sqrt()).str(65),
                "physical_tail_observation_bound": sharper_tail_bound.str(65)}
    return {"values": {key: value.str(65) for key, value in values.items()},
            "potential_observations": observations}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--cell-stop", type=int, default=65536)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    source = json.loads(args.input.read_text())
    kernel = Kernel(256, source["kernel_cutoff"], 24)
    rows = []
    for row in source["rows"]:
        family = row["families"]["original"]
        output: dict[str, Any] = {"N": row["N"], "M": row["M"]}
        for label, field, comparison in [
            ("old", "old_coefficients", "E_N"),
            ("new", "proposed_coefficients", "unit_step_energy")]:
            coefficients = [arb(v) for v in family[field]]
            record = evaluate(coefficients, row["M"], args.cell_stop, kernel, label == "old")
            assert arb(record["values"]["complete_energy"]).overlaps(arb(family["values"][comparison]))
            output[label] = record
        rows.append(output)
        print(json.dumps({"N": row["N"], "bits": args.bits,
                          "old": output["old"]["values"], "new": output["new"]["values"]}), flush=True)
    result = {"classification": "independent complete physical-cell and arithmetic-potential certificates",
              "precision_bits": args.bits, "cell_stop": args.cell_stop,
              "input_file": args.input.name,
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "dependencies": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in [KERNEL_PATH, HERE/"certify_newton.py"]}, "rows": rows}
    args.output.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
