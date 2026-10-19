# All-Vector Weil Positivity Beyond $a_{\star\star\star\star} = \frac{1}{2}\log(15/2)$ up to the Three-Island Isometric Horizon $a_{\star\star\star\star\star} = \frac{3}{2}\log 2 = \frac{1}{2}\log 8 \approx 1.039721$ (`2026-10-15-v1`)

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this audit claims a proof of RH or global Weil positivity.

---

## 1. Contents of This Audit Package

- [`PROPOSAL.md`](./PROPOSAL.md): Scope, mathematical claims, and falsifiability criteria.
- [`derivation.md`](./derivation.md): Complete mathematical derivations of:
  1. **Theorem 1 (Exact 4-Point Klein 4-Group Fiber Closure on $(\frac{1}{2}\log(15/2), \frac{3}{2}\log 2]$)**: For $x_6 < d_5$, every 4-point fiber $\{x_1, x_2, x_3, x_4\}$ on $[x_6, d_5]$ is an orbit of the commuting involutions $g_5(x_1) = \tau_6 - \tau_5 - x_1$ and $g_6(x_1) = \tau_6 - x_1$, closing in the Klein 4-group $V_4 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ of size 4 and block-diagonalizing into two $2 \times 2$ blocks $B_\pm(a) \succ 0$, with determinant-graded inverse $(P_{0,\mathrm{odd}}^{-1})_{ij} = \det(\gamma_{ij})(P_{0,\mathrm{even}}^{-1})_{ij}$ on $O(1) = \mathbb{R} \rtimes \{\pm 1\}$.
  2. **Theorem 2 (Exact Triple Structural Coincidence at $a_{\star\star\star\star\star} = \frac{3}{2}\log 2 = \frac{1}{2}\log 8 \approx 1.0397207708$)**: Simultaneous threshold where $2b = \log 2$ (end of the 3-island isometric identity $P_b L_2^2 P_b = \frac{13}{4}I$), $2a = \log 8$ ($m = 8 = 2^3$ prime-power entry), and $x_6 = s_3 = \log(16/15) \approx 0.0588915178$ (merging partitions to $K = 46$ subintervals and $M_{\mathrm{prime}} = 11$ prime step vectors).
  3. **Theorem 3 (Courant–Fischer 2-Mode Deflated Trace Theorem)**: For any positive compact self-adjoint operator $T \succeq 0$ and 2-dimensional subspace $U_2 = \operatorname{span}\{u_1, u_2\}$ with orthonormal basis $(u_1, u_2)$, $\lambda_1(T) \le \operatorname{Tr}(T) - \mu_2(C_2)$, where $C_2 = (\langle u_m, T u_n\rangle)_{m,n=1}^2$.
  4. **Theorem 4 (Universal Prime-2 Dyadic Poisson Kernel Collapse for All $a > 0$)**: The infinite prime-2 dyadic preconditioner $L_{2,\infty} = I + 2\sum_{k=1}^\infty 2^{-k/2} T_{k\log 2}$ collapses the infinite $p=2$ prime-power series identically to a single nearest-neighbor tridiagonal shift $\frac{5\log 2}{2}I + \frac{\sqrt{2}\log 2}{2}S_{\log 2}$ for every support radius $a > 0$.
- [`verify_three_island_horizon.py`](./verify_three_island_horizon.py): Deterministic 384-bit ball arithmetic (`flint.ctx.prec = 384`) verification script with exact `SymReal` symbolic cut-point algebra ($\mathbb{Q} + \sum_{p \in \{2,3,5,7\}} \mathbb{Q}\log p$, zero decimal tolerances; `pyright` clean: `0 errors, 0 warnings`).
- [`verification.json`](./verification.json): Full machine-readable output (`sha256=3f8c384812d748cb84adea492600859022c74ebc647f68ee172e1eee8ebf2cc3`, zero `numpy`/`scipy`/`mpmath` imports).
- [`../all-vector-positivity-three-island-horizon-2026-10-15-v1.html`](../all-vector-positivity-three-island-horizon-2026-10-15-v1.html), [`../all-vector-positivity-three-island-horizon-2026-10-15-v2.html`](../all-vector-positivity-three-island-horizon-2026-10-15-v2.html), and [`../all-vector-positivity-three-island-horizon-2026-10-15-v3.html`](../all-vector-positivity-three-island-horizon-2026-10-15-v3.html): Styled HTML reports (`v1` and `v2` preserved untouched; `v3` updated with exact `SymReal` cut-point algebra and `.contains(0)` identity checks).

---

## 2. Summary of 384-Bit `flint.arb` Certified Checkpoints

| Checkpoint | $a$ (mid) | $b = a - \log 2$ | $\Delta\alpha$ | $\xi_{\Delta\alpha}$ | $K$ | $M_{\mathrm{prime}}$ | $\operatorname{Tr}(T_{\mathrm{even}})$ | $\mu_2(C_2)$ | $\mathcal{T}_{\mathrm{even}}^{\mathrm{defl}} = \operatorname{Tr} - \mu_2$ | $\mathcal{T}_{\mathrm{odd}}(a)$ | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `a_1.015` | `1.0150000000` | `0.3218528194` | `0.30` | `8.4863334740` | `51` | `13` | `1.0157811440` | `0.0208868911` | `0.9948942529 < 1` | `0.8686815881 < 1` | **CERTIFIED** |
| `a_1.025` | `1.0250000000` | `0.3318528194` | `0.30` | `8.4863334740` | `52` | `13` | `1.0201039754` | `0.0241042493` | `0.9959997261 < 1` | `0.9244456663 < 1` | **CERTIFIED** |
| `a_1.032` | `1.0320000000` | `0.3388528194` | `0.35` | `8.9209441395` | `53` | `13` | `1.0255919138` | `0.0293312953` | `0.9962606185 < 1` | `0.9538547120 < 1` | **CERTIFIED** |
| `a_half_log8` | `1.0397207708` | `0.3465735903` | `0.35` | `8.9209441395` | `46` | `11` | `1.0300268903` | `0.0320721764` | `0.9979547138 < 1` | `0.9991578524 < 1` | **CERTIFIED** |

---

## 3. Reproducibility

```bash
pyright audits/all-vector-positivity-three-island-horizon-2026-10-15-v1/verify_three_island_horizon.py
.venv/bin/python audits/all-vector-positivity-three-island-horizon-2026-10-15-v1/verify_three_island_horizon.py
```

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
