# Reproduce the scoped meta-obstruction checks

This is an analytic result. No new finite-window certificate or floating-point
diagnostic is used in its proof.

From the repository root:

```sh
python3 evidence/v139/check_exact_models.py
python3 tools/verify_manifest.py v139
./manuscript/build.sh
```

The exact-rational script verifies six finite-dimensional unitary examples
preserving the entire source column (including a nonzero residual), three
positive location-blind mass-cap examples, and the rational constant used
in the v1.37 probe. These checks test the proposed obstruction and its scope;
the complete proofs are in `new_section.tex` and the live manuscript.

The source proxy, both-parity identity, cutoff probe, and bounded-floor
implication used as prerequisites are the existing results
`eq:v135-full-symbol`, `prop:v137-conditional-mass`,
`prop:v136-bounded-floor`, and `cor:v136-complement-floor`.
The new proof is reviewed in `adversarial_review.md`.

Building produces a temporary, ignored PDF solely to check compilation.
Delivery remains LaTeX only. No PDF or cumulative bundle is part of this evidence.

All inequalities in the models are exact rational identities, so this is
not an interval computation requiring two numerical precision passes.
No lambda=8 computation is run. No G2 or RH conclusion is claimed.
