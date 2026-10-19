# Complete Mathematical Derivation: Multi-Prime Split-Pole Causal Euler Preconditioner ($B_{\mathcal{P}_+, \mathcal{P}_-}$ and $B_{2, 3}$), the Mertens Zero-Shift Diagonal Gain Theorem, and All-Vector Weil Positivity on $\operatorname{Ran}(B_{2, 3})$ Up to $a = \frac{1}{2}\log 10$

**Date:** 2026-10-15  
**Lane:** `KERNEL-API` (`multiprime-euler-preconditioner-2026-10-15-v1`, Audit-Repaired v2)

> **Wall check:** No derivation in this document closes **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, or either of the **two historical missing-original evidence groups** in `evidence/MISSING.md`. All four remain **OPEN**.

---

## 1. Theorem 1: Universal Single-Prime Causal Euler Identity for All Primes $p \ge 2$

For any prime $p \ge 2$, define the causal half-shift Euler operator and its adjoint on $L^2(\mathbb{R})$ by
$$\widetilde{E}_p := T_{-\frac{1}{2}\log p} - p^{-1/2} T_{+\frac{1}{2}\log p}, \qquad \widetilde{E}_p^* = T_{+\frac{1}{2}\log p} - p^{-1/2} T_{-\frac{1}{2}\log p},$$
where $(T_u f)(x) := f(x - u)$. Their product is the self-adjoint, parity-preserving 3-tap prime Laplacian
$$L_p := \widetilde{E}_p^* \widetilde{E}_p = \widetilde{E}_p \widetilde{E}_p^* = \left(1 + \frac{1}{p}\right)I - \frac{1}{\sqrt{p}}\,S_{\log p}, \qquad S_\tau := T_\tau + T_{-\tau},$$
with Fourier symbol $\sigma_{L_p}(\xi) = 1 + p^{-1} - 2p^{-1/2}\cos(\xi\log p) = |e^{i\frac{\xi}{2}\log p} - p^{-1/2}e^{-i\frac{\xi}{2}\log p}|^2 \ge (1 - p^{-1/2})^2 > 0$.

Let $W_p := -\sum_{k=1}^\infty (\log p) p^{-k/2} S_{k\log p}$ be the full prime-$p$ Weil shift operator on $L^2(\mathbb{R})$.

**Theorem 1.** *For every prime $p \ge 2$, the operators $L_p$ and $W_p$ satisfy the exact algebraic identity on $L^2(\mathbb{R})$:*
$$\widetilde{E}_p^* W_p \widetilde{E}_p = L_p W_p = (\log p)\,L_p - (\log p)\left(1 - \frac{1}{p}\right)I = (\log p)\left(\frac{2}{p}\,I - \frac{1}{\sqrt{p}}\,S_{\log p}\right).$$

*Proof.* Set $z := p^{-1/2} T_{\log p}$. Since $\|z\|_{\mathrm{op}} = p^{-1/2} \le 2^{-1/2} < 1$, the geometric series $\sum_{k=1}^\infty z^k = z(I - z)^{-1}$ converges in operator norm on $L^2(\mathbb{R})$, and
$$W_p = -(\log p)\sum_{k=1}^\infty \bigl(z^k + (z^*)^k\bigr) = -(\log p)\left(z(I - z)^{-1} + z^*(I - z^*)^{-1}\right).$$
Observe that $(I - z)(I - z^*) = I - (z + z^*) + z z^* = (1 + p^{-1})I - p^{-1/2} S_{\log p} = L_p$. Multiplying $W_p$ by $L_p = (I - z)(I - z^*)$ gives
$$L_p W_p = -(\log p)\bigl(z(I - z^*) + z^*(I - z)\bigr) = -(\log p)\bigl(z + z^* - 2 z z^*\bigr) = (\log p)\left(\frac{2}{p}\,I - \frac{1}{\sqrt{p}}\,S_{\log p}\right).$$
Comparing with $(\log p)L_p = (\log p)\bigl((1 + p^{-1})I - p^{-1/2}S_{\log p}\bigr)$ yields $L_p W_p = (\log p)L_p - (\log p)(1 - p^{-1})I$. Since $\widetilde{E}_p$ commutes with every translation-invariant operator $W_p$, $\widetilde{E}_p^* W_p \widetilde{E}_p = \widetilde{E}_p^* \widetilde{E}_p W_p = L_p W_p$. $\square$

