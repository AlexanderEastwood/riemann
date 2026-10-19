# Evidence availability ledger

Updated 2026-10-18 (`NS-1` / `NS-38` historical recovery remains **OPEN**; for the scoped standalone paper `manuscript/standalone_weil_certificates_and_obstructions_v4.tex` and the 274-page standalone monograph `manuscript/standalone_weil_certificates_and_obstructions_monograph_v4.tex` [with `v1`–`v3` preserved], all unrecovered historical `v1.27–v1.34` diagnostic files are omitted and replaced by the archived certificates and analytical proofs mapped below).

| Evidence group | Status | Available evidence or remaining gap |
| --- | --- | --- |
| v1.25 complete even λ=4 certificate: `g2_simultaneous` | RESTORED | [58 original files](v126/g2_simultaneous/), including frozen witnesses, verifiers and saved complete residual ingredients, restored from the original v1.26 bundle. These files also match the original v1.25 bundle. |
| v1.26 complete odd λ=4 certificate: `g2_odd_complement` | RESTORED | [51 original files](v126/g2_odd_complement/), including complement and directional witnesses, verifiers, saved reports and the exact shared-head check. |
| λ=5 disproof evidence through v1.28 | OPEN (historical originals unrecovered; omitted from scoped standalone paper) | Historical `g2_lambda5_transfer` ($N=16$) and `g2_block_metric` files remain unarchived. For the scoped standalone paper, the $\lambda=5$ comparison closures use only the archived replacement certificates [NS-44](ns44_metric_replay/) (`prop:v152-tail-comparison`, $\lambda=5$ `10^-8 D` tail comparison failure in both parities) and [NS-45](ns45_block_replay/) (`prop:v152-block-comparison`, $\lambda=5, N=25$ dyadic block-norm comparison failure in both parities), indexed in [v1.52](v152/) at `320/448` bits. |
| v1.31–v1.34 concentration evidence and diagnostics | OPEN (historical originals unrecovered; omitted from scoped standalone paper) | Historical scripts and finite-grid diagnostics (`g2_schatten_no_go`, `g2_nested_commutator` degree-four check, `g2_primitive_transport` finite tables) remain unarchived; the [v1.31 report](v131/g2_weighted_concentration_report.md) is a partial recovery only. The scoped standalone paper omits those unarchived diagnostics and relies only on the analytical proofs in `manuscript/fixed_space_prime_action_v1.tex` (`prop:v131-concentration`, `prop:v132-schatten`, `prop:v132-flat-top`, `prop:v133-leakage`, `prop:v133-noncommute` degree-two proof, `prop:v134-disjoint`, `prop:v134-primitive`), the `192/320`-bit Arb and `128/256`-bit digamma-series replacement certificates for `prop:v132-global-index` ($\beta_{\log 4}(1) < -3/5$) in [bounds-six-agent-2026-09-30-v1](../audits/bounds-six-agent-2026-09-30-v1/README.md), and the archived cofinal scalar drawdown divergence (`cor:v137-scalar-no-go`) in [v1.37](v137/). |


## What the recovery establishes

