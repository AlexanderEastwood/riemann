# Milestone 17 Derivation (v2): Infinite-Dimensional High-Mode Operator Lower Bound, Exact Two-Shift Product Defect Algebra, Global Remainder Block-Schur Positivity Certificate on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$, and Matched Davenport–Heilbronn Control Separation

**Date**: 2026-10-15  
**Milestone**: M17 (`infinite-dimensional-tail-floor-and-shift-coupling-defect-2026-10-15-v1`, Revision v2 repaired per `argon-m17-review-2026-10-15-v1`)  
**Lanes**: `WEIL-FLOOR`, `NB-GAIN / COEFF`, and `KERNEL-API`

> **Wall check**: This package does **NOT** prove the Riemann Hypothesis (`RH`), Goal 2 (`G2`), or the cofinal prime-shift lower bound as $a \to \infty$ (or $K \to \infty$). It certifies full-space infinite-dimensional positivity on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$ for $K = 2$ ($\mathcal{P}_2 = \{2, 3\}$) at the **five discrete rational bandwidths** $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$. Both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.

---

## 1. Theorem 1: Exact Two-Shift Operator Product Identity & Finite-Rank Multi-Shift Coupling Gram Matrix

### 1.1 Proof of the Two-Shift Product Identity on $L^2(-b, b)$
Let $b > 0$ and let $P_b : L^2(\mathbb{R}) \to L^2(-b, b)$ denote orthogonal projection onto $[-b, b]$. For any shift $\tau \ge 0$, define the compressed symmetric shift operator $S_\tau^{(b)} := P_b (T_{-\tau} + T_\tau) P_b$ on $L^2(-b, b)$, acting on $f \in L^2(-b, b)$ by
$$\bigl(S_\tau^{(b)} f\bigr)(x) = f(x + \tau)\,\mathbf{1}_{[-b,\, b - \tau]}(x) + f(x - \tau)\,\mathbf{1}_{[-b + \tau,\, b]}(x).$$
When $b \le \tau < 2b$ ($1 \le u = \tau / b < 2$), we have $b - \tau \le 0 \le -b + \tau$, so the two support intervals $[-b, b - \tau]$ and $[-b + \tau, b]$ are disjoint (up to $\{0\}$ if $\tau = b$). Hence for any $f \in L^2(-b, b)$ and $b \le \tau < 2b$,
$$\bigl\|S_\tau^{(b)} f\bigr\|_{L^2(-b, b)}^2 = \int_{-b}^{b - \tau} |f(x + \tau)|^2\,dx + \int_{-b + \tau}^b |f(x - \tau)|^2\,dx = \int_{-b + \tau}^b |f(y)|^2\,dy + \int_{-b}^{b - \tau} |f(y)|^2\,dy \le \|f\|_{L^2(-b, b)}^2,$$
establishing the exact operator norm bound:
$$\bigl\|S_\tau^{(b)}\bigr\|_{\mathrm{op}} \le \nu(\tau, b) := \begin{cases} 1, & b \le \tau < 2b, \\ 2, & 0 < \tau < b, \\ 0, & \tau \ge 2b. \end{cases}$$

Now let $0 \le \tau_1 \le \tau_2 < 2b$ ($u_1 = \tau_1 / b, u_2 = \tau_2 / b \in [0, 2)$). On $L^2(\mathbb{R})$, the uncompressed symmetric shifts satisfy
$$(T_{-\tau_1} + T_{\tau_1})(T_{-\tau_2} + T_{\tau_2}) = (T_{-(\tau_1 + \tau_2)} + T_{\tau_1 + \tau_2}) + (T_{-(\tau_2 - \tau_1)} + T_{\tau_2 - \tau_1}).$$
When compressed to $L^2(-b, b)$ via $S_{\tau_1}^{(b)} S_{\tau_2}^{(b)} = P_b (T_{-\tau_1} + T_{\tau_1}) P_b (T_{-\tau_2} + T_{\tau_2}) P_b$, the intermediate projection $P_b$ removes those paths $x \mapsto x \pm \tau_1 \mapsto x \pm \tau_1 \mp \tau_2$ where the intermediate point $y = x \pm \tau_1$ exits $[-b, b]$ while both endpoints $x$ and $x \pm (\tau_1 - \tau_2)$ remain inside $[-b, b]$:
1. For the sum paths $x \mapsto x + \tau_1 \mapsto x + \tau_1 + \tau_2$ and $x \mapsto x - \tau_1 \mapsto x - \tau_1 - \tau_2$: since $\tau_1, \tau_2 \ge 0$, whenever $x \in [-b, b]$ and $x + \tau_1 + \tau_2 \in [-b, b]$, the intermediate point $x + \tau_1$ automatically lies in $[-b, b - \tau_2] \subset [-b, b]$. Thus the sum term $S_{\tau_1 + \tau_2}^{(b)}$ suffers **zero intermediate truncation defect**.
2. For the difference paths $x \mapsto x + \tau_1 \mapsto x + \tau_1 - \tau_2$ and $x \mapsto x - \tau_1 \mapsto x - \tau_1 + \tau_2$:
   - On $x \mapsto x + \tau_1 \mapsto x - (\tau_2 - \tau_1)$, the endpoint check $x \in [-b + (\tau_2 - \tau_1), b]$ and the intermediate check $x + \tau_1 > b$ hold simultaneously on the upper boundary strip
     $$I_+(\tau_1, \tau_2) := \bigl(\max(-b + \tau_2 - \tau_1,\, b - \tau_1),\, b\bigr].$$
   - By reflection $x \mapsto -x$, on $x \mapsto x - \tau_1 \mapsto x + (\tau_2 - \tau_1)$, the intermediate check $x - \tau_1 < -b$ holds on the lower boundary strip $I_-(\tau_1, \tau_2) = -I_+(\tau_1, \tau_2)$.

