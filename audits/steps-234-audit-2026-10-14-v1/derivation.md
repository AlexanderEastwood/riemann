# Mathematical Derivations: Tasks 2, 3, and 4 (2026-10-14, v1)

**Wall check: Known wall** for the general single-power bilinear logarithmic-derivative hierarchy in `ZERO-GEOMETRY` (`PR #72`, `NS-101`) and for universal $n^{-3}$-weighted recovery on $V_{2N}\cap V_N^\perp$ in `NB-GAIN`/`COEFF` (`NS-61`); **Same open gap** for `KERNEL-API` / `WEIL-FLOOR` (`NS-50/51/55/57/58`, `PR #63`) and for the actual `NB-GAIN` optimizer (`NS-53/61/78/80/87`). What changes:
1. In `ZERO-GEOMETRY`, we prove the **General Bilinear Single-Power Obstruction Theorem** via the Bell-polynomial triangular isomorphism $\Phi_M$, establishing that any polynomial in the higher logarithmic derivatives $\mathbf{P}(2(p+t)), \mathbf{P}(2(p-t))$ whose denominator is cleared by a single power of $K(p,t) = \phi(p+t)\phi(p-t)$ lies in the Bell subspace $\operatorname{span}\{Y_m(\mathbf{P}(p+t))Y_n(\mathbf{P}(p-t))\}$ and collapses identically to $\sum_{m,n} c_{mn}\phi^{(m)}(p+t)\phi^{(n)}(p-t)$, while the Planat–Solé Jacobi ODE polynomial $\mathcal{J}_{\mathrm{PS}}(P_0, P_1, P_2)$ has an irreducible degree-3 non-Bell remainder $\frac{9}{8}D_1 D_2 - \frac{3}{4}D_1^3 - 2c_1 D_1^2$.
2. In `NB-GAIN`/`COEFF`, we deliver `audits/coeff-specialist-brief-2026-10-14-v3.html`, incorporating the `NS-61` refutation of universal $n^{-3}$ recovery and the exact untruncated Schur–Rayleigh reduction for $\psi_N(t) = -t^2(t\beta_N'(t))'$.
3. In `KERNEL-API`, we prove the **Three-Island Gap and Exact Prime Diagonalization Theorem** on $\log 2 < a \le \frac{1}{2}\log 5$ ($q_{\mathrm{prime}}[L_2 g] \equiv \frac{5\log 2}{2}\|g\|_2^2$), prove low-frequency indefiniteness of the unrestricted symbol $M_a(0) < 0$, and establish **explicit finite-window separation of the `NS-57` control ($\delta_2 = -\frac{\log 2}{100}$) at $a = \log 3$** on the 2D even interior subspace $\operatorname{span}\{L_2 g_1^+, L_2 g_2^+\} \subset V_{\log 3}$ ($\lambda_{\min}^{\mathrm{NS57}}(\log 3) = -0.0268795922 < 0$ vs. $\lambda_{\min}^{\mathrm{orig}}(\log 3) = +0.0023039536 > 0$, locating $a_*^+(\mathrm{NS57}) \in (\frac{1}{2}\log 7, \log 3)$).
**RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.

---

## 1. Task 2 (`ZERO-GEOMETRY`): The General Bilinear Single-Power Obstruction Theorem

### 1.1 Jet setup and the Bell-polynomial triangular isomorphism

Let $\phi : \mathbb{R} \to (0, \infty)$ be a smooth positive even kernel with rapid decay and two-sided Laplace/Fourier transform $f(z) = \int_{-\infty}^\infty \phi(u)e^{zu}\,du$. In `01-jacobi-transfer.md` (`PR #72`), with $w = 2u$ and $G(w) = \log \phi(w/2)$, the logarithmic derivative hierarchy is defined by
$$P_k(u) := \left.\frac{d^k}{dw^k} P(w)\right|_{w=2u} = 2^{-(k+1)} \frac{d^{k+1}}{du^{k+1}} \log \phi(u), \qquad k \ge 0,$$
and the normalized linear derivatives of $\phi$ are defined by
$$D_m(u) := \frac{\phi^{(m)}(u)}{\phi(u)}, \qquad m \ge 1, \quad D_0(u) := 1.$$

**Lemma 1.1 (Bell-Polynomial Triangular Isomorphism).** *For every integer $M \ge 1$:*
1. *Each normalized linear derivative $D_m$ ($1 \le m \le M$) is given in terms of $(P_0, \dots, P_{m-1})$ by the complete exponential Bell polynomial $Y_m$:*
   $$D_m = 2^m Y_m(P_0, P_1, \dots, P_{m-1}) = 2^m P_{m-1} + 2^m \widetilde{Y}_m(P_0, \dots, P_{m-2}), \tag{1.1}$$
   *where $\widetilde{Y}_m \in \mathbb{Z}_{\ge 0}[P_0, \dots, P_{m-2}]$ has zero constant and linear part (every monomial in $\widetilde{Y}_m$ has total degree $\ge 2$ and partition weight $m$).*
2. *The polynomial map $\Phi_M : \mathbb{Q}[P_0, \dots, P_{M-1}] \to \mathbb{Q}[D_1, \dots, D_M]$ defined by (1.1) is an invertible triangular polynomial isomorphism over $\mathbb{Q}$, with recursive inverse*
   $$P_{m-1} = 2^{-m} D_m - \widetilde{Y}_m\bigl(P_0(D_1), \dots, P_{m-2}(D_1, \dots, D_{m-1})\bigr). \tag{1.2}$$
   *Explicitly, for $1 \le m \le 4$:*
   $$\begin{aligned}
   D_1 &= 2 P_0, & P_0 &= \tfrac{1}{2} D_1, \\
   D_2 &= 4 P_0^2 + 4 P_1, & P_1 &= \tfrac{1}{4} D_2 - \tfrac{1}{4} D_1^2, \\
   D_3 &= 8 P_0^3 + 24 P_0 P_1 + 8 P_2, & P_2 &= \tfrac{1}{8} D_3 - \tfrac{3}{8} D_1 D_2 + \tfrac{1}{4} D_1^3, \\
   D_4 &= 16 P_0^4 + 96 P_0^2 P_1 + 48 P_1^2 + 64 P_0 P_2 + 16 P_3, & P_3 &= \tfrac{1}{16} D_4 - \tfrac{1}{4} D_1 D_3 - \tfrac{3}{16} D_2^2 + \tfrac{3}{4} D_1^2 D_2 - \tfrac{3}{8} D_1^4.
   \end{aligned}$$

*Proof.* Writing $\phi(u) = \exp(\log\phi(u))$ and applying Faà di Bruno's formula with $\frac{d^j}{du^j}\log\phi(u) = 2^j P_{j-1}(u)$ gives $D_m = Y_m(2P_0, 2^2 P_1, \dots, 2^m P_{m-1}) = 2^m Y_m(P_0, \dots, P_{m-1})$ by the weight-$m$ homogeneity of $Y_m$. The single-block partition of $m$ contributes $P_{m-1}$ with coefficient $1$, while all multi-block partitions involve only $P_0, \dots, P_{m-2}$ with total degree $\ge 2$. Triangular invertibility (1.2) follows immediately by induction on $m$. $\square$

### 1.2 Theorem (General Bilinear Single-Power Obstruction)

**Theorem 1.2.** *In the universal jet ring $\mathcal{R}_M = \mathbb{Q}[\phi, \phi^{-1}, \phi', \dots, \phi^{(M)}]$:*
1. *(Univariate single-power denominator clearing)* *A polynomial $A(P_0, \dots, P_{M-1}) \in \mathbb{Q}[P_0, \dots, P_{M-1}]$ satisfies $\phi(u)\,A(P_0(u), \dots, P_{M-1}(u)) \in \mathbb{Q}[\phi(u), \phi'(u), \dots, \phi^{(M)}(u)]$ **if and only if** $\widehat{A}(D_1, \dots, D_M) := A(\Phi_M^{-1}(D_1, \dots, D_M))$ has total degree $\le 1$ in $(D_1, \dots, D_M)$, i.e.,*
   $$A(P_0, \dots, P_{M-1}) = c_0 + \sum_{m=1}^M c_m 2^m Y_m(P_0, \dots, P_{m-1}) \quad \Longleftrightarrow \quad \phi(u)\,A(\mathbf{P}(u)) = \sum_{m=0}^M c_m \phi^{(m)}(u). \tag{1.3}$$
2. *(Bilinear single-power collapse)* *For any two-point polynomial $\mathcal{Q}(\mathbf{P}(p+t); \mathbf{P}(p-t))$ in $P_0, \dots, P_{M-1}$ at $u = p+t$ and $P_0, \dots, P_{N-1}$ at $v = p-t$, multiplication by a single power of the product kernel $K(p,t) = \phi(p+t)\phi(p-t)$ clears the denominators $\phi(p+t), \phi(p-t)$ in the universal jet ring **if and only if** $\mathcal{Q}$ belongs to the $(M+1)(N+1)$-dimensional Bell subspace*
   $$\mathcal{Q}\bigl(\mathbf{P}(u); \mathbf{P}(v)\bigr) = \sum_{m=0}^M \sum_{n=0}^N c_{mn}\, 2^{m+n} Y_m(\mathbf{P}(u))\,Y_n(\mathbf{P}(v)), \tag{1.4}$$
   *in which case the integrand collapses tautologically to the linear-derivative bilinear form*
   $$\mathcal{Q}\bigl(\mathbf{P}(p+t); \mathbf{P}(p-t)\bigr)\,K(p,t) \equiv \sum_{m=0}^M \sum_{n=0}^N c_{mn}\,\phi^{(m)}(p+t)\,\phi^{(n)}(p-t), \tag{1.5}$$
   *and its strip Laplace–Fourier integral satisfies the universal identity*
   $$4\int_{-\infty}^\infty \int_0^\infty \mathcal{Q}\bigl(\mathbf{P}(p+t); \mathbf{P}(p-t)\bigr) K(p,t)\cos(2rt)e^{2xp}\,dt\,dp = \operatorname{Re}\!\left(\sum_{m=0}^M \sum_{n=0}^N c_{mn}(-z)^m(-\bar{z})^n |f(z)|^2\right) \tag{1.6}$$
   *for $z = x+ir$ and every smooth rapidly decaying even kernel $\phi$ (including Davenport–Heilbronn and `NS-101`).*

*Proof.* Under the isomorphism $\Phi_M$, any polynomial $A(\mathbf{P})$ is uniquely represented as $\widehat{A}(D_1, \dots, D_M) = \sum_\alpha a_\alpha D_1^{\alpha_1}\cdots D_M^{\alpha_M}$. Since $D_m = \phi^{(m)}/\phi$ and the jets $\phi, \phi', \dots, \phi^{(M)}$ are algebraically independent over $\mathbb{Q}$, the monomial $D_1^{\alpha_1}\cdots D_M^{\alpha_M} = \phi^{-|\alpha|} (\phi')^{\alpha_1}\cdots(\phi^{(M)})^{\alpha_M}$ has exact denominator degree $|\alpha| = \alpha_1 + \dots + \alpha_M$ in $\phi$. Multiplication by $\phi^1$ clears $\phi^{-|\alpha|}$ if and only if $|\alpha| \le 1$ for every nonzero monomial in $\widehat{A}$, proving (1.3). Applying (1.3) in each variable $u = p+t$ and $v = p-t$ yields (1.4)–(1.5). Finally, changing variables to $u = p+t, v = p-t$ ($du\,dv = 2\,dp\,dt$, $2xp \pm 2irt = zu + \bar{z}v$) factors the integral (1.6) into $\operatorname{Re}\sum_{m,n} c_{mn}\bigl(\int_{\mathbb{R}} \phi^{(m)}(u)e^{zu}\,du\bigr)\bigl(\int_{\mathbb{R}} \phi^{(n)}(v)e^{\bar{z}v}\,dv\bigr) = \operatorname{Re}\sum_{m,n} c_{mn}(-z)^m(-\bar{z})^n |f(z)|^2$. $\square$

### 1.3 Corollary (Exclusion of the Planat–Solé Jacobi ODE from the Single-Power Subspace)

In `01-jacobi-transfer.md` (`PR #72`), the Planat–Solé Jacobi differential polynomial is
$$\mathcal{J}_{\mathrm{PS}}(P_0, P_1, P_2) := P_2 + 12 P_0 P_1 + 4 P_0^3 - 4 c_1 P_1 - 12 c_1 P_0^2 + c_2 P_0 + c_3.$$
Substituting the inverse Bell isomorphism (1.2) yields the exact decomposition into its degree-$\le 1$ Bell projection and its degree-$3$ non-Bell remainder:
$$\mathcal{J}_{\mathrm{PS}}\bigl(\Phi_3^{-1}(D_1, D_2, D_3)\bigr) = \underbrace{\left(\frac{1}{8} D_3 - c_1 D_2 + \frac{c_2}{2} D_1 + c_3\right)}_{\text{Bell projection (cleared by }\phi^1\text{)}} + \underbrace{\left(\frac{9}{8} D_1 D_2 - \frac{3}{4} D_1^3 - 2 c_1 D_1^2\right)}_{\text{non-Bell remainder (pole order }\phi^{-3}\text{)}}. \tag{1.7}$$
Because the non-Bell remainder $\frac{9\phi'\phi''}{8\phi^2} - \frac{3(\phi')^3}{4\phi^3} - \frac{2c_1(\phi')^2}{\phi^2}$ has pole order $3$ in $\phi$, multiplying $\mathcal{J}_{\mathrm{PS}}$ by a single power of $\phi$ leaves uncancelled denominators $\phi^{-1}$ and $\phi^{-2}$, whereas clearing denominators with $\phi(p+t)^3\phi(p-t)^3 = K(p,t)^3$ converts the Fourier–Laplace transform into a 6-fold frequency convolution of $f(z)$ rather than a quadratic $|f(z)|^2$ energy identity.

---

## 2. Task 3 (`NB-GAIN` / `COEFF`): Specialist Brief v3 and the Untruncated Dual Extractor

The separately versioned specialist brief is delivered at `audits/coeff-specialist-brief-2026-10-14-v3.html` (preserving `v1` and `v2`). It records:
1. **`NS-61` refutation of universal $n^{-3}$ recovery (`Known wall` for `R3(perp)`)**: For $N+2 \le n \le 2N-1$, the adjacent second-difference vector $W_n = \varepsilon_{n+1} - \frac{n}{n+1}\varepsilon_n = \sigma_{n+1} - \frac{2n}{n+1}\sigma_n + \frac{n-1}{n+1}\sigma_{n-1}$ is supported purely in the new block $\{N+1, \dots, 2N\}$, satisfies $\sum_{k=N+1}^{2N} |y_k|^2/k^3 \sim 6/n^3$ (`5.9883 / n^3` at $n=1024$), and has $n^3 \|(I-\Pi_N)W_n\|_{\mathcal{H}}^2 \le n^3 \|W_n\|_{\mathcal{H}}^2 \to 0$ by strong continuity of dilations on $L^2$.
2. **Untruncated Schur–Rayleigh reduction for $\psi_N(t) = -t^2(t\beta_N'(t))'$**: With $b(s) = (s-1)^3(2-s)^3(2s-3)\mathbf{1}_{[1,2]}(s)$, exact rational polynomial integration (`verify_steps_234.py`) gives
   $$C_b = \frac{6904}{45045}, \qquad \operatorname{Var}_{\mathbb{R}}(b''') = \frac{543}{14}, \qquad A_b = \frac{181}{3360}, \qquad I_{\mathrm{diag}} = \frac{1219}{38798760},$$
   and on $V_{2N}\cap V_N^\perp$, $M_N(u,y) = \tilde{\lambda}_N^T y = \tilde{\lambda}_N^T S^{-1} h = \langle (\Pi_{2N}-\Pi_N)\psi_N, \tau \rangle_{\mathcal{H}}$ satisfies
   $$\Delta_N = h^T S^{-1} h \ge \frac{(\tilde{\lambda}_N^T S^{-1} h)^2}{\tilde{\lambda}_N^T S^{-1}\tilde{\lambda}_N} \ge \frac{|M_N(u,y)|^2}{C_b N}$$
   without low-old alias truncation at $K = \lfloor\sqrt{N}\rfloor$ and without the `NS-78` constant $B = 1536\zeta(2)^2$.

---

## 3. Task 4 (`KERNEL-API`): Single-Prime $p=2$ Interior Archimedean Dominance Screen on $V_{a-\log 2}$

### 3.1 Exact pole-free interior form and the Three-Island Gap Theorem

For $\ell_2 = \log 2$, $r_2 = 2^{-1/2}$, and $a > \ell_2$, set $b := a - \ell_2 > 0$ and let $L_2 = \frac{3}{2}I - 2^{-1/2}(T_{\ell_2} + T_{-\ell_2}) : V_b \to V_a$. For every $g \in V_b$ ($\operatorname{supp}(g) \subset [-b, b]$), $f = L_2 g$ has $\operatorname{supp}(f) \subset [-a, a]$, $K_{\mathrm{pole}}(L_2 g) = 0$ identically, and $(C_2 - I)L_2 = \frac{1}{2}I - L_2$. Thus the complete Weil quadratic form on $L_2 g$ is
$$q[L_2 g] = \left\langle L_2^2 \alpha(D) g, g \right\rangle - (\log 2)\left\langle \left(\frac{1}{2}L_2 - L_2^2\right) g, g \right\rangle - \sum_{\substack{q \ge 3\text{ prime},\, m \ge 1 \\ m\log q < 2a}} \frac{\log q}{q^{m/2}} \left\langle (T_{m\log q} + T_{-m\log q}) L_2 g, L_2 g \right\rangle. \tag{3.1}$$
In the Fourier domain ($\widehat{g}(\xi) = \int_{-b}^b g(x)e^{-i\xi x}\,dx$, $\sigma(L_2)(\xi) = \frac{3}{2} - \sqrt{2}\cos(\xi\log 2)$), (3.1) equals $\int_{\mathbb{R}} M_a(\xi)|\widehat{g}(\xi)|^2\,\frac{d\xi}{2\pi}$ with
$$M_a(\xi) = \sigma(L_2)(\xi)^2\left[\alpha(\xi) - \sum_{\substack{q \ge 3,\, m \ge 1 \\ m\log q < 2a}} \frac{2\log q}{q^{m/2}}\cos(m\xi\log q)\right] - (\log 2)\,\sigma(L_2)(\xi)\left(\frac{1}{2} - \sigma(L_2)(\xi)\right). \tag{3.2}$$

**Proposition 3.1 (Low-Frequency Indefiniteness of the Unrestricted Symbol $M_a(\xi)$).** *Because $K_{\mathrm{pole}} L_2 = 0$ removes the positive even pole stabilization at $\xi = 0$, the unrestricted symbol $M_a(\xi)$ is strictly negative at $\xi = 0$ for every $a > \log 2$:*
- *For $\log 2 < a \le \frac{1}{2}\log 5$: $M_a(0) \approx -0.07350160 < 0$ (and $M_a^{\mathrm{NS57}}(0) \approx -0.07339957 < 0$).*
- *For $\frac{1}{2}\log 5 < a \le \frac{1}{2}\log 7$: $M_a(0) \approx -0.08409551 < 0$.*
- *For $\frac{1}{2}\log 7 < a \le \log 3$: $M_a(0) \approx -0.09492084 < 0$.*
*Hence positivity of $q[L_2 g]$ on $V_{a-\log 2}$ cannot hold as a pointwise multiplier inequality on $L^2(\mathbb{R})$; it relies essentially on the compact-support confinement $\operatorname{supp}(g) \subset [-b, b]$.*

**Theorem 3.2 (Three-Island Gap and Exact Prime Diagonalization on $\log 2 < a \le \frac{1}{2}\log 5$).** *For every window $a \in (\log 2, \frac{1}{2}\log 5]$ (so $0 < 2b = 2(a - \log 2) \le \log(5/4) \approx 0.223144$) and every $g \in V_{a-\log 2}$:*
1. *The support of $f = L_2 g$ is contained in three disjoint islands $[-\ell_2-b, -\ell_2+b] \cup [-b, b] \cup [\ell_2-b, \ell_2+b]$, so $\langle (T_\tau + T_{-\tau}) L_2 g, L_2 g \rangle$ can be nonzero only if $\min_{s \in \{0,1,2\}} |\tau - s\log 2| < 2b \le \log(5/4)$.*
2. *Every odd prime power $n = q^m$ ($q \ge 3$) satisfies $\min_{s \in \{0,1,2\}} |\log n - s\log 2| \ge \log(5/4)$ (since $q=3$ has $|\log 3 - \log 4| = \log(4/3) > \log(5/4)$ and $q=5$ has $|\log 5 - \log 4| = \log(5/4)$), so **every odd prime power $q^m$ ($q \ge 3$) vanishes identically** on $L_2(V_{a-\log 2})$!*
3. *Furthermore, because $\log 2 > \log(5/4) \ge 2b$, all nonzero shifts in $\langle L_2 g, g \rangle$ and $\langle L_2^2 g, g \rangle$ vanish, reducing the entire prime-power quadratic form on $V_{a-\log 2}$ to an exact positive scalar multiple of the $L^2(-b,b)$ norm:*
   $$q_{\mathrm{prime}}[L_2 g] \equiv -(\log 2)\left(\frac{1}{2}\cdot\frac{3}{2} - \frac{13}{4}\right)\|g\|_{L^2(-b,b)}^2 = +\frac{5\log 2}{2}\,\|g\|_{L^2(-b,b)}^2 \approx 1.73286795\,\|g\|_{L^2(-b,b)}^2. \tag{3.3}$$

### 3.2 Exact spatial archimedean reduction and constructive separation of `NS-57` at $a = \log 3$

Using the exact elementary identity $2\int_{2a}^\infty \frac{e^{t/2}}{2\sinh t}\,dt = \log\frac{1+e^{-a}}{1-e^{-a}} + 2\arctan(e^{-a})$, the archimedean form on $f_j = L_2 g_j, f_k = L_2 g_k$ ($g_j, g_k \in V_b$) reduces to a finite piecewise-analytic integral over $[0, 2a]$:
$$q_{\mathrm{arch}}(L_2 g_j, L_2 g_k) = \left(\psi\!\left(\frac{1}{4}\right) - \log\pi + \log\frac{1+e^{-a}}{1-e^{-a}} + 2\arctan(e^{-a})\right) c_{j,k}(0) + \int_0^{2a} \frac{e^{t/2}}{\sinh t}\bigl(c_{j,k}(0) - c_{j,k}(t)\bigr)\,dt, \tag{3.4}$$
where $c_{j,k}(t) = \frac{1}{2}\langle (T_t + T_{-t}) L_2 g_j, L_2 g_k \rangle$. Evaluating (3.1) and (3.4) on the orthonormal Dirichlet basis $g_k^+(x) = b^{-1/2}\cos\bigl(\frac{(2k-1)\pi x}{2b}\bigr)\mathbf{1}_{[-b,b]}(x)$ ($k=1,2$) and $g_1^-(x) = b^{-1/2}\sin\bigl(\frac{\pi x}{b}\bigr)\mathbf{1}_{[-b,b]}(x)$ across $\log 2 < a \le \log 3$ (`verify_steps_234.py`, 60-digit working precision) yields:

| Window $a$ | $b = a - \log 2$ | $\frac{\pi}{2b}$ | Active odd $q^m < e^{2a}$ | Even $2\times 2$ $\lambda_{\min}^{\mathrm{orig}}$ | Even $2\times 2$ $\lambda_{\min}^{\mathrm{NS57}}$ | Odd $k=1$ $q^{\mathrm{orig}}$ | Odd $k=1$ $q^{\mathrm{NS57}}$ |
|---|---:|---:|---|---:|---:|---:|---:|
| $0.75$ | $0.056853$ | $27.6292$ | $\{3\}$ (gap: $0$ overlap) | $+4.46867804$ | $+4.43927029$ | $+8.13754251$ | $+8.10813476$ |
| $\frac{1}{2}\log 5 \approx 0.804719$ | $0.111572$ | $14.0788$ | $\{3\}$ (gap: $0$ overlap) | $+2.54047166$ | $+2.51106392$ | $+5.93965990$ | $+5.91025216$ |
| $0.90$ | $0.206853$ | $7.5938$ | $\{3, 5\}$ | $+0.66064473$ | $+0.63123698$ | $+4.39662431$ | $+4.36721656$ |
| $\frac{1}{2}\log 7 \approx 0.972955$ | $0.279808$ | $5.6138$ | $\{3, 5\}$ | $+0.10578924$ | $+0.07638149$ | $+2.85982229$ | $+2.83041455$ |
| $\log 3 \approx 1.098612$ | $0.405465$ | $3.8741$ | $\{3, 5, 7\}$ | **$+0.00230395$** | **$-0.02687959$** | $+0.16809537$ | $+0.13676094$ |

**Constructive Separation of `NS-57` at $a = \log 3$:**
1. At $a = \log 3$ ($b = \log(3/2) \approx 0.405465$), both even Dirichlet frequencies $w_1 = \frac{\pi}{2b} \approx 3.8741$ and $w_2 = \frac{3\pi}{2b} \approx 11.6222$ lie strictly below the first Riemann zero $\gamma_1 \approx 14.134725$, while $w_1 \approx 3.8741$ sits inside `NS-57`'s negative perturbation band $\left(\frac{2\pi}{3\log 2}, \frac{4\pi}{3\log 2}\right) \approx (3.0216, 6.0431)$ where $\cos(w_1\log 2) \approx -0.8967 < 0$.
2. For the **original Riemann $\xi$ function**, the $2\times 2$ even interior matrix at $a = \log 3$ is
   $$M_{\mathrm{orig}}(\log 3) = \begin{pmatrix} +0.057304815 & -0.454863832 \\ -0.454863832 & +3.764083291 \end{pmatrix}, \qquad \det M_{\mathrm{orig}}(\log 3) = +0.008798993 > 0, \qquad \lambda_{\min}^{\mathrm{orig}}(\log 3) = +0.002303954 > 0,$$
   which agrees with the explicit-formula zero sum $\sum_{k=1}^{59} 2\,\sigma(L_2)(\gamma_k)^2 \widehat{g_j^+}(\gamma_k)\widehat{g_k^+}(\gamma_k)$ (`M00 = 0.05728014`, `M01 = -0.45478962`, `M11 = 3.76386006`, `lambda_min = +0.00229411 > 0`).
3. For the **`NS-57` control ($\delta_2 = -\frac{\log 2}{100}$)** on the exact same 2D subspace $\operatorname{span}\{L_2 g_1^+, L_2 g_2^+\} \subset H^1_0(-\log 3, \log 3) \subset V_{\log 3}$, the matrix is
   $$M_{\mathrm{NS57}}(\log 3) = \begin{pmatrix} +0.028410279 & -0.464821578 \\ -0.464821578 & +3.758272276 \end{pmatrix}, \qquad \det M_{\mathrm{NS57}}(\log 3) = -0.101977278 < 0, \qquad \lambda_{\min}^{\mathrm{NS57}}(\log 3) = -0.026879592 < 0.$$
   Thus the eigenvector $g_* \in \operatorname{span}\{g_1^+, g_2^+\}$ provides an **explicit, elementary, two-mode trigonometric negative test vector $f_* = L_2 g_* \in V_{\log 3}$ for `NS-57`**, constructively bounding `NS-57`'s even first-zero window inside Sub-window III:
   $$\frac{1}{2}\log 7 \approx 0.972955 < a_*^+(\mathrm{NS57}) < \log 3 \approx 1.098612.$$
4. **Why `KERNEL-API` remains at `Same open gap`**: While $L_2 : V_{a-\log 2} \to V_a$ eliminates the pole kernel $K_{\mathrm{pole}}$, collapses the $2$-chain, diagonalizes the prime form on $\log 2 < a \le \frac{1}{2}\log 5$, and constructively separates `NS-57` from Riemann $\xi$ at $a = \log 3$, as $a$ increases past $\log 3$ the original minimum eigenvalue $\lambda_{\min}^{\mathrm{orig}}(a)$ decays rapidly toward zero (`0.002304` at $a=\log 3$, `0.000305` at $a=1.20$, `0.000024` at $a=1.40$) as higher Dirichlet modes cancel low frequencies below $\gamma_1 \approx 14.1347$, and by the **Multi-Prime Interior Support Barrier** (`four-lane-audit-2026-10-14-v1`, §2.2), every larger window activates additional odd prime chains $q \notin \mathcal{P}$ that cannot be cleared by finite interior Euler products alone.
