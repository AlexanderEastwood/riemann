# Certified finite Weil matrix — v1.12 checkpoint

September 20, 2026. This is a computer-assisted result for one exact finite matrix and one explicitly specified candidate. G2 and RH remain open.

## What is certified

Take lambda=3, L=2 log(3), Fourier indices -64 through 64, and the manuscript's actual 129-dimensional arithmetic Weil matrix W. The matrix contains the pole contribution, all prime powers 2, 3, 4, 5, 7, 8, 9, and the archimedean term with its correct separate logarithmic diagonal. No zeta-zero list or RH hypothesis is used.

Interpret the 65 coefficient strings in `g2_finite_candidate.json` as exact decimal rational numbers, reflect them evenly, and normalize in the ordinary Euclidean norm. Call this exact unit vector u. It was generated from a numerical prolate-source approximation, but no accuracy assumption about that approximation enters the certificate.

For P the orthogonal projection onto u-perp, alpha=<Wu,u>, r=PWu, C=PWP restricted to u-perp, and A=C-alpha I, both calculation paths establish:

- A > 10^(-34) I.
- q=||A^(-1)r|| < 0.000216.
- 3.64 x 10^(-38) < the lowest eigenvalue of W < 5.32 x 10^(-38).

Consequently W is positive definite with a simple even ground state, and the sine of its angle to u is less than 0.000216. The conditional min-max/Schur proof is Proposition 20.25; the precise finite certificate is Proposition A.1 in the complete manuscript.

The input file SHA-256 is `6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e`.

## Reproduce

Use ordinary Python without the `-O` option, since the second script uses assertions as strict verification gates. Install Python-FLINT 0.9.0, then run the scripts in this order from this directory:

```sh
python -m pip install python-flint==0.9.0
python certify_g2_finite.py
python certify_g2_series.py
```

The first run used FLINT 3.6.0. It uses 512-bit Arb/Acb ball arithmetic, certified integration with the removable singularity rewritten using sinc, exact parity decomposition, a Householder complement and interval LDL/LU. Its matrix export is required by the second script only for the cross-check. The second run uses 768-bit arithmetic, 128 terms of a digamma/trigamma series with explicit symmetric geometric-tail enclosures, and a full rational nonorthonormal complement with its Gram matrix retained. It does not use quadrature or Householder coordinates. Both passes verify strict comparisons on interval enclosures; requested precision or quadrature tolerance alone is not treated as a certificate.

All 8,321 parity-block matrix entries have overlapping independent assembly enclosures. The methods share the Arb software implementation, so this is not an independent software verification, formal proof-assistant verification, or external referee review. The exact mathematical identities and the rigorous-arithmetic implementation are the trusted basis of this computer-assisted result.

Files `g2_finite_certificate.json` and `g2_finite_series_certificate.json` record strict checks, pivot enclosures, input hash, precision and resulting intervals. `g2_finite_matrix_intervals.json` and `g2_finite_series_intervals.json` retain assembly data. The optional numerical generator `make_g2_finite_candidate.py` depends on the earlier pilot scripts supplied in `../g2_spectral_pilot/`; running the generator is unnecessary for checking the exact frozen candidate and is not part of its certification. Do not overwrite the candidate if checking the published hash.

## Scope and next step

This establishes neither an error bound between u and the exact PSWF source nor any statement about an omitted Fourier complement, a growing window/cutoff sequence, endpoint recovery, graph convergence or full-strip transfer. The earlier non-certified source pilot had relative physical-endpoint error about 1.375 at N=64. Ordinary norm/angle control does not repair that endpoint limitation.

The next concrete task is a rigorous coefficient/projector error bound for the exact repaired source at this same parameter, using a validated PSWF spectral approximation and exact-moment repair. It should include a separate physical-endpoint error budget; merely attaching a small L2 error is insufficient. A uniform signed-arithmetic inverse-weighted residual/complement estimate remains the main spectral route to G2. The independent signed evaluator shell inequality at p=2 remains an alternative open target.

## Primary implementation references

- [Python-FLINT matrix arithmetic and enclosed LU solves](https://python-flint.readthedocs.io/en/stable/arb_mat.html)
- [Python-FLINT complex ball integration](https://python-flint.readthedocs.io/en/stable/acb.html)
