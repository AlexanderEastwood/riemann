# NS-47: exact Clifford representation; uniform floor still open

Classification: exact identities, proved implications with stated hypotheses,
and a named open input. No numerical illustration or certified computation is
claimed. G2 and RH remain open.

User assignment: use geometric algebra to construct a representation of the
existing complete Weil form that yields an ordinary lower bound uniform over
growing windows. The representation is constructed; the uniform estimate is
**not** obtained. A scoped obstruction to one global closed-square approach is
proved. This is a research checkpoint, not completion of the uniform-floor task.

## Result and exact scope

- The v1.50 identity yields explicit linear maps `D` (all positive continuous
  and prime edges) and `N` (centered variance and the negative odd pole), with
  `q[f] = ||Df||^2 - ||Nf||^2`. `D` is a closed, densely defined maximal edge
  operator. Its standard graded Dirac block squares to the edge energy, not
  to the complete Weil operator. An explicit Cl(1,1) module represents the
  signed pairing; its coefficient space is infinite dimensional.
- Uniform domination `||Nf||^2 <= ||Df||^2 + C||f||^2` is exactly the existing
  floor/CAE target. The range-contraction formulation is equivalent, not a
  proof. The negative channel grows at least exponentially in lambda squared
  on the v1.50 admissible tests. A fixed strict contraction is excluded by
  that same archived analytic argument, in both parity sectors.
- **Scoped closure:** no single ordinary-L2 closable factor `T` and bounded
  Hermitian remainder `B` represent the global form as `||Tf||^2 + <Bf,f>`.
  Dense cutoff radicals force `T` to be bounded; the fixed-support
  high-frequency form grows like log R. Separately, a one-sided comparison
  `q >= ||Tf||^2 - C||f||^2` forces a closable `T` to be bounded with norm at
  most sqrt(C). Neither statement disproves the floor or gives a physical
  negative direction.
- Fixed-window factors, factors that do not combine into one global
  ordinary-closable operator, and different metric completions are not
  excluded. They still require the actual uniform estimate and ordinary-norm
  transfer. The global positive factor of a successful contraction would
  necessarily be nonclosable in ordinary L2.

## Artifacts

- `representation.tex`: standalone proof fragment, owned by this task;
  labels use `ns47`, with no new manuscript version assigned.
- `bibitems.tex`: the Holzmann primary reference for the standard operator
  construction; the fragment reuses the manuscript's existing `Douglas` item.
- `ns47-clifford-weil-report-2026-09-21-v1.html`: styled research report.
- `algebra-checks.mac` and `algebra-checks-output.txt`: seven exact algebra
  checks, not interval certificates or evidence for the analytic bound.
- `validate.sh`: reproducible temporary splice of this fragment and its new
  bibliography item into the integration-base manuscript; runs the real
  manuscript build without editing the live source.
- `validation.txt`: build provenance and counts.
- `baseline-build-output.txt` and `integration-build-output.txt`: actual
  build output, including intermediate passes; reported reference counts
  refer to the final LaTeX logs.
- `review-2026-09-21-v1.html`: independent review and resolved findings.
- `SHA256SUMS`: task artifact hashes, excluding the checksum file itself.

Base: `24f4ab55f623a894b3d1bc532ba0b3cedac3f286`, as coordinated with Astra
Main (PR #21, v1.52 candidate). Standalone task claim: `9608ca4`.
Branch: `codex/ns47-clifford-weil`. No dependency on the concurrent NS-46
fine-lattice work. No manuscript, map, or release-manifest change is made here;
version integration is reserved to the coordinator. Task hashes pin this
unversioned evidence until that integration generates the release manifest.

## Replay

From the repository root:

```sh
maxima --no-init --quit-on-error --very-quiet \
  --batch=evidence/ns47_clifford_weil/algebra-checks.mac
./manuscript/build.sh
evidence/ns47_clifford_weil/validate.sh
shasum -a 256 -c evidence/ns47_clifford_weil/SHA256SUMS
```

The temporary splice is placed before the bibliography purely to validate
typesetting and references. Its appendix numbering is not a proposed final
manuscript location. The coordinator must choose a semantic anchor when
integrating. No new window, tail metric, RH assumption or G2 claim enters.
