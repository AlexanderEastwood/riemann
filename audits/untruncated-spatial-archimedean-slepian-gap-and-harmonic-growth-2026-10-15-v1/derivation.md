# Derivation — Untruncated Spatial Archimedean Formula, Rational Harmonic & Weber–Schafheitlin Legendre Asymptotics, Arbitrary-Bandwidth Positivity up to $2b = 2.50$ ($260$ Shifts), and Slepian Concentration Diagnostic (`WEIL-FLOOR`, `NB-GAIN` / `COEFF`, & `KERNEL-API`)

## Wall Check & Open-Status Disclosure

- **Does this milestone prove the Riemann Hypothesis (RH)?** **No (`OPEN`).**
- **Does this milestone prove `G2` or the cofinal prime-shift lower bound as $a \to \infty$ ($K \to \infty$, $b \to \infty$, $N_{\mathrm{leg}} \to \infty$)?** **No (`OPEN`).** Theorem 1.2 is a **diagonal growth identity** proving that the untruncated zero-shift archimedean diagonal entries grow logarithmically as $\mathcal{J}_{m, m}(0; b) = \mathcal{H}_m - \gamma_E - \log(4\pi b) - \frac{b^2}{12(2m-1)(2m+3)} + O(b^4/m^4) \sim \log\!\left(\frac{m}{\pi b}\right) \to +\infty$ with Legendre degree $m \to \infty$, and Theorem 2 certifies strict positive definiteness of the untruncated 6-mode even and odd Legendre Weil matrices $W_{\mathrm{full}}^{(6, \mathrm{even})}(b) \succ 0$ and $W_{\mathrm{full}}^{(6, \mathrm{odd})}(b) \succ 0$ across free bandwidths $2b \in \{0.50, 1.00, 1.50, 2.00, 2.50\}$ ($e^{2b} \approx 12.18$, up to **260 active shifts** at $N = 365 > 12 P_3$). Growing diagonal entries alone do **not** bound the infinite high-degree block $\mathcal{H}_{> N}$ from below without an infinite-dimensional tail operator lower bound and off-diagonal block coupling control (established for the five discrete rational bandwidths $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$ in Milestone 17, while the cofinal $b \to \infty$ lower bound remains **OPEN**).
- **Missing-original evidence disclosure**: Both historical missing-original evidence groups documented in `evidence/MISSING.md` (`src/verify_phase2.py` and `final_weil_check.py`) remain **OPEN**.

---

## 1. Theorem 1: Exact Untruncated Spatial Archimedean Formula & Rational Harmonic / Weber–Schafheitlin Legendre Asymptotics (Attacking Wall A)

### 1.1 Logarithmic Sobolev Form Domain & Exact Untruncated Spatial Archimedean Representation ($\Xi_{\mathrm{cap}} = \infty$)

Let $\alpha(\xi) := \operatorname{Re}\psi\!\left(\frac{1}{4} + \frac{i\xi}{2}\right) - \log\pi$. Because $\alpha(\xi) = \log|\xi| - \log(2\pi) + O(\xi^{-2})$ grows logarithmically as $|\xi| \to \infty$, the untruncated archimedean quadratic form on $L^2(-b, b)$ is an unbounded semi-bounded quadratic form with **logarithmic Sobolev form domain**
$$\mathcal{Q}(A_{\mathrm{arch}}) := \left\{g \in L^2(-b, b) : \int_{-\infty}^\infty \log(2 + |\xi|)\,\left|\widehat{g}(\xi)\right|^2 d\xi < \infty\right\}.$$
Every polynomial and Legendre basis mode $e_m(t) = \sqrt{\frac{2m+1}{2b}} P_m(t/b) \in C^\infty[-b, b]$ satisfies $|\widehat{e}_m(\xi)|^2 = 2b(2m+1) j_m(b\xi)^2 \ll (1 + |\xi|)^{-2}$ as $|\xi| \to \infty$, so $e_m \in \mathcal{Q}(A_{\mathrm{arch}})$ and its autocorrelation $\Phi(t) = (e_m * \widetilde{e}_n)(t)$ is Lipschitz and compactly supported in $[-2b, 2b]$.

