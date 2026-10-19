# Analytic Derivations & Quantitative Diagnostics for the Six Post-`v18` Candidate Mechanisms (`cofinal-candidate-mechanisms-screen-2026-10-16-v1`, Repaired per Review)

**Wall check:** Same open gap. Closest results: `WEIL-FLOOR`, `NS24/39/43`, `NB-GAIN` (`NS53/61/83/87/98`), and `ZERO-GEOMETRY` (`NS100/101`). We still need a bound that remains valid as the window grows ($b \to \infty$ or $N \to \infty$), retaining every signed arithmetic contribution and coupling. `RH`, `G2`, and both missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. `M17 v2` and all audited lanes remain **PAUSED**.

---

## 1. Theorem 1: Boundary-Free Dual-Pole Chebyshev–Legendre Identity in Both Parities (`WEIL-FLOOR`, Candidate I)

### 1.1 Statement
Let $a > 0$, let $e_m^{(a)}(x) = \sqrt{\frac{2m+1}{2a}}\,P_m\!\left(\frac{x}{a}\right)\mathbf{1}_{(-a,a)}(x)$ ($m \ge 0$) be the orthonormal Legendre basis of $L^2(-a,a)$, and let
$$C_{m,n}(u) := \int_{-1}^{1-u} \sqrt{\frac{2m+1}{2}}\,P_m(y)\,\sqrt{\frac{2n+1}{2}}\,P_n(y+u)\,dy \qquad (u \in [0, 2]),$$
$$\widetilde{C}_{m,n}(u) := \frac{C_{m,n}(u) + C_{n,m}(u)}{2}.$$
For any $m, n \ge 0$ of the same parity ($m \equiv n \pmod 2$), the signed prime-power shift matrix entry is
$$\bigl(T_{\mathrm{arith}}(a)\bigr)_{m,n} = \sum_{2 \le k < e^{2a}} \frac{\Lambda(k)}{\sqrt{k}}\,2\,\widetilde{C}_{m,n}\!\left(\frac{\log k}{a}\right) = \int_{1^-}^{e^{2a}} x^{-1/2}\,2\,\widetilde{C}_{m,n}\!\left(\frac{\log x}{a}\right) d\psi(x),$$
and the polar matrix entry is
$$\bigl(T_{\mathrm{pole}}(a)\bigr)_{m,n} = \begin{cases} +2\,c_m(a)c_n(a) & (m, n \text{ even}), \\ -2\,s_m(a)s_n(a) & (m, n \text{ odd}), \end{cases}$$
where $c_m(a) = \int_{-a}^a e_m^{(a)}(x)\cosh(x/2)\,dx$ and $s_m(a) = \int_{-a}^a e_m^{(a)}(x)\sinh(x/2)\,dx$.

