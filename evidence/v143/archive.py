"""Load the unchanged v1.42 complete-ground verifier from the archive."""
from __future__ import annotations
import importlib.util
from pathlib import Path
from types import ModuleType


COARSE_PATH = Path(__file__).resolve().parents[1] / "v142/certify_ground_zero.py"

def load_coarse() -> ModuleType:
    path = COARSE_PATH
    spec = importlib.util.spec_from_file_location("v142_ground_zero", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


coarse = load_coarse()