In the orthonormal Legendre basis $e_m(x) = \sqrt{\frac{2m+1}{2b}}\,P_m(x/b)$ on $[-b, b]$, using $P_m(-t) = (-1)^m P_m(t)$, for $m + n$ even (both even or both odd) the two boundary strips $I_+(\tau_1, \tau_2)$ and $I_-(\tau_1, \tau_2)$ contribute equally, yielding **Theorem 1**:
$$S_{\tau_1}^{(b)} S_{\tau_2}^{(b)} = S_{\tau_1 + \tau_2}^{(b)} + S_{\tau_2 - \tau_1}^{(b)} - D_{\tau_1, \tau_2}(b),$$
where for $m + n$ even,
$$\bigl(D_{\tau_1, \tau_2}(b)\bigr)_{m, n} = \sqrt{(2m+1)(2n+1)} \int_{\max(-1 + \Delta u,\, 1 - u_1)}^1 P_m(x)\,P_n(x - \Delta u)\,dx, \qquad \Delta u = u_2 - u_1 = \frac{\tau_2 - \tau_1}{b}.$$

### 1.2 Certified Verification of Theorem 1 & Exact Multi-Shift Coupling Gram Matrix
At $2b = 0.50$ ($b = 0.25$) with $\tau_1 = \log(7/6) \approx 0.15415068$ and $\tau_2 = \log(6/5) \approx 0.18232156$, we verify $(S_{\tau_1 + \tau_2} + S_{\tau_2 - \tau_1} - D_{\tau_1, \tau_2})_{m, n}$ against direct piecewise ball quadrature of $\langle S_{\tau_1} e_m, S_{\tau_2} e_n \rangle_{L^2(-b, b)}$ and compare against finite-mode Legendre sums $\sum_{k=0}^{M_{\mathrm{cut}}} (S_{\tau_1})_{m, k} (S_{\tau_2})_{k, n}$:

| Mode Pair $(m, n)$ | Exact Product Entry $(S_{\tau_1} S_{\tau_2})_{m, n}$ | Defect Entry $(D_{\tau_1, \tau_2})_{m, n}$ | Quadrature Ball Difference | Truncation Error ($M_{\mathrm{cut}} = 20$) | Truncation Error ($M_{\mathrm{cut}} = 80$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $(0, 0)$ | $+1.92482483$ | $+0.61660272$ | $\le 1.93 \times 10^{-75}$ | $2.72 \times 10^{-3}$ | $2.05 \times 10^{-5}$ |
| $(0, 2)$ | $+0.05996332$ | $+0.06950723$ | $\le 1.23 \times 10^{-23}$ | $6.37 \times 10^{-3}$ | $7.72 \times 10^{-5}$ |
| $(2, 2)$ | $+0.75067966$ | $+0.39887868$ | $\le 4.09 \times 10^{-23}$ | $1.40 \times 10^{-2}$ | $1.19 \times 10^{-4}$ |
| $(2, 4)$ | $-0.56974808$ | $-0.31716505$ | $\le 1.19 \times 10^{-22}$ | $2.09 \times 10^{-2}$ | $3.77 \times 10^{-4}$ |
| $(1, 1)$ | $+0.04451769$ | $+0.79946345$ | $\le 1.10 \times 10^{-23}$ | $1.59 \times 10^{-2}$ | $5.61 \times 10^{-5}$ |
| $(1, 3)$ | $+0.35195749$ | $-0.37650826$ | $\le 4.17 \times 10^{-23}$ | $2.52 \times 10^{-2}$ | $6.20 \times 10^{-6}$ |
| $(3, 3)$ | $+1.29292939$ | $+0.48019303$ | $\le 1.18 \times 10^{-22}$ | $3.91 \times 10^{-2}$ | $1.82 \times 10^{-4}$ |

Consequently, for any finite linear combination of active shift operators $W_{\mathrm{comb}, R}^{\mathrm{off}}(b) = \sum_{0 < \tau_r < 2b} d_r(R)\,S_{\tau_r}^{(b)}$, the $N_{\mathrm{leg}} \times N_{\mathrm{leg}}$ low-to-high coupling Gram matrix
$$\mathcal{G}_{\mathrm{comb}, R}^{(N_{\mathrm{leg}}, \mathrm{sector})}(b) = B_{\mathrm{comb}, R}^* B_{\mathrm{comb}, R} = P_{\le}^{\mathrm{sector}} \bigl(W_{\mathrm{comb}, R}^{\mathrm{off}}(b)\bigr)^2 P_{\le}^{\mathrm{sector}} - \bigl(P_{\le}^{\mathrm{sector}} W_{\mathrm{comb}, R}^{\mathrm{off}}(b) P_{\le}^{\mathrm{sector}}\bigr)^2$$
is evaluated in closed form in `flint.arb` without summing an infinite Legendre tail, capturing the destructive interference between the negative external prime shifts ($c_{7/6} \approx -0.300260$, $c_{6/5} \approx -0.293842$) and the positive internal shift $d_{3/2}(R) = c_{3/2} + \frac{\alpha(R)}{\sqrt{6}} > 0$.

---

## 2. Theorem 2: Window-Localized Archimedean Frequency Splitting, Poisson–Bessel Tail Trace Bound, & Laplace–Bessel External Enclosure

### 2.1 Window-Localized Archimedean Splitting & Exact Holomorphic Digamma Extension
For $K = 2$ ($\mathcal{P}_2 = \{2, 3\}$) and $2b \le 0.50 < \log 2 \approx 0.693147$, decompose the Fourier symbol $\sigma_{L_{\mathcal{P}_2}}(\xi)$ into its local positive component ($\lambda_r \in \{0, \log(3/2)\}$) and its smooth external component ($\lambda_r \in \{\log 2, \log 3, \log 6\} > 2b$):
$$\sigma_{L_{\mathcal{P}_2}}(\xi) = \sigma_{\mathrm{loc}}(\xi) + \sigma_{\mathrm{ext}}(\xi),$$
where (since $l_{\mathrm{full}}[2] = -\frac{4}{3\sqrt{2}}$, $l_{\mathrm{full}}[3] = -\frac{\sqrt{3}}{2}$, $l_{\mathrm{full}}[6] = \frac{1}{\sqrt{6}}$, $l_{\mathrm{full}}[3/2] = \frac{1}{\sqrt{6}}$, and each $r > 1$ has multiplicity $2$ from $r$ and $r^{-1}$):
$$\sigma_{\mathrm{loc}}(\xi) := 2 + \frac{2}{\sqrt{6}}\cos\bigl(\xi \log(3/2)\bigr) \in \left[2 - \frac{2}{\sqrt{6}},\, 2 + \frac{2}{\sqrt{6}}\right] \approx [1.183503,\, 2.816497],$$
$$\sigma_{\mathrm{ext}}(\xi) := -\frac{8}{3\sqrt{2}}\cos(\xi \log 2) - \sqrt{3}\cos(\xi \log 3) + \frac{2}{\sqrt{6}}\cos(\xi \log 6).$$
For any frequency threshold $R \ge \xi_0 \approx 6.289836$, $\alpha(\xi) = \operatorname{Re}\psi(1/4 + i\xi/2) - \log\pi$ is strictly increasing on $[0, \infty)$ with $\alpha(R) > 0$. For complex quadrature in `flint.acb.integral`, $\alpha(\xi)$ is extended holomorphically to the strip $|\operatorname{Im}(\xi)| < 1/2$ by
$$\alpha_{\mathrm{acb}}(\xi) := \frac{1}{2}\left(\psi\!\left(\frac{1}{4} + \frac{i\xi}{2}\right) + \psi\!\left(\frac{1}{4} - \frac{i\xi}{2}\right)\right) - \log\pi,$$
which coincides identically with $\alpha(\xi)$ on $\mathbb{R}$ (verified by self-test at $\xi = 9$: $\alpha(9) = 0.35883198893599235\dots$).

Since $\sigma_{\mathrm{loc}}(\xi) > 0$ for all $\xi \in \mathbb{R}$, the localized archimedean quadratic form $A_{\mathrm{loc}}(b) = P_b \mathcal{F}^* \sigma_{\mathrm{loc}}(\xi)\alpha(\xi)\mathcal{F} P_b$ decomposes **globally on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$** as:
$$A_{\mathrm{loc}}(b) = \mathcal{A}_{\mathrm{loc}, +, R}(b) + \alpha(R)\,L_{\mathrm{loc}}(b) - \mathcal{D}_{\mathrm{loc}, R}(b),$$
where:
1. $\mathcal{A}_{\mathrm{loc}, +, R}(b) = P_b \mathcal{F}^* \sigma_{\mathrm{loc}}(\xi)\bigl(\alpha(\xi) - \alpha(R)\bigr)_+ \mathcal{F} P_b \succeq 0$ is **globally positive semidefinite on all of $\mathcal{Q}(A_{\mathrm{arch}})$**.
2. On $L^2(-b, b)$, $L_{\mathrm{loc}}(b) = 2 I + \frac{1}{\sqrt{6}} S_{\log(3/2)}^{(b)}$ satisfies $L_{\mathrm{loc}}(b) = 2 I$ for $2b \le \log(3/2)$ and $L_{\mathrm{loc}}(b) \succeq \bigl(2 - \frac{1}{\sqrt{6}}\bigr) I \approx 1.591752\,I$ for $\log(3/2) < 2b \le 0.50$ (since $b \le 0.25 < \log(3/2)$ implies $\|S_{\log(3/2)}^{(b)}\|_{\mathrm{op}} \le 1$).
3. $\mathcal{D}_{\mathrm{loc}, R}(b) = P_b \mathcal{F}^* \sigma_{\mathrm{loc}}(\xi)\bigl(\alpha(R) - \alpha(\xi)\bigr)\mathbf{1}_{|\xi| \le R} \mathcal{F} P_b \succeq 0$ is trace-class. Since $\widehat{e_m}(\xi) = (-i)^m \sqrt{2b(2m+1)}\,j_m(b\xi)$ and $|j_m(u)| \le \frac{|u|^m}{(2m+1)!!}$, integrating $(b\xi)^{2m}$ over $\xi \in [0, R]$ cancels $2m+1$ identically:
   $$\int_0^R 2b(2m+1)\,j_m(b\xi)^2\,d\xi \le \frac{2(bR)^{2m+1}}{\bigl((2m+1)!!\bigr)^2}.$$
   Summing over $m \in \{M_0, M_0 + 2, \dots\}$ ($M_0 = 2 N_{\mathrm{leg}}$ for even parity, $2 N_{\mathrm{leg}} + 1$ for odd parity) yields the closed-form geometric enclosure:
   $$\left\|P_{\ge M_0}^{\mathrm{sector}} \mathcal{D}_{\mathrm{loc}, R}(b) P_{\ge M_0}^{\mathrm{sector}}\right\|_{\mathrm{op}} \le \operatorname{Tr}\!\left(P_{\ge M_0}^{\mathrm{sector}} \mathcal{D}_{\mathrm{loc}, R}(b) P_{\ge M_0}^{\mathrm{sector}}\right) \le \mathcal{B}_{\mathrm{PB}, \mathrm{loc}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}}) := M_{\mathrm{loc}}\bigl(\alpha(R) - \alpha(0)\bigr)\,\frac{2}{\pi} \frac{(b R)^{2 M_0 + 1}}{\bigl((2 M_0 + 1)!!\bigr)^2\bigl(1 - \rho_{M_0}(b R)\bigr)},$$
   where $\rho_{M_0}(bR) = \frac{(bR)^4}{(2M_0 + 3)^2(2M_0 + 5)^2} < 1$. Furthermore, since $0 \preceq \mathcal{D}_{\mathrm{loc}, R}(b) \preceq M_{\mathrm{loc}}\bigl(\alpha(R) - \alpha(0)\bigr) I$ globally on $L^2(-b, b)$, its low-to-high off-diagonal block satisfies
   $$\left\|P_{\ge M_0}^{\mathrm{sector}} \mathcal{D}_{\mathrm{loc}, R}(b) P_{< M_0}^{\mathrm{sector}}\right\|_{\mathrm{op}} \le \sqrt{M_{\mathrm{loc}}\bigl(\alpha(R) - \alpha(0)\bigr)\,\mathcal{B}_{\mathrm{PB}, \mathrm{loc}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}})}.$$

