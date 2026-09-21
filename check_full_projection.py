"""Full Fourier projection: finite identities and holomorphic rational check.

No zeta zeros or Weil matrix are used. Moderate cutoffs test conventions,
not the theorem's exponential-cutoff estimates or RH.
"""
import json
from pathlib import Path
import numpy as np


def main():
    mu, nu = 0.23 + 0.7j, 0.37 + 1.4j
    b = np.diag([mu, mu, nu])
    b[0, 1] = 1
    eta = np.array([1., 0., 1.])
    d = np.array([1.2 + .4j, -.2 + .7j, .6 - .1j])

    def source(v):
        return (v-mu)**2 * (v-nu) / ((v+2)**8 * (2-v))

    def outputs(v):
        base = 1 / ((v+2)**8 * (2-v))
        return np.array([(v-mu)*(v-nu)*base,
                         (v-nu)*base, (v-mu)**2*base])

    rows = []
    for length in (8., 12., 16., 24., 32.):
        k = int(4*length**2)
        n = np.arange(-2*k, 2*k+1)
        t = 2*np.pi*n/length
        phase = np.where(n % 2 == 0, 1., -1.)
        z = phase*source(1j*t)/np.sqrt(length)
        jc = phase[:, None]*outputs(1j*t).T/np.sqrt(length)
        c = np.where(np.abs(n) > k, np.sqrt(length)/(2*k), 0.)
        dc = t*c
        e = np.column_stack((c/np.linalg.norm(c), dc/np.linalg.norm(dc)))

        def q(x):
            return x-e@(e.conj().T@x)

        u = q(z)
        w = u/np.linalg.norm(u)

        def s(x):
            return q(x)-np.outer(w, w.conj()@x) if x.ndim == 2 else q(x)-w*np.vdot(w, x)

        j = jc+np.outer(c, d)
        r = 1j*np.outer(dc, d)-np.outer(c, d@b)
        y = np.outer(z, eta)+r
        sj = s(j)
        alpha = u.conj()@q(jc)/np.vdot(u, u)
        exact_repr = q(jc-np.outer(z, alpha))
        gram = j.conj().T@sj
        ell = gram@b+b.conj().T@gram
        comm_j = t[:, None]*sj-s(t[:, None]*j)
        errors = {
            'shell_basis_orthonormal': np.linalg.norm(e.conj().T@e-np.eye(2)),
            'source_annihilation': np.linalg.norm(s(z)),
            'shell_annihilation': np.linalg.norm(s(e)),
            'full_graph_identity': np.linalg.norm(1j*t[:, None]*j-j@b-y),
            'graph_defect_annihilation': np.linalg.norm(s(r)),
            'projection_on_sample': np.linalg.norm(s(sj)-sj),
            'projected_sample_representation': np.linalg.norm(sj-exact_repr),
            'commutator_only_budget': np.linalg.norm(ell+1j*j.conj().T@comm_j),
        }
        assert max(errors.values()) < 1e-9, errors
        assert np.linalg.eigvalsh(gram)[0] > 0
        # Use the exact representation to avoid subtracting a large shell
        # correction from the small analytic output in this transform check.
        def transform(v):
            denom = 1j*t-v
            kernel = np.empty(len(n), complex)
            mask = np.abs(denom) > 1e-12
            kernel[mask] = -2*np.sinh(v*length/2)/denom[mask]
            kernel[~mask] = length*phase[~mask]
            return kernel@exact_repr/np.sqrt(length)

        strip_checks = []
        for real in (-.5, -.25, 0., .25, .5):
            for imag in (-8., -1.4, 0., .7, 8.):
                v = real+1j*imag
                target = outputs(v)-alpha*source(v)
                err = np.max(np.abs(transform(v)-target))
                strip_checks.append(float((1+abs(imag))*err))
        # The order-eight pole gives a polynomial times exp(-2 y), so
        # use the admissible strict tail rate p=1, not p=2.
        eps_bound_scale = np.exp(-.5*length/2)+length*np.exp(length/4)*(1+k/length)**(-4)
        rows.append({
            'L': length, 'K': k, 'sample_count': len(n),
            'errors': {key: float(val) for key, val in errors.items()},
            'pullback_min_eigenvalue': float(np.linalg.eigvalsh(gram)[0]),
            'weighted_strip_grid_max_error': max(strip_checks),
            'strip_bound_scale_without_constant_R6_p1': float(eps_bound_scale),
            'eigenvector_relative_defect': float(abs(ell[0, 0])/gram[0, 0].real),
            'shell_graph_norm': float(np.linalg.norm(r)),
            'source_projection_coefficient': [[float(a.real), float(a.imag)] for a in alpha],
        })
    result = {
        'scope': 'Floating-point convention checks only; no zeta zero, Weil matrix or RH evidence.',
        'model': 'Z(v)=(v-mu)^2(v-nu)/((v+2)^8(2-v)); root outputs have no poles in the closed critical strip.',
        'cutoff': 'K=4 L^2 for tractability, not the theorem cutoff.',
        'first_slot_linear': True, 'rows': rows,
    }
    Path(__file__).with_name('full_projection_checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
