# NS-43 capacity channel note (internal)

Classification: the two propositions in `prime_channel_obstruction.tex` are proved implications using the already established positive Gaussian weight bounds and complete v1.50 identities. The final two-by-two signed prime-remainder bound is a named proposed open input. No computation, certificate, new window or manuscript version is involved.

## What changes relative to NS-34

NS-34 closed deleting prime 2. The first proposition closes deleting **any fixed nonzero prime-power channel**, with explicit dependence on its label and a support geometry closer to the edge. It does not apply the ratio estimate outside x >= log n.

The second proposition is stronger than a fixed-channel statement: any omitted channel n(a) <= theta exp(2a), for fixed theta < 1, is covered uniformly, even when n(a) changes. It uses the evenness of h at x-log n < 0. It does NOT use the positive-argument ratio formula there. The same two-dimensional source-kernel construction supplies exactly admissible even tests, with no source approximation and no dropped mixture cross terms. Odd parity is automatic. All selected edges are strictly interior; exterior edges remain in the full identity.

The ordinary physical-form upper bound is A_b + (8a+1) exp(a) + 2a, including the pole and prime contributions. The channel lower bound overwhelms it. This establishes failure of a modified comparison q-L >= -eta, not failure of q >= -eta.

## Explicitly ruled out

With all signed terms retained unchanged and every retained channel coefficient <= 1:

- Fixed finite prime-power retention.
- Fixed finite prime retention, even if all powers of those primes are retained.
- Uniformly bounded counts of retained channels/primes, with window-dependent labels.
- Prime-power cutoffs M(a)=o(exp(2a)); also limsup M(a)/exp(2a)<1/2, using only the next dyadic power, not a prime-distribution theorem.
- More generally, any fixed coefficient loss in an omitted channel at distance bounded away from the strict cutoff in the multiplicative ratio n/exp(2a).

The obstruction is already present if one keeps all exterior edges and all other channels at coefficient one. Deleting additional nonnegative energies cannot repair that particular comparison.

## Not ruled out

- Every local window has finitely many nonzero interior channels. Finiteness per window is not itself an obstruction.
- A moving omitted channel with n(a)/exp(2a) -> 1 is not covered by the uniform-theta argument.
- Deficits tending to zero fast enough to meet the stated necessary inequality are not ruled out categorically.
- Exact signed cancellation, including compensating changes in the potential/variance/pole, is outside the coefficientwise-loss model.
- Increasing other channel coefficients is outside this monotone deletion comparison.
- Other positive weights and the unmodified CAE/floor target stay open.

## Surviving next lemma, deliberately smaller than CAE

The two-by-two matrix E(t) in the proof fragment is an explicit smoothly weighted prime-minus-continuum discrepancy near n=exp(2t). A uniform operator-norm bound on this matrix for one fixed pair of even bumps would control the *unmodified* form on exactly the translating parity spaces used to expose the transformed-channel loss. It retains the signed arithmetic cancellation and every mixture cross term. The matrix identity D +/- C(t), with C(t)=E(t)+O(exp(-t)), gives a direct independently checkable reduction.

This is a concrete restricted-family next input, not an estimate for arbitrary f and not a logical claim of reduced RH strength. No proof of the bound or transfer from these spaces to the complete domain is supplied. If choosing a next research step, first derive its complete corrected-zero-field expression with the smooth Mellin weight and all endpoint conventions, then assess what a known zero estimate actually gives. A finite zero prefix or finitely many translated tests cannot establish the cofinal claim.
