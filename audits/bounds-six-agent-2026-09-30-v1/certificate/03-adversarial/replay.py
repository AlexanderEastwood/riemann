"""Adversarial fixed-input replay; never writes another reviewer's files."""
from __future__ import annotations
import contextlib
import hashlib
import importlib.util
import io
import json
import subprocess
from pathlib import Path
from typing import Any
from flint import arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
CERT = HERE.parent
SOURCE = Path('/private/tmp/riemann-prime-folding-review-20260930')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rational(value: dict[str, str]) -> arb:
    return arb(fmpq(int(value['numerator']), int(value['denominator'])))


def main() -> None:
    commit = subprocess.check_output(['git', '-C', str(SOURCE), 'rev-parse', 'HEAD'], text=True).strip()
    assert commit == '769359298fada57711b6895c4bde3fabe2cc5168'
    checks: dict[str, bool] = {}
    before: dict[str, str] = {}
    for folder, seal_name, field in [('01-direct', 'seal.json', 'sha256'), ('02-independent', 'sealed.json', 'files')]:
        base = CERT / folder
        seal = json.loads((base / seal_name).read_text())
        for filename, expected in seal[field].items():
            rel = f'{folder}/{filename}'
            before[rel] = digest(base / filename)
            checks[f'seal:{rel}'] = before[rel] == expected
    direct = load('direct_verifier', CERT / '01-direct/verify_beta.py')
    independent = load('series_verifier', CERT / '02-independent/certify_series.py')
    for name, module, destination, output in [('direct', direct, 'direct-replay', 'outputs.json'), ('series', independent, 'series-replay', 'certificate.json')]:
        owned = HERE / destination
        owned.mkdir(exist_ok=True)
        if name == 'direct':
            module.HERE = owned
        else:
            module.BASE = owned
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            module.main()
        (owned / 'stdout.txt').write_text(stdout.getvalue())
        original = CERT / ('01-direct' if name == 'direct' else '02-independent') / output
        checks[f'{name}:byte_identical_replay'] = (owned / output).read_bytes() == original.read_bytes()
    saved_direct = json.loads((CERT / '01-direct/outputs.json').read_text())
    saved_series = json.loads((CERT / '02-independent/certificate.json').read_text())
    cross: list[dict[str, Any]] = []
    for bits in (128, 256):
        ctx.prec = bits
        gamma = independent.gamma_interval(4096)
        psi, _ = independent.digamma_real(1024, gamma)
        continuum, tail = independent.continuum_series(arb(16).log(), 40)
        powers = independent.strict_prime_powers(16)
        prime_sum = sum((arb(p).log() / arb(m).sqrt() * arb(m).log().cos() for m, p in powers), arb(0))
        beta = psi - arb.pi().log() - 2 * prime_sum + 2 * continuum
        checks[f'{bits}:independent_wide_rational'] = bool(beta > arb(fmpq(-640150, 1000000)) and beta < arb(fmpq(-639904, 1000000)))
        checks[f'{bits}:continuum_tail'] = bool(tail < arb(fmpq(404, 10**32)))
        checks[f'{bits}:independent_saved_ball_contains'] = arb(saved_series['runs'][0 if bits == 128 else 1]['beta_interval']).contains(beta)
        ctx.prec = 384
        for dr in saved_direct['runs']:
            dyad = dr['beta']
            db = rational(dyad['lower_dyadic']).union(rational(dyad['upper_dyadic']))
            e = dr['outward_rational_enclosure']
            encloses = bool(db > rational(e['lower']) and db < rational(e['upper']))
            contains = bool(beta.contains(db))
            checks[f'{bits}:contains_direct_{dr["precision_bits"]}'] = contains
            checks[f'direct_{dr["precision_bits"]}:45_decimal_enclosure'] = encloses
            cross.append({'series_bits': bits, 'direct_bits': dr['precision_bits'], 'series_contains_direct': contains, 'direct_strict_45_decimal_gate': encloses})
    checks['same_strict_prime_power_list'] = direct.prime_power_base(16) == 2 and independent.strict_prime_powers(16) == [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13)]
    for rel, old in before.items():
        checks[f'unchanged:{rel}'] = digest(CERT / rel) == old
    source_files = ['AGENTS.md','research-map.json','README.md','NEXT_STEPS.md','evidence/MISSING.md','manuscript/fixed_space_prime_action_v1.tex']
    result = {'classification': 'Same open gap; fixed existing-claim validation', 'source_commit': commit, 'checks': checks, 'all_pass': all(checks.values()), 'cross_enclosures': cross, 'direct_outward_enclosure': saved_direct['runs'][0]['outward_rational_enclosure'], 'independent_broader_enclosure_exact': ['-0.640150','-0.639904'], 'input_hashes_verified_before_and_after': before, 'source_hashes': {p:digest(SOURCE/p) for p in source_files}, 'scope': {'new_negative_index_numeric_premise_validated': True, 'full_line_even_negative_index': 'infinite by existing analytic implication', 'finite_constraints': 'arbitrary fixed finite homogeneous linear constraints; codimension at most their number', 'physical_window_negative_test': False, 'original_evidence_recovered': False, 'historical_original_groups': 'both OPEN', 'RH_G2_cofinal_floor_NB_gain': 'all remain open'}, 'replayed_in_subprocess': True, 'replay_script_sha256': digest(Path(__file__))}
    (HERE/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_pass':result['all_pass'],'checks':len(checks),'failures':[k for k,v in checks.items() if not v],'enclosure':result['direct_outward_enclosure']},indent=2))
    assert result['all_pass']


if __name__ == '__main__':
    main()