By Gauss's integral representation of the digamma function for $\operatorname{Re}(z) > 0$,
$$\psi(z) = -\gamma_E + \int_0^\infty \frac{e^{-u} - e^{-zu}}{1 - e^{-u}}\,du.$$
Setting $z = \frac{1}{4} + \frac{i\xi}{2}$ and substituting $u = 2t$ ($du = 2\,dt$) gives
$$\alpha(\xi) = -(\gamma_E + \log\pi) + 2 \int_0^\infty \frac{e^{-2t} - e^{-t/2}\cos(\xi t)}{1 - e^{-2t}}\,dt.$$
Specializing to $\xi = 0$ gives the identity $2 \int_0^\infty \frac{e^{-2t} - e^{-t/2}}{1 - e^{-2t}}\,dt = \psi(1/4) + \gamma_E$, so subtracting the $\xi = 0$ integrand yields the subtraction-regularized representation
$$\alpha(\xi) = \left(\psi\!\left(\frac{1}{4}\right) - \log\pi\right) + 2 \int_0^\infty \frac{e^{-t/2}\left(1 - \cos(\xi t)\right)}{1 - e^{-2t}}\,dt.$$

**Proposition 1.1 (Exact Compact Spatial Archimedean Integral).**
*Let $\Phi(t) = \Phi(-t)$ be an even Lipschitz correlation function supported in $[-T, T]$ ($T > 0$) with $\int_{-\infty}^\infty \log(2 + |\xi|)\,|\widehat{\Phi}(\xi)|\,d\xi < \infty$ and Fourier transform $\widehat{\Phi}(\xi) = 2 \int_0^T \Phi(t)\cos(\xi t)\,dt$. Then the untruncated frequency integral over $\xi \in (-\infty, \infty)$ equals the compact spatial integral on $[0, T]$:*
$$\frac{1}{2\pi} \int_{-\infty}^\infty \widehat{\Phi}(\xi) \alpha(\xi)\,d\xi = \left(\psi\!\left(\frac{1}{4}\right) - \log\pi + \log\!\left(\frac{1 + e^{-T/2}}{1 - e^{-T/2}}\right) + 2\arctan\!\left(e^{-T/2}\right)\right)\Phi(0) + 2 \int_0^T \frac{e^{-t/2}\left(\Phi(0) - \Phi(t)\right)}{1 - e^{-2t}}\,dt.$$

*Proof.* By Fourier inversion, $\frac{1}{2\pi}\int_{-\infty}^\infty \widehat{\Phi}(\xi)\,d\xi = \Phi(0)$ and $\frac{1}{2\pi}\int_{-\infty}^\infty \widehat{\Phi}(\xi)\cos(\xi t)\,d\xi = \Phi(t)$. Substituting the subtraction-regularized formula for $\alpha(\xi)$ and applying Fubini's theorem gives
$$\frac{1}{2\pi} \int_{-\infty}^\infty \widehat{\Phi}(\xi) \alpha(\xi)\,d\xi = \left(\psi\!\left(\frac{1}{4}\right) - \log\pi\right)\Phi(0) + 2 \int_0^\infty \frac{e^{-t/2}\left(\Phi(0) - \Phi(t)\right)}{1 - e^{-2t}}\,dt.$$
Since $\Phi(t) = 0$ for all $t \ge T$, the tail integral on $[T, \infty)$ is $2\Phi(0) \int_T^\infty \frac{e^{-t/2}}{1 - e^{-2t}}\,dt$. Substituting $w = e^{-t/2} \in (0, e^{-T/2}]$ ($dw = -\frac{1}{2}e^{-t/2}\,dt$) yields
$$2 \int_T^\infty \frac{e^{-t/2}}{1 - e^{-2t}}\,dt = 4 \int_0^{e^{-T/2}} \frac{dw}{1 - w^4} = \int_0^{e^{-T/2}} \left(\frac{1}{1+w} + \frac{1}{1-w} + \frac{2}{1+w^2}\right)dw = \log\!\left(\frac{1 + e^{-T/2}}{1 - e^{-T/2}}\right) + 2\arctan\!\left(e^{-T/2}\right). \quad \square$$

