# Derivation — Multi-Mode Jacobi–Stieltjes–Divisor Extractors in `NS-61` Hilbert Space, Loewner Matrix Bessel Inequality, and Specialist Brief v6 (2026-10-15, v1)

## Wall Check

- **Target walls**: `NB-GAIN` and `COEFF`.
- **Closest prior results**: `NS-61`, `NS-71`, `NS-72`, `NS-74`, `audits/codex-review-and-all-vector-extension-2026-10-15-v1/`, and `audits/coeff-specialist-brief-2026-10-15-v5.html`.
- **What changes in this derivation**:
  1. Constructs the complete Jacobi–Stieltjes–Divisor hierarchy $\widetilde{\psi}_\nu^{(m)}(u) := (u-1)^\nu(2-u)^\nu \widetilde{P}_m^{(\nu, \nu)}(2u-3)$ ($\nu \in \{2, 3\}, m \ge 1$) and proves that every mode $m \ge 1$ automatically satisfies the mean-zero condition $\int_1^2 \widetilde{\psi}_\nu^{(m)}(u)\,du = 0$ by orthogonality of the Jacobi polynomials $P_m^{(\nu, \nu)}$ to $P_0^{(\nu, \nu)} = 1$.
  2. Proves the exact linear-in-$N$ rational Gram matrix identity $G_{N, \nu}^{(K)} = N\,\widehat{\mathcal{G}}^{(\nu, K)}$ ($\widehat{\mathcal{G}}^{(\nu, K)} \in \mathbb{Q}^{K \times K}$), the unconditional Loewner matrix Bessel inequality $0 \prec \widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)} \preceq N\,\widehat{\mathcal{G}}^{(\nu, K)}$, and the exact rational Cholesky $L D L^T$ diagonalization $\widehat{\mathcal{G}}^{(\nu, K)} = L_\nu D_\nu L_\nu^T$ into a sum of $K$ non-negative squares.
  3. Certifies in 384-bit `flint.arb` across $N \in \{4, 8, 16, 32, 64\}$ that the 4-mode Jacobi–Stieltjes–Divisor basis completely resolves the $N = 16$ single-mode phase-cancellation dip (improving the captured dyadic step gain at $N = 16$ by **$1,306.9\times$ in Rayleigh** and **$1,339.9\times$ in Bessel** for $\nu = 3$, and capturing **$71.17\%$ of $\Delta_{16}$** for $\nu = 2$).
- **Mandatory Open-Status Disclosure**: **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

---

## 1. Theorem 1 (The Complete Jacobi–Stieltjes–Divisor Hierarchy in $H_{0,0}^\nu([1, 2])$)

### 1.1 Shifted Jacobi Polynomials and Automatic Mean-Zero Orthogonality

For each smoothness order $\nu \in \{2, 3\}$, consider the mean-zero Sobolev space on $[1, 2]$:
$$H_{0,0}^\nu([1, 2]) := \left\{ \widetilde{\psi} \in H^\nu([1, 2]) : \widetilde{\psi}^{(r)}(1) = \widetilde{\psi}^{(r)}(2) = 0 \;\;(0 \le r \le \nu - 1), \quad \int_1^2 \widetilde{\psi}(u)\,du = 0 \right\}.$$
Introduce the affine coordinate $t := 2u - 3 \in [-1, 1]$ ($u = \frac{t + 3}{2}, du = \frac{dt}{2}$), under which:
$$u - 1 = \frac{1 + t}{2}, \qquad 2 - u = \frac{1 - t}{2}, \qquad (u - 1)^\nu (2 - u)^\nu = 2^{-2\nu}(1 - t^2)^\nu.$$
Let $\widetilde{P}_m^{(\nu, \nu)}(t) \in \mathbb{Z}[t]$ ($m \ge 0$) denote the primitive integer-coefficient multiples of the symmetric Jacobi polynomials $P_m^{(\nu, \nu)}(t)$ orthogonal on $[-1, 1]$ with respect to the weight $w_{\nu, \nu}(t) := (1 - t^2)^\nu$:
- **For $\nu = 3$ ($H_{0,0}^3([1, 2])$)**:
  $$\widetilde{P}_1^{(3, 3)}(t) = t, \quad \widetilde{P}_2^{(3, 3)}(t) = 9t^2 - 1, \quad \widetilde{P}_3^{(3, 3)}(t) = t(11t^2 - 3), \quad \widetilde{P}_4^{(3, 3)}(t) = 143t^4 - 66t^2 + 3.$$