### 2.2 Laplace–Bessel Enclosure for Smooth External Archimedean Kernels ($\lambda_r > 2b$)
For each external shift $\lambda_r \in \{\log 2, \log 3, \log 6\} > 2b$ (with cosine weight $2 w_r \in \bigl\{-\frac{8}{3\sqrt{2}}, -\sqrt{3}, +\frac{2}{\sqrt{6}}\bigr\}$), the spatial integral formula in `exact_spatial_j_mn` for $\lambda_r > 2b$ expands via $\frac{e^{-t/2}}{1 - e^{-2t}} = \sum_{k=0}^\infty e^{-\beta_k t}$ ($\beta_k = 2k + \frac{1}{2}$) into the convergent rank-1 series on $L^2_{\mathrm{sector}}(-b, b)$:
$$\mathcal{J}_{m, n}(\lambda_r; b) = (-1)^{m+1} \sum_{k=0}^\infty e^{-\beta_k \lambda_r}\,\langle e_m, \psi_k^{\mathrm{sector}} \rangle \langle e_n, \psi_k^{\mathrm{sector}} \rangle,$$
where $\psi_k^{\mathrm{even}}(x) = \cosh(\beta_k x)$, $\psi_k^{\mathrm{odd}}(x) = \sinh(\beta_k x)$, and
$$\langle e_m, \psi_k^{\mathrm{sector}} \rangle = \sqrt{2b(2m+1)}\,i_m(\beta_k b), \qquad \langle e_m, \psi_k^{\mathrm{sector}} \rangle^2 = 2b(2m+1)\,i_m(\beta_k b)^2.$$
(Thus $\mathcal{J}^{\mathrm{even}}(\lambda_r; b) \preceq 0$ and $\mathcal{J}^{\mathrm{odd}}(\lambda_r; b) \succeq 0$.) Using $0 \le i_m(z) \le \frac{z^m}{(2m+1)!!} e^z$ for $0 \le k < k_{\mathrm{cut}} = 12$ and $\|P_{\ge M_0}^{\mathrm{sector}} \psi_k^{\mathrm{sector}}\|_{L^2}^2 \le \|\psi_k^{\mathrm{sector}}\|_{L^2}^2 \le 2b\,e^{2\beta_k b}$ for $k \ge k_{\mathrm{cut}}$ gives the certified closed-form bounds ($M_0 = 2N_{\mathrm{leg}}$ or $2N_{\mathrm{leg}}+1$, $\Delta_r = \lambda_r - 2b > 0$):
$$\mathcal{E}_{\mathrm{diag}}^{\mathrm{sector}}(b, N_{\mathrm{leg}}) = \sum_{r \in \{2, 3, 6\}} |2 w_r|\!\left[\sum_{k=0}^{k_{\mathrm{cut}}-1} 2b\,\frac{2M_0 + 1}{1 - \rho_{M_0}(\beta_k b)} \frac{(\beta_k b)^{2M_0}}{\bigl((2M_0+1)!!\bigr)^2} e^{-\beta_k \Delta_r} + \frac{2b\,e^{-\beta_{k_{\mathrm{cut}}} \Delta_r}}{1 - e^{-2\Delta_r}}\right],$$
$$\mathcal{E}_{\mathrm{off}}^{\mathrm{sector}}(b, N_{\mathrm{leg}}) = \sum_{r \in \{2, 3, 6\}} |2 w_r|\!\left[\sum_{k=0}^{k_{\mathrm{cut}}-1} 2b\,\sqrt{\frac{2M_0 + 1}{1 - \rho_{M_0}(\beta_k b)}} \frac{(\beta_k b)^{M_0}}{(2M_0+1)!!} e^{-\beta_k \Delta_r} + \frac{2b\,e^{-\beta_{k_{\mathrm{cut}}} \Delta_r}}{1 - e^{-2\Delta_r}}\right].$$

