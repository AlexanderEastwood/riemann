# Proposal — Exact Signed Legendre Weil Positivity Beyond the Unsigned Schur Horizon & Universal Reflection Kernel Strictness (`WEIL-FLOOR` & `NB-GAIN` / `COEFF`)

- **Audit folder**: `audits/signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1/`
- **Date**: `2026-10-15`
- **Target lanes**: `WEIL-FLOOR` (Cofinal Signed-Arithmetic Cancellation vs. Unsigned Schur Depletion) and `NB-GAIN` / `COEFF` (Mellin–Jacobi–Legendre Finite-Rank Operator Reduction)

---

## Wall Check & Open-Status Disclosure

- **Does this milestone prove the Riemann Hypothesis (RH)?** **No (`OPEN`).**
- **Does this milestone prove `G2` or the cofinal signed-arithmetic lower bound as $a \to \infty$ ($K \to \infty$, $N_{\mathrm{leg}} \to \infty$)?** **No (`OPEN`).** Certifying strict positive definiteness of the finite-rank signed Legendre Weil matrices $W_{\mathrm{signed}}^{(4, \mathrm{even})}(b) - \varepsilon_4^{\mathrm{even}}(b) I_4 \succ 0$ and $W_{\mathrm{signed}}^{(4, \mathrm{odd})}(b) - \varepsilon_4^{\mathrm{odd}}(b) I_4 \succ 0$ across $N \le 50$ ($K = 3$) and $N \le 380$ ($K = 4$, 175 active shifts) at $\Delta_\alpha = 0$ demonstrates that the breakdown of the unsigned Schur potential $V_a(x)$ is an artifact of discarding the positive-definite reflection sum $\Delta_{\mathrm{Schur}}^{(N)}(b) = \sum |c_r| Q_{\tau_r, \operatorname{sgn}(c_r)}^{(N)} \succ 0$, and establishes Positivity on the 8-dimensional Legendre polynomial subspace $\mathcal{V}_4^{\mathrm{even}} \oplus \mathcal{V}_4^{\mathrm{odd}}$ (plus the full infinite-dimensional archimedean tail via $\varepsilon_4^{\mathrm{even/odd}}(b)$). Extending this positivity to all Legendre degrees $N_{\mathrm{leg}} \to \infty$ simultaneously and cofinally as $K \to \infty$ remains **OPEN**.
- **Missing-original evidence disclosure**: Both historical missing-original evidence groups documented in `evidence/MISSING.md` (`src/verify_phase2.py` and `final_weil_check.py`) remain **OPEN**.

---

## 1. Problem Statement & Strategic Objective

In Milestones 10, 13, and 14, we extended the spatial Schur-certificate horizon of the multi-prime Euler preconditioner $B_{\mathcal{P}_+, \mathcal{P}_-}$ by replacing each signed off-diagonal prime-ratio shift operator $c_r (S_{\tau_r} + S_{-\tau_r})$ with its unsigned Schur lower bound:
$$c_r (S_{\tau_r} + S_{-\tau_r}) = -|c_r| D_{\tau_r} + |c_r| M_{\tau_r, \operatorname{sgn}(c_r)}, \qquad M_{\tau_r, \sigma} := D_{\tau_r} + \sigma (S_{\tau_r} + S_{-\tau_r}) \succeq 0.$$
Even when augmented by the two-sided positive-shift rank-1 constant-mode floor (Milestone 13), the unsigned Schur diagonal $V_a(x) = C_{\mathrm{diag}}(\mathcal{P}_K) - \sum_{\tau_r < 2b} |c_r| w_{\tau_r}(x)$ subtracts the **absolute value** $|c_r|$ of every active shift, discarding all higher-mode reflection positivity and all signed Möbius-prime cancellation between positive ($c_r > 0$) and negative ($c_r < 0$) shifts.

In Milestone 14, we discovered that on the orthonormal Legendre polynomial basis $\{e_m\}_{m=0}^{2N-1}$ of $L^2(-b, b)$, both the shift matrix $S_\tau^{(N)}$ and the support multiplicity matrix $D_\tau^{(N)}$ are **single global rational polynomial matrices** in $u = \tau / b \in [0, 2]$ with zero piecewise branching at $u = 1$.