The [original v1.26 ZIP](https://github.com/AlexanderEastwood/riemann/releases/tag/v1.26-evidence)
and its complete extracted snapshot are available. All 468 extracted files
match the archive byte-for-byte. Final proof gates using the saved
ingredients, witness bindings and exact rational shared-head equality were
replayed successfully. The full residual assemblies were not rerun during
publication. RESTORED therefore records availability, not completion of a
new independent audit of every computation.

See the [recovery record](../manifest/README_v126_evidence_recovery.md)
and [per-file checksums](../manifest/v1.26_evidence_recovery.json).

## What remains unresolved

The later 207,224,098-byte v1.34 cumulative ZIP remains unavailable. The
v1.26 release cannot contain the later evidence in the two OPEN rows.
Manuscript statements, research-log descriptions and newer proof files do
not substitute for those original witnesses and diagnostics.

Keep each row OPEN until its original evidence and dependencies have been
recovered, checked against its stated provenance and made accessible in
the repository or an immutable release asset. Recovering these files would
close an availability gap; any new verification must be recorded separately.
This ledger does not certify completeness of every historical archive.
G2 and RH remain open.


## September 21 follow-up (NS-1, v1.41)

Both later evidence groups remain **OPEN**. A fresh search checked all four
available local ZIPs, matching script paths across repository refs, and the
saved project records. No original missing script or witness was recovered.
GitHub exposes only the already restored v1.26 evidence release. The earlier
v1.34 library download failure remains recorded; no library-download
connector is available in this session to retry it. Archive hashes and exact
search scope are in [the availability record](v141/ns1_recovery_status.json).
An accessible original archive or extracted evidence with provenance is
still required. The v1.31 report remains a partial recovery only.

## September 21 follow-up after v1.43

**Classification: open input; availability search, not a certificate.**
NS-1 remains blocked and both evidence groups remain **OPEN**. No missing
original script, witness or saved output was recovered in this follow-up.

The search refreshed all remote refs and checked matching paths in their
history, then checked current GitHub release assets. Only the original
v1.26 ZIP and its checksum are released. Local filename searches covered
Downloads, Desktop, Documents (including the ChatGPT research directory
and Codex workspaces), CloudStorage, Codex attachments, repository
worktrees and temporary files. Saved research/recovery transcripts supplied
references, not the absent originals. The four previously inspected ZIPs
remain the available local bundles; this follow-up did not repeat their
byte-level validation.

The recorded source in [the v1.31 provenance](v131/recovery_provenance.json)
is `fixed_space_prime_action_v1_34_bundle.zip`, library file
`libfile_386d5bdf90848191b485e716d0205c09`, version `37`, recorded size
`207224098` bytes. These identifiers are historical metadata, not a fresh
verification that the remote binary is retrievable. No ChatGPT-library
connector is available in the current session; its accessible web session
is signed out. The historical HTTP 502 was not replayed. An accessible
original archive, or the six named original directories with their shared
dependencies and provenance, is required to continue recovery.

The public repository already contained v1.43 at the time of this search.
This follow-up changes only the recovery ledger and task status. It does
not close MAJOR M1, change the manuscript, regenerate historical evidence,
or claim a new verification. G2 and RH remain open.


## September 22 disposition (NS-38)

**Classification: evidence-availability disclosure, not recovery or a new certificate.**
For **each of the two original groups**, the chosen action is explicit disclosure.
No original witness, verifier or output was recovered or regenerated. Earlier OPEN
entries above describe the search history; they are not a claim of archive availability.

- **λ=5 group:** the abstract, both reported computational propositions, their
  verification accounts, downstream route summaries and both appendices now state
  that originals are not archived. The integer Rayleigh arithmetic printed in v1.28
  is available; its comparison to actual blocks still depends on missing witnesses.
  Recorded hashes are historical metadata, not checks against retrieved originals.
- **Concentration group:** local diagnostic discussions and each reproduction appendix
  state that original scripts, outputs and reviews are not archived. The reported
  rational β(log 4, 1) enclosure is separated from the analytic negative-index
  implication conditional on it. The stronger degree-four commutator check is marked
  unavailable; the printed degree-two proof remains the actual available argument.
  The v1.31 report-only recovery is preserved and is not described as full recovery.

The same sweep records **additional companion gaps**: the v1.29
`g2_capacity_candidate` register/review/recomputation artifacts and v1.30
`g2_continuum_cancellation` report, `test_continuum_symbol.py` and output
are **NOT ARCHIVED**. The underlying v1.24 λ=3 source certificate and complete
v1.29/v1.30 manuscript identities are present; they do not stand in for the missing
companion artifacts. V1.50 uses the printed identities, not those absent files.

**V1.35 is not an absent scientific evidence set.** All five original scientific
files under `evidence/v135/` match hashes in the legacy v1.35 manifest. The same is
true of the five scientific files in each of v1.36 and v1.37; obsolete directory
names in the manuscript now point to these actual paths. The legacy v1.35 manifest checker also reports two publication paths missing and
a mutable research log mismatch in the current tree. **Their exact original bytes
are already archived in tag `v1.35`**: `fixed_space_prime_action_v1.tex`,
`v1_revision_notes.md` and `RH_G1_G2_research_log.md` each match the corresponding
legacy manifest hash. See the [tag provenance](ns38_archival_disclosure/v135_publication_tag_provenance.json).
These are path/relocation findings, not unavailable historical content. V1/v2 of
the NS-38 report incorrectly called the two snapshots unavailable; v3 corrects
that statement after checking the tag. Historical manifests are not rewritten.


The [claim-by-claim changes](ns38_archival_disclosure/claim_changes.json),
[present-file hash comparison](ns38_archival_disclosure/present_proof_hashes.json)
and [versioned report](ns38_archival_disclosure/ns38-archival-disclosure-2026-09-22-v3.html)
record this disposition. Recovery remains an open input. The archival overclaim
is corrected; availability has not been restored. No manuscript version bump is
made for NS-38 alone, and no original numerical gate was replayed.

## Fresh replacement certificates (NS-44/45, v1.52)

New exact dyadic witnesses and fresh 320/448-bit verifiers now establish failure
of the stipulated lambda=5 `10^-8 D` tail comparison and the N=25 tested dyadic
block-norm comparison in both parities. See [NS-44](ns44_metric_replay/) and
[NS-45](ns45_block_replay/), indexed by [v1.52](v152/). These are replacement
certificates, not recovered v1.27/v1.28 artifacts; the historical displayed
ratios, four-block tables, and original protocols remain unarchived. The first
evidence group therefore remains **recovery OPEN**, while these two precisely
scoped mathematical comparison closures now have current replayable evidence.
The concentration-era group is unchanged and remains **recovery OPEN**.

## September 30 forward note: beta replacement evidence (NS38)

The [six-agent audit](../audits/bounds-six-agent-2026-09-30-v1/README.md)
now supplies **REPLACEMENT evidence** for the numerical premise of
`prop:v132-global-index`: `beta_(log4)(1)<-3/5`. Direct Arb at 192/320 bits
and an independent digamma-series enclosure at 128/256 bits confirm the
historically reported interval; the third review records 37 passing
replay/integrity checks. Only the direct method certifies the narrower
45-place interval. This is a new implementation of the same fixed claim.

The beta certificate does NOT transfer to the physical lambda=4 form:
its tests are not compactly supported in that physical window.
It supplies evidence for the existing full-line even-sector negative-index
implication, including fixed finite homogeneous constraints.

The original `certify_beta4_negative.py` and its output remain **NOT ARCHIVED**.
This note does not close either original-recovery row, recover the other
concentration-era scripts, or change RH/G2 or the cofinal signed floor.
The manuscript is preserved; this forward note qualifies its historical
statement that the numerical premise could not then be replayed.

The preserved audit notes refer to earlier local coefficient working files
that are not included in this publication. Those provenance references are
not an assertion that the files are archived in this public repository.
The [forward dependency note](../audits/bounds-six-agent-2026-09-30-v1/publication/weighted-dependency.md)
states the full inherited coefficient corollary from public NS78 needed by
the present audit; the certificate replay does not depend on those local files.

## October 18 scoping note: replacement mapping for the standalone paper (`v4` / `monograph_v4`) vs. historical recovery (`OPEN`)

Per user direction on 2026-10-18, the scoped standalone extraction (`manuscript/standalone_weil_certificates_and_obstructions_v4.tex` and `manuscript/standalone_weil_certificates_and_obstructions_monograph_v4.tex`, with `v1`–`v3` preserved) omits all unrecovered historical `v1.27–v1.34` diagnostic tables and relies exclusively on archived replacement certificates and self-contained analytical proofs (verified by `audits/standalone-paper-v4-verification-2026-10-18-v1/verify_standalone_v4.py`, `61/61` checks passing):

1. **$\lambda = 5$ comparison closures:** Uses only the archived `320/448`-bit `flint.arb` certificates in [NS-44](ns44_metric_replay/) (`prop:v152-tail-comparison`) and [NS-45](ns45_block_replay/) (`prop:v152-block-comparison`), indexed in [v1.52](v152/). The historical `v1.27` ($N=16$) and `v1.28` four-block diagnostic tables are omitted.
2. **Concentration and operator no-go propositions:** Uses only the self-contained analytical proofs in `manuscript/fixed_space_prime_action_v1.tex` (`prop:v131-concentration`, `prop:v132-schatten`, `prop:v132-flat-top`, `prop:v133-leakage`, `prop:v133-noncommute` degree-two proof, `prop:v134-disjoint`, `prop:v134-primitive`), the `192/320`-bit Arb and `128/256`-bit digamma-series replacement certificates for `prop:v132-global-index` ($\beta_{\log 4}(1) < -3/5$) in [bounds-six-agent-2026-09-30-v1](../audits/bounds-six-agent-2026-09-30-v1/README.md), and the archived cofinal drawdown divergence (`cor:v137-scalar-no-go`) in [v1.37](v137/).
3. **Historical provenance (`OPEN`):** Choosing replacement evidence for a scoped standalone paper does not constitute historical recovery. The `207,224,098`-byte bundle `fixed_space_prime_action_v1_34_bundle.zip` remains unrecovered, so both historical original-recovery rows in this ledger remain **OPEN**. `G2` and `RH` remain open.


