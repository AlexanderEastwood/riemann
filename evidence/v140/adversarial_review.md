# NS-5 independent adversarial review

Date: 2026-09-21. Reviewer: a separate mathematical audit agent.

**Verdict: the new shifted comparison, certificate implementation and exact
Connes–van Suijlekom implication pass this review.** The certificate proves a
simple even ground state of the complete canonical `W_4`, with
`0 < mu_0 < 2.454e-75` and `mu_1 > 1e-73`. This is a fixed-window result;
it does not close G2 or prove RH. No claim of worldwide novelty or publication
readiness is made by this review.

## Reviewed bytes

SHA-256 at review time:

| File | SHA-256 |
|---|---|
| `certify_ground4.py` | `2c5d4a44de0a8e280e9c4cb2672eb715470df859fc0234c5c7be0305ddf3e4c0` |
| `new_section.tex` | `71acc45cdf2200668e8a74338008087f58ebdcaac04b54df6d275ffc4d541f21` |
| `ground4_b1024_shift1e-73.json` | `e7bcf35e64482ff0415c490155cbacdb7fa3ddcb607386ce7d353e3d16cbd1d2` |
| `ground4_b1280_shift1e-73.json` | `8eaef58850ab2a86fb070d1e553f6c7af866784a5a36e5dd78a71b8d2726ba1e` |

The earlier foundations examined were `prop:v114-weil-core`,
`prop:v117-ground-order`, `prop:v120-lambda4-tail`,
`prop:v125-even-complete`, `eq:v125-relative-margin`,
`prop:v126-direction-complement`, `prop:v126-full-window`, and the full
physical form in `prop:v135-both-parities`. Original v126 trial assembly and
directional verification code were also compared with the new reconstruction.

## Exact shifted comparison

The finite trial is `G=(V;Z)`, where `Z` means its actual tail coefficients,
including their signs. Set `r=BV+TZ`, `C=r* T^{-1} r`, and `Y=T^{-1}BV`.
Here every adjoint uses the manuscript's first-slot-linear convention.
Square completion gives

\[
V^*SV=K-C,\qquad 0\preceq C\preceq K.
\]

The upper bound on `C` follows from the already certified positive complete
Schur form, not from a numerical residual. Since `T >= delta I`,

\[
Y=-Z+T^{-1}r,\qquad
Y^*Y\preceq2Z^*Z+2r^*T^{-2}r
\preceq2H_t+2\delta^{-1}K.
\]

For `0 < sigma < delta`, the resolvent identity gives exactly

\[
V^*S_\sigma V=V^*SV-\sigma H_h
-\sigma Y^*(I-\sigma T^{-1})^{-1}Y.
\]

Spectral calculus bounds the inverse by `(1-sigma/delta)^{-1} I`. This proves
the new lower matrix in `lem:v140-shifted-schur`. It includes the entire change
in the infinite tail inverse. It is not the invalid operation of shifting the
finite head while keeping an unshifted Schur correction unchanged.

The old even and odd margins apply to exactly the reconstructed old trials.
No claim that a relative head margin is an ordinary spectral gap is used.
The new physical Grams `V*V` and `Z*Z` supply that missing coordinate information.
The complete tail floor `delta=1.7940e-8` comes from the existing signed tail
certificate and the archimedean diagonal lower bound, not from a finite tail.

## Implementation checks

- The new construction reproduces the original `simultaneous_trial.py` indexing:
  even rows include mode zero; odd rows start at one; both correction arrays
  begin at physical mode 17. Support ends at 4096. Parity coordinates are
  orthonormal, so the ordinary norm is the sum of coefficient squares.
- All frozen coefficient reconstructions are checked exact. The script has no
  midpoint solve in the proof path. Floating values select a trial column or a
  nonzero projection coordinate only; all gates on the selected objects are
  outward interval gates.
- The old ingredient witness SHA values are checked, the exact reconstructed
  head is enclosed by the saved head, and the head determinant excludes zero.
- The even relative inequality is replayed from its saved complete Gram upper.
  The odd complement inequality is replayed on the exact `K`-orthogonal
  complement. Exact Fraction arithmetic verifies that the larger odd trial
  has exactly the required physical head.
- The odd directional denominator is inherited from the original verifier's
  use of this same old `K` and frozen direction. The overlap check in the new
  script is a consistency check, not itself a proof that unrelated scalars are
  equal. The original construction and its provenance establish equality.
- Signed LDL retains negative pivots; it does not stop on the first negative
  pivot. Every reported pivot excludes zero.