---

## 2. Theorem 2: Multi-Prime Split-Pole Preconditioner $B_{\mathcal{P}_+, \mathcal{P}_-}$ and the Mertens Zero-Shift Diagonal Gain Theorem

Let $\mathcal{P} = \mathcal{P}_+ \sqcup \mathcal{P}_-$ be any finite set of primes partitioned into two non-empty subsets $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$. For any $a > \frac{1}{2}\sum_{p \in \mathcal{P}} \log p$, set $b_{\mathcal{P}} := a - \frac{1}{2}\sum_{p \in \mathcal{P}} \log p > 0$ and define the **Split-Pole Causal Euler Operator**:
$$B_{\mathcal{P}_+, \mathcal{P}_-} := \left(\prod_{p \in \mathcal{P}_+} \widetilde{E}_p\right)\left(\prod_{q \in \mathcal{P}_-} \widetilde{E}_q^*\right) : L^2(-b_{\mathcal{P}}, b_{\mathcal{P}}) \longrightarrow L^2(-a, a).$$

**Theorem 2.** *For every $a > \frac{1}{2}\sum_{p \in \mathcal{P}} \log p$:*
1. **Half-Shift Support Budget & Filtered Subspace (`range`):** *Each factor $\widetilde{E}_p$ or $\widetilde{E}_p^*$ expands support by $\pm\frac{1}{2}\log p$, so $\operatorname{supp}(B_{\mathcal{P}_+, \mathcal{P}_-} h) \subset [-a, a]$ for all $h \in L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$ without any truncation projection $P_a$. As $h$ ranges over $L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$, $f = B_{\mathcal{P}_+, \mathcal{P}_-} h$ ranges over the multi-prime Euler-filtered subspace*
   $$\operatorname{Ran}(B_{\mathcal{P}_+, \mathcal{P}_-}) \subsetneq L^2_{\mathrm{pole\text{-}free}}(-a, a) := \{f \in L^2(-a, a) : \widehat{f}(\pm i/2) = 0\},$$
   *consisting of functions in $L^2(-a, a)$ satisfying the periodic Fourier vanishing conditions $\widehat{f}(+\frac{i}{2} + \frac{2\pi k}{\log p}) = 0$ ($\forall p \in \mathcal{P}_+, k \in \mathbb{Z}$) and $\widehat{f}(-\frac{i}{2} + \frac{2\pi k}{\log q}) = 0$ ($\forall q \in \mathcal{P}_-, k \in \mathbb{Z}$).*