---

## 3. Theorem 3: Global Subtraction of $\mathcal{A}_{\mathrm{loc}, +, R}(b)$ & Full-Space Block-Schur Positivity Certificate on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$

### 3.1 Why $\mathcal{A}_{\mathrm{loc}, +, R}(b)$ Must Be Subtracted Globally Across All Blocks
Write the full untruncated Weil operator on $\mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$ as
$$\mathcal{W}_{\mathcal{P}_2}^{\mathrm{full}}(b) = \mathcal{A}_{\mathrm{loc}, +, R}(b) + \mathcal{R}_R(b),$$
where $\mathcal{A}_{\mathrm{loc}, +, R}(b) \succeq 0$ globally on $\mathcal{Q}(A_{\mathrm{arch}})$, and the **bounded self-adjoint remainder operator** $\mathcal{R}_R(b)$ on $L^2(-b, b)$ is
$$\mathcal{R}_R(b) := \underbrace{\alpha(R)\,L_{\mathrm{loc}}(b) + W_{\mathrm{sh}}(b)}_{W_{\mathrm{comb}, R}(b)} + C_{\mathrm{diag}}(\mathcal{P}_2)\,I - \mathcal{D}_{\mathrm{loc}, R}(b) + A_{\mathrm{ext}}(b).$$
Because $\mathcal{A}_{\mathrm{loc}, +, R}(b) \succeq 0$ on the entire form domain $\mathcal{Q}(A_{\mathrm{arch}})$, we have the **global quadratic-form inequality**
$$\langle g, \mathcal{W}_{\mathcal{P}_2}^{\mathrm{full}}(b) g \rangle \ge \langle g, \mathcal{R}_R(b) g \rangle \qquad \forall g \in \mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b).$$
*(Crucial audit note per `argon-m17-review` Findings 1 & 2: One cannot drop $\mathcal{A}_{\mathrm{loc}, +, R}(b)$ on the high-high and low-high blocks while keeping $P_{\le}\mathcal{A}_{\mathrm{loc}, +, R}(b)P_{\le}$ on the low-low block, because $\mathcal{A}_{\mathrm{loc}, +, R}(b)$ carries the logarithmic singularity $-\log|x-y|$ of $A_{\mathrm{loc}}(b)$ and therefore has an $O(1)$ low-to-high coupling entry $\langle e_{12}, A_{\mathcal{P}_2}(b) e_{10} \rangle \approx +1.252539$ at $2b = 0.50$. By subtracting $\mathcal{A}_{\mathrm{loc}, +, R}(b) \succeq 0$ from **all blocks**, the logarithmic singularity is removed globally, and the remaining archimedean off-diagonal block $B_{\mathrm{rem, arch}, R} = P_{>}^{\mathrm{sector}}(-\mathcal{D}_{\mathrm{loc}, R}(b) + A_{\mathrm{ext}}(b))P_{\le}^{\mathrm{sector}}$ has entry $\langle e_{12}, (-\mathcal{D}_{\mathrm{loc}, R}(b) + A_{\mathrm{ext}}(b)) e_{10} \rangle = +1.526734 \times 10^{-9} \ll \beta_{\mathrm{rem, arch}}^{\mathrm{even}}(0.25, 18, 6) = 2.619743 \times 10^{-2}$.)*

### 3.2 Block Structure of the Bounded Remainder Operator $\mathcal{R}_R(b)$
On $L^2_{\mathrm{sector}}(-b, b) = \mathcal{H}_{\le}^{\mathrm{sector}} \oplus \mathcal{H}_{>}^{\mathrm{sector}}$, the bounded remainder operator $\mathcal{R}_R(b)$ has block representation
$$\mathcal{R}_R^{\mathrm{sector}}(b) = \begin{pmatrix} R_{\le}^{\mathrm{sector}}(b) & B_{\mathrm{rem}, R}^* \\ B_{\mathrm{rem}, R} & R_{>}^{\mathrm{sector}}(b) \end{pmatrix},$$
where:
1. **Exact Low-Low Remainder Block $R_{\le}^{\mathrm{sector}}(b) = P_{\le}^{\mathrm{sector}} \mathcal{R}_R(b) P_{\le}^{\mathrm{sector}}$**:
   $$R_{\le}^{\mathrm{sector}}(b) = \bigl(2\alpha(R) + C_{\mathrm{diag}}(\mathcal{P}_2)\bigr) I_{\le} + P_{\le}^{\mathrm{sector}} W_{\mathrm{comb}, R}^{\mathrm{off}}(b) P_{\le}^{\mathrm{sector}} - P_{\le}^{\mathrm{sector}} \mathcal{D}_{\mathrm{loc}, R}(b) P_{\le}^{\mathrm{sector}} + P_{\le}^{\mathrm{sector}} A_{\mathrm{ext}}(b) P_{\le}^{\mathrm{sector}},$$
   where $W_{\mathrm{comb}, R}^{\mathrm{off}}(b) = \sum_{0 < \tau_r < 2b} d_r(R) S_{\tau_r}^{(b)}$ combines $W_{\mathrm{sh}}(b)$ and $\frac{\alpha(R)}{\sqrt{6}} S_{\log(3/2)}^{(b)}$ ($d_{3/2}(R) = c_{3/2} + \frac{\alpha(R)}{\sqrt{6}}$).