In addition to inspecting the script, the reviewer independently recomputed
all leading principal determinant signs with Arb's matrix determinant routine,
rather than the script's custom LDL routine, at 1024 and 1280 bits. The results
were sixteen positive leading minors followed by one negative leading minor
in the even sector, and sixteen positive leading minors in the odd sector.
These yield the same inertia counts. Selected column norms were independently
reconstructed from the frozen base and correction arrays with Python exact
`Fraction` arithmetic; the new Arb Grams enclosed those exact rational norms.
The prior small final gates were replayed in memory during these checks.

The even column 16 complete Rayleigh quotient is enclosed by

\[
(2.45361754930,\;2.45361754931)\,10^{-75}.
\]

The old odd column 15 has complete Rayleigh quotient approximately
`3.59269956625301170615e-71`. In particular the earlier trial threshold
`1e-70` cannot lie below the entire odd spectrum. The smaller successful
threshold `1e-73` is a substantive correction to the initial diagnostic-based
choice, not numerical roundoff. No finite-cutoff eight-order gap is promoted
to a complete spectral gap.

## Passage from a lower matrix to the complete spectrum

The even lower matrix has exactly one negative eigenvalue and sixteen strictly
positive eigenvalues. Monotonicity of finite eigenvalues under quadratic-form
order makes the exact shifted even Schur matrix have at most one nonpositive
eigenvalue. The actual finite-supported even trial has complete Rayleigh
quotient below the shift, forcing one strictly negative eigenvalue. These
facts together exclude a zero eigenvalue of that Schur matrix. The odd Schur
matrix is positive definite.

Because the head is finite and belongs to the operator domain, its coupling
`B` is bounded, and `(T-sigma I)^{-1}B` lies in the tail operator domain.
The triangular square completion is boundedly invertible and preserves the
closed form domain. It transfers the negative index and the kernel exactly.
Compact resolvent and the existing strict positivity at lambda=4 therefore
give `0 < mu_0 < 2.454e-75` and `mu_1 > 1e-73`. The ordinary gap exceeds
`9.7546e-74`. This reasoning treats the complete operator, not the finite
trial compression.

## External theorem and normalization audit

Primary sources read directly:

- [Connes–van Suijlekom, arXiv:2511.23257v1, Theorem 6.1 and Remark 4.3](https://arxiv.org/html/2511.23257v1#S6)
- [Connes–Consani–Moscovici, arXiv:2511.22755v1, Lemma 3.1 and Propositions 3.2–3.4](https://arxiv.org/html/2511.22755v1#S3)

Theorem 6.1 requires a real distribution on the one-sided interval `[0,L]`,
the associated form on trigonometric polynomials, essential self-adjointness
and lower boundedness there, and a simple isolated global minimum with a
reflection-even eigenfunction. A generic self-adjoint extension would not
meet the stated operator-core hypothesis. Nor should an unspecified even
kernel replace the one-sided distribution: Remark 4.3 records an origin
distribution counterexample to that simplification.

The explicit distribution in `new_section.tex` has a convergent canceled
origin integral and order at most one. Substituting
`h_n(t)=2(1-t/L)cos(2*pi*n*t/L)` recovers the exact old diagonal `d_n`, including
`log(tanh(L/2))`; its pole contribution at `n=0` is `32*sinh(L/4)^2/L` as in
v114. Actual autocorrelations vanish at `t=L`, so the prime at 16 creates no
endpoint ambiguity. This checks the normalization and the one-sided
distribution hypothesis rather than relying on a Fourier-symbol analogy.

The established v114 decomposition is a real diagonal operator with logarithmic
growth plus a bounded self-adjoint commutator. It establishes the required
trigonometric operator core and compact resolvent for the actual physical
form. The new certificate establishes the remaining spectral hypotheses.

Writing `a=log(4)` and translating the centered eigenfunction to `[0,2a]`
multiplies its unitary Fourier transform by `sqrt(2*pi)*exp(-i*a*z)` when using
the external paper's unnormalized transform. That factor is zero-free.
Thus the claimed zero set is unchanged. Real zeros need not be simple, and
the theorem does not require a nonzero boundary value of the complete ground
eigenfunction.

## Exact scope of the replay

This review and the new run reuse the complete v125/v126 residual certificates;
they do not freshly assemble their 65536-row products and remote moment tails.
The even inherited ingredients have independent 768/896-bit evaluations;
the odd complement ingredients are the old 768-bit enclosure, reused for both
new precisions. The odd directional reports are the inherited 1024/1280-bit
evaluations. These limitations are correctly stated in the new proof and
reports. The new shifted gates and physical Grams themselves were evaluated
at 1024/1280 bits.

No new result about the repaired source endpoint, sampler graph defect,
cofinal positivity, Riemann's Xi function, or convergence of zero sets follows.
The specific NS-5 fixed-window hypothesis is closed; G2 and RH remain open.
