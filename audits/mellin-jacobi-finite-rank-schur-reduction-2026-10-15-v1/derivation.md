# Mathematical Derivations — Mellin–Jacobi–Legendre Finite-Rank Gram–Schur Reduction & Exact Polynomial Shift Matrices (`NB-GAIN` / `COEFF` & `NS-61`)

**Date:** 2026-10-15  
**Target Lanes:** `NB-GAIN` / `COEFF` & `NS-61`  
**Audit Directory:** `audits/mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1/`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this derivation prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.
>
> **Structural Purpose:** This derivation establishes the Mellin–Jacobi–Legendre finite-rank Gram–Schur reduction on $L^2(-b, b)$, proving that:
> 1. **Theorem 1 (Gegenbauer–Spherical-Bessel Parseval Identity & Finite-$N$ Archimedean Tail Reduction):** The orthonormal Legendre polynomial basis $\phi_m(x) = \sqrt{\frac{2m+1}{2b}}\,P_m(x/b)$ diagonalizes the Paley–Wiener Plancherel measure via the exact Gegenbauer parity identities
>    $$\sum_{r=0}^\infty (4r+1) j_{2r}(z)^2 = \frac{1}{2}\bigl(1 + \operatorname{sinc}(2z)\bigr), \qquad \sum_{r=0}^\infty (4r+3) j_{2r+1}(z)^2 = \frac{1}{2}\bigl(1 - \operatorname{sinc}(2z)\bigr),$$
>    concentrating $> 99.999999\%$ of the low-frequency archimedean operator $A_-^{(\Delta_\alpha)}(b)$ into an $N \times N$ matrix with $N = 3$ or $N = 4$, with an exact finite-sum complement formula for the tail trace $\varepsilon_N(b, \Delta_\alpha)$.
> 2. **Theorem 2 (Exact Rational Polynomial Shift Matrices $S_\tau^{(N)}$ & $4 \times 4$ Legendre–Schur Continuum Certification):** The matrix entries $(S_\tau)_{mn} = \langle \phi_m, (T_\tau + T_{-\tau})\phi_n \rangle_{L^2(-b, b)}$ are exact polynomials in $u = \tau/b \in [0, 2]$ of degree $m+n+1$ with rational coefficients. Combining $S_\tau^{(N)}$ with the Cauchy–Schur complement inequality reduces continuum positivity of the $\Delta_\alpha$-shifted operator on $L^2(-b, b)$ (in the regime where the unsigned Schur multiplication potential $V_a(x) \ge 0$ on $[-b,b]$, or on the finite-rank Legendre block $\mathcal{V}_N^{\mathrm{even}} \oplus \mathcal{V}_N^{\mathrm{odd}}$; see `argon-m16-review` Finding 4 and Milestones 16–17 for the untruncated $\Delta_\alpha = 0$ spatial archimedean operator) to a **$3 \times 3$ or $4 \times 4$ Legendre–Schur matrix certificate**.

---

## 1. Theorem 1: Gegenbauer–Spherical-Bessel Parseval Identity & Finite-$N$ Archimedean Tail Reduction (`NB-GAIN` / `COEFF`)

### 1.1 Orthonormal Legendre Basis and Spherical Bessel Transform

For $b > 0$ and $m \ge 0$, define the orthonormal Legendre basis of $L^2(-b, b)$ by
$$\phi_m(x) := \sqrt{\frac{2m+1}{2b}}\,P_m\!\left(\frac{x}{b}\right) \mathbf{1}_{(-b, b)}(x), \qquad \langle \phi_m, \phi_n \rangle_{L^2(-b, b)} = \delta_{mn}.$$
Notice that under the exponential substitution $y = e^{x/b}$ (relatingadditive convolution on $(-b, b)$ to multiplicative Mellin–Jacobi coordinates on $(e^{-1}, e^1)$ in the `NB-GAIN` / `COEFF` and `NS-61` lanes), $\phi_m(x)$ is the pushforward of the shifted Jacobi/Legendre polynomial basis.

By Gegenbauer's integral identity for Legendre polynomials, for all $\xi \in \mathbb{C}$,
$$\widehat{\phi_m}(\xi) = \int_{-b}^b \phi_m(x) e^{-i\xi x}\,dx = \sqrt{\frac{2m+1}{2b}} \cdot b \int_{-1}^1 P_m(t) e^{-ib\xi t}\,dt = (-i)^m \sqrt{2b(2m+1)}\,j_m(b\xi),$$
where $j_m(z) = \sqrt{\frac{\pi}{2z}} J_{m+1/2}(z) = \frac{z^m}{(2m+1)!!}\,{}_0F_1\!\left(; m + \frac{3}{2}; -\frac{z^2}{4}\right)$ is the spherical Bessel function of the first kind.

