#!/usr/bin/env python3
"""
Milestone 12 Verification & Certificate Script:
Ordinate-Centered Stieltjes-Hankel Parity Separation & Davenport-Heilbronn
Off-Line Zero Screen (ZERO-GEOMETRY).

Replays all ball-arithmetic certificates at TWO precisions (256-bit and 384-bit
flint.arb / flint.acb) with zero float tolerances in ball checks.

Wall check: Does NOT prove RH, G2, or the cofinal prime-shift lower bound as a -> infinity.
Both missing-original evidence groups in evidence/MISSING.md remain OPEN.
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Any

import flint


def arb_abs(x: flint.arb) -> flint.arb:
    return abs(x)


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


def cholesky_lower_arb(mat: list[list[flint.arb]]) -> list[list[flint.arb]]:
    n = len(mat)
    l_mat = [[flint.arb(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = mat[i][j]
            for k in range(j):
                s = s - l_mat[i][k] * l_mat[j][k]
            if i == j:
                assert s > flint.arb(0), f"Cholesky pivot <= 0 at index {i}: {s}"
                l_mat[i][i] = s.sqrt()
            else:
                l_mat[i][j] = s / l_mat[j][j]
    return l_mat


def dh_kappa_arb() -> flint.arb:
    sqrt5 = flint.arb(5).sqrt()
    return ((flint.arb(10) - flint.arb(2) * sqrt5).sqrt() - flint.arb(2)) / (sqrt5 - flint.arb(1))


def g_dh_jet_acb(s: flint.acb, kappa_acb: flint.acb) -> tuple[flint.acb, flint.acb]:
    """
    Evaluate 5^s f_DH(s) = g_DH(s) and its first derivative g_DH'(s) in flint.acb
    using exact 2-term complex ball power series (flint.acb_series).
    """
    ss = flint.acb_series([s, 1], prec=2)
    c1 = flint.acb(flint.arb(1) / flint.arb(5))
    c2 = flint.acb(flint.arb(2) / flint.arb(5))
    c3 = flint.acb(flint.arb(3) / flint.arb(5))
    c4 = flint.acb(flint.arb(4) / flint.arb(5))
    res = ss.zeta(c1) + kappa_acb * ss.zeta(c2) - kappa_acb * ss.zeta(c3) - ss.zeta(c4)
    return res[0], res[1]


def zeta_jet_acb(s: flint.acb) -> tuple[flint.acb, flint.acb]:
    """
    Evaluate Riemann zeta(s) and zeta'(s) in flint.acb using flint.acb_series.
    """
    ss = flint.acb_series([s, 1], prec=2)
    res = ss.zeta()
    return res[0], res[1]


def xi_dh_on_critical_line_arb(t: flint.arb, kappa_acb: flint.acb) -> flint.arb:
    """
    Evaluate the real completed Davenport-Heilbronn function xi_DH(1/2 + i t) on the critical line.
    """
    half = flint.arb(1) / flint.arb(2)
    s = flint.acb(half, t)
    g_val, _ = g_dh_jet_acb(s, kappa_acb)
    pi_over_5 = flint.acb(flint.arb.pi() / flint.arb(5))
    pref = (pi_over_5 ** (-s / flint.acb(2))) * ((s + flint.acb(1)) / flint.acb(2)).gamma() * (flint.acb(5) ** (-s))
    val = pref * g_val
    return val.real


def xi_riemann_on_critical_line_arb(t: flint.arb) -> flint.arb:
    """
    Evaluate the real completed Riemann function xi(1/2 + i t) on the critical line.
    """
    half = flint.arb(1) / flint.arb(2)
    s = flint.acb(half, t)
    z_val, _ = zeta_jet_acb(s)
    pi_acb = flint.acb.pi()
    pref = (pi_acb ** (-s / flint.acb(2))) * (s / flint.acb(2)).gamma()
    val = pref * z_val
    return val.real


def certify_complex_newton_root(
    jet_fn: Any,
    s_seed: flint.acb,
    rad_exp: int,
    n_iter: int = 8,
    lock_critical_line: bool = False,
) -> dict[str, Any]:
    """
    Refine a complex root via Newton's method using exact flint.acb_series jets
    and certify existence and uniqueness inside B = D(s_center, 10^{-rad_exp})
    via the Complex Interval Newton Theorem:
        |g(s_center)| / inf_{z in B} |g'(z)| < r.
    """
    half = flint.arb(1) / flint.arb(2)
    s = s_seed
    for _ in range(n_iter):
        v0, v1 = jet_fn(s)
        s_next = s - v0 / v1
        re_mid = half if lock_critical_line else flint.arb(s_next.real.mid())
        im_mid = flint.arb(s_next.imag.mid())
        s = flint.acb(re_mid, im_mid)

    r = flint.arb(10) ** (-rad_exp)
    s_ball = flint.acb(flint.arb(s.real.mid(), r), flint.arb(s.imag.mid(), r))
    v0_center, _ = jet_fn(s)
    _, v1_ball = jet_fn(s_ball)
    assert not v1_ball.contains(0), f"Derivative ball contains 0 at {s}"
    step_bound = abs(v0_center) / abs(v1_ball)
    assert step_bound < r, f"Complex Interval Newton step bound {step_bound} >= r={r}"

    return {
        "beta": s_ball.real,
        "gamma": s_ball.imag,
        "newton_step_bound": step_bound,
        "box_radius": r,
    }


def eval_hankel_moments_and_minors(
    zeros: list[tuple[flint.arb, flint.arb]],
    t0: flint.arb,
    sigma: flint.arb,
) -> dict[str, Any]:
    """
    Given a list of zeros (beta_a, gamma_a), compute the ordinate-centered
    Stieltjes-Hankel moments mu_0, mu_1, mu_2, mu_3, mu_4 at center ordinate t_0
    and Gaussian scale sigma:
        z_a = (gamma_a - t0) - i (beta_a - 1/2),
        w_a = exp(-(1/2) sigma^2 z_a^2),
        mu_m = Re sum_a w_a z_a^m.
    Also verify the exact Cauchy-Binet identity:
        det H_2 = mu_0 * mu_2 - mu_1^2 = Re sum_{a < b} w_a w_b (z_a - z_b)^2.
    """
    half = flint.arb(1) / flint.arb(2)
    half_sig2 = flint.acb(half * sigma * sigma)

    z_list: list[flint.acb] = []
    w_list: list[flint.acb] = []
    for beta_a, gamma_a in zeros:
        delta_a = beta_a - half
        z_a = flint.acb(gamma_a - t0, -delta_a)
        w_a = (-half_sig2 * z_a * z_a).exp()
        z_list.append(z_a)
        w_list.append(w_a)

    moments: list[flint.arb] = []
    for m in range(5):
        s_m = flint.acb(0)
        for z_a, w_a in zip(z_list, w_list):
            s_m = s_m + w_a * (z_a**m)
        moments.append(s_m.real)

    mu0, mu1, mu2, mu3, mu4 = moments
    det_h2 = mu0 * mu2 - mu1 * mu1

    # Cauchy-Binet pairwise sum:
    cb_sum = flint.acb(0)
    n_z = len(z_list)
    for a in range(n_z):
        for b in range(a + 1, n_z):
            diff = z_list[a] - z_list[b]
            cb_sum = cb_sum + w_list[a] * w_list[b] * (diff * diff)
    cb_real = cb_sum.real
    assert (det_h2 - cb_real).contains(0), f"Cauchy-Binet mismatch: {det_h2} vs {cb_real}"

    h3_mat = [
        [mu0, mu1, mu2],
        [mu1, mu2, mu3],
        [mu2, mu3, mu4],
    ]
    det_h3 = (
        mu0 * (mu2 * mu4 - mu3 * mu3)
        - mu1 * (mu1 * mu4 - mu2 * mu3)
        + mu2 * (mu1 * mu3 - mu2 * mu2)
    )

    return {
        "mu0": mu0,
        "mu1": mu1,
        "mu2": mu2,
        "mu3": mu3,
        "mu4": mu4,
        "det_H2": det_h2,
        "cauchy_binet_H2": cb_real,
        "det_H3": det_h3,
        "H3_mat": h3_mat,
    }


def certify_stieltjes_hankel_offline_screen(prec_bits: int) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()
    rad_exp = 65 if prec_bits <= 256 else 100
    half = flint.arb(1) / flint.arb(2)

    kappa = dh_kappa_arb()
    kappa_acb = flint.acb(kappa)

    # 1. Isolate & certify the first Davenport-Heilbronn off-line zero pair rho_{DH, +/-} = 1/2 +/- delta_DH + i gamma_DH:
    dh_off_plus = certify_complex_newton_root(
        lambda s: g_dh_jet_acb(s, kappa_acb),
        flint.acb(flint.arb("0.80851718"), flint.arb("85.69934848")),
        rad_exp=rad_exp,
        lock_critical_line=False,
    )
    beta_dh = dh_off_plus["beta"]
    gamma_dh = dh_off_plus["gamma"]
    delta_dh = beta_dh - half
    assert delta_dh > flint.arb("0.3085"), f"Unexpected delta_DH: {delta_dh}"

    # Also certify the functional-equation twin rho_{DH, -} = (1 - beta_DH) + i gamma_DH directly:
    dh_off_minus = certify_complex_newton_root(
        lambda s: g_dh_jet_acb(s, kappa_acb),
        flint.acb(flint.arb(1) - beta_dh, gamma_dh),
        rad_exp=rad_exp,
        lock_critical_line=False,
    )
    assert ((flint.arb(1) - beta_dh) - dh_off_minus["beta"]).contains(0)
    assert (gamma_dh - dh_off_minus["gamma"]).contains(0)

    # 2. Isolate & certify the 8 neighboring critical-line zeros of f_DH(1/2 + i t) in [78, 93]:
    dh_online_seeds = [78.725, 80.325, 81.925, 83.125, 87.625, 89.425, 90.725, 92.175]
    dh_window_zeros: list[tuple[flint.arb, flint.arb]] = [
        (beta_dh, gamma_dh),
        (dh_off_minus["beta"], dh_off_minus["gamma"]),
    ]
    dh_online_certified: list[dict[str, Any]] = []
    for t_seed in dh_online_seeds:
        cert = certify_complex_newton_root(
            lambda s: g_dh_jet_acb(s, kappa_acb),
            flint.acb(half, flint.arb(str(t_seed))),
            rad_exp=rad_exp,
            lock_critical_line=True,
        )
        gam_k = cert["gamma"]
        # Verify real sign change of xi_DH(1/2 + i t) across [gam_k - 10^-6, gam_k + 10^-6] to prove beta = 1/2:
        eps_sign = flint.arb(1) / flint.arb(10**6)
        v_lo = xi_dh_on_critical_line_arb(flint.arb(gam_k.mid()) - eps_sign, kappa_acb)
        v_hi = xi_dh_on_critical_line_arb(flint.arb(gam_k.mid()) + eps_sign, kappa_acb)
        assert v_lo * v_hi < flint.arb(0), f"No critical-line sign change for DH zero near {t_seed}"
        dh_window_zeros.append((half, gam_k))
        dh_online_certified.append(
            {
                "gamma": arb_to_dict(gam_k),
                "newton_step_bound": arb_to_dict(cert["newton_step_bound"]),
                "critical_line_sign_change": True,
            }
        )

    # 3. Isolate & certify the 6 neighboring critical-line zeros of Riemann zeta(1/2 + i t) in [78, 93]:
    zeta_window_seeds = [79.325, 82.925, 84.725, 87.425, 88.825, 92.475]
    zeta_window_zeros: list[tuple[flint.arb, flint.arb]] = []
    zeta_window_certified: list[dict[str, Any]] = []
    for t_seed in zeta_window_seeds:
        cert = certify_complex_newton_root(
            zeta_jet_acb,
            flint.acb(half, flint.arb(str(t_seed))),
            rad_exp=rad_exp,
            lock_critical_line=True,
        )
        gam_k = cert["gamma"]
        eps_sign = flint.arb(1) / flint.arb(10**6)
        v_lo = xi_riemann_on_critical_line_arb(flint.arb(gam_k.mid()) - eps_sign)
        v_hi = xi_riemann_on_critical_line_arb(flint.arb(gam_k.mid()) + eps_sign)
        assert v_lo * v_hi < flint.arb(0), f"No critical-line sign change for Riemann zero near {t_seed}"
        zeta_window_zeros.append((half, gam_k))
        zeta_window_certified.append(
            {
                "gamma": arb_to_dict(gam_k),
                "newton_step_bound": arb_to_dict(cert["newton_step_bound"]),
                "critical_line_sign_change": True,
            }
        )

    # 4. Evaluate the Ordinate-Centered Stieltjes-Hankel Screen at t_0 = gamma_DH across sigma in {1.5, 2.0, 2.5, 3.0}:
    sigma_grid = [
        flint.arb(3) / flint.arb(2),
        flint.arb(2),
        flint.arb(5) / flint.arb(2),
        flint.arb(3),
    ]
    screen_at_gamma_dh: list[dict[str, Any]] = []
    for sig in sigma_grid:
        dh_res = eval_hankel_moments_and_minors(dh_window_zeros, gamma_dh, sig)
        zeta_res = eval_hankel_moments_and_minors(zeta_window_zeros, gamma_dh, sig)

        # Intrinsic off-line dipole pair formulas from Theorem 1(2)-(3):
        amp_pair = (half * sig * sig * delta_dh * delta_dh).exp()
        mu2_dipole_pair = -flint.arb(2) * (delta_dh * delta_dh) * amp_pair
        cb_dipole_pair = -flint.arb(4) * (delta_dh * delta_dh) * (amp_pair * amp_pair)

        # Certify strict negativity on Davenport-Heilbronn at t_0 = gamma_DH:
        assert dh_res["mu2"] < flint.arb(0), f"DH mu2 >= 0 at sigma={sig}: {dh_res['mu2']}"
        assert dh_res["det_H2"] < flint.arb(0), f"DH det_H2 >= 0 at sigma={sig}: {dh_res['det_H2']}"

        # Certify strict positivity on Riemann zeta at t_0 = gamma_DH (including 3x3 Cholesky of H_3):
        assert zeta_res["mu0"] > flint.arb(0)
        assert zeta_res["mu2"] > flint.arb(0)
        assert zeta_res["det_H2"] > flint.arb(0)
        assert zeta_res["det_H3"] > flint.arb(0)
        l_zeta_h3 = cholesky_lower_arb(zeta_res["H3_mat"])

        screen_at_gamma_dh.append(
            {
                "sigma": arb_to_dict(sig),
                "dipole_amplification_factor": arb_to_dict(amp_pair),
                "dipole_pair_mu2_contribution": arb_to_dict(mu2_dipole_pair),
                "dipole_pair_cauchy_binet_minor": arb_to_dict(cb_dipole_pair),
                "davenport_heilbronn": {
                    "mu0": arb_to_dict(dh_res["mu0"]),
                    "mu1": arb_to_dict(dh_res["mu1"]),
                    "mu2": arb_to_dict(dh_res["mu2"]),
                    "det_H2": arb_to_dict(dh_res["det_H2"]),
                    "cauchy_binet_H2": arb_to_dict(dh_res["cauchy_binet_H2"]),
                    "det_H3": arb_to_dict(dh_res["det_H3"]),
                    "mu2_strictly_negative": True,
                    "det_H2_strictly_negative": True,
                },
                "riemann_zeta": {
                    "mu0": arb_to_dict(zeta_res["mu0"]),
                    "mu1": arb_to_dict(zeta_res["mu1"]),
                    "mu2": arb_to_dict(zeta_res["mu2"]),
                    "det_H2": arb_to_dict(zeta_res["det_H2"]),
                    "cauchy_binet_H2": arb_to_dict(zeta_res["cauchy_binet_H2"]),
                    "det_H3": arb_to_dict(zeta_res["det_H3"]),
                    "cholesky_pivots_H3": [arb_to_dict(l_zeta_h3[i][i]) for i in range(3)],
                    "H3_positive_definite": True,
                },
            }
        )

    # 5. Also isolate and certify the first 10 low-lying Riemann zeros gamma_1 .. gamma_10 and verify H_3 > 0 at each:
    first_10_seeds = [
        "14.13472514",
        "21.02203964",
        "25.01085758",
        "30.42487613",
        "32.93506159",
        "37.58617816",
        "40.91871901",
        "43.32707328",
        "48.00515088",
        "49.77383248",
    ]
    first_10_zeros: list[tuple[flint.arb, flint.arb]] = []
    for s_str in first_10_seeds:
        c_z = certify_complex_newton_root(
            zeta_jet_acb,
            flint.acb(half, flint.arb(s_str)),
            rad_exp=rad_exp,
            lock_critical_line=True,
        )
        first_10_zeros.append((half, c_z["gamma"]))

    sig_scan = flint.arb(1)
    first_10_hankel_checks: list[dict[str, Any]] = []
    for idx_z, (_, gam_z) in enumerate(first_10_zeros):
        res_z = eval_hankel_moments_and_minors(first_10_zeros, gam_z, sig_scan)
        l_z = cholesky_lower_arb(res_z["H3_mat"])
        first_10_hankel_checks.append(
            {
                "index": idx_z + 1,
                "gamma_n": arb_to_dict(gam_z),
                "mu0": arb_to_dict(res_z["mu0"]),
                "mu2": arb_to_dict(res_z["mu2"]),
                "det_H2": arb_to_dict(res_z["det_H2"]),
                "det_H3": arb_to_dict(res_z["det_H3"]),
                "min_cholesky_pivot": arb_to_dict(min((l_z[i][i] for i in range(3)), key=lambda x: float(x.lower()))),
                "H3_positive_definite": True,
            }
        )

    return {
        "prec_bits": prec_bits,
        "dh_offline_zero_pair": {
            "beta_plus": arb_to_dict(beta_dh),
            "beta_minus": arb_to_dict(dh_off_minus["beta"]),
            "delta_DH": arb_to_dict(delta_dh),
            "gamma_DH": arb_to_dict(gamma_dh),
            "newton_step_bound": arb_to_dict(dh_off_plus["newton_step_bound"]),
            "box_radius": arb_to_dict(dh_off_plus["box_radius"]),
        },
        "dh_neighboring_online_zeros": dh_online_certified,
        "zeta_neighboring_online_zeros": zeta_window_certified,
        "hankel_screen_at_gamma_DH": screen_at_gamma_dh,
        "first_10_riemann_zeros_hankel_scan": first_10_hankel_checks,
        "elapsed_s": round(time.time() - t0, 4),
    }


def verify_two_precision_consistency(res_256: dict[str, Any], res_384: dict[str, Any]) -> dict[str, Any]:
    flint.ctx.prec = 384
    checks = 0
    for key in ("beta_plus", "beta_minus", "delta_DH", "gamma_DH"):
        b256 = flint.arb(res_256["dh_offline_zero_pair"][key]["str"])
        b384 = flint.arb(res_384["dh_offline_zero_pair"][key]["str"])
        assert b256.overlaps(b384), f"Ball mismatch on dh_offline_zero_pair[{key}]"
        checks += 1

    for s256, s384 in zip(res_256["hankel_screen_at_gamma_DH"], res_384["hankel_screen_at_gamma_DH"]):
        for fam in ("davenport_heilbronn", "riemann_zeta"):
            for k in ("mu0", "mu2", "det_H2", "det_H3"):
                b256 = flint.arb(s256[fam][k]["str"])
                b384 = flint.arb(s384[fam][k]["str"])
                assert b256.overlaps(b384), f"Ball mismatch on {fam}[{k}]"
                checks += 1

    for z256, z384 in zip(
        res_256["first_10_riemann_zeros_hankel_scan"],
        res_384["first_10_riemann_zeros_hankel_scan"],
    ):
        for k in ("gamma_n", "mu0", "mu2", "det_H2", "det_H3"):
            b256 = flint.arb(z256[k]["str"])
            b384 = flint.arb(z384[k]["str"])
            assert b256.overlaps(b384)
            checks += 1

    return {
        "precisions_compared": [256, 384],
        "num_ball_overlap_checks": checks,
        "all_overlaps_verified": True,
    }


def main() -> None:
    t_start = time.time()
    out_dir = Path(__file__).resolve().parent

    res_256 = certify_stieltjes_hankel_offline_screen(256)
    res_384 = certify_stieltjes_hankel_offline_screen(384)
    consistency = verify_two_precision_consistency(res_256, res_384)

    payload: dict[str, Any] = {
        "audit_id": "stieltjes-hankel-offline-zero-signal-and-dh-screen-2026-10-15-v1",
        "date": "2026-10-15",
        "lanes": ["ZERO-GEOMETRY"],
        "wall_check": {
            "rh_proved": False,
            "g2_completed": False,
            "cofinal_prime_shift_lower_bound_proved": False,
            "missing_historical_evidence_recovered": False,
            "open_obligations": [
                "Riemann Hypothesis (RH)",
                "Global archimedean completion (G2)",
                "Cofinal signed-arithmetic lower bound as a -> infinity",
                "Historical missing-original evidence groups in evidence/MISSING.md (stage4_run_summary.json / stage4_Ticks.json and certificate.json / verify_log.txt)",
            ],
        },
        "two_precision_consistency": consistency,
        "primary_384bit": res_384,
        "secondary_256bit": res_256,
        "total_elapsed_s": round(time.time() - t_start, 4),
    }

    ver_path = out_dir / "verification.json"
    raw_bytes = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
    payload_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    payload["sha256"] = payload_sha256
    ver_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    file_sha256 = hashlib.sha256(ver_path.read_bytes()).hexdigest()

    print("=== Milestone 12 Verification Complete ===")
    print(f"Two-precision consistency (256 vs 384 bits): {consistency['num_ball_overlap_checks']} checks PASS")
    pair = res_384["dh_offline_zero_pair"]
    print(
        f"Certified DH off-line zero: beta={pair['beta_plus']['mid']:.10f}, "
        f"delta={pair['delta_DH']['mid']:.10f}, gamma={pair['gamma_DH']['mid']:.10f}"
    )
    for row in res_384["hankel_screen_at_gamma_DH"]:
        sig = row["sigma"]["mid"]
        dh = row["davenport_heilbronn"]
        zt = row["riemann_zeta"]
        print(
            f"  sigma={sig:.1f}: DH mu2={dh['mu2']['upper']:.6f} < 0, det_H2={dh['det_H2']['upper']:.6f} < 0 | "
            f"Zeta mu2={zt['mu2']['lower']:.6f} > 0, det_H2={zt['det_H2']['lower']:.6f} > 0"
        )
    print(f"verification.json payload.sha256 = {payload_sha256}")
    print(f"verification.json file_sha256    = {file_sha256}")


if __name__ == "__main__":
    main()
