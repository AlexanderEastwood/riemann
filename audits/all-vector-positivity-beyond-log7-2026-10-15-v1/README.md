# All-Vector Positivity Beyond $a = \frac{1}{2}\log 7$ up to the 3-Point Fiber Closure Horizon $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.007452$ (`2026-10-15-v1`)

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity across all test functions), the cofinal signed-arithmetic lower bound in the $B_2$/Stieltjes lane, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**. Nothing in this directory claims a proof of RH or global Weil positivity.

---

## Contents

- [`PROPOSAL.md`](PROPOSAL.md): Scope, falsifiability criteria, and lane (`KERNEL-API`).
- [`derivation.md`](derivation.md): Proof of the 3-Point Fiber Closure Theorem up to $a_{\star\star\star\star} = \frac{1}{2}\log(15/2) \approx 1.0074515103$ ($d_5 = x_6$ exact saturation), the Smooth 2-Mode Positive-Semidefinite Loewner Plancherel Minorant, and the Courant–Fischer 2-Mode Deflated Trace Theorem over $[0, \xi_{\Delta\alpha}]$ ($\alpha(\xi_{\Delta\alpha}) = \Delta\alpha = 0.25$, $\xi_{\Delta\alpha} \approx 8.0372408860$).
- [`verify_beyond_log7.py`](verify_beyond_log7.py): 384-bit `flint.arb` certification script with exact `SymReal` symbolic cut-point algebra ($\mathbb{Q} + \sum_{p \in \{2,3,5,7\}} \mathbb{Q}\log p$, zero decimal tolerances; `pyright` clean: `0 errors, 0 warnings`).
- [`verification.json`](verification.json): Deterministic 384-bit ball arithmetic certificate (`sha256=dcfc150ad4c29bbbf9fd94475347b5b5cc4bf7cad9489c7475898b53f404af1e`, `all_certified=True` in `83.647s`, zero `numpy`/`scipy`/`mpmath` imports).
- [`../all-vector-positivity-beyond-log7-2026-10-15-v1.html`](../all-vector-positivity-beyond-log7-2026-10-15-v1.html), [`../all-vector-positivity-beyond-log7-2026-10-15-v2.html`](../all-vector-positivity-beyond-log7-2026-10-15-v2.html), and [`../all-vector-positivity-beyond-log7-2026-10-15-v3.html`](../all-vector-positivity-beyond-log7-2026-10-15-v3.html): Styled HTML reports (v1 and v2 preserved untouched; v3 updated with exact `SymReal` symbolic cut-point algebra and pure ball arithmetic).

---

## Certified Summary Table (`PREC_BITS = 384`, $\Delta\alpha = 0.250$, $\xi_{\Delta\alpha} \approx 8.0372408860$)

| Landmark / Regime | $a$ | $b = a - \log 2$ | $(K_{\mathrm{sub}}, M_{\mathrm{prime}}, M_{\mathrm{pl}})$ | $\operatorname{Tr}(T_{\mathrm{even}})$ | $\mu_2(G_2^{-1}M_2)$ | $\mathcal{T}_{\mathrm{even}}^{\mathrm{defl}} = \operatorname{Tr} - \mu_2$ | $\mathcal{T}_{\mathrm{odd}}$ | $1 - \mathcal{T}_{\mathrm{even}}^{\mathrm{defl}}$ | Certified |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| $\tau_3 = \log(4/3)$ reflection saturation | $\log(8/3) \approx 0.98082925$ | $0.28768207$ | $(28, 7, 2)$ | $1.00252576$ | $0.01095257$ | $0.99157318 \pm 3.31\times 10^{-17}$ | $0.74217857 \pm 1.30\times 10^{-18}$ | $+0.00842682 > 0$ | **YES** |
| Simultaneous $m=3$ shift/refl + $m=7$ refl | $0.99000000$ | $0.29685282$ | $(41, 10, 2)$ | $1.00679590$ | $0.01279308$ | $0.99400282 \pm 2.33\times 10^{-17}$ | $0.77622783 \pm 1.33\times 10^{-18}$ | $+0.00599718 > 0$ | **YES** |
| **Unit-Support Landmark ($2a = 2.0$)** | $1.00000000$ | $0.30685282$ | $(40, 10, 2)$ | $1.01004310$ | $0.01493306$ | $0.99511004 \pm 5.80\times 10^{-17}$ | $0.81236072 \pm 1.30\times 10^{-18}$ | $+0.00488996 > 0$ | **YES** |
| **3-Point Fiber Closure Horizon ($d_5 = x_6$)** | $\frac{1}{2}\log(15/2) \approx 1.00745151$ | $0.31430433$ | $(46, 11, 2)$ | $1.00942901$ | $0.01665326$ | $0.99277575 \pm 5.57\times 10^{-17}$ | $0.83529956 \pm 1.31\times 10^{-18}$ | $+0.00722425 > 0$ | **YES** |

---

## Reproduction

```bash
pyright audits/all-vector-positivity-beyond-log7-2026-10-15-v1/verify_beyond_log7.py
.venv/bin/python audits/all-vector-positivity-beyond-log7-2026-10-15-v1/verify_beyond_log7.py
```

---

**Wall check:** The Riemann Hypothesis, G2 (global Weil positivity), the cofinal signed-arithmetic lower bound, and both historical missing-original evidence groups in `evidence/MISSING.md` remain **OPEN**.
