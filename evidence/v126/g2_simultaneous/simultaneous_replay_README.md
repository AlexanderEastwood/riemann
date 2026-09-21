# v1.25 complete even certificate and growth audit

Run from `g2_simultaneous` after extracting the cumulative bundle; sibling `g2_low_schur` and `g2_weighted_signed` provide the original exact witnesses and assembly. Python dependencies: python-flint 0.9.0, numpy, scipy; mpmath for the smallest finite diagnostic margin. PDF generation additionally needs LaTeX and PyMuPDF/Pillow for layout review.

Main verification (does not regenerate or change the frozen witness):

```sh
python simultaneous_trial.py --mode verify --normalized --parity even --M 4096 --J 65536 --steps 16 --bits 768
python simultaneous_trial.py --mode verify --normalized --parity even --M 4096 --J 65536 --steps 16 --bits 896
python complete_margin.py 768
python complete_margin.py 896
```

The reports must say PASS_COMPLETE_HEAD and PASS_COMPLETE_EVEN_RELATIVE_MARGIN. The same exact dyadic witness hash is used in both replays. The latter verifies U < (1-62629/100000)K by interval LDL, not by a floating eigenvalue estimate. The complete remote bound accounts for every mode beyond65536; the inverse majorant uses the previously certified shifted inner factors, whereas the outer energy/residual are unshifted.

`joint_remote_gate.py` is a supplementary bound with a common remote Gram; it is not needed for the main sign. `quantify_head_error.py` records ordinary-error estimates for failed trial bounds. The unscaled even and both odd trial reports are exploratory and inconclusive for exact sign. Positive individual directions never replace the simultaneous matrix test.

`window_scaling_probe.py --lambda-value 3` (and4,5,6,8) is a DIFFERENT, finite-only pipeline: even heads throughlambda², cuts256/384,4096-bit arithmetic. It is not a complete-tail certificate. Floating diagnostics can lose tiny margins; the lambda8 inverse-metric branch avoids subtracting nearly equal numbers and records a separately verified relative threshold. Earlier exploratory2048-bit/interval-LU attempts were rejected and are discussed in the log, not asserted as certificates.

To replay the two fresh far-cut tables without launching the finite study:

```sh
python - <<'PY'
from window_scaling_probe import far_cuts
for bits in [320,384]:
    for lam in [3,4,5,6,8]:
        print(far_cuts(lam,bits))
PY
```

These thresholds certify positivity of the stated scalar remote comparison only. They do not certify the intervening inner head. No mu/rho or moment constants have been transferred fromlambda4 to another complete window.

Main result: complete even form atlambda4 positive; oddlambda4 and cofinal G2/RH remain open. See the full manuscript, research log, interval reports and adverse reviews for hypotheses and limitations.
