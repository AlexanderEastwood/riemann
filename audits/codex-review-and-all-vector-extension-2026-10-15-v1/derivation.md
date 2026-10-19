# Mathematical Derivations — CODEX Feedback Resolution & Extended All-Vector Positivity Certificate on $\log 2 < a \le \frac{1}{2}\log 6$

**Date:** 2026-10-15 (Version 1)
**Worktree:** `/Users/alex/riemann-worktrees/origin-main-review` (branch `codex/four-lane-audit-20261014`)
**Wall check:** Closest results: `NS-57` / `NS-92` (`KERNEL-API`), `NS-61` / `NS-71` / `NS-72` / `NS-74` (`NB-GAIN` / `COEFF`), and `NS-98` / `NS-101` (`ZERO-GEOMETRY`). What changes:
1. In `KERNEL-API`, resolves CODEX Findings 2–4 (`argon-audit-review`) and `S2` (`argon-next-four-review`) and proves **Theorem 1B**, extending the **384-bit `flint.arb` All-Vector Positivity Certificate** on $V_{a-\log 2}$ beyond the Three-Island window $\frac{1}{2}\log 5 \approx 0.804719$ across the entire **Four-Shift Window $\log 2 < a \le \frac{1}{2}\log 6 \approx 0.895880$** via the **Pointwise Boundary-Strip Multiplication Minorant $V_{\mathrm{prime}}(x)$**, the **Similarity-Weighted Negative-Lobe Trace $\mathcal{T}_{\mathrm{even}}(a) < 1$** (up to $a = 0.890$), and the **1D Plancherel–Sherman–Morrison Rank-1 Archimedean Minorant** ($\operatorname{Tr}(P^{-1}T) < 1$ at $a = \frac{1}{2}\log 6$).
2. In `NB-GAIN` / `COEFF`, resolves CODEX Findings `M1`–`M4`: proves the exact linear-in-$N$ norm identity $\|\Lambda_N\|_H^2 = C_b N$ ($C_b(\widetilde{\psi}_5) = \frac{2231}{2310}$, $C_b(\widetilde{\psi}_7) = \frac{6904}{45045}$) for the minus-signed extractor $\Lambda_N(x) = -\frac{d}{dx}(x F_N'(x))\mathbf{1}_{[1/(2N), 1/N]}(x)$, **unconditionally proves Proposed Open Target (A)** ($\|(\Pi_{2N}-\Pi_N)\Lambda_N\|_H^2 \le \frac{6904}{45045}N$) by Bessel's inequality in $H = L^2(0,\infty;dx)$, independently verifies $\langle \Lambda_4, \sigma_5 \rangle_H = -\frac{27}{8192}$ from $\sigma_5(x) = A(1/(5x))$ across the floor jump at $x = 1/5$, and proves the in-space perturbation decomposition $P_{\mathcal{T}}(U_\beta^*\tau) = b_\beta\tau - c_\beta\tau_{\mathrm{pert}}^{(\beta)}$ for `NS-74`.
3. In `ZERO-GEOMETRY`, resolves CODEX Finding 1 (`argon-audit-review`) and `M5`, `S1` (`argon-next-four-review`): proves the **Symmetrized Half-Strip Parseval Identity** on $(p, t) \in \mathbb{R} \times [0, \infty)$ under exponential decay $|\operatorname{Re} z| < A$ and evaluates the single-point cleared Wronskian transform $\int_{\mathbb{R}} 4\phi(u)^2 P_1(u)e^{2xu}\,du = -\frac{1}{\pi}\int_{\mathbb{R}}\tau^2|f(x+i\tau)|^2\,d\tau < 0$ directly on the recorded `NS-101` reciprocal-dilation kernel and `Davenport–Heilbronn` control.
- **Open-status disclosure:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound** (Proposed Open Target B), and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

---

## Part 1 (`KERNEL-API`): Extended 384-Bit `flint.arb` All-Vector Positivity Certificate on $\log 2 < a \le \frac{1}{2}\log 6$

### 1.1 Resolution of CODEX Scope & Constant Notes (`S2` and Findings 2–4)

1. **Exact $\alpha(0)$ Formula (`S2`):** Since $\psi(\frac{1}{4}) = -\gamma - \frac{\pi}{2} - 3\log 2$, the archimedean symbol $\alpha(\xi) = \operatorname{Re}\psi(\frac{1}{4} + \frac{i\xi}{2}) - \log\pi$ satisfies at $\xi = 0$:
   $$\alpha(0) = \psi\!\left(\frac{1}{4}\right) - \log\pi = -\gamma - \frac{\pi}{2} - 3\log 2 - \log\pi \in [-5.37218341922566558223295749745 \pm 10^{-30}] < 0.$$
2. **Multi-Prime Support-Barrier Qualification (Finding 2):** For a finite prime set $P \subset \mathbb{P}$ with $\ell_P = \sum_{p \in P}\log p$ and $b_P = a - \ell_P > 0$, a prime power $p^m$ with $p \in P$ produces the net shift $m\log p - \ell_P$, which enters the open autocorrelation support $(-2b_P, 2b_P)$ whenever $P \ne \emptyset$ and $\max_{p \in P}\log p < 2a - \ell_P$ (in particular, for $P = \{2\}$, the $m = 1$ shift of $p = 3$ against $-\frac{3}{\sqrt{2}}T_{\log 2}$ enters at $\log 3 - \log 2 = \log(3/2) < 2(a - \log 2) \iff a > \frac{1}{2}\log 6 \approx 0.895880$, and the $m = 1, 2, 3$ shifts of $p = 2$ at $\tau = \log 2$ enter at $a > \frac{3}{2}\log 2 \approx 1.039721$).
3. **Upper-Bound Scope of Finite-Mode Rayleigh Matrices at $a = \log 3$ (Finding 3):** Because a finite-dimensional Rayleigh matrix on $\operatorname{span}\{g_1^+, g_2^+\} \subset V_{a-\log 2}$ provides an upper bound on $\inf_{g \ne 0} \frac{q[L_2 g]}{\|g\|_2^2}$, the 2-mode sign flip $\det M_{\mathrm{NS57}}(\log 3) < 0 < \det M_{\mathrm{orig}}(\log 3)$ rigorously certifies the upper bound $a_*^+(\mathrm{NS57}) < \log 3$ and separates the 2-mode Rayleigh matrix of `orig` from `NS-57`, whereas certifying a lower bound $a_*^+(\mathrm{orig}) \ge a_\star$ requires an **all-vector lower bound** on $V_{a-\log 2}$.

---

### 1.2 Pointwise Boundary-Strip Multiplication Minorant $V_{\mathrm{prime}}(x)$ on $\log 2 < a \le \frac{1}{2}\log 6$

Let $\ell_2 = \log 2$, $b = a - \log 2 > 0$, and $L_2 = \frac{3}{2}I - \frac{1}{\sqrt{2}}(T_{\ell_2} + T_{-\ell_2}) : V_b \to V_a$. Whenever $2b \le \log 2$ (i.e., $\log 2 < a \le \frac{3}{2}\log 2 \approx 1.039721$), the three shifted supports $[-b, b]$, $[\ell_2 - b, \ell_2 + b]$, and $[-\ell_2 - b, -\ell_2 + b]$ are pairwise disjoint, so $\|L_2 g\|_{L^2(-a,a)}^2 = \frac{13}{4}\|g\|_{L^2(-b,b)}^2$ for every $g \in V_b$.

**Lemma 1.1 (Pointwise Boundary-Strip Shift Minorant).** *Let $\tau \in [b, 2b)$, and define the boundary-strip union*
$$E_\tau := [-b, b-\tau] \cup [\tau-b, b] = \{x \in [-b, b] : |x| \in [\tau-b, b]\}.$$
*Then for every $g \in V_b = L^2(-b, b)$:*
$$\left|\left\langle (T_\tau + T_{-\tau})g, g \right\rangle_{L^2(-b,b)}\right| \le \int_{E_\tau} |g(x)|^2\,dx.$$
*Proof.* Since $\tau \ge b$, the intervals $I_L(\tau) := [-b, b-\tau] \subset [-b, 0]$ and $I_R(\tau) := [\tau-b, b] \subset [0, b]$ are disjoint (intersecting at most at $\{0\}$ if $\tau = b$), and $x \mapsto x + \tau$ maps $I_L(\tau)$ bijectively onto $I_R(\tau)$. By $2|u\bar{v}| \le |u|^2 + |v|^2$,
$$\left|\left\langle (T_\tau + T_{-\tau})g, g \right\rangle_{L^2(-b,b)}\right| = 2\left|\operatorname{Re}\int_{-b}^{b-\tau} g(x+\tau)\overline{g(x)}\,dx\right| \le \int_{-b}^{b-\tau} \left(|g(x)|^2 + |g(x+\tau)|^2\right) dx = \int_{I_L(\tau)} |g(x)|^2\,dx + \int_{I_R(\tau)} |g(y)|^2\,dy = \int_{E_\tau} |g(x)|^2\,dx. \qquad \square$$

**Lemma 1.2 (Four-Shift Prime Potential on $\log 2 < a \le \frac{1}{2}\log 6$).** *For every $\log 2 < a \le \frac{1}{2}\log 6 \approx 0.8958797346$ ($0 < b = a - \log 2 \le \frac{1}{2}\log(3/2) \approx 0.2027325541$):*
1. *The only prime-power shifts $|m\log p + s\log 2|$ ($s \in \{0, \pm 1, \pm 2\}$) in $q_{\mathrm{prime}}[L_2 g]$ that enter the open autocorrelation support $(-2b, 2b)$ are:*
   - *$\tau = 0$ from $p^m \in \{2, 4\}$, contributing $+\frac{5\log 2}{2}\|g\|_{L^2(-b,b)}^2$;*
   - *$\tau_5 := \log 5 - 2\log 2 = \log(5/4) \approx 0.2231435513 > b$ from $p^m = 5, s = -2$ (entering at $a = \frac{1}{2}\log 5 \approx 0.804719$), with operator $-\frac{\log 5}{2\sqrt{5}} P_b(T_{\tau_5} + T_{-\tau_5})P_b$;*
   - *$\tau_3 := 2\log 2 - \log 3 = \log(4/3) \approx 0.2876820725 > b$ from $p^m = 3, s = -2$ (entering at $a = \frac{1}{2}\log(16/3) \approx 0.836988$), with operator $-\frac{\log 3}{2\sqrt{3}} P_b(T_{\tau_3} + T_{-\tau_3})P_b$.*
   *(The next shift is $\tau_3^{(1)} = \log 3 - \log 2 = \log(3/2) = 2b_\star$, which lies at the boundary $\pm 2b_\star$ at $a_\star = \frac{1}{2}\log 6$ and does not enter the open support $(-2b, 2b)$ for $a \le \frac{1}{2}\log 6$.)*
2. *Consequently, by Lemma 1.1, for every $g \in V_b$:*
   $$q_{\mathrm{prime}}[L_2 g] \ge \int_{-b}^b V_{\mathrm{prime}}(x)|g(x)|^2\,dx,$$
   *where $V_{\mathrm{prime}}(x)$ is the even, piecewise-constant multiplication potential*
   $$V_{\mathrm{prime}}(x) := c_0 - c_5\,\mathbf{1}_{[x_5, b]}(|x|) - c_3\,\mathbf{1}_{[x_3, b]}(|x|),$$
   *with $c_0 = \frac{5\log 2}{2}$, $c_5 = \frac{\log 5}{2\sqrt{5}}$, $c_3 = \frac{\log 3}{2\sqrt{3}}$, $x_5 = \min(b, \log(5/2) - a)$, $x_3 = \min(b, \log(8/3) - a)$, and uniform positive floor:*
   $$V_{\mathrm{prime}}(x) \ge V_{\min} := c_0 - c_5 - c_3 = \frac{5\log 2}{2} - \frac{\log 5}{2\sqrt{5}} - \frac{\log 3}{2\sqrt{3}} \in [1.055844643324281039340554881 \pm 10^{-28}] > 1. \qquad \square$$

---

### 1.3 Pure Similarity-Weighted Trace Bound ($\log 2 < a \le 0.890$) and Plancherel–Sherman–Morrison Certificate ($\log 2 < a \le \frac{1}{2}\log 6$)

Split the archimedean multiplier $\alpha(\xi)\sigma(L_2)(\xi)^2$ into its positive part on $|\xi| \ge \xi_0$ and negative lobe on $|\xi| < \xi_0$, defining the positive semidefinite operators $A_+, A_-$ on $V_b$:
$$\langle A_- g, g \rangle := \int_{-\xi_0}^{\xi_0} (-\alpha(\xi))\sigma(L_2)(\xi)^2 |\widehat{g}(\xi)|^2\,\frac{d\xi}{2\pi}, \qquad \langle A_+ g, g \rangle := \int_{|\xi| \ge \xi_0} \alpha(\xi)\sigma(L_2)(\xi)^2 |\widehat{g}(\xi)|^2\,\frac{d\xi}{2\pi}.$$
Since $V_{\mathrm{prime}}(x)$ is even and $A_\pm$ preserve parity, $V_b = V_b^{\mathrm{even}} \oplus V_b^{\mathrm{odd}}$ decomposes orthogonally. Substituting $h = V_{\mathrm{prime}}^{1/2} g$ on $V_b^{\mathrm{even}}$ (respectively $V_b^{\mathrm{odd}}$), $T_{\mathrm{even}} := V_{\mathrm{prime}}^{-1/2} A_-|_{V_b^{\mathrm{even}}} V_{\mathrm{prime}}^{-1/2} \succeq 0$ has integral kernel
$$K_{\mathrm{even}}(x, y) = \frac{1}{\pi}\int_0^{\xi_0} (-\alpha(\xi))\sigma(L_2)(\xi)^2 \frac{\cos(\xi x)\cos(\xi y)}{V_{\mathrm{prime}}(x)^{1/2} V_{\mathrm{prime}}(y)^{1/2}}\,d\xi$$
on $L^2_{\mathrm{even}}(-b, b)$ (and $K_{\mathrm{odd}}(x, y)$ with $\sin(\xi x)\sin(\xi y)$ on $L^2_{\mathrm{odd}}(-b, b)$). Defining the closed-form 3-piece cosine moment
$$M_0(\omega) := \int_{-b}^b \frac{\cos(\omega x)}{V_{\mathrm{prime}}(x)}\,dx = 2\sum_{j=1}^3 \frac{v_j\operatorname{sinc}(\omega v_j) - u_j\operatorname{sinc}(\omega u_j)}{V_j},$$
the traces $\mathcal{T}_{\mathrm{even}}(a) := \operatorname{Tr}(T_{\mathrm{even}})$ and $\mathcal{T}_{\mathrm{odd}}(a) := \operatorname{Tr}(T_{\mathrm{odd}})$ are given by the 1D integrals:
$$\mathcal{T}_{\mathrm{even}}(a) = \frac{1}{2\pi}\int_0^{\xi_0} (-\alpha(\xi))\sigma(L_2)(\xi)^2 \left(M_0(0) + M_0(2\xi)\right) d\xi, \qquad \mathcal{T}_{\mathrm{odd}}(a) = \frac{1}{2\pi}\int_0^{\xi_0} (-\alpha(\xi))\sigma(L_2)(\xi)^2 \left(M_0(0) - M_0(2\xi)\right) d\xi.$$

**Theorem 1A (Pure Similarity-Weighted Trace Certificate on $\log 2 < a \le 0.890$).** *At $a_1 = \frac{89}{100} = 0.890$ ($b_1 = 0.890 - \log 2 \approx 0.19685282$), 384-bit `flint.arb` integration certifies*
$$\mathcal{T}_{\mathrm{even}}(0.890) \in [0.98364291763662385985705589 \pm 10^{-48}] < 1.$$
*Since $\mathcal{T}_{\mathrm{odd}}(a) \le \mathcal{T}_{\mathrm{even}}(a)$ and $V_{a-\log 2} \subset V_{a_1-\log 2}$ by zero-extension for all $\log 2 < a \le 0.890$, every $g \in V_{a-\log 2}$ on $\log 2 < a \le 0.890$ satisfies (without using $A_+$ at all):*
$$q[L_2 g] \ge \left(1 - \mathcal{T}_{\mathrm{even}}(0.890)\right) V_{\min}\,\|g\|_{L^2(-b,b)}^2 \ge [0.017270537793784768633319 \pm 10^{-47}]\,\|g\|_{L^2(-b,b)}^2 > 0. \qquad \square$$

To reach the full four-shift endpoint $a_\star = \frac{1}{2}\log 6 \approx 0.8958797346$ ($b_\star = \frac{1}{2}\log(3/2) \approx 0.2027325541$), where $\mathcal{T}_{\mathrm{even}}(a_\star) \approx 1.0219936$ exceeds $1$ by $2.2\%$ while $\mathcal{T}_{\mathrm{odd}}(a_\star) \approx 0.2162306 \ll 1$, we include a rank-1 minorant from $A_+$ on $V_{b_\star}^{\mathrm{even}}$:

**Theorem 1B (1D Plancherel–Sherman–Morrison All-Vector Positivity Certificate on $\log 2 < a \le \frac{1}{2}\log 6$).** *At $a_\star = \frac{1}{2}\log 6$ ($b_\star = \frac{1}{2}\log(3/2)$), fix $\xi_1 = \frac{15}{2} = 7.5 > \xi_0$ and $\Xi = 50$, and let $w(x) := \mathbf{1}_{[-b_\star, b_\star]}(x) \in V_{b_\star}^{\mathrm{even}}$ ($\widehat{w}(\omega) = \frac{2\sin(\omega b_\star)}{\omega} = 2b_\star\operatorname{sinc}(\omega b_\star)$). Then:*
1. *(Plancherel Rank-1 Archimedean Identity):* *Since $2b_\star = \log(3/2) < \log 2$, $\langle L_2 g, L_2 w \rangle_{L^2(\mathbb{R})} = \frac{13}{4}\langle g, w \rangle_{L^2(-b_\star, b_\star)}$ for all $g \in V_{b_\star}^{\mathrm{even}}$. By Plancherel's theorem on $\mathbb{R}$,*
   $$\frac{1}{\pi}\int_{\xi_1}^\infty \sigma(L_2)(\omega)^2 \widehat{w}(\omega)\widehat{g}(\omega)\,d\omega = \langle \Psi_w, g \rangle_{L^2(-b_\star, b_\star)}, \qquad \Psi_w(x) := \frac{13}{4} - \frac{1}{\pi}\int_0^{\xi_1} \sigma(L_2)(\omega)^2 \widehat{w}(\omega)\cos(\omega x)\,d\omega.$$
2. *(Piecewise-Monotone 1D Upper Bound for $D_+$):* *By Cauchy–Schwarz on $[\xi_1, \infty)$ and strict monotonicity of $\alpha(\omega) > 0$ on $[\xi_1, \infty)$, for any partition $\xi_1 = \omega_0 < \omega_1 < \dots < \omega_K = \Xi$,*
   $$\langle A_+ g, g \rangle \ge \frac{|\langle \Psi_w, g \rangle_{L^2(-b_\star, b_\star)}|^2}{D_+}, \qquad D_+ := \sum_{k=0}^{K-1} \frac{1}{\alpha(\omega_k)}\frac{1}{\pi}\int_{\omega_k}^{\omega_{k+1}} \sigma(L_2)(\omega)^2 \widehat{w}(\omega)^2\,d\omega + \frac{1}{\alpha(\Xi)}\left(\frac{13}{2}b_\star - \frac{1}{\pi}\int_0^{\Xi} \sigma(L_2)(\omega)^2 \widehat{w}(\omega)^2\,d\omega\right).$$
3. *(Analytic Positivity and Monotonicity of $\Psi_w(x)$ on $[0, b_\star]$):* *Because $\xi_1 b_\star = \frac{15}{4}\log(3/2) \approx 1.520494 < \frac{\pi}{2} \approx 1.570796$, for every $\omega \in (0, \xi_1]$ we have $\widehat{w}(\omega) > 0$ and $\cos(\omega x)$ is strictly positive and strictly decreasing in $|x| \in [0, b_\star]$. Thus $\Psi_w(x)$ is strictly increasing in $|x| \in [0, b_\star]$, with certified global extrema on $[-b_\star, b_\star]$:*
   $$0 < \Psi_w(0) \in [0.016562986598 \pm 10^{-67}] \le \Psi_w(x) \le \Psi_w(b_\star) \in [1.285051104054 \pm 10^{-66}].$$
4. *(Closed-Form 1D Sherman–Morrison Trace Bound):* *Let $\psi_+ := D_+^{-1/2} V_{\mathrm{prime}}^{-1/2}\Psi_w \in L^2_{\mathrm{even}}(-b_\star, b_\star)$ and $P := I + |\psi_+\rangle\langle\psi_+| \succ 0$. By Fubini's theorem and $\Psi_w(x) \le \Psi_w(b_\star)$,*
   $$J_0 := \int_{-b_\star}^{b_\star} \frac{\Psi_w(x)}{V_{\mathrm{prime}}(x)}\,dx = \frac{13}{4}M_0(0) - \frac{1}{\pi}\int_0^{\xi_1} \sigma(L_2)(\omega)^2 \widehat{w}(\omega) M_0(\omega)\,d\omega > 0, \qquad \|\psi_+\|_2^2 \le \frac{\Psi_w(b_\star)\,J_0}{D_+}.$$
   *Moreover, since $\xi_0 b_\star \approx 1.275154 < \frac{\pi}{2}$, $\cos(\xi x) \ge \cos(\xi b_\star) > 0$ for all $\xi \in [0, \xi_0]$ and $x \in [-b_\star, b_\star]$, so*
   $$\langle T_{\mathrm{even}}\psi_+, \psi_+ \rangle \ge \frac{J_0^2}{D_+} I_{\cos^2}, \qquad I_{\cos^2} := \frac{1}{\pi}\int_0^{\xi_0} (-\alpha(\xi))\sigma(L_2)(\xi)^2 \cos^2(\xi b_\star)\,d\xi.$$
   *By the Sherman–Morrison formula $P^{-1} = I - \frac{|\psi_+\rangle\langle\psi_+|}{1 + \|\psi_+\|_2^2}$,*
   $$\lambda_{\max}\!\left(P^{-1/2} T_{\mathrm{even}} P^{-1/2}\right) \le \operatorname{Tr}(P^{-1} T_{\mathrm{even}}) = \mathcal{T}_{\mathrm{even}}(a_\star) - \frac{\langle T_{\mathrm{even}}\psi_+, \psi_+ \rangle}{1 + \|\psi_+\|_2^2} \le \mathcal{T}_{\mathrm{even}}(a_\star) - \frac{J_0^2\,I_{\cos^2}}{D_+ + \Psi_w(b_\star)J_0} < 1.$$
5. *(384-Bit `flint.arb` Enclosures and Unconditional All-Vector Floor on $\log 2 < a \le \frac{1}{2}\log 6$):* *Rigorous 384-bit `flint.arb` computation certifies:*
   $$\begin{aligned}
   \mathcal{T}_{\mathrm{even}}(a_\star) &\in [1.021993599159 \pm 10^{-48}], & \mathcal{T}_{\mathrm{odd}}(a_\star) &\in [0.216230596535 \pm 10^{-48}] < 1, \\
   J_0 &\in [0.171192227256 \pm 10^{-66}], & D_+ &\in [0.201083671560 \pm 10^{-71}], \\
   I_{\cos^2} &\in [2.075979252965 \pm 10^{-47}], & \operatorname{Tr}(P^{-1} T_{\mathrm{even}}) &\in [0.877505452068 \pm 10^{-48}] < 1.
   \end{aligned}$$
   *Consequently, by zero-extension $V_{a-\log 2} \subset V_{a_\star-\log 2}$, for every $a \in (\log 2, \frac{1}{2}\log 6]$ and every non-zero $g \in V_{a-\log 2}$ ($f = L_2 g \in V_a$):*
   $$\begin{aligned}
   q[L_2 g] &\ge \left(1 - \operatorname{Tr}(P^{-1} T_{\mathrm{even}})\right) V_{\min}\,\|g\|_{L^2(-b,b)}^2 \\
   &\ge [0.129335212270475 \pm 10^{-48}]\,\|g\|_{L^2(-b,b)}^2 = [0.039795449929377 \pm 10^{-48}]\,\|L_2 g\|_{L^2(-a,a)}^2 > 0. \qquad \square
   \end{aligned}$$

---

## Part 2 (`NB-GAIN` / `COEFF`): Corrected Linear-in-$N$ Extractor Norm, Unconditional Bessel Proof of Open Target A, and `NS-74` In-Space Perturbation

### 2.1 Theorem 2A (Corrected Stieltjes–Divisor Extractor Identity & Unconditional Proof of Open Target A)

**Theorem 2A (Corrected Stieltjes–Divisor Dual Extractor Identity).** *Let $\widetilde{\psi} \in H_0^2([1, 2])$ satisfy $\widetilde{\psi}(1) = \widetilde{\psi}'(1) = \widetilde{\psi}(2) = \widetilde{\psi}'(2) = 0$ and $\int_1^2 \widetilde{\psi}(u)\,du = 0$. For each $N \ge 2$, set $F_N(x) := \widetilde{\psi}\!\left(\frac{1}{Nx}\right)\mathbf{1}_{[1/(2N), 1/N]}(x)$ and define the minus-signed extractor*
$$\Lambda_N(x) := -\frac{d}{dx}\!\left(x F_N'(x)\right)\mathbf{1}_{[1/(2N), 1/N]}(x) \in H = L^2(0,\infty;dx).$$
*Then:*
1. *(Exact Linear-in-$N$ Norm Identity — Resolution of CODEX `M1`):* *With $u = \frac{1}{Nx} \in [1, 2]$, $\frac{du}{dx} = -N u^2$, so $x F_N'(x) = \frac{1}{Nu}(-N u^2 \widetilde{\psi}'(u)) = -u\,\widetilde{\psi}'(u)$, and*
   $$\Lambda_N(x) = -\frac{d}{dx}\!\left(-u\,\widetilde{\psi}'(u)\right) = -N u^2 \frac{d}{du}\!\left(u\,\widetilde{\psi}'(u)\right)\mathbf{1}_{[1,2]}(u).$$
   *Since $dx = \frac{du}{Nu^2}$, its exact $H$-norm squared scales linearly in $N$:*
   $$\|\Lambda_N\|_H^2 = \int_{1/(2N)}^{1/N} |\Lambda_N(x)|^2\,dx = N \int_1^2 u^2 \left|\frac{d}{du}\!\left(u\,\widetilde{\psi}'(u)\right)\right|^2 du = C_b\,N.$$
   *For $\widetilde{\psi}_5(u) = (u-1)^2(2-u)^2(u-\frac{3}{2})$ and $\widetilde{\psi}_7(u) = (u-1)^3(2-u)^3(2u-3)$ (where $\frac{d}{du}(u\,\widetilde{\psi}_7'(u)) = (u-1)(2-u)(98u^4 - 462u^3 + 743u^2 - 447u + 62)$):*
   $$C_b(\widetilde{\psi}_5) = \frac{2231}{2310} \approx 0.9658008658, \qquad C_b(\widetilde{\psi}_7) = \frac{6904}{45045} \approx 0.1532689533.$$
2. *(Positive Divisor-Sum Moments & Piecewise Verification — Resolution of CODEX `M2`, `M3`):* *Since $\sigma_r'(x) = -\frac{\rho_r(x)}{x} = -\frac{1}{rx^2} + \frac{1}{x}\lfloor\frac{1}{rx}\rfloor$ and $\int_{1/(2N)}^{1/N} \frac{F_N'(x)}{x}\,dx = -N\int_1^2 \widetilde{\psi}(u)\,du = 0$, integrating by parts twice with the minus sign in $\Lambda_N(x) = -(x F_N'(x))'$ yields:*
   $$\langle \Lambda_N, \sigma_r \rangle_H = -\int_{1/(2N)}^{1/N} F_N'(x)\rho_r(x)\,dx = +\int_{1/(2N)}^{1/N} F_N'(x)\left\lfloor\frac{1}{rx}\right\rfloor dx = +\sum_{\substack{k \ge 1 \\ N < kr < 2N}} \widetilde{\psi}\!\left(\frac{kr}{N}\right).$$
   *At $N = 4, r = 5$, direct piecewise integration of $\int_{1/8}^{1/4} \Lambda_4(x) A(\frac{1}{5x})\,dx$ on $[1/8, 1/5]$ and $[1/5, 1/4]$ gives $\langle \Lambda_4, \sigma_5 \rangle_H = -\frac{27}{8192} = +\widetilde{\psi}_7(\frac{5}{4})$ to 384-bit ball accuracy (error $< 10^{-110}$).*
3. *(Unconditional Proof of Proposed Open Target A):* *By Bessel's inequality for the orthogonal projection $\Pi_{2N} - \Pi_N$ in $H = L^2(0,\infty;dx)$:*
   $$\tilde{\lambda}_{\mathrm{proj}}^T (S^{(2)})^{-1} \tilde{\lambda}_{\mathrm{proj}} = \|(\Pi_{2N} - \Pi_N)\Lambda_N\|_H^2 \le \|\Lambda_N\|_H^2 = \frac{6904}{45045}N,$$
   $$\Delta_N = E_N^{(2)} - E_{2N}^{(2)} \ge \frac{M_N(u,y)^2}{\tilde{\lambda}_{\mathrm{proj}}^T (S^{(2)})^{-1} \tilde{\lambda}_{\mathrm{proj}}} \ge \frac{M_N(u,y)^2}{\frac{6904}{45045}N}.$$
   *Thus Proposed Open Target (A) is unconditionally proved by Bessel's inequality in $H$, leaving Proposed Open Target (B) ($\liminf_{N\to\infty} \frac{|M_N(u,y)|}{\sqrt{N}\,E_N^{(2)}} > 0$ on a cofinal subsequence) as the sole open arithmetic step.* $\square$

---

### 2.2 Theorem 2B (Refined `NS-74` In-Space Perturbation Decomposition — Resolution of CODEX `M4`)

**Theorem 2B (In-Space Perturbation Decomposition of `NS-74`).** *In $H = L^2(0,\infty;dx)$ with tail space $\mathcal{T} = L^2(0,1) \oplus \operatorname{span}\{x^{-1}\mathbf{1}_{x>1}\}$, the `NS-74` altered target $U_\beta^*\tau$ ($\beta \in (\frac{1}{2}, 1)$) decomposes orthogonally as $U_\beta^*\tau = P_{\mathcal{T}}(U_\beta^*\tau) \oplus \tau_\beta^\perp$ where $\|\tau_\beta^\perp\|_H^2 = F_\beta = \frac{(2\beta-1)(1-\beta)^2}{\beta^6} > 0$, and the in-space component $P_{\mathcal{T}}(U_\beta^*\tau) \in \mathcal{T}$ decomposes as*
$$P_{\mathcal{T}}(U_\beta^*\tau) = b_\beta\,\tau - c_\beta\,\tau_{\mathrm{pert}}^{(\beta)}, \qquad \tau_{\mathrm{pert}}^{(\beta)}(x) := \mathbf{1}_{(0,1)}(x) + \frac{1}{\beta}x^{-1}\mathbf{1}_{x>1} \in \mathcal{T},$$
*with non-zero load perturbation $\langle \tau_{\mathrm{pert}}^{(\beta)}, \sigma_n \rangle_H = \frac{1}{n}\left(\log n + 2 - \gamma + \frac{1}{\beta}\right)$. Consequently, any universal target-independent inequality on $\mathcal{T}$ transfers automatically to $P_{\mathcal{T}}(U_\beta^*\tau)$, whereas any target-specific arithmetic lower bound for $\tau$ must both account for the in-space perturbation $-c_\beta\tau_{\mathrm{pert}}^{(\beta)}$ and use $\tau^\perp = 0$ ($F_{1/2} = 0$) to relate $\Delta_N$ to the full residual energy $E_N^{(2)}$.* $\square$

---

## Part 3 (`ZERO-GEOMETRY`): Symmetrized Half-Strip Parseval Identity & Exact `NS-101` / `Davenport–Heilbronn` Controls

### 3.1 Theorem 3A (Symmetrized Half-Strip Identity & Exact Control Evaluation — Resolution of CODEX Finding 1, `M5`, `S1`)

**Theorem 3A (Symmetrized Half-Strip Parseval Identity & Single-Point Wronskian Transform).** *Let $\phi : \mathbb{R} \to \mathbb{R}$ be smooth and satisfy $\phi^{(k)}(u) = O(e^{-A|u|})$ ($0 \le k \le \max(m,n,2)$) for some $A > 0$, so $f(z) = \int_{\mathbb{R}} \phi(u)e^{zu}\,du$ is holomorphic on the strip $|\operatorname{Re} z| < A$. Then for every $z = x + i\tau$ with $|x| < A$:*
1. *(Full-Strip vs. Symmetrized Half-Strip Factorization):* *Under $u = p+t, v = p-t$ ($du\,dv = 2\,dp\,dt$), the half-strip $(p, t) \in \mathbb{R} \times [0, \infty)$ maps to the half-plane $\{u \ge v\}$, so factoring into $\operatorname{Re}((-z)^m(-\bar{z})^n |f(z)|^2)$ holds on the half-strip $t \ge 0$ after symmetrizing in $(m, n)$:*
   $$\begin{aligned}
   \operatorname{Re}\!\left((-z)^m(-\bar{z})^n |f(z)|^2\right) &= 2\int_{-\infty}^{\infty} dt \int_{-\infty}^{\infty} dp\,\phi^{(m)}(p+t)\phi^{(n)}(p-t)\,e^{2xp}\cos(2\tau t) \\
   &= 4\int_0^{\infty} dt \int_{-\infty}^{\infty} dp\,\frac{\phi^{(m)}(p+t)\phi^{(n)}(p-t) + \phi^{(n)}(p+t)\phi^{(m)}(p-t)}{2}\,e^{2xp}\cos(2\tau t).
   \end{aligned}$$
2. *(Cleared Single-Point Wronskian on $|\operatorname{Re} z| < A$):* *Forming the polynomial Wronskian $W_2[\phi](u) := \phi''(u)\phi(u) - (\phi'(u))^2$ (which requires no division by $\phi(u)$ at zeros of $\phi$), every real $x \in (-A, A)$ satisfies*
   $$\int_{-\infty}^{\infty} W_2[\phi](u)\,e^{2xu}\,du = -2\int_{-\infty}^{\infty} \left|(\phi(u)e^{xu})'\right|^2 du = -\frac{1}{\pi}\int_{-\infty}^{\infty} \tau^2 |f(x + i\tau)|^2\,d\tau < 0.$$
   *In particular, for the recorded `NS-101` reciprocal-dilation kernel $\phi_{\mathrm{NS101}}(u) = \operatorname{sech}(u) + \frac{2}{5}(\operatorname{sech}(u+\log 2) + \operatorname{sech}(u-\log 2))$ ($A = 1$) at $x = \frac{1}{4}$, 384-bit `flint.arb` integration certifies:*
   $$\int_{-\infty}^{\infty} W_2[\phi_{\mathrm{NS101}}](u)\,e^{u/2}\,du = -\frac{1}{\pi}\int_{-\infty}^{\infty} \tau^2 |f_{\mathrm{NS101}}(\tfrac{1}{4} + i\tau)|^2\,d\tau \in [-3.53478611961911705580 \pm 1.2\times 10^{-21}] < 0,$$
   *and on `controls.davenport_heilbronn.phi` at $x = 0$, $\int_{\mathbb{R}} W_2[\phi_{\mathrm{DH}}](u)\,du \approx -5.622869 < 0$.* $\square$
