"""API prime-chain control screen; numerical samples are not certificates."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from types import ModuleType
from typing import Any

import mpmath as mp

BASE = "9db64fdfdc1237005c071f777088291df254ac72"
ROOT = Path(__file__).resolve().parents[2]


def control_module() -> tuple[ModuleType, str]:
    data = subprocess.check_output(
        ["git", "show", f"{BASE}:controls/davenport_heilbronn.py"], cwd=ROOT
    )
    module = ModuleType("pinned_control")
    exec(compile(data, "pinned_control.py", "exec"), module.__dict__)
    return module, hashlib.sha256(data).hexdigest()


def number(value: Any) -> str:
    return str(mp.nstr(value, 35))


def poisson(radius: Any, cosine: Any) -> Any:
    return (1 - radius * radius) / (1 - 2 * radius * cosine + radius * radius)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.dps
    module, source_hash = control_module()
    dh = module.screen(
        lambda function, kernel: None,
        "Prime-chain bounds imply first-window kernel exclusion",
        sample_domain="Every prime; all theta; complete fixed-window Weil family",
        applicability="Different conductor, gamma/poles and coefficient object: not the stipulated original prime-chain family.",
        applicable=False,
    )
    radius = 1 / mp.sqrt(2)
    epsilon = mp.mpf(1) / 100
    lower = (1 - radius) / (1 + radius)
    upper = 1 / lower
    samples = []
    for k in range(65):
        theta = mp.pi * k / 64
        cosine = mp.cos(theta)
        original = poisson(radius, cosine)
        changed = original - 2 * epsilon * cosine
        samples.append({
            "k": k, "theta_over_pi": f"{k}/64",
            "original": number(original), "changed": number(changed),
            "lower_slack": number(changed - lower),
            "upper_slack": number(upper - changed),
        })
    lower_slack = min(mp.mpf(row["lower_slack"]) for row in samples)
    upper_slack = min(mp.mpf(row["upper_slack"]) for row in samples)
    result = {
        "classification": "Diagnostic screen of retained chain bounds; not a Weil-form or first-zero certificate",
        "reviewed_commit": BASE, "dps": args.dps, "control_sha256": source_hash,
        "Davenport_Heilbronn": dh,
        "NS100_NS101": "Not applicable: their alterations do not preserve the literal original prime/gamma/pole family.",
        "NS57_matched_control": {
            "epsilon": "1/100", "delta_2": number(-epsilon * mp.log(2)),
            "modified_w_2": number(mp.log(2) * (radius - epsilon)),
            "all_other_weights": "unchanged", "constant_chain_coefficient": 1,
            "original_lower_bound": number(lower), "original_upper_bound": number(upper),
            "minimum_sampled_lower_slack": number(lower_slack),
            "minimum_sampled_upper_slack": number(upper_slack),
            "sampled_bounds_pass": bool(lower_slack > 0 and upper_slack > 0),
            "exact_geometric_recursion": "not retained: only the first 2-chain coefficient changes",
            "first_zero": "Inherited analytic NS57 theorem; no window location, eigenvector or certificate computed",
        },
        "samples": samples,
        "scope": "Any full-domain comparison requires separate exact reasoning. No negative original Weil direction or API closure is claimed.",
    }
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"output": str(args.output), "dps": args.dps,
                      "NS57_bounds_pass": result["NS57_matched_control"]["sampled_bounds_pass"],
                      "minimum_lower_slack": number(lower_slack),
                      "minimum_upper_slack": number(upper_slack)}))


if __name__ == "__main__":
    main()