2. **Exact Bilateral Pole Annihilation:** *For every $p \in \mathcal{P}_+$, $\widetilde{E}_p^*(e^{+x/2}) = (p^{-1/4} - p^{-1/2}p^{+1/4})e^{x/2} = 0$, and for every $q \in \mathcal{P}_-$, $\widetilde{E}_q(e^{-x/2}) = (q^{-1/4} - q^{-1/2}q^{+1/4})e^{-x/2} = 0$. Since all factors commute, $\langle B_{\mathcal{P}_+, \mathcal{P}_-} h, e^{\pm x/2} \rangle_{L^2(-a, a)} = 0$ for all $h \in L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$, and thus $B_{\mathcal{P}_+, \mathcal{P}_-}^* K_{\mathrm{pole}} B_{\mathcal{P}_+, \mathcal{P}_-} = 0$ identically.*
3. **Self-Adjoint Parity-Preserving Compressed Pullback (`parity`):** *For any self-adjoint, parity-preserving translation-invariant operator $W$ on $L^2(\mathbb{R})$ (such as $S_\tau = T_\tau + T_{-\tau}$, $W_p$, or $\alpha(D)$), we have on $L^2(\mathbb{R})$*
   $$B_{\mathcal{P}_+, \mathcal{P}_-}^* W B_{\mathcal{P}_+, \mathcal{P}_-} = L_{\mathcal{P}} W, \qquad L_{\mathcal{P}} := B_{\mathcal{P}_+, \mathcal{P}_-}^* B_{\mathcal{P}_+, \mathcal{P}_-} = \prod_{p \in \mathcal{P}} L_p,$$
   *and restricting to $h \in L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$ via the orthogonal projection $P_{b_{\mathcal{P}}} : L^2(\mathbb{R}) \to L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$ yields the compressed operator $P_{b_{\mathcal{P}}} L_{\mathcal{P}} W P_{b_{\mathcal{P}}}$ on $L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$. Because $P_{b_{\mathcal{P}}}$, $L_{\mathcal{P}}$, and $W$ are all self-adjoint and commute with the parity reflection $(R_0 h)(x) = h(-x)$, $P_{b_{\mathcal{P}}} L_{\mathcal{P}} W P_{b_{\mathcal{P}}}$ is self-adjoint and preserves the orthogonal decomposition $L^2(-b_{\mathcal{P}}, b_{\mathcal{P}}) = L^2_{\mathrm{even}}(0, b_{\mathcal{P}}) \oplus L^2_{\mathrm{odd}}(0, b_{\mathcal{P}})$.*
4. **Simultaneous Multi-Prime Tower Collapse:** *Summing Theorem 1 over $p \in \mathcal{P}$ and multiplying by $\prod_{q \in \mathcal{P} \setminus \{p\}} L_q$ gives the exact finite Laurent polynomial identity on $L^2(\mathbb{R})$:*
   $$B_{\mathcal{P}_+, \mathcal{P}_-}^*\left(\sum_{p \in \mathcal{P}} W_p\right) B_{\mathcal{P}_+, \mathcal{P}_-} = \left(\sum_{p \in \mathcal{P}} \log p\right) L_{\mathcal{P}} - \sum_{p \in \mathcal{P}} (\log p)\left(1 - \frac{1}{p}\right)\prod_{q \in \mathcal{P} \setminus \{p\}} L_q,$$
   *in which all higher prime powers $p^k$ ($k \ge 2, p \in \mathcal{P}$) are identically eliminated.*
