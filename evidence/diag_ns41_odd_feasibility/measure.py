"""DIAGNOSTIC, NOT A CERTIFICATE: odd finite-head weighted-bin feasibility.

Float optimization proposes states. Every saved witness is a normalized fixed
256-coordinate decimal vector. Twenty bin slacks are rechecked on the original
and a refined grid. Its untruncated finite-form energy uses higher-precision
assembly midpoints at two precisions. No midpoint result is an enclosure.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path
from typing import Any

# Set before importing numerical libraries for reproducible bounded threading.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
import mpmath as mp
import numpy as np
from flint import ctx
from scipy.linalg import eigh
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "evidence/v124/g2_schur_cancellation"),
                str(ROOT / "evidence/diag_true_symbol")]
from assembly_general import block, sequences
from pencil import beta_grid

OUT = Path(__file__).resolve().parent
N = 256
NB = 20
XI = 800.0


def original_grid() -> tuple[Any, Any]:
    """Historical weighted intervals, including the small gap above xi=40."""
    xs = np.concatenate([np.arange(.001, 40., .002), np.arange(40.005, XI, .005)])
    return xs, np.where(xs < 40., .002, .005)


def build_grid(lam: int, refinement: int, edges: Any | None = None) -> dict[str, Any]:
    """Assemble odd bin-MASS matrices and normalized one-sided reference mass."""
    x0, h0 = original_grid()
    offsets = (np.arange(refinement) + .5) / refinement - .5
    xs = (x0[:, None] + h0[:, None] * offsets).ravel()
    hs = np.repeat(h0 / refinement, refinement)
    beta, length = beta_grid(lam, xs)
    depth = float(-beta.min())
    if edges is None:
        edges = np.linspace(-depth, 0., NB + 1)
    # Freeze the old edges for replay. The first bin includes any samples below
    # the old minimum, preventing refined points from silently disappearing.
    selections = [beta < edges[1]] + [
        (beta >= lo) & (beta < hi) for lo, hi in zip(edges[1:-1], edges[2:])]
    indices = np.arange(1, N + 1)
    omega = 2 * math.pi * indices / length
    # sinc form avoids removable singularities. This real common-imaginary
    # transform convention matches pencil_odd, including the (-1)^n basis sign.
    fs = np.sqrt(length / (4 * math.pi)) * (
        np.sinc((omega[:, None] - xs[None, :]) * length / (2 * math.pi))
        - np.sinc((omega[:, None] + xs[None, :]) * length / (2 * math.pi)))
    fs *= ((-1.) ** indices)[:, None]
    masses = np.array([2 * (fs[:, sel] * hs[sel]) @ fs[:, sel].T for sel in selections])
    reference = np.array([float(hs[sel].sum()) / XI for sel in selections])
    assert np.all(reference > 0)
    return {"masses": masses, "reference": reference, "edges": edges,
            "sampled_depth": depth, "samples": len(xs), "refinement": refinement,
            "sampled_interval_weight": float(hs.sum())}


def assembly(lam: int, bits: int) -> Any:
    """Arb head assembly; callers intentionally use midpoints for diagnostics."""
    ctx.prec = bits
    _, b, d, _ = sequences(lam, N + 8, bits)
    rows = list(range(1, N + 1))
    return block(rows, rows, "odd", b, d)


def witness_screen(vector: Any, grid: dict[str, Any]) -> dict[str, Any]:
    """Evaluate every mass inequality at c'=1 after normalizing the fixed vector."""
    norm2 = float(vector @ vector)
    masses = np.einsum('i,bij,j->b', vector, grid['masses'], vector) / norm2
    reference = grid['reference']
    slack = masses - reference
    return {"refinement": grid['refinement'], "masses": masses.tolist(),
            "required": reference.tolist(), "slacks": slack.tolist(),
            "ratios": (masses / reference).tolist(), "min_ratio": float(min(masses / reference)),
            "min_slack": float(min(slack)), "float_pass": bool(np.all(slack > 0)),
            "decimal_vector_norm2_float": norm2}


