# Controls for pre-registration

**Diagnostics, not certificates.** These tools screen an actual candidate
before proof, certification or a wider scan. Running the unchanged example
only tests that example. A sampled pass is not universal validity; a sampled
failure is a reason to pause and investigate, not a proved route closure.

A control refutes a proposed general implication only if **all** premises,
normalizations and quantifiers match. If the entire candidate condition is
established on an applicable function with off-axis zeros, that condition
alone cannot force critical-line zeros. Record unmatched hypotheses, not
just the name of a function or the presence of a functional equation.

| Control | Shared structure | Scope limitations |
|---|---|---|
| Davenport-Heilbronn | Even completed function; real even theta-type kernel; double-exponential decay; off-line zeros | Odd-character conductor-5 completion and weight-3/2 theta relation, not Riemann's exact coefficients or gamma factor |
| NS100 log-concave order-2 | Positive even smooth strongly log-concave kernel | Order two; not all original arithmetic hypotheses |
| NS101 reciprocal dilation | Positive Gaussian mixture, reciprocity, order one | Original one-lattice coefficients changed; not every modular law or log-concavity |

## Run the diagnostics

```
.venv/bin/python controls/davenport_heilbronn.py --dps 25
.venv/bin/python controls/example_screen.py
.venv/bin/python -m unittest controls.test_controls
```

The main script compares the **raw** kernel formulas at moderate positive
and negative arguments, evaluates the functional equation at several
points, locates an off-line zero and computes a diagnostic contour count,
and samples the horizontal-growth expression nearby. These are floating
point results. The saved `davenport_heilbronn_dps25.json` remains the
original replay and is not overwritten by the correction.

For candidates, import `F`, `phi`, and `screen`. Supply `name`,
`sample_domain`, `applicability`, and observations (values or residuals).
The callback returns True, False or None. Outputs are `sampled-pass`,
`sampled-failure`, `inconclusive`, or `not-applicable`; no automatic output
is a proved obstruction. Example:

```python
from controls.davenport_heilbronn import screen
result = screen(lambda F, phi: phi(3) > 0, "one kernel value",
                sample_domain="t=3", applicability="real kernel value only")
```

The public `phi(t)` requires real t and uses the analytic reflection
identity to evaluate on t>=0, avoiding catastrophic cancellation in the
negative tail. `phi_raw` is retained only for independent moderate-range
reciprocity diagnostics. Do not use raw negative-tail values as evidence.
`F_xi(z)=xi(1/2+z)/2` reflects to Re(s)>=1/2 and handles s=0,1 by continuation.
It also avoids the canceled gamma poles at negative even integers.

Normalization:
`Lambda(s)=(5/pi)^((s+1)/2) Gamma((s+1)/2) f(s)` and
`F(z)=Lambda(1/2+z)=int_R phi(t) exp(zt) dt`.
The raw kernel is `2 exp(3t/2) theta_f(exp(2t))`, where
`theta_chi(y)=sum n chi(n) exp(-pi*n*n*y/5)`, chi(2)=i,
`theta_f=a*theta_chi+b*theta_chibar`, and
`a,b=(1-/+i*kappa)/2`,
`kappa=(sqrt(10-2sqrt(5))-2)/(sqrt(5)-1)`.
The historical zero near 0.8085+85.699i is discussed by Spira (1994).
No new zero-location certificate is claimed here.
