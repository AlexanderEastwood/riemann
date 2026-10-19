# Complete Mathematical Derivations: Two-Sided Positive-Shift Step-Rank-1 Minorant & Crossing the First Internal Primorial Horizons for $K=3$ and $K=4$ (`three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1`)

> **Wall check & Scope Disclosure (`argon-m16-review` Finding 4)**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. In Section 3 below, the unshifted checkpoints at $\Delta_\alpha = 0$ ($N \in \{36, \dots, 42\}$ for $K=3$ and $N \in \{225, 240\}$ for $K=4$) certify full-space $L^2(-b,b)$ positivity of the unshifted operator via $\operatorname{Tr}(K_{\mathrm{sherman, even}}) < 1$ and $\operatorname{Tr}(K_{\mathrm{pure, odd}}) < 1$; the shifted checkpoints at $\Delta_\alpha = 3/5 = 0.60$ ($N \in \{42, 43, 44, 45\}$ for $K=3$) certify positivity of the $\Delta_\alpha$-shifted operator, where removing the artificial shift $\Delta_\alpha > 0$ requires the untruncated spatial archimedean integral developed in Milestones 16–17.

---

## 1. Complete Reduced-Fraction Shift Spectrum of $L_{\mathcal{P}_K}(-W_{\mathrm{arith}})$ and the Two Geometric Regimes

Let $\mathcal{P}_K = \{p_1, \dots, p_K\}$ be the first $K$ primes with primorial $P_K = \prod_{p \in \mathcal{P}_K} p$ and half-lag $c(\mathcal{P}_K) = \frac{1}{2}\log P_K$. Under the Euler-factor tower operator
$$L_{\mathcal{P}_K} = \prod_{p \in \mathcal{P}_K} \left(\frac{p+1}{p} I - \frac{1}{\sqrt{p}}(T_{\log p} + T_{-\log p})\right),$$
Theorem 1 of Milestone 8 (`multiprime-three-prime-and-scaling-2026-10-15-v1`) established that on $(-2b, 2b)$ ($b = a - c(\mathcal{P}_K)$), the preconditioned arithmetic distribution $Q_{\mathrm{arith}}(\mathcal{P}_K) := L_{\mathcal{P}_K}(-W_{\mathrm{arith}})$ expands into an exact linear combination of symmetric translation operators $T_{\tau_r} + T_{-\tau_r}$ indexed by reduced fractions $r = \frac{\max(d_1 q^k, d_2)}{\min(d_1 q^k, d_2)} > 1$ ($d_1, d_2 \mid P_K$, $\gcd(d_1, d_2) = 1$, $q^k$ a prime power):
$$P_b L_{\mathcal{P}_K}(-W_{\mathrm{arith}}) P_b = C_{\mathrm{diag}}(\mathcal{P}_K) I + \sum_{\substack{r > 1 \\ \tau_r = \log r < 2b}} c_r P_b (T_{\tau_r} + T_{-\tau_r}) P_b,$$
where
$$C_0(\mathcal{P}_K) = \prod_{p \in \mathcal{P}_K} \left(1 + \frac{1}{p}\right), \qquad C_{\mathrm{diag}}(\mathcal{P}_K) = C_0(\mathcal{P}_K) \sum_{p \in \mathcal{P}_K} \frac{2\log p}{p + 1}.$$

On the interval $[-b, b]$, the active shifts $\tau_r \in (0, 2b)$ fall into two distinct geometric regimes:
1. **Single-Reflection Regime ($b \le \tau_r < 2b$)**:
   - The intervals $[-b, b - \tau_r] \subset [-b, 0]$ and $[\tau_r - b, b] \subset [0, b]$ are disjoint.
   - On $L^2_{\mathrm{even}}(0, b)$ ($f(-u) = f(u)$) and $L^2_{\mathrm{odd}}(0, b)$ ($f(-u) = -f(u)$), the restricted shift operator $P_b(T_{\tau_r} + T_{-\tau_r})P_b$ acts exclusively on $[\tau_r - b, b]$ as $\pm R_{\tau_r}$, where $(R_{\tau_r} f)(x) = f(\tau_r - x)$ is the midpoint reflection involution across $\tau_r / 2$.
