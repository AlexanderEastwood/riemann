"""Verify v1.52's incremental external artifacts and manuscript integration.

This checks archival integrity, not the mathematical interval gates. Replay
NS44/NS45 with their frozen verifiers to recompute those gates.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def main() -> None:
    """Fail on a missing/changed indexed artifact or an integration mismatch."""
    document = json.loads((HERE / "provenance.json").read_text())
    failures: list[str] = []
    for item in document["artifacts"]:
        path = ROOT / item["path"]
        if not path.is_file():
            failures.append(f"MISSING {item['path']}")
            continue
        payload = path.read_bytes()
        if len(payload) != item["size_bytes"]:
            failures.append(f"SIZE {item['path']}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            failures.append(f"HASH {item['path']}")
    fragment = (HERE / "route_selection.tex").read_text()
    manuscript = (ROOT / "manuscript/fixed_space_prime_action_v1.tex").read_text()
    if manuscript.count(fragment) != 1:
        failures.append("INTEGRATION: expected one exact v1.52 fragment")
    if (HERE / "comparison_replays.tex").read_text() not in fragment:
        failures.append("INTEGRATION: comparison statement differs")
    for name in ("ns44_metric_replay", "ns45_block_replay"):
        certificate = json.loads((ROOT / "evidence" / name / "certificate.json").read_text())
        for source, expected in certificate["source_sha256"].items():
            if hashlib.sha256((ROOT / source).read_bytes()).hexdigest() != expected:
                failures.append(f"CERTIFICATE SOURCE {source}")
        witness = ROOT / "evidence" / name / "witnesses.json"
        if hashlib.sha256(witness.read_bytes()).hexdigest() != certificate["witness_sha256"]:
            failures.append(f"CERTIFICATE WITNESS {name}")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"PASS: {len(document['artifacts'])} indexed artifacts; exact integration; certificate bindings")


if __name__ == "__main__":
    main()
