"""Replay preserved September 29 audit scripts from any Git checkout.

Only the location of the pinned Git source is overridden. Original scripts
and evidence remain byte-for-byte unchanged, including historical paths.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys
from types import ModuleType


def load(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("audit_replay", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("test", choices=["prime-scaling", "jacobi-product"])
    parser.add_argument("--dps", type=int, choices=[50, 80], required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    if args.test == "prime-scaling":
        source = root / "audits/prime-scaling-admission-2026-09-29-v1/screen_projection.py"
        module = load(source)
        setattr(module, "REPO", root)
        extra: list[str] = []
    else:
        source = root / "audits/jacobi-product-admission-2026-09-29-v1/screen_product.py"
        module = load(source)
        setattr(module, "REVIEW", str(root))
        extra = ["--witness", "0.25", "14", "--direct"]
    previous = sys.argv
    try:
        sys.argv = [str(source), "--dps", str(args.dps), "--output", str(args.output), *extra]
        module.main()
    finally:
        sys.argv = previous


if __name__ == "__main__":
    main()