**Theorem 1.** For all $m, n \ge 0$ with $m \equiv n \pmod 2$ and every $a > 0$,
$$\bigl(T_{\mathrm{pole}}(a)\bigr)_{m,n} = \int_1^{e^{2a}} x^{-1/2}\,2\,\widetilde{C}_{m,n}\!\left(\frac{\log x}{a}\right) d(x + \log x - 1). \tag{1.1}$$
Consequently, defining the dual-pole Chebyshev remainder $\widetilde{R}_\psi(x) := \psi(x) - x - \log x + 1$, Stieltjes integration by parts on $[1, e^{2a}]$ produces **identically zero boundary terms at both endpoints** ($\widetilde{R}_\psi(1) = 0$ at $x = 1$ and $\widetilde{C}_{m,n}(2) = 0$ at $x = e^{2a}$) and yields the exact identity
$$\bigl(T_{\mathrm{arith}}(a) - T_{\mathrm{pole}}(a)\bigr)_{m,n} = \int_0^2 \frac{\psi(e^{au}) - e^{au} - au + 1}{e^{au/2}}\,\bigl(a\,\widetilde{C}_{m,n}(u) - 2\,\widetilde{C}_{m,n}'(u)\bigr)\,du. \tag{1.2}$$

### 1.2 Proof
Using $\cosh\!\left(\frac{x-y}{2}\right) = \cosh(x/2)\cosh(y/2) - \sinh(x/2)\sinh(y/2)$ and the parity of $e_m^{(a)}, e_n^{(a)}$:
- If $m, n$ are **even**, $\int_{-a}^a e_m^{(a)}(x)\sinh(x/2)\,dx = 0$, so
  $$\iint_{(-a,a)^2} e_m^{(a)}(x)e_n^{(a)}(y)\,2\cosh\!\left(\frac{x-y}{2}\right) dx\,dy = 2\,c_m(a)c_n(a) = \bigl(T_{\mathrm{pole}}(a)\bigr)_{m,n}.$$
- If $m, n$ are **odd**, $\int_{-a}^a e_m^{(a)}(x)\cosh(x/2)\,dx = 0$, so
  $$\iint_{(-a,a)^2} e_m^{(a)}(x)e_n^{(a)}(y)\,2\cosh\!\left(\frac{x-y}{2}\right) dx\,dy = -2\,s_m(a)s_n(a) = \bigl(T_{\mathrm{pole}}(a)\bigr)_{m,n}.$$
In **both** parities simultaneously, changing variables to $\tau = |x-y| \in (0, 2a)$ gives
$$\bigl(T_{\mathrm{pole}}(a)\bigr)_{m,n} = \int_0^{2a} 2\cosh(\tau/2)\,2\,\widetilde{C}_{m,n}\!\left(\frac{\tau}{a}\right) d\tau = \int_0^{2a} \bigl(e^{\tau/2} + e^{-\tau/2}\bigr)\,2\,\widetilde{C}_{m,n}\!\left(\frac{\tau}{a}\right) d\tau.$$
Substituting $x = e^\tau \in [1, e^{2a}]$ ($\tau = \log x$, $d\tau = dx/x$) gives
$$\bigl(e^{\tau/2} + e^{-\tau/2}\bigr)\,d\tau = x^{-1/2}\!\left(1 + \frac{1}{x}\right) dx = x^{-1/2}\,d(x + \log x - 1),$$
which proves $(1.1)$ for both even and odd parities simultaneously. Subtracting $(1.1)$ from $T_{\mathrm{arith}}(a)$ and integrating by parts against $\widetilde{R}_\psi(x) = \psi(x) - x - \log x + 1$ with $\widetilde{R}_\psi(1) = 0$ and $\widetilde{C}_{m,n}(2) = 0$ yields $(1.2)$ with zero boundary terms. $\square$

### 1.3 Quantitative Verification & Finite-Shell Scope
Certified at `256`-bit and `384`-bit precision in `verify_cofinal_candidate_mechanisms.py`:
- Across all 8 benchmark pairs $(m,n) \in \{(0,0), (0,2), (2,4), (4,4), (1,1), (1,3), (3,3), (3,5)\}$ at $\lambda = 5$ ($a = \log 5$), `lhs - rhs` in $(1.2)$ satisfies `.contains(0)` with ball radius $\le 1.31 \times 10^{-65}$ (`256`-bit) and $\le 1.48 \times 10^{-98}$ (`384`-bit).
- On the unpreconditioned, unshifted $8\times 8$ Legendre subspaces $V_8^{\mathrm{even}}(-a,a)$ and $V_8^{\mathrm{odd}}(-a,a)$, the compressed Weil matrix $\mathsf{W}_\lambda^{(8)} = P_8\bigl(A_{\mathrm{arch}}^{\mathrm{full}}(a) + T_{\mathrm{pole}}(a) - T_{\mathrm{arith}}(a)\bigr)P_8$ is certified strictly positive definite via `cholesky_lower_arb` across all four benchmark windows $\lambda \in \{2, 3, 5, 8\}$ (up to 26 prime-power shifts, $k \le 61$).
- **Finite-Shell Scope Note**: The Frobenius ratio $\frac{\sum 2\Lambda(k)/\sqrt{k}}{\|T_{\mathrm{arith}}(a)|_{V_{[4,8]}^{\mathrm{even}}}\|_F} = 53.16\times$ at $\lambda = 8$ ($0.498479$ vs. $26.497679$) measures cancellation on the **finite 4-mode Legendre shell** $V_{[4,8]}^{\mathrm{even}}$ ($m \in \{8, 10, 12, 14\}$) only; it does not bound the infinite-dimensional tail $V_4(a)^\perp$ or cross-couplings to $(V_8^{\mathrm{even}})^\perp$.

---

## 2. Theorem 2 & Candidate II / IIb: Critical-Zero Screening vs. Position-Weighted Radical $x\,h(x)$ (`WEIL-FLOOR`)

### 2.1 Statement, Exact Phase/Normalization, and Closed-Form Odd Pole Moment
By `eq:v150-mellin` (`evidence/v150/capacity_weight.tex`, lines 66–69), the even Gaussian arithmetic radical $h(x)$ satisfies for all $z \in \mathbb{C}$:
$$M(z) := \int_{\mathbb{R}} h(x)\,e^{(z - 1/2)x}\,dx = \frac{z(z-1)}{\sqrt{3}}\,\pi^{-z/2}\Gamma\!\left(\frac{z}{2}\right)\zeta(z) = \frac{2}{\sqrt{3}}\,\xi(z), \tag{2.1}$$
where $\xi(z) := \frac{1}{2}z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z)$ satisfies $\xi(1) = \frac{1}{2}$ and $\Xi(\gamma) := \xi(\frac{1}{2} + i\gamma)$ satisfies $\Xi'(\gamma) = i\,\xi'(\frac{1}{2} + i\gamma)$.
1. **Critical-Zero Screening of Translated Radicals (`Candidate II`)**: For every translation $h_\tau(x) = h(x - \tau)$, $\widehat{h_\tau}(\gamma) = e^{-i\gamma\tau}\frac{2}{\sqrt{3}}\Xi(\gamma)$ vanishes identically at every critical-line zero $\rho_k = \frac{1}{2} + i\gamma_k$ ($\Xi(\gamma_k) = 0$).
2. **Position-Weighted Radical $f_{\mathrm{pos}}(x) := x\,h(x)$ (`Candidate IIb`, Theorem 2)**: Differentiating $(2.1)$ with respect to $z$ gives
   $$M'(z) = \int_{\mathbb{R}} x\,h(x)\,e^{(z - 1/2)x}\,dx = \frac{2}{\sqrt{3}}\,\xi'(z). \tag{2.2}$$
   - **Fourier Phase at Critical Zeros**: Since $f_{\mathrm{pos}}(x) = x\,h(x)$ is real and odd, its Fourier transform $\widehat{f_{\mathrm{pos}}}(\gamma) := \int_{\mathbb{R}} x\,h(x)\,e^{-i\gamma x}\,dx$ is purely imaginary:
     $$\widehat{f_{\mathrm{pos}}}(\gamma_k) = M'\!\left(\frac{1}{2} - i\gamma_k\right) = -M'\!\left(\frac{1}{2} + i\gamma_k\right) = -\frac{2}{\sqrt{3}}\,\xi'\!\left(\frac{1}{2} + i\gamma_k\right) = +\frac{2i}{\sqrt{3}}\,\Xi'(\gamma_k) \ne 0$$
     for simple critical-line zeros. At $\gamma_1 = 14.134725141734695\dots$, `flint.acb_series` jet evaluation certifies $\Xi(\gamma_1) \ni 0$ (`rad = 3.18e-81` at 256-bit) and $\Xi'(\gamma_1) = -0.001382719089216254\dots \ne 0$.
   - **Closed-Form Odd Pole Moment at $z = 1$**: Since $x\,h(x)$ is odd, $\int_{\mathbb{R}} x\cosh(x/2)h(x)\,dx = 0$, and therefore $\sinh(x/2) = e^{x/2} - \cosh(x/2)$ gives
     $$\int_{\mathbb{R}} x\sinh\!\left(\frac{x}{2}\right)h(x)\,dx = \int_{\mathbb{R}} x\,e^{x/2}h(x)\,dx = M'(1) = \frac{2}{\sqrt{3}}\,\xi'(1).$$
     Since $M(1) = \frac{2}{\sqrt{3}}\xi(1) = \frac{1}{\sqrt{3}}$ (`eq:v150-pole-mass`) and the logarithmic derivative of $z\pi^{-z/2}\Gamma(z/2)\cdot (z-1)\zeta(z)$ at $z = 1$ is $1 - \frac{1}{2}\log\pi + \frac{1}{2}\psi(1/2) + \gamma_E = 1 + \frac{\gamma_E - \log(4\pi)}{2}$, we obtain in closed form:
     $$\int_{\mathbb{R}} x\sinh\!\left(\frac{x}{2}\right)h(x)\,dx = \frac{1}{\sqrt{3}}\!\left(1 + \frac{\gamma_E - \log(4\pi)}{2}\right) = +0.01333431378871523222883\dots > 0. \tag{2.3}$$
   - **Complete Two-Sided Tail-Enclosed Quadrature & Complex-Box Kernel Verification**:
     - *Repaired $[3.5, \infty)$ Integral Tail (`lem:v150-weight`)*: Earlier `v3`/`v4` had an extraneous factor of $2$ inside the outer exponential (`exp(-2*pi*exp(7))` $\approx 1.65 \times 10^{-2991}$), which was smaller than the true tail lower bound $> 8.53 \times 10^{-1492}$. By `lem:v150-weight` (`eq:v150-weight-bounds`), $A_- e^{9x/2 - \pi e^{2x}} \le h(x) \le A_+ e^{9x/2 - \pi e^{2x}}$ for $x \ge 0$ with $A_- = \frac{4\pi(2\pi - 3)}{\sqrt{3}}$ and $A_+ = \frac{16\pi^2}{\sqrt{3}}$. Since $-\frac{d}{dx}(x e^{3x - \pi e^{2x}}) = (2\pi - (3 + 1/x)e^{-2x}) x e^{5x - \pi e^{2x}}$, integrating on $[x_0, \infty)$ at $x_0 = 3.5$ ($w_0 = e^7$) yields the exact two-sided enclosure
       $$2.81357192 \times 10^{-1491} = \frac{(1 - e^{-x_0})A_- x_0 e^{3x_0 - \pi w_0}}{2\pi} \le 2\int_{x_0}^\infty x\sinh(x/2)h(x)\,dx \le \frac{A_+ x_0 e^{3x_0 - \pi w_0}}{2\pi - (3 + 1/x_0)e^{-2x_0}} = 1.11095453 \times 10^{-1490}.$$
       Adding `arb(0, tail_35_upper)` to the $[0, 3.5]$ quadrature certifies `m1_num - m1_closed` via `.contains(0)` to radius $2.68 \times 10^{-29}$ (`256`-bit) and $3.22 \times 10^{-41}$ (`384`-bit), leaving the rounded moment unchanged.
     - *Repaired Complex-Box & Negative-Input Kernel Evaluator (`h_and_dh_acb`)*: Earlier `v4` evaluated the unsplit convolution at negative arguments $\frac{1}{2}\log k - u < 0$ (where the truncated $\operatorname{Re}(z) \ge 0$ series returned negative values such as $-1.2486 \times 10^{-4}$ at $x = -1.7$, even though $h(-1.7) = h(1.7) = +1.2357 \times 10^{-36} > 0$) and used a static real-$z=0$ tail radius (`exp(-144*pi)`) that is invalid on complex quadrature boxes $z = x + iy$ where $\alpha = \operatorname{Re}(e^{2z}) = e^{2x}\cos(2y) < 1$ (or $\le 0$ on wide un-subdivided boxes). In the repaired verifier: (i) the convolution integral is split at $u_{\mathrm{split}} = \min(a - \frac{1}{2}\log k, \frac{1}{2}\log k)$ using $h(-v) = h(v)$ so all contour inputs lie in $[0, a]$; (ii) for $\operatorname{Re}(z) < 0$, `h_and_dh_acb` applies exact Poisson reflection $h(z) = h(-z)$ and $h'(z) = -h'(-z)$; (iii) on wide complex boxes where $\operatorname{Re}(z) \le -0.25$ or $\alpha = \operatorname{Re}(e^{2z}) \le 0.5$, `h_and_dh_acb` returns `nan` so `acb.integral` bisects the box; and (iv) on valid boxes ($\operatorname{Re}(z) > -0.25$, $\alpha > 0.5$), the $n \ge 16$ tail radius is computed dynamically in `flint.arb` from $r = |e^z|$ and $\alpha = \operatorname{Re}(e^{2z})$.
   - **Compressed 8-Mode Residual Scope, Infinite-Dimensional $L^2(-a,a)$ Parseval Tail, and Omitted $V_8(a)^\perp$ Coupling Scope**:
     1. Via Parseval's identity $\|(I - P_8)f\|_{L^2(-a,a)}^2 = \int_{-a}^a |f(x)|^2\,dx - \|P_8 f\|_2^2$, `verify_cofinal_candidate_mechanisms.py` encloses the orthogonal tail norm on $V_8(-a,a)^\perp \subset L^2(-a,a)$ alongside the exterior pole-mass leakage bound $2\int_a^\infty \cosh(x/2)h(x)\,dx \le \frac{32\pi^2\lambda^5 e^{-\pi\lambda^2}}{\sqrt{3}(2\pi\lambda^2 - 5)}$ (`lem:v150-weight`).
     2. Via split-contour 1D convolution quadrature on $[0, a]$, it encloses $\langle f, (T_{\mathrm{pole}}(a) - T_{\mathrm{arith}}(a))f\rangle_{L^2(-a,a)}$ and $\Delta_{\mathrm{AP},\perp}(f; a) := \langle f, (T_{\mathrm{pole}}(a) - T_{\mathrm{arith}}(a))f\rangle_{L^2(-a,a)} - \langle P_8 f, (T_{\mathrm{pole}}(a) - T_{\mathrm{arith}}(a))P_8 f\rangle$.
     3. **Explicit Scope Limitation**: These coupling calculations concern **only two specific functions** ($f = h$ and $f = x\,h$) at **four finite windows** ($\lambda \in \{2, 3, 5, 8\}$), cover **only the arithmetic-plus-pole contribution** $T_{\mathrm{pole}}(a) - T_{\mathrm{arith}}(a)$ (not the full unbounded archimedean form $A_{\mathrm{arch}}^{\mathrm{full}}(a)$ on $V_8(a)^\perp$ or all $f \in \mathcal{Q}(A_{\mathrm{arch}})$), and **do not establish the full uniform Weil bound**. Moreover, agreement between two precisions (`176 / 176` ball overlaps) checks only numerical conditioning of the implemented expressions and cannot by itself detect an analytic formula or tail-bound error shared by both runs.