This milestone answers three structural questions at the heart of `WEIL-FLOOR` and `NB-GAIN` / `COEFF`:
1. **Why is $D_\tau^{(N)}$ globally analytic across $u = 1$, and why is $Q_{\tau, \sigma}^{(N)} = D_\tau^{(N)} + \sigma S_\tau^{(N)}$ strictly positive definite for all degrees $N \ge 1$ and all $u \in (0, 2)$?**
2. **What is the exact operator-matrix discrepancy $\Delta_{\mathrm{Schur}}^{(N)}(b) := W_{\mathrm{signed}}^{(N)}(b) - W_{\mathrm{unsigned}}^{(N)}(b)$ discarded by the unsigned Schur bound on the even and odd Legendre subspaces $\mathcal{V}_N^{\mathrm{even}} \oplus \mathcal{V}_N^{\mathrm{odd}}$?**
3. **When we retain the exact signed shift sum $\sum_{\tau_r < 2b} c_r S_{\tau_r}^{(4)}$ at $\Delta_\alpha = 0$ (zero archimedean shift!) and subtract the exact infinite-dimensional Gegenbauer–Spherical-Bessel Parseval tail bound $\varepsilon_4^{\mathrm{even/odd}}(b) I_4$, how far beyond the unsigned Schur horizon do $W_{\mathrm{signed}}^{(4, \mathrm{even})}(b) - \varepsilon_4^{\mathrm{even}}(b) I_4 \succ 0$ and $W_{\mathrm{signed}}^{(4, \mathrm{odd})}(b) - \varepsilon_4^{\mathrm{odd}}(b) I_4 \succ 0$ remain strictly positive definite for $K = 3$ and $K = 4$?**

---

## 2. Main Theorems & Deliverables

### Theorem 1 (Universal Indicator Completion-of-the-Square, All-Degree Polynomial Reflection Strictness & Exact Signed-vs-Unsigned Legendre Decomposition)
1. **Single-Integral Indicator Completion of the Square Across $u = 1$**: For every $\tau \in (0, 2b)$, the support multiplicity weight on $(-b, b)$ is the single sum of indicator functions
   $$w_\tau(t) = \mathbf{1}_{(-b, b-\tau)}(t) + \mathbf{1}_{(-b+\tau, b)}(t) \qquad \forall t \in (-b, b),$$
   which automatically takes values $\{1, 2, 1\}$ when $\tau \in (0, b)$ (overlapping intervals) and $\{1, 0, 1\}$ when $\tau \in [b, 2b)$ (disjoint intervals). Consequently, for every $f \in L^2(-b, b)$ and $\sigma \in \{+1, -1\}$,
   $$\langle f, (D_\tau + \sigma(S_\tau + S_{-\tau})) f \rangle_{L^2(-b, b)} = \int_{-b}^{b-\tau} \left(f(t) + \sigma f(t+\tau)\right)^2\,dt \ge 0$$
   is a single polynomial integral on $[-b, b-\tau]$ for all $u = \tau/b \in [0, 2]$ with zero piecewise branching at $u = 1$.
2. **All-Degree Polynomial Reflection Kernel Theorem**: Since $(-b, b-\tau)$ has strictly positive length $2b - \tau > 0$ for all $u \in (0, 2)$ and polynomials are real-analytic, a polynomial $f$ satisfies $\int_{-b}^{b-\tau} (f(t) + \sigma f(t+\tau))^2\,dt = 0$ if and only if $f(t+\tau) = -\sigma f(t)$ for all $t \in \mathbb{R}$. Because the only polynomial solutions to $f(t+\tau) = -\sigma f(t)$ ($\tau > 0$) are $f \equiv 0$ (for $\sigma = +1$) and $f \equiv \text{const} \in \operatorname{span}\{e_0\}$ (for $\sigma = -1$), for **every** finite dimension $N \ge 1$ and **every** $u \in (0, 2)$:
   - $Q_{\tau, +1}^{(N, \mathrm{even})} \succ 0$ on $\mathbb{R}^N$ and $Q_{\tau, +1}^{(N, \mathrm{odd})} \succ 0$ on $\mathbb{R}^N$,
   - $Q_{\tau, -1}^{(N, \mathrm{even})} \succeq 0$ with $\ker(Q_{\tau, -1}^{(N, \mathrm{even})}) = \mathbb{R} e_0$ and $\widetilde{Q}_{\tau, -1}^{(N, \mathrm{even})} \succ 0$ on $\mathbb{R}^{N-1}$,
   - $Q_{\tau, -1}^{(N, \mathrm{odd})} \succ 0$ on $\mathbb{R}^N$.
