# NS98: projected-cost attempt — no new arithmetic bound

**Wall check: Same open gap.** Closest results: NS92/93, with the exact
projected Gram already in NS53/61/73. The attempted change was to retain
the old-coefficient subtraction in a bound on the fixed Mobius direction.
No scale-independent average bound was obtained. No theorem node or
manuscript version is added.

[Attempt and stop condition](argument.tex) records the complete projected
cross term that remains unestimated. Its diagonal is bounded, by the same
elementary separation method used in NS93. This is not a cost bound.
Contractivity plus the signed-suffix triangle inequality gives precisely
NS92 again; productwise absolute values then reach NS93's already closed
majorant. The smaller projected cost and the actual numerator remain open.

Two finite blocks check the decomposition and its signs, not gain
efficiency. Their costs reproduce NS73. The negative signed cross sums
at N=16 and 32 are not extrapolated. All complete Gram tails and old/new
cross terms are included.

Replay from repository root with the pinned environment:

```sh
python evidence/ns98_projected_cost/certify_cost.py --bits 256 --sizes 16 32 --output /tmp/ns98-256.json
python evidence/ns98_projected_cost/certify_cost.py --bits 384 --sizes 16 32 --output /tmp/ns98-384.json
python evidence/ns98_projected_cost/certify_cost.py --bits 384 --sizes 16 32 --cutoff 256 --output /tmp/ns98-cutoff.json
python evidence/ns98_projected_cost/verify.py
maxima --very-quiet -b evidence/ns98_projected_cost/checks.mac
```

[Readable report](../../audits/projected-cost-attempt-2026-09-23-v1.html).
Author review only. Both original-evidence gaps and RH/G2 remain open.
