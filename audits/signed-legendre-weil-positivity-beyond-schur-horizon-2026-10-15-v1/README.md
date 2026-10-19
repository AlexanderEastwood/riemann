# Milestone 15 Audit Package — Exact Signed Legendre Weil Positivity Beyond the Unsigned Schur Horizon & Universal Reflection Kernel Strictness (`WEIL-FLOOR` & `NB-GAIN` / `COEFF`)

- **Audit folder**: `audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/`
- **HTML report**: `audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1.html`
- **Target lanes**: `WEIL-FLOOR` and `NB-GAIN` / `COEFF`

## Wall Check & Open-Status Disclosure

- **Does this milestone prove the Riemann Hypothesis (RH)?** **No (`OPEN`).**
- **Does this milestone prove `G2` or the cofinal prime-shift lower bound as $a \to \infty$ ($K \to \infty$, $N_{\mathrm{leg}} \to \infty$)?** **No (`OPEN`).** Certifying strict positive definiteness of the finite-rank signed Legendre Weil matrices $W_{\mathrm{signed, tail}}^{(4, \mathrm{even})}(b) \succ 0$ and $W_{\mathrm{signed, tail}}^{(4, \mathrm{odd})}(b) \succ 0$ up to $N = 50$ ($K = 3$, $2b = \log(5/3) \approx 0.5108$, 23 active shifts) and $N = 380$ ($K = 4$, $2b = \log(38/21) \approx 0.5931$, 175 active shifts) at $\Delta_\alpha = 0$ demonstrates that the breakdown of the unsigned Schur potential $V_a(x)$ is an artifact of discarding the positive-definite reflection sum $\Delta_{\mathrm{Schur}}^{(N)}(b) = \sum |c_r| Q_{\tau_r, \operatorname{sgn}(c_r)}^{(N)} \succ 0$, and establishes positivity of the low-frequency archimedean lower bound (dropping $\int_{\xi_0}^\infty \sigma_{L_{\mathcal{P}}}(\xi)\alpha(\xi)\dots d\xi \ge 0$) restricted to the 8-dimensional Legendre polynomial subspace $\mathcal{V}_4^{\mathrm{even}} \oplus \mathcal{V}_4^{\mathrm{odd}}$. *(Scope note per `argon-m16-review` Finding 4: this finite-subspace certificate does not control low-to-high shift coupling outside $\mathcal{V}_4^{\mathrm{even}} \oplus \mathcal{V}_4^{\mathrm{odd}}$; the exact untruncated spatial archimedean integral $\mathcal{J}_{m,n}(\lambda; b)$ is derived in Milestone 16, and the full-space infinite-dimensional Block-Schur certificate on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b,b)$ is established in Milestone 17 v2.)* Extending signed positivity simultaneously to all Legendre degrees $N_{\mathrm{leg}} \to \infty$ and cofinally as $b \to \infty$ remains **OPEN**.
- **Missing-original evidence disclosure**: Both historical missing-original evidence groups documented in `evidence/MISSING.md` (`src/verify_phase2.py` and `final_weil_check.py`) remain **OPEN**.

## Contents

1. [`PROPOSAL.md`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/PROPOSAL.md): Problem statement, theorem summary, and scope boundaries.
2. [`derivation.md`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/derivation.md): Analytic proofs of Theorem 1 (Universal Indicator Completion-of-the-Square Across $u = 1$, All-Degree Polynomial Reflection Strictness Theorem, and Exact Signed-vs-Unsigned Legendre Decomposition) and Theorem 2 (Signed Legendre Positivity at $\Delta_\alpha = 0$ Across 175 Active Shifts vs. Unsigned Schur Breakdown & Davenport–Heilbronn Indefiniteness).
3. [`verify_signed_legendre_weil.py`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/verify_signed_legendre_weil.py): Self-contained two-precision (`256`-bit and `384`-bit) `flint.arb` verification script with exact `Fraction` shift thresholds and zero `numpy`/`scipy`/`mpmath` dependencies, passing `pyright` with `0 errors, 0 warnings, 0 informations`.
4. [`verification.json`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/verification.json): Two-precision ball-arithmetic certificate (`92/92` full-precision string ball overlaps PASS, `payload.sha256=08530eb9ffdc49744f0201011699dd9b1848ad438775049100c9cf9fc9c9b183`, `file_sha256=651abf0f5009da23933c41fa3c8bd9dcbe8576ea7e6e6d983258b08020bbef04`).

## Replay Command

```bash
pyright audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/verify_signed_legendre_weil.py
.venv/bin/python audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/verify_signed_legendre_weil.py
```