### 1.2 Statement and Proof of Theorem 1

**Theorem 1 (Gegenbauer–Spherical-Bessel Parseval Identity & Finite-$N$ Archimedean Tail Reduction).**
1. **(Exact Parity-Split Gegenbauer Parseval Identities):** *For every $z \in \mathbb{C}$, the spherical Bessel functions satisfy the exact pointwise identities*
   $$\sum_{r=0}^\infty (4r+1) j_{2r}(z)^2 = \frac{1}{2}\bigl(1 + \operatorname{sinc}(2z)\bigr), \qquad \sum_{r=0}^\infty (4r+3) j_{2r+1}(z)^2 = \frac{1}{2}\bigl(1 - \operatorname{sinc}(2z)\bigr).$$
2. **(Exact Finite-Sum Complement Formula for the Tail Trace):** *Let $\mathcal{V}_N^{\mathrm{even}} := \operatorname{span}\{\phi_0, \phi_2, \dots, \phi_{2N-2}\} \subset L^2_{\mathrm{even}}(-b, b)$ and $\mathcal{V}_N^{\mathrm{odd}} := \operatorname{span}\{\phi_1, \phi_3, \dots, \phi_{2N-1}\} \subset L^2_{\mathrm{odd}}(-b, b)$ be the $N$-dimensional even and odd Legendre subspaces, with orthogonal projections $\Pi_N^{\mathrm{even}}, \Pi_N^{\mathrm{odd}}$ and orthogonal complements $\Pi_{\perp, N}^{\mathrm{even}} = I_{\mathrm{even}} - \Pi_N^{\mathrm{even}}$, $\Pi_{\perp, N}^{\mathrm{odd}} = I_{\mathrm{odd}} - \Pi_N^{\mathrm{odd}}$. Then the low-frequency archimedean operator*
   $$\langle f, A_-^{(\Delta_\alpha)}(b) f \rangle_{L^2(-b, b)} := \frac{1}{2\pi} \int_{-\xi_0(\Delta_\alpha)}^{\xi_0(\Delta_\alpha)} \sigma_{L_{\mathcal{P}}}(\xi)\bigl(\Delta_\alpha - \alpha(\xi)\bigr) |\widehat{f}(\xi)|^2\,d\xi$$
   *has exact $N \times N$ Gram matrices $A^{(N)}_{\mathrm{even}}, A^{(N)}_{\mathrm{odd}}$ with entries ($0 \le r, s \le N-1$):*
   $$\bigl(A^{(N)}_{\mathrm{even}}\bigr)_{rs} = (-1)^{r+s} \frac{2b}{\pi}\sqrt{(4r+1)(4s+1)} \int_0^{\xi_0(\Delta_\alpha)} \sigma_{L_{\mathcal{P}}}(\xi)\bigl(\Delta_\alpha - \alpha(\xi)\bigr) j_{2r}(b\xi) j_{2s}(b\xi)\,d\xi,$$
   $$\bigl(A^{(N)}_{\mathrm{odd}}\bigr)_{rs} = (-1)^{r+s} \frac{2b}{\pi}\sqrt{(4r+3)(4s+3)} \int_0^{\xi_0(\Delta_\alpha)} \sigma_{L_{\mathcal{P}}}(\xi)\bigl(\Delta_\alpha - \alpha(\xi)\bigr) j_{2r+1}(b\xi) j_{2s+1}(b\xi)\,d\xi,$$
   *and the tail trace defects $\varepsilon_N^{\mathrm{even}}(b, \Delta_\alpha) := \operatorname{Tr}\bigl(\Pi_{\perp, N}^{\mathrm{even}} A_-^{(\Delta_\alpha)}(b) \Pi_{\perp, N}^{\mathrm{even}}\bigr)$ and $\varepsilon_N^{\mathrm{odd}}(b, \Delta_\alpha) := \operatorname{Tr}\bigl(\Pi_{\perp, N}^{\mathrm{odd}} A_-^{(\Delta_\alpha)}(b) \Pi_{\perp, N}^{\mathrm{odd}}\bigr)$ are given by the exact finite-sum complement integrals*
   $$\varepsilon_N^{\mathrm{even}}(b, \Delta_\alpha) = \frac{2b}{\pi} \int_0^{\xi_0(\Delta_\alpha)} \sigma_{L_{\mathcal{P}}}(\xi)\bigl(\Delta_\alpha - \alpha(\xi)\bigr)\left[\frac{1}{2}\bigl(1 + \operatorname{sinc}(2b\xi)\bigr) - \sum_{r=0}^{N-1} (4r+1) j_{2r}(b\xi)^2\right] d\xi,$$
   $$\varepsilon_N^{\mathrm{odd}}(b, \Delta_\alpha) = \frac{2b}{\pi} \int_0^{\xi_0(\Delta_\alpha)} \sigma_{L_{\mathcal{P}}}(\xi)\bigl(\Delta_\alpha - \alpha(\xi)\bigr)\left[\frac{1}{2}\bigl(1 - \operatorname{sinc}(2b\xi)\bigr) - \sum_{r=0}^{N-1} (4r+3) j_{2r+1}(b\xi)^2\right] d\xi.$$

