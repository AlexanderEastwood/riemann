#!/usr/bin/env python3
"""Reuse the exact N=64 trial in the canonical full lambda=3 Weil form.

Computes a full residual enclosure including all omitted Fourier modes.
Overlap bounds are conditional on the independently certified complete-even spectral
threshold, explicitly labeled in the JSON. No RH or source identification
is assumed for the trial Rayleigh calculation.
"""
import hashlib,json,sys,time
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,fmpq,ctx

BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
sys.path.insert(0,str(ROOT/'g2_schur_directional'))
from assembly import assemble_sequences,parity_block
from directional_tail_gram import remote_gram_majorant

HASH='6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e'

def exact(s):
    q=Fraction(s);return arb(fmpq(q.numerator,q.denominator))

def main():
    start=time.time();bits=768;ctx.prec=bits
    source=ROOT/'g2_certificate'/'g2_finite_candidate.json'
    data=source.read_bytes();assert hashlib.sha256(data).hexdigest()==HASH
    candidate=json.loads(data);assert candidate['N']==64 and candidate['lambda_exact']=='3'
    # Preserve the precise witness locally without invoking its optional
    # non-certified numerical generator.
    (BASE/'g2_finite_candidate.json').write_bytes(data)
    c=[exact(s) for s in candidate['positive_coefficients']]
    assert len(c)==65
    s=c[0]**2+2*sum((x*x for x in c[1:]),arb(0));norm=s.sqrt()
    J=4096;L,b,d=assemble_sequences(J,bits,128)
    raw_even=arb_mat([[c[0]]]+[[arb(2).sqrt()*x] for x in c[1:]])
    we=parity_block(range(65),range(65),'even',b,d)
    alpha=(raw_even.transpose()*we*raw_even)[0,0]/s
    assert alpha>0 and alpha<exact('5.32e-38')
    for name in ['g2_finite_certificate.json','g2_finite_series_certificate.json']:
        old=json.loads((ROOT/'g2_certificate'/name).read_text())
        assert old['candidate_sha256']==HASH and alpha.overlaps(arb(old['alpha']))
    u=raw_even/norm
    # An exactly defined even correction in u-perp, using the true enclosed
    # matrix rather than treating a numerical eigenvector as an exact one.
    housevec=arb_mat(u);housevec[0,0]+=1
    eye=arb_mat([[int(i==j) for j in range(65)] for i in range(65)])
    house=eye-2*housevec*housevec.transpose()/(housevec.transpose()*housevec)[0,0]
    basis=arb_mat([[house[i,j] for j in range(1,65)] for i in range(65)])
    complement=basis.transpose()*we*basis
    eye64=arb_mat([[int(i==j) for j in range(64)] for i in range(64)])
    off=basis.transpose()*we*u
    correction=(complement-alpha*eye64).solve(off,algorithm='lu')
    q2=(correction.transpose()*correction)[0,0]
    energy=(off.transpose()*correction)[0,0]
    beta=alpha-energy/(1+q2)
    corrected_sine=(q2/(1+q2)).sqrt()
    assert beta>0 and beta<exact('3.644e-38')
    assert corrected_sine<exact('.000216')
    y=parity_block(range(J+1),range(65),'even',b,d)*u
    for n in range(65):y[n,0]-=alpha*u[n,0]
    finite_residual_squared=(y.transpose()*y)[0,0]
    full_u=arb_mat([[c[abs(n)]/norm] for n in range(-64,65)])
    full_b=[b[abs(n)] if n>=0 else -b[abs(n)] for n in range(-64,65)]
    pdat=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
    P=sum((arb(p).log()/arb(m).sqrt() for m,p in pdat),arb(0))
    B=(arb(4)/3+P+1+arb.pi()/4)/arb.pi()
    remote=remote_gram_majorant(full_u,full_b,64,J,48,B,exact('1e-6'),remainder='weighted')
    remote_upper=remote['upper'][0,0]
    residual_lower=finite_residual_squared.sqrt()
    residual_upper=(finite_residual_squared+remote_upper).sqrt()
    assert residual_upper.is_finite()

    # Exact P64 repaired-source identification is a separate imported
    # v1.13 certificate. This norm error is transferred geometrically,
    # never by perturbing an energy of order 1e-38.
    source_cert=ROOT/'g2_source_certificate'/'pswf_source_certificate.json'
    source_proof=json.loads(source_cert.read_text())
    assert source_proof['status'].startswith('PASS')
    assert source_proof['frozen_candidate_sha256']==HASH
    assert all(source_proof['checks'].values())
    eps=exact('2.60e-36')
    assert arb(source_proof['exact_repaired_source_projection_vs_frozen_norm_bound'])<eps
    rho=eps/norm
    source_normalized_distance=(2*rho*rho/(1+(1-rho*rho).sqrt())).sqrt()
    assert source_normalized_distance<exact('4e-36')
    gaps=[]
    for a in ['1e-36','1e-35','1e-34']:
        threshold=exact(a);mass=alpha/threshold;sin=mass.sqrt()
        distance=(2*mass/(1+(1-mass).sqrt())).sqrt()
        overlap=(1-mass).sqrt()
        gaps.append(dict(threshold_exact=a,
            required_hypothesis='Complete even sector positive with exactly one eigenvalue below threshold. u0 is its ground; global ordering against the odd sector is a separate certificate.',
            trial_ground_sine_upper=sin.str(65),trial_phase_aligned_distance_upper=distance.str(65),
            trial_ground_overlap_lower=overlap.str(65),
            exact_projected_source_ground_sine_upper=(sin+source_normalized_distance).str(65),
            corrected_trial_ground_sine_upper=(beta/threshold).sqrt().str(65),
            improved_original_trial_ground_sine_upper=(corrected_sine+(beta/threshold).sqrt()).str(65),
            improved_exact_projected_source_ground_sine_upper=(corrected_sine+(beta/threshold).sqrt()+source_normalized_distance).str(65),
            crude_full_residual_gap_upper=(residual_upper/(threshold-alpha)).str(65)))

    result=dict(status='PASS: full-form trial Rayleigh and complete residual enclosure.',
        scope='Rayleigh and residual are unconditional fixed-window facts. Listed ground-overlap bounds require the stated complete-even spectral threshold; global odd/even ordering is separate.',
        lambda_exact=3,N=64,trial_dimension=129,even_dimension=65,precision_bits=bits,
        candidate_sha256=HASH,first_slot_linear=True,
        physical_basis='L^(-1/2) exp(2 pi i n log(3u)/L), u in [1/3,3], zero extended.',
        source_norm=norm.str(75),source_norm_squared=s.str(75),full_form_rayleigh=alpha.str(75),
        normalized_endpoint=((c[0]+2*sum(c[1:],arb(0)))/(L*s).sqrt()).str(75),
        finite_even_correction=dict(definition='v_corr=(u-basis*z)/sqrt(1+q^2), z=(C-alpha I)^(-1)r, all in the even N64 space.',
            q_squared=q2.str(75),schur_energy=energy.str(75),
            corrected_full_rayleigh=beta.str(75),sine_to_original_trial=corrected_sine.str(75),
            corrected_rayleigh_below_3_644e_minus38=True),
        explicit_residual_rows_through=J,remote_expansion_order=48,
        finite_residual_squared=finite_residual_squared.str(75),remote_residual_squared_majorant=remote_upper.str(75),
        full_residual_lower=residual_lower.str(75),full_residual_upper=residual_upper.str(75),
        projected_source_absolute_error_imported='2.60e-36',
        projected_source_norm_lower=(norm-eps).str(75),
        projected_source_normalized_distance_upper=source_normalized_distance.str(75),
        source_certificate_sha256=hashlib.sha256(source_cert.read_bytes()).hexdigest(),
        conditional_overlap_bounds=gaps,
        checks=dict(trial_rayleigh_below_5_32e_minus38=True,independent_old_rayleigh_intervals_overlap=True,
                    normalized_projected_source_distance_below_4e_minus36=True),
        elapsed_seconds=time.time()-start)
    (BASE/'full_trial_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
