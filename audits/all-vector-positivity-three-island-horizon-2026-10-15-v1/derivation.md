# Mathematical Derivation — Klein 4-Group Dihedral Fiber Closure up to the Exact Three-Island Isometric Horizon $a_{\star\star\star\star\star} = \frac{3}{2}\log 2 = \frac{1}{2}\log 8$ & Universal Prime-2 Poisson Collapse

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this document claims a proof of RH or global Weil positivity.

---

## 1. Theorem 1 — Klein 4-Group ($\mathbb{Z}_2 \times \mathbb{Z}_2$) Dihedral Fiber Closure on $(\frac{1}{2}\log(15/2), \frac{3}{2}\log 2]$

Let $a \in \left(\frac{1}{2}\log(15/2),\, \frac{3}{2}\log 2\right] = \left(\frac{1}{2}\log(7.5),\, \frac{1}{2}\log 8\right] \approx (1.0074515103,\, 1.0397207708]$, and let $b := a - \log 2 \in \left(\frac{1}{2}\log(15/8),\, \frac{1}{2}\log 2\right] \approx (0.3143043298,\, 0.3465735903]$.

### 1.1 Exact $a$-Independent Midpoint Invariance of the $[x_6, d_5]$ Overlap
Recall that inside $P_0(a)$ on $L^2_{\mathrm{even/odd}}(0, b)$, the two off-diagonal partial isometries retained in the baseline operator are:
- the $m = 5$ shift $T_{\tau_5}: [0, d_5] \leftrightarrow [\tau_5, b]$ with $\tau_5 = \log 5 - 2\log 2 = \log(5/4) \approx 0.2231435513$ and $d_5 = b - \tau_5 = a + \log 2 - \log 5$, and
- the $m = 6$ reflection $R_{\tau_6}f(x) = f(\tau_6 - x)$ on $[x_6, b]$ with $\tau_6 = \log 3 - \log 2 = \log(3/2) \approx 0.4054651081$ and $x_6 = \tau_6 - b = \log 3 - a$.

When $a > \frac{1}{2}\log(15/2)$, we have $x_6 < d_5$, so the left shift domain $[0, d_5]$ and the reflection domain $[x_6, b]$ overlap on the non-empty interval $[x_6, d_5]$.
Observe the **exact $a$-independent sum identity**:
$$x_6 + d_5 = (\tau_6 - b) + (b - \tau_5) = \tau_6 - \tau_5 = \log(6/5) \approx 0.1823215568 \qquad \forall\, a \in \mathbb{R}.$$
Consequently, for every $a \in (\frac{1}{2}\log(15/2), \frac{3}{2}\log 2]$:
1. The overlap interval $[x_6, d_5]$ is **symmetric** about the fixed midpoint $m_{65} := \frac{1}{2}(\tau_6 - \tau_5) = \frac{1}{2}\log(6/5) \approx 0.0911607784$.
2. Its shifted image $[x_6 + \tau_5, d_5 + \tau_5] = [\tau_6 - d_5, b] \subset [\tau_5, b]$ is **symmetric** about $\frac{1}{2}(\tau_6 + \tau_5) = \frac{1}{2}\log(15/8) \approx 0.3143043298$ and equals the reflected image $R_{\tau_6}([x_6, d_5]) = [\tau_6 - d_5, \tau_6 - x_6] = [\tau_6 - d_5, b]$!

### 1.2 Conjugacy in $O(1) = \mathbb{R} \rtimes \{\pm 1\}$ and 4-Cycle Closure
In the 1-dimensional affine orthogonal group $O(1) = \mathbb{R} \rtimes \{\pm 1\}$, let $T_\tau(x) = x + \tau$ denote translation by $\tau$ ($\det = +1$) and $R_\sigma(x) = \sigma - x$ denote reflection across $\sigma/2$ ($\det = -1$). For any $\sigma, \tau \in \mathbb{R}$ and any $x \in \mathbb{R}$:
$$\left(R_\sigma \circ T_{-\tau} \circ R_\sigma\right)(x) = \sigma - \bigl((\sigma - x) - \tau\bigr) = x + \tau = T_\tau(x),$$
$$\left(R_\sigma \circ T_{\tau}\right)(x) = \sigma - (x + \tau) = (\sigma - \tau) - x = R_{\sigma - \tau}(x),$$
$$\left(T_{\tau} \circ R_\sigma\right)(x) = (\sigma - x) + \tau = (\sigma + \tau) - x = R_{\sigma + \tau}(x).$$
Applying these exact identities with $\sigma = \tau_6$ and $\tau = \tau_5$ on $[x_6, d_5] \cup [\tau_6 - d_5, b]$:
- Every $x \in [x_6, d_5]$ generates a **closed 4-element orbit**
  $$\mathcal{O}_x = \bigl\{\, x,\; y := x + \tau_5,\; x' := (\tau_6 - \tau_5) - x,\; y' := \tau_6 - x \,\bigr\},$$
  where $x, x' \in [x_6, d_5]$ and $y, y' \in [\tau_6 - d_5, b]$.
