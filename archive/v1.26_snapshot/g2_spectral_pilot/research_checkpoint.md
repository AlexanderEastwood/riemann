## Current research checkpoint: September 20, 2026 — actual finite Weil spectral pilot; manuscript remains v1.11

Continued the preceding deep-research recommendation using the actual finite Weil matrix and the manuscript's repaired n=0,4 prolate source. The complete v1.11 source and current research log were retrieved before work began. **No G2 arithmetic sign gap was closed. No RH proof or interval-certified finite positivity result is claimed.** The full 105-page manuscript and its PDF remain unchanged; this is an experimental checkpoint in the cumulative reproducibility bundle.

### Exact conditional improvement

For a unit candidate u, write alpha=<Wu,u>, r=P_(u perp)Wu, C=P_(u perp)WP_(u perp)|_(u perp), and A=C-alpha I. If A>=gamma I>0, elementary min–max and the scalar Schur equation prove a unique ground state and

`tan(theta)<=q:=||A^(-1)r||`, `sin(theta)<=q/sqrt(1+q²)`, and `alpha-<A^(-1)r,r> <= lambda_0 <= alpha`.

The proof uses `(C-lambda_0)^(-1)=(A+t)^(-1)` with t=alpha-lambda_0>=0; spectral calculus for the same positive A gives both bounds. An approximate solve z obeys `q<=||z||+||r-Az||/gamma`. For errors delta_A,delta_r and certified gamma_tilde>delta_A, use `||z||+(delta_r+delta_A||z||+||r_tilde-A_tilde z||)/(gamma_tilde-delta_A)`. For fixed exact u and matrix norm error eta, delta_r=eta and delta_A=2eta are valid. Source error remains separate; certify the fixed numerical candidate first, then add the true source's projector-distance error. These are conditional linear-algebra estimates, not independently established arithmetic assumptions or claims of originality.

### Actual computation and what it says

Used L=2 log(lambda), c=2 pi lambda², normalized even Legendre PSWF modes 0 and 4, and source coefficients from the same finite approximation's integrals. The fixed allowed smooth repair has support radius b=3/4: phi=exp(1-1/(1-(v/b)²)), psi=phi(1-Cv²), C=integral(phi)/integral(v²phi). All spectral computations include this repair. The translated Fourier coefficients retain (-1)^n, Haar measure, and the sole sqrt(u) factor in E(h). The physical endpoint uses n<lambda² at integer lambda². The matrix includes prime powers, poles, archimedean subtraction and its separate logarithmic diagonal. Both parity sectors enter the complement minimum.

At N=32, refined calculations give:

| lambda | ordinary residual/gap | inverse-weighted q | computed ground-angle sine |
|---:|---:|---:|---:|
| 2 | 553.598 | 0.00121100321 | 0.00121099977 |
| 2.5 | 4.55575e7 | 0.000514694790 | 0.000514694569 |
| 3 | 1.41142e14 | 0.000217848696 | 0.000217848671 |

At lambda=3,N=64, q≈0.000215892094 and angle sine≈0.000215892075, while the ordinary residual/gap is approximately 4.67624e14. Thus the crude bound loses useful spectral information. The positive computed complement minimum is approximately 1.313e-34; it is not certified. Small cutoffs can give gamma<0 without disproving convergence, as the explicit three-dimensional adversarial counterexample in the report shows.

Double precision was inadequate for the tiny lower spectrum: observed matrix changes under quadrature refinement were about 4.2e-12. Those apparent tiny negative/positive eigenvalues were discarded as sign evidence. N=32 runs at 80 digits/55 even modes/160 quadrature points and 105 digits/70 modes/224 points preserve the reported figures; matrix entries agree at the stored 70-digit precision. Source coefficient differences were approximately 9.17e-65, 1.91e-48 and 1.02e-36; at lambda=3 the endpoint differed relatively by 1.68e-17. Agreement is not an error enclosure. N=64 used 105 digits/70 modes/320 points. Five direct adaptive correlation integrals independently check matrix entries to the exported precision, with discrepancies below 5e-72.

### Independent endpoint experiment

Derived an exact finite-polynomial Mellin formula for the translated source coefficients and checked its phase and factors independently. This avoids oscillatory quadrature for the endpoint-only extension to N=4096. It is exact for a finite Legendre polynomial; the Galerkin approximation and numerical evaluation remain non-certified. The smooth repair was omitted only in this secondary endpoint calculation, with explicit absolute bound `|h_circle(0)|(2N+1)||E psi||_1/L` and `||E psi||_1<=2 sqrt(b) floor(b lambda)(1+C b²)`. At lambda=3 its relative bound is below 4.5e-16 even at N=4096.

For lambda=3, B≈5.58669542e-19. Relative endpoint errors are approximately 1.37454 at N64, 1.63677 at N128, 0.798989 at N512, 0.412764 at N1024, 0.208431 at N2048 and 0.104617 at N4096. No N4096 Weil matrix was assembled. This is a Fourier-cutoff effect, not merely the discarded double-precision noise. Do not infer a proved 1/N asymptotic; interior jumps can contribute oscillatory terms. Small ordinary-norm ground-state error does not imply relative physical-endpoint accuracy.

### Adversarial findings and next concrete step

The authorized adversarial agent checked basis phase, source normalization, strict endpoint trace, the full parity complement, the weighted Schur proof, the polynomial moment formula and the repair bound. It emphasized that gamma<=0 invalidates this sufficient certificate only, not source-to-ground convergence. It also rejected reading a tiny residual or an unconstrained numerical inverse as proof.

Next certify the fixed finite candidate at lambda=3,N=64: obtain interval/operator-norm bounds for matrix assembly, a genuine complement lower bound and an error-controlled solve. Add true-source error separately. Then seek a uniform signed-arithmetic estimate for the inverse-weighted residual on a valid growing window/cutoff sequence. For endpoint efficiency, the existing jump/continuous-derivative decomposition is the appropriate next target; the present observations do not justify deleting its terms. Full Fourier-complement control, continuum domain, endpoint normalization and full-strip convergence remain open. A source approximation theorem without spectral ordering is insufficient.

The centered sampler and its graph defect were not modified or used to claim metric transfer. Endpoint-shell insertion would still require its full derivative and graph terms. The independent p=2 evaluator-shell sign alternative remains open and must pass the preceding nonzero-forcing test. Weak G1 is unchanged.

### Saved deliverables

`G2_Spectral_Pilot_Report.md` gives the full conditional proof, settings, tables, limitations and reproduction instructions. The cumulative bundle contains `g2_spectral_pilot/` with five runnable scripts, JSON outputs and this checkpoint, plus the preceding deep-research artifacts. The canonical research log is updated while preserving all earlier attempts. The LaTeX/PDF pair is not regenerated because these numerical findings do not change a manuscript theorem or close a proof obligation.