- **For $\nu = 2$ ($H_{0,0}^2([1, 2])$)**:
  $$\widetilde{P}_1^{(2, 2)}(t) = t, \quad \widetilde{P}_2^{(2, 2)}(t) = 7t^2 - 1, \quad \widetilde{P}_3^{(2, 2)}(t) = t(3t^2 - 1), \quad \widetilde{P}_4^{(2, 2)}(t) = 33t^4 - 18t^2 + 1.$$

**Theorem 1 (Jacobi–Stieltjes–Divisor Hierarchy & Multi-Mode Dual Identity).** *For each $\nu \in \{2, 3\}$ and each mode $m \ge 1$, define on $u \in [1, 2]$:*
$$\widetilde{\psi}_\nu^{(m)}(u) := (u - 1)^\nu (2 - u)^\nu \widetilde{P}_m^{(\nu, \nu)}(2u - 3).$$
*For each dyadic block size $N \ge 2$, set $F_{N, \nu}^{(m)}(x) := \widetilde{\psi}_\nu^{(m)}\!\left(\frac{1}{Nx}\right)\mathbf{1}_{[1/(2N), 1/N]}(x)$ and define the Stieltjes–Divisor extractor in $H = L^2(0, \infty; dx)$:*
$$\Lambda_{N, \nu}^{(m)}(x) := -\frac{d}{dx}\!\left(x\,\bigl(F_{N, \nu}^{(m)}\bigr)'(x)\right)\mathbf{1}_{[1/(2N), 1/N]}(x).$$
*Then:*
1. *(Automatic Mean-Zero Property for All $m \ge 1$):* *Every $\widetilde{\psi}_\nu^{(m)}$ ($m \ge 1$) belongs to $H_{0,0}^\nu([1, 2])$. In particular, because $\widetilde{P}_0^{(\nu, \nu)}(t) = 1$ and $(u-1)^\nu(2-u)^\nu = 2^{-2\nu}(1-t^2)^\nu$ is the exact Jacobi weight for $\widetilde{P}_m^{(\nu, \nu)}(t)$, orthogonality of $\widetilde{P}_m^{(\nu, \nu)}$ to $\widetilde{P}_0^{(\nu, \nu)}$ on $[-1, 1]$ yields:*
   $$\int_1^2 \widetilde{\psi}_\nu^{(m)}(u)\,du = 2^{-(2\nu + 1)} \int_{-1}^1 (1 - t^2)^\nu \widetilde{P}_m^{(\nu, \nu)}(t)\,\widetilde{P}_0^{(\nu, \nu)}(t)\,dt = 0 \qquad (\forall\, m \ge 1).$$
   *For $\nu = 3, m = 1$, $\widetilde{\psi}_3^{(1)}(u) = (u-1)^3(2-u)^3(2u-3)$ coincides with the degree-7 profile $\widetilde{\psi}_7(u)$ of Specialist Briefs v3–v5.*
2. *(Exact Multi-Mode Divisor-Sum Moments):* *For every $N \ge 2$ and every $m \ge 1$, $\langle \Lambda_{N, \nu}^{(m)}, \tau \rangle_H = 0$, and for every atom $\sigma_r(x) = A(1/(rx))$ ($r \ge 1$):*
   $$\langle \Lambda_{N, \nu}^{(m)}, \sigma_r \rangle_H = +\sum_{\substack{k \ge 1 \\ N < kr < 2N}} \widetilde{\psi}_\nu^{(m)}\!\left(\frac{kr}{N}\right).$$
   *Consequently, with $\lambda_{\mathrm{new}, \nu, n}^{(m)} := \widetilde{\psi}_\nu^{(m)}(n/N)$ ($N < n \le 2N$), $\lambda_{\mathrm{old}, \nu, d}^{(m)} := \sum_{k \ge 2,\, N < kd < 2N} \widetilde{\psi}_\nu^{(m)}(kd/N)$ ($1 \le d \le N$), and $\tilde{\lambda}_{\mathrm{proj}, \nu}^{(m)} := \lambda_{\mathrm{new}, \nu}^{(m)} - (C^{(2)})^T (G^{(2)})^{-1}\lambda_{\mathrm{old}, \nu}^{(m)}$, the $m$-th mode pairing satisfies the exact three-way identity:*
   $$M_{N, \nu}^{(m)}(u, y) := \langle \Lambda_{N, \nu}^{(m)}, r_N - r_{2N} \rangle_H = \bigl(\tilde{\lambda}_{\mathrm{proj}, \nu}^{(m)}\bigr)^T y = \bigl(\lambda_{\mathrm{new}, \nu}^{(m)}\bigr)^T y + \bigl(\lambda_{\mathrm{old}, \nu}^{(m)}\bigr)^T u = \sum_{n=N+1}^{2N-1} \widetilde{\psi}_\nu^{(m)}\!\left(\frac{n}{N}\right)\left(y_n + \sum_{\substack{d \mid n \\ d \le N}} u_d\right).$$

*Proof.* Statement (1) is immediate from the orthogonality relation $\int_{-1}^1 (1-t^2)^\nu P_m^{(\nu,\nu)}(t)P_0^{(\nu,\nu)}(t)\,dt = 0$ for all $m \ge 1$. For Statement (2), since $[1/(2N), 1/N] \subset (0, 1)$ where $\tau(x) = -\log x$ satisfies $(x\tau'(x))' = (-1)' = 0$ and $F_{N, \nu}^{(m)}, (F_{N, \nu}^{(m)})'$ vanish at the endpoints $1/(2N)$ and $1/N$, two integrations by parts give $\langle \Lambda_{N, \nu}^{(m)}, \tau \rangle_H = 0$. Similarly, since $\sigma_r'(x) = -\rho_r(x)/x = -\frac{1}{rx^2} + \frac{1}{x}\lfloor\frac{1}{rx}\rfloor$ and
$$\int_{1/(2N)}^{1/N} \frac{(F_{N, \nu}^{(m)})'(x)}{x}\,dx = \int_1^2 u\,\bigl(\widetilde{\psi}_\nu^{(m)}\bigr)'(u)\,du = \Bigl[u\,\widetilde{\psi}_\nu^{(m)}(u)\Bigr]_1^2 - \int_1^2 \widetilde{\psi}_\nu^{(m)}(u)\,du = 0,$$
integrating by parts twice yields $\langle \Lambda_{N, \nu}^{(m)}, \sigma_r \rangle_H = \int_{1/(2N)}^{1/N} (F_{N, \nu}^{(m)})'(x)\lfloor\frac{1}{rx}\rfloor\,dx = \sum_{N < kr < 2N} \widetilde{\psi}_\nu^{(m)}(kr/N)$. $\square$

---

## 2. Theorem 2 (Exact Linear-in-$N$ Rational Gram Matrix, Loewner Bessel Inequality, and Exact $L D L^T$ Diagonalization)

**Theorem 2 (Multi-Mode Loewner Bessel Inequality & Exact Rational Diagonalization).** *Fix $\nu \in \{2, 3\}$ and $K \ge 1$, and define the scale-invariant differential operator $\mathcal{D}f(u) := \frac{d}{du}\bigl(u f'(u)\bigr)$ on $[1, 2]$. Then:*
1. *(Exact Linear-in-$N$ Rational Gram Matrix):* *Under $u = \frac{1}{Nx} \in [1, 2]$ ($dx = \frac{du}{N u^2}$), $\Lambda_{N, \nu}^{(m)}(x) = -N u^2 \mathcal{D}\widetilde{\psi}_\nu^{(m)}(u)\mathbf{1}_{[1, 2]}(u)$, so the $K \times K$ full-space Gram matrix in $H = L^2(0, \infty; dx)$ scales purely linearly in $N$:*
   $$G_{N, \nu}^{(K)} := \left[\langle \Lambda_{N, \nu}^{(j)}, \Lambda_{N, \nu}^{(k)} \rangle_H\right]_{1 \le j, k \le K} = N\,\widehat{\mathcal{G}}^{(\nu, K)}, \qquad \widehat{\mathcal{G}}_{j, k}^{(\nu, K)} := \int_1^2 u^2 \mathcal{D}\widetilde{\psi}_\nu^{(j)}(u)\,\mathcal{D}\widetilde{\psi}_\nu^{(k)}(u)\,du \in \mathbb{Q}.$$
   *For $K = 4$, the exact $4 \times 4$ rational Gram matrices $\widehat{\mathcal{G}}^{(3, 4)}$ and $\widehat{\mathcal{G}}^{(2, 4)}$ are:*
   $$\widehat{\mathcal{G}}^{(3, 4)} = \begin{pmatrix} \frac{6904}{45045} & \frac{1424}{5005} & -\frac{70222}{255255} & -\frac{26256}{17017} \\[4pt] \frac{1424}{5005} & \frac{64256}{12155} & \frac{21696}{17017} & -\frac{12923744}{969969} \\[4pt] -\frac{70222}{255255} & \frac{21696}{17017} & \frac{5129856}{1616615} & \frac{363776}{46189} \\[4pt] -\frac{26256}{17017} & -\frac{12923744}{969969} & \frac{363776}{46189} & \frac{597629440}{2909907} \end{pmatrix},$$
   $$\widehat{\mathcal{G}}^{(2, 4)} = \begin{pmatrix} \frac{4462}{1155} & \frac{4288}{385} & \frac{4038}{5005} & \frac{2000}{3003} \\[4pt] \frac{4288}{385} & \frac{49256}{455} & \frac{17740}{1001} & \frac{42464}{1365} \\[4pt] \frac{4038}{5005} & \frac{17740}{1001} & \frac{147824}{15015} & \frac{84224}{2145} \\[4pt] \frac{2000}{3003} & \frac{42464}{1365} & \frac{84224}{2145} & \frac{5303296}{9945} \end{pmatrix}.$$
2. *(Unconditional Loewner Matrix Bessel Inequality — Multi-Mode Proof of Target A):* *Let $\widetilde{\Lambda}_{\mathrm{proj}, N, \nu}^{(K)} := [\tilde{\lambda}_{\mathrm{proj}, \nu}^{(1)}, \dots, \tilde{\lambda}_{\mathrm{proj}, \nu}^{(K)}] \in \mathbb{R}^{N \times K}$ and let*
   $$\widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)} := \bigl(\widetilde{\Lambda}_{\mathrm{proj}, N, \nu}^{(K)}\bigr)^T \bigl(S^{(2)}\bigr)^{-1} \widetilde{\Lambda}_{\mathrm{proj}, N, \nu}^{(K)} = \left[\langle (\Pi_{2N} - \Pi_N)\Lambda_{N, \nu}^{(j)}, (\Pi_{2N} - \Pi_N)\Lambda_{N, \nu}^{(k)} \rangle_H\right]_{1 \le j, k \le K}$$
   *be the Schur-projected Gram matrix on the innovation subspace $\mathcal{W}_N = \operatorname{Ran}(\Pi_{2N} - \Pi_N)$. Since $\Pi_{2N} - \Pi_N$ is an orthogonal projection in $H$, for every $\mathbf{a} \in \mathbb{R}^K$:*
   $$\mathbf{a}^T \widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)} \mathbf{a} = \left\|(\Pi_{2N} - \Pi_N)\sum_{k=1}^K a_k \Lambda_{N, \nu}^{(k)}\right\|_H^2 \le \left\|\sum_{k=1}^K a_k \Lambda_{N, \nu}^{(k)}\right\|_H^2 = N\,\mathbf{a}^T \widehat{\mathcal{G}}^{(\nu, K)} \mathbf{a},$$
   *so for every $1 \le K \le N - 2$, in the Loewner positive-definite ordering:*
   $$0 \prec \widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)} \preceq N\,\widehat{\mathcal{G}}^{(\nu, K)}, \qquad \bigl(\widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)}\bigr)^{-1} \succeq \frac{1}{N}\bigl(\widehat{\mathcal{G}}^{(\nu, K)}\bigr)^{-1}.$$
