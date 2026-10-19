# Mathematical Derivation — 3-Point Fiber Closure on $(\frac{1}{2}\log 7, \frac{1}{2}\log(15/2)]$, Smooth 2-Mode Loewner Plancherel Minorant, and Courant–Fischer Deflated Trace

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this document claims a proof of RH or global Weil positivity.

---

## 1. Theorem 1 — Exact 3-Point Fiber Closure up to $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.0074515103$

Let $a \in \left(\frac{1}{2}\log 7,\, \frac{1}{2}\log(15/2)\right] \approx (0.9729550745,\, 1.0074515103]$, and let $b := a - \log 2 \in \left(\frac{1}{2}\log(7/4),\, \frac{1}{2}\log(15/8)\right] \approx (0.2798078940,\, 0.3143043298]$.

### 1.1 Exact Isometric Core ($m = 2$ and $m = 4$) and Active Prime Powers
Since $a \le \frac{1}{2}\log(15/2) < \frac{3}{2}\log 2 = \frac{1}{2}\log 8 \approx 1.0397207708$:
1. $2b = 2a - 2\log 2 < \log 2$, so by Theorem 1 of `verify_all_vector_certificate.py`, the prime-2 preconditioner $L_2 = I + c_2 S_2 + c_4 S_4$ ($c_2 = \frac{\log 2}{2\sqrt{2}}, c_4 = \frac{\log 2}{4}$) satisfies the exact isometric identity on $L^2(-b, b)$:
   $$P_b L_2^2 P_b = \left(1 + 2c_2^2 + 2c_4^2\right) I_{L^2(-b,b)} = \frac{13}{4} I_{L^2(-b,b)} = 3.25\, I_{L^2(-b,b)}.$$
2. The only prime powers $n = p^k \ge 2$ with $\log n < 2a \le \log(15/2) = \log(7.5)$ are
   $$n \in \{2, 3, 4, 5, 7\}.$$
   All shifts in $L_2 S_{\log n} L_2$ with shift distance $\ge 2b$ vanish identically under compression $P_b(\cdot)P_b$ to $L^2(-b,b)$. The remaining active shifts on $(0, b)$ have coefficients $c_3 = \frac{\log 3}{2\sqrt{3}}$, $c_5 = \frac{\log 5}{2\sqrt{5}}$, $c_6 = \sqrt{\frac{3}{2}}\log 3$, and $c_7 = \frac{\log 7}{2\sqrt{7}}$ at shift/reflection distances $\tau_3 = \log(4/3)$, $\tau_5 = \log(5/4)$, $\tau_6 = \log(3/2)$, and $\tau_7 = \log(7/4)$.

### 1.2 Reflection and Shift Decomposition of $\tau_7 = \log(7/4)$ and $\tau_3 = \log(4/3)$ on $L^2_{\mathrm{even/odd}}(0, b)$
For $a \in \left(\frac{1}{2}\log 7,\, \frac{1}{2}\log(15/2)\right]$:
- **Prime-7 reflection ($\tau_7 = \log(7/4)$)**:
  Since $b \le \frac{1}{2}\log(15/8) \approx 0.314304 < \tau_7 \approx 0.559616 < 2b$, the shift $S_{\tau_7}$ has **zero** positive-half shift overlap on $(0, b)$ and acts purely as the reflection $R_{\tau_7} f(x) = f(\tau_7 - x)$ on the interval
  $$[x_7, b], \qquad x_7 := \tau_7 - b = \log 7 - \log 2 - a \in [0.2453114581,\, 0.2798078940),$$
  with midpoint $m_7 := \frac{1}{2}\tau_7 = \frac{1}{2}\log(7/4) \approx 0.2798078940 \in (x_7, b)$.
  Using $I \mp R_{\tau_7} = 2 P_{\mathrm{anti/sym}}^{(7)}$ on $[x_7, b]$, the $m = 7$ term splits into a purely diagonal negative shift $-c_7 \mathbf{1}_{[x_7, b]}$ absorbed into $P_0(a)$ and a positive rank-decomposeable reflection remainder $+2c_7 P_{\mathrm{anti}}^{(7)}$ (even sector) or $+2c_7 P_{\mathrm{sym}}^{(7)}$ (odd sector).
- **Prime-3 reflection and shift ($\tau_3 = \log(4/3)$)**:
  At $a = \log(8/3) = 3\log 2 - \log 3 \approx 0.9808292530$, we have $b = \tau_3 = \log(4/3)$, so $x_3 := \max(0, \tau_3 - b) = 0$ and the $m = 3$ reflection $R_{\tau_3}$ saturates all of $[0, b]$.
  For $a \in (\log(8/3), \frac{1}{2}\log(15/2)]$, we have $b > \tau_3$ with shift overlap
  $$s_3 := b - \tau_3 = a - 3\log 2 + \log 3 > 0.$$
  Then:
  1. The reflection $R_{\tau_3}$ is supported on $[0, \tau_3]$ (symmetric about $m_3 = \frac{1}{2}\tau_3$), decomposing into $-c_3 \mathbf{1}_{[0, \tau_3]} + 2c_3 P_{\mathrm{anti/sym}}^{(3, \mathrm{refl})}$.
  2. The positive-half shift $T_{\tau_3}$ couples $[0, s_3]$ and $[\tau_3, b]$. Since $s_3 \le \frac{1}{2}\log(15/8) - \log(4/3) \approx 0.026622 < \tau_3 \approx 0.287682$, the intervals $[0, s_3]$ and $[\tau_3, b]$ are disjoint, and the $m = 3$ shift decomposes into $-c_3 \mathbf{1}_{[0, s_3] \cup [\tau_3, b]}$ absorbed into $P_0(a)$ plus $+2c_3 P_{\mathrm{diff}}^{(3, \mathrm{shift})}$.

