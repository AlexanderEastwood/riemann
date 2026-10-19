# Complete Mathematical Derivation: All-Vector Weil Positivity Beyond $a = \frac{1}{2}\log 6$ Up to $a = \frac{1}{2}\log 7$

**Date:** 2026-10-15  
**Lane:** `KERNEL-API` (`all-vector-positivity-beyond-log6-2026-10-15-v1`)

---

## 1. Theorem 1: Exact Three-Island Identity Up to $a = \frac{3}{2}\log 2$

Let $L_2 := \frac{3}{2}I - \frac{1}{\sqrt{2}}(T_{\log 2} + T_{-\log 2}) : V_b \to V_a$, where $b = a - \log 2 > 0$ and $V_b = L^2(-b, b)$. Expanding $L_2^2$ gives
$$L_2^2 = \frac{13}{4}I - \frac{3}{\sqrt{2}}\bigl(T_{\log 2} + T_{-\log 2}\bigr) + \frac{1}{2}\bigl(T_{2\log 2} + T_{-2\log 2}\bigr).$$

**Theorem 1.** *For all $a \in (\log 2, \frac{3}{2}\log 2] \approx (0.693147, 1.039721]$, we have $2b = 2(a - \log 2) \le \log 2 < 2\log 2$, so $P_b(T_{\pm\log 2})P_b = 0$ and $P_b(T_{\pm 2\log 2})P_b = 0$. Consequently,*
$$P_b L_2^2 P_b = \frac{13}{4}\,I_{L^2(-b, b)} = 3.25\,I_{L^2(-b, b)} \quad \text{and} \quad \|L_2 g\|_{L^2(-a, a)}^2 = \frac{13}{4}\,\|g\|_{L^2(-b, b)}^2 \qquad \forall g \in V_b.$$
*Equivalently, on $V_b^{\mathrm{even}} \cong L^2(0, b)$ with cosine modes $u_\omega(x) = \cos(\omega x)$ and on $V_b^{\mathrm{odd}} \cong L^2(0, b)$ with sine modes $s_\omega(x) = \sin(\omega x)$,*
$$\frac{2}{\pi}\int_0^{\infty} \sigma(L_2)(\omega)^2 |u_\omega\rangle\langle u_\omega|\, d\omega = \frac{13}{4}\,I_{L^2(0, b)}, \qquad \frac{2}{\pi}\int_0^{\infty} \sigma(L_2)(\omega)^2 |s_\omega\rangle\langle s_\omega|\, d\omega = \frac{13}{4}\,I_{L^2(0, b)}.$$

*Proof.* For any $g \in L^2(-b, b)$, the support of $T_{\pm k\log 2}g$ is $[-b \pm k\log 2, b \pm k\log 2]$, which is disjoint from $(-b, b)$ whenever $2b \le k\log 2$. Since $a \le \frac{3}{2}\log 2 \iff 2b \le \log 2$, both $k = 1$ and $k = 2$ vanish identically under compression by $P_b$. The Plancherel identities follow immediately from Fourier inversion on $V_b^{\mathrm{even}}$ and $V_b^{\mathrm{odd}}$. $\square$

---

## 2. Exact Prime Compression $B_{\mathrm{prime}} = P_b L_2 \mathcal{Q}_{\mathrm{prime}} L_2 P_b$ on $[\frac{1}{2}\log 6, \frac{1}{2}\log 7]$

For $a \le \frac{1}{2}\log 7 \approx 0.9729550745$, the maximum shift length in $L_2 g$ is $2a \le \log 7$, so only prime powers $m = p^k \le 7$ ($m \in \{2, 3, 4, 5, 7\}$) can contribute to $\langle L_2 g, \mathcal{Q}_{\mathrm{prime}} L_2 g \rangle$. Expanding $L_2 (T_{\log m} + T_{-\log m}) L_2$ against $P_b$ and dropping all positive prime shifts ($m = 2, 4$ give $+c_0 I$ with $c_0 = \frac{5}{2}\log 2$ plus positive shifts; $m = 7$ at $a \le \frac{1}{2}\log 7$ has $\tau_7 = \log(7/4) \ge 2b$), the only non-zero compressed shifts on $V_b$ are:
- $\tau_5 = \log 5 - 2\log 2 = \log(5/4) \approx 0.2231435513$ with coefficient $-c_5 = -\frac{\log 5}{2\sqrt{5}} \approx -0.3598818669$,
- $\tau_3 = 2\log 2 - \log 3 = \log(4/3) \approx 0.2876820725$ with coefficient $-c_3 = -\frac{\log 3}{2\sqrt{3}} \approx -0.3171472409$,
- $\tau_6 = \log 3 - \log 2 = \log(3/2) \approx 0.4054651081$ with coefficient $+c_6 = +\sqrt{\frac{3}{2}}\log 3 \approx +1.3455382671$.

Thus on $V_b = L^2(-b, b)$,
$$B_{\mathrm{prime}} \succeq c_0 I_{V_b} - c_5 P_b(T_{\tau_5} + T_{-\tau_5})P_b - c_3 P_b(T_{\tau_3} + T_{-\tau_3})P_b + c_6 P_b(T_{\tau_6} + T_{-\tau_6})P_b.$$

