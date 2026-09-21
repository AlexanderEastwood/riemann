"""Scalar consequences of the existing exact N=64 inverse certificate.

The computations establish only the numerical constants. Ground overlap
additionally requires the complete parity-resolved spectral certificates.
"""
import json
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx

BASE = Path(__file__).resolve().parent
ctx.prec = 256

def exact_decimal(text):
    q = Fraction(text)
    return arb(q.numerator) / q.denominator

old = json.loads((BASE / "g2_finite_certificate.json").read_text())
alpha = arb(old["alpha"])
energy = arb(old["schur_energy"])
q = arb(old["q"])
alpha_cap = exact_decimal("5.312382e-38")
energy_floor = exact_decimal("1.668982e-38")
q_cap = exact_decimal(".000216")
assert alpha < alpha_cap and energy > energy_floor and q < q_cap

# The exact finite-supported trial (u-z)/sqrt(1+||z||^2) has Rayleigh
# alpha-E/(1+||z||^2). Monotonicity gives this conservative upper bound.
beta_upper = alpha_cap - energy_floor / (1 + q_cap**2)
beta_cap = exact_decimal("3.644e-38")
assert 0 < beta_upper < beta_cap
rows = []
for threshold, promised in [("1e-36", ".19112"), ("1e-34", ".01931")]:
    a = exact_decimal(threshold)
    sine_upper = q_cap + (beta_cap / a).sqrt()
    assert sine_upper < exact_decimal(promised)
    rows.append(dict(even_sector_threshold=threshold,
                     sine_upper=sine_upper.str(65),
                     conservative_claim=promised))

result = dict(
    status="PASS: exact-input scalar interval inequalities",
    scope="Overlap statements require a proved complete even-sector gap and an odd-sector lower threshold above the trial Rayleigh value; no endpoint statement.",
    prior_certificate="g2_finite_certificate.json",
    candidate_sha256=old["candidate_sha256"],
    precision_bits=ctx.prec,
    alpha_upper="5.312382e-38",
    energy_lower="1.668982e-38",
    finite_inverse_norm_upper=".000216",
    improved_trial_rayleigh_upper=beta_upper.str(65),
    conservative_trial_rayleigh_cap="3.644e-38",
    conditional_ground_overlap=rows)
(BASE / "ground_overlap_scalar_certificate.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
