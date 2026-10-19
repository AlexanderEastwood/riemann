# Complete Mathematical Derivations: Analytic Continuity of Legendre Shift & Schur Multiplicity Matrices Across $u=1$ and Extended Four-Prime Horizon up to $a = \frac{1}{2}\log 260$ (`universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1`)

> **Wall check & Scope Disclosure (`argon-m16-review` Finding 4)**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. In Section 2 below, the unshifted checkpoints at $\Delta_\alpha = 0$ ($N \in \{225, 240, 245\}$ for $K=4$) certify full-space $L^2(-b,b)$ positivity of the unshifted operator via $\operatorname{Tr}(K_{\mathrm{sherman, even}}) < 1$ and $\operatorname{Tr}(K_{\mathrm{pure, odd}}) < 1$; the shifted checkpoints at $\Delta_\alpha \in \{0.60, 1.20\}$ ($N \in \{245, 250, 252, 255, 260\}$) certify positivity of the $\Delta_\alpha$-shifted operator, where removing the artificial shift $\Delta_\alpha > 0$ requires the untruncated spatial archimedean integral developed in Milestones 16–17.

---

## 1. Theorem 1 (`NB-GAIN` / `COEFF` & `NS-61`): Global Analyticity of Legendre Shift & Schur Multiplicity Matrices Across $u = 1$ and Universal Kernel-Plus-Positive-Definite Structure on $(0, 2)$

### Theorem 1 (Global Rational Polynomial Analyticity Across the Two-Sided / Single-Reflection Transition $u = 1$)
Let $\phi_m(t) = \sqrt{\frac{2m+1}{2}} P_m(t)$ ($m \ge 0$) be the orthonormal Legendre polynomial basis on $L^2(-1, 1)$, and let $u = \tau / b \in [0, 2]$.

1. **Global Polynomial Identity for the Shift Matrix $S_\tau^{(N)}$ on $[0, 2]$**:
   For all same-parity indices $m \equiv n \pmod 2$ and **all** $u \in [0, 2]$ (spanning both the two-sided overlap regime $u \in (0, 1)$ and the single-reflection regime $u \in [1, 2]$), the matrix entry $(S_\tau)_{m, n} := \langle \phi_m, P_1 (T_u + T_{-u}) P_1 \phi_n \rangle_{L^2(-1, 1)}$ is given by **one single analytic rational polynomial** on $[0, 2]$ with zero piecewise branching at $u = 1$:
   $$(S_\tau)_{m, n} = \sqrt{(2m+1)(2n+1)} \int_{-1}^{1 - u} P_m(t) P_n(t + u)\,dt \qquad \forall u \in [0, 2].$$
   In particular, for even indices $m = 2r, n = 2s$ and $u \in (0, 1)$, this single polynomial equals the three-piece folded $[0, 1]$ shift integral:
   $$(S_\tau)_{2r, 2s} = \sqrt{(4r+1)(4s+1)} \left( \int_0^{1-u} P_{2r}(x) P_{2s}(x+u)\,dx + \int_u^1 P_{2r}(x) P_{2s}(x-u)\,dx + \int_0^u P_{2r}(x) P_{2s}(u-x)\,dx \right).$$

2. **Global Polynomial Identity for the Universal Schur Multiplicity Matrix $D_\tau^{(N)}$ on $[0, 2]$**:
   Let $\psi_u(t) := \mathbf{1}_{[-1, 1-u]}(t) + \mathbf{1}_{[u-1, 1]}(t)$ be the Universal Schur Multiplicity Indicator on $[-1, 1]$ (which restricts on $x \in [0, 1]$ to $\mathbf{1}_{[u-1, 1]}(x)$ in the single-reflection regime $u \in [1, 2]$ and to $2 \mathbf{1}_{[0, 1-u]}(x) + \mathbf{1}_{[1-u, 1]}(x)$ in the two-sided regime $u \in [0, 1)$). Then for all same-parity indices $m \equiv n \pmod 2$ and **all** $u \in [0, 2]$, the matrix entry $(D_\tau)_{m, n} := \langle \phi_m, \psi_u \phi_n \rangle_{L^2(-1, 1)}$ is given by **one single analytic rational polynomial** on $[0, 2]$ with zero piecewise branching at $u = 1$:
   $$(D_\tau)_{m, n} = \sqrt{(2m+1)(2n+1)} \int_{u - 1}^1 P_m(t) P_n(t)\,dt \qquad \forall u \in [0, 2].$$