5. **Fundamental Theorem of Arithmetic + Mertens Zero-Shift Diagonal Gain (`diagonal`):** *Expanding $L_{\mathcal{P}} = \prod_{p \in \mathcal{P}} \bigl((1 + p^{-1})I - p^{-1/2}(T_{\log p} + T_{-\log p})\bigr)$ produces shifts at $\tau(\varepsilon) = \sum_{p \in \mathcal{P}} \varepsilon_p \log p = \log\bigl(\prod_{p \in \mathcal{P}} p^{\varepsilon_p}\bigr)$ with $\varepsilon_p \in \{-1, 0, +1\}$. By unique prime factorization in $\mathbb{Z}$, $\tau(\varepsilon) = 0 \iff \varepsilon_p = 0$ for all $p \in \mathcal{P}$. Hence no cross-shift between distinct primes ever lands at $\tau = 0$, and the exact zero-translation ($I$) coefficients of $L_{\mathcal{P}}$ and $B_{\mathcal{P}_+, \mathcal{P}_-}^*(\sum_{p \in \mathcal{P}} W_p)B_{\mathcal{P}_+, \mathcal{P}_-}$ are*
   $$C_{\mathrm{zero}}(\mathcal{P}) := [I]L_{\mathcal{P}} = \prod_{p \in \mathcal{P}}\left(1 + \frac{1}{p}\right), \qquad C_{\mathrm{diag}}(\mathcal{P}) := [I]\left(L_{\mathcal{P}}\sum_{p \in \mathcal{P}} W_p\right) = C_{\mathrm{zero}}(\mathcal{P}) \sum_{p \in \mathcal{P}} \frac{2\log p}{p + 1}.$$
   *By Mertens' first theorem, for $\mathcal{P}_{\le X} = \{p \le X\}$, the zero-shift prime-diagonal-to-core ratio satisfies*
   $$\gamma(\mathcal{P}_{\le X}) := \frac{C_{\mathrm{diag}}(\mathcal{P}_{\le X})}{C_{\mathrm{zero}}(\mathcal{P}_{\le X})} = \sum_{p \le X} \frac{2\log p}{p + 1} = 2\log X + O(1) \xrightarrow{X \to \infty} +\infty.$$
   *When $2b_{\mathcal{P}} \le \tau_{\mathrm{iso}}(\mathcal{P}) := \min\{\tau(\varepsilon) > 0 : \varepsilon \in \{-1, 0, 1\}^{\mathcal{P}}\}$, all non-zero shifts in $L_{\mathcal{P}}$ vanish under $P_{b_{\mathcal{P}}}$, so $P_{b_{\mathcal{P}}} L_{\mathcal{P}} P_{b_{\mathcal{P}}} = C_{\mathrm{zero}}(\mathcal{P}) I_{L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})}$ and $C_{\mathrm{zero}}(\mathcal{P})$ is also the exact isometric compression constant.*
   *Remark on untruncated symbol at $\xi = 0$:* On the full line $L^2(\mathbb{R})$ without spatial truncation $P_{b_{\mathcal{P}}}$, the Fourier multiplier at $\xi = 0$ is $\sigma_{L_{\mathcal{P}}}(0)\sum_{p \in \mathcal{P}} W_p(0) = \bigl(\prod_{p \in \mathcal{P}}(1 - p^{-1/2})^2\bigr)\sum_{p \in \mathcal{P}}\bigl(-\frac{2\log p}{\sqrt{p}-1}\bigr) < 0$ because all shifts $\tau(\varepsilon) > 0$ contribute at $\xi = 0$ on $L^2(\mathbb{R})$. Positivity of the compressed operator on $L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$ relies on the spatial truncation $P_{b_{\mathcal{P}}}$, which annihilates all shifts $|\tau| \ge 2b_{\mathcal{P}}$ and leaves the positive zero-shift diagonal $C_{\mathrm{diag}}(\mathcal{P}) I$ dominant over the surviving shifts $|\tau| < 2b_{\mathcal{P}}$. $\square$

---

## 3. Theorem 3: Exact Two-Prime Split-Pole Preconditioner $B_{2, 3} = \widetilde{E}_2 \widetilde{E}_3^*$ and One-Shot Continuum Certification Across $(\frac{1}{2}\log 6, \log 3] = (\frac{1}{2}\log 6, \frac{1}{2}\log 9]$

Set $\mathcal{P}_+ = \{2\}$ and $\mathcal{P}_- = \{3\}$, so $B_{2, 3} := \widetilde{E}_2 \widetilde{E}_3^* : L^2(-b, b) \to L^2(-a, a)$ with $b = a - \frac{1}{2}\log 6$. Expanding $L_2 L_3$ and Theorem 2(4) gives:
$$L_2 L_3 = 2I - \frac{2\sqrt{2}}{3}S_{\log 2} - \frac{\sqrt{3}}{2}S_{\log 3} + \frac{1}{\sqrt{6}}S_{\log 6} + \frac{1}{\sqrt{6}}S_{\log(3/2)},$$
$$B_{2, 3}^*(W_2 + W_3)B_{2, 3} = c_0^{(2, 3)} I + c_{3/2} S_{\log(3/2)} - \left(\frac{2\sqrt{2}}{3}\log 6 - \frac{\sqrt{2}}{3}\log 3\right)S_{\log 2} - \left(\frac{\sqrt{3}}{2}\log 6 - \frac{\log 2}{2\sqrt{3}}\right)S_{\log 3} + c_{3/2} S_{\log 6},$$
where $c_0^{(2, 3)} = \frac{4}{3}\log 2 + \log 3 \approx 2.0228085294$ and $c_{3/2} = \frac{\log 6}{\sqrt{6}} \approx 0.7314828346$.

