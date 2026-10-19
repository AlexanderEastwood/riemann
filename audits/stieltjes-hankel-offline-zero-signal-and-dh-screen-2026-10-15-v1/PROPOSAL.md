# PROPOSAL — Milestone 12: Ordinate-Centered Stieltjes–Hankel Parity Separation & Davenport–Heilbronn Off-Line Zero Screen (`ZERO-GEOMETRY`)

**Date:** 2026-10-15  
**Target Lane:** `ZERO-GEOMETRY` (Stieltjes–Hankel Moment Positivity & Off-Line Zero Dipole Detection)  
**Audit Directory:** `audits/stieltjes-hankel-offline-zero-signal-and-dh-screen-2026-10-15-v1/`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this deliverable prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.
>
> **Why this milestone moves us closer to RH (not smaller bounds):**  
> In earlier `ZERO-GEOMETRY` audits (`audits/zero-geometry-hilbert-hankel-2026-10-15-v1/`), the real-axis Stieltjes–Hankel kernel $(k + j + 1)^{-1} = \int_0^\infty e^{-(k+j+1)y}\,dy$ centered at $t_0 = 0$ exhibited rapid exponential damping $e^{-\pi\gamma_n / 2}$ with zero height $\gamma_n$, making high-ordinate off-line zeros invisible from $t_0 = 0$.
>
> This milestone resolves that geometric obstruction by proving the **Ordinate-Centered Stieltjes–Hankel Parity Separation & Cauchy–Binet Off-Line Zero Dipole Theorem** at general ordinate $t_0 \in \mathbb{R}$, and certifying in 256-bit and 384-bit `flint.arb` / `flint.acb` ball arithmetic that centering at $t_0 = \gamma_{DH} \approx 85.6993484854$ (the first off-line zero ordinate of Davenport–Heilbronn $f_{DH}(s)$) produces an exponentially amplified, strictly negative $2 \times 2$ and $3 \times 3$ Hankel dipole signature on $f_{DH}(s)$ while remaining strictly positive definite on Riemann $\zeta(s)$ across $t_0 \in [14, 90]$.

---

## Theorems & Technical Scope

1. **Theorem 1 (Ordinate-Centered Stieltjes–Hankel Parity Separation & Cauchy–Binet Off-Line Zero Dipole Theorem):**
   - For any complex frequency spectrum $\{\xi_\rho\}$ where $\xi_\rho = -i(\rho - 1/2) = \gamma - i(\beta - 1/2)$ satisfies functional-equation conjugate symmetry ($\xi_\rho \leftrightarrow \overline{\xi_\rho}$), define the ordinate-centered Gaussian-regularized Stieltjes–Hankel moments at ordinate $t_0 \in \mathbb{R}$ and window scale $\sigma > 0$:
     $$\mu_m^{(\sigma)}(t_0) := \sum_{\rho} (\xi_\rho - t_0)^m\,e^{-\frac{1}{2}\sigma^2(\xi_\rho - t_0)^2}, \qquad \bigl(H_N^{(\sigma)}(t_0)\bigr)_{j, k} := \mu_{j+k}^{(\sigma)}(t_0) \quad (0 \le j, k \le N - 1).$$
   - **(On-Line Hamburger Positivity):** If all zeros lie on the critical line ($\beta = 1/2$, $\xi_\rho = \gamma \in \mathbb{R}$), then for every $t_0 \in \mathbb{R}$, $\sigma > 0$, and $N \ge 1$, $H_N^{(\sigma)}(t_0) \succeq 0$ is real symmetric positive semi-definite (and strictly positive definite whenever $\ge N$ distinct ordinates exist), with $\mu_{2r}^{(\sigma)}(t_0) > 0$ and $\det H_k^{(\sigma)}(t_0) > 0$ for all $1 \le k \le N$.
   - **(Off-Line Dipole Negativity & Cauchy–Binet Minor Identity):** If an off-line zero twin pair $\rho_{\star, \pm} = \frac{1}{2} \pm \delta_\star + i\gamma_\star$ ($\delta_\star = \beta_\star - 1/2 > 0$) exists at ordinate $\gamma_\star$, then at $t_0 = \gamma_\star$ we have $\xi_{\star, \pm} - \gamma_\star = \mp i\delta_\star \in i\mathbb{R}\setminus\{0\}$, so:
     1. Its Gaussian weight is **exponentially amplified** by $e^{+\frac{1}{2}\sigma^2\delta_\star^2} > 1$ while every neighboring on-line zero at distance $|\gamma_n - \gamma_\star| \ge \Delta\gamma$ is **exponentially suppressed** by $e^{-\frac{1}{2}\sigma^2(\Delta\gamma)^2} < 1$.
     2. Its even moments alternate in sign: $\mu_{2r, \mathrm{pair}}^{(\sigma)}(\gamma_\star) = 2(-1)^r \delta_\star^{2r} e^{+\frac{1}{2}\sigma^2\delta_\star^2}$, yielding a strictly negative dipole contribution $-2\delta_\star^2 e^{+\frac{1}{2}\sigma^2\delta_\star^2} < 0$ to $\mu_2^{(\sigma)}(\gamma_\star) = (H_N^{(\sigma)}(\gamma_\star))_{1,1}$.
     3. By the Cauchy–Binet formula $\det H_2^{(\sigma)}(t_0) = \sum_{a < b} w_a(t_0) w_b(t_0)(\xi_a - \xi_b)^2$, every pair of on-line zeros contributes $w_m w_n (\gamma_m - \gamma_n)^2 \ge 0$, whereas the off-line twin pair has $\xi_{\star,+} - \xi_{\star,-} = -2i\delta_\star$ and contributes the **strictly negative intrinsic dipole minor**
        $$w_{\star,+}(t_0) w_{\star,-}(t_0)(\xi_{\star,+} - \xi_{\star,-})^2 = -4\,\delta_\star^2\,e^{-\sigma^2((\gamma_\star - t_0)^2 - \delta_\star^2)} < 0.$$
