Proposal: Bounded diagnostic of an uncancelled complex zero of the ORIGINAL
M(z)=int_R phi(s+z)phi(s-z)ds, C(z)=int_R s^2 phi(s+z)phi(s-z)ds,
in 1/8<=Re z<=2, 1/8<=Im z<=5/8. A candidate is not a certificate.

Shared-input group: ZERO-GEOMETRY; validation of PR78/79's sufficient quotient-PD construction, closest NS100/101.
Status: frozen; no thaw or research-row claim. This is a falsification diagnostic of a specified sufficient mechanism, not a lower-bound proposal.

Arithmetic input beyond the functional equation:
  phi(u)=sum_(n>=1)(2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2))*exp(-pi*n^2*exp(2u)), extended evenly.
  Keep the complete original coefficients and complete M,C integrals. They determine whether this actual denominator has an uncancelled zero. The generic contour lemma alone supplies no existence claim; altered arithmetic controls cannot supply this original witness.

Dependency edge and arithmetic use (before any new candidate computation):
  Complete original M(z0)=0, C(z0)!=0, abs(Im z0)<pi/4 => uncancelled pole of k=C/M => Fourier(k) changes sign by PR79's complete-strip finite-pole argument => k is not PD. This rejects the general sufficient quotient-PD certificate. It does not refute original L1[X], RH or G2: L1[X](r)=(1/pi)int X(r-xi/2)^2 Fourier(k)(xi)dxi can be positive with a signed kernel.
  Diagnostic root/numerator samples do not establish these hypotheses. Certificate would additionally require full Arb integral/tail enclosures, a nonzero M boundary, rigorous positive argument count, and nonzero C throughout a box (or rigorously separated zeros), at two precisions. No simplicity assumption. A bounded null does not prove zero-freeness or PD.

Control screen (actual candidate, before proof/certification):
  Davenport-Heilbronn: not-applicable to this literal evaluator: different coefficients, gamma/completion and unverified complex-strip tail domain. The unchanged controls/example_screen.py computes a different derivative assertion and cannot screen a pole locator.
  NS100 log-concave order-2: not-applicable; the recorded obstruction is a per-slice cosine transform, while this tests the complete moment quotient.
  NS101 reciprocal dilation: shares generic quotient/convolution algebra and sufficient PD implication, changes the original lattice/Jacobi IVP. Known negative L1 implies its quotient is not PD but does not establish a pole; without a known pole it cannot validate locator sensitivity. Not run or called a pass.
  Additional control: SAME locator for M0=z^4+1,C0=1 on [7/10,18/25]^2 must find an approximate root with separated numerator samples. SAME M1=M0,C1=M0*exp(-z^2) must not label it an uncancelled pole. The first exact Fourier density changes sign; second quotient is exp(-z^2) with positive Fourier density. These share meromorphic/contour and axis-nonzero hypotheses, not theta arithmetic. Controls run before original evaluations; outputs archived.
  NS74/83: not-applicable: integer-dilation target sensitivity and NB per-doubling rate restriction; no NB approximation/rate claim.
  Command/artifact, precision, sample domain, values/residuals:
    evidence/diag_theta_pole_locator/locator.py controls first; original run only after control/reviewer gate. 128-bit discovery and same-cell256-bit replay. Full records and exact CLI to be archived with results. No original evaluation performed at preregistration.
  Full-scope obstruction, if any: PR78 excludes the positive sech-power mixture only, not general PD. None established for this original bounded search.

Wall check: Distinct test
  Closest result: PR78/79; NS100/101.
  What changes: search for an original uncancelled denominator zero, which would reject general quotient PD rather than only the already rejected mixture. No signed lower estimate supplied.

What success changes: a diagnostic candidate prepares one box for interval verification; only a verified uncancelled pole excludes general quotient PD.
What failure changes: no witness/control or numerical failure => inconclusive; stop this bounded test, no automatic domain enlargement or adjacent scan; no manuscript version.
Budget: 90 minutes discovery including controls, one PR; only if a promising candidate exists, at most one box and two hours for a separately scoped complete Arb certificate.
Disposition before claim: admit bounded diagnostic subject to passing matched controls and independent protocol review; no research row claimed.
Version bump expected: no for this diagnostic/audit.

## Frozen numerical protocol (before original computation)

9x9 equally spaced vertices. For each of64 cells use four-corner sampled principal-argument sum/(2*pi), not a certified winding. Rank by descending abs(round(sampled winding)), ascending min(abs(Mcorner))/max(abs(Mcorner)), then x/y indices. First four cells only. Same-cell Newton from center, <=12 iterations, each proposed step halved at most16 times to stay inside the SAME cell; otherwise stop. Analytic derivative of normalized M. Preserve all failures. Replay the SAME selected cells at256bits; do not rescan or reselect.

Approximate-root label requires endpoint residual abs(M)/corner-scale<2^-40 at both precisions and endpoints agreeing within2^-32 times cell diagonal. Numerator sample separation requires abs(C)/corner-C-scale>2^-20 at both precisions and C agreement within2^-32 relative corner scale; otherwise numerator unresolved. These thresholds prove neither an M zero nor C exclusion on a neighborhood. All cell scales and raw values retained.

Evaluator: modular-even original phi with24 lattice terms initially,32 on replay. Gauss-Legendre48/96 nodes per segment, initial real-s breakpoints [0,1/8,1/4,1/2,1,2,4], replay adds9/2. Multiply M and C by the SAME entire nonzero B(z)=exp(2*pi*exp(2z)-9*z)/(4*pi^4); include B' in normalized M derivative. Normalization preserves zeros and exact boundary winding, but sampled phase can alias. Lattice and real-tail bounds explicit. Quadrature error is NOT certified. Precision/cutoff/node replay detects instability but is not a complete integral enclosure. This limitation is part of the protocol, not a later downgrade.