**Theorem 3.** *For every $a \in (\frac{1}{2}\log 6, \log 3] = (\frac{1}{2}\log 6, \frac{1}{2}\log 9] \approx (0.895880, 1.098612]$, we have $2b = 2a - \log 6 \le \log(3/2) \approx 0.405465$, and:*
1. **Exact Isometric Core and Exact Two-Shift Prime Compression:** *All non-zero shifts in $L_2 L_3$ and $B_{2, 3}^*(W_2 + W_3)B_{2, 3}$ have length $\ge \log(3/2) \ge 2b$ and vanish identically under compression by $P_b$. Among all primes $p \ge 5$, since $2a \le \log 9$, only $p = 5$ and $p = 7$ ($k = 1$) can overlap $(-a, a)$, and in $L_2 L_3(W_5 + W_7)$ only $\tau_{7/6} = \log(7/6) \approx 0.1541506798$ and $\tau_{6/5} = \log(6/5) \approx 0.1823215568$ have shift $< \log(3/2)$. Thus on $L^2(-b, b)$, with zero omitted terms,*
   $$P_b B_{2, 3}^* B_{2, 3} P_b = 2\,I_{L^2(-b, b)}, \qquad P_b B_{2, 3}^* \mathcal{Q}_{\mathrm{prime}} B_{2, 3} P_b = c_0^{(2, 3)} I_{L^2(-b, b)} - c_{7/6} P_b S_{\tau_{7/6}} P_b - c_{6/5} P_b S_{\tau_{6/5}} P_b,$$
   *where $c_{7/6} := \frac{\log 7}{\sqrt{42}} \approx 0.3002604547$ and $c_{6/5} := \frac{\log 5}{\sqrt{30}} \approx 0.2938418165$.*
2. **Exact Pointwise Schur Decomposition and $a$-Monotonicity:** *For any $\tau > 0$ and $c_\tau > 0$, on $L^2_{\mathrm{even/odd}}(0, b)$ we have the exact operator decomposition*
   $$-c_\tau P_b S_\tau P_b\big|_{L^2_{\mathrm{even/odd}}(0, b)} = -c_\tau N_\tau(x; b) I_{L^2(0, b)} + 2c_\tau P_{\mathrm{anti/sym}}^{(\tau)} + c_\tau D_\tau^* D_\tau \succeq -c_\tau N_\tau(x; b) I_{L^2(0, b)},$$
   *where $N_\tau(x; b) := \mathbf{1}_{x + b > \tau} + \mathbf{1}_{b - x > \tau} \in \{0, 1, 2\}$, $P_{\mathrm{anti/sym}}^{(\tau)} := \frac{1}{2}(I \mp R_\tau)\mathbf{1}_{[\max(0, \tau - b), \min(b, \tau)]} \succeq 0$, and $(D_\tau g)(x) := g(x) - g(x + \tau)$ on $[0, \max(0, b - \tau)]$. Because $N_\tau(x; b)$ is pointwise monotone non-decreasing in $b = a - \frac{1}{2}\log 6$ for every $x \ge 0$, the pure scalar multiplication operator*
   $$P_0(a) := V_a(x) I_{L^2(0, b)}, \qquad V_a(x) := c_0^{(2, 3)} - c_{7/6} N_{\tau_{7/6}}(x; b) - c_{6/5} N_{\tau_{6/5}}(x; b) \ge c_0^{(2, 3)} - 2c_{7/6} - 2c_{6/5} \approx 0.8346039869 > 0$$
   *is pointwise monotone non-increasing in $a$. Consequently, at $\Delta_\alpha = 0$, $\mathcal{T}_{\mathrm{even/odd}}^{(0)}(a) = \operatorname{Tr}\bigl(P_0(a)^{-1} A_-^{(0)}(a)\bigr)$ is strictly increasing in $a$ across $(\frac{1}{2}\log 6, \log 3]$, and a single endpoint evaluation at $a = \log 3 = \frac{1}{2}\log 9 \approx 1.0986122887$ ($\mathcal{T}_{\mathrm{even}}^{(0)}(\log 3) = 0.9150349476 < 1$, $\mathcal{T}_{\mathrm{odd}}^{(0)}(\log 3) = 0.1036923511 < 1$) certifies all-vector Weil positivity on $\operatorname{Ran}(B_{2, 3})$ across the entire continuum interval $a \in (\frac{1}{2}\log 6, \log 3]$.* $\square$