def pure_search(w: Any, grid: dict[str, Any], lam: int) -> dict[str, Any]:
    """Maximize the smallest bin ratio inside expanding low-energy subspaces."""
    _, vectors = eigh(w)
    rng = np.random.default_rng(4100 + lam)
    attempts: list[dict[str, Any]] = []
    best: dict[str, Any] | None = None
    for rank in (2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 56, 80):
        basis = vectors[:, :rank]
        # Whiten the stored decimal basis consistently, instead of assuming
        # its float eigenvectors have mathematically exact orthonormal columns.
        inverse = np.linalg.inv(np.linalg.cholesky(basis.T @ basis))
        basis = basis @ inverse.T
        restricted = np.array([basis.T @ matrix @ basis / mass
                               for matrix, mass in zip(grid['masses'], grid['reference'])])
        for start in range(8):
            x = rng.normal(size=rank)
            x /= np.linalg.norm(x)

            def objective(z: Any) -> tuple[float, Any]:
                return -float(z[-1]), np.r_[np.zeros(rank), -1.]

            def constraint(z: Any) -> Any:
                return np.einsum('i,bij,j->b', z[:-1], restricted, z[:-1]) - z[-1]

            def derivative(z: Any) -> Any:
                return np.column_stack([2 * np.einsum('bij,j->bi', restricted, z[:-1]), -np.ones(NB)])

            result = minimize(objective, np.r_[x, 0.], jac=True, method='SLSQP',
                constraints=[{'type': 'eq', 'fun': lambda z: float(z[:-1] @ z[:-1] - 1),
                              'jac': lambda z: np.r_[2 * z[:-1], 0.]},
                             {'type': 'ineq', 'fun': constraint, 'jac': derivative}],
                options={'maxiter': 700, 'ftol': 1e-12})
            vector = basis @ result.x[:-1]
            vector /= np.linalg.norm(vector)
            screen = witness_screen(vector, grid)
            record = {'rank': rank, 'start': start, 'optimizer_success': bool(result.success),
                      'optimizer_message': str(result.message), 'min_ratio': screen['min_ratio'],
                      'slacks': screen['slacks'], 'float_pass': screen['float_pass']}
            attempts.append(record)
            if best is None or screen['min_ratio'] > best['screen']['min_ratio']:
                best = {'rank': rank, 'start': start, 'vector_decimal': [str(x) for x in vector],
                        'screen': screen}
        assert best is not None
        print(f"lambda={lam} pure search rank={rank} best ratio={best['screen']['min_ratio']:.12g}", flush=True)
        # A material margin is preferable to an optimizer's equality tolerance.
        if best['screen']['min_ratio'] > 1.08:
            break
    assert best is not None
    return {'attempts': attempts, 'best': best,
            'scope': 'Pure real odd head states; no source constraint; not an optimized energy minimum.'}


def dual_search(w: Any, grid: dict[str, Any]) -> dict[str, Any]:
    """A separate float SDP dual screen, never an upper or feasibility witness."""
    masses, required = grid['masses'], grid['reference']

    def objective(y: Any) -> tuple[float, Any]:
        a = w - np.einsum('b,bij->ij', y, masses)
        values, vectors = eigh(a, subset_by_index=[0, 0])
        vector = vectors[:, 0]
        measured = np.einsum('i,bij,j->b', vector, masses, vector)
        return -float(values[0] + y @ required), measured - required

    results = [minimize(objective, np.full(NB, start), jac=True, method='L-BFGS-B',
                       bounds=[(0., None)] * NB,
                       options={'maxiter': 1000, 'ftol': 1e-15, 'gtol': 1e-12})
               for start in (0., .01, .1)]
    result = min(results, key=lambda item: item.fun)
    y = np.maximum(result.x, 0.)
    a = w - np.einsum('b,bij->ij', y, masses)
    values, vectors = eigh(a, subset_by_index=[0, 0])
    vector = vectors[:, 0]
    screen = witness_screen(vector, grid)
    return {'direction': 'In exact arithmetic, lambda_min(W-sum y_b M_b)+y.r is a lower bound on the finite-grid mixed-state optimum; the value here is unenclosed float.',
            'value_float': float(values[0] + y @ required),
            'spectral_term_float': float(values[0]), 'linear_term_float': float(y @ required),
            'multipliers': y.tolist(), 'min_multiplier': float(min(y)),
            'optimizer_success': bool(result.success), 'optimizer_message': str(result.message),
            'minimizing_eigenvector_screen': screen,
            'minimizing_eigenvector_decimal': [str(x) for x in vector],
            'eigenvector_is_not_used_as_upper_witness': True}


