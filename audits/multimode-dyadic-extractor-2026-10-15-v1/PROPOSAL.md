# PROPOSAL — Multi-Mode Jacobi–Stieltjes–Divisor Extractors in `NS-61` Hilbert Space, Loewner Bessel Matrix Inequality, and Specialist Brief v6 (2026-10-15, v1)

## Wall Check

- **Target walls**: `NB-GAIN` and `COEFF`.
- **Closest prior results**: `NS-61`, `NS-71`, `NS-72`, `NS-74`, `audits/codex-review-and-all-vector-extension-2026-10-15-v1/`, and `audits/coeff-specialist-brief-2026-10-15-v5.html`.
- **What changes in this audit**:
  1. **Complete Jacobi–Stieltjes–Divisor Hierarchy in $H_{0,0}^\nu([1, 2])$ ($\nu \in \{2, 3\}$)**:
     Proves that for every smoothness order $\nu \in \{2, 3\}$ and every mode index $m \ge 1$, the shifted Jacobi polynomial profile
     $$\widetilde{\psi}_\nu^{(m)}(u) := (u - 1)^\nu (2 - u)^\nu \widetilde{P}_m^{(\nu, \nu)}(2u - 3) \in H_0^\nu([1, 2])$$
     satisfies the mean-zero condition $\int_1^2 \widetilde{\psi}_\nu^{(m)}(u)\,du = 0$ **identically** by Jacobi orthogonality against $P_0^{(\nu, \nu)}(2u - 3) = 1$ with respect to the exact endpoint weight $(u - 1)^\nu(2 - u)^\nu = 2^{-2\nu}(1 - t^2)^\nu$. Note that for $\nu = 3, m = 1$, $\widetilde{\psi}_3^{(1)}(u) = (u - 1)^3(2 - u)^3(2u - 3)$ is the exact degree-7 profile $\widetilde{\psi}_7(u)$ of Specialist Briefs v3–v5.
  2. **Exact Linear-in-$N$ Rational Gram Matrix $G_{N, \nu}^{(K)} = N\,\widehat{\mathcal{G}}^{(\nu, K)}$ and Loewner Matrix Bessel Inequality**:
     Proves that for the $K$-mode Stieltjes–Divisor extractor family $\Lambda_{N, \nu}^{(m)}(x) := -\frac{d}{dx}\bigl(x(F_{N, \nu}^{(m)})'(x)\bigr)\mathbf{1}_{[1/(2N), 1/N]}(x)$ ($F_{N, \nu}^{(m)}(x) = \widetilde{\psi}_\nu^{(m)}(1/(Nx))$), the $K \times K$ full-space Gram matrix in $H = L^2(0, \infty; dx)$ scales **purely linearly in $N$** with an $N$-independent **exact rational** symmetric positive-definite matrix $\widehat{\mathcal{G}}^{(\nu, K)} \in \mathbb{Q}^{K \times K}$:
     $$G_{N, \nu}^{(K)} = N\,\widehat{\mathcal{G}}^{(\nu, K)}, \qquad \widehat{\mathcal{G}}_{j, k}^{(\nu, K)} = \int_1^2 u^2 \mathcal{D}\widetilde{\psi}_\nu^{(j)}(u)\,\mathcal{D}\widetilde{\psi}_\nu^{(k)}(u)\,du \in \mathbb{Q}, \qquad \mathcal{D}f(u) := \frac{d}{du}\bigl(u f'(u)\bigr).$$
     Proves unconditionally that the Schur-projected innovation Gram matrix $\widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)}$ satisfies the **Loewner matrix Bessel inequality**
     $$0 \prec \widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)} \preceq N\,\widehat{\mathcal{G}}^{(\nu, K)} \qquad (\forall\, K \le N - 2),$$
     generalizing the rank-1 unconditional proof of Open Target A to arbitrary finite subspace dimension $K$.
  3. **Exact Rational Cholesky $L D L^T$ Diagonalization and Sum-of-Squares Lower Bound**:
     Factors $\widehat{\mathcal{G}}^{(\nu, 4)} = L_\nu D_\nu L_\nu^T$ in exact rational arithmetic ($L_\nu \in \mathbb{Q}^{4 \times 4}$ unit lower-triangular, $D_\nu = \operatorname{diag}(d_{\nu, 1}, d_{\nu, 2}, d_{\nu, 3}, d_{\nu, 4}) \in \mathbb{Q}_{>0}^4$) so that the $\mathcal{D}$-orthogonalized polynomial profiles $\widetilde{\boldsymbol{\phi}}_\nu = L_\nu^{-1}\widetilde{\boldsymbol{\psi}}_\nu \in \mathbb{Q}[u]^4$ yield **mutually $H$-orthogonal** extractors for every $N \ge 2$, and the unconditional $K$-mode Bessel lower bound splits into an **exact diagonal sum of $K$ squares**:
     $$\Delta_N = E_N^{(2)} - E_{2N}^{(2)} \ge \mathcal{R}_{N, \nu}^{(K)} := \mathbf{M}_{N, \nu}^{(K)}(u, y)^T \bigl(\widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)}\bigr)^{-1} \mathbf{M}_{N, \nu}^{(K)}(u, y) \ge \mathcal{B}_{N, \nu}^{(K)} := \frac{1}{N}\sum_{k=1}^K \frac{\bigl|\widetilde{M}_{N, \nu}^{(k)}(u, y)\bigr|^2}{d_{\nu, k}}.$$
  4. **Resolution of the $N = 16$ Single-Mode Phase-Cancellation Dip and Specialist Brief v6**:
     Certifies in 384-bit `flint.arb` across $N \in \{4, 8, 16, 32, 64\}$ that at $N = 16$ — where the single odd mode $K = 1$ ($\widetilde{\psi}_3^{(1)} = \widetilde{\psi}_7$) experiences a near-orthogonality phase dip ($\mathcal{R}_{16, 3}^{(1)}/\Delta_{16} = 0.000265$, $\mathcal{B}_{16, 3}^{(1)}/\Delta_{16} = 0.000052$) because $(1 * \Delta c)(n)$ is predominantly even/quadrupolar — the 4-mode Jacobi–Stieltjes–Divisor basis ($K = 4$) increases the captured dyadic step gain by **$1,306.9\times$ (Rayleigh: $34.57\%$ of $\Delta_{16}$)** and **$1,339.9\times$ (Bessel: $6.97\%$ of $\Delta_{16}$)** in $H_{0,0}^3([1,2])$, and captures **$71.17\%$ of $\Delta_{16}$ (Rayleigh)** / **$7.21\%$ of $\Delta_{16}$ (Bessel)** in $H_{0,0}^2([1,2])$. At $N = 64$, $K = 4$ captures **$59.32\%$ of $\Delta_{64}$** in $H_{0,0}^3([1,2])$ and **$64.86\%$ of $\Delta_{64}$** in $H_{0,0}^2([1,2])$. Delivers the separately versioned `audits/coeff-specialist-brief-2026-10-15-v6.html` upgrading Open Target B to the phase-robust multi-mode $\ell^2$-condition.

## Mandatory Open-Status Disclosure

**RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
