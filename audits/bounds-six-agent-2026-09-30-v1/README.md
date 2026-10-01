# September 30 six-agent round — publication record

**Classification: fixed-claim validation and scoped gain audits. Same open gap — NB-GAIN / NS53/61/87.** Six separate agents completed two groups of three. This index is a forward publication note; the original 31 manifested files and their manifest are preserved byte-for-byte. Their local paths and earlier unpublished-status fields record the original execution environment, not the current publication status.

## Replacement certificate for NS38

The direct 192/320-bit Arb method certifies

    -0.640027118160897146421661394744768547319369747
      < beta_(log4)(1) <
    -0.640027118160897146421661394744768547319369746 < -3/5.

The independent 128/256-bit digamma-series method certifies the broader interval `(-0.640150, -0.639904)`, also inside the historically reported enclosure and below `-3/5`. Only the direct method establishes the 45-place interval. The methods use different analytic evaluations but share Arb as the interval backend. The third reviewer passed all 37 recorded replay/integrity checks.

This is **REPLACEMENT evidence** for the numerical premise of NS38 / `prop:v132-global-index`, not recovery of `certify_beta4_negative.py` or its output. The beta certificate does NOT transfer to the physical lambda=4 form: its tests are not compactly supported in that physical window. It supports the existing full-line negative-index implication, including the even sector and finitely many homogeneous linear constraints. Both original-evidence recovery groups remain OPEN.

- [Direct method](certificate/01-direct/explanation.md), [verifier](certificate/01-direct/verify_beta.py), [outputs](certificate/01-direct/outputs.json).
- [Independent series proof](certificate/02-independent/proof.md), [verifier](certificate/02-independent/certify_series.py), [outputs](certificate/02-independent/certificate.json).
- [Adversarial review, including support and scope](certificate/03-adversarial/review.md), [37-check record](certificate/03-adversarial/replay.json).

## Scoped gain audits

[Gain01](gain/01-derivation/derivation-2026-09-30-v1.md) checks the previously derived weighted coefficient inequality, retaining full old refit. `L <= B S` gives `S^-1 <= B L^-1`, hence an upper gain bound in corrected-load coordinates. The valid lower bound in optimizer coordinates still needs an arithmetic estimate of those coordinates. A hypothetical Mobius-sized new block contributes only an `N^-3` certificate, whose normalized dyadic sum converges. This is a limitation of that certificate, not an upper bound on actual gain or a route closure.

[Gain02](gain/02-independent/assessment.md) assesses the literal structured-phase import for the complete projected kernel. It leaves the representation/complexity, a factor-N allowance and the companion actual signed numerator unestimated. A fixed theorem exponent cannot become A(N) with unchanged constants. [Gain03](gain/03-adversarial/review-2026-09-30-v1.md) accepts both scoped audits after correction G03-01: little-o model error is sufficient, not necessary; fixed strict signal/error separation also suffices. None supplies a nonsummable actual signed gain.

The [dependency note](publication/weighted-dependency.md) makes the previously local coefficient-corollary dependency explicit from public NS78. Historical references to local six-review working files are provenance references, not additional claimed public evidence. The [arXiv source addendum](publication/arxiv-source-note.md) records the structured-phase source and its exact scope. No new research row, theorem node, thaw or manuscript version is claimed. RH, G2 and all cofinal arithmetic inputs remain open.

## Portable fixed-certificate replay

The preserved original programs point to their historical local checkout. Use the new wrapper to replay the mathematics from this public checkout without modifying those records:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r audits/bounds-six-agent-2026-09-30-v1/publication/requirements-replay.txt
.venv/bin/python audits/bounds-six-agent-2026-09-30-v1/publication/replay_publication.py --output .local-runs/beta-six-publication.json
```

Choose a fresh output path. The wrapper verifies every original manifested file and the unchanged manuscript source hash, recomputes the same four fixed-precision runs, compares every numerical field with the sealed records, checks cross-enclosures, and confirms the originals remain unchanged. It does not call the old output-writing entry points, fetch data, or require any private/local historical path. The output and environment from the publication replay are recorded under `publication/`.

The original [manifest](manifest.json) binds the historical round. The additive [publication manifest](publication/publication-manifest.json) and [validation record](publication/validation.json) bind the portable wrapper, forward notes, and completed build. The wrapper's first failed display-ball check is preserved and its correction recorded; the final replay passes all 85 checks. Section 9 disposition: this is replacement validation of the same previously reported scalar at the same parameters, not a newly selected certificate or a new mathematical result. Publish as an audit without a version bump; preserve the manuscript and its historical conditional wording, with the forward ledger link identifying the now-available replacement evidence.