3. *(Exact Rational Cholesky $L D L^T$ Diagonalization & Sum-of-Squares Lower Bound):* *Let $\widehat{\mathcal{G}}^{(\nu, K)} = L_\nu D_\nu L_\nu^T$ be the exact rational Cholesky factorization ($L_\nu \in \mathbb{Q}^{K \times K}$ unit lower-triangular, $D_\nu = \operatorname{diag}(d_{\nu, 1}, \dots, d_{\nu, K}) \in \mathbb{Q}_{>0}^K$), and define the $\mathcal{D}$-orthogonal polynomial profiles $\widetilde{\boldsymbol{\phi}}_\nu := L_\nu^{-1}\widetilde{\boldsymbol{\psi}}_\nu \in \mathbb{Q}[u]^K$, with exact rational diagonal norms:*
   - *For $\nu = 3$ ($H_{0,0}^3([1, 2])$):*
     $$d_{3, 1} = \frac{6904}{45045} \approx 0.153269, \quad d_{3, 2} = \frac{69877856}{14685671} \approx 4.758234, \quad d_{3, 3} = \frac{54811238229308}{27278622628075} \approx 2.009311, \quad d_{3, 4} = \frac{74321698811043079500}{588658995773210593} \approx 126.255947,$$
     *with $\widetilde{\phi}_3^{(1)}(u) = \widetilde{\psi}_3^{(1)}(u)$ and $\widetilde{\phi}_3^{(2)}(u) = \widetilde{\psi}_3^{(2)}(u) - \frac{1602}{863}\widetilde{\psi}_3^{(1)}(u)$.*
   - *For $\nu = 2$ ($H_{0,0}^2([1, 2])$):*
     $$d_{2, 1} = \frac{4462}{1155} \approx 3.863203, \quad d_{2, 2} = \frac{850246088}{11166155} \approx 76.144930, \quad d_{2, 3} = \frac{136163193922736}{20745473143395} \approx 6.563514, \quad d_{2, 4} = \frac{13972789817205142528}{39495836437213611} \approx 353.778805,$$
     *with $\widetilde{\phi}_2^{(1)}(u) = \widetilde{\psi}_2^{(1)}(u)$ and $\widetilde{\phi}_2^{(2)}(u) = \widetilde{\psi}_2^{(2)}(u) - \frac{6432}{2231}\widetilde{\psi}_2^{(1)}(u)$.*
   *Setting $\widetilde{M}_{N, \nu}^{(k)}(u, y) := \sum_{n=N+1}^{2N-1} \widetilde{\phi}_\nu^{(k)}\!\left(\frac{n}{N}\right)(1 * \Delta c)(n)$, the dyadic step gain $\Delta_N = E_N^{(2)} - E_{2N}^{(2)}$ satisfies the unconditional chain:*
   $$\Delta_N \ge \mathcal{R}_{N, \nu}^{(K)} := \mathbf{M}_{N, \nu}^{(K)}(u, y)^T \bigl(\widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)}\bigr)^{-1} \mathbf{M}_{N, \nu}^{(K)}(u, y) \ge \mathcal{B}_{N, \nu}^{(K)} := \frac{1}{N}\sum_{k=1}^K \frac{\bigl|\widetilde{M}_{N, \nu}^{(k)}(u, y)\bigr|^2}{d_{\nu, k}}. \qquad \square$$