2. **High-High Tail Floor $R_{>}^{\mathrm{sector}}(b) \succeq \mu_{\mathrm{tail}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}})\,I_{>}^{\mathrm{sector}}$**:
   $$\mu_{\mathrm{tail}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}}) = \alpha(R)\,\lambda_{\min}\bigl(L_{\mathrm{loc}}(b)\bigr) + C_{\mathrm{diag}}(\mathcal{P}_2) - \sum_{0 < \tau_r < 2b} \nu(\tau_r, b)|c_r| - \mathcal{B}_{\mathrm{PB}, \mathrm{loc}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}}) - \mathcal{E}_{\mathrm{diag}}^{\mathrm{sector}}(b, N_{\mathrm{leg}}) > 0.$$
3. **Low-to-High Remainder Coupling $B_{\mathrm{rem}, R} = B_{\mathrm{comb}, R} + B_{\mathrm{rem, arch}, R}$**:
   - $B_{\mathrm{comb}, R} = P_{>}^{\mathrm{sector}} W_{\mathrm{comb}, R}^{\mathrm{off}}(b) P_{\le}^{\mathrm{sector}}$ (which **includes** $\alpha(R) P_{>}^{\mathrm{sector}} L_{\mathrm{loc}}(b) P_{\le}^{\mathrm{sector}}$ when $\log(3/2) < 2b$) has **exact** $N_{\mathrm{leg}} \times N_{\mathrm{leg}}$ Gram matrix $\mathcal{G}_{\mathrm{comb}, R}^{(N_{\mathrm{leg}}, \mathrm{sector})}(b) = B_{\mathrm{comb}, R}^* B_{\mathrm{comb}, R}$ from Theorem 1.
   - $B_{\mathrm{rem, arch}, R} = P_{>}^{\mathrm{sector}}\bigl(-\mathcal{D}_{\mathrm{loc}, R}(b) + A_{\mathrm{ext}}(b)\bigr)P_{\le}^{\mathrm{sector}}$ satisfies $\|B_{\mathrm{rem, arch}, R}\|_{\mathrm{op}} \le \beta_{\mathrm{rem, arch}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}}) := \sqrt{M_{\mathrm{loc}}(\alpha(R) - \alpha(0))\,\mathcal{B}_{\mathrm{PB}, \mathrm{loc}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}})} + \mathcal{E}_{\mathrm{off}}^{\mathrm{sector}}(b, N_{\mathrm{leg}})$.

By Young's operator inequality $B_{\mathrm{rem}, R}^* B_{\mathrm{rem}, R} \preceq (1 + \eta)\,\mathcal{G}_{\mathrm{comb}, R}^{(N_{\mathrm{leg}}, \mathrm{sector})}(b) + \bigl(1 + \frac{1}{\eta}\bigr)\beta_{\mathrm{rem, arch}}^2\,I_{\le}$ ($\eta = 1/20$), whenever $\mu_{\mathrm{tail}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}}) > 0$ and the $N_{\mathrm{leg}} \times N_{\mathrm{leg}}$ **Remainder Matrix Schur Complement**
$$\mathcal{S}_{\mathrm{mat}}^{(N_{\mathrm{leg}}, \mathrm{sector})}(b) := R_{\le}^{\mathrm{sector}}(b) - \frac{1}{\mu_{\mathrm{tail}}^{\mathrm{sector}}(b, R, N_{\mathrm{leg}})}\left(\frac{21}{20}\,\mathcal{G}_{\mathrm{comb}, R}^{(N_{\mathrm{leg}}, \mathrm{sector})}(b) + 21\,\beta_{\mathrm{rem, arch}}^2\,I_{\le}\right) \succ 0,$$
we have $\mathcal{W}_{\mathcal{P}_2}^{\mathrm{full}}(b) \succeq \mathcal{R}_R(b) \succ 0$ on all of $\mathcal{Q}(A_{\mathrm{arch}}) \cap L^2_{\mathrm{sector}}(-b, b)$.

### 3.3 Certified Full-Space Table (`256`-bit and `384`-bit `flint.arb`)

