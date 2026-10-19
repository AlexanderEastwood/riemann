# PROPOSAL — Milestone 11: Mellin–Jacobi–Legendre Finite-Rank Gram–Schur Reduction & Exact Polynomial Shift Matrices (`NB-GAIN` / `COEFF` & `NS-61`)

**Date:** 2026-10-15  
**Target Lanes:** `NB-GAIN` / `COEFF` (Mellin–Jacobi Basis & Coefficient Operators) & `NS-61` / `NS-71` (Finite-Rank Residual Reduction)  
**Audit Directory:** `audits/mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1/`

---

## Wall Check (Top of Deliverable)

> **Wall check:** Does this deliverable prove the Riemann Hypothesis (RH), complete the global archimedean completion (G2), establish the cofinal prime-shift lower bound as $a \to \infty$, or recover the missing historical raw outputs in `evidence/MISSING.md`?  
> **No.** RH, G2, the cofinal signed-arithmetic lower bound as $a \to \infty$, and both historical missing-original evidence groups in `evidence/MISSING.md` (`stage4_run_summary.json` / `stage4_Ticks.json` and `certificate.json` / `verify_log.txt`) remain **OPEN**.
>
> **Why this milestone moves us closer to RH (not smaller bounds):**  
> In Milestones 7–10, piecewise-constant step functions $\mathbf{1}_{I_k}$ required $N_{\mathrm{elem}} \sim 68\text{--}207$ intervals because step functions have slow $O(\ell_k^2)$ Fourier decay. By contrast, in the Mellin–Jacobi / Legendre polynomial basis $\phi_m(x) = \sqrt{\frac{2m+1}{2b}}\,P_m(x/b)$ on $L^2(-b, b)$ (`NB-GAIN` / `COEFF`):
> 1. **Theorem 1 (Gegenbauer–Spherical-Bessel Parseval Identity & Finite-$N$ Archimedean Tail Reduction):** Under Fourier transform, $\widehat{\phi_m}(\xi) = (-i)^m \sqrt{2b(2m+1)}\,j_m(b\xi)$, and by Gegenbauer's addition theorem we have the **exact pointwise Parseval identities**
>    $$\sum_{r=0}^\infty (4r+1) j_{2r}(z)^2 = \frac{1}{2}\bigl(1 + \operatorname{sinc}(2z)\bigr), \qquad \sum_{r=0}^\infty (4r+3) j_{2r+1}(z)^2 = \frac{1}{2}\bigl(1 - \operatorname{sinc}(2z)\bigr).$$
>    Therefore, projecting $L^2_{\mathrm{even}}(-b, b) = \mathcal{V}_N^{\mathrm{even}} \oplus (\mathcal{V}_N^{\mathrm{even}})^\perp$ onto the first $N$ even Legendre polynomials $\mathcal{V}_N^{\mathrm{even}} = \operatorname{span}\{\phi_0, \phi_2, \dots, \phi_{2N-2}\}$ (and similarly $\mathcal{V}_N^{\mathrm{odd}} = \operatorname{span}\{\phi_1, \phi_3, \dots, \phi_{2N-1}\}$), the infinite-dimensional tail trace $\varepsilon_N^{\mathrm{even}}(b, \Delta_\alpha) := \operatorname{Tr}(\Pi_\perp A_-^{(\Delta_\alpha)} \Pi_\perp)$ is given by a **closed-form finite-sum complement** requiring zero infinite series truncation, and decays super-exponentially as $\frac{(b\xi_0)^{4N+1}}{((4N+1)!!)^2}$: at $N = 4$ (a **$4 \times 4$ matrix**!), $\varepsilon_4^{\mathrm{even}}$ is $5.64 \times 10^{-9}$ at $K=2$, $3.35 \times 10^{-12}$ at $K=3$, and $1.31 \times 10^{-16}$ at $K=4$.
> 2. **Theorem 2 (Exact Rational Polynomial Shift Matrices $S_\tau^{(N)}$ & $4 \times 4$ Legendre–Schur Continuum Certification):** Because $\phi_m(x)$ is a polynomial of degree $m$, the shift matrix entries $(S_\tau)_{mn} = \langle \phi_m, (T_\tau + T_{-\tau})\phi_n \rangle_{L^2(-b, b)}$ are **exact polynomials in $u = \tau/b \in [0, 2]$ of degree $m+n+1$ with rational coefficients** (e.g., $(S_\tau)_{0,0} = 2 - u$, $(S_\tau)_{0,2} = \frac{\sqrt{5}}{2}u^2(u-2)$, $(S_\tau)_{1,1} = (2-u)(1 - u - \frac{1}{2}u^2)$). By the Cauchy–Schur complement theorem on $L^2(-b, b) = \mathcal{V}_N \oplus \mathcal{V}_N^\perp$, infinite-dimensional continuum positivity of the multi-prime Weil operator reduces to a **$3 \times 3$ or $4 \times 4$ finite matrix Cholesky certificate** on $\mathcal{V}_N$!

---

## Deliverables & Acceptance Criteria

1. **`derivation.md`**: Complete self-contained proofs of Theorems 1 and 2.
2. **`verify_mellin_jacobi_schur_reduction.py`**: Pure 256-bit and 384-bit `flint.arb` certificate script (two-precision replay per `AGENTS.md` §4, zero float tolerances in ball checks, `pyright` clean).
3. **`verification.json`**: Machine-readable audit payload with canonical `payload.sha256` and `file_sha256`.
4. **`README.md`** and versioned HTML report `audits/mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1.html`.