Furthermore, on $[0, T]$, writing $1 - e^{-2t} = 2t e^{-t} \frac{\sinh t}{t} = 2t e^{-t} \operatorname{sinc}(it)$ removes the removable singularity at $t = 0$: whenever $\Phi(0) - \Phi(t) = t \cdot Q(t)$, the integrand is $\frac{e^{t/2} Q(t)}{\operatorname{sinc}(it)}$, which is entire in a neighborhood of $t = 0$.

---

### 1.2 Exact Rational Frullani–Legendre Harmonic & Weber–Schafheitlin Identities

For the orthonormal Legendre polynomial $e_m(t) = \sqrt{\frac{2m+1}{2b}} P_m(t/b)$ on $L^2(-b, b)$, its autocorrelation on $[0, 2b]$ is
$$C_{m, m}(u b) = \langle e_m, S_{u b} e_m \rangle_{L^2(-b, b)} = \frac{1}{2}\left(S_{u b}\right)_{m, m} = \frac{2m+1}{2} \int_{-1}^{1-u} P_m(x) P_m(x+u)\,dx \qquad (u \in [0, 2]),$$
with $C_{m, m}(0) = 1$.

**Theorem 1.2 (Exact Rational Frullani–Legendre Harmonic & Weber–Schafheitlin Diagonal Identities).**
1. **(Rational Harmonic Singularity Integral):** *For every integer $m \ge 0$, the logarithmic singularity integral of $C_{m, m}(u b)$ on $u \in [0, 2]$ is an exact rational number given by:*
   $$\mathcal{H}_m := \int_0^2 \frac{1 - C_{m, m}(u b)}{u}\,du = 1 + \sum_{k=1}^{m} \frac{4k}{4k^2 - 1} = 1 + \sum_{k=1}^{m} \left(\frac{1}{2k-1} + \frac{1}{2k+1}\right) = 2 H_{2m} - H_m + \frac{1}{2m+1},$$
   *with strictly positive rational increment $\mathcal{H}_m - \mathcal{H}_{m-1} = \frac{4m}{4m^2 - 1} = \frac{1}{2m-1} + \frac{1}{2m+1} > 0$ ($\forall m \ge 1$).*
2. **(Exact Rational Weber–Schafheitlin Inverse-Square Moment):** *For every integer $m \ge 1$, $\int_0^2 C_{m, m}(u b)\,du = 0$, and the first spatial moment equals the exact rational Weber–Schafheitlin inverse-square Bessel integral:*
   $$\mathcal{M}_m^{(-2)} := \frac{2}{\pi}(2m+1) \int_0^\infty \frac{j_m(z)^2}{z^2}\,dz = -\int_0^2 u\,C_{m, m}(u b)\,du = \frac{2}{(2m - 1)(2m + 3)}.$$
3. **(Diagonal Asymptotic Expansion with Exact $\log(4\pi b)$ Constant and $O(b^2/m^2)$ Term):** *For every integer $m \ge 1$, the untruncated zero-shift archimedean diagonal entry $\mathcal{J}_{m, m}(0; b) = \frac{1}{2\pi}\int_{-\infty}^\infty |\widehat{e}_m(\xi)|^2 \alpha(\xi)\,d\xi$ satisfies*
   $$\mathcal{J}_{m, m}(0; b) = \mathcal{H}_m - \gamma_E - \log(4\pi b) - \frac{b^2}{12(2m - 1)(2m + 3)} + O\!\left(\frac{b^4}{m^4}\right) \sim \log\!\left(\frac{m}{\pi b}\right) \to +\infty \qquad (m \to \infty).$$
   *(Note: This is a diagonal growth theorem on $\mathcal{J}_{m,m}(0; b)$; bounding the infinite high-degree tail block $\mathcal{H}_{> N}$ as an operator requires controlling off-diagonal couplings $m \ne n$, which is certified for the five discrete rational bandwidths $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$ in Milestone 17.)*

