# G2 research and reproduction — full manuscript v1.14

Completed September 21, 2026. Starting point: the complete v1.13 manuscript and persistent research log. The resulting complete manuscript has 119 pages, 32 main sections, two appendices, 376 unique labels, and the unchanged 72 historical claim dispositions.

## Results integrated into the paper

1. **Proposition 20.19, pages 63–64:** the exact all-index Weil matrix is the correct logarithmic diagonal plus a bounded discrete-Hilbert commutator. This identifies the canonical semilocal Weil operator, its logarithmic operator/form domains, compact resolvent, and finite-Fourier operator core. The physical realization is identified using the actual trigonometric form-core theorem of CCM, not by choosing a new boundary extension. Periodic BV sources lie in its operator domain, with Fourier graph convergence at each fixed window. The separate arithmetic generator in Section 18 remains conditional.
2. **Proposition 20.20 and equation (174), pages 64–65:** an explicit positive lower bound for the sufficiently remote Fourier complement and an exact inverse-action Schur residual identity. The bound treats the negative pole direction, prime shifts, and archimedean off-diagonal separately. Its absolute prime estimate is expensive and does not establish the signed low-frequency Schur inequality.
3. **Lemmas 21.5–21.6 and Proposition 21.7, pages 81–84:** the unchanged ordinary projection at `N_lambda=ceil(lambda^8(1+2 log lambda))` recovers the physical endpoint of the exact repaired two-mode source with relative error `O(1/lambda)`. A finite entire extension is small on an exterior interval in L2. Degree `O(c)` polynomial approximation and Markov bounds control endpoint jets through order `ceil(c)`, where `c=2 pi lambda^2`. The exact arithmetic function jumps are separated, including the nearest threshold. The smooth compact repair is restored without taking its high derivatives. This is an analytic asymptotic proof, with no numerical threshold at lambda=3.
4. **Corollary 21.8, page 84:** a separately proved high-frequency coefficient bound puts weak G1 on the same literal projected vector, uniformly over ambient Fourier cuts in the established weighted test norm. It does not establish an unweighted operator residual, a growing source-block estimate, spectral ordering, or G2.

All first-slot-linear conventions, physical endpoint factors, source normalization, Fourier cut, logarithmic diagonal, and sampler graph defects remain explicit. No withdrawn transfer claim is reinstated.

## What adversarial research changed

The endpoint proof survived two independent internal analytic reviews. The operator/core proof and tail constants also survived review. A wording issue in the sine-series proof was corrected: the exponential factor must first be discarded before applying decreasing integral comparison. The weak-G1 consequence was reviewed separately; it is not inferred from endpoint recovery alone.

The adverse report constructs an explicit co-Poisson family with transforms equal to polynomial multiples of xi. Smooth truncations give arbitrarily large fixed-dimensional near-null subspaces. Thus no fixed positive absolute complement gap can remain after removal of a fixed-rank source family. This does not disprove uniqueness of the actual ground state with a shrinking gap. A perturbation of one prime coefficient also shows why a uniform positivity argument cannot tolerate arbitrary fixed unsigned arithmetic errors.

The endpoint-directed source-to-ground resolvent pairing remains a different problem from Fourier endpoint recovery. Ordinary norm proximity does not control it at an exponentially small endpoint. These countermodels and failed shortcuts are recorded in the research reports, not promoted into an RH proof.

## Reproduce the full document

From the cumulative bundle root, run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex
```

The TeX file is self-contained apart from standard TeX packages. The two insertion files are readable development excerpts; the full TeX does not require them as inputs. The cumulative bundle preserves all earlier scripts and certificates.

## Reproduce the new scalar interval check

Install Python-FLINT 0.9.0 with its bundled FLINT 3.6.0, then run from the bundle root:

```bash
python3 g2_deep_next/check_tail_constant.py
```

The script uses 256-bit Arb arithmetic and rigorous integration of the analytically regularized zero-mode archimedean integral. It writes `g2_deep_next/tail_constant_check.json`. Strict interval comparisons prove

`17.69849 < C_3^tail < 17.69851`, and `Gamma_(3,50000000) > 1.0797`.

No 50-million-mode matrix is assembled. This is only an evaluation of the scalar constant in the analytic tail theorem. It does not bridge the existing N=64 matrix certificate to the continuum and proves no sign for the intervening low modes or their coupling. Earlier exact matrix and source certificates are retained without optional reruns.

## Source audit

The research report checks CCM's physical form core and canonical operator, CvS's finite real-zero mechanism and continuum hypotheses, Suzuki's small-window results, and recent compact-window computation methods. No consulted primary theorem supplies the missing uniform large-window source-to-ground or signed arithmetic estimate. Direct source links and exact scope distinctions appear in `primary_source_research.md`.

## Remaining target

The next concrete proof target is a signed lower bound for the effective low block `F-B* T^(-1) B`, allowing a growing near-null source block. A rigorous inverse-action approximation `Z` yields the computable residual correction `R* T^(-1) R`, with `R=B-TZ`; the manuscript gives the exact identity. To advance G2, its lower error must tend to zero along growing windows, or a separate endpoint/strip-normalized source-to-ground theorem must be proved. The alternative independent evaluator-shell sign estimate at p=2 remains open.

**Technical prerequisites were closed. No G2 sign gap or RH proof was obtained.**