| Bandwidth $2b$ | Parity | $(N_{\mathrm{leg}}, M_0, R, M_{\mathrm{sh}})$ | Tail Floor $\mu_{\mathrm{tail}}^{\mathrm{sector}}$ | Rem Arch $\|B_{\mathrm{rem,arch}}\|_{\mathrm{op}}$ | Combined Shift $\|B_{\mathrm{comb}, R}\|_F^{1/2}$ (vs. Tri) | Full Low $\lambda_{\min}(W_{\le}^{\mathrm{full}})$ | Rem Low $\lambda_{\min}(R_{\le}^{\mathrm{sector}})$ | Matrix Schur $\lambda_{\min}(\mathcal{S}_{\mathrm{mat}})$ | Min Cholesky Pivot $L_{i,i}^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0.40$ | Even | $(4, 8, 9, 2)$ | $+1.550975$ | $1.422 \times 10^{-3}$ | $0.381662$ ($0.621127$) | $+0.462249$ | $+0.275328$ | **$+0.268994$** | $+0.287324$ |
| $0.40$ | Odd | $(4, 9, 9, 2)$ | $+1.550976$ | $1.313 \times 10^{-3}$ | $0.410572$ ($0.656473$) | $+3.683660$ | $+2.200014$ | **$+2.170277$** | $+2.415762$ |
| $0.42$ | Even | $(5, 10, 14, 3)$ | $+1.375728$ | $2.426 \times 10^{-3}$ | $0.839539$ ($1.385053$) | $+0.362670$ | $+0.286754$ | **$+0.280699$** | $+0.346734$ |
| $0.42$ | Odd | $(5, 11, 14, 3)$ | $+1.375728$ | $2.347 \times 10^{-3}$ | $0.845192$ ($1.442087$) | $+3.478759$ | $+2.519032$ | **$+2.211525$** | $+2.860255$ |
| $0.45$ | Even | $(5, 10, 14, 3)$ | $+1.372361$ | $5.904 \times 10^{-3}$ | $0.958493$ ($1.547332$) | $+0.266128$ | $+0.211137$ | **$+0.204659$** | $+0.338867$ |
| $0.45$ | Odd | $(5, 11, 14, 3)$ | $+1.372361$ | $5.731 \times 10^{-3}$ | $1.018361$ ($1.603020$) | $+2.910448$ | $+2.118756$ | **$+2.010450$** | $+2.379543$ |
| $0.48$ | Even | $(5, 10, 14, 3)$ | $+1.363990$ | $1.453 \times 10^{-2}$ | $0.960246$ ($1.587068$) | $+0.189287$ | $+0.146465$ | **$+0.133707$** | $+0.317252$ |
| $0.48$ | Odd | $(5, 11, 14, 3)$ | $+1.363991$ | $1.415 \times 10^{-2}$ | $1.049444$ ($1.651037$) | $+2.437210$ | $+1.871996$ | **$+1.828035$** | $+2.036742$ |
| $0.50$ | Even | $(6, 12, 18, 3)$ | $+1.752310$ | $2.620 \times 10^{-2}$ | $1.194467$ ($1.831863$) | $+0.143153$ | $+0.117019$ | **$+0.102995$** | $+0.362092$ |
| $0.50$ | Odd | $(6, 13, 18, 3)$ | $+1.752310$ | $2.596 \times 10^{-2}$ | $1.277561$ ($1.872579$) | $+2.193880$ | $+1.891973$ | **$+1.853019$** | $+1.945586$ |

---

## 4. Theorem 4: Dependency Edge `WEIL-FLOOR -> G2` & Matched Davenport–Heilbronn Control Separation

### 4.1 Dependency Edge (`WEIL-FLOOR -> G2`) & Exact Stirling Rate Analysis in $M_0$
Let $M_0$ denote the **first omitted Legendre degree** in the parity sector ($M_0 = 2 N_{\mathrm{leg}}$ for even parity, $M_0 = 2 N_{\mathrm{leg}} + 1$ for odd parity). By Stirling's formula, $(2M_0 + 1)!! = \frac{(2M_0 + 1)!}{2^{M_0} M_0!} \sim \sqrt{2}\left(\frac{2M_0 + 1}{e}\right)^{M_0 + 1/2}$ as $M_0 \to \infty$. Therefore:
- At the threshold cutoff $R_{M_0} = \frac{2M_0 + 1}{e b}$ (where $b R_{M_0} = \frac{2M_0 + 1}{e}$), the leading Poisson–Bessel factor satisfies
  $$\frac{(b R_{M_0})^{2M_0 + 1}}{\bigl((2M_0 + 1)!!\bigr)^2} \sim \frac{1}{2 e (2M_0 + 1)} = O(M_0^{-1}) \to 0,$$
  so multiplying by $\alpha(R_{M_0}) \sim \log\!\left(\frac{2M_0 + 1}{\pi e b}\right)$ gives $\alpha(R_{M_0}) \frac{(b R_{M_0})^{2M_0 + 1}}{((2M_0 + 1)!!)^2} = O\!\left(\frac{\log M_0}{M_0}\right) \to 0$.
- Choosing the sub-threshold linear cutoff $R_{M_0} = \frac{2M_0 + 1}{2 e b}$ (where $b R_{M_0} = \frac{2M_0 + 1}{2e}$) gives **exponential decay** of the Poisson–Bessel tail trace bound:
  $$\frac{(b R_{M_0})^{2M_0 + 1}}{\bigl((2M_0 + 1)!!\bigr)^2} \sim \frac{2^{-(2M_0 + 1)}}{2 e (2M_0 + 1)} = O\!\left(2^{-(2M_0 + 1)} M_0^{-1}\right) \to 0,$$
  while $\alpha(R_{M_0}) \sim \log\!\left(\frac{M_0}{\pi e b}\right) \to +\infty$. Thus $\lim_{N_{\mathrm{leg}} \to \infty} \mu_{\mathrm{tail}}^{\mathrm{sector}}(b, R_{M_0}, N_{\mathrm{leg}}) = +\infty$ for every fixed $(K, b)$.

However, as $K \to \infty$, the global multiplier floor $\sigma_{\min}(L_{\mathcal{P}_K}) = \prod_{p \le p_K} (1 - p^{-1/2})^2$ decays rapidly:

| $K$ | Primes $\mathcal{P}_K$ | $\sigma_{\min}(L_{\mathcal{P}_K})$ | $\sigma_{\max}(L_{\mathcal{P}_K})$ | Condition Ratio $\sigma_{\max}/\sigma_{\min}$ | Diagonal Constant $C_{\mathrm{diag}}(\mathcal{P}_K)$ |
| :---: | :--- | :---: | :---: | :---: | :---: |
| $1$ | $\{2\}$ | $8.5786 \times 10^{-2}$ | $2.914214$ | $3.397 \times 10^{1}$ | $+0.693147$ |
| $2$ | $\{2, 3\}$ | $1.5314 \times 10^{-2}$ | $7.259492$ | $4.741 \times 10^{2}$ | $+2.022809$ |
| $3$ | $\{2, 3, 5\}$ | $4.6820 \times 10^{-3}$ | $15.204469$ | $3.247 \times 10^{3}$ | $+3.495999$ |
| $4$ | $\{2, 3, 5, 7\}$ | $1.8087 \times 10^{-3}$ | $28.831676$ | $1.594 \times 10^{4}$ | $+5.049302$ |
| $5$ | $\{2, 3, 5, 7, 11\}$ | $8.8421 \times 10^{-4}$ | $48.781020$ | $5.517 \times 10^{4}$ | $+6.597327$ |
| $6$ | $\{2, 3, 5, 7, 11, 13\}$ | $4.6238 \times 10^{-4}$ | $79.711303$ | $1.724 \times 10^{5}$ | $+8.176385$ |