*Proof.* Since $\widehat{C}_{m, m}(\xi) = |\widehat{e}_m(\xi)|^2 = 2b(2m+1) j_m(b\xi)^2$, the Weber–Schafheitlin integral for $j_m(z)^2 = \frac{\pi}{2z} J_{m+1/2}(z)^2$ gives for $-2m - 1 < \operatorname{Re}(s) < 1$:
$$\frac{2}{\pi} (2m+1) \int_0^\infty j_m(z)^2 z^s\,dz = \frac{2m+1}{2^{1-s}} \frac{\Gamma(1-s)\, \Gamma\!\left(m + \frac{1}{2} + \frac{s}{2}\right)}{\Gamma\!\left(1 - \frac{s}{2}\right)^2 \Gamma\!\left(m + \frac{3}{2} - \frac{s}{2}\right)}.$$
- Evaluating at $s = -2$ for $m \ge 1$ gives $\frac{2m+1}{8} \frac{\Gamma(3)\Gamma(m - 1/2)}{\Gamma(2)^2 \Gamma(m + 5/2)} = \frac{2m+1}{4(m - 1/2)(m + 1/2)(m + 3/2)} = \frac{2}{(2m-1)(2m+3)}$. Since $\int_0^2 C_{m,m}(ub)\,du = \frac{1}{2b}\widehat{C}_{m,m}(0) = 0$ for $m \ge 1$ and $\frac{2}{\pi}\int_0^\infty \frac{1 - \cos(zu)}{z^2}\,dz = u$, Fourier cosine inversion yields $\frac{2}{\pi}(2m+1)\int_0^\infty \frac{j_m(z)^2}{z^2}\,dz = -\int_0^2 u\,C_{m,m}(ub)\,du = \frac{2}{(2m-1)(2m+3)}$, proving (2).
- At $s = 0$, the Weber–Schafheitlin right-hand side equals $1$. Differentiating with respect to $s$ at $s = 0$ yields the logarithmic Bessel moment
  $$\mu_m^{\mathrm{Bessel}} := \frac{2}{\pi}(2m+1) \int_0^\infty j_m(z)^2 \log z\,dz = \log 2 + \frac{1}{2}\left(\psi\!\left(m + \frac{1}{2}\right) + \psi\!\left(m + \frac{3}{2}\right)\right).$$
  Using $\psi(m + \frac{1}{2}) = -\gamma_E - 2\log 2 + \sum_{k=1}^m \frac{2}{2k-1}$ and $\psi(m + \frac{3}{2}) = \psi(m + \frac{1}{2}) + \frac{2}{2m+1}$ gives
  $$\frac{1}{2}\left(\psi\!\left(m + \frac{1}{2}\right) + \psi\!\left(m + \frac{3}{2}\right)\right) = -\gamma_E - 2\log 2 + 1 + \sum_{k=1}^m \left(\frac{1}{2k-1} + \frac{1}{2k+1}\right) = -\gamma_E - 2\log 2 + \mathcal{H}_m,$$
  and adding $+\log 2$ leaves
  $$\mu_m^{\mathrm{Bessel}} = \mathcal{H}_m - \gamma_E - \log 2.$$