- On $\mathcal{O}_x = \{x, y, x', y'\}$, the partial isometries $T_{\pm\tau_5}$ and $R_{\tau_6}$ act as the **Klein 4-group $\mathbb{Z}_2 \times \mathbb{Z}_2$**:
  - Identity $I$: $(x, y, x', y') \mapsto (x, y, x', y')$ (shift $0$, $\det = +1$),
  - Translation $T_{\pm\tau_5}$: $x \leftrightarrow y$ and $x' \leftrightarrow y'$ (shift $\pm\tau_5$, $\det = +1$),
  - Reflection $R_{\tau_6}$: $x \leftrightarrow y'$ and $x' \leftrightarrow y$ (reflection sum $\tau_6$, $\det = -1$),
  - Composite Reflection $R_{\tau_6} T_{\pm\tau_5}$: $x \leftrightarrow x'$ (reflection sum $\tau_6 - \tau_5$, $\det = -1$) and $y \leftrightarrow y'$ (reflection sum $\tau_6 + \tau_5$, $\det = -1$).

### 1.3 Block Diagonalization of the $4 \times 4$ Fiber Matrix into Two $2 \times 2$ Blocks
Because the diagonal potential $v(z)$ of $P_0(a)$ takes equal values on $x, x' \in [x_6, d_5]$ ($v(x) = v(x') =: v_x = \text{base}_0 - c_5 - c_3$) and on $y, y' \in [\tau_6 - d_5, b]$ ($v(y) = v(y') =: v_y$, after partitioning at $\tau_3$), the $4 \times 4$ fiber matrix of $P_0(a)$ in the basis $(e_x, e_y, e_{x'}, e_{y'})$ is:
$$F_4^{(\pm)} = \begin{pmatrix}
v_x & -c_5 & 0 & \pm c_6 \\
-c_5 & v_y & \pm c_6 & 0 \\
0 & \pm c_6 & v_x & -c_5 \\
\pm c_6 & 0 & -c_5 & v_y
\end{pmatrix}$$
($+c_6$ in the even sector, $-c_6$ in the odd sector). Under the orthogonal change of basis
$$u_\pm := \frac{e_x \pm e_{x'}}{\sqrt{2}}, \qquad w_\pm := \frac{e_y \pm e_{y'}}{\sqrt{2}},$$
$F_4^{(\pm)}$ splits into the direct sum of **two $2 \times 2$ symmetric blocks**:
$$B_+ = \begin{pmatrix} v_x & -c_5 + c_6 \\ -c_5 + c_6 & v_y \end{pmatrix}, \qquad B_- = \begin{pmatrix} v_x & -c_5 - c_6 \\ -c_5 - c_6 & v_y \end{pmatrix},$$
with closed-form determinant
$$\det(B_\pm) = v_x v_y - (c_5 \mp c_6)^2 \ge v_x v_y - (c_5 + c_6)^2 > 0$$
and minimum eigenvalue
$$\lambda_{\min}(F_4^{(\pm)}) = \frac{v_x + v_y - \sqrt{(v_x - v_y)^2 + 4(c_5 + c_6)^2}}{2} > 0. \qquad \blacksquare$$

