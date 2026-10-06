Proposal: Test the single original six-point translation matrix
B_ij=k((i-j)/4), i,j=0,...,5, k=C/M,
M(t)=int_R phi(s+t)phi(s-t)ds,
C(t)=int_R s^2 phi(s+t)phi(s-t)ds.
Seek one fixed rational v with v^T B v<0. Only a complete interval validation
would establish that inequality. No all-size or all-height positivity claim.

Shared-input group: ZERO-GEOMETRY, route-validation of PR78's sufficient quotient-PD construction; closest PR78–80, NS100/101.
Status: frozen, no thaw or research row claimed. This is a specified finite falsification question, not a new signed arithmetic lower bound.

Arithmetic input beyond the functional equation:
  The original complete single-lattice kernel
  phi(u)=sum_(n>=1)[2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2)]*exp(-pi*n^2*exp(2u)), extended evenly.
  Its actual coefficients determine all six complete M/C values. Retain lattice and real-integration tails; generic positivity of phi or functional-equation symmetry does not determine the matrix sign. No Euler-product estimating theorem is imported.

Dependency edge and arithmetic use (before any new candidate computation):
  A rigorously negative fixed rational form v^T[k(t_i-t_j)]v excludes positive definiteness of the original k by its definition. This rejects the general quotient-PD sufficient construction. It needs neither a complex pole nor PR79's strip contour asymptotics.
  k PD would imply C=M*k PD (M is an autocorrelation), hence the original first-Laguerre target via the complete Fourier identity. This sufficiency does not reverse: failure of k PD does not refute original L1[X], RH or G2. A finite PSD matrix does not imply global PD.
  Diagnostic eigendecomposition merely selects a witness. Remaining verification requirements for a candidate: complete original M,C interval enclosures including quadrature, lattice tails, integration tails and roundoff; certified M>0; fixed rational quadratic form strictly negative at two precisions. No midpoint solves. The arithmetic application is the actual original ratio, not the generic matrix criterion alone.

Control screen (actual candidate, before proof/certification):
  Davenport-Heilbronn: not-applicable to the literal theta evaluator; its coefficients, conductor and completion differ. An unchanged controls/example_screen.py checks a different derivative expression, not this matrix. No DH pass claimed.
  NS100 log-concave order-2: not-applicable; individual-slice Fourier positivity is not assumed in this full original quotient test.
  NS101 reciprocal dilation: shares positive smooth pair kernels, complete quotient and sufficient PD transfer, but changes the original lattice/Jacobi IVP. Its negative Laguerre examples force its own quotient to fail PD but do not identify a negative form on this particular six-point stencil. Not run or called a pass.
  Additional controls: SAME six-point matrix and fixed dyadic witness pipeline for g(t)=exp(-t^2), positive definite Gaussian, and f(t)=exp(-t^2)*(1+t^2), PR79's entire non-PD control. Require numerically positive Gaussian matrix and a stable negative fixed rational form for f, at128/256bits, before original evaluation. The second control shows why absence of complex poles need not prevent detection here. They share the real-even PD assertion/matrix definition, not original arithmetic coefficients or theta tails.
  NS74/83: not-applicable; NB inner-factor target sensitivity and fixed-smoothing dyadic rate restrictions involve different objects. No NB gain claim.
  Command/artifact, precision, sample domain, values/residuals:
    evidence/diag_theta_six_point/matrix_screen.py controls,128/256bits,
    points0,1/4,1/2,3/4,1,5/4; original_screen.py only after control and draft-PR gates. Exact commands/outputs archived on completion. No original values evaluated at registration.
  Full-scope obstruction, if any: PR78 rejects one positive sech-power mixture; PR80's bounded pole search was inconclusive. Neither determines this original finite matrix. Prior score-Gram/C-moment tests concern different functions/indices. No original matrix sign established yet.

Wall check: Distinct test
  Closest result: PR78–80, NS100/101.
  What changes: direct real-axis fixed rational quadratic-form witness; no complex-pole hypothesis. No changed theta coefficients and no new signed lower bound.

