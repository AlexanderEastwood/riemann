# Higher-Order Wronskian–Transvectant Parseval Hierarchy & Quartic Log-Derivative Jet-Ring Obstruction (`2026-10-15-v1`)

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this directory claims a proof of RH or global Weil positivity.

---

## Contents

- [`PROPOSAL.md`](PROPOSAL.md): Scope, theorems, and falsifiability criteria (`ZERO-GEOMETRY` lane).
- [`derivation.md`](derivation.md): Proofs of Theorem 1 (Order-$2m$ Gauge-Invariant Transvectant / Wronskian Parseval Hierarchy & Hamburger–Stieltjes Hankel Positivity) and Theorem 2 (Exact Quartic Jet-Ring Decomposition of $\phi(u)^4(\log\phi)^{(4)}(u)$).
- [`verify_wronskian_hankel_hierarchy.py`](verify_wronskian_hankel_hierarchy.py): Exact rational jet-ring and 384-bit `flint.arb` verification script (`pyright` clean: `0 errors, 0 warnings`).
- [`verification.json`](verification.json): Deterministic 384-bit ball arithmetic certificate (`file_sha256=f9f42a23baf989ed7a8b9d4aedeaaff9422b1942943870336f28fa05da7a2c41`, `script_sha256=21678a56d798612914e2bee1f98ad264473c0bbbeecd51e4352b9eb24cd18824`, `all_certified=True` in `0.203s`).
- [`../higher-order-wronskian-hankel-hierarchy-2026-10-15-v1.html`](../higher-order-wronskian-hankel-hierarchy-2026-10-15-v1.html): Styled HTML report.

---

## Certified Summary Table (`PREC_BITS = 384`)

| Kernel Family | Slice $x$ | $\mu_0(x)$ | $\mu_2(x)$ | $\mu_4(x)$ | Turán $\Delta_2 = \mu_0\mu_4 - \mu_2^2$ | $\Delta_3 = \det\mathcal{H}_2(x)$ | $\Delta_4 = \det\mathcal{H}_3(x)$ | $\int \phi^4(\log\phi)^{(4)}e^{4xu}du$ | Max 3-Way Err |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `phi_RH` (Laguerre–Pólya) | $0.00$ | $1.959269$ | $4.967656$ | $22.406563$ | $+19.222883 > 0$ | $+2413.836 > 0$ | $+7.1398\times 10^6 > 0$ | $-21.259835$ | $8.47\times 10^{-113}$ |
| `phi_RH` (Laguerre–Pólya) | $0.25$ | $2.032274$ | $5.261363$ | $23.811644$ | $+20.709835 > 0$ | $+2713.703 > 0$ | $+8.4069\times 10^6 > 0$ | $-25.343111$ | $1.16\times 10^{-112}$ |
| `phi_NS101` (Off-Line Zero) | $0.00$ | $3.729237$ | $7.587878$ | $30.845960$ | $+57.456014 > 0$ | $+10221.547 > 0$ | $+4.0330\times 10^7 > 0$ | $-40.784160$ | $1.64\times 10^{-110}$ |
| `phi_NS101` (Off-Line Zero) | $0.25$ | $3.838962$ | $7.990483$ | $32.634319$ | $+61.434111 > 0$ | $+11420.702 > 0$ | $+4.7251\times 10^7 > 0$ | $-48.391685$ | $1.81\times 10^{-110}$ |
| `phi_DH` (Davenport–Heilbronn) | $0.00$ | $3.583259$ | $5.138726$ | $16.987718$ | $+34.464888 > 0$ | $+2902.383 > 0$ | $+4.3530\times 10^6 > 0$ | $-12.709928$ | $1.65\times 10^{-111}$ |
| `phi_DH` (Davenport–Heilbronn) | $0.25$ | $3.734786$ | $5.435523$ | $18.017262$ | $+37.745720 > 0$ | $+3346.061 > 0$ | $+5.2861\times 10^6 > 0$ | $-14.994979$ | $1.94\times 10^{-111}$ |

---

## Reproduction

```bash
pyright audits/higher-order-wronskian-hankel-hierarchy-2026-10-15-v1/verify_wronskian_hankel_hierarchy.py
.venv/bin/python audits/higher-order-wronskian-hankel-hierarchy-2026-10-15-v1/verify_wronskian_hankel_hierarchy.py
```

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
