# Evidence availability ledger

Updated 2026-09-22 (NS-38; fresh NS-44/45 distinction). **Both remaining groups are explicitly NOT ARCHIVED.**
The manuscript archival overclaims are corrected by disclosure; original recovery remains OPEN.
Recovery of the original v1.26 bundle resolved the two λ=4 evidence gaps;
it did not resolve the later λ=5 or concentration-evidence gaps.

| Evidence group | Status | Available evidence or remaining gap |
| --- | --- | --- |
| v1.25 complete even λ=4 certificate: `g2_simultaneous` | RESTORED | [58 original files](v126/g2_simultaneous/), including frozen witnesses, verifiers and saved complete residual ingredients, restored from the original v1.26 bundle. These files also match the original v1.25 bundle. |
| v1.26 complete odd λ=4 certificate: `g2_odd_complement` | RESTORED | [51 original files](v126/g2_odd_complement/), including complement and directional witnesses, verifiers, saved reports and the exact shared-head check. |
| λ=5 disproof evidence through v1.28 | NOT ARCHIVED; disclosure complete, recovery OPEN | `g2_lambda5_transfer` and `g2_block_metric` remain absent. Recover the original frozen protocols, exact dyadic counterwitnesses, 320/448-bit reports and independent signed-index verifiers. The unchanged `10^-8 D` metric failure is the v1.27 checkpoint; the separate signed-block comparison failure is v1.28. Neither is restored by the v1.26 bundle. |
| v1.31–v1.34 concentration evidence and diagnostics | NOT ARCHIVED; disclosure complete, recovery OPEN | The original [v1.31 weighted-concentration report](v131/g2_weighted_concentration_report.md) is partially restored with [provenance](v131/recovery_provenance.json). Its scripts, saved outputs and complete adversarial evidence remain absent; so do the original `g2_schatten_no_go`, `g2_nested_commutator` and `g2_primitive_transport` evidence sets. Recover their original scripts, saved outputs, candidate/proof reports and adversarial reviews, including `certify_beta4_negative.py`, `certify_scaled_commutator.py` and `test_primitive_transport.py`. The finite diagnostics and the claimed rigorous interval/rational checks must retain their distinct scopes. |

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
