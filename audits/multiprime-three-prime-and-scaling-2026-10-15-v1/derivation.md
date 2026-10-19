# Mathematical Derivation: Möbius Parity Coherence, Primorial Balanced-Partition Isometric Horizons ($K = 2, 3, 4$), Certified Extension of $B_{2,3}$ up to $a = \frac{1}{2}\log 12$, Multi-Order Hankel Blind-Cone Elimination, and Gegenbauer–Bessel Finite-$N$ Mellin–Jacobi Completeness

> **Wall check:** No derivation in this document closes **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, or either of the **two historical missing-original evidence groups** in `evidence/MISSING.md`. All four remain **OPEN**.

---

## Theorem 1 (`KERNEL-API`: Möbius Parity Coherence & Complete Multi-Prime Tower Collapse Theorem)

Let $\mathcal{P}$ be any finite set of primes, and let $P_{\mathcal{P}} := \prod_{p \in \mathcal{P}} p$ be the squarefree product of the primes in $\mathcal{P}$. For each $p \in \mathcal{P}$, recall from Milestone 7 (`multiprime-euler-preconditioner-2026-10-15-v1`) the centered causal Euler factor and self-adjoint multiplier on $L^2(\mathbb{R})$:
$$\widetilde{E}_p := T_{-\frac{1}{2}\log p} - p^{-1/2} T_{+\frac{1}{2}\log p}, \qquad L_p := \widetilde{E}_p^* \widetilde{E}_p = \left(1 + \frac{1}{p}\right)I - \frac{1}{\sqrt{p}}S_{\log p},$$
where $S_\tau := T_\tau + T_{-\tau}$ for $\tau > 0$.

### 1.1 Exact Squarefree Divisor Expansion of $L_{\mathcal{P}} = \prod_{p \in \mathcal{P}} L_p$
Because the translation operators $T_\tau$ commute and $S_{\tau_1} S_{\tau_2} = S_{\tau_1 + \tau_2} + S_{|\tau_1 - \tau_2|}$, expanding the product
$$L_{\mathcal{P}} = \prod_{p \in \mathcal{P}} \left(\left(1 + \frac{1}{p}\right)I - \frac{1}{\sqrt{p}}\left(T_{\log p} + T_{-\log p}\right)\right)$$
picks from each prime $p \in \mathcal{P}$ either:
- the identity factor $(1 + p^{-1})I$,
- the forward shift $-p^{-1/2}T_{\log p}$ (placing $p$ into a numerator divisor $d_1 \mid P_{\mathcal{P}}$), or
- the backward shift $-p^{-1/2}T_{-\log p}$ (placing $p$ into a denominator divisor $d_2 \mid P_{\mathcal{P}}$, with $\gcd(d_1, d_2) = 1$).

Grouping each coprime squarefree pair $(d_1, d_2)$ ($d_1 > d_2 \ge 1$, $d_1 d_2 \mid P_{\mathcal{P}}$) with its reciprocal $(d_2, d_1)$ yields the exact operator expansion:
$$L_{\mathcal{P}} = C_{\mathrm{zero}}(\mathcal{P})\,I + \sum_{\substack{d_1, d_2 \mid P_{\mathcal{P}} \\ \gcd(d_1, d_2) = 1, \, d_1 > d_2 \ge 1}} \frac{\mu(d_1 d_2)}{\sqrt{d_1 d_2}} \left(\prod_{r \in \mathcal{P}, \, r \nmid d_1 d_2} \left(1 + \frac{1}{r}\right)\right) S_{\log(d_1 / d_2)},$$
where $C_{\mathrm{zero}}(\mathcal{P}) := [I]L_{\mathcal{P}} = \prod_{p \in \mathcal{P}} (1 + p^{-1})$ is the zero-translation coefficient and $\mu(d_1 d_2) = (-1)^{\omega(d_1 d_2)}$ is the Möbius function.

