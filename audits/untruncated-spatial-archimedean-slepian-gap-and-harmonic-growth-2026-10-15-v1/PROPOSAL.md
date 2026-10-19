# Proposal — Untruncated Spatial Archimedean Formula, Rational Harmonic Legendre Growth, Arbitrary-Bandwidth Positivity up to $2b = 2.50$ ($260$ Shifts), and Slepian Zero-Gap Duality (`WEIL-FLOOR`, `NB-GAIN` / `COEFF`, & `KERNEL-API`)

- **Audit folder**: `audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/`
- **Date**: `2026-10-15`
- **Target lanes**: `WEIL-FLOOR`, `NB-GAIN` / `COEFF`, and `KERNEL-API`

---

## Wall Check & Open-Status Disclosure

- **Does this milestone prove the Riemann Hypothesis (RH)?** **No (`OPEN`).**
- **Does this milestone prove `G2` or the cofinal prime-shift lower bound as $a \to \infty$ ($K \to \infty$, $b \to \infty$, $N_{\mathrm{leg}} \to \infty$)?** **No (`OPEN`).** Theorem 1.2 is a **diagonal growth identity** proving that the untruncated archimedean diagonal grows logarithmically as $\mathcal{J}_{m, m}(0; b) = \mathcal{H}_m - \gamma_E - \log(4\pi b) - \frac{b^2}{12(2m-1)(2m+3)} + O(b^4/m^4) \sim \log\!\left(\frac{m}{\pi b}\right) \to +\infty$ with Legendre degree $m \to \infty$, and Theorem 2 certifies strict positive definiteness of the untruncated 6-mode even and odd Legendre Weil matrices $W_{\mathrm{full}}^{(6, \mathrm{even})}(b) \succ 0$ and $W_{\mathrm{full}}^{(6, \mathrm{odd})}(b) \succ 0$ across free bandwidths $2b \in \{0.50, 1.00, 1.50, 2.00, 2.50\}$ ($e^{2b} \approx 12.18$, up to **260 active shifts** at $N = 365 > 12 P_3$). Growing diagonal entries alone do **not** bound the infinite high-degree block $\mathcal{H}_{> N}$ from below without an infinite-dimensional tail operator lower bound and off-diagonal block coupling control (established for the five discrete rational bandwidths $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$ in Milestone 17, while the cofinal $b \to \infty$ lower bound remains **OPEN**).
- **Missing-original evidence disclosure**: Both historical missing-original evidence groups documented in `evidence/MISSING.md` (`src/verify_phase2.py` and `final_weil_check.py`) remain **OPEN**.

---

## 1. Problem Statement: Attacking Wall A ($N_{\mathrm{leg}} \to \infty$) and Wall B ($2b \to \infty$)

Following Milestone 15, two concrete walls separated our finite-rank Legendre certificates from the asymptotic regime required by the Milestone 9 RH equivalence theorem:
1. **Wall A (High-Degree Legendre Diagonal Behavior as $m \to \infty$)**: When the positive high-frequency archimedean multiplier $\alpha(\xi)_+ = \max(0, \operatorname{Re}\psi(\frac{1}{4}+\frac{i\xi}{2}) - \log\pi)$ on $|\xi| > \xi_0 \approx 6.289836$ is discarded (as in the $\Delta_\alpha$ floor construction), the diagonal of the Legendre Weil matrix stays bounded by $C_{\mathrm{diag}}(\mathcal{P}_K)$ as the Legendre degree $m \to \infty$. However, integrating $\alpha(\xi)$ directly in frequency space $\xi \in (-\infty, \infty)$ suffers from slow $O(\xi^{-2}\log\xi)$ Bessel decay and rapid oscillation.
2. **Wall B (Free Bandwidth $2b = \log(N / P_K)$ Beyond $\log 2$)**: Milestones 13–15 restricted the free bandwidth to $2b < \log 2 \approx 0.6931$ ($N < 2 P_K$). To reach the cofinal regime $2b \to \infty$, we must remove the $2b < \log 2$ restriction, evaluate the exact untruncated Weil matrix for $e^{2b} \gg 2$, and compare the finite-mode prime+archimedean Rayleigh quotient against both the continuous Slepian exterior-frequency projection and a conditional 50-zero prefix diagnostic.

---

## 2. Main Theorems & Deliverables

### Theorem 1 (Exact Untruncated Spatial Archimedean Formula & Rational Harmonic / Weber–Schafheitlin Legendre Asymptotics — Attacking Wall A)
1. **Logarithmic Sobolev Form Domain & Exact Untruncated Spatial Archimedean Representation ($\Xi_{\mathrm{cap}} = \infty$)**: On the logarithmic Sobolev form domain $\mathcal{Q}(A_{\mathrm{arch}}) = \{g \in L^2(-b, b) : \int_{\mathbb{R}} \log(2 + |\xi|)|\widehat{g}(\xi)|^2\,d\xi < \infty\}$, for any even Lipschitz correlation function $\Phi(t) = \Phi(-t)$ supported in $[-T, T]$, Fourier inversion of the digamma integral representation yields the exact compact spatial integral
   $$\frac{1}{2\pi} \int_{-\infty}^\infty \widehat{\Phi}(\xi) \alpha(\xi)\,d\xi = \left(\psi\!\left(\frac{1}{4}\right) - \log\pi + \log\!\left(\frac{1 + e^{-T/2}}{1 - e^{-T/2}}\right) + 2\arctan\!\left(e^{-T/2}\right)\right)\Phi(0) + 2 \int_0^T \frac{e^{-t/2}\left(\Phi(0) - \Phi(t)\right)}{1 - e^{-2t}}\,dt,$$
   with **zero high-frequency truncation error** and exact removable-singularity cancellation $1 - e^{-2t} = 2t e^{-t} \operatorname{sinc}(it)$ at $t = 0$.
