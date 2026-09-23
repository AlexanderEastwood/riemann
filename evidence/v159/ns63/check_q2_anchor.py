"""Cross-check Mellin quadrature against the separate q=2 Gram formula."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from flint import acb, arb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'ns61'))
from certify_smoothed import Kernel
from certify_one_atom import inspect


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    kernel = Kernel(1, 128, 24)
    zeta0 = (arb(1)/2).zeta()
    load = 3-2*arb.const_euler()-acb.stieltjes(1).real
    gram_value = (2+2*load/zeta0+kernel.gram(1, 1)/(zeta0*zeta0))/2
    quadrature = inspect(1, 64)
    enclosure = arb(quadrature['relative_squared_error'])
    assert enclosure.contains(gram_value)
    result = {'classification': 'certified finite normalization check, not RH evidence',
              'precision_bits': args.bits, 'q2_gram_value': gram_value.str(35),
              'independent_quadrature': quadrature,
              'strict_containment_gate': True}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'precision_bits': args.bits,
                      'q2_gram_value': gram_value.str(15)}))


if __name__ == '__main__':
    main()