---

## 3. Candidate III: Multiprime Codimension & `flint.arb` Cholesky Weyl Enclosure (`WEIL-FLOOR` / `KERNEL-API`)

Certified in pure `flint.arb` across $\lambda \in \{2, 3, 5, 8\}$ on $V_8^{\mathrm{even}}(-a,a)$:
- Under the `NS57` single-coefficient perturbation of the weighted $k = 2$ shift coefficient $c_2 = \frac{\Lambda(2)}{\sqrt{2}} \mapsto c_2 + \delta_2$ (equivalently $\Lambda(2) \mapsto \log 2 + \sqrt{2}\,\delta_2$) with $\delta_2 = -\frac{\log 2}{100}$ (`2|\delta_2| = 0.0138629436...`), where $(S_2^{(8,\mathrm{even})}(a))_{m,n} = 2\,\widetilde{C}_{m,n}(\frac{\log 2}{a})$, the perturbation matrix is $B_{\delta_2} = -\delta_2 S_2^{(8,\mathrm{even})}(a)$.
- Rather than relying on floating-point midpoint eigenvalues, `verify_cofinal_candidate_mechanisms.py` certifies via `cholesky_lower_arb` that **both** $(2|\delta_2|)I_8 + B_{\delta_2} \succ 0$ and $(2|\delta_2|)I_8 - B_{\delta_2} \succ 0$ in `flint.arb` across all $\lambda \in \{2, 3, 5, 8\}$ (with minimum Cholesky pivots $\ge 0.048068 > 0$). By Weyl's inequality, this rigorously encloses $|\lambda_k(\mathsf{W}_\lambda^{(8),\delta_2}) - \lambda_k(\mathsf{W}_\lambda^{(8)})| < 2|\delta_2| = \frac{\log 2}{50}$ (`thm:ns57-bounded-floor-stability`).

