"""Compare the 1024- and 1280-bit scans: pointwise agreement within interval radii, identical sign-change sets and counts."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
a = json.load(open(HERE / "scan-1024bits.json"))
b = json.load(open(HERE / "scan-1280bits.json"))
assert a["grid"]["t"] == b["grid"]["t"]
va, vb, ra, rb = a["grid"]["F_mid"], b["grid"]["F_mid"], a["grid"]["F_rad"], b["grid"]["F_rad"]
worst_abs = max(abs(x - y) for x, y in zip(va, vb))
worst_rel = max(abs(x - y) / max(abs(x), abs(y)) for x, y in zip(va, vb) if max(abs(x), abs(y)) > 0)
overlap = all(abs(x - y) <= 2 * (p + q) + 1e-300 for x, y, p, q in zip(va, vb, ra, rb))
out = {
    "grid_points": len(va),
    "max_abs_difference_of_midpoints": worst_abs,
    "max_relative_difference_of_midpoints": worst_rel,
    "all_intervals_overlap": overlap,
    "sign_change_heights_identical": [m["sign_change_height"] for m in a["sign_changes"]] == [m["sign_change_height"] for m in b["sign_changes"]],
    "counts_identical": a["counts"] == b["counts"],
    "envelope_log10_identical_to_3dp": [x["log10"] for x in a["envelope_bands"]] == [x["log10"] for x in b["envelope_bands"]],
    "trial_rayleigh_rho_1024": a["trial_rayleigh_rho"], "trial_rayleigh_rho_1280": b["trial_rayleigh_rho"],
}
json.dump(out, open(HERE / "validation.json", "w"), indent=1)
print(json.dumps(out, indent=1))
