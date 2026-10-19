# Multi-Mode Jacobi–Stieltjes–Divisor Extractors in `NS-61` Hilbert Space (`2026-10-15-v1`)

## Wall Check

- **Target walls**: `NB-GAIN` and `COEFF`.
- **Closest prior results**: `NS-61`, `NS-71`, `NS-72`, `NS-74`, `audits/codex-review-and-all-vector-extension-2026-10-15-v1/`, and `audits/coeff-specialist-brief-2026-10-15-v5.html`.
- **Summary of certified results**:
  1. **Complete Jacobi–Stieltjes–Divisor Hierarchy in $H_{0,0}^\nu([1, 2])$ ($\nu \in \{2, 3\}$)**:
     Every polynomial $\widetilde{\psi}_\nu^{(m)}(u) := (u-1)^\nu(2-u)^\nu \widetilde{P}_m^{(\nu, \nu)}(2u-3)$ ($m \ge 1$) satisfies $\int_1^2 \widetilde{\psi}_\nu^{(m)}(u)\,du = 0$ identically by Jacobi orthogonality against $\widetilde{P}_0^{(\nu, \nu)}(t) = 1$, and produces an `NS-61` Hilbert-space extractor $\Lambda_{N, \nu}^{(m)}(x) = -\frac{d}{dx}\bigl(x(F_{N, \nu}^{(m)})'(x)\bigr)\mathbf{1}_{[1/(2N), 1/N]}(x)$ whose three-way divisor-sum moment $M_{N, \nu}^{(m)}(u, y) = \sum_{n=N+1}^{2N-1} \widetilde{\psi}_\nu^{(m)}(n/N)(1*\Delta c)(n)$ holds exactly.
  2. **Exact Linear-in-$N$ Rational Gram Matrix, Loewner Matrix Bessel Inequality, and $L D L^T$ Diagonalization**:
     The full-space Gram matrix in $H = L^2(0, \infty; dx)$ scales purely linearly in $N$: $G_{N, \nu}^{(K)} = N\,\widehat{\mathcal{G}}^{(\nu, K)}$ with exact $N$-independent rational matrix $\widehat{\mathcal{G}}^{(\nu, K)} \in \mathbb{Q}^{K \times K}$. By Bessel's inequality in $H$, the Schur-projected Gram matrix satisfies the Loewner inequality $0 \prec \widetilde{G}_{\mathrm{proj}, N, \nu}^{(K)} \preceq N\,\widehat{\mathcal{G}}^{(\nu, K)}$, and exact rational Cholesky factorization $\widehat{\mathcal{G}}^{(\nu, K)} = L_\nu D_\nu L_\nu^T$ diagonalizes the unconditional Bessel lower bound into a sum of $K$ squares $\mathcal{B}_{N, \nu}^{(K)} = \frac{1}{N}\sum_{k=1}^K |\widetilde{M}_{N, \nu}^{(k)}(u, y)|^2 / d_{\nu, k}$.
  3. **Resolution of the $N = 16$ Single-Mode Phase-Cancellation Dip**:
     At $N = 16$, where the single odd mode $K = 1$ dips to $\mathcal{R}_{16, 3}^{(1)}/\Delta_{16} = 0.000265$ and $\mathcal{B}_{16, 3}^{(1)}/\Delta_{16} = 0.000052$, the 4-mode Jacobi–Stieltjes–Divisor basis ($K = 4$) improves the captured dyadic step gain by **$1,306.9\times$ (Rayleigh: $34.57\%$ of $\Delta_{16}$)** and **$1,339.9\times$ (Bessel: $6.97\%$ of $\Delta_{16}$)** in $H_{0,0}^3([1, 2])$, and captures **$71.17\%$ of $\Delta_{16}$ (Rayleigh)** / **$7.21\%$ of $\Delta_{16}$ (Bessel)** in $H_{0,0}^2([1, 2])$.

## Files in This Audit Package

- `PROPOSAL.md` — Wall check, theorem statements, and summary of changes.
- `derivation.md` — Complete mathematical proofs and 384-bit `flint.arb` certified tables.
- `verify_multimode_extractor.py` — Deterministic 384-bit `flint.arb` + `fractions.Fraction` verification script (`pyright` 0 errors, 0 warnings).
- `verification.json` — Certified machine-readable output (`sha256=51fb88c333ade4176f9472734e2fe941070c0b7514721ecae7d800a06475d8be`, runtime $14.038\text{ s}$, `all_certified=True`).
- `../multimode-dyadic-extractor-2026-10-15-v1.html` — Styled HTML companion report.
- `../coeff-specialist-brief-2026-10-15-v6.html` — Separately versioned Specialist Brief v6 (preserving `-v3.html`, `-v4.html`, `-v5.html`).

## Reproduction Command

```bash
/Users/alex/riemann-worktrees/origin-main-review/.venv/bin/python \
  /Users/alex/riemann-worktrees/origin-main-review/audits/multimode-dyadic-extractor-2026-10-15-v1/verify_multimode_extractor.py
```

## Mandatory Open-Status & Scope Disclosure

- **Scope of the Multi-Mode Stieltjes–Divisor Extractor Identity:** The three-way identity $M_{N,\nu}^{(m)}(u,y) = \sum_{n=N+1}^{2N-1}\widetilde{\psi}_\nu^{(m)}(n/N)(1*\Delta c)(n)$ and Loewner Bessel bound $\Delta_N \ge \mathcal{B}_{N,\nu}^{(K)}$ are exact algebraic duality identities on the removable component $P_{\mathcal{T}}(U_\beta^*\tau)$. Because they depend on the unknown inverse-Gram increments $\Delta c = c_{2N} - c_N$ and hold identically on the `NS-74` altered-target control while $E_N^{(2)}(\beta) \to F_\beta > 0$, they do **not** supply an unconditional cofinal lower bound on $\Delta_N / E_N^{(2)}$ (see [`nb-full-residual-arithmetic-assessment-2026-10-16-v1.html`](../nb-full-residual-arithmetic-assessment-2026-10-16-v1.html)).
- **Open-Status Disclosure:** **RH**, **G2**, the **cofinal signed-arithmetic lower bound**, and **both historical missing-original evidence groups** in `evidence/MISSING.md` remain **OPEN**.
