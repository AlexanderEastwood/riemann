# Reproduce v1.19: irreducible unsigned prime norm

The root TeX/PDF contain the entire working manuscript. The cumulative bundle retains all prior audit and reproducibility material. This checkpoint adds analytic obstructions, not a G2 positivity certificate.

1. Read `prime_norm_insert.tex`. The first proposition applies at any fixed window and to every finite-rank orthogonal projection. Check the simultaneous recurrence argument, conjugation estimate and use of compactness on a weakly null sequence.
2. Check the exact ratio for `phi=e^(-x/2)+e^(-(L-x)/2)` and the leading identity involving lambda. The classical unconditional PNT and Chebyshev estimate yield the displayed norm asymptotic. No nontrivial-zero location is used.
3. Read `adversarial_prime_norm_review.md`. The cutoff consequence applies only to the stated scalar sufficient bound. It does not rule out frequency-weighted estimates, directional inverse-action bounds or actual signed positivity.
4. Optionally run `python3 check_prime_norm.py` with numpy and mpmath installed. `prime_norm_checks.json` records non-certified normalization and recurrence diagnostics, not a norm or sign certificate.
5. Compile the root manuscript with `latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex`. The saved validation record states its page count and checks. All 423 preceding labels and all 72 historical ledger rows are retained.

The full operator's fixed-window positivity and ground-ordering certificates remain unchanged. Continuum eigenfunctions still have zero physical endpoints. G2's growing-window signed estimate and RH remain open.
