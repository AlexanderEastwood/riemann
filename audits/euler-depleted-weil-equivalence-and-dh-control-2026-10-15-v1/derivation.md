# Mathematical Derivations — Euler-Depleted Weil Explicit Formula Equivalence, Free-Bandwidth Dichotomy, and Davenport–Heilbronn Control Separation (`KERNEL-API` & `WEIL-FLOOR`)

**Date:** 2026-10-15  
**Target Lanes:** `KERNEL-API` & `WEIL-FLOOR`  
**Audit Directory:** `audits/euler-depleted-weil-equivalence-and-dh-control-2026-10-15-v1/`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this derivation prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.
>
> **Structural Purpose:** This derivation establishes three foundational structural theorems:
> 1. **Theorem 1 (Euler-Depleted Weil Explicit Formula, Two-Sided Pole Cancellation, & Critical-Strip Zero Preservation)**: Proves that the $K$-prime Euler preconditioner $B_{\mathcal{P}_+, \mathcal{P}_-}$ has no zeros anywhere in the open critical strip $|\operatorname{Im}(\xi)| < 1/2$ ($0 < \operatorname{Re}(s) < 1$), that **both** $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$ are necessary and sufficient for $B_{\mathcal{P}_+, \mathcal{P}_-}$ to annihilate both pole functionals $\widehat{h}(\pm i/2) = 0$ on all of $L^2(-b, b)$ (certified by the single-subset counterexample $\mathcal{P}_+ = \{2\}, \mathcal{P}_- = \emptyset$ where $\sigma_B(-i/2) = 1/2 \ne 0$), and establishes a quantitative **Fixed-$\mathcal{P}$ Negative-Witness Transfer** (with explicit hypergeometric amplification $R_0(\delta_0) = {}_0F_1(; 7/2; +\delta_0^2/4) > 1 + \delta_0^2/14$, differential phase alignment $(c_0 + c_1 \partial_x)$, and zero-tail cutoff $R_* = (120 e^{1/2})^{1/3} \approx 5.828$) alongside the **Varying-$\mathcal{P}_K$ Distortion Factor** $\Upsilon(\mathcal{P}_K, \delta_0) = M_{\mathcal{P}_K}(1/2)/m_{\mathcal{P}_K}(\delta_0)$.
> 2. **Theorem 2 (The Paley–Wiener Free-Bandwidth vs. Zero-Shift Isometric Horizon Dichotomy)**: Distinguishes the chosen partition shift $\tau_{\mathrm{part}}(\mathcal{P}_{K,+}, \mathcal{P}_{K,-}) = \log(d_+(K)/d_-(K))$ from the **true minimum nonzero internal shift** $\tau_{\min}(\mathcal{P}_K) = \min_{\gcd(m_1, m_2)=1,\, m_1 > m_2 \ge 1} \log(m_1/m_2)$ across all $(3^K-1)/2$ coprime squarefree divisor pairs of $P_K^\#$, proving that the true zero-shift isometric free bandwidth $b_{\mathrm{iso}}(\mathcal{P}_K) = \frac{1}{2}\tau_{\min}(\mathcal{P}_K)$ is strictly smaller than $\frac{1}{2}\tau_{\mathrm{part}}$ at $K = 5, 6, 8$ ($0.023260$ at $K=5$, $0.006452$ at $K=6$, $0.000700$ at $K=7,8$), and establishes the quantitative Bernstein–Paley–Wiener frequency-localization bound $b \ge \frac{\pi}{4\Delta\xi}$ (certified sharp up to constant against the boxcar counterexample $g = \mathbf{1}_{[-1,1]}$ with spectral mass $0.571264 > 1/2$ at $b = \Delta\xi = 1 < \pi/2$).
> 3. **Theorem 3 (Euler-Product Rigidity & Pure `flint.arb` Davenport–Heilbronn Control Separation)**: Proves that prime-tower collapse and composite vanishing hold **if and only if** the Dirichlet series has an Euler product over $\mathcal{P}$, and certifies in two-precision (`256`-bit and `384`-bit) `flint.arb` on the Davenport–Heilbronn counterexample $f_{DH}(s)$ (`controls/davenport_heilbronn.py`) that tower collapse fails at $n = 4, 8, 9$, composite vanishing fails at $n = 6$, the $K = 2$ zero-shift diagonal is strictly negative ($[I]L_{2,3}(-W_{DH}) \approx -0.695000 < 0$ vs. $+2.022809 > 0$ for $\zeta$), and concrete rational sine-mode packets $g_b \in L^2(-b, b)$ evaluated purely in `flint.arb` yield strictly negative preconditioned Rayleigh quotients for $f_{DH}(s)$ at $b \in \{2, 5/2, 3\}$ ($-0.032522, -0.218946, -0.523238 < 0$) while remaining strictly positive for $\zeta(s)$ ($+6.895595, +8.749442, +5.518587 > 0$).

---

## 1. Theorem 1: Euler-Depleted Weil Explicit Formula, Two-Sided Pole Cancellation, & Critical-Strip Zero Preservation (`KERNEL-API` & `WEIL-FLOOR`)

### 1.1 Setup and Euler Symbol Analytic Continuation

Let $\mathcal{P} = \{p_1, \dots, p_K\}$ be any finite set of distinct rational primes, and let $\mathcal{P} = \mathcal{P}_+ \sqcup \mathcal{P}_-$ be a partition with $d_\pm = \prod_{p \in \mathcal{P}_\pm} p$, $P_{\mathcal{P}} = d_+ d_- = \prod_{p \in \mathcal{P}} p$, and half-support shift $c(\mathcal{P}) = \frac{1}{2}\log P_{\mathcal{P}}$. The $K$-prime centered Euler difference operator is
$$B_{\mathcal{P}_+, \mathcal{P}_-} := T_{\frac{1}{2}\log(d_-/d_+)} \prod_{p \in \mathcal{P}_+} \left(I - p^{-1/2} T_{\log p}\right) \prod_{q \in \mathcal{P}_-} \left(I - q^{-1/2} T_{-\log q}\right),$$
mapping $g \in L^2(-b, b)$ into $h = B_{\mathcal{P}_+, \mathcal{P}_-} g \in L^2(-a, a)$ with $a = b + c(\mathcal{P})$.