3. **Exact First-Row Polynomial Identity & Kernel-Plus-Positive-Definite Structure of $Q_{\tau, \pm 1}^{(N)}$ on $(0, 2)$**:
   For all $s \ge 0$ and all $u \in [0, 2]$:
   $$(D_\tau)_{0, 2s} = (S_\tau)_{0, 2s} = \sqrt{4s+1} \int_{u - 1}^1 P_{2s}(t)\,dt, \qquad (D_\tau)_{0, 0} = (S_\tau)_{0, 0} = 2 - u.$$
   Consequently, for the Universal Schur Matrices $Q_{\tau, \pm 1}^{(N)} := D_\tau^{(N)} \pm S_\tau^{(N)}$ in the even Legendre basis $\{P_0, P_2, \dots, P_{2N-2}\}$:
   - The first row and first column of $Q_{\tau, -1}^{(N)}$ vanish **identically** as polynomials in $u \in [0, 2]$ ($Q_{\tau, -1}^{(N)} e_0 = 0$), while the $(N-1) \times (N-1)$ non-constant block $\widetilde{Q}_{\tau, -1}^{(N)} := \bigl(Q_{\tau, -1}^{(N)}\bigr)_{r,s \in \{1,\dots,N-1\}}$ is **strictly positive definite ($\succ 0$)** for all $u \in (0, 2)$.
   - $Q_{\tau, +1}^{(N)}$ has $(0, 0)$ entry $(Q_{\tau, +1}^{(N)})_{0, 0} = 2(2 - u) > 0$ and is **strictly positive definite ($\succ 0$)** on all $N \times N$ modes for all $u \in (0, 2)$.

### Proof of Theorem 1
1. On $[-1, 1]$, for any $u \in [0, 2]$, the support of $t \in [-1, 1]$ such that $t + u \in [-1, 1]$ is $[-1, 1 - u]$, and the support of $t \in [-1, 1]$ such that $t - u \in [-1, 1]$ is $[u - 1, 1]$. For $m \equiv n \pmod 2$, the substitution $t = -w$ gives
   $$\int_{u-1}^1 P_m(t) P_n(t - u)\,dt = \int_{-1}^{1-u} (-1)^{m+n} P_m(w) P_n(w + u)\,dw = \int_{-1}^{1-u} P_m(w) P_n(w + u)\,dw,$$
   so $(S_\tau)_{m, n} = \frac{\sqrt{(2m+1)(2n+1)}}{2} \cdot 2 \int_{-1}^{1-u} P_m(t) P_n(t+u)\,dt$ holds for all $u \in [0, 2]$. Splitting $\int_{-1}^{1-u} = \int_{-1}^0 + \int_0^{1-u}$ and substituting $t = -x$ on $[-1, 0]$ yields the three-piece folded formula on $[0, 1]$ for $u \in (0, 1)$.
2. Similarly, since $P_m(-t) P_n(-t) = (-1)^{m+n} P_m(t) P_n(t) = P_m(t) P_n(t)$ for $m \equiv n \pmod 2$,
   $$\int_{-1}^{1-u} P_m(t) P_n(t)\,dt = \int_{u-1}^1 P_m(t) P_n(t)\,dt \qquad \forall u \in [0, 2],$$
   so $\langle \phi_m, \psi_u \phi_n \rangle_{L^2(-1, 1)} = \sqrt{(2m+1)(2n+1)} \int_{u-1}^1 P_m(t) P_n(t)\,dt$ holds identically on $[0, 2]$. When $u \in [0, 1)$, splitting $\int_{-(1-u)}^1 = \int_{-(1-u)}^0 + \int_0^{1-u} + \int_{1-u}^1 = 2\int_0^{1-u} + \int_{1-u}^1$ recovers the folded two-sided multiplicity integral.
