# controls/ — known-false analogues for screening proposals

**Diagnostics, not certificates.** Everything here is floating point and
exists to kill proposals cheaply, before a proof, an interval certificate or
a scan is attempted. Nothing here is cited as a bound.

Rule (AGENTS.md, "Proposal gate" and fact 3.5): a candidate inequality,
identity or positivity mechanism must be evaluated on these analogues first.
If it **holds** on a function that violates RH, it cannot imply RH as stated.
Record the outcome in the proposal template.

| Control | Shares with xi | Fails RH how | Where |
|---|---|---|---|
| Davenport-Heilbronn function (Titchmarsh 10.25) | functional equation even about 1/2, even theta-type kernel, double-exponential decay, modular completion, real on the critical line | zero near 0.8085 + 85.699i, winding number 1 in a 0.05 box | `davenport_heilbronn.py` |
| Log-concave order-2 kernel | positive, even, smooth, strongly log-concave kernel | Lagarias quantity negative at log 2 + i pi | `evidence/ns100_reassessment/argument.tex` |
| Reciprocal positive dilation | positive Gaussian mixtures, reciprocal identity, order one | explicit off-axis zeros in the strip | `evidence/ns101_theta_factorization/` |

## Davenport-Heilbronn

```
.venv/bin/python controls/davenport_heilbronn.py --dps 25 --output controls/davenport_heilbronn_dps25.json
```

Runs three checks (about a minute at 25 digits):

1. `phi(-t) == phi(t)` and `Lambda(s) == Lambda(1-s)`: the modular and
   functional-equation input is genuinely present.
2. An off-line zero of `f` from Newton iteration plus a winding-number
   count on a small box around it.
3. `Re(F'(z) conj F(z)) < 0` at a point with `Re z > 0`: the weighted theta
   integral of NS-100 formula (1) takes both signs here, so no identity that
   uses only the kernel's evenness, decay and modular completion can force
   its sign for xi.

To screen your own candidate, import the pair and evaluate it:

```python
from controls.davenport_heilbronn import F, phi, screen
screen(lambda F, phi: <bool: does the candidate hold for this F, phi?>, "my-candidate")
```

`holds_on_known_false_analogue: true` means stop or add a hypothesis.

Normalisation: `Lambda(s) = (5/pi)^((s+1)/2) Gamma((s+1)/2) f(s)`,
`F(z) = Lambda(1/2 + z) = int_R phi(t) e^{zt} dt`,
`phi(t) = 2 e^{3t/2} theta_f(e^{2t})` with
`theta_f(y) = a theta_chi(y) + b theta_chibar(y)`,
`theta_chi(y) = sum n chi(n) exp(-pi n^2 y/5)`, chi(2) = i, and
`a, b = (1 -/+ i kappa)/2`, `kappa = (sqrt(10 - 2 sqrt5) - 2)/(sqrt5 - 1)`.
The zero location agrees with Spira (1994) and Bombieri-Hejhal (1995).