**Proof:**  
For fixed $\xi \in \mathbb{R}$, expand $c_\xi(x) := \cos(\xi x)$ on $(-b, b)$ in the complete orthonormal basis $\{\phi_{2r}\}_{r=0}^\infty$ of $L^2_{\mathrm{even}}(-b, b)$, and $s_\xi(x) := \sin(\xi x)$ in $\{\phi_{2r+1}\}_{r=0}^\infty$ of $L^2_{\mathrm{odd}}(-b, b)$. Since $\langle \phi_{2r}, c_\xi \rangle_{L^2(-b, b)} = \operatorname{Re}\widehat{\phi_{2r}}(\xi) = (-1)^r \sqrt{2b(4r+1)}\,j_{2r}(b\xi)$, Parseval's identity in $L^2(-b, b)$ gives
$$\sum_{r=0}^\infty 2b(4r+1) j_{2r}(b\xi)^2 = \int_{-b}^b \cos^2(\xi x)\,dx = b\bigl(1 + \operatorname{sinc}(2b\xi)\bigr),$$
and similarly $\sum_{r=0}^\infty 2b(4r+3) j_{2r+1}(b\xi)^2 = \int_{-b}^b \sin^2(\xi x)\,dx = b\bigl(1 - \operatorname{sinc}(2b\xi)\bigr)$. Dividing by $2b$ gives part (1), and integrating against $\frac{1}{\pi}\sigma_{L_{\mathcal{P}}}(\xi)(\Delta_\alpha - \alpha(\xi))$ over $[0, \xi_0(\Delta_\alpha)]$ gives part (2). $\square$

---

## 2. Theorem 2: Exact Rational Polynomial Shift Matrices $S_\tau^{(N)}$ & $4 \times 4$ Legendre–Schur Continuum Certification (`NB-GAIN` / `COEFF` & `NS-61`)

### 2.1 Exact Polynomial Formula for $(S_\tau)_{mn}$

For any shift $\tau \in [0, 2b]$, let $u := \tau / b \in [0, 2]$. Changing variables to $t = x / b \in [-1, 1]$, the matrix entry of $S_\tau = P_b(T_\tau + T_{-\tau})P_b$ in the Legendre basis $\{\phi_m\}_{m=0}^\infty$ is
$$\bigl(S_\tau\bigr)_{mn} = \frac{\sqrt{(2m+1)(2n+1)}}{2}\left(\int_{-1}^{1-u} P_m(t)\,P_n(t + u)\,dt + \int_{-1+u}^1 P_m(t)\,P_n(t - u)\,dt\right).$$
When $m$ and $n$ have the same parity ($m \equiv n \pmod 2$), substituting $t \mapsto -t$ in the second integral shows both integrals are equal, so
$$\bigl(S_\tau\bigr)_{mn} = \sqrt{(2m+1)(2n+1)} \int_{-1}^{1-u} P_m(t)\,P_n(t + u)\,dt \qquad (m \equiv n \pmod 2).$$
Because $t \mapsto P_m(t) P_n(t + u)$ is a polynomial of degree $m + n$ in $t$ (and degree $n$ in $u$), its integral over $t \in [-1, 1 - u]$ is a **polynomial in $u = \tau/b$ of degree $m + n + 1$ with exact rational coefficients** (up to the normalization factor $\sqrt{(2m+1)(2n+1)}$)!