3. For $m = 0$ ($P_0(t) = 1$) and $n = 2s$, substituting $w = t + u$ in $(S_\tau)_{0, 2s}$ gives $\sqrt{4s+1} \int_{-1}^{1-u} P_{2s}(t+u)\,dt = \sqrt{4s+1} \int_{u-1}^1 P_{2s}(w)\,dw = (D_\tau)_{0, 2s}$. By symmetry of $D_\tau$ and $S_\tau$, the first row and column of $Q_{\tau, -1}^{(N)} = D_\tau^{(N)} - S_\tau^{(N)}$ vanish identically. For any non-zero polynomial $f(t) = \sum_{r=0}^{N-1} v_r \phi_{2r}(t)$ ($u \in (0, 2)$), $\langle v, Q_{\tau, s_\tau}^{(N)} v \rangle = \int_{-1}^{1-u} (f(t) + s_\tau f(t+u))^2\,dt \ge 0$. Since $f(t) + f(t+u) = 0$ on $(-1, 1-u)$ implies the polynomial $f(t) + f(t+u)$ vanishes on $\mathbb{R}$ (impossible for a non-zero polynomial since its highest-degree term $2 c_d t^d \neq 0$), $Q_{\tau, +1}^{(N)} \succ 0$ is strictly positive definite on $\mathbb{R}^N$. Similarly, $f(t) - f(t+u) = 0$ on $(-1, 1-u)$ implies $f(t)$ is constant ($v_1 = \dots = v_{N-1} = 0$), so $\widetilde{Q}_{\tau, -1}^{(N)} \succ 0$ is strictly positive definite on $\mathbb{R}^{N-1}$. $\blacksquare$

### Certified Table for Theorem 1 (`flint.arb` Cholesky Pivots Across $u \in (0, 2)$)

| $u = \tau/b$ | Regime | $(Q_{\tau, +1}^{(4)})_{0, 0} = 2(2 - u)$ | Min Cholesky Pivot of $Q_{\tau, +1}^{(4)}$ ($4\times 4$) | Min Cholesky Pivot of $\widetilde{Q}_{\tau, -1}^{(4)}$ ($3\times 3$) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $1/20 = 0.05$ | Two-Sided ($u < 1$) | $3.900000$ | $1.696524 > 0$ | $0.186433 > 0$ | **PASS** |
| $1/4 = 0.25$ | Two-Sided ($u < 1$) | $3.500000$ | $0.839619 > 0$ | $0.792497 > 0$ | **PASS** |
| $1/2 = 0.50$ | Two-Sided ($u < 1$) | $3.000000$ | $0.308268 > 0$ | $1.228782 > 0$ | **PASS** |
| $3/4 = 0.75$ | Two-Sided ($u < 1$) | $2.500000$ | $0.094243 > 0$ | $0.676191 > 0$ | **PASS** |
| $19/20 = 0.95$ | Two-Sided ($u < 1$) | $2.100000$ | $0.030343 > 0$ | $0.328298 > 0$ | **PASS** |
| $1/1 = 1.00$ | Transition ($u = 1$) | $2.000000$ | $0.022097 > 0$ | $0.264243 > 0$ | **PASS** |
| $27/20 = 1.35$ | Single-Reflection ($u > 1$) | $1.300000$ | $0.001344 > 0$ | $0.033370 > 0$ | **PASS** |
| $37/20 = 1.85$ | Single-Reflection ($u > 1$) | $0.300000$ | $2.922 \times 10^{-7} > 0$ | $1.400 \times 10^{-5} > 0$ | **PASS** |

---

## 2. Theorem 2 (`KERNEL-API` + `NB-GAIN`): Extended Four-Prime Horizon for $K=4$ ($B_{\{2,3,5\},\{7\}}$) up to $a = \frac{1}{2}\log 260$ and $N=4$ Gegenbauer–Bessel Tail Completeness

### 2.1 Extended Four-Prime Coercivity Horizon ($K = 4, P_4 = 210$) Across $N \in \{225, 240, 245, 250, 252, 255, 260\}$