---

## 4. Theorem 4: Extension Across $(\log 3, \frac{1}{2}\log 10]$ via Exact $\tau_{3/2}$-Reflection Involution, Continuum Prime Step Minorants, and the Cauchy–Poincaré Second-Eigenvalue Defect Bound

For $a \in (\log 3, \frac{1}{2}\log 10] \approx (1.0986122887, 1.1512925465]$, we have $2b \in (\log(3/2), \log(5/3)] \approx (0.4054651081, 0.5108256238]$. Every shift with $\tau \ge \log(5/3)$ vanishes identically on $L^2(-b, b)$, while $\tau_{3/2} = \log(3/2)$ enters both $P_b L_2 L_3 P_b = 2I + \frac{1}{\sqrt{6}} P_b S_{\tau_{3/2}} P_b$ and $P_b B_{2, 3}^* \mathcal{Q}_{\mathrm{prime}} B_{2, 3} P_b$ with a **positive** coefficient $+c_{3/2} = +\frac{\log 6}{\sqrt{6}} > 0$. Since $b \le \frac{1}{2}\log(5/3) \approx 0.2554128119 < \tau_{3/2} \approx 0.4054651081$, on $L^2_{\mathrm{even/odd}}(0, b)$ we have $P_b S_{\tau_{3/2}} P_b = \pm R_{\tau_{3/2}} \mathbf{1}_{[x_{3/2}, b]}$ where $x_{3/2} := \tau_{3/2} - b$.

Moreover, across all of $(\log 3, \frac{1}{2}\log 10]$, we have
$$0 < d_{6/5} := b - \tau_{6/5} < d_{7/6} := b - \tau_{7/6} \le \frac{1}{2}\log\left(\frac{60}{49}\right) \approx 0.1012621321 < 0.1500522962 \le x_{3/2} < b,$$
so the double-overlap intervals $[0, d_{6/5}]$ and $[0, d_{7/6}]$ are strictly disjoint from the reflection interval $[x_{3/2}, b]$. Thus we have the **exact operator decomposition** on $L^2_{\mathrm{even/odd}}(0, b)$:
$$P_b B_{2, 3}^*(\mathcal{Q}_{\mathrm{prime}} + \Delta_\alpha I)B_{2, 3} P_b\big|_{L^2_{\mathrm{even/odd}}(0, b)} = P_0^{\mathrm{even/odd}}(a) + 2c_{7/6} P_{\mathrm{anti/sym}}^{(7/6)} + 2c_{6/5} P_{\mathrm{anti/sym}}^{(6/5)} + c_{7/6} D_{\tau_{7/6}}^* D_{\tau_{7/6}} + c_{6/5} D_{\tau_{6/5}}^* D_{\tau_{6/5}},$$
where
$$P_0^{\mathrm{even/odd}}(a) := v_{\mathrm{full}}\mathbf{1}_{[0, d_{6/5}]} + v_{\mathrm{mid}}\mathbf{1}_{[d_{6/5}, d_{7/6}]} + v_1\mathbf{1}_{[d_{7/6}, x_{3/2}]} + \bigl(v_1 I \pm c_{3/2}(\Delta_\alpha) R_{\tau_{3/2}}\bigr)\mathbf{1}_{[x_{3/2}, b]},$$
with $v_{\mathrm{full}} = c_0^{(2, 3)} + 2\Delta_\alpha - 2c_{7/6} - 2c_{6/5}$, $v_{\mathrm{mid}} = v_{\mathrm{full}} + c_{6/5}$, $v_1 = v_{\mathrm{mid}} + c_{7/6}$, and $c_{3/2}(\Delta_\alpha) = \frac{\log 6 + \Delta_\alpha}{\sqrt{6}}$.

