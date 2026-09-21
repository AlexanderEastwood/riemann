# v1.20 Schur revision: reproduction and scope

The root LaTeX/PDF pair is the complete manuscript. This directory contains new evidence; earlier directories remain unchanged. The new propositions are20.49–20.51. G2 and the low-head sign remain open.

Run from this directory with Python3, python-flint, NumPy, SciPy, mpmath and threadpoolctl available:

```sh
python3 certify_far_inverse.py --bits 320
python3 certify_far_inverse.py --bits 384
python3 check_structured_ceiling.py --bits 896
python3 certify_low_schur.py
python3 structured_low_schur.py --M 256
python3 structured_low_schur.py --M 512
python3 structured_low_schur.py --M 1024
```

The first two commands certify complete infinite far-inverse sandwich constants67/335. The third certifies only the failure of the saved lower-bound candidates. The last four reproduce failed Schur sign gates; a FAIL_LOWER_BOUND is expected and does not assert a negative Weil form. Recomputing ingredients may change their decimal serialization; the witness verifier intentionally checks the hashes of the archived ingredients. Preserve the archived files when comparing a fresh reconstruction.

The structured code loads original exact dyadic signed-tail witnesses from `../g2_weighted_signed/` when the development evidence directory is absent. It checks their hashes and the saved320-bit congruence margins. The prior tail certificate has its own complete verifier in that directory.

All coefficient series include rigorous remainder radii and the correct separate logarithmic/pole diagonals. New cache names begin `sequences_v3_`; older discarded draft caches are never loaded. The preliminary unversioned far_inverse_contraction.json with the wrong pole scale was excluded. Only far_inverse_contraction_b320.json and_b384.json are final results.

`structured_inverse_insert.tex` contains the complete mathematical insertion, including the monotone inverse-polynomial proof. `adversarial_uniform_review.md` records independent checks and rejected routes. `current/fixed_space_prime_action_v1.tex` is the recovered baseline used for integration; it is not the revised deliverable.

The root manuscript compiles with latexmk/pdfLaTeX. The development build helper expects the complete TeX file next to it; it compiles in a fresh temporary directory and atomically installs a closed, parseable PDF.
