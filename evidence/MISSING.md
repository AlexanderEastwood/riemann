# Evidence availability ledger

Updated 2026-09-21. **Two of the four tracked evidence groups remain OPEN.**
Recovery of the original v1.26 bundle resolved the two λ=4 evidence gaps;
it did not resolve the later λ=5 or concentration-evidence gaps.

| Evidence group | Status | Available evidence or remaining gap |
| --- | --- | --- |
| v1.25 complete even λ=4 certificate: `g2_simultaneous` | RESTORED | [58 original files](v126/g2_simultaneous/), including frozen witnesses, verifiers and saved complete residual ingredients, restored from the original v1.26 bundle. These files also match the original v1.25 bundle. |
| v1.26 complete odd λ=4 certificate: `g2_odd_complement` | RESTORED | [51 original files](v126/g2_odd_complement/), including complement and directional witnesses, verifiers, saved reports and the exact shared-head check. |
| λ=5 disproof evidence through v1.28 | OPEN | `g2_lambda5_transfer` and `g2_block_metric` remain absent. Recover the original frozen protocols, exact dyadic counterwitnesses, 320/448-bit reports and independent signed-index verifiers. The unchanged `10^-8 D` metric failure is the v1.27 checkpoint; the separate signed-block comparison failure is v1.28. Neither is restored by the v1.26 bundle. |
| v1.31–v1.34 concentration evidence and diagnostics | OPEN | The original [v1.31 weighted-concentration report](v131/g2_weighted_concentration_report.md) is partially restored with [provenance](v131/recovery_provenance.json). Its scripts, saved outputs and complete adversarial evidence remain absent; so do the original `g2_schatten_no_go`, `g2_nested_commutator` and `g2_primitive_transport` evidence sets. Recover their original scripts, saved outputs, candidate/proof reports and adversarial reviews, including `certify_beta4_negative.py`, `certify_scaled_commutator.py` and `test_primitive_transport.py`. The finite diagnostics and the claimed rigorous interval/rational checks must retain their distinct scopes. |

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