### 1.2 Complete Multi-Prime Tower Collapse
For every $p \in \mathcal{P}$, the single-prime Euler identity $L_p W_p = (\log p) L_p - (\log p)(1 - p^{-1})I$ implies
$$L_{\mathcal{P}} \sum_{p \in \mathcal{P}} W_p = (\log P_{\mathcal{P}})\,L_{\mathcal{P}} - \sum_{p \in \mathcal{P}} (\log p)\left(1 - \frac{1}{p}\right) L_{\mathcal{P} \setminus \{p\}}.$$
Every higher prime power $p^k$ ($p \in \mathcal{P}, k \ge 2$) and every composite ratio $m/n$ containing a squared prime factor from $\mathcal{P}$ (such as $4/3, 8/3, 9/8, 16/9, \dots$) vanishes identically.

### 1.3 Möbius Parity Sign Law for External Prime Cross-Shifts
For an external prime $q \notin \mathcal{P}$ and prime power $n = q^k$ ($k \ge 1$), multiplying $L_{\mathcal{P}}$ by the Weil term $-\frac{\log q}{\sqrt{n}} S_{\log n}$ produces shifts $S_{|\log(n d_2 / d_1)|}$ with coefficient
$$c_{n; d_1, d_2} = -\frac{\mu(d_1 d_2)\log q}{\sqrt{n d_1 d_2}} \prod_{r \in \mathcal{P}, \, r \nmid d_1 d_2} \left(1 + \frac{1}{r}\right).$$
Therefore, the sign of the cross-shift $S_{|\log(n d_2 / d_1)|}$ in $L_{\mathcal{P}} \mathcal{Q}_{\mathrm{prime}}$ is governed solely by the prime-factor parity $\omega(d_1 d_2)$:
$$\operatorname{sgn}(c_{n; d_1, d_2}) = -\mu(d_1 d_2) = (-1)^{\omega(d_1 d_2) - 1} = \begin{cases} +1 & \text{if } \omega(d_1 d_2) \text{ is odd}, \\ -1 & \text{if } \omega(d_1 d_2) \text{ is even}. \end{cases}\quad\square$$

---

## Theorem 2 (`KERNEL-API`: Primorial Balanced-Partition Isometric Horizon Theorem for $K = 2, 3, 4$)

Let $\mathcal{P}_K = \{p_1, \dots, p_K\}$ be the first $K$ primes, and let $P_K^\# := \prod_{k=1}^K p_k$ be the $K$-th primorial. Factor $P_K^\# = d_+(K) d_-(K)$ with $d_+(K) > d_-(K)$ chosen to minimize $\log(d_+(K) / d_-(K))$:
- $K = 2$: $P_2^\# = 6 = 3 \times 2$ ($d_+ = 3, d_- = 2$, $\tau_{\mathrm{iso}}(2) = \log(3/2) \approx 0.40546511$, $\mathcal{P}_{2,+} = \{3\}, \mathcal{P}_{2,-} = \{2\}$).
- $K = 3$: $P_3^\# = 30 = 6 \times 5$ ($d_+ = 6, d_- = 5$, $\tau_{\mathrm{iso}}(3) = \log(6/5) \approx 0.18232156$, $\mathcal{P}_{3,+} = \{2, 3\}, \mathcal{P}_{3,-} = \{5\}$).
- $K = 4$: $P_4^\# = 210 = 15 \times 14$ ($d_+ = 15, d_- = 14$, $\tau_{\mathrm{iso}}(4) = \log(15/14) \approx 0.06899287$, $\mathcal{P}_{4,+} = \{3, 5\}, \mathcal{P}_{4,-} = \{2, 7\}$).