### 1.4 Exact Domain $[0, \tau_3]$ of the $m = 3$ Reflection $R_{\tau_3}$ When $b > \tau_3$ ($a > \log(8/3)$)
For $g \in L^2_{\mathrm{even}}(0, b)$, the $m = 3$ shift on $L^2(-b, b)$ restricts to $T_{\tau_3} + T_{-\tau_3} + R_{\tau_3}$, where:
- $(R_{\tau_3} g)(x) = g(\tau_3 - x)$ requires both $x \in [0, b]$ and $\tau_3 - x \in [0, b]$. When $b > \tau_3$ ($a > \log(8/3) \approx 0.980829$), this holds **if and only if $x \in [0, \tau_3]$**; for $x \in (\tau_3, b]$, $\tau_3 - x < 0 \notin [0, b]$, so $R_{\tau_3}$ acts as zero on $(\tau_3, b]$.
- On $(\tau_3, b]$, only the shift $T_{-\tau_3}: [0, s_3] \to [\tau_3, b]$ ($s_3 = b - \tau_3$) acts!
Consequently, on $(\tau_3, b]$ the Schur-complement diagonal penalty from $m = 3$ is $-c_3$ (from $T_{-\tau_3}$ alone), giving:
$$v_y = c_0 + \frac{13}{4}\Delta\alpha - c_3 - c_7 \approx 1.86049 + \frac{13}{4}(\Delta\alpha - 0.25) \quad \text{on } (\tau_3, b],$$
$$v_x = c_0 + \frac{13}{4}\Delta\alpha - c_3 - c_3 = c_0 + \frac{13}{4}\Delta\alpha - 2c_3 \approx 1.71654 + \frac{13}{4}(\Delta\alpha - 0.25) \quad \text{on } [0, s_3],$$
$$v_x = c_0 + \frac{13}{4}\Delta\alpha - c_3 \approx 2.38798 + \frac{13}{4}(\Delta\alpha - 0.25) \quad \text{on } (s_3, d_5],$$
and therefore $\det(B_-) = v_x v_y - (c_5 + c_6)^2 \ge +0.5676 > 0$ across the entire regime $(\log(8/3), \frac{3}{2}\log 2]$ with unit Schur weights ($\gamma_3 = 1$)!

---

## 2. Theorem 2 — Exact Triple Coincidence at the Three-Island Isometric Horizon $a_{\star\star\star\star\star} = \frac{3}{2}\log 2 = \frac{1}{2}\log 8$

At $a = a_{\star\star\star\star\star} := \frac{3}{2}\log 2 = \frac{1}{2}\log 8 \approx 1.0397207708$, where $b = a - \log 2 = \frac{1}{2}\log 2 \approx 0.3465735903$, three distinct geometric and arithmetic thresholds coincide simultaneously:
1. **Saturation of the Three-Island Isometric Core**:
   $$2b = \log 2, \qquad P_b L_2^2 P_b = \frac{13}{4} I_{L^2(-b,b)}.$$
2. **Boundary of the $n = 2^3 = 8$ Prime-Power Shift**:
   $$2a = 3\log 2 = \log 8,$$
   so $n \in \{2, 3, 4, 5, 7\}$ remain the only prime powers with $\log n < 2a$.
3. **Exact Meeting of the $m = 3$ Shift Domain $[0, s_3]$ and the $m = 6$ Reflection Endpoint $x_6$**:
   Since $\tau_6 + \tau_3 = (\log 3 - \log 2) + (2\log 2 - \log 3) = \log 2$ identically, we have for every $a$:
   $$x_6 - s_3 = (\tau_6 - b) - (b - \tau_3) = \tau_6 + \tau_3 - 2b = \log 2 - 2b.$$
   Hence $s_3 \le x_6$ holds on the entire Three-Island regime $a \le \frac{3}{2}\log 2$, with **exact equality**
   $$s_3 = x_6 = \log 3 - \frac{3}{2}\log 2 = \frac{1}{2}\log(9/8) \approx 0.0588915178 \qquad \text{at } a = \frac{3}{2}\log 2 = \frac{1}{2}\log 8! \qquad \blacksquare$$

---

## 3. Theorem 3 — Universal Prime-2 Poisson Collapse Identity for All $a > \log 2$

What happens to the prime-2 chain $\sum_{m \ge 1, m\log 2 < 2a} \frac{\log 2}{2^{m/2}} (T_{m\log 2} + T_{-m\log 2})$ when $a > \frac{3}{2}\log 2$ ($2b > \log 2$), where $m = 3$ ($n = 8$), $m = 4$ ($n = 16$), $m = 5$ ($n = 32$), $\dots$ enter $V_a$?

**Theorem 3 (Universal Prime-2 Poisson Collapse).** *Let $\ell_2 = \log 2$, $r_2 = 2^{-1/2}$, and $L_2 = \frac{3}{2}I - r_2(T_{\ell_2} + T_{-\ell_2})$. For **every** $a > \log 2$ ($b = a - \log 2 > 0$) and every $g \in V_b = L^2(-b, b)$, the finite prime-2 sum $\sum_{m \ge 1, m\ell_2 < 2a} \ell_2 r_2^m \langle (T_{m\ell_2} + T_{-m\ell_2}) L_2 g, L_2 g \rangle_{L^2(\mathbb{R})}$ collapses identically to the 3-term tridiagonal shift form:*
$$-\ell_2 \sum_{\substack{m \ge 1 \\ m\ell_2 < 2a}} r_2^m \langle (T_{m\ell_2} + T_{-m\ell_2}) L_2 g, L_2 g \rangle = \ell_2 \left\langle \left(L_2^2 - \frac{1}{2}L_2\right) g, g \right\rangle_{L^2(-b,b)}$$
$$= \ell_2 \left\langle \left(\frac{5}{2}I - \frac{5}{2\sqrt{2}}(T_{\ell_2} + T_{-\ell_2}) + \frac{1}{2}(T_{2\ell_2} + T_{-2\ell_2})\right) g, g \right\rangle_{L^2(-b,b)}.$$

