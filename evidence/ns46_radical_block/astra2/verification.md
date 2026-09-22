# NS-46 / Astra-2 internal verification record

Classification: analytic proofs and explicit open-input assessment. No numerical
illustration, certified computation, new finite window, or changed tail metric.

Ownership was assigned by the coordinator following Alex's explicit joint-work
request. Team claim commit: `0355edb`, based on `24f4ab5` (local v1.52 / PR21).
Astra-2 owns only this directory. No tracked files outside it were edited;
no commits, pushes, or branch switches were performed.

## Proof dependency

`complete_block_bounds.tex` uses the coordinator's
`evidence/ns46_radical_block/coordinator/finite_arc_gram.tex`, label
`lem:ns46-finite-arc`, reviewed at SHA256
`ed8d0093fb1a21e8f81857b4c3f053762a9d22a2a50d38313aec2237df1e701b`.
The finite-arc proof was independently checked: alternating bins give distinct
nodes, chord separation supplies the two factorials, Lagrange interpolation and
Parseval control arbitrary complex coefficients, and the factorial estimate has
the stated `4*pi*e` constant. No infinite-lattice hypothesis is involved.

The full residual proof uses the v1.35 Gaussian derivative tails and polarized
global radical identity, which are inherited manuscript inputs. It explicitly
controls the full cutoff loss using the tail integral of `1-chi^2`, and includes
the all-n prime rows and both pole integrals before Gram normalization.

For T=1 the tail exponent is `pi/(4*e^4) > 1/1000`. With the stated J,
`gamma^(-1/2) <= C sqrt(m) exp(3*lambda^2/10000)` eventually. The full column
aggregation then gives `C m exp(-7*lambda^2/10000)`, absorbed in
`C exp(-lambda^2/2000)`. These are eventual analytic comparisons; no numerical
threshold is certified. Gram and Weil eigenvalues are kept distinct.

## Fixed-spacing literature input

The permitted assisting agent handled the disjoint fixed-spacing question and
reported only; it made no file changes. Astra-2 checked the primary source:

- Xiannan Li and Maksym Radziwill, *The Riemann-zeta function on vertical
  arithmetic progressions*, arXiv:1208.2684v1, Theorem 4, printed p. 3.
  https://arxiv.org/pdf/1208.2684
- Source accessed 2026-09-22 UTC. It applies to every fixed positive progression
  step and every fixed real offset, unconditionally. No uniform quantitative
  threshold in those parameters is used here.
- The infinite Gram periodization and explicit two-alias orthogonality
  construction are proved directly in `fixed_lattice.tex`. The theorem is used
  only to exclude a zero periodization value. It is not needed for the dense
  finite block or its rank count.

`fixed_lattice.tex` and its bibliography addition are standalone companions,
not part of the coordinator's proposed v1.53 integration or dependencies of
the dense-block theorem. The temporary build included them only for checking.

## Build checks

The actual baseline `./manuscript/build.sh` completed at 265 pages and 0
undefined/duplicate references. A temporary copy outside the shared worktree
appended the coordinator's finite-arc lemma, `complete_block_bounds.tex`, and
`fixed_lattice.tex` before the bibliography, and the bibliography addition inside
the existing bibliography. Running the same build script produced 271 pages,
0 undefined/duplicate references, and 0 overfull boxes.

The harmless bibliography title hyphen was subsequently corrected to match the
primary source. It changes no label, citation key, formula, or proof.

These checks are not a live integration build or a new manuscript version.
The user-facing assessment is the separately versioned HTML file in this
directory. The coordinator remains responsible for integration, archival commit,
and any resulting version manifest.