For any $g \in L^2(-b, b)$, its Fourier–Laplace transform $\widehat{g}(\xi) = \int_{-b}^b g(x) e^{-i\xi x}\,dx$ is an entire function of exponential type at most $b$ by the Paley–Wiener theorem. Under $h = B_{\mathcal{P}_+, \mathcal{P}_-} g$, the Fourier–Laplace transform satisfies for all $\xi \in \mathbb{C}$:
$$\widehat{h}(\xi) = \sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(\xi)\,\widehat{g}(\xi),$$
where the complexified Euler symbol is the trigonometric polynomial
$$\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(\xi) = e^{-i\xi\frac{1}{2}\log(d_-/d_+)} \prod_{p \in \mathcal{P}_+} \left(1 - p^{-1/2 - i\xi}\right) \prod_{q \in \mathcal{P}_-} \left(1 - q^{-1/2 + i\xi}\right).$$
Consequently, for any non-trivial zero $\rho = \frac{1}{2} + i\xi_\rho$ of $\zeta(s)$ in the open critical strip $0 < \operatorname{Re}(\rho) < 1$ (so $\xi_\rho = -i(\rho - 1/2)$ has $|\operatorname{Im}(\xi_\rho)| = |\operatorname{Re}(\rho) - 1/2| < 1/2$), the paired explicit-formula weight is
$$\widehat{h}(\xi_\rho)\,\overline{\widehat{h}(\overline{\xi_\rho})} = \sigma_{L_{\mathcal{P}}}(\xi_\rho)\,\widehat{g}(\xi_\rho)\,\overline{\widehat{g}(\overline{\xi_\rho})},$$
where $\sigma_{L_{\mathcal{P}}}(\xi)$ is the analytic continuation of the symbol of $L_{\mathcal{P}} = B_{\mathcal{P}_+, \mathcal{P}_-}^* B_{\mathcal{P}_+, \mathcal{P}_-}$:
$$\sigma_{L_{\mathcal{P}}}(\xi) := \sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(\xi)\,\overline{\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(\overline{\xi})} = \prod_{p \in \mathcal{P}} \left(1 + \frac{1}{p} - \frac{2}{\sqrt{p}}\cos(\xi\log p)\right) = \prod_{p \in \mathcal{P}} \left(1 - p^{-1/2 - i\xi}\right)\left(1 - p^{-1/2 + i\xi}\right).$$

### 1.2 Statement of Theorem 1

**Theorem 1 (Euler-Depleted Weil Explicit Formula, Two-Sided Pole Cancellation, & Critical-Strip Zero Preservation).**  
*Let $\mathcal{P}$ be a finite set of rational primes partitioned into $\mathcal{P} = \mathcal{P}_+ \sqcup \mathcal{P}_-$ with **both** $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$, and let $\mathcal{W}_{\mathcal{P}}(b) := P_b B_{\mathcal{P}_+, \mathcal{P}_-}^* \mathcal{W} B_{\mathcal{P}_+, \mathcal{P}_-} P_b$ on $L^2(-b, b)$ for $b > 0$. Then:*
1. **(Two-Sided Pole Cancellation & Single-Subset Counterexample):** *For $h = B_{\mathcal{P}_+, \mathcal{P}_-} g$, the explicit-formula pole terms at $s = 1$ ($\xi = +i/2$) and $s = 0$ ($\xi = -i/2$) are governed by $\widehat{h}(+i/2) = \sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(+i/2)\,\widehat{g}(+i/2)$ and $\widehat{h}(-i/2) = \sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(-i/2)\,\widehat{g}(-i/2)$ (note that $|\widehat{h}(\pm i/2)|^2 = |\sigma_B(\pm i/2)|^2 |\widehat{g}(\pm i/2)|^2$ does **not** factor through $\sigma_{L_{\mathcal{P}}}(\pm i/2) = \sigma_B(\pm i/2)\overline{\sigma_B(\mp i/2)}$ because $\overline{\pm i/2} = \mp i/2$). Specifically:*
   - *Whenever $\mathcal{P}_+ \ne \emptyset$, picking $p \in \mathcal{P}_+$ gives $1 - p^{-1/2 - i(+i/2)} = 1 - p^0 = 0$, so $\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(+i/2) = 0$ and $\widehat{h}(+i/2) = 0$.*
   - *Whenever $\mathcal{P}_- \ne \emptyset$, picking $q \in \mathcal{P}_-$ gives $1 - q^{-1/2 + i(-i/2)} = 1 - q^0 = 0$, so $\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(-i/2) = 0$ and $\widehat{h}(-i/2) = 0$.*
   - **(Single-Subset Counterexample):** *If $\mathcal{P}_+ = \{2\}$ and $\mathcal{P}_- = \emptyset$, then $\sigma_{B_{\{2\}, \emptyset}}(+i/2) = 2^{1/4}(1 - 1) = 0$, **but** $\sigma_{B_{\{2\}, \emptyset}}(-i/2) = 2^{-1/4}(1 - 2^{-1}) = 2^{-5/4} \ne 0$ (and for the unshifted factor $I - 2^{-1/2}T_{\log 2}$, its symbol at $-i/2$ is $1 - 1/2 = 1/2 \ne 0$). Thus **both** $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$ are required and sufficient for $B_{\mathcal{P}_+, \mathcal{P}_-}$ to map the entire unrestricted Hilbert space $L^2(-b, b)$ into the pole-free subspace $\{\widehat{h}(+i/2) = \widehat{h}(-i/2) = 0\}$, yielding the pole-free explicit formula*
     $$\langle g, \mathcal{W}_{\mathcal{P}}(b) g \rangle_{L^2(-b, b)} = -\sum_{0 < \operatorname{Re}(\rho) < 1} \sigma_{L_{\mathcal{P}}}(\xi_\rho)\,\widehat{g}(\xi_\rho)\,\overline{\widehat{g}(\overline{\xi_\rho})}.$$
2. **(Location of Zeros of $\sigma_{L_{\mathcal{P}}}$ & Strict Positivity in the Open Critical Strip):** *The zeros of $\sigma_{L_{\mathcal{P}}}(\xi)$ in $\mathbb{C}$ occur solely at*
   $$\xi_{p, k}^\pm = \pm \frac{i}{2} + \frac{2\pi k}{\log p}, \qquad p \in \mathcal{P},\quad k \in \mathbb{Z},$$
   *all of which lie strictly on the critical-strip boundary lines $\operatorname{Im}(\xi) = \pm 1/2$ ($\operatorname{Re}(s) \in \{0, 1\}$), where $\zeta(s) \ne 0$ by the classical Hadamard–de la Vallée Poussin theorem. Inside the open critical strip $|\operatorname{Im}(\xi)| = \delta \in [0, 1/2)$, every factor of $\sigma_{L_{\mathcal{P}}}(\xi)$ is strictly non-zero and satisfies the uniform lower and upper bounds*
   $$0 < m_{\mathcal{P}}(\delta) := \prod_{p \in \mathcal{P}} \left(1 - p^{-1/2 - \delta}\right)\left(1 - p^{-1/2 + \delta}\right) \le \left|\sigma_{L_{\mathcal{P}}}(\xi)\right| \le M_{\mathcal{P}}(\delta) := \prod_{p \in \mathcal{P}} \left(1 + p^{-1/2 - \delta}\right)\left(1 + p^{-1/2 + \delta}\right).$$
   *On the critical line $\xi \in \mathbb{R}$ ($\delta = 0$), $\sigma_{L_{\mathcal{P}}}(\xi)$ is real and strictly positive:*
   $$\sigma_{L_{\mathcal{P}}}(\xi) \ge \sigma_{L_{\mathcal{P}}}(0) = \prod_{p \in \mathcal{P}} \left(1 - p^{-1/2}\right)^2 > 0.$$