---

## 3. Theorem 2: Exact Reflection-Involution Preconditioner and Sum-of-Squares Monotonicity on $(\frac{1}{2}\log 6, \log(5/2)]$

For $a \in (\frac{1}{2}\log 6, \log(5/2)] \approx (0.895880, 0.916291]$, we have $b = a - \log 2 \in (\frac{1}{2}\log(3/2), \log(5/4)] = (\frac{1}{2}\tau_6, \tau_5]$. Hence $\tau_6 \ge \tau_3 > \tau_5 \ge b$ while $\tau_6 < 2b < 2\tau_3 < 2\tau_5$.

1. **Exact Pointwise Diagonal Lower Bound for $-c_5$ and $-c_3$**:
   Because $\tau_5 \ge b$ and $\tau_3 > b$, the shifted intervals $[b - \tau_m, b]$ and $[-b, \tau_m - b]$ are disjoint for $m \in \{3, 5\}$. By $2|g(x)g(x-\tau_m)| \le |g(x)|^2 + |g(x-\tau_m)|^2$,
   $$-c_m\langle (T_{\tau_m} + T_{-\tau_m})g, g \rangle_{L^2(-b,b)} \ge -c_m \int_{|x| \in [\tau_m - b, b]} |g(x)|^2\,dx \qquad (m \in \{3, 5\}).$$

2. **Exact Reflection Involution for $\tau_6 = \log(3/2)$**:
   On $V_b^{\mathrm{even/odd}} \cong L^2(0, b)$, for $x \in [x_6, b]$ where $x_6 := \tau_6 - b > 0$, we have $x - \tau_6 \in [-b, -x_6]$, so $|x - \tau_6| = \tau_6 - x \in [x_6, b]$. Therefore, on $V_b^{\mathrm{even}}$ ($g(-y) = +g(y)$) and $V_b^{\mathrm{odd}}$ ($g(-y) = -g(y)$),
   $$P_b(T_{\tau_6} + T_{-\tau_6})P_b\big|_{V_b^{\mathrm{even/odd}}} = \pm R_{\tau_6}\mathbf{1}_{[x_6, b]}, \qquad (R_{\tau_6}g)(x) := g(\tau_6 - x).$$

3. **Closed-Form Inverse and Sum-of-Squares $a$-Monotonicity**:
   Splitting the archimedean multiplier at $\Delta_\alpha = \frac{7}{20} = 0.35$:
   $$\alpha(\xi) = \Delta_\alpha + \bigl(\alpha(\xi) - \Delta_\alpha\bigr)_+ - \bigl(\Delta_\alpha - \alpha(\xi)\bigr)_+$$
   adds $+\frac{13}{4}\Delta_\alpha I_{L^2(0,b)}$ to the prime operator by Theorem 1. Let
   $$v_0 := c_0 + \frac{13}{4}\Delta_\alpha, \qquad v_1 := v_0 - c_5, \qquad v_2 := v_0 - c_5 - c_3.$$
   Then $P_0^{\mathrm{even/odd}}(a) = v_0\mathbf{1}_{[0, x_5]} + v_1\mathbf{1}_{[x_5, x_3]} + v_2\mathbf{1}_{[x_3, x_6]} + (v_2 I \pm c_6 R_{\tau_6})\mathbf{1}_{[x_6, b]}$, where $x_5 = \tau_5 - b$ and $x_3 = \tau_3 - b$. Since $R_{\tau_6}^2 = I$ on $[x_6, b]$ and $v_2 \approx 2.1932 > c_6 \approx 1.3455 > 0$,
   $$(v_2 I \pm c_6 R_{\tau_6})^{-1} = \frac{v_2 I \mp c_6 R_{\tau_6}}{v_2^2 - c_6^2}.$$
   Differentiating $\langle P_0(a)^{-1} u_\xi, u_\xi \rangle_{L^2(0,b)}$ with respect to $a$ (since $\frac{db}{da} = 1$ and $\frac{dx_m}{da} = -1$) gives the exact sum of three squares:
   $$\frac{\partial}{\partial a}\left\langle P_0(a)^{-1} u_\xi, u_\xi \right\rangle_{L^2(0,b)} = \left(\frac{1}{v_1} - \frac{1}{v_0}\right)u_\xi(x_5)^2 + \left(\frac{1}{v_2} - \frac{1}{v_1}\right)u_\xi(x_3)^2 + \frac{\bigl(v_2 u_\xi(b) \mp c_6 u_\xi(x_6)\bigr)^2}{v_2(v_2^2 - c_6^2)} \ge 0.$$
   Hence $\mathcal{T}_{\mathrm{even/odd}}^{(0.35)}(a) := \operatorname{Tr}\bigl(P_0^{\mathrm{even/odd}}(a)^{-1} A_-^{(0.35)}(a)\bigr)$ is strictly increasing in $a$ across $(\frac{1}{2}\log 6, \log(5/2)]$, so a single endpoint check at $a_{\star\star} = \log(5/2)$ certifies the entire interval.