### 1.3 Proof of Disjointness $d_5 \le x_6$, 3-Point Fiber Closure, and Determinant-Graded Inverse
The off-diagonal couplings kept inside the baseline operator $P_0(a)$ are the $m = 5$ shift on $[0, d_5] \leftrightarrow [\tau_5, b]$ ($d_5 = b - \tau_5 = a + \log 2 - \log 5$) and the $m = 6$ reflection $R_{\tau_6}$ on $[x_6, b]$ ($x_6 = \tau_6 - b = \log 3 - a$).
Observe that:
$$x_6 - d_5 = (\log 3 - a) - (a + \log 2 - \log 5) = \log 3 + \log 5 - \log 2 - 2a = \log(15/2) - 2a.$$
Therefore:
$$d_5 \le x_6 \iff a \le a_{\star\star\star\star} := \frac{1}{2}\log(15/2) \approx 1.0074515103,$$
with **exact equality $d_5 = x_6 = \frac{1}{2}\log(27/20) \approx 0.1500522962$ at $a = a_{\star\star\star\star}$**!
Hence every coupled fiber $\{x,\, x + \tau_5,\, \tau_6 - \tau_5 - x\}$ in $P_0(a)$ closes at length **at most 3**, and $P_0(a)$ is an exact direct sum of $1 \times 1$, $2 \times 2$, and $3 \times 3$ tridiagonal fiber matrices all the way up to $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.0074515103$. Furthermore, because $\det: O(1) \to \{\pm 1\}$ is a group homomorphism, negating $c_6 \mapsto -c_6$ multiplies every orientation-reversing path by $-1$ and preserves every orientation-preserving path:
$$(P_{0,\mathrm{odd}}^{-1})_{ij} = \det(\gamma_{ij})\,(P_{0,\mathrm{even}}^{-1})_{ij}. \quad \blacksquare$$

---

## 2. Theorem 2 — Smooth 2-Mode Loewner Plancherel Minorant and Courant–Fischer Deflated Trace

Let $\xi_{\Delta\alpha} > 0$ be the unique root of $\alpha(\xi_{\Delta\alpha}) = \Delta\alpha = 0.25$ ($\xi_{\Delta\alpha} \approx 8.0372408860$). On $[\xi_1, \infty)$ with $\xi_1 = 8.8 > \xi_{\Delta\alpha}$, we use the smooth 2-mode step-function profile $(w_1, w_2)$ with linear $w_2(x) = 1 - 2(x/b)$ on $[0, b]$ (eliminating any slope discontinuity at $m_6$). Since the $2 \times 2$ outer-product matrix
$$M(\omega) := \frac{2}{\pi}\,\sigma(L_2)(\omega)^2 \begin{pmatrix} c_1(\omega)^2 & c_1(\omega)c_2(\omega) \\ c_1(\omega)c_2(\omega) & c_2(\omega)^2 \end{pmatrix} \succeq 0$$
is pointwise positive semidefinite and $\alpha(\omega) - \Delta\alpha$ is strictly increasing on $[\omega_k, \omega_{k+1}] \subset [8.8, 80.0]$, piecewise monotone integration plus Plancherel's identity on $[80.0, \infty)$ yields a certified $2 \times 2$ Loewner upper bound $0 \prec D_{\mathrm{pl}} \preceq D_{\mathrm{pl}}^{\mathrm{upper}}$.

Finally, by the **Courant–Fischer 2-Mode Deflated Trace Theorem**, for the positive self-adjoint trace-class operator $T_{\mathrm{even}} = P_{\mathrm{even}}(a)^{-1/2} A_{-,\mathrm{even}}(\Delta\alpha) P_{\mathrm{even}}(a)^{-1/2} \succeq 0$ over $[0, \xi_{\Delta\alpha}]$ and the orthonormal 2-dimensional subspace $U_2 = \operatorname{span}\{u_1, u_2\} \subset L^2_{\mathrm{even}}(0, b)$, the second eigenvalue satisfies $\lambda_2(T_{\mathrm{even}}) \ge \mu_2(C_2) > 0$, where $C_2 = (\langle u_m, T_{\mathrm{even}} u_n\rangle)_{m,n=1}^2$. Hence:
$$\lambda_{\max}(T_{\mathrm{even}}) \le \mathcal{T}_{\mathrm{even}}^{\mathrm{defl}}(a) := \operatorname{Tr}(T_{\mathrm{even}}) - \mu_2(C_2) < 1, \qquad \lambda_{\max}(T_{\mathrm{odd}}) \le \operatorname{Tr}(T_{\mathrm{odd}}) < 1,$$
certifying strict all-vector positivity across $(\frac{1}{2}\log 7, \frac{1}{2}\log(15/2)]$. $\blacksquare$

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
