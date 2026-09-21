# Reproducing complete fixed-window positivity — manuscript v1.16

The full manuscript is 129 pages. Propositions 20.22–20.26 establish the weighted prime bound, diagonal tail inverse comparison, remote moment enclosure, signed certificate and complete fixed-window coercivity at lambda=3. G2 for unbounded windows and RH remain open.

## Environment

The certified arithmetic used Python 3.12, python-flint 0.9.0 and FLINT 3.6.0. Install python-flint in a suitable Python environment if it is not already present. The certificate itself uses only Python's standard library and python-flint. Earlier exploratory pilots additionally use NumPy/SciPy, but they are not dependencies of the final verifier.

Run from the bundle's `g2_schur_directional` directory:

```bash
python3 certify_weighted_prime_tail.py
python3 certify_infinite_schur.py --N 256 --M 512 --J 4096 --r 80 --parity even --bits 768 --diagonal --witness schur_witness_N256_M512_even_b768.json.gz
python3 certify_infinite_schur.py --N 512 --M 1024 --J 4096 --r 100 --parity odd --bits 768 --diagonal --witness schur_witness_N512_M1024_odd_b768.json.gz
```

For the independent precision replays, replace `--bits 768` by `--bits 896` while retaining each original 768-bit witness filename. Both replays have already passed and their reports are included. The witness files contain exact dyadic mantissa/exponent pairs, not rounded decimal approximations. The verifier checks that their entries remain exact at the chosen precision.

To generate a fresh witness from the verified intermediate solve, omit `--witness`. Positivity is checked after the result is frozen, so every intermediate residual remains in the calculation. Regenerating an identical witness is not required to establish positivity; replaying the supplied one makes the precise certified object reproducible.

The `weil_sequences_n4096_b768_k128.json` and corresponding 896-bit cache store outward enclosures of exact coefficients. `assembly.py` automatically recomputes them when absent. They may be renamed or removed in a separate reproduction directory to force fresh function evaluations. No cache contains an assumed positive sign or an omitted-tail assertion.

## Exact proof dependencies

1. The canonical Weil operator and its logarithmic operator/form domains are established in the retained v1.14 material. The Fourier finite sequences form a core.
2. The sharp archimedean and pole estimates are retained from v1.15; the weighted physical prime estimate strengthens their arithmetic constant.
3. The tail has the form lower bound `T>=diag(g_n)>0`, so its inverse is bounded above by the diagonal inverse. The base cut remains fixed in every loss term.
4. The exact dyadic lift Z gives `K=K_Z-R*T^(-1)R`. All finite residual rows through J4096 are computed with the true diagonal.
5. The remote moment inequality bounds every output row beyond J4096 with all parity factors included. No finite-matrix extrapolation occurs.
6. Interval LDL certifies strict positivity of both final finite lower matrices. The tail square completion then proves complete closed-form coercivity.

The two final parameter sets and hashes are recorded in `fixed_window_certificate_report.md`, and every positive pivot enclosure appears in the associated `infinite_schur_..._diagonal.json` report. A PASS is a fixed-window result for the stated sector. Both sectors are necessary for the asserted whole-space result. Pivot magnitudes are not spectral lower bounds.

## Scope of other files

`adversarial_schur_report.md` and `directional_tail_derivation.md` contain the analytic review and derivation. The proof inserts are integrated into the complete root LaTeX source. `schur_pilot_report.md`, the pilot JSON reports and the failed full-majorant reports preserve the exploration history. A negative pivot in those lower majorants does not establish that the true Weil form has a negative direction. The large pilot block caches were not retained because the supplied pilot code regenerates them; they are unnecessary for the final proof.

Only the original two exact witness archives are retained: the 896-bit replay witnesses have identical uncompressed hashes and need not be duplicated. All prior releases' reproducibility material remains in the cumulative bundle.

## Building the complete paper

At the bundle root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_space_prime_action_v1.tex
```

The verified output has 129 pages, 407 unique labels and no LaTeX warnings or unresolved references. All pages were rendered for review; the new proofs were also inspected at higher resolution. The next mathematical target and all remaining qualifications are recorded in `RH_G1_G2_research_log.md`.
