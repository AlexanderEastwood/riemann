# Exact Euler boundary screen and research reassessment

Pre-claim admission diagnostic, not a certificate or new research row.

[Readable test and reassessment](../euler-boundary-reassessment-2026-09-29-v1.html).
[Mathematical review](independent-math-review.md),
[process review](process-review.md), and [route triage](route-triage.md)
are separate subagent assessments, not external expert reviews or historical
certificate replications. Their recommendations are integrated into the
report and the relevance gate in AGENTS.md/PROPOSAL_TEMPLATE.md.

Reviewed public base: `ccebc6524cf8adf5e83143ad00daa55b190737bd`.
All 104 existing node conclusions and 14 continuation inputs were reviewed
for scope/dependency; historical proofs and certificates were not replayed.

The screen retains the exact prime-2 and prime-3 Euler denominators but
rejects a proposed one-sided boundary ordering at a four-packet test.
At both 50 and 80 digits, the symmetric boundary defect has Rayleigh values
approximately `+0.20412414523193150818` and `-0.20412414523193150818`,
in both parities. These are direct interval-overlap *length* evaluations
with floating-point arithmetic, not interval/ball enclosures. No complete
Weil energy is computed and no compressed-product indefiniteness is claimed.

For whole-line translation operators let
`D_p=(1+1/p)I-(T_log(p)+T_-log(p))/sqrt(p)`, `Q=I-P`,
`K=(P D_p Q D_q P+P D_q Q D_p P)/2`. Commutativity on the
whole line gives the exact compression bookkeeping identity

`(P D_p P D_q P+P D_q P D_p P)/2 = P D_p D_q P-K`.

The screen tests the sign of `K`, not a factorization of the complete form.
No such factorization or bridge was supplied. The classical Euler-chain
identity fixes the factors, but the mixed boundary geometry also arises for
generic shifts and positive weights. This substantially limits the test's
research value. The independent reviews and readable report assess that
choice rather than treating it as a new RH obstruction.

## Replay

Use a Git checkout retaining the pinned base, Python with `mpmath==1.3.0`,
and fresh output paths:

```sh
.venv/bin/python audits/euler-boundary-screen-2026-09-29-v1/screen.py --dps 50 --output /tmp/euler-boundary-50.json
.venv/bin/python audits/euler-boundary-screen-2026-09-29-v1/screen.py --dps 80 --output /tmp/euler-boundary-80.json
pyright --project audits/euler-boundary-screen-2026-09-29-v1/pyrightconfig.json
```

The full-line factors are bounded, positive and commuting. Their finite-window
compression loses the commutation; the outside-window mixed term has no
automatic sign. Indicators of half-width `1/100` are normalized in ordinary
L2. Their centers are `3/2`, `3/2+log(3/2)` and their negatives, inside
`(-2,2)`. The screen retains the exterior paths explicitly.

The Davenport–Heilbronn interface and NS100/101 are marked not applicable
with the literal-operator mismatch. NS57 is not used to refute a property
that retains exact Euler coefficients. Rejection uses the original factors.

Final route classification: **Same open gap**, KERNEL-API. The bounded
distinct screen failed; no new Known-wall theorem, node, thaw or manuscript
version is added. Both historical original-evidence gaps remain open.