This quantifies the exact dependency edge `WEIL-FLOOR -> G2`: finite-$N_{\mathrm{leg}}$ Block-Schur certificates close the infinite-dimensional high-mode tail at fixed $(K, b)$, but do **not** close the cofinal limit $b \to \infty$ (`G2` / `RH`).

### 4.2 Matched Davenport–Heilbronn Control Separation (`controls/davenport_heilbronn.py`)
For the repository's matched Davenport–Heilbronn function $f_{DH}(s) = \frac{1 - i\kappa}{2} L(s, \chi_5) + \frac{1 + i\kappa}{2} L(s, \overline{\chi_5})$ built from the two **odd** primitive characters mod $5$ ($\chi_5(2) = i, \chi_5(3) = -i, \chi_5(4) = -1$) with $\kappa = \frac{\sqrt{10 - 2\sqrt{5}} - 2}{\sqrt{5} - 1} \approx 0.28407904384$:
1. **Non-Eulerian Dirichlet Convolution Coefficients $\Lambda_{DH}(n)$**: From $a_{DH} * \Lambda_{DH} = (a_{DH} \log n)$, we have $\Lambda_{DH}(2) = \kappa\log 2 \approx +0.19690878$, $\Lambda_{DH}(3) = -\kappa\log 3 \approx -0.31209172$, $\Lambda_{DH}(4) = -(2 + \kappa^2)\log 2 \approx -1.44223168$ (prime-$2$ tower failure), $\Lambda_{DH}(5) = 0$, $\Lambda_{DH}(6) = (1 + \kappa^2)\log 6 \approx +1.93635580 \ne 0$ (composite non-vanishing), $\Lambda_{DH}(8) = \kappa^3\log 2 \approx +0.01589098$, and $\Lambda_{DH}(9) = -(2 + \kappa^2)\log 3 \approx -2.28588435$.
2. **Sign Reversal of the Filtered Zero-Shift Diagonal**: Convolving with $L_{\{2, 3\}}$ yields
   $$C_{\mathrm{diag}, DH}(\{2, 3\}) = \frac{4}{3}\Lambda_{DH}(2) + \Lambda_{DH}(3) - \frac{1}{3}\Lambda_{DH}(6) = \kappa\!\left(\frac{4\log 2}{3} - \log 3\right) - \frac{1 + \kappa^2}{3}\log 6 = -0.6949999697 < 0,$$
   compared to $C_{\mathrm{diag}, \zeta}(\{2, 3\}) = +2.0228085810 > 0$.
3. **Emergence of the Non-Collapsing Prime-$2$ Tower Shift $r = 4/3$**: In $q_{\mathrm{terms}, DH}$, the shift $r = 4/3$ ($\tau = \log(4/3) \approx 0.287682 < 0.40$, which vanishes identically for $\zeta(s)$ by prime-$2$ tower telescoping) appears with a large negative coefficient $c_{4/3, DH} = -0.68364053$, inflating the active shift tail penalty $\sum_{0 < \tau_r < 2b} \nu(\tau_r, b)|c_{r, DH}|$ to $0.854236$ ($2b = 0.40$) and $1.410400$ ($2b \in \{0.45, 0.50\}$).
4. **Failure of the Sufficient Tail Positivity Certificate**: Both the global-multiplier sufficient tail lower-bound budget $\alpha_{DH}(R_{DH})\sigma_{\min}(L_{\mathcal{P}_2}) + C_{\mathrm{diag}, DH}(\{2, 3\}) = -0.687957 < 0$ (and $-1.542193, -2.098356$ after subtracting the shift penalty and Poisson–Bessel defect) and the localized sufficient tail lower-bound budget $\alpha_{DH}(R_{DH})\lambda_{\min}(L_{\mathrm{loc}}(b)) + C_{\mathrm{diag}, DH}(\{2, 3\}) - \sum \nu(\tau_r, b)|c_{r, DH}|$ ($-0.630008$ at $2b = 0.40$, $-1.373808$ at $2b \in \{0.45, 0.50\}$) are **strictly negative**. Under arithmetic substitution against the $\zeta$-archimedean block, the $(0, 0)$ entry is $-1.930740$ ($2b = 0.40$), $-2.049819$ ($2b = 0.45$), and $-2.160782$ ($2b = 0.50$). *(Scope qualification: a negative lower-bound budget certifies that the sufficient tail positivity certificate fails on $f_{DH}(s)$; actual negative Rayleigh quotients $Q_{\{2,3\}, DH}(g_b) < 0$ on the odd-character completion $\alpha_{DH}(\xi) = \operatorname{Re}\psi(3/4 + i\xi/2) + \log(5/\pi)$ are certified at $b \in \{2, 5/2, 3\}$ in Milestone 9.)*

---

> **Wall check**: This package does **NOT** prove `RH`, `G2`, or the cofinal prime-shift lower bound as $a \to \infty$ (or $K \to \infty$). Both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