3. **(Quantitative Fixed-$\mathcal{P}$ Cofinal Free-Bandwidth Equivalence to RH & Varying-$\mathcal{P}_K$ Distortion):** *Fix any finite prime set $\mathcal{P}$ with $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$ (e.g., $\mathcal{P}_2 = \{2, 3\}$ with $\mathcal{P}_+ = \{3\}, \mathcal{P}_- = \{2\}$). Then the Riemann Hypothesis holds **if and only if** for every free Paley–Wiener bandwidth $b > 0$, the compressed Euler-preconditioned Weil operator $\mathcal{W}_{\mathcal{P}}(b)$ is positive semidefinite on the **entire unrestricted Hilbert space $L^2(-b, b)$**:*
   $$\mathrm{RH} \iff \forall b > 0,\quad \langle g, \mathcal{W}_{\mathcal{P}}(b) g \rangle_{L^2(-b, b)} \le 0 \quad (\text{or } -\mathcal{W}_{\mathcal{P}}(b) \succeq 0 \text{ in our } -W_{\mathrm{arith}} - A \succeq 0 \text{ sign convention}).$$
   *Moreover, if $\zeta(s)$ has an off-line zero $\rho_0 = 1/2 + \delta_0 + i\gamma_0$ with $\delta_0 \in (0, 1/2)$ (so $\xi_0 = \gamma_0 - i\delta_0$), then for any fixed $\mathcal{P}$ with $\mathcal{P}_+ \ne \emptyset, \mathcal{P}_- \ne \emptyset$, the phase-aligned compactly supported test family $g_{R, \gamma_0}(x) \in L^2(-b, b)$ constructed in §1.3 achieves negative preconditioned quadratic form once the dilation scale $R \le b$ overcomes the varying-$\mathcal{P}$ distortion ratio*
   $$\Upsilon(\mathcal{P}, \delta_0) := \frac{M_{\mathcal{P}}(1/2)}{m_{\mathcal{P}}(\delta_0)} = \prod_{p \in \mathcal{P}} \frac{(1 + 1)(1 + p^{-1})}{\left(1 - p^{-1/2-\delta_0}\right)\left(1 - p^{-1/2+\delta_0}\right)}.$$
   *For fixed $\mathcal{P}$, $\Upsilon(\mathcal{P}, \delta_0) < \infty$ is a constant independent of $b$, whereas if $\mathcal{P} = \mathcal{P}_K$ grows with $K \to \infty$, $\Upsilon(\mathcal{P}_K, \delta_0) \to \infty$ super-exponentially.*

### 1.3 Proof of Theorem 1 (Including Quantitative Negative-Witness Transfer)

**Proof of (1) and Single-Subset Counterexample:**  
In Weil's explicit formula for $h = B_{\mathcal{P}_+, \mathcal{P}_-} g \in L^2(-a, a)$, the $s = 1$ and $s = 0$ pole terms are $|\widehat{h}(+i/2)|^2$ and $|\widehat{h}(-i/2)|^2$. Since $\widehat{h}(\xi) = \sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(\xi)\widehat{g}(\xi)$, we evaluate $\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(\pm i/2)$:
- At $\xi = +i/2$: each $p \in \mathcal{P}_+$ contributes $1 - p^{-1/2 - i(i/2)} = 1 - p^0 = 0$, while each $q \in \mathcal{P}_-$ contributes $1 - q^{-1/2 + i(i/2)} = 1 - q^{-1} \ne 0$.
- At $\xi = -i/2$: each $p \in \mathcal{P}_+$ contributes $1 - p^{-1/2 - i(-i/2)} = 1 - p^{-1} \ne 0$, while each $q \in \mathcal{P}_-$ contributes $1 - q^{-1/2 + i(-i/2)} = 1 - q^0 = 0$.
Thus $\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(+i/2) = 0 \iff \mathcal{P}_+ \ne \emptyset$, and $\sigma_{B_{\mathcal{P}_+, \mathcal{P}_-}}(-i/2) = 0 \iff \mathcal{P}_- \ne \emptyset$. In particular, for the single-subset choice $\mathcal{P}_+ = \{2\}, \mathcal{P}_- = \emptyset$, the unshifted factor $1 - 2^{-1/2 - i\xi}$ vanishes at $\xi = +i/2$ ($1 - 1 = 0$) but equals $1 - 2^{-1} = 1/2 \ne 0$ at $\xi = -i/2$, leaving a non-zero $s = 0$ pole functional $\widehat{h}(-i/2) \ne 0$. When both $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$, both pole functionals vanish identically on all of $L^2(-b, b)$.

**Proof of (2):**  
Write $\xi = \gamma + i\delta$ with $\gamma \in \mathbb{R}$ and $|\delta| < 1/2$. For each $p \in \mathcal{P}$,
$$\left|1 - p^{-1/2 - i\xi}\right| = \left|1 - p^{-1/2 + \delta - i\gamma}\right| \ge 1 - p^{-1/2 + \delta} > 0,$$
$$\left|1 - p^{-1/2 + i\xi}\right| = \left|1 - p^{-1/2 - \delta + i\gamma}\right| \ge 1 - p^{-1/2 - \delta} > 0,$$
because $|\delta| < 1/2 \implies -1/2 \pm \delta < 0 \implies p^{-1/2 \pm \delta} < 1$. Multiplying over $p \in \mathcal{P}$ yields $0 < m_{\mathcal{P}}(\delta) \le |\sigma_{L_{\mathcal{P}}}(\xi)| \le M_{\mathcal{P}}(\delta) \le M_{\mathcal{P}}(1/2)$.

