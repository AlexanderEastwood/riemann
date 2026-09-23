"""Independent complete-Gram checks of the physical canonical norm and cross terms."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

from flint import arb, ctx

from certify_cells import coefficients, mobius_sieve, rational

PREVIOUS = Path(__file__).resolve().parents[2] / 'v159' / 'ns61'
sys.path.insert(0, str(PREVIOUS))
from certify_smoothed import Kernel


def check(n: int, row: dict[str, Any], kernel: Kernel) -> dict[str, Any]:
    _, fractions = coefficients(n, mobius_sieve(n))
    c = [rational(v) for v in fractions]
    energy, cross_sigma, cross_tau = arb(2), kernel.load(n), arb(2)
    for m in range(1, n + 1):
        if fractions[m]:
            load = kernel.load(m)
            energy += 2*c[m]*load + c[m]*c[m]*kernel.gram(m, m)
            cross_sigma += c[m]*kernel.gram(m, n)
            cross_tau += c[m]*load
            for k in range(m + 1, n + 1):
                if fractions[k]:
                    energy += 2*c[m]*c[k]*kernel.gram(m, k)
    values = {'full_energy': energy, 'cross_sigma': cross_sigma, 'cross_tau': cross_tau}
    assert all(v.is_finite() for v in values.values()) and energy > 0
    for key, value in values.items():
        assert arb(row['balls'][key]).contains(value), (n, key, row['balls'][key], value)
    return {'N': n, 'all_three_gram_balls_inside_physical_enclosures': True,
            'minimum_accuracy_bits': min(v.rel_accuracy_bits() for v in values.values()),
            'balls': {key: v.str(70) for key, v in values.items()}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', required=True, type=int)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    ctx.prec = args.bits
    directory = Path(__file__).resolve().parent
    physical = json.loads((directory / f'cells-{args.bits}bits.json').read_text())
    by_n = {row['N']: row for row in physical['rows']}
    kernel = Kernel(64, 128, 24)
    rows = [check(n, by_n[n], kernel) for n in [8, 16, 64]]
    report = {'classification': 'independent complete-Gram replay of finite physical cells',
              'precision_bits': args.bits,
              'inherited_kernel_sha256': hashlib.sha256((PREVIOUS/'certify_smoothed.py').read_bytes()).hexdigest(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'rows': rows}
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status':'PASS','sizes':[8,16,64],'mixed_values_per_size':3,
                      'precision_bits':args.bits,'minimum_accuracy_bits':min(r['minimum_accuracy_bits'] for r in rows)}))


if __name__ == '__main__':
    main()
