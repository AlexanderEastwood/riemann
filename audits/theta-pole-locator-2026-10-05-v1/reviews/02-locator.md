# Review 02 — fixed locator and matched controls

**Diagnostic only; no original evaluation by this worker.** Reviewed baseline
`bc3ff0c962c485ac8104ce8cd832c119c260c871` (PR79), AGENTS, this audit's BRIEF,
and PR79 reviews 03/06. The coordinator owns the full-register review. Both
historical original-evidence recovery groups remain OPEN.

**Wall check: Distinct test.** Closest PR78/79. This pipeline searches for an
original denominator zero with a potentially nonzero numerator in one fixed
box. A later complete uncancelled-pole certificate would reject the general
quotient-PD sufficient construction, beyond PR78's mixture obstruction. A
bounded diagnostic without a certificate rejects nothing. No signed original
Laguerre estimate, RH/G2 assertion, NS row, thaw, or manuscript version.

## Frozen protocol

Original box: `1/8 <= Re z <= 2`, `1/8 <= Im z <= 5/8`. Its selection is for
tractability, not a prediction of a root. Exactly one initial 9-by-9 vertex
grid at 128 bits; no larger or adjacent scan.

The evaluator returns `m=B*M`, `c=B*C`, `dm=(B*M)'`, where
`B=exp(2*pi*exp(2*z)-9*z)/(4*pi^4)` is entire and never zero. Numerator and
denominator use the same factor. This preserves zeros and quotient; the
analytic derivative includes `B'`. The coordinator/evaluator review owns the
complete lattice and real-tail error treatment. Raw quadrature and rounding
remain unbounded errors, so every locator result is diagnostic.

For each of 64 cells, enumerate four corner values counterclockwise. Define
`q=min(abs(m_corner))/max(abs(m_corner))`. Compute the sampled argument sum
`w=sum(arg(m_next/m_current))/(2*pi)` and round to the nearest integer. This
is **not** a boundary winding certificate; between-corner aliasing is possible.
If the maximum is zero, set `q=0`; if the minimum is at most
`2^(-working_bits/2)` times the maximum, record winding unresolved and use
rounded winding zero as a deterministic ranking fallback.

Rank by descending absolute rounded winding, ascending `q`, then ascending
x/y cell indices. Select at most the first four cells. Start each refinement
at its center. Use at most 12 evaluated Newton iterates per cell. Halve a
Newton step at most 16 times to keep it inside the **same** cell; if this
fails, stop that cell. Also stop on zero sampled derivative, roundoff
stagnation, or relative denominator residual below `2^-40`. Preserve all
failure/stopping labels. This rule can miss roots and does not authorize an
adjacent-cell search.

Replay the **same selected cells** at 256 bits with the evaluator's stronger
cutoffs/quadrature. Evaluate their unique corners afresh, recompute diagnostic
scales, and restart the same center refinement. Do not rerank or rescan the
original 81 vertices. Therefore the cap is 81 initial evaluations, 48 initial
local evaluations, at most 16 replay corners and 48 replay local evaluations:
at most 193 original evaluator calls.

An approximate-root label requires at both precisions:

```text
abs(m_endpoint)/max_corner_abs(m) < 2^-40
abs(z_128-z_256) <= 2^-32 * cell_diagonal.
```

The stronger label, **sampled numerator separation; certificate needed**, also
requires at both precisions:

```text
abs(c_endpoint)/max_corner_abs(c) > 2^-20
abs(c_128-c_256) <= 2^-32 * max(corner_C_scale_128, corner_C_scale_256).
```

These thresholds are reproducibility filters, not enclosures. Small C means
**numerator unresolved**, never proved cancellation. A stable nonzero C sample
does not prove C nonzero at an actual M root. Any root/pole theorem requires
the separately specified complete Arb certificate. A null result means
inconclusive, not zero-free, PD, or positive Laguerre.

Total discovery budget: 90 minutes including control/implementation time.
The original CLI takes the coordinator's remaining seconds, bounded above by
5400, and shares that remaining budget across grid, refinements and replay.
The clock is checked before each evaluator call; an already running call must
finish before the next guard. No enlargement after time exhaustion.

## Matched control execution

Both controls used the identical pipeline on `[0.7,0.72]+i[0.7,0.72]`:

```text
M0=z^4+1, C0=1;             actual uncancelled pole control
M1=z^4+1, C1=M1*exp(-z^2);  exact removable-zero control.
```

Each completed 154 evaluator calls including replay. Cell `(2,2)` contained
the stable approximate denominator root. The first control received the
sampled-numerator-separation label. The second received **numerator unresolved,
no pole claim** and was not falsely flagged as uncancelled. The endpoint
replay difference was approximately `3.33e-39`. Other selected cells stopped
without a stable approximate root. Complete records are in
`evidence/diag_theta_pole_locator/controls.json`.

This verifies a useful diagnostic distinction. It does not certify the
algorithm's completeness or transplant synthetic conclusions to theta. These
controls share holomorphic quotient/contour structure and denominator-zero
cancellation, but not the original arithmetic coefficients. NS101 shares
quotient algebra, not original theta coefficients; its known negative
Laguerre value does not force a pole. NS100 tests per-slice positivity, not
the complete quotient. DH has different coefficients, completion and strip;
the unchanged example screen does not test this locator. NS74/83 concern NB
loads/rates and have no applicable conclusion here.

Reproduction (from repository root):

```text
/Users/alex/Documents/ChatGPT/riemann/.venv/bin/python evidence/diag_theta_pole_locator/locator.py --output evidence/diag_theta_pole_locator/controls.json
pyright evidence/diag_theta_pole_locator/locator.py --pythonpath /Users/alex/Documents/ChatGPT/riemann/.venv/bin/python
```

The diagnostic controls passed. Final pyright: **0 errors, 0 warnings**.
Original mode imports `theta_eval.evaluate`, requires both explicit parent
approval and a matching completed controls file, and preserves that control
archive. The parent supplies remaining discovery seconds and runs the original
only after the preregistration gate. No original scan or certificate was run
by this worker.

**Disposition:** locator/controls ready for the parent-approved bounded
diagnostic. This worker supplies no original pole evidence or new estimate.