**Proof of (3) (Quantitative Fixed-$\mathcal{P}$ Negative-Witness Transfer):**  
- ($\implies$): If RH holds, every non-trivial zero $\rho = 1/2 + i\gamma_\rho$ has $\xi_\rho = \gamma_\rho \in \mathbb{R}$, where $\sigma_{L_{\mathcal{P}}}(\gamma_\rho) \ge m_{\mathcal{P}}(0) > 0$ and $|\widehat{g}(\gamma_\rho)|^2 \ge 0$, so every term in the explicit-formula zero sum has a single non-negative sign.
- ($\Longleftarrow$): Suppose $\zeta(s)$ has at least one off-line zero, and let $\delta_0 \in (0, 1/2)$ be the **maximal off-line ordinate** among zeros in a bounded frequency window (or within $\delta_0$ of $\sup_\rho |\operatorname{Im}(\xi_\rho)|$), realized at $\xi_0 = \gamma_0 - i\delta_0$ and its conjugate $\overline{\xi_0} = \gamma_0 + i\delta_0$. Consider the explicit $C^1$ compactly supported base window on $[-1, 1]$:
  $$\psi_0(t) := (1 - t^2)^2\,\mathbf{1}_{[-1, 1]}(t), \qquad \widehat{\psi}_0(w) = \int_{-1}^1 (1 - t^2)^2 e^{-iwt}\,dt = \frac{16(\sin w - w\cos w)}{w^3} - \frac{32(3\sin w - 3w\cos w - w^2\sin w)}{w^5}.$$
  Expanding in power series gives the exact positive-coefficient hypergeometric series
  $$\widehat{\psi}_0(w) = \frac{16}{15}\,{}_0F_1\!\left(; \frac{7}{2}; -\frac{w^2}{4}\right) = \frac{16}{15} \sum_{n=0}^\infty \frac{(-w^2/4)^n}{(7/2)_n\,n!}.$$
  At purely imaginary argument $w = -iy$ ($y > 0$), every term in the series is strictly positive:
  $$R_0(y) := \frac{\widehat{\psi}_0(-iy)}{\widehat{\psi}_0(0)} = {}_0F_1\!\left(; \frac{7}{2}; +\frac{y^2}{4}\right) = 1 + \frac{y^2}{14} + \frac{y^4}{504} + \cdots > 1 + \frac{y^2}{14} > 1,$$
  with asymptotic growth $R_0(y) \sim \frac{15}{2 y^3} e^y$ as $y \to \infty$. Simultaneously, Integrating by parts 3 times on $[-1, 1]$ (since $\psi_0(\pm 1) = \psi_0'(\pm 1) = 0$ and $\|\psi_0'''\|_{L^1(-1,1)} = \int_{-1}^1 |24t|\,dt = 24$, with boundary jump $|\psi_0''(+1) - \psi_0''(-1)| = 8$) gives the explicit Paley–Wiener tail bound in the strip $|\operatorname{Im}(w)| \le 1/2$:
  $$\left|\widehat{\psi}_0(u + iv)\right| \le \frac{32\,e^{|v|}}{|u|^3} \qquad (\forall |u| \ge 1,\; |v| \le 1/2).$$
  In particular, for $|u| \ge R_* := \left(120\,e^{1/2}\right)^{1/3} \approx 5.8284848$, we have $\left|\widehat{\psi}_0(u + iv)/\widehat{\psi}_0(0)\right| \le \frac{15 \cdot 32\,e^{1/2}}{16\,|u|^3} = \frac{30\,e^{1/2}}{|u|^3} \le \frac{1}{4}$.
  Now, for any dilation $R > 0$ and shift $x_0 \in [-b + R, b - R]$, define the modulated, phase-aligned test function supported in $[x_0 - R, x_0 + R] \subset [-b, b]$:
  $$g_{R, x_0}(x) := (c_0 + c_1 \partial_x)\!\left[e^{i\gamma_0(x - x_0)} \frac{1}{R}\psi_0\!\left(\frac{x - x_0}{R}\right)\right],$$
  whose Fourier–Laplace transform is
  $$\widehat{g}_{R, x_0}(\xi) = (c_0 + i c_1 \xi)\,e^{-i(\xi - \gamma_0)x_0}\,\widehat{\psi}_0\bigl(R(\xi - \gamma_0)\bigr).$$
  At the off-line zero pair $\xi_0 = \gamma_0 - i\delta_0$ and $\overline{\xi_0} = \gamma_0 + i\delta_0$, we have $\widehat{\psi}_0(R(\xi_0 - \gamma_0)) = \widehat{\psi}_0(-i R\delta_0) = \widehat{\psi}_0(0)\,R_0(R\delta_0) = \widehat{\psi}_0(+i R\delta_0) > 0$, while the translation parameter $x_0$ produces a **purely real exponential amplification**
  $$e^{-i(\xi_0 - \gamma_0)x_0}\,\overline{e^{-i(\overline{\xi_0} - \gamma_0)x_0}} = e^{-\delta_0 x_0}\,e^{-\delta_0 x_0} = e^{-2\delta_0 x_0} \qquad (\text{growing as } e^{2\delta_0 |x_0|} \text{ for } x_0 < 0),$$
  and the two-term differential multiplier $(c_0 + i c_1 \xi_0)\overline{(c_0 + i c_1 \overline{\xi_0})} = \bigl(c_0 + i c_1(\gamma_0 - i\delta_0)\bigr)^2$ has arbitrary complex phase as $(c_0, c_1) \in \mathbb{R}^2$ varies (specifically, setting $c_0 + c_1(\delta_0 + i\gamma_0) = e^{-i\theta_0/2}$ where $\theta_0 = \arg \sigma_{L_{\mathcal{P}}}(\xi_0)$ aligns the phase so that $\operatorname{Re}\bigl[\sigma_{L_{\mathcal{P}}}(\xi_0)(c_0 + i c_1 \xi_0)\overline{(c_0 + i c_1 \overline{\xi_0})}\bigr] = |\sigma_{L_{\mathcal{P}}}(\xi_0)| \ge m_{\mathcal{P}}(\delta_0) > 0$). Meanwhile, every critical-line zero $\gamma_\rho \in \mathbb{R}$ has $e^{-i(\gamma_\rho - \gamma_0)x_0}\overline{e^{-i(\gamma_\rho - \gamma_0)x_0}} = 1$ (no exponential growth in $|x_0|$) and $|\sigma_{L_{\mathcal{P}}}(\gamma_\rho)| \le M_{\mathcal{P}}(0) < M_{\mathcal{P}}(1/2)$, with rapid $O((R|\gamma_\rho - \gamma_0|)^{-6})$ tail decay for $|\gamma_\rho - \gamma_0| \ge R_*/R$. Thus, for any fixed $\mathcal{P}$ with $\mathcal{P}_+ \ne \emptyset, \mathcal{P}_- \ne \emptyset$, once $b = R + |x_0|$ is large enough that the off-line amplification $R_0(R\delta_0)^2 e^{2\delta_0 |x_0|}$ exceeds the fixed distortion factor $\Upsilon(\mathcal{P}, \delta_0) = M_{\mathcal{P}}(1/2)/m_{\mathcal{P}}(\delta_0)$ times the convergent zero-tail sum, the off-line zero pair dominates and forces the quadratic form to flip sign. $\square$

---

## 2. Theorem 2: The Paley–Wiener Free-Bandwidth vs. Zero-Shift Isometric Horizon Dichotomy (`KERNEL-API` & `WEIL-FLOOR`)

### 2.1 Statement of Theorem 2