---

## 3. 384-Bit `flint.arb` Certification Across $N \in \{4, 8, 16, 32, 64\}$ and Resolution of the $N = 16$ Dip

All values below are certified in 384-bit `flint.arb` (`verify_multimode_extractor.py`, `verification.json` `sha256=51fb88c333ade4176f9472734e2fe941070c0b7514721ecae7d800a06475d8be`, completed in $14.038\text{ s}$ with `all_certified=True`):

### 3.1 Original `NS-61` Target ($\beta = 1/2$, $F_{1/2} = 0$) — $H_{0,0}^3([1, 2])$ vs. $H_{0,0}^2([1, 2])$

| $N$ | $K_{\max}$ | $\Delta_N / E_N^{(2)}$ | $H_{0,0}^3$: $K=1$ $\mathcal{R}^{(1)}/\Delta_N$ | $H_{0,0}^3$: $K=K_{\max}$ $\mathcal{R}^{(K)}/\Delta_N$ | $H_{0,0}^3$: $K=1$ $\mathcal{B}^{(1)}/\Delta_N$ | $H_{0,0}^3$: $K=K_{\max}$ $\mathcal{B}^{(K)}/\Delta_N$ | $H_{0,0}^3$ $\mathcal{B}^{(K)}/\mathcal{B}^{(1)}$ Gain | $H_{0,0}^2$: $K=K_{\max}$ $\mathcal{R}^{(K)}/\Delta_N$ | $H_{0,0}^2$: $K=K_{\max}$ $\mathcal{B}^{(K)}/\Delta_N$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $4$ | $2$ | $0.948768$ | $0.004753$ | $0.010708$ | $0.001115$ | $0.002466$ | **$2.21\times$** | $0.009083$ | $0.002950$ |
| $8$ | $4$ | $0.707195$ | $0.011190$ | $0.146327$ | $0.004052$ | $0.028919$ | **$7.14\times$** | $0.124059$ | $0.026454$ |
| $16$ | $4$ | $0.237285$ | $0.000265$ | **$0.345673$** | $0.000052$ | **$0.069726$** | **$1,339.92\times$** | **$0.711665$** | **$0.072069$** |
| $32$ | $4$ | $0.189128$ | $0.052369$ | $0.114424$ | $0.005758$ | $0.012181$ | **$2.12\times$** | $0.288576$ | $0.026334$ |
| $64$ | $4$ | $0.165203$ | $0.310292$ | **$0.593245$** | $0.025680$ | **$0.037616$** | **$1.46\times$** | **$0.648639$** | **$0.038345$** |