2. **Two-Sided Overlap Regime ($0 < \tau_r < b$)**:
   - Because $\tau_r < b$, the intervals $[-b, b - \tau_r]$ and $[\tau_r - b, b]$ overlap on the central core $[-(b - \tau_r), b - \tau_r]$.
   - For $x \in [0, b - \tau_r]$, both $x + \tau_r \in [0, b]$ and $x - \tau_r \in [-b, b]$ remain inside $[-b, b]$, so $(T_{\tau_r} + T_{-\tau_r})f(x) = f(x + \tau_r) + f(|x - \tau_r|)$ couples $x$ to two distinct points and is no longer a local reflection involution.

---

## 2. Theorem 1 (`KERNEL-API`): Universal Schur Decomposition, Two-Sided Positive-Shift Step-Rank-1 Minorant, and Single Aggregated Sherman–Morrison Trace Reduction

### Theorem 1 (Universal Schur Decomposition and Aggregated Positive-Shift Sherman–Morrison Reduction Across $(0, 2b)$)
Let $b > 0$ and let $\{\tau_r\}_{r \in \mathcal{A}(b)} \subset (0, 2b)$ be the active shifts with coefficients $c_r = s_r |c_r| \neq 0$ ($s_r \in \{\pm 1\}$).

1. **Universal Nonnegative Schur Decomposition on $(-b, b)$**:
   For every active shift $\tau_r \in (0, 2b)$ (whether $0 < \tau_r < b$ or $b \le \tau_r < 2b$), define the step indicator multiplicity function on $[-b, b]$:
   $$\psi_r(u) := \mathbf{1}_{[-b, b - \tau_r]}(u) + \mathbf{1}_{[\tau_r - b, b]}(u) = \begin{cases} \mathbf{1}_{[\tau_r - b, b]}(|u|), & \text{if } b \le \tau_r < 2b, \\ 1 + \mathbf{1}_{[0, b - \tau_r]}(|u|), & \text{if } 0 < \tau_r < b, \end{cases}$$
   and the associated Schur operator on $L^2(-b, b)$:
   $$M_{\tau_r} := |c_r| \psi_r(u) I + c_r P_b (T_{\tau_r} + T_{-\tau_r}) P_b.$$
   Then $M_{\tau_r} \succeq 0$ on $L^2(-b, b)$ with exact quadratic form
   $$\langle F, M_{\tau_r} F \rangle_{L^2(-b, b)} = |c_r| \int_{-b}^{b - \tau_r} \bigl(F(u) + s_r F(u + \tau_r)\bigr)^2\,du \ge 0,$$
   and the total shifted arithmetic operator decomposes identically as:
   $$P_b L_{\mathcal{P}_K}(-W_{\mathrm{arith}} + \Delta_\alpha I) P_b = V_a(x) I + \sum_{r \in \mathcal{A}(b)} M_{\tau_r},$$
   where $V_a(x) = C_{\mathrm{diag}}(\mathcal{P}_K) + C_0(\mathcal{P}_K)\Delta_\alpha - \sum_{r \in \mathcal{A}(b)} |c_r| \psi_r(x)$ on $[0, b]$.

