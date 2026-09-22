# v1.47 — NS-29: zero level distribution and packet coverage

**Exact identities, proved implications with explicit hypotheses, and named
open inputs. No new numerical experiment or certificate. G2 and RH remain open.**

The outcome is a reduction to **Corrected Zero Level Distribution (ZLD)**,
plus an independent bounded-energy packet-coverage input. Neither is proved
uniformly on a cofinal family. This is not a proof of the minorant closure.

What had to change: cumulative lower bounds for {beta < -t} must be replaced
by lower bounds for the measure of every interval of levels. Fourier density
must be bounded below on those level bands, not only on some positive fraction
of the frequency interval. An upper density bound has the wrong direction.
A counterexample to the cumulative inference and an exact coarea identity
make these distinctions explicit.

If F(t1)-F(t2) >= kappa*X*(t2-t1)/D on [0,theta*D], and an admissible unit
packet has density >=b/X on a set meeting at least alpha of each level band,
with original energy <=Q, the weighted density is >=2*b*alpha*kappa/D. Thus

    eta(m) >= [b*alpha*kappa*theta^2*D/K - Q]_+.

The separation is sufficient, not necessary for the original weighted
condition: a single suitably populated trough could suffice. Uniformity over
arbitrarily enlarged heads is impossible because the negative set is bounded
at each fixed window. ZLD includes a prescribed cofinal head-size rule.

The complete zero field equals beta exactly with the endpoint and trivial
terms retained. ZLD is the displayed band-measure condition for that field,
with a prescribed N(a), X=2*pi*N/L, and global D_a. It is a new name for an
open input, not a known conjecture or a consequence of RH. The primary-source
assessment examines zero counting, zero density, Landau-Gonek sums and pair
correlation. No reduction from those results or standard conjectures to ZLD
is established; its logical strength is not classified as weaker/equivalent
or independent of RH. The manuscript gives the exact missing statement.

v1.37 supplies unconditional depth divergence. The new local derivative
bound supplies width only with a window-dependent cost. The RH probe gives
an explicit cumulative bound that can vanish at a fixed fraction of D.
Neither implies the needed uniform band density. The head range may not
reach the global depth at all.

Packet spread remains substantive even if ZLD is granted. Smooth pulses
with Fourier density >=b/X on [0,X] have energy log X + O(1); their prime
lags vanish exactly. They therefore fail the uniform-Q requirement.
This does not rule out other packets. Source projection and its pointwise
and energy costs are explicit; odd parity has the same distribution
argument without the even-source constraint.

The failure is of the proposed derivation of a uniform obstruction, not
of the physical form or the valid weighted concentration inequality.
Both (a) arithmetic distribution and (b) packet coverage/energy remain
open. The route stays **blocked**, not closed. NS-28 is untouched.

## Incremental record

- `level_distribution_zero_statement.tex`: manuscript insert, three proved
  propositions, exact coarea/zero identities, and the named open input.
- `references.tex`: six primary bibliographic entries, no repository sources.
- `scope_review.md`: internal quantifier, algebra and classification audit.
- `provenance.json`: unchanged proof-input hashes.
- `build_report.json`: actual build and reference counts.
- `research-report-2026-09-21-v1.html`: user-facing section 9 report.

Build: **237 pages; 0 undefined references; 0 duplicate references;
0 overfull boxes.** No interval gate was run because no numerical bound
was introduced. The two NS-1 evidence groups remain OPEN.
