# Exact-source certification at lambda=3, N=64

The complete manuscript v1.13 now proves, by an explicit analytic error budget and rigorous interval computations, that the actual repaired G1 source's finite Fourier projection is within 2.60 x 10^(-36) of the previously certified rational candidate. Its normalized ground-state angle sine is below 0.000216. This closes the true-source identification prerequisite for that one finite matrix. G2 and RH remain open.

A separate certificate proves that the relative physical-endpoint error of this exact projection is between 1.374 and 1.375. Small ordinary ground-state angle therefore does not establish endpoint recovery.

## Exact objects and results

The parameters are lambda=3, c=18 pi, L=2 log(3), and N=64. Use the manuscript's normalized angular modes n=0 and 4, with positive value at zero; define the zero-integral combination using their exact physical integrals. Its repair is h_tilde=h_circle-h_circle(0) psi, where b=3/4, phi(t)=exp(1-1/(1-(t/b)^2)) for |t|<b and zero outside, and psi=phi(1-Ct^2), C=(integral_0^b phi)/(integral_0^b t^2 phi). Thus psi(0)=1 and its full integral is exactly zero.

The co-Poisson proxy is averaged with its multiplicative inversion on [1/3,3], then Fourier-projected in the same translated [0,L] basis and normalization as the earlier finite Weil certificate.

Certified results:

- Full infinite angular residual bounds: mode 0 <5.913e-56; mode 4 <4.796e-52.
- Angular uniform eigenfunction error: mode 0 <2.723e-52; mode 4 <2.509e-48.
- Exact projected-source coefficient error against the frozen vector <2.60e-36.
- Corresponding normalized rank-one projector distance <4e-36.
- Exact projected-source angle sine to the finite Weil ground state <0.000216.
- Physical endpoint 5.58669e-19 < B_3 <5.58670e-19.
- Relative projection endpoint error 1.374 < |delta_64(P_64 p_3)-B_3|/B_3 <1.375.

The first five claims do not imply the opposite of the last claim: coefficient error is measured against a finite candidate, while endpoint recovery compares the finite projection with the exact unprojected endpoint.

## What makes the angular bound rigorous

Let D be the self-adjoint diagonal Legendre operator with eigenvalues ell(ell+1), on its canonical domain, and J=D+c^2 X^2. Bounded self-adjoint perturbation gives compact resolvent. The even compression contains 70 coordinates. Its omitted angular tail is bounded below by 140*141=19740. The sole boundary link produces a rank-one Schur correction, bounded above by b_link^2/(19740-x). Signed interval LDL verifies equal negative inertia counts for both bounding finite matrices at xi-1 and xi+1. The counts are (0,1) for mode zero and (2,3) for mode four, identifying the exact eigenvalues and a gap of at least one from xi to every other even eigenvalue.

The full residual includes the first omitted Legendre coordinate. For its bound epsilon, the exact normalized eigenfunction error is at most sqrt(2)*epsilon. An explicit graph-norm bound is

`||(I+D)(v-psi)||_2 <= 2 epsilon + (1+|xi|+c^2) sqrt(2) epsilon`.

The Legendre evaluation sum has constant at most one by a telescoping estimate. Hence this controls pointwise values on the closed interval, including endpoints. Merely having a small L2 residual would not have justified endpoint evaluation.

Physical rescaling, integral errors and the two-mode combination retain all factors of sqrt(lambda). The repair does not require certified integration of its bump: integral(phi)<=b and integral(t^2 phi)>=b^3/128 imply ||psi||_infinity<=129. The small raw value at zero makes this coarse bound sufficient. Bessel's inequality then controls every finite projection coefficient in ordinary norm.

Exact finite-polynomial Mellin moments, evaluated with balls, replace non-certified quadrature. The m=9 integration interval has zero length and cancels in the moment formula. The interior endpoint trace uses only m=1,...,8. This distinction and the physical L^(-1/2) normalization are retained.

## Reproduction

Unpack the cumulative bundle, install `python-flint==0.9.0`, then run ordinary Python without `-O` (assertions are verification gates):

```sh
python g2_certificate/certify_g2_finite.py
python g2_certificate/certify_g2_series.py
python g2_source_certificate/certify_pswf_source.py
```

The source verifier uses 768-bit arithmetic and FLINT 3.6.0 in the recorded run. It checks the earlier candidate hash, lambda, N, dimension and PASS conditions before importing that already proved Weil-angle bound. The new result records the prior certificate hash as a dependency. This is a composed computer-assisted proof, not an independent reproof of the finite Weil matrix.

The file `pswf_rational_input.json` defines the exact approximate angular vectors and scalars. SHA-256:

`ac9dfa8c03f54a326e3ba7af59917ac435e63d41e978310301e6df6e53e83076`

The preceding frozen candidate hash remains:

`6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e`

`make_pswf_input.py` is an optional numerical input generator requiring mpmath; its accuracy is not a proof assumption. Do not regenerate the input when checking the recorded hash. `pswf_source_certificate.json` retains counts, error bounds, endpoint intervals and strict checks; `source_polynomial_intervals.json` retains enclosed polynomial and projected coefficients.

An adversarial reviewer checked the argument, implementation and saved outputs without rerunning the verifier. Both this verifier and the earlier ones rely on Arb; no independent software verification or external referee approval is claimed.

## What remains

This proves exact-source identification at one parameter and Fourier cut. It supplies no lower bound for omitted Weil Fourier directions, no uniform growing-window residual/complement inequality, and no endpoint-shell graph or full-strip estimate. The angular tail controlled here is distinct from the omitted Weil Fourier complement. Weak G1 and its corrected sampler are unchanged; the explicit graph defect remains in downstream formulas.

The next substantive spectral target is a uniform arithmetic bound for the inverse-weighted residual on a justified growing-window/cutoff sequence, with a complement lower bound and a separate relative endpoint budget. More isolated positive matrices alone do not establish that result. The independent signed evaluator-shell inequality at p=2 remains an alternative open G2 route.

Primary normalization references: [NIST DLMF 30.2](https://dlmf.nist.gov/30.2) and [30.3](https://dlmf.nist.gov/30.3). The DLMF differential spectral parameter is shifted by c^2 relative to the eigenvalue of D+c^2 X^2 used here. [Python-FLINT matrix documentation](https://python-flint.readthedocs.io/en/stable/arb_mat.html) describes the rigorous arithmetic interface.
