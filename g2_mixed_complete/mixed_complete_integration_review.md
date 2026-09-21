# Adversarial review of the v1.23 mixed-term insertion

Reviewed `mixed_complete_insert.tex`, its integrated text in the complete manuscript, `mixed_directional_check.py`, and the saved 896-bit directional result. This is an analytic and code review; the independent replay itself was performed by the parent workflow.

**Outcome: no blocking mathematical error found.**

1. **Complete mixed error.** The proof retains both the omitted input and the omitted output. Expanding with `p = Py`, `q = Qy`, and `f = Yz` gives exactly the three terms displayed in the proof. Positive-form Cauchy--Schwarz, the remote compression bound, and the contraction of `I - QHQ/m` give the stated directional enclosure. The scalar pairing `z* b` agrees with the first-slot-linear convention.

2. **Far lower bound.** For `x = ||q||`, the upper bound on the H-energy gives the quadratic
   `v - a/m - 2 sqrt(a nu) x/m + (1 - nu/m) x^2`.
   Because `nu < m`, its unrestricted nonnegative minimum is exactly `v - a/(m - nu)`. This argument does not require the omitted-norm upper bound; using that bound could improve the result but is unnecessary. The saved complete lower result `6.760969872499...e-20` exceeds the saved trial value `6.469284394158...e-20` with positive interval separation. Its scope is correctly restricted to the first-polynomial bound with the old scalar head metric.

3. **Directional certificate.** The frozen 160-bit dyadic vector is used with its enclosed actual norm. The prefix action computing eta is the quadratic form of `H` on `PYz`; the remote moment calculation applies to `[I;-Z] C* z`, whose complete support ends at 1024. Beyond that support the shifted diagonal contributes nothing, so the saved remote residual bound is applicable. The first-polynomial lower and mixed lower are combined in the correct inequality direction. The code uses interval comparisons for the acceptance gate.

4. **Monotone improved head.** Keeping the head block `M0 + Y*Y` fixed and increasing the far block `Q_j^{-1}` proves the claimed inverse monotonicity. Its Schur complement is precisely `M0 + Y*(I-P_j(A))*Y`. The sandwich between `m^{-1} D_g^{-1}` and `D_g^{-1}` gives a common far form domain, and the finite head coupling plus positive Schur floor yields closed coercive lower forms. Thus no application of the unbounded far operator to an arbitrary Hilbert vector is needed. The limit can retain slack from the initial head replacement, as stated.

5. **Finite probes.** The Gram projection gives `Y*HY >= B*G^{-1}B`. For the omitted pairing, the same projection gives `E_B*G^{-1}E_B <= Y*QHQY <= nu E_Y`. Young's inequality then gives the stated lower head matrix. The instruction to certify positivity before inversion is necessary and present. No matrix positive-part step or compression-of-powers shortcut is used.

The rounded table proves the proposition's coarser displayed strict comparison. Its finer decimal lower value is supported by the saved full interval result. Neither this failure certificate nor the monotone-head construction proves a negative Weil direction, positivity of the complete low Schur complement, or any growing-window estimate. Those limitations are stated accurately.

## Addendum: the exact first updated head is also excluded

The subsequent strengthened gate in `mixed_directional_check.py` is valid. This adds a conclusion beyond the scalar-head result reviewed above; the earlier restriction to only the unmodified scalar head is superseded by this addendum.

For the same baseline `M0 = mu I`, the exact updated head is

`M1 = mu I + Y* H Y / 20`.

Let `f = Yz = Pf + Qf`. The positive square root of the bounded operator H, together with the complete remote compression bound, gives

`||H^(1/2) f|| <= sqrt(eta_z) + sqrt(nu rho_z)`.

Consequently

`z* M1 z <= mu ||z||^2 + (sqrt(eta_z) + sqrt(nu rho_z))^2 / 20 =: D_z`.

Because `M1 >= mu I > 0`, metric Cauchy--Schwarz gives

`b* M1^(-1) b >= |z* b|^2 / (z* M1 z) >= [|z* b_P| - epsilon_z]_+^2 / D_z`.

The code correctly retains the actual norm in `D_z` and uses the unnormalized projection in the numerator; no extra normalization factor is missing. It tests the numerator's strict positivity before squaring. All remote correlations entering the denominator are covered by the existing complete bound on `rho_z` and `QHQ`.

The reviewed 896-bit result gives:

- `D_z < 1.051962237847122`;
- complete updated-head mixed energy `> 1.96504912254049e-20`;
- complete first-degree updated-head majorant `> 6.65886152240573e-20`;
- excess over the trial K `> 1.8957712824708e-21`.

This certifies failure of the **exact first-degree updated head with the saved baseline `M0 = mu I`**, as well as of the coarser scalar-head bound. It does not reject a stronger initial head certificate, a higher inverse polynomial, the true inverse, the complete Schur sign, or Weil positivity. No blocking mathematical or implementation issue was found in this additional gate.
