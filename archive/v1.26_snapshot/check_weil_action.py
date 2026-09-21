"""Actual finite Weil action at the first known critical-line zero.

Uses the historical arithmetic matrix implementation, including its logarithmic
diagonal. Floating-point convention check, not a certified estimate or RH test.
The moderate cutoffs are much smaller than the analytic theorem's cutoff.
"""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
from check_sampler import weil_matrix, hardy_samples, SIGMA, A, M


def main():
    mp.mp.dps = 40
    root = mp.zetazero(1)
    mu = complex(root-mp.mpf('.5'))
    kap = SIGMA*(SIGMA+A)**M/(SIGMA-1)*(root-1)/((root+A)**M*(SIGMA-root))
    residue = complex(kap*mp.diff(mp.zeta, root))
    rows = []
    quadrature_action_difference = None
    for length in (4., 6., 8., 10.):
        nmax = 512
        raw = hardy_samples(length, nmax)
        wmat = weil_matrix(length, nmax)
        for k in (128, 256):
            cut = 2*k
            sl = slice(nmax-cut, nmax+cut+1)
            n = np.arange(-cut, cut+1)
            t = 2*np.pi*n/length
            phase = np.where(n % 2 == 0, 1., -1.)
            z = raw[sl]*phase
            jc = z/(1j*t-mu)
            c = np.where(np.abs(n)>k, np.sqrt(length)/(2*k), 0.)
            dc = t*c
            e = np.column_stack((c/np.linalg.norm(c), dc/np.linalg.norm(dc)))
            def q(v):
                return v-e@(e.conj().T@v)
            u = q(z)
            alpha = np.vdot(u,q(jc))/np.vdot(u,u)
            projected = q(jc-alpha*z)
            action = wmat[sl,sl]@projected
            # Coefficients in the original [0,L] basis of the projection
            # of residue*exp(mu*(x-L/2)); the two half-period phases cancel.
            target = residue*2*np.sinh(mu*length/2)/(np.sqrt(length)*(mu-1j*t))
            error = np.linalg.norm(action-target)
            rows.append({'L':length,'K':k,'N':cut,
                         'action_norm':float(np.linalg.norm(action)),
                         'target_projected_norm':float(np.linalg.norm(target)),
                         'action_error':float(error),
                         'relative_action_error':float(error/np.linalg.norm(target)),
                         'self_form_real':float(np.vdot(projected,action).real),
                         'squared_metric_mass':float(np.vdot(action,action).real)})
        print(json.dumps(rows[-1]),flush=True)
        if length == 10.:
            refined = weil_matrix(length, nmax, extra_nodes=400)
            quadrature_action_difference = float(np.linalg.norm((refined-wmat)@projected))
            assert quadrature_action_difference < 1e-9
    # Direct independent physical quadrature for the target coefficient.
    length,n = 6.,7
    exact = residue*2*np.sinh(mu*length/2)/(np.sqrt(length)*(mu-2j*np.pi*n/length))
    integral = complex(mp.quad(lambda y: kap*mp.diff(mp.zeta,root)*mp.exp((root-.5)*y)
                   *mp.exp(-2j*mp.pi*n*(y+length/2)/length)/mp.sqrt(length),[-length/2,length/2]))
    delta = abs(exact-integral)
    assert delta < 1e-12
    result = {'scope':'Actual finite arithmetic Weil matrix and first known critical-line zero; floating-point convention checks, not interval certificates or RH evidence.',
              'root_imaginary':float(mp.im(root)), 'root_numerical_zeta_residual':float(abs(mp.zeta(root))),
              'assumed_numerical_multiplicity':1,
              'sigma':SIGMA,'a':A,'M':M,'mpmath_digits':40,
              'target_coefficient_quadrature_error':float(delta),
              'extra_400_nodes_action_difference_L10_N512':quadrature_action_difference,
              'cutoff_warning':'Moderate K=128,256; theorem cutoff is not numerically attained.',
              'rows':rows}
    Path(__file__).with_name('weil_action_checks.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