*Proof.* Since $\operatorname{supp}(g) \subset [-b, b]$, we have $\operatorname{supp}(L_2 g) \subset [-(b+\ell_2), b+\ell_2] = [-a, a]$. Thus for every $m \ge 1$ with $m\ell_2 \ge 2a$, $\langle T_{\pm m\ell_2} L_2 g, L_2 g \rangle = 0$ identically, so the finite sum over $m\ell_2 < 2a$ equals the complete norm-convergent series $\langle S^{(2)} L_2 g, L_2 g \rangle$, where $S^{(2)} = \sum_{m=1}^\infty r_2^m (T_{m\ell_2} + T_{-m\ell_2})$.
On $L^2(\mathbb{R})$, the Fourier symbol of $I + S^{(2)}$ is the Poisson kernel
$$1 + 2\sum_{m=1}^\infty r_2^m \cos(m\ell_2 \xi) = \frac{1 - r_2^2}{1 - 2r_2\cos(\ell_2\xi) + r_2^2} = \frac{1/2}{3/2 - \sqrt{2}\cos(\ell_2\xi)} = \frac{1}{2}\,\sigma(L_2)(\xi)^{-1}.$$
Hence $I + S^{(2)} = \frac{1}{2}L_2^{-1}$, so $S^{(2)} = \frac{1}{2}L_2^{-1} - I$, and sandwiching between $L_2$ and $L_2$ gives
$$-L_2 S^{(2)} L_2 = L_2^2 - \frac{1}{2}L_2 = \left(\frac{13}{4}I - \frac{3}{\sqrt{2}}(T_{\ell_2}+T_{-\ell_2}) + \frac{1}{2}(T_{2\ell_2}+T_{-2\ell_2})\right) - \left(\frac{3}{4}I - \frac{1}{2\sqrt{2}}(T_{\ell_2}+T_{-\ell_2})\right)$$
$$= \frac{5}{2}I - \frac{5}{2\sqrt{2}}(T_{\ell_2} + T_{-\ell_2}) + \frac{1}{2}(T_{2\ell_2} + T_{-2\ell_2}). \qquad \blacksquare$$

---

## 4. Theorem 4 — Courant–Fischer 2-Mode Deflated Trace Theorem and Exact Fubini–Plancherel Identity

**Theorem 4 (Courant–Fischer 2-Mode Deflated Trace Certificate).** *Let $P(a) \succ 0$ and $A_-(\Delta\alpha) \succeq 0$ be the positive definite baseline/Woodbury operator and the low-frequency negative-part operator on $L^2_{\mathrm{even}}(0, b)$ with shift $\Delta\alpha \ge 0$ and root $\alpha(\xi_{\Delta\alpha}) = \Delta\alpha$, so that $A(a) \succeq P(a) - A_-(\Delta\alpha)$. Let $K := P(a)^{-1/2} A_-(\Delta\alpha) P(a)^{-1/2} \succeq 0$ have eigenvalues $\lambda_1(K) \ge \lambda_2(K) \ge \dots \ge 0$.*

