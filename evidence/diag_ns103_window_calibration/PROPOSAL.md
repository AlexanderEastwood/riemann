# NS-103 proposal (filled before the claim, per PROPOSAL_TEMPLATE.md)

```
Proposal: Measure the window lambda* at which the plain Weil quadratic form,
  restricted to tests supported in [-lambda, lambda], first detects the
  Davenport-Heilbronn off-line zero (offset delta = 0.3085, height 85.70),
  and compare with the same form for zeta, which must stay nonnegative.
  A calibration of fixed-window sensitivity, not an RH mechanism.

Shared-input group: DISTINCT. Closest nodes: prop:v121-cofinal-rh (finite
  windows do not accumulate), prop:v125-cutoff-cost (window cost), NS-100/101
  controls (per-slice and factorization stops), CCM window positivity.
Status of that group: not a route; no attempts recorded on window sensitivity.

Arithmetic input beyond the functional equation:
  The actual coefficient data on the prime side: Lambda(n) (nonnegative,
  supported on prime powers) for zeta versus Lambda_f(n) for the
  Davenport-Heilbronn function (defined by -f'/f, all n, mixed signs).
  Gamma factors and evenness are identical in shape; only this data differs.

Control screen: n.a. The test evaluates the form ON the known-false analogue;
  the Davenport-Heilbronn function is the object, not a screen of a mechanism.
  Log-concave and reciprocal-dilation controls: n.a. (no positivity claim).

Wall check: Distinct test.
  Closest result: prop:v121-cofinal-rh; NS-100 (evidence/ns100_reassessment).
  What changes: the object (a function with a known off-line zero) and the
  question (at which window the restricted form turns negative, and which
  zero the negative direction resonates with). No node quantifies this.

Stated prediction (falsifiable): lambda* lies between 1/(2 delta) = 1.6 and
  2/delta = 6.5; the negative eigenvector's dominant frequency is near 85.7
  unless a zero with Re s > 1 below that height is detected first.

What success changes: a measured sensitivity law for fixed-window
  certificates (which offset an off-line zero needs before a window of size
  lambda can see it). This changes how v1.40-v1.43 windows are described.
  It does not touch G2, the uniform floor, or RH.
What failure changes: if the zeta form is not nonnegative in the pipeline the
  diagnostic is discarded as a bug; if lambda* > 5 the fixed windows are
  confirmed blind even to gross violations (recorded, no closure).

Budget: one session, one PR.   Version bump expected: no (diagnostic).
```
