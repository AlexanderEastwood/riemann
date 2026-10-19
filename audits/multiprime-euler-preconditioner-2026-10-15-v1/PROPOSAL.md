# Milestone 7 Proposal: Multi-Prime Split-Pole Causal Euler Preconditioner ($B_{\mathcal{P}_+, \mathcal{P}_-}$ and $B_{2, 3}$), the Mertens Zero-Shift Diagonal Gain Theorem, and All-Vector Weil Positivity on $\operatorname{Ran}(B_{2, 3})$ Up to $a = \frac{1}{2}\log 10$

**Date:** 2026-10-15  
**Lane:** `KERNEL-API` (`multiprime-euler-preconditioner-2026-10-15-v1`, Audit-Repaired v2)  
**Status:** Certified in 384-bit `flint.arb` (`verify_multiprime_euler.py`, `pyright` clean: `0 errors, 0 warnings, 0 informations`).

> **Wall check:** No claim in this proposal closes **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, or either of the **two historical missing-original evidence groups** (`2026-08-19-chatgpt-5-pro-g2-brainstorm.txt` and `2026-09-29-chatgpt-5-pro-nb-bottleneck-prompts/`) recorded in `evidence/MISSING.md`. All four remain **OPEN**.

---

## 1. Motivation & Subspace Qualification

In Milestones 3, 5, and 6 (`all-vector-positivity-beyond-log6`, `beyond-log7`, `three-island-horizon`), all-vector Weil positivity on the single-prime preconditioned subspace $\operatorname{Ran}(\widetilde{E}_2 \widetilde{E}_2^*) \subset L^2_{\mathrm{pole\text{-}free}}(-a, a)$ was certified up to $a = 1.070000$ using the dyadic ($p = 2$) Euler preconditioner $L_2 = \widetilde{E}_2^* \widetilde{E}_2 = \frac{3}{2}I - \frac{1}{\sqrt{2}}S_{\log 2}$. Because $L_2$ only preconditions $p = 2$:
1. Its zero-shift prime-diagonal-to-core ratio is fixed at
   $$\gamma(L_2^2) = \frac{\frac{5}{2}\log 2}{\frac{13}{4}} = \frac{10}{13}\log 2 \approx 0.53319014,$$
   which cannot grow as $a$ increases.
2. Every odd prime tower ($p = 3, 5, 7, 11, \dots$) remains uncollapsed, generating a rapidly proliferating web of non-commuting reflections and translation fibers ($K = 79$ fiber subintervals, $M_{\mathrm{prime}} = 10$ reflection vectors, and $M_{\mathrm{Planch}} = 3$ midpoint-moment Taylor vectors at $a = 1.070$).

This audit package introduces the **Multi-Prime Split-Pole Causal Euler Preconditioner** $B_{\mathcal{P}_+, \mathcal{P}_-}$, proves the **Universal Single-Prime Causal Euler Identity** (Theorem 1) and the **Fundamental-Theorem-of-Arithmetic + Mertens Zero-Shift Diagonal Gain Theorem** (Theorem 2), and applies the two-prime operator $B_{2, 3} = \widetilde{E}_2 \widetilde{E}_3^*$ to achieve:
- **One-shot closed-form continuum certification** on $\operatorname{Ran}(B_{2, 3}) \subset L^2_{\mathrm{pole\text{-}free}}(-a, a)$ across the entire interval $a \in (\frac{1}{2}\log 6, \log 3] = (\frac{1}{2}\log 6, \frac{1}{2}\log 9] \approx (0.895880, 1.098612]$ with $\Delta_\alpha = 0$ and **zero** rank-1 minorants (Theorem 3), and
- **Continuum and prime-pair certification** on $\operatorname{Ran}(B_{2, 3}) \subset L^2_{\mathrm{pole\text{-}free}}(-a, a)$ across $(\log 3, \frac{1}{2}\log 10] \approx (1.098612, 1.151293]$ via the closed-form $\tau_{3/2}$-reflection involution preconditioner $P_0(a)$, exact continuum 2-piece prime step minorants (with **zero** Plancherel vectors, **zero** Taylor expansions, and **zero** partition discretization), and the **Cauchy–Poincaré Second-Eigenvalue Defect Bound** $\|K\|_{\mathrm{op}} \le \operatorname{Tr}(K) - \mu_2$ (Theorem 4).