2. **Two-Sided & One-Sided Positive-Shift Step-Rank-1 Minorant ($c_r > 0, \tau_r \in (0, 2b)$)**:
   For every active shift $\tau_r \in (0, 2b)$ with **positive** coefficient $c_r > 0$ ($s_r = +1$), the action of $M_{\tau_r}^+ := M_{\tau_r}$ on the constant function $\mathbf{1}_{[-b, b]}$ is given identically on $[-b, b]$ by:
   $$(M_{\tau_r}^+ \mathbf{1}_{[-b, b]})(u) = 2 c_r \psi_r(u).$$
   Summing over all positive active shifts $\mathcal{A}_+(b) := \{r \in \mathcal{A}(b) : c_r > 0\}$ and defining $M_{\mathrm{pos}}^+ := \sum_{r \in \mathcal{A}_+(b)} M_{\tau_r}^+ \succeq 0$, we have on $[0, b]$:
   $$(M_{\mathrm{pos}}^+ \mathbf{1}_{[-b, b]})(x) = 2 \Psi_{\mathrm{pos}}(x), \qquad \Psi_{\mathrm{pos}}(x) := \sum_{r \in \mathcal{A}_+(b)} c_r \psi_r(x) \in \mathcal{S}_{\mathrm{step}},$$
   and
   $$\langle \mathbf{1}_{[0, b]}, M_{\mathrm{pos}}^+ \mathbf{1}_{[0, b]} \rangle_{L^2(0, b)} = 2 S_{\mathrm{pos}}, \qquad S_{\mathrm{pos}} := \sum_{r \in \mathcal{A}_+(b)} c_r (2b - \tau_r) = \int_0^b \Psi_{\mathrm{pos}}(x)\,dx > 0.$$
   By operator Cauchy–Schwarz on $M_{\mathrm{pos}}^+ \succeq 0$, on $L^2_{\mathrm{even}}(0, b)$:
   $$M_{\mathrm{pos}}^+ \succeq \frac{2}{S_{\mathrm{pos}}} |\Psi_{\mathrm{pos}}\rangle \langle \Psi_{\mathrm{pos}}| \succeq 0.$$
   Moreover:
   - This rank-1 minorant achieves **exact equality (zero loss)** on the constant mode $\mathbf{1}_{[0, b]}$:
     $$\left\langle \mathbf{1}_{[0, b]}, \frac{2}{S_{\mathrm{pos}}} |\Psi_{\mathrm{pos}}\rangle \langle \Psi_{\mathrm{pos}}| \mathbf{1}_{[0, b]} \right\rangle_{L^2(0, b)} = 2 S_{\mathrm{pos}} = \langle \mathbf{1}_{[0, b]}, M_{\mathrm{pos}}^+ \mathbf{1}_{[0, b]} \rangle_{L^2(0, b)}.$$
   - Because each $\psi_r(x) = \mathbf{1}_{[0, b - \tau_r]}(x) + \mathbf{1}_{[\tau_r - b, b]}(x)$ is constant on each subinterval of the existing cut partition $\{0, b - \tau_r, \tau_r - b, b\} \cap [0, b]$ of $V_a(x)$, $\Psi_{\mathrm{pos}} \in \mathcal{S}_{\mathrm{step}}$ lies **entirely inside the step subspace $\mathcal{S}_{\mathrm{step}}$** with **zero additional cuts**!

3. **Closed-Form Sherman–Morrison Trace Reduction**:
   When $V_a(x) > 0$ on $[0, b]$, the even preconditioner minorant
   $$P_0^{\mathrm{even}} := V_a(x) I + \frac{2}{S_{\mathrm{pos}}} |\Psi_{\mathrm{pos}}\rangle \langle \Psi_{\mathrm{pos}}| \succ 0$$
   has the exact Sherman–Morrison inverse
   $$(P_0^{\mathrm{even}})^{-1} = V_a(x)^{-1} I - \frac{\frac{2}{S_{\mathrm{pos}}} |V_a^{-1} \Psi_{\mathrm{pos}}\rangle \langle V_a^{-1} \Psi_{\mathrm{pos}}|}{1 + \frac{2}{S_{\mathrm{pos}}} J_{\mathrm{pos}}}, \qquad J_{\mathrm{pos}} := \langle \Psi_{\mathrm{pos}}, V_a^{-1} \Psi_{\mathrm{pos}} \rangle_{L^2(0, b)} = \sum_k \frac{\Psi_k^2}{V_k} (x_{k+1} - x_k).$$
   Consequently, for $K_{\mathrm{sherman, even}} := (P_0^{\mathrm{even}})^{-1/2} M_{\Delta_\alpha}^{\mathrm{even}} (P_0^{\mathrm{even}})^{-1/2}$, the exact trace is given by:
   $$\operatorname{Tr}(K_{\mathrm{sherman, even}}) = \operatorname{Tr}(K_{\mathrm{pure, even}}) - \frac{\frac{2}{S_{\mathrm{pos}}} I_{\mathrm{pos}}}{1 + \frac{2}{S_{\mathrm{pos}}} J_{\mathrm{pos}}},$$
   where
   $$I_{\mathrm{pos}} := \langle V_a^{-1} \Psi_{\mathrm{pos}}, M_{\Delta_\alpha}^{\mathrm{even}} V_a^{-1} \Psi_{\mathrm{pos}} \rangle_{L^2(0, b)} = \int_0^{\xi_0} \frac{2}{\pi} \sigma_{L_{\mathcal{P}_K}}(\xi)(\Delta_\alpha - \alpha(\xi)) \left(\sum_k \frac{\Psi_k}{V_k} \bigl(x_{k+1}\operatorname{sinc}(\xi x_{k+1}) - x_k\operatorname{sinc}(\xi x_k)\bigr)\right)^2 d\xi.$$

