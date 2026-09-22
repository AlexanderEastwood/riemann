"""DIAGNOSTIC, NOT A CERTIFICATE: reduce energy of already feasible odd witnesses.

Every original/refined bin is enforced at c'=1.03, leaving a visible margin for
reporting c'=1. This is a local pure-state search, never a Q_min computation.
"""
from __future__ import annotations

import json
import os
from typing import Any

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS', '1')
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize
from measure import OUT, N, assembly, build_grid, energy_recheck, print_screen, witness_screen


def run(lam: int) -> None:
    old = json.loads((OUT / f'lambda{lam}.json').read_text())
    grid1 = build_grid(lam, 1, np.array(old['edges']))
    grid2 = build_grid(lam, 2, np.array(old['edges']))
    bits = 1024 if lam < 6 else 2048
    wb = assembly(lam, bits)
    w = np.array([[float(wb[i, j].mid()) for j in range(N)] for i in range(N)])
    w = (w + w.T) / 2
    _, vectors = eigh(w)
    # Deliberately enlarge the proposal subspace. All saved slacks are later
    # measured in the original full 256-coordinate state.
    rank = min(N, old['pure_search']['best']['rank'] + 16)
    basis = vectors[:, :rank]
    inverse = np.linalg.inv(np.linalg.cholesky(basis.T @ basis))
    basis = basis @ inverse.T
    qr = basis.T @ w @ basis
    qr = (qr + qr.T) / 2
    initial = np.array([float(x) for x in old['pure_search']['best']['vector_decimal']])
    x0 = basis.T @ initial
    x0 /= np.linalg.norm(x0)
    scale = max(abs(float(x0 @ qr @ x0)), 1e-12)
    ms = np.array([basis.T @ m @ basis / r for grid in (grid1, grid2)
                   for m, r in zip(grid['masses'], grid['reference'])])

    def objective(x: Any) -> tuple[float, Any]:
        return float(x @ qr @ x) / scale, 2 * qr @ x / scale

    def constraints(x: Any) -> Any:
        return np.einsum('i,bij,j->b', x, ms, x) - 1.03

    def derivative(x: Any) -> Any:
        return 2 * np.einsum('bij,j->bi', ms, x)

    result = minimize(objective, x0, jac=True, method='SLSQP',
        constraints=[{'type': 'eq', 'fun': lambda x: float(x @ x - 1), 'jac': lambda x: 2*x},
                     {'type': 'ineq', 'fun': constraints, 'jac': derivative}],
        options={'maxiter': 3000, 'ftol': 1e-13})
    vector = basis @ result.x
    vector /= np.linalg.norm(vector)
    screens = [witness_screen(vector, grid) for grid in (grid1, grid2)]
    payload: dict[str, Any] = {'status': 'DIAGNOSTIC, NOT A CERTIFICATE', 'lambda': lam, 'N': N,
        'parity': 'odd', 'state_type': 'pure', 'rank_of_search_subspace': rank, 'c_prime_target': 1.03,
        'scope': 'Local feasible pure-state energy improvement. No global optimum or primal-dual equality is claimed.',
        'optimizer_success': bool(result.success), 'optimizer_message': str(result.message),
        'vector_decimal': [str(x) for x in vector], 'screens': screens,
        'all_grid_constraints_pass_at_one': all(screen['float_pass'] for screen in screens)}
    print('lambda', lam, 'optimizer', result.success, result.message, flush=True)
    for screen in screens:
        print_screen(f'lambda={lam} improved fixed pure primal grid{screen["refinement"]}', screen)
    if payload['all_grid_constraints_pass_at_one']:
        payload['energy_rechecks'] = [energy_recheck(lam, payload['vector_decimal'], bits, 80),
                                     energy_recheck(lam, payload['vector_decimal'], bits + 256, 120)]
        print('FIXED FEASIBLE ENERGY', json.dumps(payload['energy_rechecks']), flush=True)
    else:
        payload['not_an_upper_witness'] = True
        print('FAILED FEASIBILITY: no energy upper witness reported', flush=True)
    (OUT / f'lambda{lam}-improved.json').write_text(json.dumps(payload, indent=2) + '\n')


def main() -> None:
    # lambda=4 already has a robust feasible state at 1.5e-18, beneath the
    # double-precision energy scale; a float energy search is inappropriate.
    for lam in (3, 6, 8):
        run(lam)


if __name__ == '__main__':
    main()
