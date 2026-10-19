# Mathematical Derivations — Next Four Steps (`KERNEL-API` `flint.arb` Certificate, `NB-GAIN` / `COEFF` Stieltjes–Divisor Identity vs. `NS-74`, and `ZERO-GEOMETRY` Single-Point Wronskian Obstruction)

**Date:** 2026-10-15 (Version 1)
**Worktree:** `/Users/alex/riemann-worktrees/origin-main-review` (branch `codex/four-lane-audit-20261014`)
**Wall check:** Closest results: `NS-57` / `NS-92` (`KERNEL-API`), `NS-61` / `NS-71` / `NS-72` / `NS-74` (`NB-GAIN` / `COEFF`), and `NS-98` / `NS-101` (`ZERO-GEOMETRY`). What changes:
1. In `KERNEL-API`, upgrades both the **All-Vector Positivity Floor** on the Three-Island window $\log 2 < a \le \frac{1}{2}\log 5$ ($q[L_2 g] \ge [0.92182853\dots]\,\|g\|_2^2 = [0.28363954\dots]\,\|L_2 g\|_2^2 > 0$ for all $g \in V_{a-\log 2}$) and the **2-Mode Even Interior Separation of `NS-57`** at $a = \log 3$ ($\det M_{\mathrm{orig}}(\log 3) > 0 > \det M_{\mathrm{NS57}}(\log 3)$ and rational witness $g_\star = g_1^+ + \frac{3}{25}g_2^+$) to 256-bit rigorous `flint.arb` / `flint.acb.integral` interval-arithmetic ball enclosures.
2. In `NB-GAIN` / `COEFF`, proves an **Exact Stieltjes–Divisor Dual Identity** in the `NS-61` Hilbert space $H = L^2(0,\infty;dx)$ for compactly supported smooth extractors $\Lambda_b(x) = \frac{d}{dx}(x F_b'(x))\mathbf{1}_{[1/(2N), 1/N]}(x)$ ($F_b(x) = \widetilde{\psi}(1/(Nx))$, $\widetilde{\psi} \in H_0^2([1,2])$, $\int_1^2 \widetilde{\psi}(u)\,du = 0$), showing that $M_N(u,y) = \tilde{\lambda}_{\mathrm{proj}}^T (S^{(2)})^{-1} h^{(2)} = \lambda_{\mathrm{new}}^T y + \lambda_{\mathrm{old}}^T u = \sum_{n=N+1}^{2N-1} \widetilde{\psi}(n/N)(1 * \Delta c)(n)$ with unconditional Bessel bound $\|(\Pi_{2N}-\Pi_N)\Lambda_b\|_H^2 \le C_{\widetilde{\psi}} N^3$, and proves the **Exact Orthogonal Decomposition of `NS-74`** ($U_\beta^*\tau = P_{\mathcal{T}}(U_\beta^*\tau) \oplus \tau_\beta^\perp$) explaining the 256-bit `flint.arb` diagnostic across $N \in \{4, 8, 16, 32, 64\}$.
3. In `ZERO-GEOMETRY`, proves in the jet ring $\mathbb{Q}[\phi,\phi',\phi'',\phi''']$ that single-point denominator clearing of $\phi(u)^2$ in $P_1(u)$ or $\phi(u)^3$ in $\mathcal{J}_{\mathrm{PS}}(u)$ produces a vertical-line frequency convolution ($\int_{\mathbb{R}} 4\phi(u)^2 P_1(u)e^{2xu}\,du = -\frac{1}{\pi}\int_{\mathbb{R}}\tau^2|f(x+i\tau)|^2\,d\tau < 0$) and cubic normal form $8\phi^3\mathcal{J}_{\mathrm{PS}} = (\frac{1}{3}\partial_u^3 - \frac{8c_1}{3}\partial_u^2 + \frac{4c_2}{3}\partial_u + 8c_3)(\phi^3) + \frac{3}{2}\partial_u((\phi')^2\phi) - \frac{19}{2}(\phi')^3$, which have identical signs on RH-true kernels and on `NS-101` / `Davenport–Heilbronn`.
- **Open-status disclosure:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

---

## Part 1 (`KERNEL-API`): 256-Bit `flint.arb` Certificate for the Three-Island All-Vector Floor and `NS-57` Separation at $a = \log 3$

### 1.1 Theorem 1A (All-Vector Coercivity on the Three-Island Window $\log 2 < a \le \frac{1}{2}\log 5$)

Let $\ell_2 = \log 2$, $r_2 = 2^{-1/2}$, and
$$L_2 := \frac{3}{2}I - \frac{1}{\sqrt{2}}(T_{\ell_2} + T_{-\ell_2}) : V_{a-\ell_2} \longrightarrow V_a, \qquad b := a - \ell_2 > 0,$$
with Fourier multiplier $\sigma(L_2)(\xi) = \frac{3}{2} - \sqrt{2}\cos(\xi\log 2) \in [\frac{3}{2}-\sqrt{2}, \frac{3}{2}+\sqrt{2}]$.

**Theorem 1A.** *For every $\log 2 < a \le \frac{1}{2}\log 5$ (so $0 < b = a - \log 2 \le \frac{1}{2}\log(5/4) \approx 0.111571775657105 < \frac{1}{2}\log 2$) and every $g \in V_b = L^2(-b, b)$:*
1. *(Exact Three-Island Isometric Norm Identity):* *Because $2b \le \log(5/4) < \log 2$, the three supports $[-b, b]$, $[\ell_2 - b, \ell_2 + b]$, and $[-\ell_2 - b, -\ell_2 + b]$ of $g, T_{\ell_2}g, T_{-\ell_2}g$ are pairwise disjoint, so*
   $$\|L_2 g\|_{L^2(-a,a)}^2 = \left(\frac{9}{4} + \frac{1}{2} + \frac{1}{2}\right)\|g\|_{L^2(-b,b)}^2 = \frac{13}{4}\|g\|_{L^2(-b,b)}^2.$$
2. *(Exact Three-Island Prime Identity):* *All odd prime powers $q^m \ge 3$ and all non-zero shifts $\pm \ell_2, \pm 2\ell_2$ miss the open autocorrelation support $(-2b, 2b)$ (since $\log 3 - 2\ell_2 = \log(3/4) < -\log(5/4) \le -2b$ and $\log 5 - 2\ell_2 = \log(5/4) \ge 2b$), yielding*
   $$q_{\mathrm{prime}}[L_2 g] = -(\log 2)\left\langle \left(\frac{1}{2}L_2 - L_2^2\right)g, g \right\rangle = \frac{5\log 2}{2}\|g\|_{L^2(-b,b)}^2.$$
3. *(Certified All-Vector Archimedean Lower Bound):* *Let $\alpha(\xi) := \operatorname{Re}\psi(\frac{1}{4} + \frac{i\xi}{2}) - \log\pi$. Since $\alpha'(\xi) > 0$ for $\xi > 0$, $\alpha(0) = -\gamma - 2\log 2 - \frac{3}{2}\log\pi < 0$, and $\alpha(\xi) \to +\infty$, $\alpha$ has a unique positive root $\xi_0 > 0$. Setting*
   $$I_{\mathrm{neg}} := \int_0^{\xi_0} (-\alpha(\xi))\,\sigma(L_2)(\xi)^2\,d\xi, \qquad C_{\mathrm{low}} := \frac{2}{\pi}I_{\mathrm{neg}},$$
   *every $g \in V_b$ satisfies $|\widehat{g}(\xi)|^2 \le 2b\,\|g\|_{L^2(-b,b)}^2$ by Cauchy–Schwarz, so*
   $$q_{\mathrm{arch}}[L_2 g] = \int_{-\infty}^{\infty} \alpha(\xi)\sigma(L_2)(\xi)^2|\widehat{g}(\xi)|^2\,\frac{d\xi}{2\pi} \ge -\frac{1}{\pi}\int_0^{\xi_0} (-\alpha(\xi))\sigma(L_2)(\xi)^2(2b\|g\|_2^2)\,d\xi = -C_{\mathrm{low}}\,b\,\|g\|_{L^2(-b,b)}^2.$$
4. *(256-Bit `flint.arb` Enclosure):* *Rigorous interval bisection and `flint.acb.integral` certify:*
   $$\begin{aligned}
   \xi_0 &\in [6.28983598883690277966509010082 \pm 1.86\times 10^{-30}], \\
   I_{\mathrm{neg}} &\in [11.4184589828592816234524254312 \pm 3.79\times 10^{-29}], \\
   C_{\mathrm{low}} &\in [7.26921675845644026397839556004 \pm 1.63\times 10^{-30}].
   \end{aligned}$$
   *Consequently, for every $\log 2 < a \le \frac{1}{2}\log 5$ and every non-zero $g \in V_{a-\log 2}$ ($f = L_2 g \in V_a$):*
   $$\begin{aligned}
   q[L_2 g] &\ge \left(\frac{5\log 2}{2} - C_{\mathrm{low}}(a - \log 2)\right)\|g\|_{L^2(-b,b)}^2 \\
   &\ge [0.921828530022494182737893324410 \pm 3.17\times 10^{-31}]\,\|g\|_{L^2(-b,b)}^2 \\
   &= [0.283639547699228979303967176742 \pm 3.65\times 10^{-31}]\,\|L_2 g\|_{L^2(-a,a)}^2 > 0. \qquad \square
   \end{aligned}$$

---

### 1.2 Theorem 1B (256-Bit `flint.arb` Separation of `NS-57` at $a = \log 3$)

Let $g_j^+(x) = b^{-1/2}\cos(w_j x)\mathbf{1}_{[-b,b]}(x)$ ($w_j = \frac{(2j-1)\pi}{2b}$, $j \in \{1, 2\}$) be the first two orthonormal even Dirichlet modes on $[-b, b]$.

**Lemma 1.1 (Proved Plancherel Short-Interval Bound near $t = 0$).** *For any $j, k \in \{1, 2\}$, let $c_t(t) := \frac{1}{2}\langle (T_t + T_{-t})L_2 g_j^+, L_2 g_k^+ \rangle$ and $c_0 := c_t(0)$. For every $\varepsilon > 0$:*
$$\left|\int_0^\varepsilon \frac{e^{t/2}}{\sinh t}\left(c_0 - c_t(t)\right) dt\right| \le \frac{1}{4}\left(\frac{3}{2} + \sqrt{2}\right)^2 w_j w_k e^{\varepsilon/2}\,\varepsilon^2.$$
*Proof.* By Plancherel and $2(1 - \cos(\xi t)) = 4\sin^2(\xi t/2) \le \xi^2 t^2$,
$$|c_0 - c_t(t)| = \frac{1}{2}\left|\int_{\mathbb{R}} 2(1 - \cos(\xi t))\sigma(L_2)(\xi)^2 \widehat{g_j^+}(\xi)\overline{\widehat{g_k^+}(\xi)}\,\frac{d\xi}{2\pi}\right| \le \frac{t^2}{2}\left(\frac{3}{2}+\sqrt{2}\right)^2 \|(g_j^+)'\|_2 \|(g_k^+)'\|_2 = \frac{t^2}{2}\left(\frac{3}{2}+\sqrt{2}\right)^2 w_j w_k.$$
Since $0 < \frac{e^{t/2}}{\sinh t} \le \frac{e^{t/2}}{t} \le \frac{e^{\varepsilon/2}}{t}$ on $(0, \varepsilon]$, integrating $\int_0^\varepsilon t\,dt = \frac{1}{2}\varepsilon^2$ gives the stated bound. $\square$

On $[\varepsilon, 2a]$ ($\varepsilon = 2^{-60}$), the breakpoints where $|\pm t + s_\tau| \in \{0, 2b\}$ ($s_\tau \in \{0, \pm \ell_2, \pm 2\ell_2\}$) partition $[\varepsilon, 2a]$ into finitely many open subintervals on each of which $c_t(t)$ is an entire trigonometric expression enclosed by `flint.acb.integral`.

**Theorem 1B (`flint.arb` Separation Certificate at $a = \log 3$).** *At $a = \log 3$ ($b = \log(3/2)$), the $2\times 2$ even interior Rayleigh matrices $M_{\mathrm{orig}}(\log 3)$ and $M_{\mathrm{NS57}}(\log 3)$ ($\delta_2 = -\frac{\log 2}{100}$) satisfy the 256-bit `flint.arb` enclosures:*
$$\begin{aligned}
M_{\mathrm{orig}}(\log 3)_{11} &\in [0.05730481539705892939448536 \pm 1.98\times 10^{-28}], \\
M_{\mathrm{orig}}(\log 3)_{12} &\in [-0.4548638317890171561586411 \pm 1.45\times 10^{-26}], \\
M_{\mathrm{orig}}(\log 3)_{22} &\in [3.764083291490190045952996 \pm 1.36\times 10^{-25}], \\
\det M_{\mathrm{orig}}(\log 3) &\in [+0.008798992688212002396305839 \pm 1.29\times 10^{-28}] > 0, \\
\det M_{\mathrm{NS57}}(\log 3) &\in [-0.1019772783625828702627252 \pm 1.87\times 10^{-26}] < 0.
\end{aligned}$$
*Moreover, for the explicit rational combination $g_\star := g_1^+ + \frac{3}{25}g_2^+ \in H_0^1(-\log(3/2), \log(3/2))$, $f_\star := L_2 g_\star \in H_0^1(-\log 3, \log 3)$ satisfies:*
$$\begin{aligned}
q_{\mathrm{orig}}[f_\star] &\in [+0.002340295165153548578134644 \pm 3.87\times 10^{-28}] > 0, \\
\widetilde{q}_{\mathrm{NS57}}[f_\star] &\in [-0.02726145566330497541025701 \pm 4.68\times 10^{-27}] < 0. \qquad \square
\end{aligned}$$

---

## Part 2 (`NB-GAIN` / `COEFF`): Exact Stieltjes–Divisor Dual Identity in `NS-61` Hilbert Space and `NS-74` Orthogonal-Splitting Diagnostic

### 2.1 Theorem 2A (Exact Stieltjes–Divisor Dual Identity in $H = L^2(0,\infty;dx)$)

In `NS-61` (`evidence/v159/ns61/proof.tex`), $H = L^2(0,\infty;dx)$, $\sigma_r(x) = (J\rho_r)(x) = A(1/(rx))$ where $A(z) = \int_0^z \frac{\{v\}}{v}\,dv$, and $\tau(x) = (-\log x)\mathbf{1}_{(0,1)}(x)$. Since $A'(z) = \frac{\{z\}}{z}$, $\sigma_r$ is continuous on $(0, \infty)$ with weak derivative
$$\sigma_r'(x) = -\frac{\rho_r(x)}{x} = -\frac{1}{rx^2} + \frac{1}{x}\left\lfloor\frac{1}{rx}\right\rfloor.$$

**Theorem 2A (Stieltjes–Divisor Dual Extractor Identity).** *Let $\widetilde{\psi} \in H_0^2([1, 2])$ be any polynomial or $H^2$ profile satisfying $\widetilde{\psi}(1) = \widetilde{\psi}'(1) = \widetilde{\psi}(2) = \widetilde{\psi}'(2) = 0$ and $\int_1^2 \widetilde{\psi}(u)\,du = 0$. For each $N \ge 2$, set $F_b(x) := \widetilde{\psi}\!\left(\frac{1}{Nx}\right)\mathbf{1}_{[1/(2N), 1/N]}(x) \in H_0^2([1/(2N), 1/N])$ and define the compactly supported extractor*
$$\Lambda_b(x) := \frac{d}{dx}\!\left(x F_b'(x)\right)\mathbf{1}_{[1/(2N), 1/N]}(x) \in H = L^2(0,\infty;dx).$$
*Then:*
1. *(Exact $H$-Norm and Unconditional Bessel Bound):* *Substituting $u = \frac{1}{Nx} \in [1, 2]$ gives*
   $$\|\Lambda_b\|_H^2 = \int_{1/(2N)}^{1/N} \left|\frac{d}{dx}\!\left(x F_b'(x)\right)\right|^2 dx = C_{\widetilde{\psi}}\,N^3, \qquad C_{\widetilde{\psi}} := \int_1^2 u^2 \left|\frac{d}{du}\!\left(u^2 \widetilde{\psi}'(u)\right)\right|^2 du.$$
   *For the degree-5 profile $\widetilde{\psi}_5(u) = (u-1)^2(2-u)^2(u-\frac{3}{2})$ and the Specialist Brief v3 degree-7 profile $\widetilde{\psi}_7(u) = (u-1)^3(2-u)^3(2u-3)$:*
   $$C_{\widetilde{\psi}_5} = \frac{46183}{15015} \approx 3.07579088, \qquad C_{\widetilde{\psi}_7} = \frac{5132}{12155} \approx 0.42221308.$$
2. *(Target Orthogonality on $(0,1)$):* *For any function $f_0(x) = \alpha(-\log x) + \beta$ linear in $\log x$ on $[1/(2N), 1/N]$ (including both $\tau(x) = -\log x$ and the interior part $U_\beta^*\tau|_{(0,1)} = b_\beta(-\log x) - c_\beta$ of `NS-74`), $\langle \Lambda_b, f_0 \rangle_H = 0$.*
3. *(Exact Rational Atom Moments):* *Integrating by parts twice on $[1/(2N), 1/N]$ and using $\int_{1/(2N)}^{1/N} \frac{F_b'(x)}{x}\,dx = \int_{1/(2N)}^{1/N} \frac{F_b(x)}{x^2}\,dx = N\int_1^2 \widetilde{\psi}(u)\,du = 0$ yields:*
   $$\langle \Lambda_b, \sigma_r \rangle_H = \int_{1/(2N)}^{1/N} F_b'(x)\rho_r(x)\,dx = -\int_{1/(2N)}^{1/N} F_b'(x)\left\lfloor\frac{1}{rx}\right\rfloor dx = \sum_{\substack{k \ge 1 \\ N < kr < 2N}} \widetilde{\psi}\!\left(\frac{kr}{N}\right).$$
   *In particular, on the new block $n \in \{N+1, \dots, 2N\}$ and old block $m \in \{1, \dots, N\}$:*
   $$\lambda_{\mathrm{new}, n} = \widetilde{\psi}\!\left(\frac{n}{N}\right) \quad (N < n < 2N), \quad \lambda_{\mathrm{new}, 2N} = 0, \qquad \lambda_{\mathrm{old}, m} = \sum_{\substack{k \ge 2 \\ N < km < 2N}} \widetilde{\psi}\!\left(\frac{km}{N}\right).$$
4. *(Three-Way Exact Identity for $M_N(u, y)$ and Unconditional Cauchy–Schwarz Bound):* *Let $G^{(2)}, C^{(2)}, D^{(2)}, S^{(2)}$ be the exact `NS-61` Gram and Schur matrices on $W_{2N}$, $c^{(N)} = (G^{(2)})^{-1}b_{\mathrm{old}}^{(2)}$, $h^{(2)} = b_{\mathrm{new}}^{(2)} - (C^{(2)})^T c^{(N)}$, $y = (S^{(2)})^{-1}h^{(2)}$, $u = -(G^{(2)})^{-1}C^{(2)}y$, and $\tilde{\lambda}_{\mathrm{proj}} := \lambda_{\mathrm{new}} - (C^{(2)})^T (G^{(2)})^{-1}\lambda_{\mathrm{old}}$. Then:*
   $$M_N(u, y) := \tilde{\lambda}_{\mathrm{proj}}^T (S^{(2)})^{-1} h^{(2)} = \lambda_{\mathrm{new}}^T y + \lambda_{\mathrm{old}}^T u = \sum_{n=N+1}^{2N-1} \widetilde{\psi}\!\left(\frac{n}{N}\right)\left(y_n + \sum_{\substack{m \mid n \\ 1 \le m \le N}} u_m\right) = \sum_{n=N+1}^{2N-1} \widetilde{\psi}\!\left(\frac{n}{N}\right)(1 * \Delta c)(n),$$
   *and by Bessel's inequality for the orthogonal projection $\Pi_{2N} - \Pi_N$ in $H$:*
   $$\tilde{\lambda}_{\mathrm{proj}}^T (S^{(2)})^{-1} \tilde{\lambda}_{\mathrm{proj}} = \|(\Pi_{2N} - \Pi_N)\Lambda_b\|_H^2 \le \|\Lambda_b\|_H^2 = C_{\widetilde{\psi}}\,N^3,$$
   $$\Delta_N = E_N^{(2)} - E_{2N}^{(2)} = (h^{(2)})^T (S^{(2)})^{-1} h^{(2)} \ge \frac{M_N(u,y)^2}{\tilde{\lambda}_{\mathrm{proj}}^T (S^{(2)})^{-1} \tilde{\lambda}_{\mathrm{proj}}} \ge \frac{M_N(u,y)^2}{C_{\widetilde{\psi}}\,N^3}. \qquad \square$$

---

### 2.2 Theorem 2B (Orthogonal Splitting of `NS-74` and Why Relative-to-$\Delta_N$ Efficiency Cannot Certify $E_N^{(2)} \to 0$)

**Theorem 2B (Exact Orthogonal Decomposition of the `NS-74` Altered Target).** *Let $\mathcal{T} = L^2(0,1) \oplus \operatorname{span}\{x^{-1}\mathbf{1}_{x>1}\} \subset H$ be the closed `NS-61` tail space containing all atoms $\sigma_n$ ($n \ge 1$). For any $\beta \in (\frac{1}{2}, 1)$, the `NS-74` altered target $U_\beta^*\tau$ decomposes orthogonally in $H = L^2(0,\infty;dx)$ as*
$$U_\beta^*\tau = P_{\mathcal{T}}(U_\beta^*\tau) \oplus \tau_\beta^\perp,$$
*where:*
1. $\tau_\beta^\perp(x) := -c_\beta\left(x^{-\beta} - \frac{1}{\beta}x^{-1}\right)\mathbf{1}_{x > 1}$ *satisfies $\tau_\beta^\perp \perp \mathcal{T}$ (and hence $\langle \tau_\beta^\perp, \sigma_n \rangle_H = 0$ for all $n \ge 1$) with squared norm*
   $$\|\tau_\beta^\perp\|_H^2 = c_\beta^2\left(\frac{1}{2\beta-1} - \frac{1}{\beta^2}\right) = \frac{(2\beta-1)(1-\beta)^2}{\beta^6} = F_\beta > 0.$$
2. *The in-space component $P_{\mathcal{T}}(U_\beta^*\tau)(x) = \left(b_\beta(-\log x) - c_\beta\right)\mathbf{1}_{(0,1)}(x) - \frac{c_\beta}{\beta}x^{-1}\mathbf{1}_{x>1} \in \mathcal{T}$ has squared norm $\|P_{\mathcal{T}}(U_\beta^*\tau)\|_H^2 = 2 - F_\beta$ and generates the entire load sequence $b_n^{(\beta)} = \langle U_\beta^*\tau, \sigma_n \rangle_H = \langle P_{\mathcal{T}}(U_\beta^*\tau), \sigma_n \rangle_H$.*
3. *Consequently, at every block size $N$, the solved coefficients $c^{(N)}(\beta), c^{(2N)}(\beta), u(\beta), y(\beta)$, the dyadic gain $\Delta_N(\beta) = E_N^{(2)}(\beta) - E_{2N}^{(2)}(\beta)$, and the Stieltjes–Divisor pairing $M_N(u(\beta), y(\beta))$ depend solely on $P_{\mathcal{T}}(U_\beta^*\tau)$, whereas the total residual energy splits as*
   $$E_N^{(2)}(\beta) = \underbrace{\left\|P_{\mathcal{T}}(U_\beta^*\tau) - \Pi_N(P_{\mathcal{T}}(U_\beta^*\tau))\right\|_H^2}_{=: E_{N,\mathrm{rem}}^{(2)}(\beta)} + F_\beta.$$
   *Therefore, any finite-block or asymptotic bound comparing $M_N(u,y)^2$ only to $\Delta_N$ or to the removable error $E_{N,\mathrm{rem}}^{(2)}$ holds identically for `NS-74`, whereas comparing $M_N(u,y)^2$ to the unsplit energy $E_N^{(2)} = 2 - (b_{\mathrm{old}}^{(2)})^T c^{(N)}$ requires $\tau_\beta^\perp = 0$ ($F_\beta = 0$) and separates the original family from `NS-74` as soon as $E_{N,\mathrm{rem}}^{(2)}(\beta) \ll F_\beta$.* $\square$

---

## Part 3 (`ZERO-GEOMETRY`): Single-Point Wronskian & Cubic Integrating-Factor Obstruction

### 3.1 Theorem 3A (Single-Point Quadratic Wronskian Parseval Identity)

**Theorem 3A (Gauge-Invariant Single-Point Wronskian Transform).** *Let $\phi : \mathbb{R} \to \mathbb{R}$ be any smooth rapidly decaying kernel with strip Laplace transform $f(z) = \int_{\mathbb{R}}\phi(u)e^{zu}\,du$, and let $P_1(u) = \frac{1}{4}(\log\phi)''(u) = \frac{\phi''(u)\phi(u) - (\phi'(u))^2}{4\phi(u)^2}$. Clear the quadratic denominator $\phi(u)^2$ at the single coordinate $u$ by forming the Wronskian*
$$W_2[\phi](u) := 4\phi(u)^2 P_1(u) = \phi''(u)\phi(u) - (\phi'(u))^2.$$
*Then for every $z \in \mathbb{C}$, putting $\psi_z(u) := \phi(u)e^{zu}$:*
1. *(Exact Gauge Invariance):* *Because $(\log(\phi(u)e^{zu}))'' = (\log\phi)''(u)$,*
   $$W_2[\phi](u)e^{2zu} = \psi_z''(u)\psi_z(u) - (\psi_z'(u))^2 = \frac{d}{du}\!\left(\psi_z'(u)\psi_z(u)\right) - 2(\psi_z'(u))^2.$$
2. *(Vertical-Line Convolution Identity):* *Integrating over $u \in \mathbb{R}$ gives*
   $$\int_{-\infty}^{\infty} 4\phi(u)^2 P_1(u)\,e^{2zu}\,du = -2\int_{-\infty}^{\infty} (\psi_z'(u))^2\,du = -\frac{1}{\pi}\int_{-\infty}^{\infty} \tau^2 f(z + i\tau)f(z - i\tau)\,d\tau.$$
3. *(Strict Negativity on Real Slices for All Kernels):* *At every real argument $z = x \in \mathbb{R}$, since $\psi_x(u) = \phi(u)e^{xu}$ is real-valued and $\overline{f(x+i\tau)} = f(x-i\tau)$:*
   $$\int_{-\infty}^{\infty} 4\phi(u)^2 P_1(u)\,e^{2xu}\,du = -2\int_{-\infty}^{\infty} \left|(\phi(u)e^{xu})'\right|^2 du = -\frac{1}{\pi}\int_{-\infty}^{\infty} \tau^2 |f(x + i\tau)|^2\,d\tau < 0$$
   *for every non-zero real kernel $\phi$, regardless of whether $f(z)$ satisfies RH or has off-line zeros (including `NS-101` and `Davenport–Heilbronn`).* $\square$

---

### 3.2 Theorem 3B (Cubic Jet-Ring Normal Form of $8\phi(u)^3\mathcal{J}_{\mathrm{PS}}(u)$)

**Theorem 3B (Cubic Integrating-Factor Normal Form).** *In the jet ring $\mathbb{Q}[c_1,c_2,c_3][\phi,\phi',\phi'',\phi''']$, multiplying the Planat–Solé Jacobi polynomial*
$$\mathcal{J}_{\mathrm{PS}}(P_0,P_1,P_2) = P_2 + 12 P_0 P_1 + 4 P_0^3 - 4c_1 P_1 - 12c_1 P_0^2 + c_2 P_0 + c_3$$
*by the minimal single-point denominator-clearing factor $8\phi(u)^3$ yields the exact decomposition:*
$$8\phi(u)^3\mathcal{J}_{\mathrm{PS}}(u) = \left(\frac{1}{3}\frac{d^3}{du^3} - \frac{8c_1}{3}\frac{d^2}{du^2} + \frac{4c_2}{3}\frac{d}{du} + 8c_3\right)\!\left(\phi(u)^3\right) + \frac{3}{2}\frac{d}{du}\!\left((\phi'(u))^2\phi(u)\right) - \frac{19}{2}(\phi'(u))^3.$$
*Proof.* Direct expansion in $\mathbb{Q}[\phi,\phi',\phi'',\phi''']$ gives:
- $(\phi^3)' = 3\phi'\phi^2$, $(\phi^3)'' = 3\phi''\phi^2 + 6(\phi')^2\phi = 3\phi^3(D_2 + 2D_1^2) = 12\phi^3(P_1 + 3P_0^2)$, so $-\frac{8c_1}{3}(\phi^3)'' = 8\phi^3(-4c_1 P_1 - 12c_1 P_0^2)$ and $\frac{4c_2}{3}(\phi^3)' = 8\phi^3(c_2 P_0)$.
- $(\phi^3)''' = 3\phi'''\phi^2 + 18\phi'\phi''\phi + 6(\phi')^3$ and $((\phi')^2\phi)' = 2\phi'\phi''\phi + (\phi')^3$, so
  $$\frac{1}{3}(\phi^3)''' + \frac{3}{2}((\phi')^2\phi)' - \frac{19}{2}(\phi')^3 = \phi'''\phi^2 + (6+3)\phi'\phi''\phi + \left(2 + \frac{3}{2} - \frac{19}{2}\right)(\phi')^3 = \phi'''\phi^2 + 9\phi'\phi''\phi - 6(\phi')^3 = 8\phi^3(P_2 + 12P_0 P_1 + 4P_0^3).$$
Because $\phi(u)^3$ transforms to the 3-fold frequency convolution $(f * f * f)(z)$ and $-\frac{19}{2}(\phi'(u))^3$ is an irreducible cubic non-divergence remainder, clearing $\phi(u)^3$ at a single coordinate $u$ never factors through pointwise evaluations of $f(z)$. $\square$