### Proof of Theorem 1
1. For any $F \in L^2(-b, b)$, expansion of $|c_r| \int_{-b}^{b - \tau_r} (F(u) + s_r F(u + \tau_r))^2\,du \ge 0$ gives
   $$|c_r| \int_{-b}^{b - \tau_r} F(u)^2\,du + |c_r| \int_{\tau_r - b}^b F(v)^2\,dv + 2 c_r \int_{-b}^{b - \tau_r} F(u) F(u + \tau_r)\,du = \langle F, M_{\tau_r} F \rangle_{L^2(-b, b)},$$
   proving $M_{\tau_r} \succeq 0$ for all $\tau_r \in (0, 2b)$.
2. For $c_r > 0$ ($s_r = +1$) and $F = \mathbf{1}_{[-b, b]}$, we have $F(u) + F(u + \tau_r) = 2$ for all $u \in [-b, b - \tau_r]$ (since $u + \tau_r \in [\tau_r - b, b] \subset [-b, b]$) and $F(u) + F(u - \tau_r) = 2$ for all $u \in [\tau_r - b, b]$ (since $u - \tau_r \in [-b, b - \tau_r] \subset [-b, b]$). Thus
   $$(M_{\tau_r}^+ \mathbf{1}_{[-b, b]})(u) = c_r \bigl(2 \mathbf{1}_{[-b, b - \tau_r]}(u) + 2 \mathbf{1}_{[\tau_r - b, b]}(u)\bigr) = 2 c_r \psi_r(u).$$
   Summing over $r \in \mathcal{A}_+(b)$ gives $(M_{\mathrm{pos}}^+ \mathbf{1}_{[-b, b]})(x) = 2 \Psi_{\mathrm{pos}}(x)$ and $\langle \mathbf{1}_{[0, b]}, M_{\mathrm{pos}}^+ \mathbf{1}_{[0, b]} \rangle_{L^2(0, b)} = 2 \int_0^b \Psi_{\mathrm{pos}}(x)\,dx = 2 S_{\mathrm{pos}}$. Since $M_{\mathrm{pos}}^+ \succeq 0$ is self-adjoint and positive semidefinite on $L^2_{\mathrm{even}}(0, b)$, the Cauchy–Schwarz inequality $|\langle \mathbf{1}_{[0, b]}, M_{\mathrm{pos}}^+ f \rangle|^2 \le \langle \mathbf{1}_{[0, b]}, M_{\mathrm{pos}}^+ \mathbf{1}_{[0, b]} \rangle \langle f, M_{\mathrm{pos}}^+ f \rangle$ gives
   $$\langle f, M_{\mathrm{pos}}^+ f \rangle_{L^2(0, b)} \ge \frac{|\langle M_{\mathrm{pos}}^+ \mathbf{1}_{[0, b]}, f \rangle_{L^2(0, b)}|^2}{\langle \mathbf{1}_{[0, b]}, M_{\mathrm{pos}}^+ \mathbf{1}_{[0, b]} \rangle_{L^2(0, b)}} = \frac{4 |\langle \Psi_{\mathrm{pos}}, f \rangle_{L^2(0, b)}|^2}{2 S_{\mathrm{pos}}} = \frac{2}{S_{\mathrm{pos}}} |\langle \Psi_{\mathrm{pos}}, f \rangle_{L^2(0, b)}|^2.$$