---

## 4. Candidates A, B, and C: Finite-Block Residual Diagnostics (`NB-GAIN`)

Certified at `256`-bit and `384`-bit precision across $N \in \{4, 8, 16, 32\}$:
- **Candidate A (Dual Stieltjes–Divisor Identity vs. `NS74` Obstruction)**: On both the true load ($\beta = 1/2$) and the `NS74` positive-floor load ($\beta = 1/2 + 10^{-2}$), the Schur-complement pairing equals the exact divisor-bundled pairing to `.contains(0)` across all $N \in \{4, 8, 16, 32\}$. Because `NS74` has a strictly positive asymptotic floor ($E_\infty(\beta) \ge 4.9532 \times 10^{-7} > 0$), this algebraic rearrangement alone cannot force $E_N^{(2)} \to 0$.
- **Candidate B (Exact `NS83` $q = 2$ Target Mellin Value $T_2(\rho_1)$ & Finite-Block Scope)**:
  - By `eq:ns83-transforms` (`evidence/v166/ns83/proof.tex`, line 54), for smoothing order $q = 2$ ($E_N^{(2)} = E_N$), the transformed target $h_2 = W\tau_2$ has Mellin transform
    $$T_2(s) = \widehat{h}_2(s) = \frac{s - 1}{s^3}.$$
    At the first critical zero $\rho_1 = \frac{1}{2} + i\gamma_1$ ($|\rho_1 - 1| = |\rho_1|$), its exact magnitude is
    $$|T_2(\rho_1)| = \frac{|\rho_1 - 1|}{|\rho_1|^3} = \frac{1}{|\rho_1|^2} = \frac{1}{\gamma_1^2 + 1/4} = 0.004998988833723139\dots,$$
    with first conjugate-pair weight $\frac{2}{|\rho_1|^4} = 2|T_2(\rho_1)|^2 = 4.9979778719377274 \times 10^{-5}$ and 50-pair `NS83` critical-zero floor $C_{2,50} = \sum_{k=1}^{50} \frac{2}{(\gamma_k^2 + 1/4)^2} = 7.407941924932869 \times 10^{-5}$ (correcting `v1`, which displayed $0.00035169\dots$ from a different $(1-x)^2$ expression).
  - **Finite-Block Scope Note**: The four finite dyadic values of $(\log N)E_N^{(2)}$ ($2.952\times 10^{-3}, 2.269\times 10^{-4}, 8.858\times 10^{-5}, 8.445\times 10^{-5}$) and $\frac{\log N}{\log 2}\frac{\Delta_N}{E_N^{(2)}}$ ($1.8975, 2.1216, 0.9491, 0.9456$) across $N \in \{4, 8, 16, 32\}$ are finite-block observations only; they **cannot** establish asymptotic convergence or persistent cofinal gain (`prop:ns83-log-floor` in `evidence/v166/ns83/proof.tex` is an asymptotic $\liminf$ lower bound with no finite-$N$ onset threshold).
- **Candidate C (Finite-Block Inverse-Gram & Old-Space Refit Ratios)**: At $N = 32$, $\operatorname{tr}(H_N)/\operatorname{tr}(D_N) = 0.0043075$ and $\|h_N\|_2^2 / \|b_{\mathrm{new}}\|_2^2 = 2.0511 \times 10^{-9}$, quantifying finite-block old-space refit cancellation while leaving the $N \to \infty$ analytic transfer open.