### Filtered Subspace vs. Full Pole-Free Window and Horizon Context (`range` & `horizon`)
- **Subspace Qualification (`range`):** For $h \in L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$ ($b_{\mathcal{P}} = a - \frac{1}{2}\sum_{p \in \mathcal{P}} \log p$), the test function $f = B_{\mathcal{P}_+, \mathcal{P}_-} h$ lies in the multi-prime Euler-filtered subspace
  $$\operatorname{Ran}(B_{\mathcal{P}_+, \mathcal{P}_-}) \subsetneq L^2_{\mathrm{pole\text{-}free}}(-a, a) := \{f \in L^2(-a, a) : \widehat{f}(\pm i/2) = 0\}.$$
  Specifically, each factor $\widetilde{E}_p$ ($p \in \mathcal{P}_+$) imposes periodic Fourier zeros $\widehat{f}(+\frac{i}{2} + \frac{2\pi k}{\log p}) = 0$ for all $k \in \mathbb{Z}$, and each factor $\widetilde{E}_q^*$ ($q \in \mathcal{P}_-$) imposes $\widehat{f}(-\frac{i}{2} + \frac{2\pi k}{\log q}) = 0$ for all $k \in \mathbb{Z}$, whereas pole annihilation requires only the $k = 0$ zeros $\widehat{f}(\pm i/2) = 0$. Passing from positivity on the filtered subspaces $\operatorname{Ran}(B_{\mathcal{P}_+, \mathcal{P}_-})$ to full-window positivity on $L^2_{\mathrm{pole\text{-}free}}(-a, a)$ or to a cofinal RH equivalence requires an explicit approximation/density transfer theorem (which remains **OPEN**).
- **Horizon Comparison (`horizon`):** Within the Euler-preconditioned operator family, $B_{2, 3}$ extends the certified horizon from the single-prime $L_2^2$ checkpoint $a = 1.070000$ (`three-island-horizon`) to $a = \frac{1}{2}\log 10 \approx 1.151293$ in this package (and to $a = \frac{1}{2}\log 12 \approx 1.242453$ for $B_{2, 3}$, $a = \log 6 \approx 1.791759$ for $B_{\{2, 3\}, \{5\}}$, and $a = \log 15 \approx 2.708050$ for $B_{\{3, 5\}, \{2, 7\}}$ in Milestone 8). For comparison on the **unfiltered** full pole-free window $L^2_{\mathrm{pole\text{-}free}}(-a, a)$, existing fixed-window complete $\lambda = 4$ certificates already reach $a = \log 4 \approx 1.386294$ (`certified_c1_p128_n96.json`), while the 3-prime and 4-prime primorial windows in Milestone 8 surpass $\log 4$ on their respective filtered subspaces.

---

## 2. Summary of Certified Theorems

1. **Theorem 1 (Universal Single-Prime Causal Euler Identity):**  
   For every prime $p \ge 2$, $\widetilde{E}_p := T_{-\frac{1}{2}\log p} - p^{-1/2}T_{+\frac{1}{2}\log p}$ and $L_p := \widetilde{E}_p^*\widetilde{E}_p = (1 + p^{-1})I - p^{-1/2}S_{\log p}$ satisfy the exact operator identity on $L^2(\mathbb{R})$:
   $$\widetilde{E}_p^* W_p \widetilde{E}_p = L_p W_p = (\log p)\,L_p - (\log p)\left(1 - \frac{1}{p}\right)I = (\log p)\left(\frac{2}{p}\,I - \frac{1}{\sqrt{p}}\,S_{\log p}\right),$$
   identically annihilating all higher prime powers $p^2, p^3, p^4, \dots$ ($k \ge 2$) and converting the zero-shift coefficient of $W_p$ into $+\frac{2\log p}{p}I > 0$.

2. **Theorem 2 (Multi-Prime Split-Pole Preconditioner $B_{\mathcal{P}_+, \mathcal{P}_-}$ and Mertens Zero-Shift Diagonal Gain Theorem):**  
   For any finite set of primes $\mathcal{P} = \mathcal{P}_+ \sqcup \mathcal{P}_-$ ($\mathcal{P}_+ \ne \emptyset, \mathcal{P}_- \ne \emptyset$), the operator
   $$B_{\mathcal{P}_+, \mathcal{P}_-} := \left(\prod_{p \in \mathcal{P}_+} \widetilde{E}_p\right)\left(\prod_{q \in \mathcal{P}_-} \widetilde{E}_q^*\right) : L^2(-b_{\mathcal{P}}, b_{\mathcal{P}}) \longrightarrow L^2(-a, a), \qquad b_{\mathcal{P}} := a - \frac{1}{2}\sum_{p \in \mathcal{P}} \log p$$
   annihilates both pole modes $e^{\pm x/2}$ ($K_{\mathrm{pole}} B_{\mathcal{P}_+, \mathcal{P}_-} = 0$), has self-adjoint parity-preserving compressed pullback $P_{b_{\mathcal{P}}} B_{\mathcal{P}_+, \mathcal{P}_-}^* W B_{\mathcal{P}_+, \mathcal{P}_-} P_{b_{\mathcal{P}}} = P_{b_{\mathcal{P}}} L_{\mathcal{P}} W P_{b_{\mathcal{P}}}$ for every self-adjoint parity-preserving translation-invariant operator $W$ ($L_{\mathcal{P}} = \prod_{p \in \mathcal{P}} L_p$), collapses all prime-power towers $p^k$ ($p \in \mathcal{P}, k \ge 2$) simultaneously, and by unique prime factorization achieves the exact zero-shift diagonal ratio
   $$\gamma(\mathcal{P}) := \frac{C_{\mathrm{diag}}(\mathcal{P})}{C_{\mathrm{zero}}(\mathcal{P})} = \sum_{p \in \mathcal{P}} \frac{2\log p}{p + 1} = 2\log X + O(1) \xrightarrow{X \to \infty} +\infty,$$
   where $C_{\mathrm{zero}}(\mathcal{P}) := [I]L_{\mathcal{P}} = \prod_{p \in \mathcal{P}}(1 + p^{-1})$ is the zero-translation coefficient of $L_{\mathcal{P}}$ (which equals the exact isometric compression constant on $L^2(-b_{\mathcal{P}}, b_{\mathcal{P}})$ whenever $2b_{\mathcal{P}} \le \tau_{\mathrm{iso}}(\mathcal{P})$).