def energy_recheck(lam: int, vector_decimal: list[str], bits: int, digits: int) -> dict[str, Any]:
    """Evaluate q of the exact saved decimal vector, normalized in mp arithmetic."""
    wb = assembly(lam, bits)
    mp.mp.dps = digits
    vector = mp.matrix([mp.mpf(x) for x in vector_decimal])
    w = mp.matrix([[mp.mpf(wb[i, j].str(digits + 10, radius=False)) for j in range(N)]
                   for i in range(N)])
    norm2 = (vector.T * vector)[0]
    energy = (vector.T * w * vector)[0] / norm2
    return {'bits': bits, 'decimal_digits': digits, 'normalized_energy_midpoint': mp.nstr(energy, 60),
            'decimal_vector_norm2': mp.nstr(norm2, 60),
            'direction': 'Energy of the fixed normalized pure vector. If the stated grid inequalities hold, it is a finite-grid primal upper witness. Midpoint evaluation is not an enclosure.'}


def print_screen(name: str, screen: dict[str, Any]) -> None:
    """Print each constraint individually, including all failures."""
    print(name, 'min_ratio=', screen['min_ratio'], 'float_pass=', screen['float_pass'], flush=True)
    print('bin required mass slack ratio', flush=True)
    for i, row in enumerate(zip(screen['required'], screen['masses'], screen['slacks'], screen['ratios'])):
        print(i, *(f'{x:.17g}' for x in row), flush=True)


def run(lam: int) -> None:
    start = time.time()
    bits = 1024 if lam < 6 else 2048
    wb = assembly(lam, bits)
    w = np.array([[float(wb[i, j].mid()) for j in range(N)] for i in range(N)])
    w = (w + w.T) / 2
    grid1 = build_grid(lam, 1)
    payload: dict[str, Any] = {'status': 'DIAGNOSTIC, NOT A CERTIFICATE', 'lambda': lam,
        'N': N, 'indices': '1 through 256 inclusive', 'parity': 'odd', 'bin_count': NB, 'c_prime': 1,
        'source_constraint': 'None: the prescribed source is even.',
        'grid_definition': 'Historical weighted midpoint intervals from xi=.001:.002:40 and 40.005:.005:800; no tail completion; normalization is by 800, not by covered grid length.',
        'bin_definition': 'First bin extends below the original sampled minimum; remaining edges frozen from original grid. Beta=0 excluded.',
        'edges': grid1['edges'].tolist(),
        'grid1': {key: grid1[key] for key in ('sampled_depth', 'samples', 'refinement', 'sampled_interval_weight')}}
    search = pure_search(w, grid1, lam)
    payload['pure_search'] = search
    vector = np.array([float(x) for x in search['best']['vector_decimal']])
    print_screen(f'lambda={lam} FIXED PURE PRIMAL grid1', search['best']['screen'])
    payload['dual_grid1'] = dual_search(w, grid1)
    print('SEPARATE DUAL', payload['dual_grid1']['value_float'], flush=True)
    print_screen('dual minimizing eigenvector, NOT AN UPPER WITNESS',
                 payload['dual_grid1']['minimizing_eigenvector_screen'])
    # Release matrix-heavy grid before the refined allocation.
    edges = grid1['edges'].copy()
    del grid1
    grid2 = build_grid(lam, 2, edges)
    payload['grid2'] = {key: grid2[key] for key in ('sampled_depth', 'samples', 'refinement', 'sampled_interval_weight')}
    payload['pure_grid2'] = witness_screen(vector, grid2)
    print_screen(f'lambda={lam} FIXED PURE PRIMAL grid2', payload['pure_grid2'])
    del grid2
    payload['energy_rechecks'] = [energy_recheck(lam, search['best']['vector_decimal'], bits, 80),
                                 energy_recheck(lam, search['best']['vector_decimal'], bits + 256, 120)]
    print('FIXED PURE ENERGY', json.dumps(payload['energy_rechecks']), flush=True)
    payload['runtime_seconds'] = time.time() - start
    (OUT / f'lambda{lam}.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(f'FINISHED lambda={lam} in {time.time()-start:.1f}s', flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('lambdas', nargs='*', type=int, default=[3, 4, 6, 8])
    args = parser.parse_args()
    for lam in args.lambdas:
        if lam not in (3, 4, 6, 8):
            raise ValueError('NS-41 only permits the existing four windows.')
        run(lam)


if __name__ == '__main__':
    main()
