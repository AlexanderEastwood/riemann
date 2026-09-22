"""NS-36 numerical illustration: weighted-bin feasibility after any rank-one source constraint.

This is not a certificate. Float quadrature defines twenty finite-bin mass
matrices. The construction removes an arbitrary one-dimensional source from a
low-energy subspace; its conservative mass estimate uses the largest eigenvalue
of each restricted bin matrix. A passing mixture need not have a feasible pure
component. Run from the repository root with its existing virtual environment.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
from flint import ctx
from scipy.linalg import eigh
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "evidence/v124/g2_schur_cancellation"),
                str(ROOT / "evidence/diag_true_symbol")]
from assembly_general import block, sequences
from pencil import Fe_grid, beta_grid

OUT = Path(__file__).resolve().parent


def matrices(refinement: int) -> tuple[Any, Any, Any, Any, float]:
    """Reproduce the original grid or subdivide its weighted intervals."""
    original_x = np.concatenate([np.arange(.001, 40, .002),
                                 np.arange(40.005, 800, .005)])
    original_h = np.where(original_x < 40, .002, .005)
    # Refinement preserves the original covered intervals, including its
    # 0.0025 gap above 40 and below 800, so only quadrature resolution changes.
    offsets = (np.arange(refinement) + .5) / refinement - .5
    xs = (original_x[:, None] + original_h[:, None] * offsets).ravel()
    hs = np.repeat(original_h / refinement, refinement)
    beta, length = beta_grid(4, xs)
    original_beta, _ = beta_grid(4, original_x)
    depth = float(-original_beta.min())
    # Freeze the original bin edges. Extend the first bin downward so a refined
    # sample below the old sampled minimum remains assigned to the deepest bin.
    edges = np.linspace(-depth, 0, 21)
    fs = np.array([(-1) ** n * Fe_grid(n, length, xs) for n in range(257)])
    sels = [(beta < edges[1])] + [
        (beta >= lo) & (beta < hi) for lo, hi in zip(edges[1:-1], edges[2:])]
    masses = np.array([2 * (fs[:, s] * hs[s]) @ fs[:, s].T for s in sels])
    reference = np.array([float(hs[s].sum()) / 800 for s in sels])
    return masses, reference, edges, beta, depth


def source_independent_screen(w: Any, masses: Any, reference: Any) -> tuple[list[dict[str, Any]], Any]:
    """Find conservative feasible mixtures in low-energy spectral subspaces."""
    eigenvalues, vectors = eigh(w)
    results = []
    for rank in range(2, 41):
        basis = vectors[:, :rank]
        # Use the decimal-basis Gram in the mass test as in the energy recheck.
        # Both evaluations are still numerical, not error enclosures.
        gram = basis.T @ basis
        inverse = np.linalg.inv(np.linalg.cholesky(gram))
        restricted = np.array([inverse @ (basis.T @ m @ basis) @ inverse.T for m in masses])
        maximum = np.array([eigh(m, eigvals_only=True, subset_by_index=[rank-1, rank-1])[0]
                            for m in restricted])
        traces = np.trace(restricted, axis1=1, axis2=2)
        # If P_E u != 0, remove z=P_Eu/||P_Eu||. Every bin loses <=lambda_max.
        # If P_E u=0, the unmodified uniform mixture has mass trace/rank,
        # which is at least this same conservative bound.
        lower = (traces - maximum) / (rank - 1)
        results.append({"rank": rank, "subspace_energy_ceiling_float": float(eigenvalues[rank-1]),
                        "min_guaranteed_ratio": float(np.min(lower / reference)),
                        "guaranteed_masses": lower.tolist(),
                        "slacks_at_one": (lower - reference).tolist()})
    return results, vectors


def mp_energy_matrix(basis: Any, wb: Any) -> dict[str, Any]:
    """Re-evaluate the saved decimal subspace with midpoint arithmetic at 90 digits."""
    mp.mp.dps = 90
    b = mp.matrix([[mp.mpf(str(value)) for value in row] for row in basis])
    w = mp.matrix([[mp.mpf(wb[i, j].str(100, radius=False)) for j in range(257)]
                   for i in range(257)])
    gram = b.T * b
    chol = mp.cholesky(gram)
    inverse = mp.inverse(chol)
    energy = inverse * (b.T * w * b) * inverse.T
    energy = (energy + energy.T) / 2
    values = mp.eigsy(energy, eigvals_only=True)
    return {"arithmetic": "90 decimal digits, Arb assembly midpoints; not an enclosure",
            "minimum": mp.nstr(values[0], 35), "maximum": mp.nstr(values[-1], 35),
            "source_removed_mixture_energy_ceiling": mp.nstr(
                (mp.fsum(values) - values[0]) / (values.rows - 1), 35),
            "gram_distance_frobenius": mp.nstr(mp.norm(gram - mp.eye(gram.rows)), 15)}


def raw_pure_search(vectors: Any, masses: Any, reference: Any) -> dict[str, Any]:
    """Search for raw pure witnesses; every returned state is explicitly rechecked.

    These vectors do not impose the actual source constraint. A failed search
    does not prove infeasibility. This separately tests the original raw claim.
    """
    rng = np.random.default_rng(36)
    attempts = []
    best: Any = None
    for rank in (11, 12, 13, 14):
        basis = vectors[:, :rank]
        ms = np.array([basis.T @ m @ basis / r for m, r in zip(masses, reference)])
        for start in range(12):
            x = rng.normal(size=rank)
            x /= np.linalg.norm(x)
            def objective(z: Any) -> tuple[float, Any]:
                return -float(z[-1]), np.r_[np.zeros(rank), -1.]
            def constraints(z: Any) -> Any:
                return np.einsum('i,bij,j->b', z[:-1], ms, z[:-1]) - z[-1]
            def derivative(z: Any) -> Any:
                return np.column_stack([2 * np.einsum('bij,j->bi', ms, z[:-1]), -np.ones(20)])
            res = minimize(objective, np.r_[x, 0.], jac=True, method='SLSQP',
                constraints=[{'type': 'eq', 'fun': lambda z: float(z[:-1] @ z[:-1] - 1),
                              'jac': lambda z: np.r_[2*z[:-1], 0.]},
                             {'type': 'ineq', 'fun': constraints, 'jac': derivative}],
                options={'maxiter': 600, 'ftol': 1e-12})
            v = basis @ res.x[:-1]
            v /= np.linalg.norm(v)
            measured = np.array([v @ m @ v for m in masses])
            ratio = float(np.min(measured / reference))
            item = {'rank': rank, 'start': start, 'success': bool(res.success),
                    'min_ratio': ratio, 'slacks_at_one': (measured-reference).tolist()}
            attempts.append(item)
            if best is None or ratio > best['min_ratio']:
                best = dict(item, vector_decimal=[str(value) for value in v])
        print('raw pure search', rank, max(a['min_ratio'] for a in attempts if a['rank']==rank), flush=True)
        if best['min_ratio'] > 1.001:
            break
    return {'scope': 'RAW vector; source constraint not imposed', 'attempts': attempts, 'best': best}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refinement", type=int, default=1)
    parser.add_argument("--raw-search", action='store_true')
    args = parser.parse_args()
    ctx.prec = 1024
    _, b, d, _ = sequences(4, 264, 1024)
    wb = block(list(range(257)), list(range(257)), "even", b, d)
    w = np.array([[float(wb[i,j].mid()) for j in range(257)] for i in range(257)])
    w = (w + w.T) / 2
    print("assembled lambda=4 N=256", flush=True)
    masses, reference, edges, beta, depth = matrices(args.refinement)
    rows, vectors = source_independent_screen(w, masses, reference)
    payload: dict[str, Any] = {"status": "DIAGNOSTIC, NOT A CERTIFICATE", "lambda": 4, "N": 256,
        "refinement": args.refinement, "bin_count": 20, "original_sampled_depth": depth,
        "sampled_depth_this_run": float(-beta.min()), "reference_masses": reference.tolist(),
        "original_edges": edges.tolist(), "deepest_bin": "extends below original sampled minimum",
        "screen": rows}
    passing = [row for row in rows if row["min_guaranteed_ratio"] > 1.001]
    if passing:
        selected = passing[0]
        rank = selected["rank"]
        basis = vectors[:, :rank]
        payload["selected"] = selected
        payload["basis_decimal"] = [[str(value) for value in row] for row in basis]
        payload["energy_recheck"] = mp_energy_matrix(basis, wb)
        print("PASSING MIXTURE", json.dumps(selected), flush=True)
        print("ENERGY RECHECK", json.dumps(payload["energy_recheck"]), flush=True)
    else:
        print("No passing source-independent mixture among tested subspaces", flush=True)
    if args.raw_search:
        payload['raw_pure_search'] = raw_pure_search(vectors, masses, reference)
        raw = np.array([float(s) for s in payload['raw_pure_search']['best']['vector_decimal']])
        mp.mp.dps = 90
        v = mp.matrix([mp.mpf(str(value)) for value in raw])
        wmp = mp.matrix([[mp.mpf(wb[i,j].str(100, radius=False)) for j in range(257)] for i in range(257)])
        payload['raw_pure_search']['best']['energy_90dps'] = mp.nstr((v.T*wmp*v)[0]/(v.T*v)[0], 35)
        print('RAW PURE BEST', payload['raw_pure_search']['best']['min_ratio'],
              payload['raw_pure_search']['best']['energy_90dps'], flush=True)
    for row in rows:
        print(row["rank"], row["subspace_energy_ceiling_float"], row["min_guaranteed_ratio"], flush=True)
    (OUT / f"feasibility_grid{args.refinement}.json").write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
