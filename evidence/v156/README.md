# v1.56 — NS-57 finite prime-weight controls

Classification: exact identities, proved implications, and open input.
No new interval certificate, positive window, arithmetic sign estimate, API,
uniform floor, G2, or RH proof.

- [Integrated proof fragment](proof.tex), included verbatim in the manuscript
- [Versioned report](prime-weight-rigidity-2026-09-22-v2.html)
- [Local integration audit](integration-review-2026-09-22-v1.html), not an independent review
- [Validation](validation.json) and [complete build output](build-output.txt)
- [Twelve exact Maxima checks](exact-checks.mac) and [saved replay](exact-checks-output.txt)
- [Original standalone proof source](standalone-checkpoint-2026-09-22-v1.tex), retained as provenance

The total near-radical lemma detects every negative bounded perturbation.
Every nonzero finite change to the prime-shift coefficients has negative
directions in both parities, hence negative compact tests for the altered
complete forms. The altered family has finite first-zero windows and retains
the corresponding support geometry and modified affine-potential equation.
It does not retain the original arithmetic near-radical identity.

For a fixed coefficient pattern scaled by epsilon, the v1.53 residual gives
an analytic first-zero upper bound `lambda_* = O(sqrt(log(1/epsilon)))`.
Constants depend on the fixed pattern; there is no numerical threshold or
matching lower bound. Bounded perturbations preserve the uniform-floor
objective. Exact scalar compensation and an RH-conditional limiting lower
edge follow from v1.36; they do not establish its open sign input.

What changed from the standalone checkpoint: this version integrates the
proof into the complete manuscript, links its actual theorem dependencies,
registers NS-57 and the scoped NS-58 next question, and archives a fresh
Maxima replay plus full-build validation. The original private email and
personal correspondence are not included.

## Replay

From the repository root:

```sh
maxima --no-init --quit-on-error --very-quiet --batch=evidence/v156/exact-checks.mac
./manuscript/build.sh
python3 tools/verify_manifest.py v156
```

Actual complete build: 291 pages, zero undefined/duplicate references and
zero overfull boxes. This release is incremental, not cumulative.
