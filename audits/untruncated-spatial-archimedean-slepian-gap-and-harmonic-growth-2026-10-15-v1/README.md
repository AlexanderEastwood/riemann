# Milestone 16 Audit Package — Untruncated Spatial Archimedean Formula, Rational Harmonic Legendre Growth, Arbitrary-Bandwidth Positivity up to $2b = 2.50$ ($260$ Shifts), and Slepian Zero-Gap Duality (`WEIL-FLOOR`, `NB-GAIN` / `COEFF`, & `KERNEL-API`)

- **Audit folder**: `audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/`
- **HTML report**: `audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1.html`
- **Target lanes**: `WEIL-FLOOR`, `NB-GAIN` / `COEFF`, and `KERNEL-API`
- **Verification hashes**:
  - `payload.sha256 = 4592cff3eb909f0b3b6ef6dafc56c29aba2e079c344a45c319d49de56ab90a2f`
  - `file_sha256 = f049fdb0183e87e6b4da552376a19b517c70180f59508db9e76abc667e233804`
  - Two-precision (`256`-bit and `384`-bit) `flint.arb` overlap checks: `80/80` (`all_passed = True`)

## Wall Check & Open-Status Disclosure

- **Does this milestone prove the Riemann Hypothesis (RH)?** **No (`OPEN`).**
- **Does this milestone prove `G2` or the cofinal prime-shift lower bound as $a \to \infty$ ($K \to \infty$, $b \to \infty$, $N_{\mathrm{leg}} \to \infty$)?** **No (`OPEN`).** Theorem 1.2 is a **diagonal growth identity** proving that the untruncated archimedean diagonal grows logarithmically as $\mathcal{J}_{m, m}(0; b) = \mathcal{H}_m - \gamma_E - \log(4\pi b) - \frac{b^2}{12(2m-1)(2m+3)} + O(b^4/m^4) \sim \log\!\left(\frac{m}{\pi b}\right) \to +\infty$ with Legendre degree $m \to \infty$, and Theorem 2 certifies strict positive definiteness of the untruncated 6-mode even and odd Legendre Weil matrices $W_{\mathrm{full}}^{(6, \mathrm{even})}(b) \succ 0$ and $W_{\mathrm{full}}^{(6, \mathrm{odd})}(b) \succ 0$ across free bandwidths $2b \in \{0.50, 1.00, 1.50, 2.00, 2.50\}$ ($e^{2b} \approx 12.18$, up to **260 active shifts** at $N = 365 > 12 P_3$). Growing diagonal entries alone do **not** bound the infinite high-degree block $\mathcal{H}_{> N}$ from below without an infinite-dimensional tail operator lower bound and off-diagonal block coupling control (established for the five discrete rational bandwidths $2b \in \{0.40, 0.42, 0.45, 0.48, 0.50\}$ in Milestone 17, while the cofinal $b \to \infty$ lower bound remains **OPEN**).
- **Missing-original evidence disclosure**: Both historical missing-original evidence groups documented in `evidence/MISSING.md` (`src/verify_phase2.py` and `final_weil_check.py`) remain **OPEN**.

## Contents

1. [`PROPOSAL.md`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/PROPOSAL.md): Problem statement, theorem summary, and scope boundaries.
2. [`derivation.md`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/derivation.md): Analytic proofs of Theorem 1 (Exact Untruncated Spatial Archimedean Formula & Rational Harmonic / Weber–Schafheitlin Legendre Asymptotics), Theorem 2 (All-Bandwidth Internal Prime-Tower Telescoping & Multi-Degree Untruncated Weil Positivity up to $2b = 2.50$, 260 Shifts), and Section 3 (Certified Slepian Exterior-Frequency Leakage & Conditional 50-Zero Prefix Spectral Concentration Diagnostic).
3. [`verify_untruncated_spatial_slepian.py`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/verify_untruncated_spatial_slepian.py): Self-contained two-precision (`256`-bit and `384`-bit) `flint.arb` / `flint.acb` verification script (zero `numpy`/`mpmath` imports) passing `pyright` with `0 errors, 0 warnings, 0 informations`.
4. [`verification.json`](file:///Users/alex/riemann-worktrees/origin-main-review/audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/verification.json): Two-precision ball-arithmetic certificate artifact (`80/80` overlap checks PASS).

## Replay Command

```bash
pyright audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/verify_untruncated_spatial_slepian.py
.venv/bin/python audits/untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1/verify_untruncated_spatial_slepian.py
```