What success changes: a diagnostic negative candidate identifies one rational form for complete validation; only certified negativity rejects general quotient PD. Original first-Laguerre positivity remains open.
What failure changes: if no candidate or unstable/control-failed, stop this screen. A finite positive matrix proves no global PD and authorizes no stencil/spacing enlargement. Shelve further quotient screens until independent analytic input appears.
Budget: one hour including controls/setup. Fixed conservative deadline2026-10-06T15:59:00Z for discovery. Only a negative candidate may receive at most two hours for one complete Arb witness validation. One findings PR.
Disposition before claim: admit this bounded route-validation diagnostic after controls and independent protocol review; no research row.
Version bump expected: no for diagnostic/audit; no manuscript version planned.

## Frozen numerical protocol

Exactly six nonnegative arguments t=j/4,j=0,...,5; symmetry supplies negative differences. Original diagnostic uses the archived PR80 evaluator unchanged:128/256bits,24/32theta terms,Gauss-Legendre48/96per segment,R=4/4.5. Both M,C share the same analytic nonzero normalization and it cancels in k. Full raw normalized values, tail metadata and all matrices are archived. Roundoff and finite quadrature errors remain unbounded in this diagnostic. Realness/positive-M checks must pass; an invalid input is inconclusive, never silently repaired.

At128bits choose the first eigenvector returned by mpmath eigsy (ascending eigenvalues); a repeated eigenvalue makes no uniqueness claim. Normalize maximum component magnitude to1, orient the first attained maximum positive, then round each component to nearest multiple of2^-32 (ties-to-even). Preserve this ONE rational vector in both precision runs; require it nonzero. Candidate only if Q_p=v^T B_p v < -2^-40*k_p(0)*||v||² at BOTH precisions. Agreement requires max_j abs(k128_j-k256_j)<=2^-40*max(abs(k128_0),abs(k256_0)), and abs(Q128/(k128_0||v||²)-Q256/(k256_0||v||²))<=2^-40. Eigenvalues and midpoints certify nothing.

Independent replay, if diagnostic completes, evaluates exactly these same six t values with direct theta summands and adaptive tanh-sinh (256bits,36terms,R=5); no root search, alternative stencil or spacing. If no negative witness, no certificate stage. Any candidate interval validation is separate, complete, at two precisions, and limited to the frozen rational v.

## Pre-run implementation details and control gate

Original samples require finite M,C,M', positive real parts of M and C, and
max relative imaginary part of M,C,k no greater than2^(-bits/2); otherwise
stop inconclusive. The real part is stored only after this check. Exact
realness/positivity are properties of the original real integrals; these
numerical checks do not certify those integrals. The fixed dyadic vector is
nonzero because its oriented maximum component rounds exactly to1.

Both same-pipeline controls passed at128/256bits before original evaluation:
Gaussian minimum eigenvalue approximately1.2953787e-5; pole-free non-PD
control minimum eigenvalue approximately-0.11062796 and fixed rational
quadratic form approximately-0.41556783. These are diagnostic values,
not interval bounds. The complete records are controls.json.

## Completed result (original computation followed preregistration)

No negative diagnostic witness. All six computed eigenvalues are positive
at both precisions; the minimum is approximately0.000528172731. The ONE
frozen rational form is approximately+0.001688860965. The entry/form
agreement gates pass. A separate direct-theta, unnormalized tanh-sinh
replay at exactly the same six arguments reproduces the form and quotients
(maximum observed relative quotient discrepancy below3.85e-69). Neither
agreement nor positive computed eigenvalues is a certified lower bound.

The Gaussian and entire non-PD controls passed before original evaluation.
Preregistration commit1b9efc9 in draftPR81 preceded all12original quotient
evaluations (six per precision). The independent replay used six arguments,
no changed spacing/stencil, and no new vector selection. No negative
candidate justified the conditional interval stage. No certification run.

What had to change: nothing in the registered mathematical protocol.
A review note initially transcribed strict agreement signs; a coordinator
check of the preregistered code corrected the note to <=. Negative-margin
comparison remains strict. This was a reporting correction, not a rerun or
change of data. A pre-completion independent serialization adjustment did
not change any mathematical input.

Final disposition: stop this finite screen, shelve further quotient
falsification screens pending independent analytic input. General quotient
PD and the original Laguerre estimate remain open. No arithmetic lower
estimate, research row, theorem node, thaw or manuscript version.

Validation: three new Python scripts pass pyright with0errors/0warnings.
Unchanged manuscript builds to358pages with0undefined/duplicate references.
The104node records and14input demands are unchanged; ZERO-GEOMETRY receives
an audit annotation/source. No new-version manifest applies. Six assigned
reviews are archived with their exact scope and evidence limitations.