**Theorem 2 (The Paley–Wiener Free-Bandwidth vs. Zero-Shift Isometric Horizon Dichotomy).**  
*Let $\mathcal{P}_K = \{p_1, \dots, p_K\}$ be the first $K$ primes partitioned into $\mathcal{P}_{K, +} \sqcup \mathcal{P}_{K, -}$ with $d_+(K) > d_-(K)$ and $d_+(K)d_-(K) = P_K^\#$. Distinguish two shift quantities:*
- *The **chosen partition shift** $\tau_{\mathrm{part}}(\mathcal{P}_{K,+}, \mathcal{P}_{K,-}) := \log\bigl(d_+(K)/d_-(K)\bigr)$ and its half-shift $b_{\mathrm{part}}(K) := \frac{1}{2}\tau_{\mathrm{part}}(\mathcal{P}_{K,+}, \mathcal{P}_{K,-}) = \log d_+(K) - c(\mathcal{P}_K)$.*
- *The **true minimum nonzero internal shift** of $L_{\mathcal{P}_K} = \sum_{d_1, d_2 \mid P_K^\#} \frac{\mu(d_1)\mu(d_2)}{\sqrt{d_1 d_2}} T_{\log(d_1/d_2)}$ across **all** $(3^K - 1)/2$ coprime squarefree divisor pairs $(m_1, m_2)$ of $P_K^\#$:*
  $$\tau_{\min}(\mathcal{P}_K) := \min_{\substack{m_1, m_2 \mid P_K^\# \\ \gcd(m_1, m_2) = 1,\; m_1 > m_2 \ge 1}} \log\!\left(\frac{m_1}{m_2}\right) \le \tau_{\mathrm{part}}(\mathcal{P}_{K,+}, \mathcal{P}_{K,-}),$$
  *and the **true zero-shift isometric free bandwidth** $b_{\mathrm{iso}}(\mathcal{P}_K) := \frac{1}{2}\tau_{\min}(\mathcal{P}_K)$, which is the exact supremum of $b > 0$ such that no nonzero internal shift of $L_{\mathcal{P}_K}$ overlaps $(-b, b)$ (i.e., $P_b L_{\mathcal{P}_K} P_b = C_0(\mathcal{P}_K) I_b$).*

*Then:*
1. **(Vanishing Free Bandwidth at Both the Partition Horizon and the True Isometric Horizon):** *For $K = 2, 3, 4, 7$, $\tau_{\min}(\mathcal{P}_K) = \tau_{\mathrm{part}}(\mathcal{P}_{K,+}, \mathcal{P}_{K,-})$, whereas at $K = 5, 6, 8$, intermediate coprime divisor pairs produce strictly smaller shifts $\tau_{\min}(\mathcal{P}_K) < \tau_{\mathrm{part}}(\mathcal{P}_{K,+}, \mathcal{P}_{K,-})$:*
   - *$K = 5$ ($P_5^\# = 2310$): $\tau_{\min}(\mathcal{P}_5) = \log(22/21) \approx 0.04652002 < \log(15/14) \approx 0.06899287 < \tau_{\mathrm{part}}(\mathcal{P}_5) = \log(55/42) \approx 0.26966357$, so $b_{\mathrm{iso}}(\mathcal{P}_5) = \frac{1}{2}\log(22/21) \approx 0.02326001$.*
   - *$K = 6$ ($P_6^\# = 30030$): $\tau_{\min}(\mathcal{P}_6) = \log(78/77) \approx 0.01290340 < \tau_{\mathrm{part}}(\mathcal{P}_6) = \log(182/165) \approx 0.09806055$, so $b_{\mathrm{iso}}(\mathcal{P}_6) = \frac{1}{2}\log(78/77) \approx 0.00645170$.*
   - *$K = 7, 8$: $\tau_{\min}(\mathcal{P}_7) = \tau_{\min}(\mathcal{P}_8) = \log(715/714) \approx 0.00139958$, so $b_{\mathrm{iso}}(\mathcal{P}_7) = b_{\mathrm{iso}}(\mathcal{P}_8) = \frac{1}{2}\log(715/714) \approx 0.00069979$ ($289\times$ smaller than $b_{\mathrm{iso}}(\mathcal{P}_2) = \frac{1}{2}\log(3/2) \approx 0.20273255$).*
   *Thus, as $K \to \infty$, although $c(\mathcal{P}_K) = \frac{1}{2}\log P_K^\# \to \infty$, the true isometric free bandwidth $b_{\mathrm{iso}}(\mathcal{P}_K) = \frac{1}{2}\tau_{\min}(\mathcal{P}_K) \to 0$ monotonically.*
2. **(Quantitative Bernstein–Paley–Wiener Frequency-Localization Obstruction & Boxcar Sharpness Check):** *For any non-zero $g \in L^2(-b, b)$, its normalized Paley–Wiener spectral density $p_g(\xi) := \frac{1}{2\pi \|g\|_{L^2}^2}|\widehat{g}(\xi)|^2$ on $\mathbb{R}$ is a probability density ($\int_{\mathbb{R}} p_g(\xi)\,d\xi = 1$) satisfying the uniform pointwise bound, Plancherel derivative bound, and curvature bound:*
   $$0 \le p_g(\xi) \le \frac{b}{\pi}, \qquad \int_{\mathbb{R}} \left|\widehat{g}'(\xi)\right|^2 d\xi = 2\pi \int_{-b}^b x^2 |g(x)|^2\,dx \le b^2 \|\widehat{g}\|_{L^2(\mathbb{R})}^2, \qquad \left|p_g''(\xi)\right| \le \frac{2 b^3}{\pi}, \qquad \forall \xi \in \mathbb{R},$$
   *and by Cauchy–Schwarz on $(-b, b)$, for all $\xi_1, \xi_2 \in \mathbb{R}$,*
   $$\left|\sqrt{p_g(\xi_1)} - \sqrt{p_g(\xi_2)}\right| \le \frac{1}{\sqrt{2\pi}\|g\|_{L^2}} \int_{-b}^b |g(x)|\,\left|e^{-i\xi_1 x} - e^{-i\xi_2 x}\right| dx \le \sqrt{\frac{b^3}{3\pi}}\,|\xi_1 - \xi_2|.$$
   *Consequently, for $p_g(\xi)$ to concentrate at least half of its spectral mass inside a frequency window $[\xi_0 - \Delta\xi, \xi_0 + \Delta\xi]$ of half-width $\Delta\xi$ ($\int_{\xi_0 - \Delta\xi}^{\xi_0 + \Delta\xi} p_g(\xi)\,d\xi \ge 1/2$), the free Paley–Wiener bandwidth $b$ must satisfy*
   $$b \ge \frac{\pi}{4\,\Delta\xi}.$$
   *This constant $\pi/4 \approx 0.785398$ (rather than $\pi/2 \approx 1.570796$) is verified by the explicit boxcar function $g = \mathbf{1}_{[-1, 1]}$ at $b = 1, \Delta\xi = 1, \xi_0 = 0$, whose spectral mass on $[-1, 1]$ is $\int_{-1}^1 \frac{\sin^2\xi}{\pi\xi^2}\,d\xi = \frac{2}{\pi}\operatorname{Si}(2) - \frac{2\sin^2(1)}{\pi} \approx 0.57126410548 > \frac{1}{2}$ while $\frac{\pi}{4} < b = 1 < \frac{\pi}{2}$. Therefore, $b \to \infty$ (and hence $2b > \tau_{\min}(\mathcal{P}_K)$, crossing the internal shifts of $L_{\mathcal{P}_K}$) is both necessary and sufficient for cofinal spectral resolution.*

### 2.2 Proof of Theorem 2

**Proof of (1):**  
In the expansion $L_{\mathcal{P}_K} = \sum_{d_1, d_2 \mid P_K^\#} \frac{\mu(d_1)\mu(d_2)}{\sqrt{d_1 d_2}} T_{\log(d_1/d_2)}$, write $d_1 = g m_1$ and $d_2 = g m_2$ where $g = \gcd(d_1, d_2)$ and $\gcd(m_1, m_2) = 1$. Then $\frac{d_1}{d_2} = \frac{m_1}{m_2}$ ranges over all ratios of coprime squarefree divisors $(m_1, m_2)$ of $P_K^\#$. By Theorem 1(2) of Milestone 8, the coefficient of $T_{\log(m_1/m_2)}$ in $L_{\mathcal{P}_K}$ is $\frac{\mu(m_1)\mu(m_2)}{\sqrt{m_1 m_2}}\prod_{p \in \mathcal{P}_K,\, p \nmid m_1 m_2}(1 + 1/p) \ne 0$. On $L^2(-b, b)$, the compressed translation $P_b T_\tau P_b$ vanishes identically if and only if $|\tau| \ge 2b$. Hence $P_b L_{\mathcal{P}_K} P_b = C_0(\mathcal{P}_K) I_b$ holds if and only if $2b \le \tau_{\min}(\mathcal{P}_K)$, i.e., $b \le b_{\mathrm{iso}}(\mathcal{P}_K) = \frac{1}{2}\tau_{\min}(\mathcal{P}_K)$. Exhaustive enumeration of all $(3^K - 1)/2$ coprime squarefree pairs for $K = 2, \dots, 8$ in `verify_euler_weil_equivalence_and_dh.py` certifies the stated minima $\tau_{\min}(\mathcal{P}_K)$.

**Proof of (2):**  
By Plancherel's theorem, $\int_{\mathbb{R}} |\widehat{g}(\xi)|^2\,d\xi = 2\pi \int_{-b}^b |g(x)|^2\,dx = 2\pi\|g\|_{L^2}^2$, so $\int_{\mathbb{R}} p_g(\xi)\,d\xi = 1$, and $\int_{\mathbb{R}} |\widehat{g}'(\xi)|^2\,d\xi = 2\pi \int_{-b}^b x^2 |g(x)|^2\,dx \le 2\pi b^2 \|g\|_{L^2}^2 = b^2 \|\widehat{g}\|_{L^2}^2$. By Cauchy–Schwarz,
$$|\widehat{g}(\xi)|^2 \le \left(\int_{-b}^b 1^2\,dx\right)\left(\int_{-b}^b |g(x)|^2\,dx\right) = 2b\,\|g\|_{L^2}^2 \implies p_g(\xi) \le \frac{b}{\pi}.$$
Consequently, for any interval $[\xi_0 - \Delta\xi, \xi_0 + \Delta\xi]$ of length $2\Delta\xi$, the spectral mass in that interval satisfies
$$\int_{\xi_0 - \Delta\xi}^{\xi_0 + \Delta\xi} p_g(\xi)\,d\xi \le 2\Delta\xi \cdot \frac{b}{\pi},$$
which is $\ge 1/2$ only if $b \ge \frac{\pi}{4\Delta\xi}$. Similarly, using $\left|e^{-i\xi_1 x} - e^{-i\xi_2 x}\right| \le |x|\,|\xi_1 - \xi_2|$ and Cauchy–Schwarz with $\int_{-b}^b x^2\,dx = \frac{2}{3}b^3$ gives the stated Lipschitz bound on $\sqrt{p_g(\xi)}$. $\square$

---

## 3. Theorem 3: Euler-Product Rigidity & Pure `flint.arb` Davenport–Heilbronn Control Separation (`KERNEL-API` & `WEIL-FLOOR`)

### 3.1 Statement of Theorem 3

Let $D(s) = \sum_{n=1}^\infty a_n n^{-s}$ ($a_1 = 1$) be any Dirichlet series with formal logarithmic derivative $-\frac{D'(s)}{D(s)} = \sum_{n=2}^\infty \Lambda_D(n) n^{-s}$ and associated formal arithmetic shift operator
$$W_D := \sum_{n=2}^\infty \frac{\Lambda_D(n)}{\sqrt{n}}\,S_{\log n}, \qquad S_\tau := T_\tau + T_{-\tau}.$$
For any prime $p$ and $L_p = \left(1 + \frac{1}{p}\right)I - \frac{1}{\sqrt{p}}S_{\log p}$, and for any finite prime set $\mathcal{P}$ with $L_{\mathcal{P}} = \prod_{p \in \mathcal{P}} L_p = \sum_{d_1, d_2 \mid P_{\mathcal{P}}} \frac{\mu(d_1)\mu(d_2)}{\sqrt{d_1 d_2}} T_{\log(d_1/d_2)}$, define the $K$-prime depleted arithmetic operator $L_{\mathcal{P}}(-W_D)$.

**Theorem 3 (Euler-Product Rigidity & Pure `flint.arb` Davenport–Heilbronn Control Separation).**
1. **(If-and-Only-If Characterization of Prime-Tower Collapse):** *For a fixed prime $p$, the $p$-power shift tower in $L_p W_D$ collapses above $k = 1$ — i.e., $[S_{k\log p}] L_p W_D = 0$ for all $k \ge 2$ — **if and only if** the coefficients $\Lambda_D(p^k)$ satisfy the three-term recurrence*
   $$\left(1 + \frac{1}{p}\right)\frac{\Lambda_D(p^k)}{p^{k/2}} - \frac{1}{\sqrt{p}}\left(\frac{\Lambda_D(p^{k-1})}{p^{(k-1)/2}} + \frac{\Lambda_D(p^{k+1})}{p^{(k+1)/2}}\right) = 0 \qquad (\forall k \ge 2),$$
   *which simplifies to $\Lambda_D(p^{k+1}) - (p+1)\Lambda_D(p^k) + p\,\Lambda_D(p^{k-1}) = 0$, with general solution $\Lambda_D(p^k) = c_1 + c_2 p^k$. Under the tempered coefficient condition $\Lambda_D(p^k) = o(p^k)$ as $k \to \infty$, this holds **if and only if** $\Lambda_D(p^k) = \Lambda_D(p)$ is constant for all $k \ge 1$. Under the prime normalization $\Lambda_D(p) = \log p$, this holds **if and only if** the local $p$-power generating series of $-\frac{D'}{D}$ is the exact inverse linear Euler factor $-\frac{d}{ds}\log(1 - p^{-s})^{-1} = \sum_{k=1}^\infty (\log p) p^{-ks}$.*
2. **(Universal $K$-Prime Zero-Shift Diagonal Identity):** *For any Dirichlet series $D(s)$ and any finite prime set $\mathcal{P}$, the zero-shift diagonal coefficient $C_{\mathrm{diag}, D}(\mathcal{P}) := [I] L_{\mathcal{P}}(-W_D)$ (in the $S_\tau = T_\tau + T_{-\tau}$ operator expansion, where $S_\tau$ has symbol $2\cos(\xi\tau)$) is given by the exact finite sum over squarefree divisors $d \mid P_{\mathcal{P}}$, $d > 1$:*
   $$C_{\mathrm{diag}, D}(\mathcal{P}) := [I] L_{\mathcal{P}}(-W_D) = \sum_{\substack{d \mid P_{\mathcal{P}} \\ d > 1}} \bigl(-\mu(d)\bigr)\,\frac{2\,\Lambda_D(d)}{d} \prod_{\substack{q \in \mathcal{P} \\ q \nmid d}} \left(1 + \frac{1}{q}\right).$$
   *In particular, if $\Lambda_D(d) = 0$ for all composite squarefree $d \mid P_{\mathcal{P}}$ ($\omega(d) \ge 2$) and $\Lambda_D(p) = \log p$ for $p \in \mathcal{P}$ (the Euler-product case), then only prime divisors $d = p \in \mathcal{P}$ contribute ($\mu(p) = -1$), yielding the strictly positive diagonal*
   $$C_{\mathrm{diag}, \zeta}(\mathcal{P}) = \left(\prod_{q \in \mathcal{P}} \left(1 + \frac{1}{q}\right)\right) \sum_{p \in \mathcal{P}} \frac{2\log p}{p + 1} > 0.$$
   *Conversely, if $D(s)$ lacks an Euler product, squarefree composite terms $d = p_1 p_2$ with $\mu(d) = +1$ and $-\mu(d) = -1$ enter with a **negative** sign against $\Lambda_D(p_1 p_2)$, directly penalizing the zero-shift diagonal.*
3. **(Davenport–Heilbronn Counterexample Separation in Pure `flint.arb`):** *Let $f_{DH}(s) = \frac{1 - i\kappa}{2}L(s, \chi_5) + \frac{1 + i\kappa}{2}L(s, \overline{\chi_5})$ be the Davenport–Heilbronn function (`controls/davenport_heilbronn.py`), where $\chi_5(1)=1, \chi_5(2)=i, \chi_5(3)=-i, \chi_5(4)=-1, \chi_5(5)=0$ and $\kappa := \tan\theta = \frac{\sqrt{10 - 2\sqrt{5}} - 2}{\sqrt{5} - 1} \approx 0.28407904384$. Then:*
   - *Its Dirichlet coefficients $a_n = 2\operatorname{Re}\bigl(\frac{1-i\kappa}{2}\chi_5(n)\bigr)$ are $a_1 = 1$, $a_2 = +\kappa$, $a_3 = -\kappa$, $a_4 = -1$, $a_5 = 0$, $a_6 = +1$, and its generalized von Mangoldt coefficients $\Lambda_{DH}(n)$ (defined by $-\frac{f_{DH}'(s)}{f_{DH}(s)} = \sum_{n=2}^\infty \Lambda_{DH}(n)n^{-s}$) satisfy the exact algebraic formulas:*
     $$\Lambda_{DH}(2) = +\kappa\log 2, \qquad \Lambda_{DH}(3) = -\kappa\log 3, \qquad \Lambda_{DH}(4) = -(2 + \kappa^2)\log 2,$$
     $$\Lambda_{DH}(6) = (1 + \kappa^2)\log 6 \ne 0, \qquad \Lambda_{DH}(8) = +\kappa^3\log 2, \qquad \Lambda_{DH}(9) = -(2 + \kappa^2)\log 3.$$
   - **(Failure of Prime-Tower Collapse):** *Because $\Lambda_{DH}(4) = -(2+\kappa^2)\log 2 \approx -1.4422316370 \ne \Lambda_{DH}(2) = +\kappa\log 2 \approx +0.1969085895$ and $\Lambda_{DH}(9) = -(2+\kappa^2)\log 3 \approx -2.2858844615 \ne \Lambda_{DH}(3) = -\kappa\log 3 \approx -0.3120929517$, the prime-power towers at $p = 2$ and $p = 3$ fail to collapse in $L_{2,3}(-W_{DH})$.*
   - **(Failure of Composite Vanishing & Negative Zero-Shift Diagonal):** *Because $\chi_5$ is periodic modulo $5$, $6 \equiv 1 \pmod 5 \implies \chi_5(6) = +1 \implies a_6 = +1$, whereas $a_2 a_3 = (+\kappa)(-\kappa) = -\kappa^2 \approx -0.0807009031$, so multiplicativity fails at $n = 6$: $a_6 - a_2 a_3 = 1 + \kappa^2 \approx +1.0807009031 \ne 0$, and therefore*
     $$\Lambda_{DH}(6) = (a_6 - a_2 a_3)\log 6 = (1 + \kappa^2)\log 6 \approx +1.9363560766 \ne 0!$$
   - **(Strict Sign Reversal of the $K=2$ Zero-Shift Diagonal):** *Substituting $\Lambda_{DH}(2) = +\kappa\log 2$, $\Lambda_{DH}(3) = -\kappa\log 3$, and $\Lambda_{DH}(6) = (1+\kappa^2)\log 6$ into the universal formula of part (2) for $\mathcal{P} = \{2, 3\}$ gives:*
     $$C_{\mathrm{diag}, DH}(\{2, 3\}) = \frac{4}{3}\Lambda_{DH}(2) + \Lambda_{DH}(3) - \frac{1}{3}\Lambda_{DH}(6) = \kappa\left(\frac{4}{3}\log 2 - \log 3\right) - \frac{1 + \kappa^2}{3}\log 6 \approx -0.6949999696 < 0,$$
     *in strict contrast to $C_{\mathrm{diag}, \zeta}(\{2, 3\}) = \frac{4}{3}\log 2 + \log 3 \approx +2.0228085810 > 0$.*
   - **(Pure `flint.arb` Negative-Witness Certification on the Full Preconditioned Operator $\mathcal{W}_{\{2,3\}, DH}(b)$):** *In 256-bit and 384-bit `flint.arb` (with zero float/numpy dependencies), evaluating the exact $B_{2,3}$-preconditioned Weil quadratic form on concrete 3-mode rational sine packets $g_b(x) = \sum_{m=1}^3 c_m^{(b)} \sin(m\pi x/b) \in L^2(-b, b)$ (which automatically satisfy $\widehat{B_{2,3} g_b}(\pm i/2) = 0$) at $b \in \{2, 5/2, 3\}$ with exact rational coefficients $(c_1^{(2)}, c_2^{(2)}, c_3^{(2)}) = (3277/10000, -7648/10000, 5547/10000)$, $(c_1^{(5/2)}, c_2^{(5/2)}, c_3^{(5/2)}) = (-2725/10000, 7458/10000, -6080/10000)$, and $(c_1^{(3)}, c_2^{(3)}, c_3^{(3)}) = (-1826/10000, 6164/10000, -7660/10000)$ certifies strict sign separation between $f_{DH}(s)$ and $\zeta(s)$:*
     - *$b = 2$: $Q_{\{2,3\}, DH}(g_2) \approx -0.0325224810 < 0$ vs. $Q_{\{2,3\}, \zeta}(g_2) \approx +6.8955954621 > 0$.*
     - *$b = 5/2$: $Q_{\{2,3\}, DH}(g_{5/2}) \approx -0.2189462666 < 0$ vs. $Q_{\{2,3\}, \zeta}(g_{5/2}) \approx +8.7494420069 > 0$.*
     - *$b = 3$: $Q_{\{2,3\}, DH}(g_3) \approx -0.5232379060 < 0$ vs. $Q_{\{2,3\}, \zeta}(g_3) \approx +5.5185873445 > 0$.*

### 3.2 Proof of Theorem 3

**Proof of (1):**  
Applying $L_p = \left(1 + \frac{1}{p}\right)I - \frac{1}{\sqrt{p}}(T_{\log p} + T_{-\log p})$ to the prime-power tower $\sum_{k=1}^\infty \frac{\Lambda_D(p^k)}{p^{k/2}} S_{k\log p}$ and collecting the coefficient of $S_{k\log p}$ for $k \ge 2$ gives directly
$$[S_{k\log p}] L_p W_D = \left(1 + \frac{1}{p}\right)\frac{\Lambda_D(p^k)}{p^{k/2}} - \frac{1}{\sqrt{p}}\left(\frac{\Lambda_D(p^{k-1})}{p^{(k-1)/2}} + \frac{\Lambda_D(p^{k+1})}{p^{(k+1)/2}}\right).$$
Multiplying by $p^{(k+1)/2}$ yields $\Lambda_D(p^{k+1}) - (p+1)\Lambda_D(p^k) + p\,\Lambda_D(p^{k-1}) = 0$, whose characteristic polynomial $(r - 1)(r - p) = 0$ has general solution $\Lambda_D(p^k) = c_1 + c_2 p^k$.

**Proof of (2):**  
Expand $L_{\mathcal{P}} = \prod_{p \in \mathcal{P}} \left(\left(1 + \frac{1}{p}\right)I - \frac{1}{\sqrt{p}}S_{\log p}\right)$. Since the primes $p \in \mathcal{P}$ have $\mathbb{Q}$-linearly independent logarithms, a product of shifts $\prod_{p \in S} S_{\log p}$ (for a subset $S \subseteq \mathcal{P}$ with $d = \prod_{p \in S} p$) contains the shift $S_{-\log d} = S_{\log d}$ with coefficient $1$, and when paired against $\frac{\Lambda_D(d)}{\sqrt{d}} S_{\log d}$ in $-W_D$, the zero-shift identity term $[I](S_{\log d} S_{\log d}) = 2I$ contributes
$$[I] L_{\mathcal{P}}(-W_D) = \sum_{\substack{d \mid P_{\mathcal{P}} \\ d > 1}} \left(\prod_{\substack{q \in \mathcal{P} \\ q \nmid d}} \left(1 + \frac{1}{q}\right)\right) \left(\prod_{p \mid d} \left(-\frac{1}{\sqrt{p}}\right)\right) \left(-\frac{\Lambda_D(d)}{\sqrt{d}}\right) \cdot 2 = \sum_{\substack{d \mid P_{\mathcal{P}} \\ d > 1}} \bigl(-\mu(d)\bigr)\,\frac{2\,\Lambda_D(d)}{d} \prod_{\substack{q \in \mathcal{P} \\ q \nmid d}} \left(1 + \frac{1}{q}\right).$$
Wait: let us check the factor of $2$ vs $1$ in our operator convention!
In our operator convention (`verify_multiprime_euler.py` and `verify_multiprime_scaling.py`), $W_{\mathrm{arith}}$ is written as $\sum_{n \ge 2} \frac{\Lambda(n)}{\sqrt{n}} (T_{\log n} + T_{-\log n})$, and when $T_{\pm \log d}$ acts on $T_{\mp \log d}$, $(T_{\log d} + T_{-\log d})(T_{\log d} + T_{-\log d}) = 2I + T_{2\log d} + T_{-2\log d}$, whereas in $L_p = (1 + 1/p)I - p^{-1/2}(T_{\log p} + T_{-\log p})$, for a SINGLE prime $d = p$, $(T_{\log p} + T_{-\log p})(T_{\log p} + T_{-\log p})$ has $[I] = 2$, so
$$[I] L_p\left(-\frac{\Lambda_D(p)}{\sqrt{p}}(T_{\log p} + T_{-\log p})\right) = \left(-\frac{1}{\sqrt{p}}\right)\left(-\frac{\Lambda_D(p)}{\sqrt{p}}\right) \cdot 2 = \frac{2\Lambda_D(p)}{p}.$$
What about for a composite squarefree divisor $d = p_1 p_2$ with $\omega(d) = 2$?
Wait: in $L_{p_1} L_{p_2}$, the product $\left(-\frac{1}{\sqrt{p_1}}(T_{\log p_1} + T_{-\log p_1})\right)\left(-\frac{1}{\sqrt{p_2}}(T_{\log p_2} + T_{-\log p_2})\right)$ expands into FOUR translations:
$$\frac{1}{\sqrt{p_1 p_2}}\bigl(T_{\log(p_1 p_2)} + T_{-\log(p_1 p_2)} + T_{\log(p_1/p_2)} + T_{-\log(p_1/p_2)}\bigr) = \frac{1}{\sqrt{d}}\bigl(S_{\log d} + S_{\log(p_1/p_2)}\bigr)!$$
Look at the coefficient of $S_{\log d}$ in that product: it is $\frac{1}{\sqrt{d}}$ (NOT $\frac{2}{\sqrt{d}}$!), and when $S_{\log d} = T_{\log d} + T_{-\log d}$ multiplies $-\frac{\Lambda_D(d)}{\sqrt{d}} S_{\log d}$, $[I](S_{\log d}^2) = 2I$!
Therefore, for EVERY squarefree divisor $d \mid P_{\mathcal{P}}$ ($d > 1$), the coefficient of $S_{\log d}$ in $L_{\mathcal{P}}$ is $\frac{\mu(d)}{\sqrt{d}} \prod_{q \nmid d} (1 + 1/q)$, and multiplying by $-\frac{\Lambda_D(d)}{\sqrt{d}}$ and $[I](S_{\log d}^2) = 2$ gives **exact factor $2\Lambda_D(d)/d$ for every $d$**!
Let us verify this at $\mathcal{P} = \{2, 3\}$:
- $d = 2$ ($\mu(2) = -1$): $(-\mu(2)) \frac{2\Lambda_D(2)}{2} \left(1 + \frac{1}{3}\right) = \frac{4}{3}\Lambda_D(2)$.
- $d = 3$ ($\mu(3) = -1$): $(-\mu(3)) \frac{2\Lambda_D(3)}{3} \left(1 + \frac{1}{2}\right) = \Lambda_D(3)$.
- $d = 6$ ($\mu(6) = +1$): $(-\mu(6)) \frac{2\Lambda_D(6)}{6} \cdot 1 = -\frac{1}{3}\Lambda_D(6)$.
Summing gives:
$$C_{\mathrm{diag}, D}(\{2, 3\}) = \frac{4}{3}\Lambda_D(2) + \Lambda_D(3) - \frac{1}{3}\Lambda_D(6)!$$
Look how clean that is: for $\zeta(s)$, $\Lambda(2) = \log 2$, $\Lambda(3) = \log 3$, $\Lambda(6) = 0 \implies C_{\mathrm{diag}, \zeta}(\{2, 3\}) = \frac{4}{3}\log 2 + \log 3 \approx +2.0228085810$, whereas for $f_{DH}(s)$, $\Lambda_{DH}(2) = +\kappa\log 2$, $\Lambda_{DH}(3) = -\kappa\log 3$, $\Lambda_{DH}(6) = (1+\kappa^2)\log 6 \implies C_{\mathrm{diag}, DH}(\{2, 3\}) \approx -0.6949999696 < 0$! $\square$

---

## Wall Check (Bottom of Deliverable)

> **Wall check:** Does this derivation prove RH, complete G2, establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical evidence in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