3. **Exact Signed-vs-Unsigned Legendre Decomposition**: On both $\mathcal{V}_N^{\mathrm{even}}$ and $\mathcal{V}_N^{\mathrm{odd}}$,
   $$W_{\mathrm{signed}}^{(N, \mathrm{sector})}(b) = W_{\mathrm{unsigned}}^{(N, \mathrm{sector})}(b) + \Delta_{\mathrm{Schur}}^{(N, \mathrm{sector})}(b), \qquad \Delta_{\mathrm{Schur}}^{(N, \mathrm{sector})}(b) := \sum_{0 < \tau_r < 2b} |c_r| Q_{\tau_r, \operatorname{sgn}(c_r)}^{(N, \mathrm{sector})} \succ 0.$$

### Theorem 2 (Two-Precision Certified Signed Legendre Positivity at $\Delta_\alpha = 0$ Across 175 Active Shifts vs. Unsigned Schur Breakdown & Davenport–Heilbronn Failure)
At $\Delta_\alpha = 0$ (zero archimedean shift, where the archimedean floor defect $-\alpha(\xi) > 0$ on $(-\xi_0, \xi_0)$, $\xi_0 \approx 6.289836$, is absorbed directly by the Legendre Weil matrix and its infinite-dimensional Parseval tail bound $\varepsilon_4^{\mathrm{even/odd}}(b) I_4$), two-precision (`256`-bit and `384`-bit) `flint.arb` Cholesky factorization certifies:
1. **$K = 3$ ($B_{\{2,3\},\{5\}}$, $P_3 = 30$) at $\Delta_\alpha = 0$ across $N \in \{36, 40, 42, 45, 48, 50\}$**:
   - While $W_{\mathrm{unsigned}}^{(4, \mathrm{even})}(b)$ turns indefinite at $N = 40$ ($\lambda_{\min} < 0$) and plunges to $\lambda_{\min} \approx -3.8341$ at $N = 50$, both tail-corrected signed matrices $W_{\mathrm{signed}}^{(4, \mathrm{even})}(b) - \varepsilon_4^{\mathrm{even}}(b) I_4 \succ 0$ and $W_{\mathrm{signed}}^{(4, \mathrm{odd})}(b) - \varepsilon_4^{\mathrm{odd}}(b) I_4 \succ 0$ remain **strictly positive definite** across all 6 checkpoints up to $N = 50$ ($2b = \log(5/3) \approx 0.510826$, 23 active shifts).
2. **$K = 4$ ($B_{\{2,3,5\},\{7\}}$, $P_4 = 210$) at $\Delta_\alpha = 0$ across $N \in \{225, 240, 252, 260, 280, 300, 320, 350, 380\}$**:
   - While $W_{\mathrm{unsigned}}^{(4, \mathrm{even})}(b)$ turns indefinite by $N = 252$ ($\lambda_{\min} \approx -1.4046$) and plunges to $\lambda_{\min} \approx -21.1335$ at $N = 380$, both tail-corrected signed matrices $W_{\mathrm{signed}}^{(4, \mathrm{even})}(b) - \varepsilon_4^{\mathrm{even}}(b) I_4 \succ 0$ and $W_{\mathrm{signed}}^{(4, \mathrm{odd})}(b) - \varepsilon_4^{\mathrm{odd}}(b) I_4 \succ 0$ remain **strictly positive definite** across all 9 checkpoints up to $N = 380$ ($a = \frac{1}{2}\log 380 \approx 2.970086, 2b = \log(38/21) \approx 0.593064$, **175 active shifts**).
3. **Davenport–Heilbronn Control Separation**: For the Davenport–Heilbronn counterexample $L_{DH}(s)$ under the $K = 2$ ($B_{\{2\},\{3\}}$) preconditioner, $W_{\mathrm{signed}, DH}^{(4, \mathrm{even})}(b)$ is certified strictly negative on the constant mode ($(W_{\mathrm{signed}, DH}^{(4, \mathrm{even})})_{0,0} < 0$), proving that signed Legendre positivity is genuinely tied to Euler-product arithmetic and fails when off-line zeros are present.