3. Direct multiplication verifies $(V_a I + \alpha_{\mathrm{pos}} |\Psi_{\mathrm{pos}}\rangle \langle \Psi_{\mathrm{pos}}|) (V_a^{-1} I - \frac{\alpha_{\mathrm{pos}}}{1 + \alpha_{\mathrm{pos}} J_{\mathrm{pos}}} |V_a^{-1}\Psi_{\mathrm{pos}}\rangle \langle V_a^{-1}\Psi_{\mathrm{pos}}|) = I$ for $\alpha_{\mathrm{pos}} = 2 / S_{\mathrm{pos}}$. Taking the trace against $M_{\Delta_\alpha}^{\mathrm{even}}$ yields the exact Sherman–Morrison trace identity. $\blacksquare$

---

## 3. Theorem 2 (`KERNEL-API`): Crossing the First Internal Primorial Horizons for $K=3$ ($B_{\{2,3\},\{5\}}$) and $K=4$ ($B_{\{2,3,5\},\{7\}}$)

Applying Theorem 1 in two-precision (`256`-bit and `384`-bit) `flint.arb` ball arithmetic with zero float tolerances (`91/91` ball overlap checks PASS):

### 3.1 Three-Prime Preconditioner $K = 3$ ($B_{\{2,3\},\{5\}}$, $P_3 = 30$) at $\Delta_\alpha = 0$ Across $N \in \{36, 37, 38, 39, 40, 41, 42\}$
At $\Delta_\alpha = 0$ (zero archimedean shift, $\xi_0 \approx 6.289836$), we cross the first internal shift horizon $a_{\mathrm{iso}}(3) = \frac{1}{2}\log 36 = \log 6 \approx 1.791759$ ($N = 36$, 7 shifts) all the way up to $a = \frac{1}{2}\log 42 \approx 1.868835$ ($N = 42$, $2b = \log(7/5) \approx 0.336472$, 14 active shifts):

| $N$ ($a = \frac{1}{2}\log N$) | $a$ | $2b = \log(N/30)$ | Shifts (2-Sided / 1-Ref / Pos) | $\min_x V_a(x)$ | $\operatorname{Tr}(K_{\mathrm{pure, even}})$ | Sherman Gain | $\operatorname{Tr}(K_{\mathrm{sherman, even}})$ | $\operatorname{Tr}(K_{\mathrm{pure, odd}})$ | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $36$ ($\log 6$) | $1.791759$ | $0.182322$ | $7$ ($3 / 4 / 3$) | $2.147066$ | $0.289114$ | $0.083391$ | **$0.205724 < 1$** | $0.006216 < 1$ | **CERTIFIED** |
| $37$ | $1.805459$ | $0.209721$ | $8$ ($4 / 4 / 3$) | $1.526095$ | $0.405971$ | $0.134512$ | **$0.271459 < 1$** | $0.012422 < 1$ | **CERTIFIED** |
| $38$ | $1.818793$ | $0.236389$ | $9$ ($4 / 5 / 4$) | $1.299329$ | $0.543084$ | $0.218274$ | **$0.324811 < 1$** | $0.020662 < 1$ | **CERTIFIED** |
| $39$ | $1.831781$ | $0.262364$ | $10$ ($5 / 5 / 4$) | $1.156093$ | $0.725438$ | $0.339306$ | **$0.386132 < 1$** | $0.033451 < 1$ | **CERTIFIED** |
| $40$ | $1.844440$ | $0.287682$ | $12$ ($6 / 6 / 5$) | $0.736779$ | $1.030545$ (FAIL) | $0.572142$ | **$0.458404 < 1$** | $0.059600 < 1$ | **CERTIFIED** |
| $41$ | $1.856786$ | $0.312375$ | $13$ ($7 / 6 / 5$) | $0.456765$ | $1.467972$ (FAIL) | $0.937605$ | **$0.530367 < 1$** | $0.095287 < 1$ | **CERTIFIED** |
| $42$ ($\frac{1}{2}\log 42$) | $1.868835$ | $0.336472$ | $14$ ($7 / 7 / 6$) | $0.318554$ | $2.400252$ (FAIL) | $1.773418$ | **$0.626834 < 1$** | $0.181220 < 1$ | **CERTIFIED** |

