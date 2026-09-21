#!/usr/bin/env python3
"""Complete shifted-Schur inertia from the archived lambda=4 certificates.

All new computations use outward Arb arithmetic on exact frozen dyadic trials.
The v1.25/v1.26 complete residual enclosures are reused, not silently recomputed.
"""
import argparse
import gzip
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path
from flint import arb, arb_mat, ctx

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
OLD = ROOT / 'evidence/v126'


def A(q):
    q = Fraction(q)
    return arb(q.numerator) / q.denominator


def sym(M):
    return (M + M.transpose()) / 2


def inertia(M):
    n = M.nrows()
    L = arb_mat(n, n)
    D, signs = [], []
    for j in range(n):
        p = M[j, j] - sum((L[j, k] * L[j, k] * D[k]
                           for k in range(j)), arb(0))
        if p > 0:
            signs.append(1)
        elif p < 0:
            signs.append(-1)
        else:
            return {'status': 'UNRESOLVED', 'index': j, 'pivot': p.str(70)}
        D.append(p)
        for i in range(j + 1, n):
            L[i, j] = (M[i, j] - sum((L[i, k] * L[j, k] * D[k]
                                      for k in range(j)), arb(0))) / p
    return {'status': 'CERTIFIED', 'negative': signs.count(-1),
            'positive': signs.count(1), 'signs': signs,
            'pivots': [p.str(80) for p in D]}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dyadic_fraction(pair):
    n, e = pair
    return Fraction(int(n)) * Fraction(2)**int(e)


def replay_prior_gates(parity, data, m, bits):
    """Recheck small final gates, not the archived full residual assemblies."""
    dependencies = []
    def read(path):
        dependencies.append({'path': str(path.relative_to(ROOT)), 'sha256': sha(path)})
        return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz'
                          else path.read_text())
    tr = read(OLD / 'g2_weighted_signed' / f'weighted_tail_l4_s16_{parity}_b320.json')
    assert tr['status'] == 'PASS' and tr['literal_tail_start'] == 16
    assert tr['witness_sha256'] == data['inner_sha256']
    assert Fraction(tr['c']) == Fraction('1e-8')
    assert arb(tr['arch_diagonal_floor']) > A('1.7940')
    assert arb(tr['Gershgorin_margin']) > A('0.9999999999')
    # Independently reevaluate the elementary archimedean lower floor.
    ell = 2 * arb(4).log()
    t = 2 * arb.pi() * 17 / ell
    err = 1/(15*t) + arb(7)/(2*t*t) + arb.pi()/(2*ell*t) + (2 + arb(128)/255)/(ell*t*t)
    assert (arb(17)/ell).log() - err > A('1.7940')
    K, mu, rho = sym(m['K']), arb(data['mu']), arb(data['rho'])
    tau = A('1/10') if parity == 'even' else A('1/20')
    U = m['V'] + m['E'] + ((1 + tau)*m['HGram'] + (1 + 1/tau)*rho*m['E'])/mu
    if parity == 'even':
        gate = inertia(sym((1 - A('62629/100000'))*K - U))
        assert gate['status'] == 'CERTIFIED' and gate['negative'] == 0
        return {'even_relative_gate': gate, 'dependencies': dependencies}
    folder = OLD / 'g2_odd_complement'
    old = read(folder / 'simultaneous_odd_M4096_s16_normalized_witness.json.gz')
    dw = read(folder / 'simultaneous_odd_M4096_s32_normalized_witness.json.gz')
    nw = read(folder / 'directional_odd_M8192_s24_witness.json.gz')
    oldhash = data['trial_witness_sha256']
    assert dw['parent_witness_sha256'] == nw['parent_witness_sha256'] == oldhash
    assert dw['base_columns'] == old['base_columns']
    assert nw['direction_dyadics'] == dw['direction_dyadics']
    vv = list(map(dyadic_fraction, nw['direction_dyadics']))
    exact_head = [sum((dyadic_fraction(old['base_columns'][j][i])*vv[j]
                      for j in range(16)), Fraction(0)) for i in range(16)]
    assert exact_head == list(map(dyadic_fraction, nw['dyadics'][:16]))
    v = arb_mat([[A(q)] for q in vv])
    den = (v.transpose()*K*v)[0, 0]
    assert den > 0
    omit = max(range(16), key=lambda i: float(abs(v[i, 0])))
    assert not v[omit, 0].contains(0)
    I = arb_mat([[int(i == j) for j in range(16)] for i in range(16)])
    P = I - v*(v.transpose()*K)/den
    Z = arb_mat([[P[i, j] for j in range(16) if j != omit] for i in range(16)])
    gate = inertia(sym(Z.transpose()*(A('1/1000')*K - U)*Z))
    assert gate['status'] == 'CERTIFIED' and gate['negative'] == 0
    rb = 1024 if bits <= 1024 else 1280
    rep = read(folder / f'directional_odd_M8192_s24_report_b{rb}_J65536.json')
    assert rep['trial_witness_sha256'] == sha(folder / 'directional_odd_M8192_s24_witness.json.gz')
    assert rep['parent_witness_sha256'] == oldhash
    assert (rep['M'], rep['J'], rep['rho_source_J'], rep['bits']) == (8192, 65536, 65536, rb)
    energy, far, remote, mixed, rho2, oldden = [arb(rep[k]) for k in
        ['K', 'finite_far_upper', 'remote_outer_upper', 'finite_mixed_squared',
         'rho_upper', 'old_direction_denominator']]
    assert oldden.overlaps(den)
    corr = far + remote + (mixed.sqrt() + (rho2*remote).sqrt())**2 / mu
    directional = (energy - corr) / oldden
    assert directional > A('429/1000')
    return {'odd_complement_gate': gate, 'odd_direction_lower': directional.str(90),
            'exact_shared_head_check': True, 'directional_ingredient_bits': rb,
            'dependencies': dependencies}