1. **Closed-Form Inverse and Sum-of-Squares $a$-Monotonicity on $(\log 3, 1.135000]$ (`stale_numbers` synchronized):**  
   Since $R_{\tau_{3/2}}^2 = I$ on $[x_{3/2}, b]$ and $v_1 > c_{3/2}(\Delta_\alpha) > 0$,
   $$P_0^{\mathrm{even/odd}}(a)^{-1} = \frac{1}{v_{\mathrm{full}}}\mathbf{1}_{[0, d_{6/5}]} + \frac{1}{v_{\mathrm{mid}}}\mathbf{1}_{[d_{6/5}, d_{7/6}]} + \frac{1}{v_1}\mathbf{1}_{[d_{7/6}, x_{3/2}]} + \bigl(\alpha_1 I \mp \beta_1 R_{\tau_{3/2}}\bigr)\mathbf{1}_{[x_{3/2}, b]},$$
   where $\alpha_1 = \frac{v_1}{v_1^2 - c_{3/2}(\Delta_\alpha)^2}$ and $\beta_1 = \frac{c_{3/2}(\Delta_\alpha)}{v_1^2 - c_{3/2}(\Delta_\alpha)^2}$. Differentiating $\langle P_0^{\mathrm{even/odd}}(a)^{-1} u_\xi, u_\xi \rangle_{L^2(0, b)}$ with respect to $a$ (using $\frac{d}{da}(d_{6/5}) = \frac{d}{da}(d_{7/6}) = \frac{db}{da} = +1$ and $\frac{d}{da}(x_{3/2}) = -1$) gives the exact sum of three squares:
   $$\frac{\partial}{\partial a}\left\langle P_0^{\mathrm{even/odd}}(a)^{-1} u_\xi, u_\xi \right\rangle_{L^2(0, b)} = \left(\frac{1}{v_{\mathrm{full}}} - \frac{1}{v_{\mathrm{mid}}}\right)u_\xi(d_{6/5})^2 + \left(\frac{1}{v_{\mathrm{mid}}} - \frac{1}{v_1}\right)u_\xi(d_{7/6})^2 + \frac{\bigl(v_1 u_\xi(b) \mp c_{3/2}(\Delta_\alpha) u_\xi(x_{3/2})\bigr)^2}{v_1\bigl(v_1^2 - c_{3/2}(\Delta_\alpha)^2\bigr)} \ge 0.$$
   At $\Delta_\alpha = \frac{7}{20} = 0.35$, evaluating the single endpoint $a = 1.135000$ gives $\mathcal{T}_{\mathrm{even}}^{(0.35)}(1.135000) = 0.9960149627 < 1$ and $\mathcal{T}_{\mathrm{odd}}^{(0.35)}(1.135000) = 0.2932931339 < 1$, certifying the entire continuum interval $(\log 3, 1.135000]$ with **zero** minorants.