- Simultaneously, in Proposition 1.1 with $\Phi(t) = C_{m,m}(t)$ and $T = 2b$, split $\frac{2 e^{-t/2}}{1 - e^{-2t}} = \frac{1}{t} + K_{\mathrm{reg}}(t)$ where $K_{\mathrm{reg}}(t) := \frac{2 e^{-t/2}}{1 - e^{-2t}} - \frac{1}{t} = \frac{1}{2\sinh(t/2)} - \frac{1}{t} + \frac{1}{2\cosh(t/2)} = \frac{1}{2} - \frac{t}{24} - \frac{t^2}{16} + \frac{7 t^3}{5760} + \frac{5 t^4}{768} - \cdots$. Because $\int_0^{2b} K_{\mathrm{reg}}(t)\,dt = \left[-\log\!\left(\frac{1+e^{-t/2}}{1-e^{-t/2}}\right) - 2\arctan(e^{-t/2}) - \log t\right]_0^{2b} = 2\log 2 + \frac{\pi}{2} - \log(2b) - \log\!\left(\frac{1+e^{-b}}{1-e^{-b}}\right) - 2\arctan(e^{-b})$ and $\psi(1/4) = -\gamma_E - \frac{\pi}{2} - 3\log 2$, the constant terms in Proposition 1.1 combine identically to $-\gamma_E - \log(4\pi b)$:
  $$\mathcal{J}_{m, m}(0; b) = \int_0^2 \frac{1 - C_{m, m}(u b)}{u}\,du - \gamma_E - \log(4\pi b) - \int_0^{2b} K_{\mathrm{reg}}(t)\,C_{m, m}(t)\,dt.$$
  On the other hand, in frequency space $\alpha(\xi) = \log(b|\xi|) - \log(2\pi b) + R_\alpha(\xi)$ with $R_\alpha(\xi) = -\frac{1}{24\xi^2} + O(\xi^{-4})$, so $\mathcal{J}_{m,m}(0; b) = \mu_m^{\mathrm{Bessel}} - \log(2\pi b) + O(b^2/m^2) = \mathcal{H}_m - \gamma_E - \log(4\pi b) + O(b^2/m^2)$. Taking $b \to 0^+$ (where $\int_0^{2b} K_{\mathrm{reg}}(t) C_{m,m}(t)\,dt \to 0$) identifies $\int_0^2 \frac{1 - C_{m,m}(ub)}{u}\,du = \mathcal{H}_m$ for every $m \ge 0$, proving (1). Finally, for $m \ge 1$, $\int_0^{2b} C_{m,m}(t)\,dt = 0$ annihilates $K_{\mathrm{reg}}(0) = \frac{1}{2}$, and substituting the linear Taylor term $-\frac{t}{24}$ of $K_{\mathrm{reg}}(t) - K_{\mathrm{reg}}(0)$ with $-\int_0^{2b} t\,C_{m,m}(t)\,dt = \frac{2b^2}{(2m-1)(2m+3)}$ (or equivalently integrating $R_\alpha(\xi) = -\frac{1}{24\xi^2} + O(\xi^{-4})$ against $\mathcal{M}_m^{(-2)} = \frac{2}{(2m-1)(2m+3)}$) yields the exact $-\frac{b^2}{12(2m-1)(2m+3)}$ correction in (3). $\square$

| Legendre Degree $m$ | Exact Rational $\mathcal{H}_m$ | Weber–Schafheitlin $\mathcal{M}_m^{(-2)} = \frac{2}{(2m-1)(2m+3)}$ | $\mathcal{J}_{m,m}(0; b)$ at $2b=0.50$ | $\mathcal{J}_{m,m}(0; b)$ at $2b=1.00$ | $\mathcal{J}_{m,m}(0; b)$ at $2b=2.00$ | Refined Asymptotic Error at $2b=1.00$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $1$ | — | $-0.8446$ | $-1.6532$ | $-2.5455$ | $-2.381 \times 10^{-1}$ |
| $1$ | $7/3$ | $2/5$ | $+0.6097$ | $-0.0908$ | $-0.8238$ | $-4.826 \times 10^{-3}$ |
| $2$ | $43/15$ | $2/21$ | $+1.1445$ | $+0.4505$ | $-0.2481$ | $-1.116 \times 10^{-4}$ |
| $3$ | $337/105$ | $2/45$ | $+1.4875$ | $+0.7940$ | $+0.0992$ | $-3.930 \times 10^{-6}$ |
| $4$ | $1091/315$ | $2/77$ | $+1.7415$ | $+1.0481$ | $+0.3541$ | $-5.955 \times 10^{-7}$ |
| $5$ | $12701/3465$ | $2/117$ | $+1.9435$ | $+1.2502$ | $+0.5566$ | $-2.247 \times 10^{-7}$ |
| $6$ | $172673/45045$ | $2/165$ | $+2.1114$ | $+1.4181$ | $+0.7246$ | $-1.087 \times 10^{-7}$ |
| $7$ | $179141/45045$ | $2/221$ | $+2.2550$ | $+1.5617$ | $+0.8683$ | $-5.934 \times 10^{-8}$ |
| $8$ | $3141493/765765$ | $2/285$ | $+2.3805$ | $+1.6873$ | $+0.9939$ | $-3.521 \times 10^{-8}$ |
| $9$ | $61309987/14549535$ | $2/357$ | $+2.4919$ | $+1.7987$ | $+1.1054$ | $\mathbf{-2.223 \times 10^{-8}}$ |