3. **Theorem 3 (One-Shot Continuum Certification on $\operatorname{Ran}(B_{2, 3})$ Across $(\frac{1}{2}\log 6, \log 3] = (\frac{1}{2}\log 6, \frac{1}{2}\log 9]$):**  
   For $\mathcal{P} = \{2, 3\}$, $B_{2, 3} = \widetilde{E}_2 \widetilde{E}_3^*$ increases the zero-shift prime-diagonal ratio to $\gamma(\{2, 3\}) = \frac{2}{3}\log 2 + \frac{1}{2}\log 3 \approx 1.011404$ ($1.896892\times$ the $L_2^2$ ratio). On $(\frac{1}{2}\log 6, \log 3]$, $P_b B_{2, 3}^* B_{2, 3} P_b = 2I$ and $P_b B_{2, 3}^* \mathcal{Q}_{\mathrm{prime}} B_{2, 3} P_b = c_0^{(2, 3)} I - c_{7/6} P_b S_{\tau_{7/6}} P_b - c_{6/5} P_b S_{\tau_{6/5}} P_b$ holds with zero omitted shifts. Using the pointwise-monotone scalar multiplication preconditioner $P_0(a) = V_a(x) I$ at $\Delta_\alpha = 0$ with **zero** rank-1 minorants, a single endpoint evaluation at $a = \log 3 \approx 1.098612$ ($\mathcal{T}_{\mathrm{even}}^{(0)}(\log 3) = 0.9150349476 < 1$, $\mathcal{T}_{\mathrm{odd}}^{(0)}(\log 3) = 0.1036923511 < 1$) certifies the entire continuum interval $(\frac{1}{2}\log 6, \log 3]$.

4. **Theorem 4 (Extension on $\operatorname{Ran}(B_{2, 3})$ Across $(\log 3, \frac{1}{2}\log 10] \approx (1.098612, 1.151293]$):**  
   On $(\log 3, \frac{1}{2}\log 10]$, the only additional active shift is $\tau_{3/2} = \log(3/2)$, which enters with a **positive** coefficient $+c_{3/2} = +\frac{\log 6}{\sqrt{6}} > 0$ on $[x_{3/2}, b] = [\tau_{3/2} - b, b]$ disjoint from $[0, b - \tau_{7/6}]$. Keeping $(v_1 I \pm c_{3/2}(\Delta_\alpha) R_{\tau_{3/2}})$ on $[x_{3/2}, b]$ yields a closed-form inverse $P_0(a)^{-1}$ with sum-of-squares $a$-monotonicity certifying $(\log 3, 1.135000]$ with $M = 0$ minorants ($\mathcal{T}_{\mathrm{even}}^{(0.35)}(1.135) = 0.9960149627 < 1$, $\mathcal{T}_{\mathrm{odd}}^{(0.35)}(1.135) = 0.2932931339 < 1$), and certifying $a = \frac{1}{2}\log 10 \approx 1.151293$ with $M = 4$ (and $M = 8$) exact 2-piece continuum prime step vectors (pairwise orthogonal within each of the 4 positive operator families and inverted jointly via the full $M \times M$ Woodbury matrix $M_{\mathrm{wood}} = B + W^T P_0^{-1} W$) and the Cauchy–Poincaré second-eigenvalue defect bound ($\|K_{\mathrm{even}}\|_{\mathrm{op}} \le 0.9760706672 < 1$).

---

> **Wall check:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