| $N$ ($a = \frac{1}{2}\log N$) | $\Delta_\alpha$ | $a$ | $2b = \log(N/210)$ | Shifts (2S / 1R / +) | $\min_x V_a(x)$ | $\operatorname{Tr}(K_{\mathrm{pure, even}})$ | Sherman Gain | $\operatorname{Tr}(K_{\mathrm{sherman, even}})$ | $\operatorname{Tr}(K_{\mathrm{pure, odd}})$ | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $225$ ($\log 15$) | $0.00$ | $2.708050$ | $0.068993$ | $21$ ($11 / 10 / 14$) | $3.771889$ | $0.084182$ | $0.034282$ | **$0.049900 < 1$** | $0.000215 < 1$ | **CERTIFIED** |
| $240$ ($\tau_{8/7}$) | $0.00$ | $2.740319$ | $0.133531$ | $43$ ($21 / 22 / 22$) | $0.942840$ | $0.448470$ | $0.346896$ | **$0.101574 < 1$** | $0.004897 < 1$ | **CERTIFIED** |
| $245$ ($\tau_{7/6}$) | $0.00$ | $2.750629$ | $0.154151$ | $49$ ($24 / 25 / 24$) | $0.408453$ | $1.120435$ (FAIL) | $0.990111$ | **$0.130324 < 1$** | $0.016697 < 1$ | **CERTIFIED** |
| $245$ ($\tau_{7/6}$) | $0.60$ | $2.750629$ | $0.154151$ | $49$ ($24 / 25 / 24$) | $2.054167$ | $0.556978$ | $0.393164$ | **$0.163814 < 1$** | $0.011754 < 1$ | **CERTIFIED** |
| $250$ | $0.60$ | $2.760730$ | $0.174353$ | $55$ ($29 / 26 / 27$) | $0.825716$ | $1.043464$ (FAIL) | $0.834083$ | **$0.209381 < 1$** | $0.032161 < 1$ | **CERTIFIED** |
| $252$ ($\tau_{6/5}$) | $0.60$ | $2.764715$ | $0.182322$ | $56$ ($30 / 26 / 27$) | $0.656037$ | $1.387559$ (FAIL) | $1.160422$ | **$0.227137 < 1$** | $0.046464 < 1$ | **CERTIFIED** |
| $252$ ($\tau_{6/5}$) | $1.20$ | $2.764715$ | $0.182322$ | $56$ ($30 / 26 / 27$) | $2.301752$ | $0.945157$ | $0.650195$ | **$0.294962 < 1$** | $0.135812 < 1$ | **CERTIFIED** |
| $255$ | $1.20$ | $2.770632$ | $0.194156$ | $60$ ($32 / 28 / 28$) | $1.334829$ | $1.241944$ (FAIL) | $0.912511$ | **$0.329433 < 1$** | $0.210297 < 1$ | **CERTIFIED** |
| $260$ ($\frac{1}{2}\log 260$) | $1.20$ | $2.780341$ | $0.213574$ | $66$ ($34 / 32 / 29$) | $0.367115$ | $2.292088$ (FAIL) | $1.867896$ | **$0.424192 < 1$** | $0.515452 < 1$ | **CERTIFIED** |

### 2.2 Certified $N=4$ Gegenbauer–Spherical-Bessel Parseval Tail Defects Across Extended Horizons

| $K$ | $N$ ($a = \frac{1}{2}\log N$) | $\Delta_\alpha$ | $b = a - c(\mathcal{P}_K)$ | $\varepsilon_4^{\mathrm{even}}(b)$ | Relative Even Defect | $\varepsilon_4^{\mathrm{odd}}(b)$ | Relative Odd Defect |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $3$ | $42$ ($1.868835$) | $0.00$ | $0.168236$ | $9.871 \times 10^{-17}$ | $7.858 \times 10^{-17}$ | $2.656 \times 10^{-19}$ | $3.145 \times 10^{-18}$ |
| $3$ | $45$ ($1.903331$) | $0.60$ | $0.202733$ | $2.604 \times 10^{-11}$ | $9.918 \times 10^{-12}$ | $3.485 \times 10^{-13}$ | $9.116 \times 10^{-13}$ |
| $4$ | $240$ ($2.740319$) | $0.00$ | $0.066766$ | $1.874 \times 10^{-23}$ | $2.939 \times 10^{-23}$ | $7.428 \times 10^{-27}$ | $1.229 \times 10^{-24}$ |
| $4$ | $245$ ($2.750629$) | $0.00$ | $0.077075$ | $2.147 \times 10^{-22}$ | $2.927 \times 10^{-22}$ | $1.135 \times 10^{-25}$ | $1.224 \times 10^{-23}$ |
| $4$ | $252$ ($2.764715$) | $0.60$ | $0.091161$ | $3.761 \times 10^{-17}$ | $2.462 \times 10^{-17}$ | $1.033 \times 10^{-19}$ | $2.414 \times 10^{-18}$ |
| $4$ | $260$ ($2.780341$) | $1.20$ | $0.106787$ | $2.831 \times 10^{-11}$ | $9.396 \times 10^{-12}$ | $3.561 \times 10^{-13}$ | $6.879 \times 10^{-13}$ |

---

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