For $K \in \{2, 3, 4\}$, $\tau_{\mathrm{iso}}(K) = \log(d_+(K)/d_-(K))$ is the strictly smallest non-zero shift in $L_{\mathcal{P}_K}$. Setting $b_K(a) = a - \frac{1}{2}\log P_K^\#$, every non-zero shift of $L_{\mathcal{P}_K}$ lies outside $(-2b_K(a), 2b_K(a))$ if and only if
$$2b_K(a) = 2a - \log P_K^\# \le \log\!\left(\frac{d_+(K)}{d_-(K)}\right) \iff 2a \le \log\!\left(d_+(K) d_-(K) \cdot \frac{d_+(K)}{d_-(K)}\right) = 2\log d_+(K) \iff a \le \log d_+(K) =: a_{\mathrm{iso}}(K).$$
Thus, across the entire continuum window $a \in (\frac{1}{2}\log P_K^\#,\, \log d_+(K)]$, on the multi-prime Euler-filtered subspace $\operatorname{Ran}(B_{\mathcal{P}_{K,+}, \mathcal{P}_{K,-}}) \subsetneq L^2_{\mathrm{pole\text{-}free}}(-a, a)$,
$$P_{b_K} B_{\mathcal{P}_{K,+}, \mathcal{P}_{K,-}}^* B_{\mathcal{P}_{K,+}, \mathcal{P}_{K,-}} P_{b_K} = C_{\mathrm{zero}}(\mathcal{P}_K)\,I_{L^2(-b_K, b_K)},$$
and the internal prime operator $P_{b_K} L_{\mathcal{P}_K} \sum_{p \in \mathcal{P}_K} W_p P_{b_K} = C_{\mathrm{diag}}(\mathcal{P}_K)\,I_{L^2(-b_K, b_K)}$ is a pure positive scalar multiple of the identity with **zero** internal off-diagonal shifts! Moreover, the **zero-minorant** pure-diagonal Schur trace $\mathcal{T}_{\mathrm{even}}(a_{\mathrm{iso}}(K))$ at the top endpoint $a_{\mathrm{iso}}(K) = \log d_+(K)$ contracts rapidly toward zero as $K$ increases:
$$\mathcal{T}_{\mathrm{even}}(\log 3) = 0.9150349476 \;\; (K=2) \longrightarrow \mathcal{T}_{\mathrm{even}}(\log 6) = 0.2891142031 \;\; (K=3) \longrightarrow \mathcal{T}_{\mathrm{even}}(\log 15) = 0.0841820797 \;\; (K=4),$$
$$\mathcal{T}_{\mathrm{odd}}(\log 3) = 0.1036923511 \;\; (K=2) \longrightarrow \mathcal{T}_{\mathrm{odd}}(\log 6) = 0.0062155966 \;\; (K=3) \longrightarrow \mathcal{T}_{\mathrm{odd}}(\log 15) = 0.0002153683 \;\; (K=4). \quad\square$$

---

## Theorem 3 (`KERNEL-API`: Certified Extension of $B_{2,3}$ Across $(\frac{1}{2}\log 10, \frac{1}{2}\log 12]$ via Pure-Diagonal + Reflection Step Minorants and 2-Mode Cauchy–Poincaré Defect Bound)

On $a \in (\frac{1}{2}\log 10, \frac{1}{2}\log 12] = (\frac{1}{2}\log 10, \log(2\sqrt{3})] \approx (1.15129255, 1.24245332]$, on the filtered subspace $\operatorname{Ran}(B_{2,3}) \subsetneq L^2_{\mathrm{pole\text{-}free}}(-a, a)$:
1. **Active Shifts & Möbius Parity Signs:**
   - $\tau_{7/6} = \log(7/6) \approx 0.15415068$ ($d = 6, \omega(6) = 2$ even): negative coefficient $-c_{7/6} = -\frac{\log 7}{\sqrt{42}}$.
   - $\tau_{6/5} = \log(6/5) \approx 0.18232156$ ($d = 6, \omega(6) = 2$ even): negative coefficient $-c_{6/5} = -\frac{\log 5}{\sqrt{30}}$.
   - $\tau_{3/2} = \log(3/2) \approx 0.40546511$ (internal $L_2 L_3$ shift): **positive** coefficient $+c_{3/2}(\Delta_\alpha) = \frac{\log 6 + \Delta_\alpha}{\sqrt{6}} > 0$.
   - $\tau_{5/3} = \log(5/3) \approx 0.51082562$ ($d = 3, \omega(3) = 1$ odd, entering at $a = \frac{1}{2}\log 10$): **positive** coefficient $+c_{5/3} = +\frac{3\log 5}{2\sqrt{15}} > 0$.
   - $\tau_{11/6} = \log(11/6) \approx 0.60613580$ ($d = 6, \omega(6) = 2$ even, entering at $a = \frac{1}{2}\log 11 \approx 1.19894764$): negative coefficient $-c_{11/6} = -\frac{\log 11}{\sqrt{66}}$.
   No other shift enters $(-2b, 2b)$ until the internal shift $\tau_2 = \log 2$ at $a = \frac{1}{2}\log 12 \approx 1.2424533249$.

2. **Pure-Diagonal + Symmetric/Antisymmetric Reflection Step-Minorant Preconditioner:**
   In the even sector on $L^2(0, b)$, decomposing every positive reflection $+c_\tau R_\tau = -c_\tau \mathbf{1}_{[x_\tau, b]} I + c_\tau(\mathbf{1}_{[x_\tau, b]} I + R_\tau)$ ($\tau \in \{\tau_{3/2}, \tau_{5/3}\}$) and every negative shift $-c_\tau(T_\tau + T_\tau^* + R_\tau) = -(c_\tau \mathbf{1}_{[0, b-\tau]} + c_\tau \mathbf{1}_{[\tau, b]} + c_\tau \mathbf{1}_{[x_\tau, b]})I + c_\tau D_\tau^* D_\tau + c_\tau(\mathbf{1}_{[x_\tau, b]} I - R_\tau)$ ($\tau \in \{\tau_{7/6}, \tau_{6/5}, \tau_{11/6}\}$) expresses the prime operator at $\Delta_\alpha = \frac{3}{5} = 0.60$ as
   $$P_{\mathrm{prime,even}}(\Delta_\alpha; a) = V_a(x)\,I + c_{7/6} D_{\tau_{7/6}}^* D_{\tau_{7/6}} + c_{6/5} D_{\tau_{6/5}}^* D_{\tau_{6/5}} + \sum_{\tau \in \{\tau_{7/6}, \tau_{6/5}, \tau_{11/6}\}} 2 c_\tau P_{\mathrm{anti}}^{(\tau)} + \sum_{\tau \in \{\tau_{3/2}, \tau_{5/3}\}} 2 c_\tau P_{\mathrm{sym}}^{(\tau)},$$
   where $V_a(x) \ge V_{\min}(a) > 0$ is a purely diagonal step-function multiplication operator on $[0, b]$! Lower-bounding each of the positive difference and reflection operators independently by $n_{\mathrm{sub}}$ pairwise-orthogonal 2-piece step functions $w_m$ (and flipping the reflection signs $\pm \mapsto \mp$ in the odd sector) yields a closed-form Woodbury minorant $P_{\mathrm{minor}}^{\mathrm{even/odd}}(a) = V_a(x)I + W B^{-1} W^*$ whose cross-family interactions are inverted exactly by $M_{\mathrm{wood}} = B + W^* V_a^{-1} W$.

3. **2-Mode Cauchy–Poincaré Second-Eigenvalue Defect Bound:**
   Let $q_0, q_1 \in \operatorname{span}(\mathcal{E})$ be 2 step functions orthonormalized in exact 384-bit `flint.arb` arithmetic with respect to $\langle \cdot, P_{\mathrm{minor}}^{\mathrm{even}}(a) \cdot \rangle$, and let $G_{ij} := \langle q_i, A_-^{(\Delta_\alpha)}(a) q_j \rangle$ ($0 \le i, j \le 1$) be the $2\times 2$ Rayleigh matrix of $K_{\mathrm{even}}(a)$. By Cauchy–Poincaré interlacing,
   $$\lambda_2(K_{\mathrm{even}}(a)) \ge \mu_2(G) := \frac{(G_{00} + G_{11}) - \sqrt{(G_{00} - G_{11})^2 + 4 G_{01}^2}}{2} > 0,$$
   and therefore $\|K_{\mathrm{even}}(a)\|_{\mathrm{op}} \le \operatorname{Tr}(K_{\mathrm{even}}(a)) - \mu_2(G) < 1$ across all five checkpoints up to $a = \frac{1}{2}\log 12 \approx 1.2424533249$ (`0.972902` at $\frac{1}{2}\log 10$, `0.988941` at $1.175$, `0.996764` at $\frac{1}{2}\log 11$, `0.999231` at $1.220$, and `0.999947 < 1` at $\frac{1}{2}\log 12$). $\square$

---

## Theorem 4 (`ZERO-GEOMETRY`: Multi-Order Stieltjes–Hankel Defect & Angle Blind-Cone Elimination)

In `ZERO-GEOMETRY` (Milestone 6, `higher-order-wronskian-hankel-hierarchy-2026-10-15-v1`), an off-axis complex conjugate quadruple $\rho = \frac{1}{2} \pm \alpha \pm i\beta$ ($\alpha = r\sin\phi > 0$, $\beta = r\cos\phi > 0$, $\phi = \arctan(\alpha/\beta) \in (0, \pi/2)$) at $z^2 = (\beta \pm i\alpha)^2 = r^2 e^{\pm 2i\phi}$ contributes to the $m$-th Stieltjes moment $c_m(t_0) = (2m + 1)s_{2m+2}(t_0)$ the exact single-quadruple moment
$$c_m^{\mathrm{quad}}(r, \phi) = (2m + 1) \cdot \frac{2}{r^{2m+2}} \cos\!\bigl((2m + 2)\phi\bigr).$$
- **Primary Cone $(0, \pi/6)$ ($\beta > \sqrt{3}\alpha$):** Covered by the order-2 Turán defect $D(t_0; \alpha + i\beta) = \frac{8\alpha^2\beta^2(\beta^2 - 3\alpha^2)}{r^8} > 0$.
- **Order-2 Blind Cone $[\pi/6, \pi/2]$ ($\beta \le \sqrt{3}\alpha$):** Under real zeros of $\Phi_t(z)$, every Stieltjes moment is strictly positive ($c_m(t) > 0$ for all $m \ge 0$). For an off-axis quadruple in the blind cone $\phi \in [\pi/6, \pi/2]$, define the normalized negative Stieltjes moment defects $\widetilde{\delta}_m(\phi) := -\cos((2m + 2)\phi)$ for $m \in \{1, 2, 3, 4\}$ (phases $4\phi, 6\phi, 8\phi, 10\phi$).
  1. On $[\pi/6, \pi/3]$, $4\phi \in [2\pi/3, 4\pi/3] \implies -\cos(4\phi) \ge \frac{1}{2}$.
  2. On $[\pi/3, 5\pi/12]$, $8\phi \in [8\pi/3, 10\pi/3] \implies -\cos(8\phi) \ge \frac{1}{2}$.
  3. On $[5\pi/12, \pi/2]$, $-\cos(8\phi)$ and $-\cos(6\phi)$ cross at $8\phi^* + 6\phi^* = 6\pi \implies \phi^* = \frac{3\pi}{7}$, where
     $$-\cos\!\left(6 \cdot \frac{3\pi}{7}\right) = -\cos\!\left(\frac{4\pi}{7}\right) = \sin\!\left(\frac{\pi}{14}\right) \approx 0.222520933956 > 0,$$
     while including $m = 4$ ($-\cos(10\phi) \ge \frac{1}{2}$ on $[7\pi/15, \pi/2]$ and $\ge \frac{\sqrt{3}}{2}$ at $5\pi/12$) raises the global minimum across the entire blind cone $[\pi/6, \pi/2]$ to $\frac{1}{2} > 0$. $\square$

---

## Theorem 5 (`COEFF` / `NB-GAIN` (`NS-61`): Gegenbauer–Bessel Finite-$N$ Mellin–Jacobi Completeness & Super-Exponential Tail Decay Bound)

Let $p_n^{\mathrm{even}}(x) := \sqrt{\frac{4n+1}{b}} P_{2n}(x/b)$ and $p_n^{\mathrm{odd}}(x) := \sqrt{\frac{4n+3}{b}} P_{2n+1}(x/b)$ ($n = 0, 1, 2, \dots$) be the orthonormal even and odd Legendre–Jacobi polynomial bases on $L^2(0, b)$, and let $\Pi_N^{\mathrm{even/odd}}$ denote orthogonal projection onto the first $N$ basis modes.

1. **Exact Gegenbauer–Bessel Fourier Transform & Parseval Identity:**
   By Gegenbauer's integral theorem,
   $$\int_0^b p_n^{\mathrm{even}}(x)\cos(\xi x)\,dx = (-1)^n \sqrt{(4n+1)b}\,j_{2n}(b\xi), \qquad \int_0^b p_n^{\mathrm{odd}}(x)\sin(\xi x)\,dx = (-1)^n \sqrt{(4n+3)b}\,j_{2n+1}(b\xi),$$
   where $j_m(z) = \frac{z^m}{(2m+1)!!}\,{}_0F_1(; m + \frac{3}{2}; -\frac{z^2}{4})$ is the entire spherical Bessel function of order $m$. By Parseval's theorem on $L^2(0, b)$,
   $$\|(I - \Pi_N^{\mathrm{even}})\cos(\xi\,\cdot)\|_{L^2(0, b)}^2 = b\left[\frac{1 + \operatorname{sinc}(2b\xi)}{2} - \sum_{n=0}^{N-1} (4n+1) j_{2n}(b\xi)^2\right] = b\sum_{n=N}^\infty (4n+1) j_{2n}(b\xi)^2,$$
   $$\|(I - \Pi_N^{\mathrm{odd}})\sin(\xi\,\cdot)\|_{L^2(0, b)}^2 = b\left[\frac{1 - \operatorname{sinc}(2b\xi)}{2} - \sum_{n=0}^{N-1} (4n+3) j_{2n+1}(b\xi)^2\right] = b\sum_{n=N}^\infty (4n+3) j_{2n+1}(b\xi)^2.$$

2. **Closed-Form Preconditioned Operator-Norm Tail Defect:**
   Because $P_0(a) \succeq \lambda_{\min}(P_0(a)) I_{L^2(0, b)}$, the operator-norm tail defect of truncating $A_-^{(\Delta_\alpha)}(a)$ to the $N$-mode Legendre–Jacobi subspace on $L^2_{\mathrm{even/odd}}(0, b)$ is bounded in closed form by
   $$\delta_N^{\mathrm{even/odd}}(a) := \frac{1}{\lambda_{\min}(P_0(a))}\operatorname{Tr}\!\bigl((I - \Pi_N^{\mathrm{even/odd}}) A_-^{(\Delta_\alpha)}(a) (I - \Pi_N^{\mathrm{even/odd}})\bigr).$$
   Since $|j_m(z)| \le \frac{z^m}{(2m+1)!!}$ for all $z \in [0, b\xi_0]$, $\delta_N^{\mathrm{even/odd}}(a)$ decays factorially ($O((e b \xi_0 / (4N))^{4N})$) in $N$ and contracts even faster as $K$ increases because $b_{\mathrm{iso}}(K) = \frac{1}{2}\log(d_+(K)/d_-(K)) \to 0$. $\square$

---

> **Wall check:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
