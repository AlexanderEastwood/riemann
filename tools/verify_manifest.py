#!/usr/bin/env python3
"""Verify artifacts against a manifest.

Usage:  python3 tools/verify_manifest.py v137 [--all]

Exit 0 only if every listed file is present with a matching sha256.
Paths that a manifest records at a pre-reorganization location are
reported as RELOCATED rather than MISSING when the basename is found
under evidence/ or manuscript/.
"""
import argparse, hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def find_moved(rel: str, version: str = ""):
    """Locate a file a manifest records at a pre-reorganization path.

    Prefers the longest matching path TAIL, so that a bare basename cannot
    match an unrelated copy nested inside another version's inputs.
    """
    parts = Path(rel).parts
    best = None
    for base in ("manuscript", "log", "manifest", "audits", "evidence"):
        root = ROOT / base
        if not root.is_dir():
            continue
        for cand in root.rglob(Path(rel).name):
            if not cand.is_file():
                continue
            cp = cand.relative_to(ROOT).parts
            n = 0
            while n < min(len(parts), len(cp)) and parts[-1 - n] == cp[-1 - n]:
                n += 1
            # prefer the evidence directory of the manifest's own version
            same_version = 1 if version and f"evidence/{version}/" in str(
                cand.relative_to(ROOT)).replace("\\", "/") + "/" else 0
            key = (same_version, n)
            if best is None or key > best[0]:
                best = (key, cand)
    return best[1] if best else None

def check(mf: Path) -> bool:
    doc = json.loads(mf.read_text())
    version = "v" + mf.name.split("_")[0].lstrip("v").replace(".", "")
    files = doc.get("files", [])
    ok = miss = moved = bad = 0
    for ent in files:
        rel, want = ent.get("path"), ent.get("sha256")
        p = ROOT / rel
        if not p.exists():
            alt = find_moved(rel, version)
            if alt is None:
                print(f"  MISSING    {rel}"); miss += 1; continue
            p, moved = alt, moved + 1
            print(f"  RELOCATED  {rel} -> {p.relative_to(ROOT)}")
        if want and sha256(p) != want:
            print(f"  MISMATCH   {p.relative_to(ROOT)}"); bad += 1
        else:
            ok += 1
    print(f"{mf.name}: {ok} ok, {moved} relocated, {miss} missing, {bad} mismatched"
          f"  [{len(files)} listed]")
    return miss == 0 and bad == 0

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("version", nargs="?")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    md = ROOT / "manifest"
    if a.all:
        mfs = sorted(md.glob("v*_manifest.json"))
    elif a.version:
        v = a.version.lstrip("v")
        dot = f"v{v[0]}.{v[1:]}" if "." not in v else f"v{v}"
        mfs = [md / f"{dot}_manifest.json"]
    else:
        ap.error("give a version or --all")
    allok = True
    for mf in mfs:
        if not mf.exists():
            print(f"{mf.name}: not found"); allok = False; continue
        allok &= check(mf)
    return 0 if allok else 1

if __name__ == "__main__":
    raise SystemExit(main())