---

## 2. Theorem 2: All-Bandwidth Internal Prime-Tower Telescoping & Multi-Degree Untruncated Weil Positivity up to $2b = 2.50$ ($260$ Active Shifts)

### 2.1 All-Bandwidth Internal Prime-Tower Telescoping Identity

**Proposition 2.1 (All-Bandwidth Internal Prime-Tower Collapse on Compactly Supported Test Functions).**
*For every prime $p$ and $L_p = \frac{p+1}{p} I - \frac{1}{\sqrt{p}}(S_{\log p} + S_{-\log p})$, the prime-power shift series telescopes Coefficient-by-Coefficient (and as a finite sum on $P_b L^2(-b, b)$ for every $b > 0$, since $P_b S_{k\log p} P_b = 0$ for all $k\log p \ge 2b$):*
$$L_p\!\left(-\sum_{k=1}^\infty \frac{\log p}{p^{k/2}} (S_{k\log p} + S_{-k\log p})\right) = (\log p)\,L_p - \frac{p-1}{p}(\log p)\,I.$$

*Proof.* Using $(S_{\log p} + S_{-\log p})(S_{k\log p} + S_{-k\log p}) = (S_{(k+1)\log p} + S_{-(k+1)\log p}) + (S_{(k-1)\log p} + S_{-(k-1)\log p})$ (with $S_0 + S_{-0} = 2I$ at $k = 1$), the coefficient of $S_{k\log p} + S_{-k\log p}$ in $L_p\!\left(I + \sum_{k=1}^\infty p^{-k/2}(S_{k\log p} + S_{-k\log p})\right)$ for every $k \ge 1$ is
$$\frac{p+1}{p} p^{-k/2} - p^{-1/2} p^{-(k-1)/2} - p^{-1/2} p^{-(k+1)/2} = p^{-k/2}\!\left(\frac{p+1}{p} - 1 - \frac{1}{p}\right) = 0,$$
while the zero-shift coefficient is $\frac{p+1}{p} - 2 p^{-1/2} p^{-1/2} = \frac{p-1}{p}$. Multiplying by $\log p$ completes the proof. $\square$

### 2.2 Certified Untruncated Multi-Degree Legendre Weil Positivity up to $2b = 2.50$ ($e^{2b} \approx 12.18$)

Combining Proposition 1.1 (across all shifts $\lambda_r = \log r \ge 0$ of $L_{\mathcal{P}_K}$) with Proposition 2.1 yields the **Untruncated $N_{\mathrm{leg}}$-Mode Legendre Weil Matrix** $W_{\mathrm{full}}^{(N_{\mathrm{leg}}, \mathrm{sector})}(b)$ ($\mathrm{sector} \in \{\mathrm{even}, \mathrm{odd}\}$). In two-precision (`256`-bit and `384`-bit) `flint.arb` ball arithmetic, exact Cholesky factorization certifies $W_{\mathrm{full}}^{(N_{\mathrm{leg}}, \mathrm{even})}(b) \succ 0$ and $W_{\mathrm{full}}^{(N_{\mathrm{leg}}, \mathrm{odd})}(b) \succ 0$ across $N_{\mathrm{leg}} \in \{2, 4, 6\}$ and $2b \in \{0.50, 1.00, 1.50, 2.00, 2.50\}$:

| Family | $2b$ | $e^{2b} = N/P_K$ | Active Shifts | $\lambda_{\min}(W_{\mathrm{full}}^{(2,\mathrm{even})})$ | $\lambda_{\min}(W_{\mathrm{full}}^{(4,\mathrm{even})})$ | $\lambda_{\min}(W_{\mathrm{full}}^{(6,\mathrm{even})})$ | $\lambda_{\min}(W_{\mathrm{full}}^{(2,\mathrm{odd})})$ | $\lambda_{\min}(W_{\mathrm{full}}^{(4,\mathrm{odd})})$ | $\lambda_{\min}(W_{\mathrm{full}}^{(6,\mathrm{odd})})$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $K=2$ | $0.50$ | $1.65$ | $3$ | $+1.446 \times 10^{-1}$ | $+1.442 \times 10^{-1}$ | $+1.432 \times 10^{-1}$ | $+2.326$ | $+2.225$ | $+2.194$ |
| $K=2$ | $1.00$ | $2.72$ | $9$ | $+9.966 \times 10^{-3}$ | $+1.474 \times 10^{-5}$ | $+4.095 \times 10^{-6}$ | $+3.069 \times 10^{-1}$ | $+1.302 \times 10^{-3}$ | $+6.258 \times 10^{-4}$ |
| $K=2$ | $1.50$ | $4.48$ | $18$ | $+2.563 \times 10^{-3}$ | $+3.368 \times 10^{-6}$ | $+1.270 \times 10^{-7}$ | $+9.200 \times 10^{-2}$ | $+1.368 \times 10^{-4}$ | $+6.773 \times 10^{-7}$ |
| $K=2$ | $2.00$ | $7.39$ | $32$ | $+5.552 \times 10^{-4}$ | $+2.538 \times 10^{-7}$ | $+1.536 \times 10^{-8}$ | $+3.181 \times 10^{-2}$ | $+2.573 \times 10^{-5}$ | $+2.276 \times 10^{-9}$ |
| $K=2$ | $2.50$ | $12.18$ | $53$ | $+6.788 \times 10^{-4}$ | $+4.235 \times 10^{-7}$ | $+1.161 \times 10^{-9}$ | $+1.284 \times 10^{-2}$ | $+1.111 \times 10^{-6}$ | $+4.463 \times 10^{-10}$ |
| $K=3$ | $0.50$ | $1.65$ | $23$ | $+2.395 \times 10^{-1}$ | $+2.383 \times 10^{-1}$ | $+2.367 \times 10^{-1}$ | $+4.083$ | $+3.945$ | $+3.911$ |
| $K=3$ | $1.00$ | $2.72$ | $51$ | $+1.492 \times 10^{-2}$ | $+2.188 \times 10^{-5}$ | $+7.027 \times 10^{-6}$ | $+5.565 \times 10^{-1}$ | $+2.075 \times 10^{-3}$ | $+9.609 \times 10^{-4}$ |
| $K=3$ | $1.50$ | $4.48$ | $95$ | $+4.661 \times 10^{-3}$ | $+5.587 \times 10^{-6}$ | $+1.759 \times 10^{-7}$ | $+1.679 \times 10^{-1}$ | $+1.692 \times 10^{-4}$ | $+9.585 \times 10^{-7}$ |
| $K=3$ | $2.00$ | $7.39$ | $159$ | $+9.771 \times 10^{-4}$ | $+3.566 \times 10^{-7}$ | $+2.594 \times 10^{-8}$ | $+5.704 \times 10^{-2}$ | $+4.323 \times 10^{-5}$ | $+3.264 \times 10^{-9}$ |
| $K=3$ | $2.50$ | $12.18$ | $\mathbf{260}$ | $+1.143 \times 10^{-3}$ | $+7.198 \times 10^{-7}$ | $+1.915 \times 10^{-9}$ | $+2.248 \times 10^{-2}$ | $+1.707 \times 10^{-6}$ | $+6.062 \times 10^{-10}$ |

---

## 3. Certified Slepian Exterior-Frequency Leakage & Conditional 50-Zero Prefix Spectral Concentration Diagnostic

