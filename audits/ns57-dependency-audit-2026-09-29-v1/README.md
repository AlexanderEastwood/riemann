# NS57 dependency audit

[Readable report](../ns57-dependency-audit-2026-09-29-v1.html).

**Verdict:** no defect found in the specific first-zero chain used by PR63,
with `delta_2=-log(2)/100` and every other coefficient change zero, under
the explicitly inherited canonical-form and arithmetic-radical inputs.
No correction to the theorem or PR63's stated scope is required.

**Wall check: Same open gap**, KERNEL-API (NS51/55/58). This is independent
agent validation of a reused control, not a new arithmetic estimate,
external expert review, numerical certificate or research admission.

## What was reconstructed

Two separate reviewers split the proof at the negative compact-test input;
the coordinator read both derivations and checked their assumptions match.

| Link | Review | Outcome |
| --- | --- | --- |
| Negative bounded perturbation directions in real even/odd sectors | [Detection review](detection-review.md), sections 2–3 | Explicit paired Fourier bumps; one fixed finite radical approximation preserves a strict negative margin. |
| Complete cutoff transfer | [Detection review](detection-review.md), sections 4–5 | All exterior prime rows, both poles and actual operator-domain membership retained; window limit taken only after fixing the finite combination. |
| Small-window positivity and continuity | [First-zero review](first-zero-review.md), sections 1–3 | Restricted logarithmic scaling gives initial positivity. Compact form-energy sets supply the additional ingredient needed beyond strong continuity of compressed shifts. |
| Attainment and support | [First-zero review](first-zero-review.md), section 4 | Compactness yields a nonzero operator nullvector; translation or centered parity support arguments give endpoint saturation. |

The full first-zero parameter is the smaller of the two parity first-zero
parameters. At a sector's own first zero only that sector is asserted
nonnegative. Endpoint saturation concerns essential support, not a nonzero
trace. No location, eigenvector, simplicity or effective threshold was
computed.

## Inherited inputs and work not repeated

The canonical complete form and its identification with the physical
explicit formula remain inherited from v1.14/v1.18 and NS55. The original
Gaussian source, its derivative decay and the polarized global radical
theorem remain inherited from v1.35. The totality argument, real/parity
projections and complete fixed-combination cutoff transfer were reconstructed
from those inputs; the Gaussian construction and Poisson summation were not
reproved. V1.36's existing independent review remains part of the record.

NS46/v1.53's sensitivity rate, NS57's bounded-floor equivalences and spectral
limit, all historical numerical certificates, and the universal finite-pattern
theorem beyond the stated perturbation are not separately re-audited here.
No new arithmetic sign estimate or control screen is proposed, so no unrelated
Davenport–Heilbronn computation was run. No new research row, theorem node,
thaw, manuscript version, Python change or interval replay is needed.

## Consequence for the project

The scoped NS57 dependency supporting PR63 remains usable. PR63 separately
checks that this altered family retains its proposed prime-chain bounds;
those bounds alone still cannot exclude the control's nullvector. The exact
Euler recurrence and original radical identity are lost by the control, so
original API and arguments using those exact inputs remain open. Negative
altered tests do not exclude a uniform bounded-floor method.

The audit closes its validation question. It does not admit a new RH route.
Any next research proposal remains subject to the relevance and control gate.
Both historical original-evidence recovery groups remain open.
