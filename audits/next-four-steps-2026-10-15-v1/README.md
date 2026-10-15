# Audit Package — Next Four Steps (`next-four-steps-2026-10-15-v1`)

**Date:** 2026-10-15 (Version 1)
**Worktree:** `/Users/alex/riemann-worktrees/origin-main-review` (branch `codex/four-lane-audit-20261014`)
**Wall check:** Closest results: `NS-57` / `NS-92` (`KERNEL-API`), `NS-61` / `NS-71` / `NS-72` / `NS-74` (`NB-GAIN` / `COEFF`), and `NS-98` / `NS-101` (`ZERO-GEOMETRY`). What changes:
1. **`KERNEL-API` (`flint.arb` / `flint.acb` Rigorous Ball Certificate):** Certifies in 256-bit interval arithmetic both the **All-Vector Positivity Floor** on $V_{a-\log 2}$ across the Three-Island window $\log 2 < a \le \frac{1}{2}\log 5$ ($q[L_2 g] \ge [0.92182853\dots]\,\|g\|_2^2 = [0.28363954\dots]\,\|L_2 g\|_2^2 > 0$ for all $g \in V_{a-\log 2}$) and the **2-Mode Even Interior Separation of `NS-57`** at $a = \log 3$ ($\det M_{\mathrm{orig}}(\log 3) > 0 > \det M_{\mathrm{NS57}}(\log 3)$ and rational witness $g_\star = g_1^+ + \frac{3}{25}g_2^+ \in H_0^1(-\log(3/2), \log(3/2))$ satisfying $q_{\mathrm{orig}}[L_2 g_\star] > 0 > \widetilde{q}_{\mathrm{NS57}}[L_2 g_\star]$).
2. **`NB-GAIN` / `COEFF` (Stieltjes–Divisor Dual Identity & `NS-74` Control Diagnostic):** Proves the exact Stieltjes–Divisor identity $M_N(u,y) = \tilde{\lambda}_{\mathrm{proj}}^T (S^{(2)})^{-1}h^{(2)} = \lambda_{\mathrm{new}}^T y + \lambda_{\mathrm{old}}^T u = \sum_{n=N+1}^{2N-1}\widetilde{\psi}(n/N)(1 * \Delta c)(n)$ with unconditional Bessel bound $\|(\Pi_{2N}-\Pi_N)\Lambda_b\|_H^2 \le C_{\widetilde{\psi}} N^3$ ($C_{\widetilde{\psi}_5} = \frac{46183}{15015}$, $C_{\widetilde{\psi}_7} = \frac{5132}{12155}$) and proves the exact orthogonal splitting of `NS-74` ($U_\beta^*\tau = P_{\mathcal{T}}(U_\beta^*\tau) \oplus \tau_\beta^\perp$, $\|\tau_\beta^\perp\|_H^2 = F_\beta$), verified in 256-bit `flint.arb` across $N \in \{4, 8, 16, 32, 64\}$.
3. **`ZERO-GEOMETRY` (Single-Point Wronskian & Cubic Integrating-Factor Obstruction):** Proves in $\mathbb{Q}[\phi,\phi',\phi'',\phi''']$ that single-point denominator clearing of $\phi(u)^2$ in $P_1(u)$ or $\phi(u)^3$ in $\mathcal{J}_{\mathrm{PS}}(u)$ produces a vertical-line Parseval integral $\int_{\mathbb{R}} 4\phi(u)^2 P_1(u)e^{2xu}\,du = -\frac{1}{\pi}\int_{\mathbb{R}}\tau^2|f(x+i\tau)|^2\,d\tau < 0$ and cubic normal form $8\phi^3\mathcal{J}_{\mathrm{PS}} = (\frac{1}{3}\partial_u^3 - \frac{8c_1}{3}\partial_u^2 + \frac{4c_2}{3}\partial_u + 8c_3)(\phi^3) + \frac{3}{2}\partial_u((\phi')^2\phi) - \frac{19}{2}(\phi')^3$, which have identical signs on RH-true kernels and on `NS-101` / `Davenport–Heilbronn`.
- **Open-status disclosure:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

---

## Contents

- [`PROPOSAL.md`](./PROPOSAL.md) — Audit scope, wall check, and mathematical targets.
- [`derivation.md`](./derivation.md) — Full self-contained proofs of Theorems 1A, 1B, 2A, 2B, 3A, and 3B.
- [`verify_next_four_steps.py`](./verify_next_four_steps.py) — Deterministic 256-bit `flint.arb` + 50-digit `mpmath` verification script (`pyright`: 0 errors, 0 warnings).
- [`verification.json`](./verification.json) — Machine-checkable JSON verification output.
- [`../next-four-steps-2026-10-15-v1.html`](../next-four-steps-2026-10-15-v1.html) — Companion styled HTML report (inline CSS, Georgia serif, email-paste-ready).
- [`../coeff-specialist-brief-2026-10-15-v4.html`](../coeff-specialist-brief-2026-10-15-v4.html) — Version 4 update of the `COEFF`/`NB-GAIN` Specialist Brief incorporating Theorems 2A and 2B and the 256-bit `flint.arb` diagnostic table.

---

## Reproduction

```bash
pyright audits/next-four-steps-2026-10-15-v1/verify_next_four_steps.py
./.venv/bin/python audits/next-four-steps-2026-10-15-v1/verify_next_four_steps.py
```