2. **Theorem 2 (100-Digit Complex Interval Newton Isolation of $\rho_{DH, \pm}$ & Certified Stieltjes–Hankel Screen Separating $\zeta(s)$ from $f_{DH}(s)$):**
   - Using 384-bit and 256-bit `flint.acb_series` Hurwitz zeta jets (`ss.zeta(c_j)`) and the Complex Interval Newton Theorem, isolates and certifies the first off-line zero pair $\rho_{DH, \pm} = \frac{1}{2} \pm \delta_{DH} + i\gamma_{DH}$ of Davenport–Heilbronn $f_{DH}(s)$ inside complex balls of radius $10^{-65}$ (256-bit) and $10^{-100}$ (384-bit), together with neighboring on-line zeros of $f_{DH}(s)$ and Riemann $\zeta(s)$.
   - Certifies in pure ball arithmetic that at $t_0 = \gamma_{DH} \approx 85.6993484854$ across $\sigma \in \{1.5, 2.0, 2.5, 3.0\}$, the Davenport–Heilbronn Hankel matrix violates positivity ($\mu_{2, DH}^{(\sigma)}(\gamma_{DH}) < 0$, $\det H_{2, DH}^{(\sigma)}(\gamma_{DH}) < 0$, and $\lambda_{\min}(H_{3, DH}^{(\sigma)}(\gamma_{DH})) < 0$), whereas for Riemann $\zeta(s)$ both at $t_0 = \gamma_{DH}$ and across the first 25 Riemann zero ordinates $\gamma_1, \dots, \gamma_{25}$, $H_{3, \zeta}^{(\sigma)}(t_0) \succ 0$ is strictly positive definite (certified by exact Cholesky factorization in `flint.arb`).

---

## Deliverables & Acceptance Criteria

1. **`derivation.md`**: Complete self-contained proofs of Theorems 1 and 2.
2. **`verify_stieltjes_hankel_offline_screen.py`**: Two-precision (`256` and `384` bits) `flint.arb` / `flint.acb` certificate script (`pyright` clean).
3. **`verification.json`**: Machine-readable audit payload with canonical `payload.sha256` and `file_sha256`.
4. **`README.md`** and versioned HTML report `audits/stieltjes-hankel-offline-zero-signal-and-dh-screen-2026-10-15-v1.html`.