def load_trial(parity, bits):
    folder = OLD / ('g2_simultaneous' if parity == 'even' else 'g2_odd_complement')
    stem = f'simultaneous_{parity}_M4096_s16_normalized'
    # The saved even ingredients have two independent precision evaluations;
    # odd ingredients were evaluated at 768 bits and are reused as enclosures.
    ibits = (768 if bits <= 1024 else 896) if parity == 'even' else 768
    ipath = folder / (stem + f'_ingredients_b{ibits}.json')
    wpath = folder / (stem + '_witness.json.gz')
    data = json.loads(ipath.read_text())
    w = json.loads(gzip.decompress(wpath.read_bytes()))
    assert data['trial_witness_sha256'] == sha(wpath)
    assert data['parity'] == w['parity'] == parity
    assert data['M'] == w['M'] == 4096 and data['J'] == 65536
    assert w['inner_sha256'] == data['inner_sha256']
    assert w['outer_sha256'] == data['outer_sha256']
    n = 17 if parity == 'even' else 16
    offset = 0 if parity == 'even' else 1
    columns = []
    for base, correction in zip(w['base_columns'], w['dyadic_columns']):
        assert len(base) == 257 - offset and len(correction) == 4080
        f = [arb(v) * arb(2)**e for v, e in base] + [arb(0)] * (4096 - 256)
        for k, (v, e) in enumerate(correction):
            f[17 - offset + k] -= arb(v) * arb(2)**e
        assert all(x.is_exact() for x in f), 'raise precision to reconstruct exact trial'
        columns.append(f)
    assert len(columns) == n
    G = arb_mat(columns).transpose()
    V = arb_mat([[G[i, j] for j in range(n)] for i in range(n)])
    Z = arb_mat([[G[i, j] for j in range(n)] for i in range(n, G.nrows())])
    m = {k: arb_mat([[arb(t) for t in row] for row in v])
         for k, v in data['matrices'].items()}
    assert not V.det().contains(0)
    # The reconstructed exact head must be contained in the saved enclosure.
    assert all(m['head'][i, j].contains(V[i, j]) for i in range(n) for j in range(n))
    return data, m, G, V, Z, {'ingredients': str(ipath.relative_to(ROOT)),
                             'ingredient_sha256': sha(ipath),
                             'ingredient_precision_bits': ibits,
                             'witness': str(wpath.relative_to(ROOT)),
                             'witness_sha256': sha(wpath)}


def run(bits=1024, shift='1e-73'):
    start = time.time()
    ctx.prec = bits
    delta = A('1.7940e-8')
    s = A(shift)
    assert 0 < s < delta
    output = {'precision_bits': bits, 'lambda': 4, 'literal_tail_start': 16,
              'ordinary_tail_floor': '1.7940e-8', 'shift': shift,
              'scope': 'New shifted inertia and Rayleigh gates on archived complete '
                       'v125/v126 enclosures; not a fresh full residual assembly.',
              'sectors': {}}
    for parity, kappa in [('even', '62629/100000'), ('odd', '428/1000')]:
        data, m, G, V, Z, provenance = load_trial(parity, bits)
        prior = replay_prior_gates(parity, data, m, bits)
        K = sym(m['K'])
        assert inertia(K)['negative'] == 0
        Hh = V.transpose() * V
        Ht = Z.transpose() * Z
        H = Hh + Ht
        penalty = Hh + 2 / (1 - s / delta) * (Ht + K / delta)
        lower = sym(A(kappa) * K - s * penalty)
        gate = inertia(lower)
        trials = [K[j, j] / H[j, j] for j in range(K.nrows())]
        trial_index = min(range(len(trials)), key=lambda j: float(trials[j].upper()))
        result = {'kappa': kappa, 'shifted_inertia': gate,
                  'trial_column': trial_index,
                  'trial_rayleigh': trials[trial_index].str(90),
                  'trial_energy': K[trial_index, trial_index].str(90),
                  'trial_norm_squared': H[trial_index, trial_index].str(90),
                  'trial_below_shift': bool(trials[trial_index] < s),
                  'prior_complete_gates': prior,
                  'provenance': provenance}
        if parity == 'even':
            assert trials[trial_index] < A('2.454e-75')
        output['sectors'][parity] = result
        print(parity, {k: v for k, v in result.items() if k not in ['provenance', 'shifted_inertia', 'prior_complete_gates']},
              {k: v for k, v in gate.items() if k != 'pivots'}, flush=True)
    ev, od = output['sectors']['even'], output['sectors']['odd']
    passed = (ev['shifted_inertia']['status'] == od['shifted_inertia']['status'] == 'CERTIFIED'
              and ev['shifted_inertia']['negative'] == 1
              and od['shifted_inertia']['negative'] == 0 and ev['trial_below_shift'])
    output['status'] = 'PASS_COMPLETE_SIMPLE_EVEN_GROUND' if passed else 'INCONCLUSIVE_LOWER_BOUND'
    output['elapsed_seconds'] = time.time() - start
    path = BASE / f'ground4_b{bits}_shift{shift}.json'
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(output['status'], output['elapsed_seconds'], flush=True)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, default=1024)
    parser.add_argument('--shift', default='1e-73')
    args = parser.parse_args()
    run(**vars(args))
