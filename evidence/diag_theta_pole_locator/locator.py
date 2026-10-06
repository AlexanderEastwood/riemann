"""Bounded, preregistered DIAGNOSTIC; sampled winding is not a zero certificate.

Run controls before any original evaluation. Original mode needs the separate
explicit --original-approved flag, and never changes the registered rectangle.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import time
from typing import Any, Callable

import mpmath as mp


Number = Any  # mpmath has no shipped static type declarations.
Evaluator = Callable[[Number, int, bool], dict[str, Any]]
GRID_SIZE = 9
CELL_CAP = 4
STEP_CAP = 12
DISCOVERY_SECONDS = 90 * 60


@dataclass(frozen=True)
class Rectangle:
    """Rational decimal/string coordinates, converted at active precision."""

    x0: str
    x1: str
    y0: str
    y1: str

    def point(self, i: int, j: int) -> Number:
        """Return a vertex of the fixed grid."""
        x0, x1, y0, y1 = map(mp.mpf, (self.x0, self.x1, self.y0, self.y1))
        return mp.mpc(x0 + (x1 - x0) * i / 8, y0 + (y1 - y0) * j / 8)


ORIGINAL_BOX = Rectangle("0.125", "2", "0.125", "0.625")
CONTROL_BOX = Rectangle("0.7", "0.72", "0.7", "0.72")


def real_text(value: Number) -> str:
    """Store enough digits for the current working precision."""
    return str(mp.nstr(value, mp.mp.dps))


def complex_text(value: Number) -> dict[str, str]:
    """Serialize a complex mpmath quantity without a binary64 conversion."""
    return {"re": real_text(mp.re(value)), "im": real_text(mp.im(value))}


def unpack_complex(value: dict[str, str]) -> Number:
    """Read an archived point at the current working precision."""
    return mp.mpc(value["re"], value["im"])


def safe_json(value: Any) -> Any:
    """Keep evaluator metadata JSON compatible without dropping precision."""
    if isinstance(value, dict):
        return {str(k): safe_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [safe_json(v) for v in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if hasattr(value, "imag") and value.imag != 0:
        return complex_text(value)
    return real_text(value)


class BudgetExceeded(RuntimeError):
    """The registered discovery time cap has elapsed."""


class Recorder:
    """Evaluation log and shared wall-clock guard, including replay."""

    def __init__(self, evaluator: Evaluator, seconds: float = DISCOVERY_SECONDS) -> None:
        self.evaluator = evaluator
        self.start = time.monotonic()
        self.seconds = seconds
        self.calls: list[dict[str, Any]] = []

    def evaluate(self, z: Number, bits: int, replay: bool, purpose: str) -> dict[str, Any]:
        """Record every requested evaluation; failed calls remain visible."""
        if time.monotonic() - self.start >= self.seconds:
            raise BudgetExceeded("90-minute discovery budget exhausted; stop, no enlargement")
        item: dict[str, Any] = {"z": complex_text(z), "bits": bits,
                                "replay": replay, "purpose": purpose}
        self.calls.append(item)
        started = time.monotonic()
        try:
            result = self.evaluator(z, bits, replay)
            for key in ("m", "c", "dm"):
                if key not in result:
                    raise ValueError(f"evaluator omitted {key}")
                if not mp.isfinite(abs(result[key])):
                    raise ValueError(f"nonfinite evaluator {key}")
            item["values"] = {key: complex_text(result[key]) for key in ("m", "c", "dm")}
            item["metadata"] = safe_json({k: v for k, v in result.items() if k not in ("m", "c", "dm")})
            return result
        except Exception as error:
            item["error"] = f"{type(error).__name__}: {error}"
            raise
        finally:
            item["elapsed_seconds"] = time.monotonic() - started


def sample_cell(i: int, j: int, grid: dict[tuple[int, int], dict[str, Any]]) -> dict[str, Any]:
    """Four-corner sampled winding/ranking, deliberately not a boundary proof."""
    corners = [grid[i, j], grid[i + 1, j], grid[i + 1, j + 1], grid[i, j + 1]]
    values = [corner["m"] for corner in corners]
    scale = max(map(abs, values))
    smallest = min(map(abs, values))
    cscale = max(abs(corner["c"]) for corner in corners)
    undefined = scale == 0 or smallest <= mp.power(2, -mp.mp.prec / 2) * scale
    winding = None if undefined else mp.fsum(mp.arg(values[(k + 1) % 4] / values[k]) for k in range(4)) / (2 * mp.pi)
    winding_integer = 0 if winding is None else int(mp.nint(winding))
    return {"i": i, "j": j, "sampled_winding": winding,
            "rounded_winding": winding_integer,
            "corner_ratio": mp.mpf(0) if scale == 0 else smallest / scale,
            "m_scale": scale, "c_scale": cscale,
            "winding_unresolved": undefined}


def serialize_cell(cell: dict[str, Any]) -> dict[str, Any]:
    """Preserve cell ranking inputs and the sampled-winding warning."""
    return {key: (real_text(value) if key in ("sampled_winding", "corner_ratio", "m_scale", "c_scale") and value is not None else value)
            for key, value in cell.items()}


def refine_cell(recorder: Recorder, box: Rectangle, cell: dict[str, Any], bits: int,
                replay: bool) -> dict[str, Any]:
    """At most 12 center-started Newton evaluations, staying in the chosen cell."""
    i, j = cell["i"], cell["j"]
    lower, upper = box.point(i, j), box.point(i + 1, j + 1)
    z = (lower + upper) / 2
    steps: list[dict[str, Any]] = []
    stop = "step_cap"
    last: dict[str, Any] | None = None
    for index in range(STEP_CAP):
        last = recorder.evaluate(z, bits, replay, f"cell_{i}_{j}_step_{index}")
        mscale = cell["m_scale"]
        ratio = abs(last["m"]) / mscale if mscale else mp.inf
        steps.append({"iteration": index, "z": complex_text(z),
                      "m": complex_text(last["m"]), "c": complex_text(last["c"]),
                      "relative_m_residual": real_text(ratio)})
        if ratio < mp.power(2, -40):
            stop = "residual_threshold"
            break
        if last["dm"] == 0:
            stop = "zero_sampled_derivative"
            break
        delta = last["m"] / last["dm"]
        accepted = False
        for halvings in range(17):
            candidate = z - delta / mp.power(2, halvings)
            if lower.real <= candidate.real <= upper.real and lower.imag <= candidate.imag <= upper.imag:
                accepted = True
                break
        if not accepted:
            stop = "newton_step_leaves_cell_after_16_halvings"
            break
        if candidate == z:
            stop = "roundoff_stagnation"
            break
        if index + 1 < STEP_CAP:
            z = candidate
    if last is None:
        raise RuntimeError("no refinement sample")
    return {"i": i, "j": j, "bits": bits, "stop": stop, "steps": steps,
            "endpoint": complex_text(z), "m": complex_text(last["m"]),
            "c": complex_text(last["c"]), "m_scale": real_text(cell["m_scale"]),
            "c_scale": real_text(cell["c_scale"]),
            "cell_diagonal": real_text(abs(upper - lower))}


def compare_replays(first: dict[str, Any], second: dict[str, Any]) -> dict[str, Any]:
    """Diagnostic labels only; samples never prove numerator separation."""
    z1, z2 = unpack_complex(first["endpoint"]), unpack_complex(second["endpoint"])
    m1, m2 = unpack_complex(first["m"]), unpack_complex(second["m"])
    c1, c2 = unpack_complex(first["c"]), unpack_complex(second["c"])
    ms1, ms2 = mp.mpf(first["m_scale"]), mp.mpf(second["m_scale"])
    cs1, cs2 = mp.mpf(first["c_scale"]), mp.mpf(second["c_scale"])
    diagonal = mp.mpf(second["cell_diagonal"])
    roots_small = ms1 > 0 and ms2 > 0 and abs(m1) / ms1 < mp.power(2, -40) and abs(m2) / ms2 < mp.power(2, -40)
    root_agreement = abs(z1 - z2) <= mp.power(2, -32) * diagonal
    numerator_large = cs1 > 0 and cs2 > 0 and abs(c1) / cs1 > mp.power(2, -20) and abs(c2) / cs2 > mp.power(2, -20)
    numerator_agreement = max(cs1, cs2) > 0 and abs(c1 - c2) <= mp.power(2, -32) * max(cs1, cs2)
    promising = bool(roots_small and root_agreement and numerator_large and numerator_agreement)
    label = ("approximate_root_with_sampled_numerator_separation_certificate_needed" if promising else
             "approximate_root_numerator_unresolved_no_pole_claim" if roots_small and root_agreement else
             "inconclusive_no_stable_approximate_root")
    return {"i": first["i"], "j": first["j"], "classification": label,
            "promising_for_certificate": promising, "root_residuals_small": bool(roots_small),
            "root_agreement": bool(root_agreement), "numerator_samples_large": bool(numerator_large),
            "numerator_replay_agreement": bool(numerator_agreement),
            "endpoint_difference": real_text(abs(z1 - z2))}


def locate(evaluator: Evaluator, box: Rectangle, budget_seconds: float = DISCOVERY_SECONDS) -> dict[str, Any]:
    """One initial grid, four cells maximum, then the same cells at 256 bits."""
    recorder = Recorder(evaluator, budget_seconds)
    result: dict[str, Any] = {"status": "running", "diagnostic_only": True,
                              "box": vars(box), "protocol_version": 1,
                              "grid_size": GRID_SIZE, "cell_cap": CELL_CAP,
                              "step_cap": STEP_CAP, "precisions_bits": [128, 256],
                              "calls": recorder.calls}
    try:
        with mp.workprec(128):
            grid = {(i, j): recorder.evaluate(box.point(i, j), 128, False, f"grid_{i}_{j}")
                    for i in range(GRID_SIZE) for j in range(GRID_SIZE)}
            cells = [sample_cell(i, j, grid) for i in range(8) for j in range(8)]
            ranked = sorted(cells, key=lambda cell: (-abs(cell["rounded_winding"]), cell["corner_ratio"], cell["i"], cell["j"]))
            chosen = ranked[:CELL_CAP]
            result["all_cells"] = [serialize_cell(cell) for cell in cells]
            result["selected_cells"] = [serialize_cell(cell) for cell in chosen]
            first = [refine_cell(recorder, box, cell, 128, False) for cell in chosen]
            result["first_refinements"] = first
        with mp.workprec(256):
            replay_grid: dict[tuple[int, int], dict[str, Any]] = {}
            for cell in chosen:
                i, j = cell["i"], cell["j"]
                for vertex in [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]:
                    if vertex not in replay_grid:
                        replay_grid[vertex] = recorder.evaluate(box.point(*vertex), 256, True, f"replay_corner_{vertex[0]}_{vertex[1]}")
            replay_cells = [sample_cell(cell["i"], cell["j"], replay_grid) for cell in chosen]
            result["replay_cells"] = [serialize_cell(cell) for cell in replay_cells]
            second = [refine_cell(recorder, box, cell, 256, True) for cell in replay_cells]
            result["second_refinements"] = second
            result["comparisons"] = [compare_replays(a, b) for a, b in zip(first, second)]
        result["status"] = "completed_bounded_diagnostic"
    except Exception as error:
        result["status"] = "inconclusive_stopped"
        result["error"] = f"{type(error).__name__}: {error}"
    result["elapsed_seconds"] = time.monotonic() - recorder.start
    result["evaluation_count"] = len(recorder.calls)
    result["warning"] = "No sampled winding, approximate root, or numerator sample is a certificate. No witness means inconclusive, not zero-free or PD."
    return result


def control_evaluator(removable: bool) -> Evaluator:
    """The two matched controls share the exact same denominator."""
    def evaluate(z: Number, bits: int, replay: bool) -> dict[str, Any]:
        m = z**4 + 1
        return {"m": m, "c": m * mp.exp(-z**2) if removable else mp.mpc(1),
                "dm": 4 * z**3, "exact_formula_control": True,
                "requested_bits": bits, "replay": replay}
    return evaluate


def run_controls() -> dict[str, Any]:
    """Exercise the actual pipeline, including cancellation-sensitive labels."""
    started = time.monotonic()
    pole = locate(control_evaluator(False), CONTROL_BOX)
    removable = locate(control_evaluator(True), CONTROL_BOX, DISCOVERY_SECONDS - (time.monotonic() - started))
    pole_seen = any(item["promising_for_certificate"] for item in pole.get("comparisons", []))
    removable_root_seen = any(item["root_residuals_small"] and item["root_agreement"] for item in removable.get("comparisons", []))
    removable_wrongly_flagged = any(item["promising_for_certificate"] for item in removable.get("comparisons", []))
    return {"diagnostic_only": True, "passed": pole_seen and removable_root_seen and not removable_wrongly_flagged,
            "pole_control": pole, "removable_control": removable,
            "checks": {"uncancelled_control_promising": pole_seen,
                       "removable_denominator_root_located": removable_root_seen,
                       "removable_wrongly_flagged_as_uncancelled": removable_wrongly_flagged},
            "elapsed_seconds": time.monotonic() - started}


def main() -> None:
    """Write a reproducible diagnostic JSON; default is controls only."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", action="store_true")
    parser.add_argument("--original-approved", action="store_true")
    parser.add_argument("--budget-seconds", type=float, default=DISCOVERY_SECONDS,
                        help="Remaining registered discovery budget, including prior control/implementation time")
    parser.add_argument("--controls-path", type=Path, default=Path(__file__).with_name("controls.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 0 < args.budget_seconds <= DISCOVERY_SECONDS:
        parser.error("remaining budget must be positive and at most 5400 seconds")
    if args.original:
        if not args.original_approved:
            parser.error("original evaluations require parent approval after preregistration/controls")
        try:
            controls = json.loads(args.controls_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            parser.error(f"matching completed controls are required: {error}")
        if not controls.get("passed") or controls.get("checks") != {
            "uncancelled_control_promising": True,
            "removable_denominator_root_located": True,
            "removable_wrongly_flagged_as_uncancelled": False,
        }:
            parser.error("both matched controls must have passed before original mode")
        for name in ("pole_control", "removable_control"):
            record = controls.get(name, {})
            if (record.get("protocol_version") != 1 or record.get("box") != vars(CONTROL_BOX)
                    or record.get("status") != "completed_bounded_diagnostic"):
                parser.error("control records do not match this protocol and rectangle")
        from theta_eval import evaluate
        payload = locate(evaluate, ORIGINAL_BOX, args.budget_seconds)
        payload["controls_path"] = str(args.controls_path)
        payload["remaining_budget_seconds_at_start"] = args.budget_seconds
    else:
        payload = run_controls()
    output = args.output or Path(__file__).with_name("original.json" if args.original else "controls.json")
    if args.original and output.resolve() == args.controls_path.resolve():
        parser.error("original output must preserve the matched control archive")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "status": payload.get("status"),
                      "controls_passed": payload.get("passed"), "evaluation_count": payload.get("evaluation_count")}, indent=2))


if __name__ == "__main__":
    main()