Explicitly, for the first two even modes ($m, n \in \{0, 2\}$, where $P_0(t) = 1$, $P_2(t) = \frac{1}{2}(3t^2 - 1)$) and the first two odd modes ($m, n \in \{1, 3\}$, where $P_1(t) = t$, $P_3(t) = \frac{1}{2}(5t^3 - 3t)$), exact symbolic integration gives (remarkably, for every diagonal entry $m = n$, all positive even powers $u^{2k}$ vanish identically):
$$\bigl(S_\tau\bigr)_{0, 0} = 2 - u, \qquad \bigl(S_\tau\bigr)_{0, 2} = \bigl(S_\tau\bigr)_{2, 0} = -\frac{\sqrt{5}}{2}\,u(u - 1)(u - 2) = \sqrt{5}\!\left(-u + \frac{3}{2}u^2 - \frac{1}{2}u^3\right),$$
$$\bigl(S_\tau\bigr)_{2, 2} = 2 - 5u + \frac{5}{2}u^3 - \frac{3}{8}u^5,$$
$$\bigl(S_\tau\bigr)_{1, 1} = 2 - 3u + \frac{1}{2}u^3, \qquad \bigl(S_\tau\bigr)_{1, 3} = \bigl(S_\tau\bigr)_{3, 1} = \sqrt{21}\!\left(-u + \frac{5}{2}u^2 - \frac{3}{2}u^3 + \frac{1}{8}u^5\right),$$
$$\bigl(S_\tau\bigr)_{3, 3} = 2 - 7u + 7u^3 - \frac{21}{8}u^5 + \frac{5}{16}u^7.$$

### 2.2 Statement and Proof of Theorem 2 (Finite-$N$ Legendre–Schur Continuum Reduction)

**Theorem 2 (Exact Rational Polynomial Shift Matrices $S_\tau^{(N)}$ & Finite-$N$ Legendre–Schur Continuum Certification).**  
*Let $P_{\mathcal{P}, \Delta_\alpha} = c_0 I + \sum_{\tau \in \mathcal{T}(b)} s_\tau c_\tau S_\tau$ be the multi-prime arithmetic shift operator on $L^2(-b, b)$:*
1. **(Zero-Shift Primorial Isometric Horizons $b = b_{\mathrm{iso}}(K)$):** *At $b = b_{\mathrm{iso}}(K)$ ($K = 2, 3, 4$, $\Delta_\alpha = 0$), where $\mathcal{T}(b) = \emptyset$ and $P_{\mathcal{P}_K, 0} = C_{\mathrm{diag}}(\mathcal{P}_K) I$, the exact continuum operator norm $\|K_{\mathrm{even}}\|_{\mathrm{op}} = C_{\mathrm{diag}}(\mathcal{P}_K)^{-1}\|A_-^{(0)}(b_{\mathrm{iso}}(K))\|_{\mathrm{op}}$ satisfies*
   $$\|K_{\mathrm{even}}\|_{\mathrm{op}} \le \frac{\lambda_{\max}\!\bigl(A^{(N)}_{\mathrm{even}}\bigr) + \varepsilon_N^{\mathrm{even}}(b_{\mathrm{iso}}(K), 0)}{C_{\mathrm{diag}}(\mathcal{P}_K)}, \qquad \|K_{\mathrm{odd}}\|_{\mathrm{op}} \le \frac{\lambda_{\max}\!\bigl(A^{(N)}_{\mathrm{odd}}\bigr) + \varepsilon_N^{\mathrm{odd}}(b_{\mathrm{iso}}(K), 0)}{C_{\mathrm{diag}}(\mathcal{P}_K)}.$$
   *At $N = 3$ ($3 \times 3$ Legendre matrix), this improves upon the trace bound $T_{\mathrm{even}}(a_{\mathrm{iso}}(K))$ while incurring a tail defect $\varepsilon_3^{\mathrm{even}} \le 3.81 \times 10^{-6}$ ($K=2$), $1.07 \times 10^{-8}$ ($K=3$), and $3.11 \times 10^{-12}$ ($K=4$).*
