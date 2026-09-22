# v1.46 — exact lattice identity and scoped minorant obstruction

**Exact identities and proved implications, with numerical illustrations
kept separately under `evidence/diag_beta_lattice_identity/`. G2 and RH
remain open. No new window, head, Weil-tail metric or zero enclosure.**

## NS-26: finished

`prop:v146-beta-explicit` gives the unconditional shifted Perron formula
for the exact beta_a. Its archimedean/log-derivative/lower-limit block
cancels by the functional equation, without RH. The remaining terms are
the complete zero sum, trivial zeros and the strict-cutoff endpoint;
a finite zero prefix retains an explicit Perron remainder.

The saved cutoffs 9,16,36,64 are integers. The endpoint term is
+Lambda(x)/sqrt(x) cos(xi log x); dropping it changes the answer.
The lattice phase gives alternation, but its cosine and sine envelopes
vary. Equal crests and exact quarter-integer zeros are not identities.
The zero-frequency amplitude is a weighted arithmetic remainder, not
psi(x)-x. The naive zero sum omits the endpoint and trivial terms,
shifted denominators and finite-sum remainder, and confuses amplitude
with crest-minus-trough.

All forty old low-frequency locations and fourteen deep-trough/centroid
locations at lambda=4,8 were reproduced against the unchanged original
symbol. The analytic sum uses symmetric height/Perron ordering. The
finite numerical evaluation uses Gaussian Perron residues, epsilon=.025,
and exact desmoothing to the original sharp cutoff. Sufficient empirical
counts of positive zeros (plus conjugates) are 83/83/80/80 at the ten
low samples for lambda=3/4/6/8, and 530/609 for the selected deep samples
at lambda=4/8. All corresponding residuals are below 1.5e-7 at both
precisions. These counts are sample- and convention-specific, not sharp-sum
counts or interval certificates. The reference run uses 1200 positive
zeros, checks 1000-to-1200 stability, and checks the finite zero count.
The three-decimal legacy output is checked by rounding; 1e-6 agreement
is against recomputation. Full float NS-22 trough depths agree within
7e-13. Two binding centroids lie where beta is positive, so centroids
are not silently relabelled as trough locations.

This is the explicit formula restated, including at the deep troughs.
It supplies no new positivity or cofinal zero-spacing/density theorem.

## NS-27: scoped bounds proved; proposed closure not established

For a finite step minorant m, eta(m) is the negative spectral floor of
P F* m F P, not the norm of F*(beta-m)F. The correct packet bounds are

    eta(m) >= [(b+B)c_{a,u}(E) - B]_+

when m<=-b on E and m<=B globally, and

    eta(m) >= [c delta - Q]_+

when beta-m>=delta on E and an admissible unit packet has E-mass>=c
and original Weil energy<=Q. Positive spill/original energy cannot be
omitted. A two-value countermodel shows that depth growth and a fixed
concentration fraction alone do not imply divergent eta; it is not a
counterexample for the arithmetic beta.

For carrier a*omega>=10*pi, a cosine packet has mass at least 7/10 on a
full-cell-width mirrored band and 11/25 on a half-cell-width band. If
its source overlap is <=1/20, the projected bounds are 3/5 and 3/8.
The fixed-window overlap cost is explicit; the known source convergence
makes it vanish cofinally. Odd sine packets obey the same uncompressed
bounds and have no constraint from the even source. A single half-cell's
even concentration norm is <0.509, so the diagnostic 0.6-0.8 for the whole
negative set cannot be used for an isolated half-cell.

For K distinct values, a proved conditional bound is

    eta(m) >= [c D_a/(2K) - Q]_+.

It assumes a source-admissible bounded-energy packet whose pushforward
Fourier-mass distribution under beta dominates (c/D_a) dt throughout
[-D_a,0]. Uniform c>0 and Q<infinity would give the requested cofinal
linear level-count obstruction using the unconditional D_a->infinity.
Neither this arithmetic distribution nor the bounded packet energy is
provided by v1.37 or by the finite diagnostics. For the particular
nonpositive J-trough lobe-floor minorant one does have eta>=d_{J+1};
cofinal divergence then needs the corresponding trough multiplicity.
J arbitrary weighted sets can have 2^J values; set count is not level count.

The route therefore remains **blocked, not closed**. The weighted
concentration proposition is still a valid sufficient criterion.
This is a gap in the obstruction proof, not a failure of the object.

Actual build: **232 pages; 0 undefined references; 0 duplicate references;
0 overfull boxes.** The new Python diagnostics report 0 errors and 0 warnings.

## Incremental record

- `beta_lattice_identity.tex`: exact identity and initial numerical discussion.
- `beta_lattice_deep_checks.tex`: deep samples, convention and zero counts.
- `step_minorant_scope.tex`: explicit packet bounds, conditional level theorem,
  countermodel and missing arithmetic hypotheses.
- `scope_review.md`: internal algebra, scope and quantifier audit.
- `provenance.json`: hashes of new diagnostics and unchanged source inputs.
- `build_report.json`: actual final build counts and source hash.
- `research-report-2026-09-21-v1.html`: user-facing report.

The two NS-1 evidence groups remain OPEN; this work does not recover their
original scripts. Verify with `python3 tools/verify_manifest.py v146` and
build with `./manuscript/build.sh` from the repository root.
