# Where the certified window sits relative to published work

This file exists because the manuscript's window parameter `lambda` is not
the parameter used in the published literature, and a referee cannot tell
from either side whether the `W_4 >= 0` certificate is beyond or inside
the published state of the art. The translation below settles it.

Only published (arXiv) prior art is compared here. Self-published and
repository-only work is deliberately excluded.

## The translation

The semilocal window `lambda > 1` corresponds to test functions supported
multiplicatively in `[lambda^{-1}, lambda]`, i.e. in the logarithmic
coordinate to support half-width

    a = log lambda

The published literature parameterizes directly by that half-width (Zhu
writes it `L`; the classical Yoshida / Connes–Consani bound is stated as
`supp f ⊂ [-(log 2)/2, (log 2)/2]`). So every result can be placed on one
axis:

| result | half-width `a` | `lambda = e^a` |
|---|---:|---:|
| classical Yoshida / Connes–Consani | 0.3466 | 1.414 |
| Zhu, arXiv:2608.24827, certified `L = 0.8` | 0.8000 | 2.226 |
| this manuscript, `lambda = 3` (`prop:v116-window-positive`) | 1.0986 | 3.000 |
| this manuscript, `lambda = 4` (`W_4 >= 0`, `prop:v126-full-window`) | **1.3863** | **4.000** |

**The `lambda = 4` certificate is at 1.73× the half-width of the
published Zhu window and 4× the classical range.** It is not subsumed on
reach.

The comparison is legitimate because the semilocal form `QW_lambda` and
the global Weil form agree on every test supported inside the window
(`prop:v121-cofinal-rh` relies on exactly this), so the two sides certify
the same object on the same functions.

## What each side establishes — they are not the same strength

| | Zhu (`a = 0.8`) | this manuscript (`a = 1.386`) |
|---|---|---|
| statement | two-sided **quantitative** enclosure `8.9e-18 <= lambda_min <= 2.27e-17` | **nonnegativity** `W_4 >= 0`; no ordinary spectral gap claimed |
| parity | both sectors; ground state simple and even | both sectors; ground state simple and even (`prop:v117-ground-order`, at `a = 1.099`) |
| method | one-stroke reduction to a single finite PSD matrix | structured inverse, simultaneous 17-column certificate, direction–complement gluing |
| arithmetic | interval | Arb ball arithmetic, 768–1280 bits, two-precision replay |

Zhu is stronger *in kind* (a certified two-sided gap) on a smaller window.
This manuscript is stronger *in reach*. Neither subsumes the other, and the
manuscript should say so rather than leave it to the reader.

The `LDL*` pivots and the invariant margin `1 - lambda_max(U, K)` recorded in
`evidence/v126/g2_simultaneous/` are **not** an ordinary-norm eigenvalue
bound and must not be quoted as one; see the scope string inside each
certificate JSON.

## A cross-check that validates both sides at once

Zhu's empirical law for the window infimum,

    -ln lambda_min(L) ~ 2 pi^2 N(T*) / ln N(T*),    T* = 2 pi e^{2L},

evaluated at this manuscript's windows and compared with the smallest
eigenvalue of the finite compression computed independently here:

| `lambda` | `a` | Zhu law predicts | computed compression `lmin` | ratio |
|---:|---:|---:|---:|---:|
| 3 | 1.0986 | 1.39e-39 | 3.64e-38 | 26× |
| 4 | 1.3863 | 2.07e-73 | 3.74e-72 | 18× |

Agreement to a factor of ~20 across 34 orders of magnitude, from an
asymptotic law. If the translation above were wrong the law would miss by
tens of orders, not a constant factor. This corroborates the coordinate
identification, the compression computation, and the law itself.

(Compression eigenvalues are diagnostics: `lmin` of a compression is an
*upper* bound on the operator infimum and certifies nothing. They are used
here only to check the translation.)

## The one no-go with published prior art

`prop:v125-cutoff-cost` proves the scalar diagonal far majorant needs a
remote cutoff `N+1 > L exp(M_phi/(1-c))` with `M_phi / lambda -> 1`, i.e.
`N ~ exp(e^a)` — doubly exponential in the half-width.

Zhu's abstract states that any one-stroke certificate must resolve
frequencies up to `2 pi e^{A_L}` with `A_L ~ 4 e^L` — the same doubly
exponential shape, drawn as the same conclusion ("why the positivity route
cannot reach RH unassisted"). Groskin, arXiv:2607.02828, gives the
corresponding brute-cutoff cost (`T ~ 10^{63}` at `c = 100`) for
Connes–van Suijlekom truncations, using cutoff-free interval `LDL^T` —
the same factorization technique used here.

The objects differ: Zhu bounds frequency resolution for a one-stroke
certificate; this manuscript bounds the remote cutoff for one specific
scalar majorant, and says explicitly that this is a cost of that majorant
rather than of every possible argument. But the result belongs to a
published family and should be cited as such, not presented as new.

No published prior art was found for: norm contraction
(`prop:v120-norm-counterexample`), Schatten / Hilbert–Schmidt summation
(`prop:v132-schatten`), reciprocal-band approximate commutation (v1.33),
or the unconditional divergence of the scalar signed-primitive budget
(`cor:v137-scalar-no-go`).

## Recommended structural differentiation

The certified-Weil-positivity literature now shares a house style
(certificate-first, "not a proof of RH", scoped no-gos, checksummed
witnesses), so tone does not distinguish this project. Two things would:

1. **A semantic lock.** A short, checkable statement pinning `QW_lambda`
   as assembled in `assembly_general.py` to the published
   Connes–Consani–Moscovici normalization (arXiv:2511.22755), by
   reproducing one of CCM's own §6 numerical values from this code. CCM
   ship no ancillary files, so that reproduction would be a citable
   contribution on its own and would let a reviewer trust the object
   without trusting the definitions.
2. **A named external reviewer** on `evidence/MISSING.md` and the
   certificate ledger. Self-review cannot reach a `REVIEWED` state.

## References

- Zhu, X., *Weil positivity in compact windows: a finite reduction,
  certified two-sided bounds, and a Landau–Widom decay law*,
  arXiv:2608.24827 (2026).
- Groskin, A., *A finite Guinand–Weil dictionary and archimedean tail
  order for the truncated Weil quadratic form*, arXiv:2607.02828 (2026).
- Connes, A., Consani, C., Moscovici, H., arXiv:2511.22755 (2025).
- Yoshida; Connes–Consani — the classical `(log 2)/2` positivity range.