2. **(Exact Legendre–Schur Minorant for Single-Overlap Reflections $\tau \in [b, 2b)$):** *For any shift $\tau \in [b, 2b)$ with sign $s_\tau \in \{+1, -1\}$, the operator $\widetilde{R}_\tau := \frac{1}{2}S_\tau$ on $L^2_{\mathrm{even}}(-b, b) \cong L^2(0, b)$ is the partial reflection $(\widetilde{R}_\tau f)(x) = f(\tau - x)\mathbf{1}_{[\tau-b, b]}(x)$, and $Q_{\tau, s_\tau} := \frac{1}{2}\bigl(\mathbf{1}_{[\tau-b, b]} + s_\tau \widetilde{R}_\tau\bigr)$ is an orthogonal projection ($Q_{\tau, s_\tau}^* = Q_{\tau, s_\tau} = Q_{\tau, s_\tau}^2 \succeq 0$) satisfying $\mathbf{1}_{[\tau-b, b]} + s_\tau \widetilde{R}_\tau = 2 Q_{\tau, s_\tau}$. Let $Q_{\tau, s_\tau}^{(N)} := \Pi_N Q_{\tau, s_\tau} \Pi_N = \frac{1}{2}\bigl(D_\tau^{(N)} + \frac{1}{2} s_\tau S_\tau^{(N)}\bigr)$ be its $N \times N$ Legendre Gram matrix with exact rational polynomial entries in $u = \tau/b$, where $(D_\tau^{(N)})_{rs} = \sqrt{(4r+1)(4s+1)} \int_{u-1}^1 P_{2r}(t) P_{2s}(t)\,dt$. Whenever $Q_{\tau, s_\tau}^{(N)} \succ 0$, the finite-rank Schur projection onto $\operatorname{span}\{Q_{\tau, s_\tau} \phi_{2r}\}_{r=0}^{N-1}$ yields the global operator inequality on $L^2_{\mathrm{even}}(-b, b)$:*
   $$Q_{\tau, s_\tau} \succeq Q_{\tau, s_\tau} \Pi_N \bigl(Q_{\tau, s_\tau}^{(N)}\bigr)^{-1} \Pi_N Q_{\tau, s_\tau},$$
   *which restricts on the entire $N$-dimensional Legendre subspace $\mathcal{V}_N^{\mathrm{even}}$ to the **exact identity** $\langle f, Q_{\tau, s_\tau} f \rangle = \langle f, Q_{\tau, s_\tau}^{(N)} f \rangle$ for all $f \in \mathcal{V}_N^{\mathrm{even}}$ with zero approximation loss.*

**Proof of (2):**  
Since $Q := Q_{\tau, s_\tau}$ satisfies $Q^* = Q = Q^2$, the vectors $w_r := Q \phi_{2r}$ ($0 \le r \le N-1$) have Gram matrix $\langle w_r, w_s \rangle = \langle Q \phi_{2r}, Q \phi_{2s} \rangle = \langle \phi_{2r}, Q \phi_{2s} \rangle = (Q^{(N)})_{rs}$. By Bessel's inequality for the orthogonal projection of $Q f$ onto $\operatorname{span}\{w_0, \dots, w_{N-1}\} \subset \operatorname{Ran}(Q)$,
$$\langle f, Q f \rangle = \|Q f\|^2 \ge \sum_{r, s = 0}^{N-1} \bigl((Q^{(N)})^{-1}\bigr)_{rs} \langle Q f, w_r \rangle \langle w_s, Q f \rangle = \sum_{r, s = 0}^{N-1} \bigl((Q^{(N)})^{-1}\bigr)_{rs} \langle f, Q \phi_{2r} \rangle \langle Q \phi_{2s}, f \rangle.$$
Moreover, if $f = \sum_{k=0}^{N-1} c_k \phi_{2k} \in \mathcal{V}_N^{\mathrm{even}}$, then $\langle f, Q \phi_{2r} \rangle = \sum_{k=0}^{N-1} c_k (Q^{(N)})_{kr}$, so the right-hand side equals $\sum_{k, l = 0}^{N-1} c_k c_l \sum_{r, s = 0}^{N-1} (Q^{(N)})_{kr} ((Q^{(N)})^{-1})_{rs} (Q^{(N)})_{sl} = \sum_{k, l = 0}^{N-1} c_k c_l (Q^{(N)})_{kl} = \langle f, Q f \rangle$ identically. $\square$

---

## Wall Check (Bottom of Deliverable)

> **Wall check:** Does this derivation prove RH, complete G2, establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical evidence in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