*For any two linearly independent step functions $\psi_1, \psi_2 \in \mathcal{S}_K \subset L^2_{\mathrm{even}}(0, b)$, set $u_r := P(a)^{1/2}\psi_r$ ($r \in \{1, 2\}$), and define the $2 \times 2$ matrices:*
$$M_{rs} := \langle u_r, K u_s \rangle_{L^2(0,b)} = \langle \psi_r, A_-(\Delta\alpha)\psi_s \rangle_{L^2(0,b)} = \int_0^{\xi_{\Delta\alpha}} \frac{2}{\pi}(\Delta\alpha - \alpha(\xi))\sigma(L_2)(\xi)^2 \widehat{\psi}_r(\xi)\widehat{\psi}_s(\xi)\,d\xi,$$
$$G_{rs} := \langle u_r, u_s \rangle_{L^2(0,b)} = \langle \psi_r, P(a)\psi_s \rangle_{L^2(0,b)}$$
$$= \langle \psi_r, P_0(a)\psi_s \rangle + \sum_{k=1}^{R_{\mathrm{pr}}} d_{\mathrm{pr},k}^{-1}\langle \psi_r, \phi_k\rangle\langle \phi_k, \psi_s\rangle + \sum_{p,q=1}^{M_p} \bigl((D_{\mathrm{pl}}^{\mathrm{upper}})^{-1}\bigr)_{pq} \langle \psi_r, W_p\rangle\langle W_q, \psi_s\rangle,$$
*where for each $p \in \{1, \dots, M_p\}$ and $r \in \{1, 2\}$, by Fubini–Plancherel on $L^2(0, b)$,*
$$\langle \psi_r, W_p \rangle_{L^2(0,b)} = \frac{13}{4}\langle \psi_r, w_p \rangle_{L^2(0,b)} - \int_0^{\xi_1} \frac{2}{\pi}\sigma(L_2)(\omega)^2 \widehat{\psi}_r(\omega)\widehat{w}_p(\omega)\,d\omega.$$
*If $G \succ 0$ and $\mu_2 := \lambda_{\min}(G^{-1}M) > 0$, then by the Courant–Fischer Min-Max Theorem $\lambda_2(K) \ge \mu_2$, and hence:*
$$\lambda_{\max}(K) = \lambda_1(K) \le \mathrm{Tr}(K) - \lambda_2(K) \le \mathcal{T}_{\mathrm{defl}}(a) := \mathrm{Tr}\!\left(P(a)^{-1}A_-(\Delta\alpha)\right) - \mu_2.$$
*In particular, if $\mathcal{T}_{\mathrm{defl}}(a) < 1$, then $P(a) - A_-(\Delta\alpha) \succ 0$ and $A(a) \succeq (1 - \mathcal{T}_{\mathrm{defl}}(a))P(a) \succ 0$ on all of $L^2_{\mathrm{even}}(0, b)$.*

*Proof.* Since $K \succeq 0$ is trace-class on $L^2_{\mathrm{even}}(0, b)$, $\mathrm{Tr}(K) = \sum_{j=1}^\infty \lambda_j(K) \ge \lambda_1(K) + \lambda_2(K)$. By the 2-dimensional Courant–Fischer Min-Max Principle,
$$\lambda_2(K) = \sup_{\substack{U \subset L^2_{\mathrm{even}}(0,b) \\ \dim U = 2}} \min_{0 \ne u \in U} \frac{\langle u, K u \rangle}{\langle u, u \rangle} \ge \min_{0 \ne c \in \mathbb{R}^2} \frac{c^T M c}{c^T G c} = \lambda_{\min}(G^{-1}M) = \mu_2.$$
Moreover, for $u_r = P(a)^{1/2}\psi_r$ with $\psi_r \in \mathcal{S}_K$, the factor $P(a)^{1/2}$ cancels $P(a)^{-1/2}$ in $\langle u_r, K u_s \rangle = \langle \psi_r, A_-(\Delta\alpha)\psi_s \rangle$, while in $G_{rs} = \langle \psi_r, P(a)\psi_s \rangle$ the projection $W_p(x) = \int_0^{\xi_1} \sqrt{\frac{2}{\pi}}\sigma(L_2)(\omega)(L_2 w_p)\widehat{\;}(\omega)\cos(\omega x)\,d\omega - \int_0^b k_{\mathrm{high}}(x, y)w_p(y)\,dy$ satisfies for every $\psi_r \in L^2_{\mathrm{even}}(0, b)$:
$$\langle \psi_r, W_p \rangle_{L^2(0,b)} = \langle L_2 \psi_r, L_2 w_p \rangle_{L^2(\mathbb{R})} - \int_0^{\xi_1} \frac{2}{\pi}\sigma(L_2)(\omega)^2 \widehat{\psi}_r(\omega)\widehat{w}_p(\omega)\,d\omega$$
$$= \frac{13}{4}\langle \psi_r, w_p \rangle_{L^2(0,b)} - \int_0^{\xi_1} \frac{2}{\pi}\sigma(L_2)(\omega)^2 \widehat{\psi}_r(\omega)\widehat{w}_p(\omega)\,d\omega$$
whenever $2b \le \log 2$ ($a \le \frac{3}{2}\log 2$). Since both $\psi_r$ and $w_p$ are step functions on the partition $\mathcal{P}_K$, every inner product in $M$ and $G$ is an exact finite 1D integral on $[0, \xi_{\Delta\alpha}]$ or $[0, \xi_1]$. $\blacksquare$

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