2. **Exact Rational Frullani–Legendre Harmonic & Weber–Schafheitlin Diagonal Identities**: For every integer $m \ge 0$, the logarithmic singularity integral of the diagonal Legendre shift polynomial $C_{m, m}(u b) = \frac{1}{2}(S_{u b})_{m, m}$ on $u \in [0, 2]$ is an exact rational number given by the harmonic sum
   $$\mathcal{H}_m := \int_0^2 \frac{1 - \frac{1}{2}(S_{u b})_{m, m}}{u}\,du = 1 + \sum_{k=1}^{m} \frac{4k}{4k^2 - 1} = 2 H_{2m} - H_m + \frac{1}{2m+1},$$
   and for every $m \ge 1$, the first spatial moment equals the exact rational Weber–Schafheitlin inverse-square Bessel integral $-\int_0^2 u\,C_{m,m}(ub)\,du = \frac{2}{\pi}(2m+1)\int_0^\infty \frac{j_m(z)^2}{z^2}\,dz = \frac{2}{(2m-1)(2m+3)}$. Consequently, the untruncated archimedean diagonal entry on the $m$-th Legendre mode satisfies
   $$\mathcal{J}_{m, m}(0; b) = \mathcal{H}_m - \gamma_E - \log(4\pi b) - \frac{b^2}{12(2m - 1)(2m + 3)} + O\!\left(\frac{b^4}{m^4}\right) \sim \log\!\left(\frac{m}{\pi b}\right) \to +\infty \qquad (m \to \infty).$$

### Theorem 2 (All-Bandwidth Internal Prime-Tower Telescoping & Multi-Degree Untruncated Weil Positivity up to $2b = 2.50$, $260$ Active Shifts — Attacking Wall B)
1. **All-Bandwidth Internal Prime-Tower Telescoping**: For every internal prime $p \in \mathcal{P}_K$, the prime-power shift series telescopes coefficient-by-coefficient (and as a finite sum on $P_b L^2(-b, b)$ for every $b > 0$):
   $$L_p\!\left(-\sum_{k=1}^\infty \frac{\log p}{p^{k/2}}(S_{k\log p} + S_{-k\log p})\right) = (\log p) L_p - \frac{p-1}{p}(\log p) I,$$
   certified against the direct Dirichlet convolution up to $R_{\max} = e^{2b} = 6$ ($N = 180$ for $K = 3$) with `0` discrepancies across all 151 shifts in $[1, 6)$.
2. **Two-Precision (`256`-bit and `384`-bit) Cholesky Certification up to $2b = 2.50$ ($e^{2b} \approx 12.18$)**: Both the even and odd 6-mode Untruncated Legendre Weil Matrices $W_{\mathrm{full}}^{(6, \mathrm{even})}(b) \succ 0$ and $W_{\mathrm{full}}^{(6, \mathrm{odd})}(b) \succ 0$ (12 total Legendre modes up to $\deg = 11$, plus nested subblocks $N_{\mathrm{leg}} \in \{2, 4, 6\}$) are certified **strictly positive definite** across $2b \in \{0.50, 1.00, 1.50, 2.00, 2.50\}$ for $K = 2$ ($\mathcal{P}_2 = \{2, 3\}$, up to 53 active shifts) and $K = 3$ ($\mathcal{P}_3 = \{2, 3, 5\}$, up to **260 active shifts** at $N = 365 > 12 P_3$).

### Section 3 (Certified Slepian Exterior-Frequency Leakage & Conditional 50-Zero Prefix Spectral Concentration Diagnostic)
By the unconditional Euler-Depleted Weil Explicit Formula, $\langle g, W_{\mathrm{full}}(b) g \rangle = \sum_{\rho} \sigma_{L_{\mathcal{P}_K}}(z_\rho)\widehat{g}(z_\rho)\overline{\widehat{g}(\overline{z_\rho})}$ with $z_\rho = (\rho - 1/2)/i$. In two-precision (`256`-bit and `384`-bit) `flint.arb`, we compute both the continuous Slepian exterior-frequency matrix $E_{\mathrm{Slep}}^{(6, \mathrm{even})}(b; \gamma_1) = I_6 - K_{\mathrm{Slep}}^{(6, \mathrm{even})}(b; \gamma_1)$ on $\mathcal{V}_6^{\mathrm{even}}(-b, b)$ and the conditional 50-zero prefix sum using FLINT's certified interval enclosures `flint.acb.zeta_zero(k).imag` ($k = 1, \dots, 50$), showing that the 50-zero prefix captures `86.52%` ($2b = 1.00$), `94.02%` ($2b = 1.50$), and `91.79%` ($2b = 2.00$) of the prime+archimedean Rayleigh quotient on $v_{\min}$.