By Milestone 9 (Theorem 1), for every $g \in \mathcal{Q}(A_{\mathrm{arch}}) \subset L^2(-b, b)$ (when $\mathcal{P}_+ \ne \emptyset$ and $\mathcal{P}_- \ne \emptyset$), the unconditional Euler-Depleted Weil Explicit Formula reads
$$\langle g, W_{\mathrm{full}}(b) g \rangle_{L^2(-b, b)} = \sum_{0 < \operatorname{Re}(\rho) < 1} \sigma_{L_{\mathcal{P}_K}}(z_\rho)\,\widehat{g}(z_\rho)\,\overline{\widehat{g}(\overline{z_\rho})}, \qquad z_\rho := \frac{\rho - 1/2}{i}.$$
For any zero $\rho_k = \frac{1}{2} \pm i\gamma_k$ lying on the critical line $\operatorname{Re}(\rho) = 1/2$ (which holds for the first $50$ verified non-trivial zeros enclosed via `flint.acb.zeta_zero(k).imag`), $z_{\rho_k} = \pm \gamma_k \in \mathbb{R}$, so $\overline{z_{\rho_k}} = z_{\rho_k}$ and the paired contribution is $\sigma_{L_{\mathcal{P}_K}}(\gamma_k)\,|\widehat{g}(\gamma_k)|^2 \ge 0$.

To compare the continuous Slepian exterior-frequency projection against the discrete explicit-formula zero sum without conflating the two operators, we compute **both** quantities directly in two-precision (`256`-bit and `384`-bit) `flint.arb` in `verify_untruncated_spatial_slepian.py`:
1. **Certified Continuous Slepian Exterior-Frequency Matrix $E_{\mathrm{Slep}}^{(6, \mathrm{even})}(b; \gamma_1)$**: On $\mathcal{V}_6^{\mathrm{even}}(-b, b)$, the projection onto frequencies $|\xi| \ge \gamma_1 \approx 14.13472514$ has exact spatial representation
   $$\left(E_{\mathrm{Slep}}^{(6, \mathrm{even})}(b; \gamma_1)\right)_{i, j} = \frac{1}{2\pi}\int_{|\xi| \ge \gamma_1} \widehat{e}_{2i}(\xi)\overline{\widehat{e}_{2j}(\xi)}\,d\xi = \delta_{i, j} - \frac{2 b \gamma_1}{\pi} \int_0^2 C_{2i, 2j}(u b)\,\operatorname{sinc}(b\gamma_1 u)\,du.$$
2. **Conditional 50-Zero Prefix Spectral Concentration Diagnostic**: Using FLINT's certified interval enclosures $\gamma_k = \operatorname{Im}(\texttt{flint.acb.zeta\_zero}(k))$ for $k = 1, \dots, 50$ on the rational near-minimizer vector $v_{\min} \in \mathbb{Q}^6$ of $W_{\mathrm{full}}^{(6, \mathrm{even})}(b)$ ($K = 3$), we evaluate the 50-zero partial sum $\sum_{k=1}^{50} 2\sigma_{L_{\mathcal{P}_3}}(\gamma_k)|\widehat{g}_{\min}(\gamma_k)|^2 / \|g_{\min}\|_{L^2}^2$:

| $2b$ | $c = b\gamma_1$ | Certified Slepian Exterior Min RQ $1 - \lambda_0(b\gamma_1)$ | Slepian Exterior Leakage on $v_{\min}$ | Prime+Archimedean RQ on $v_{\min}$ ($K=3$) | Certified 50-Zero Prefix Sum (`flint.acb.zeta_zero`) | 50-Zero Prefix Capture Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $1.00$ | $7.07$ | $1.2783 \times 10^{-5}$ | $1.2019 \times 10^{-4}$ | $+7.0273 \times 10^{-6}$ | $+6.0804 \times 10^{-6}$ | $86.52\%$ |
| $1.50$ | $10.60$ | $1.6788 \times 10^{-7}$ | $5.4098 \times 10^{-7}$ | $+1.7589 \times 10^{-7}$ | $+1.6537 \times 10^{-7}$ | $94.02\%$ |
| $2.00$ | $14.13$ | $7.0847 \times 10^{-9}$ | $2.2033 \times 10^{-6}$ | $+2.5939 \times 10^{-8}$ | $+2.3809 \times 10^{-8}$ | $91.79\%$ |