### 3.2 Structural Explanation of the $N = 16$ Phenomenon

At $N = 16$, the interior dyadic integers $n \in \{17, \dots, 31\}$ carry a divisor-difference profile $(1 * \Delta c)(n)$ whose odd component around the midpoint $n = 24$ ($u = 3/2$) nearly cancels, causing the single odd mode $\widetilde{\psi}_3^{(1)} = \widetilde{\psi}_7$ ($K = 1$) to drop to $\mathcal{R}_{16, 3}^{(1)}/\Delta_{16} = 2.65 \times 10^{-4}$ and $\mathcal{B}_{16, 3}^{(1)}/\Delta_{16} = 5.20 \times 10^{-5}$. When the orthogonalized even modes ($m = 2, 4$) and second odd mode ($m = 3$) are adjoined ($K = 4$):
- In $H_{0,0}^3([1, 2])$, $\mathcal{R}_{16, 3}^{(4)}/\Delta_{16}$ jumps to **$0.345673$ ($1,306.9\times$ gain)** and $\mathcal{B}_{16, 3}^{(4)}/\Delta_{16}$ jumps to **$0.069726$ ($1,339.9\times$ gain)**.
- In $H_{0,0}^2([1, 2])$, $\mathcal{R}_{16, 2}^{(4)}/\Delta_{16}$ reaches **$0.711665$ ($71.17\%$ of the entire dyadic step gain $\Delta_{16}$)** and $\mathcal{B}_{16, 2}^{(4)}/\Delta_{16}$ reaches **$0.072069$**.
- Across all blocks $N \in \{8, 16, 32, 64\}$, the 4-mode unconditional Bessel bound $\mathcal{B}_{N, 2}^{(4)}/\Delta_N$ stays uniformly in $[2.63\%, 7.21\%]$ of $\Delta_N$ without any phase-cancellation dip.