### 3.2 Three-Prime Preconditioner $K = 3$ ($B_{\{2,3\},\{5\}}$) at $\Delta_\alpha = 3/5 = 0.60$ Across $N \in \{42, 43, 44, 45\}$ up to the Second Internal Shift Horizon $a = \frac{1}{2}\log 45 = \log(3\sqrt{5})$
At $\Delta_\alpha = 3/5 = 0.60$ ($\xi_0 \approx 11.452353$), we cross $\tau_{7/5} = \log(7/5)$ and the two-sided threshold $b = \tau_{6/5}$ ($N = 43.2$) all the way up to the **second internal shift horizon** $a = \frac{1}{2}\log 45 = \log(3\sqrt{5}) \approx 1.903331$ ($2b = \log(3/2) \approx 0.405465$, 18 active shifts):

| $N$ ($a = \frac{1}{2}\log N$) | $a$ | $2b = \log(N/30)$ | Shifts (2-Sided / 1-Ref / Pos) | $\min_x V_a(x)$ | $\operatorname{Tr}(K_{\mathrm{pure, even}})$ | Sherman Gain | $\operatorname{Tr}(K_{\mathrm{sherman, even}})$ | $\operatorname{Tr}(K_{\mathrm{pure, odd}})$ | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $42$ | $1.868835$ | $0.336472$ | $14$ ($7 / 7 / 6$) | $1.758554$ | $1.131822$ (FAIL) | $0.488192$ | **$0.643630 < 1$** | $0.119677 < 1$ | **CERTIFIED** |
| $43$ | $1.880600$ | $0.360003$ | $16$ ($7 / 9 / 7$) | $0.822934$ | $1.465187$ (FAIL) | $0.750171$ | **$0.715016 < 1$** | $0.189324 < 1$ | **CERTIFIED** |
| $44$ | $1.892095$ | $0.382992$ | $17$ ($8 / 9 / 8$) | $0.718213$ | $2.002820$ (FAIL) | $1.190467$ | **$0.812353 < 1$** | $0.311833 < 1$ | **CERTIFIED** |
| $45$ ($\log(3\sqrt{5})$) | $1.903331$ | $0.405465$ | $18$ ($8 / 10 / 9$) | $0.491447$ | $2.768965$ (FAIL) | $1.837074$ | **$0.931891 < 1$** | $0.494288 < 1$ | **CERTIFIED** |

### 3.3 Four-Prime Preconditioner $K = 4$ ($B_{\{2,3,5\},\{7\}}$, $P_4 = 210$) at $\Delta_\alpha = 0$ Across $N \in \{225, 240\}$ up to the Second Internal Shift Horizon $a = \frac{1}{2}\log 240 = \log(4\sqrt{15})$
For $K = 4$ ($P_4 = 210$) at $\Delta_\alpha = 0$ (zero archimedean shift!), we cross the first internal shift horizon $a_{\mathrm{iso}}(4) = \frac{1}{2}\log 225 = \log 15 \approx 2.708050$ ($2b = \log(15/14)$, 21 active shifts) all the way up to the **second internal shift horizon** $a = \frac{1}{2}\log 240 = \log(4\sqrt{15}) \approx 2.740319$ ($2b = \log(8/7) \approx 0.133531$, **43 active shifts**):

| $N$ ($a = \frac{1}{2}\log N$) | $a$ | $2b = \log(N/210)$ | Shifts (2-Sided / 1-Ref / Pos) | $\min_x V_a(x)$ | $\operatorname{Tr}(K_{\mathrm{pure, even}})$ | Sherman Gain | $\operatorname{Tr}(K_{\mathrm{sherman, even}})$ | $\operatorname{Tr}(K_{\mathrm{pure, odd}})$ | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $225$ ($\log 15$) | $2.708050$ | $0.068993$ | $21$ ($11 / 10 / 14$) | $3.771889$ | $0.084182$ | $0.034282$ | **$0.049900 < 1$** | $0.000215 < 1$ | **CERTIFIED** |
| $240$ ($\log(4\sqrt{15})$) | $2.740319$ | $0.133531$ | $43$ ($21 / 22 / 22$) | $0.942840$ | $0.448470$ | $0.346896$ | **$0.101574 < 1$** | $0.004897 < 1$ | **CERTIFIED** |

---

> **Wall check**: The Riemann Hypothesis (RH), G2, the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