2. **Exact Continuum Step-Function Woodbury Reduction up to $a = \frac{1}{2}\log 10 \approx 1.1512925465$ (`orthogonality` clarified):**  
   Partitioning $[0, d_{7/6}]$, $[0, d_{6/5}]$, $[0, \frac{1}{2}\tau_{7/6}]$, and $[0, \frac{1}{2}\tau_{6/5}]$ into $n_{\mathrm{sub}} \in \{1, 2\}$ equal subintervals yields $M = 4n_{\mathrm{sub}}$ 2-piece step vectors $w_1, \dots, w_M$ that are **pairwise orthogonal within each of the 4 positive operator families** ($D_{\tau_{7/6}}^* D_{\tau_{7/6}}$, $D_{\tau_{6/5}}^* D_{\tau_{6/5}}$, $2c_{7/6} P_{\mathrm{anti}}^{(7/6)}$, and $2c_{6/5} P_{\mathrm{anti}}^{(6/5)}$). By Cauchy–Schwarz within each of the 4 positive operator families independently, adding the 4 valid operator minorants gives
   $$2c_{7/6} P_{\mathrm{anti}}^{(7/6)} + 2c_{6/5} P_{\mathrm{anti}}^{(6/5)} + c_{7/6} D_{\tau_{7/6}}^* D_{\tau_{7/6}} + c_{6/5} D_{\tau_{6/5}}^* D_{\tau_{6/5}} \succeq \sum_{f=1}^4 W_f B_f^{-1} W_f^* = W B^{-1} W^*,$$
   where $B = \operatorname{diag}(b_1, \dots, b_M)$ is diagonal and cross-family inner products are handled exactly by inverting the full $M \times M$ Woodbury matrix $M_{\mathrm{wood}} = B + W^* P_0^{\mathrm{even}}(a)^{-1} W$ (so no cross-family orthogonality is required or assumed).
   Because $P_0^{\mathrm{even}}(a)^{-1}$ maps any step function on $[0, b]$ to an **exact step function** $U_m := P_0^{\mathrm{even}}(a)^{-1} w_m$ on $[0, b]$, the Woodbury trace identity on $L^2(0, b)$ holds **identically in the continuum without any partition discretization or Taylor expansion**:
   $$\operatorname{Tr}\!\left(\bigl(P_0^{\mathrm{even}}(a) + W B^{-1} W^*\bigr)^{-1} A_-^{(\Delta_\alpha)}(a)\right) = \mathcal{T}_{\mathrm{even}, 0}^{(\Delta_\alpha)}(a) - \operatorname{Tr}\!\left((B + W^* U)^{-1} G_-\right),$$
   where $(W^* U)_{ij} = \langle w_i, U_j \rangle_{L^2(0, b)}$ is an exact interval-overlap matrix and $(G_-)_{ij} = \frac{2}{\pi}\int_0^{\xi_0} w_-^{(2, 3)}(\xi; \Delta_\alpha) \widehat{U_i}(\xi)\widehat{U_j}(\xi)\,d\xi$. At $a = \frac{1}{2}\log 10 \approx 1.1512925465$ with $\Delta_\alpha = 0.35$, this gives $\mathcal{T}_{\mathrm{even}}^{(0.35)}(\frac{1}{2}\log 10) = 0.9814962730 < 1$ ($M = 4$) and $0.9801070780 < 1$ ($M = 8$).

3. **Cauchy–Poincaré Second-Eigenvalue Defect Bound:**  
   For any positive semidefinite trace-class operator $K = \widetilde{P}_0^{-1} A_- \succeq 0$ on $(\mathcal{H}, \langle \cdot, \cdot \rangle_{\widetilde{P}_0})$ with eigenvalues $\lambda_1(K) \ge \lambda_2(K) \ge \dots \ge 0$, and any two linearly independent test vectors $u_1, u_2 \in \mathcal{H}$ with $2\times 2$ Gram matrix $M_{ij} = \langle u_i, \widetilde{P}_0 u_j \rangle_{L^2(0, b)}$ and quadratic-form matrix $G_{ij} = \langle u_i, A_- u_j \rangle_{L^2(0, b)}$, the Courant–Fischer–Weyl min-max theorem guarantees $\lambda_2(K) \ge \mu_2(G, M) > 0$, where $\mu_1 \ge \mu_2 > 0$ are the roots of $\det(G - \mu M) = 0$. Therefore,
   $$\|K\|_{\mathrm{op}} = \lambda_1(K) = \operatorname{Tr}(K) - \lambda_2(K) - \sum_{j=3}^\infty \lambda_j(K) \le \operatorname{Tr}(K) - \mu_2(G, M).$$
   Choosing the two half-interval step functions $u_1 = \mathbf{1}_{[0, b/2]}$ and $u_2 = \mathbf{1}_{[b/2, b]}$ at $a = \frac{1}{2}\log 10$ tightens the upper bound on $\|K_{\mathrm{even}}\|_{\mathrm{op}}$ to $0.9773297465 < 1$ ($M = 4$) and $0.9760706672 < 1$ ($M = 8$). $\square$

---

> **Wall check:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