---

## Closing Wall Check & Mandatory Open-Status Disclosure

- **Wall check**: `NB-GAIN` and `COEFF`. Closest prior results: `NS-61`, `NS-71`, `NS-72`, `NS-74`, `audits/codex-review-and-all-vector-extension-2026-10-15-v1/`, and `audits/coeff-specialist-brief-2026-10-15-v5.html`.
- **Scope Qualification (`NS-74` & Pre-Computation Assessment)**: Theorem 1 and Theorem 2 establish exact algebraic duality identities and Bessel Gram bounds on the innovation subspace $\operatorname{Ran}(\Pi_{2N}-\Pi_N)$. Because $M_{N,\nu}^{(m)}(u,y)$ depends on the solved inverse-Gram increments $\Delta c = c_{2N}-c_N$ and acts identically on the removable component $P_{\mathcal{T}}(U_\beta^*\tau)$ of the `NS-74` unitary Blaschke control, these finite-block capture ratios ($N \le 64$) do **not** provide an unconditional cofinal lower bound on $\Delta_N / E_N^{(2)}$ (see [`nb-full-residual-arithmetic-assessment-2026-10-16-v1.html`](../nb-full-residual-arithmetic-assessment-2026-10-16-v1.html)).
- **Open-Status Disclosure**: **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
