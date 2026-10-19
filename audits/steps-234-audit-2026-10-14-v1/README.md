# Audit Package: Tasks 2, 3, and 4 (`steps-234-audit-2026-10-14-v1`)

**Wall check: Known wall** for the general single-power bilinear logarithmic-derivative hierarchy in `ZERO-GEOMETRY` (`PR #72`, `NS-101`) and for universal $n^{-3}$-weighted recovery on $V_{2N}\cap V_N^\perp$ in `NB-GAIN`/`COEFF` (`NS-61`); **Same open gap** for `KERNEL-API` / `WEIL-FLOOR` (`NS-50/51/55/57/58`, `PR #63`) and for the actual `NB-GAIN` optimizer (`NS-53/61/78/80/87`). What changes:
1. **Task 2 (`ZERO-GEOMETRY`)**: Proves the **General Bilinear Single-Power Obstruction Theorem** via the Bell-polynomial triangular isomorphism $\Phi_M$ and establishes the exact degree-3 non-Bell remainder $\frac{9}{8}D_1 D_2 - \frac{3}{4}D_1^3 - 2c_1 D_1^2$ of the Planat–Solé Jacobi ODE polynomial $\mathcal{J}_{\mathrm{PS}}(P_0, P_1, P_2)$.
2. **Task 3 (`NB-GAIN` / `COEFF`)**: Delivers the separately versioned specialist brief `../coeff-specialist-brief-2026-10-14-v3.html`, incorporating the `NS-61` refutation of universal $n^{-3}$ recovery and the exact untruncated Schur–Rayleigh reduction for $\psi_N(t) = -t^2(t\beta_N'(t))'$.
3. **Task 4 (`KERNEL-API`)**: Proves the **Three-Island Gap and Exact Prime Diagonalization Theorem** on $\log 2 < a \le \frac{1}{2}\log 5$ ($q_{\mathrm{prime}}[L_2 g] \equiv \frac{5\log 2}{2}\|g\|_2^2$), low-frequency indefiniteness of the unrestricted symbol $M_a(0) < 0$, and **explicit finite-window separation of the `NS-57` control ($\delta_2 = -\frac{\log 2}{100}$) at $a = \log 3$** on the 2D even interior subspace $\operatorname{span}\{L_2 g_1^+, L_2 g_2^+\} \subset V_{\log 3}$ ($\lambda_{\min}^{\mathrm{NS57}}(\log 3) = -0.0268795922 < 0$ vs. $\lambda_{\min}^{\mathrm{orig}}(\log 3) = +0.0023039536 > 0$).
**RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

## Contents

- [`../steps-234-audit-2026-10-14-v1.html`](../steps-234-audit-2026-10-14-v1.html) — Styled HTML mathematical audit report for Tasks 2, 3, and 4.
- [`../coeff-specialist-brief-2026-10-14-v3.html`](../coeff-specialist-brief-2026-10-14-v3.html) — Separately versioned specialist feasibility brief v3 (`NB-GAIN`/`COEFF`).
- [`PROPOSAL.md`](PROPOSAL.md) — Pre-verification proposal and control screen plan.
- [`derivation.md`](derivation.md) — Complete proofs for Tasks 2, 3, and 4.
- [`verify_steps_234.py`](verify_steps_234.py) — Deterministic exact-rational and 60-digit `mpmath` verification script (`pyright` clean: 0 errors, 0 warnings).
- [`verification.json`](verification.json) — Saved verification output.

## Replay

From `/Users/alex/riemann-worktrees/origin-main-review`:

```sh
pyright audits/steps-234-audit-2026-10-14-v1/verify_steps_234.py
.venv/bin/python audits/steps-234-audit-2026-10-14-v1/verify_steps_234.py
```
