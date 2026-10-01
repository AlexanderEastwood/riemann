"""Portable fixed-certificate replay without modifying the sealed historical files.

Run from any checkout containing the unchanged source manuscript. Only the
existing a=log4, xi=1 certificate is evaluated; this is not a candidate scan.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

import flint
from flint import arb, ctx, fmpq

AUDIT = Path(__file__).resolve().parents[1]
ROOT = AUDIT.parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rational(value: dict[str, str]) -> arb:
    return arb(fmpq(int(value['numerator']), int(value['denominator'])))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='New JSON output path, outside the sealed audit directory')
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(AUDIT) or output.exists():
        raise SystemExit('Choose a new output path outside the sealed audit directory.')
    if flint.__version__ != '0.9.0':
        raise SystemExit('This exact replay requires python-flint==0.9.0.')
    checks: dict[str, bool] = {}
    manifest = json.loads((AUDIT / 'manifest.json').read_text())
    for name, expected in manifest.items():
        path = (AUDIT / name).resolve()
        if not path.is_relative_to(AUDIT):
            raise SystemExit('Invalid manifest path.')
        checks[f'original:{name}'] = digest(path) == expected
    cert = AUDIT / 'certificate'
    direct_saved = json.loads((cert / '01-direct/outputs.json').read_text())
    series_saved = json.loads((cert / '02-independent/certificate.json').read_text())
    historical = json.loads((cert / '03-adversarial/replay.json').read_text())
    checks['historical_37_checks_recorded_pass'] = (
        len(historical['checks']) == 37 and all(historical['checks'].values()))
    manuscript = ROOT / 'manuscript/fixed_space_prime_action_v1.tex'
    checks['unchanged_manuscript_source'] = digest(manuscript) == direct_saved[
        'source_sha256']['manuscript/fixed_space_prime_action_v1.tex']
    if not all(checks.values()):
        raise SystemExit('Original record/source integrity failure; review before replay.')
    direct = load('beta_direct_public', cert / '01-direct/verify_beta.py')
    series = load('beta_series_public', cert / '02-independent/certify_series.py')
    direct_runs = [direct.evaluate(bits) for bits in (192, 320)]
    series_runs = [series.certify(bits) for bits in (128, 256)]
    for actual, saved in zip(direct_runs, direct_saved['runs'], strict=True):
        bits = actual['precision_bits']
        checks[f'direct_{bits}_all_numeric_fields_identical'] = actual == saved
        checks[f'direct_{bits}_historical_interval'] = actual['historical_reported_interval_verified']
        checks[f'direct_{bits}_threshold'] = actual['beta_strictly_below_minus_three_fifths']
    for actual, saved in zip(series_runs, series_saved['runs'], strict=True):
        bits = actual['bits']
        checks[f'series_{bits}_all_numeric_fields_identical'] = actual == saved
        checks[f'series_{bits}_gates'] = all(actual['checks'].values())
        ctx.prec = bits
        gamma = series.gamma_interval(series.GAMMA_TERMS)
        psi, _ = series.digamma_real(series.DIGAMMA_TERMS, gamma)
        continuum, _ = series.continuum_series(arb(16).log(), series.EXP_TERMS)
        prime_sum = sum((arb(p).log() / arb(m).sqrt() * arb(m).log().cos()
                         for m, p in series.strict_prime_powers(16)), arb(0))
        ball = psi - arb.pi().log() - 2 * prime_sum + 2 * continuum
        checks[f'series_{bits}_display_contains_actual_ball'] = bool(
            arb(actual['beta_interval']).contains(ball))
        ctx.prec = 384
        checks[f'series_{bits}_broad_rational_interval'] = bool(
            ball > arb(fmpq(-640150, 1000000)) and
            ball < arb(fmpq(-639904, 1000000)))
        for dr in direct_runs:
            dball = rational(dr['beta']['lower_dyadic']).union(
                rational(dr['beta']['upper_dyadic']))
            enclosure = dr['outward_rational_enclosure']
            checks[f'series_{bits}_contains_direct_{dr["precision_bits"]}'] = bool(ball.contains(dball))
            checks[f'direct_{dr["precision_bits"]}_strict_45_places'] = bool(
                dball > rational(enclosure['lower']) and dball < rational(enclosure['upper']))
    checks['strict_prime_powers'] = series.strict_prime_powers(16) == [
        (2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3), (11, 11), (13, 13)]
    for name, expected in manifest.items():
        checks[f'unmodified:{name}'] = digest(AUDIT / name) == expected
    result = {
        'purpose': 'Publication replay of one fixed existing certificate; no research candidate scan',
        'python_flint': flint.__version__,
        'source_sha256': digest(manuscript),
        'original_record_manifest_sha256': digest(AUDIT / 'manifest.json'),
        'checks': checks, 'all_pass': all(checks.values()),
        'direct_runs': direct_runs, 'series_runs': series_runs,
        'scope': 'REPLACEMENT evidence for NS38 / prop:v132-global-index only. The beta certificate does NOT transfer to the physical lambda=4 form: its tests are not compactly supported in that physical window. Both original-evidence recovery groups remain OPEN; RH/G2 and NB-GAIN remain open.',
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'all_pass': result['all_pass'], 'checks': len(checks),
                      'failed': [key for key, passed in checks.items() if not passed]}))
    if not result['all_pass']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