---

## 4. Theorem 3: $3\times 3$ Fiber-Bundle Preconditioner and Step Minorants on $(\log(5/2), \frac{1}{2}\log 7]$

For $a \in (\log(5/2), \frac{1}{2}\log 7] \approx (0.916291, 0.972955]$, we have $b = a - \log 2 \in (\tau_5, \frac{1}{2}\tau_7]$ so $d_5 := b - \tau_5 \in (0, \frac{1}{2}\log(28/25)] \approx (0, 0.056664]$, while $b < \tau_3 < \tau_6$.

1. **Exact Prime Decomposition into $P_0$ and Reflection Projectors**:
   On $V_b^{\mathrm{even/odd}} \cong L^2(0, b)$:
   - The $\tau_3$-shift on $[x_3, b]$ ($x_3 = \tau_3 - b$) is $\mp c_3 R_{\tau_3} = -c_3 I_{[x_3, b]} + 2c_3 P_{\mathrm{anti/sym}}^{(3)}$, where $P_{\mathrm{anti/sym}}^{(3)} = \frac{1}{2}(I \mp R_{\tau_3})\mathbf{1}_{[x_3, b]} \succeq 0$.
   - The $\tau_5$-shift on $[0, b]$ splits into the reflection $\mp c_5 R_{\tau_5} = -c_5 I_{[0, \tau_5]} + 2c_5 P_{\mathrm{anti/sym}}^{(5)}$ on $[0, \tau_5]$ plus the exact translation coupling $-c_5(T_{\tau_5} + T_{-\tau_5})$ between $I_1 := [0, d_5]$ and $I_2 := [\tau_5, b]$.
   - Notably, on $I_2 = [\tau_5, b]$, there is **no** $-c_5 I_{I_2}$ diagonal penalty because for $x \in [\tau_5, b]$, $x + \tau_5 > b$ and $x - \tau_5 \in [0, d_5] = I_1$ is kept exactly in the $I_1 \leftrightarrow I_2$ off-diagonal block!

2. **$3\times 3$ Fiber Bundle Structure of $P_0$**:
   Because $d_5 < x_6 = \tau_6 - b$ and $\tau_6 - \tau_5 < \tau_5$, the three intervals $I_1 = [0, d_5]$, $I_2 = [\tau_5, b]$, and $I_3 = [\tau_6 - b, \tau_6 - \tau_5]$ are pairwise disjoint of equal length $d_5$. For $u \in [0, d_5]$, $P_0^{\mathrm{even/odd}}$ couples $(g(u), g(u+\tau_5), g(\tau_6-\tau_5-u))$ via the $3\times 3$ constant symmetric tridiagonal matrix
   $$M_3^{\mathrm{even/odd}}(u) = \begin{pmatrix} V_1(u) & -c_5 & 0 \\ -c_5 & v_2 + c_5 & \pm c_6 \\ 0 & \pm c_6 & v_2 \end{pmatrix}, \qquad V_1(u) = v_1\mathbf{1}_{[0, x_3]}(u) + v_2\mathbf{1}_{[x_3, d_5]}(u),$$
   while on $[\tau_6 - \tau_5, \tau_5]$ it acts as the $2\times 2$ reflection $v_2 I \pm c_6 R_{\tau_6}$ and on $[d_5, x_6]$ as multiplication by $v_1$ or $v_2$.

3. **4-Step Midpoint-Moment Enclosure for the Single Plancherel Step Vector at $a = \frac{1}{2}\log 7$**:
   For the single step vector $w_{\star, i} = \mathbf{1}_{m_i < x_6} + (\frac{9}{10} - \frac{3}{5}\frac{m_i - x_6}{b - x_6})\mathbf{1}_{m_i > x_6}$ on the fiber-closed partition $\{I_1, \dots, I_K\}$ ($K = 19$):
   $$\Psi_{w_\star}(x) = \frac{13}{4}w_\star(x) - \frac{2}{\pi}\int_0^{\xi_1} \sigma(L_2)(\omega)^2 C_{w_\star}(\omega)\cos(\omega x)\,d\omega.$$
   Expanding $\cos(\omega x) = \sum_{n=0}^{M-1} \frac{(-1)^n}{(2n)!}\omega^{2n}x^{2n} + R_M(\omega, x)$ ($M = 16$, uniform remainder $\varepsilon_1 \le 4\times 10^{-24}$ on $[0, b]$) and shifting the resulting polynomial $\widetilde{\Psi}(x)$ to local midpoint coordinates $s = x - m_j \in [-L_j/2, L_j/2]$ makes the action of $P_0^{-1}$ diagonal in even/odd powers of $s$ ($s \mapsto +s$ under translation and $s \mapsto -s$ under reflection), reducing $J_{WW}, J_{We},$ and $v_W(\xi)$ to exact algebraic contractions plus explicit `flint.arb` error balls of radius $< 10^{-20}$.
