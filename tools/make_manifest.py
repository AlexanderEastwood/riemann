#!/usr/bin/env python3
"""Generate or refresh a version manifest.

Usage:  python3 tools/make_manifest.py v137 [--note "..."]

Walks evidence/<version>/ plus the live manuscript and writes
manifest/v1.NN_manifest.json with a sha256 for every artifact.
Keeps the existing schema: a top-level "files" list of
{path, size_bytes, sha256}. Any prior manifest's non-"files" keys
are preserved, so hand-written provenance and validation blocks survive.
"""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def dotted(version: str) -> str:
    """v137 -> v1.37"""
    v = version.lstrip("v")
    return f"v{v[0]}.{v[1:]}" if "." not in v else f"v{v}"

def git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return ""

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("version", help="evidence directory name, e.g. v137")
    ap.add_argument("--note", default=None)
    a = ap.parse_args()

    ev = ROOT / "evidence" / a.version
    if not ev.is_dir():
        print(f"error: {ev.relative_to(ROOT)} does not exist", file=sys.stderr)
        return 2

    # Evidence only. The live manuscript is deliberately NOT included: it is
    # rewritten every version, so listing it would make every prior version's
    # manifest report a spurious MISMATCH. Manuscript versions are pinned by
    # git tags (v1.NN), which is the right primitive for that.
    targets = sorted(p for p in ev.rglob("*") if p.is_file())

    files, total, oversize = [], 0, []
    for p in targets:
        n = p.stat().st_size
        total += n
        if n > 100 * 1024 * 1024:
            oversize.append((str(p.relative_to(ROOT)), n))
        files.append({"path": str(p.relative_to(ROOT)),
                      "size_bytes": n, "sha256": sha256(p)})

    out = ROOT / "manifest" / f"{dotted(a.version)}_manifest.json"
    doc = {}
    if out.exists():
        try:
            doc = json.loads(out.read_text())
        except json.JSONDecodeError:
            doc = {}
    doc["manuscript_revision"] = dotted(a.version)
    doc["base_commit"] = git("rev-parse", "HEAD")
    doc["files"] = files
    doc["file_count"] = len(files)
    doc["total_bytes"] = total
    if a.note:
        doc["note"] = a.note
    out.write_text(json.dumps(doc, indent=1) + "\n")

    print(f"{out.relative_to(ROOT)}: {len(files)} files, {total/1048576:.1f} MB")
    for path, n in oversize:
        print(f"  *** OVER 100 MB, GitHub will reject: {path} ({n/1048576:.1f} MB)")
    return 1 if oversize else 0

if __name__ == "__main__":
    raise SystemExit(main())
