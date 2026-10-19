"""Regression tests for the October 15-16 18/18 pure-flint bounded repair audit,
synthesis correction (v17), and full-residual NB arithmetic-lemma stop report."""
import ast
import glob
import hashlib
import json
import os
import re
import unittest
from typing import Any, Dict, List, Set


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

EXPECTED_PACKAGES: List[str] = [
    "all-vector-positivity-beyond-log6-2026-10-15-v1",
    "all-vector-positivity-beyond-log7-2026-10-15-v1",
    "all-vector-positivity-three-island-horizon-2026-10-15-v1",
    "codex-review-and-all-vector-extension-2026-10-15-v1",
    "euler-depleted-weil-equivalence-and-dh-control-2026-10-15-v1",
    "higher-order-wronskian-hankel-hierarchy-2026-10-15-v1",
    "infinite-dimensional-tail-floor-and-shift-coupling-defect-2026-10-15-v1",
    "mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1",
    "multimode-dyadic-extractor-2026-10-15-v1",
    "multiprime-euler-preconditioner-2026-10-15-v1",
    "multiprime-internal-shift-and-block-interlacing-2026-10-15-v1",
    "multiprime-three-prime-and-scaling-2026-10-15-v1",
    "next-four-steps-2026-10-15-v1",
    "signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1",
    "stieltjes-hankel-offline-zero-signal-and-dh-screen-2026-10-15-v1",
    "three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1",
    "universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1",
    "untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1",
]

FORBIDDEN_IMPORTS = {"numpy", "scipy", "mpmath"}


def _collect_nested_sha256(obj: Any, out: Set[str]) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and len(v) == 64 and all(c in "0123456789abcdef" for c in v):
                out.add(v)
            else:
                _collect_nested_sha256(v, out)
    elif isinstance(obj, list):
        for item in obj:
            _collect_nested_sha256(item, out)


class Oct15BoundedRepairAuditTests(unittest.TestCase):
    def test_all_18_packages_present_and_complete(self) -> None:
        audits_dir = os.path.join(REPO_ROOT, "audits")
        found_dirs = sorted(
            os.path.basename(p)
            for p in glob.glob(os.path.join(audits_dir, "*2026-10-15*"))
            if os.path.isdir(p)
        )
        self.assertEqual(found_dirs, EXPECTED_PACKAGES)
        for pkg in EXPECTED_PACKAGES:
            pkg_dir = os.path.join(audits_dir, pkg)
            for req in ("README.md", "derivation.md", "PROPOSAL.md", "verification.json"):
                self.assertTrue(
                    os.path.isfile(os.path.join(pkg_dir, req)),
                    f"Missing {req} in {pkg}",
                )
            verifiers = glob.glob(os.path.join(pkg_dir, "verify_*.py"))
            self.assertEqual(len(verifiers), 1, f"Expected 1 verifier in {pkg}, got {verifiers}")

    def test_zero_floating_point_and_tolerance_dependencies(self) -> None:
        audits_dir = os.path.join(REPO_ROOT, "audits")
        symreal_packages = {
            "all-vector-positivity-beyond-log6-2026-10-15-v1",
            "all-vector-positivity-beyond-log7-2026-10-15-v1",
            "all-vector-positivity-three-island-horizon-2026-10-15-v1",
            "multiprime-euler-preconditioner-2026-10-15-v1",
            "multiprime-three-prime-and-scaling-2026-10-15-v1",
            "multiprime-internal-shift-and-block-interlacing-2026-10-15-v1",
            "three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1",
            "universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1",
            "euler-depleted-weil-equivalence-and-dh-control-2026-10-15-v1",
        }
        forbidden_tol_literals = (
            "1e-65",
            "1e-80",
            "1e-90",
            "1e-100",
            "1e-15",
            "1e-13",
            "1e-12",
            "1e-11",
            "1e-10",
        )
        for pkg in EXPECTED_PACKAGES:
            verifiers = glob.glob(os.path.join(audits_dir, pkg, "verify_*.py"))
            vpath = verifiers[0]
            with open(vpath, "r", encoding="utf-8") as f:
                src = f.read()
            tree = ast.parse(src, filename=vpath)
            docstring_nodes = set()
            for node in ast.walk(tree):
                if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    if (
                        node.body
                        and isinstance(node.body[0], ast.Expr)
                        and isinstance(node.body[0].value, ast.Constant)
                        and isinstance(node.body[0].value.value, str)
                    ):
                        docstring_nodes.add(node.body[0].value)
            class_names = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        root_mod = alias.name.split(".")[0]
                        self.assertNotIn(root_mod, FORBIDDEN_IMPORTS, f"Forbidden import {alias.name} in {vpath}")
                elif isinstance(node, ast.ImportFrom) and node.module:
                    root_mod = node.module.split(".")[0]
                    self.assertNotIn(root_mod, FORBIDDEN_IMPORTS, f"Forbidden import from {node.module} in {vpath}")
                elif isinstance(node, ast.FunctionDef):
                    self.assertNotEqual(
                        node.name,
                        "deduplicate_and_sort_arb",
                        f"Forbidden deduplicate_and_sort_arb in {vpath}",
                    )
                elif isinstance(node, ast.ClassDef):
                    class_names.add(node.name)
                elif (
                    isinstance(node, ast.Constant)
                    and isinstance(node.value, str)
                    and node not in docstring_nodes
                ):
                    self.assertNotIn(
                        node.value.strip(),
                        forbidden_tol_literals,
                        f"Decimal tolerance literal {node.value} found in executable AST node in {vpath}",
                    )
            self.assertNotIn("deduplicate_and_sort_arb", src, f"deduplicate_and_sort_arb found in {vpath}")
            if pkg in symreal_packages:
                self.assertIn("SymReal", class_names, f"Expected SymReal symbolic cut-point class in {vpath}")

    def test_verification_json_hashes_and_readme_sync(self) -> None:
        audits_dir = os.path.join(REPO_ROOT, "audits")
        for pkg in EXPECTED_PACKAGES:
            pkg_dir = os.path.join(audits_dir, pkg)
            vpath = os.path.join(pkg_dir, "verification.json")
            rpath = os.path.join(pkg_dir, "README.md")
            with open(vpath, "rb") as fb:
                raw_bytes = fb.read()
            actual_file_sha = hashlib.sha256(raw_bytes).hexdigest()
            data: Dict[str, Any] = json.loads(raw_bytes.decode("utf-8"))
            with open(rpath, "r", encoding="utf-8") as fr:
                readme_txt = fr.read()
            self.assertIn(
                actual_file_sha[:16],
                readme_txt,
                f"verification.json file_sha256 prefix {actual_file_sha[:16]} missing from {pkg}/README.md",
            )
            if "audit_integrity" in data and "sha256_of_payload" in data["audit_integrity"]:
                pay_sha = str(data["audit_integrity"]["sha256_of_payload"])
                self.assertIn(pay_sha[:16], readme_txt, f"payload sha256 missing from {pkg}/README.md")
            elif "audit_Integrity_Check" in data and "payload_sha256" in data["audit_Integrity_Check"]:
                pay_sha = str(data["audit_Integrity_Check"]["payload_sha256"])
                self.assertIn(pay_sha[:16], readme_txt, f"payload_sha256 missing from {pkg}/README.md")

    def test_zero_stale_hashes_or_forbidden_claims_in_package_docs(self) -> None:
        audits_dir = os.path.join(REPO_ROOT, "audits")
        for pkg in EXPECTED_PACKAGES:
            pkg_dir = os.path.join(audits_dir, pkg)
            vpath = os.path.join(pkg_dir, "verification.json")
            pypath = glob.glob(os.path.join(pkg_dir, "verify_*.py"))[0]
            with open(vpath, "rb") as fb:
                vbytes = fb.read()
            with open(pypath, "rb") as fb:
                pybytes = fb.read()
            valid_hashes: Set[str] = {
                hashlib.sha256(vbytes).hexdigest(),
                hashlib.sha256(pybytes).hexdigest(),
            }
            vdata: Dict[str, Any] = json.loads(vbytes.decode("utf-8"))
            _collect_nested_sha256(vdata, valid_hashes)
            for doc_name in ("README.md", "PROPOSAL.md", "derivation.md"):
                doc_path = os.path.join(pkg_dir, doc_name)
                with open(doc_path, "r", encoding="utf-8") as fd:
                    doc_txt = fd.read()
                for hex_match in re.findall(r"\b[0-9a-f]{64}\b", doc_txt):
                    if not hex_match.isdigit():
                        self.assertIn(
                            hex_match,
                            valid_hashes,
                            f"Stale SHA-256 hash {hex_match} in {pkg}/{doc_name} (valid: {valid_hashes})",
                        )
                self.assertNotIn(
                    "deduplicate_and_sort_arb",
                    doc_txt,
                    f"Forbidden deduplicate_and_sort_arb reference in {pkg}/{doc_name}",
                )

    def test_synthesis_v17_and_nb_assessment_invariants(self) -> None:
        audits_dir = os.path.join(REPO_ROOT, "audits")
        v16_path = os.path.join(audits_dir, "coeff-specialist-brief-2026-10-15-v16.html")
        v17_path = os.path.join(audits_dir, "coeff-specialist-brief-2026-10-16-v17.html")
        v18_path = os.path.join(audits_dir, "coeff-specialist-brief-2026-10-16-v18.html")
        v19_path = os.path.join(audits_dir, "coeff-specialist-brief-2026-10-16-v19.html")
        v20_path = os.path.join(audits_dir, "coeff-specialist-brief-2026-10-16-v20.html")
        m3_v2_path = os.path.join(audits_dir, "all-vector-positivity-beyond-log6-2026-10-15-v2.html")
        m4_v3_path = os.path.join(audits_dir, "all-vector-positivity-beyond-log7-2026-10-15-v3.html")
        m5_v3_path = os.path.join(audits_dir, "all-vector-positivity-three-island-horizon-2026-10-15-v3.html")
        nb_path = os.path.join(audits_dir, "nb-full-residual-arithmetic-assessment-2026-10-16-v1.html")
        wf_path = os.path.join(audits_dir, "weil-floor-cofinal-arithmetic-assessment-2026-10-16-v1.html")
        zg_path = os.path.join(audits_dir, "zero-geometry-arithmetic-assessment-2026-10-16-v1.html")
        next_steps_path = os.path.join(REPO_ROOT, "NEXT_STEPS.md")

        for req_html in (
            v16_path,
            v17_path,
            v18_path,
            v19_path,
            v20_path,
            m3_v2_path,
            m4_v3_path,
            m5_v3_path,
            nb_path,
            wf_path,
            zg_path,
        ):
            self.assertTrue(os.path.isfile(req_html), f"Required HTML report missing: {req_html}")

        for brief_path in (v17_path, v18_path, v19_path, v20_path):
            with open(brief_path, "r", encoding="utf-8") as f:
                brief_txt = f.read()
            self.assertIn("Fourier leakage above", brief_txt)
            self.assertIn("prop:v121-cofinal-rh", brief_txt)
            self.assertIn("prop:v138-shifted-floor", brief_txt)

        with open(nb_path, "r", encoding="utf-8") as f:
            nb_txt = f.read()
        for required_token in ("NS87/98", "PR66/68", "NS74", "NS83", "Candidate A", "Candidate B", "Candidate C"):
            self.assertIn(required_token, nb_txt)

        with open(wf_path, "r", encoding="utf-8") as f:
            wf_txt = f.read()
        for required_token in (
            "prop:v136-bounded-floor",
            "prop:v138-shifted-floor",
            "thm:ns57-bounded-floor-stability",
            "Candidate I",
            "Candidate II",
            "Candidate III",
        ):
            self.assertIn(required_token, wf_txt)

        with open(zg_path, "r", encoding="utf-8") as f:
            zg_txt = f.read()
        for required_token in (
            "NS94/100/101",
            "OPERATOR-BRIDGES",
            "two-prime-contact",
            "geometric-swarm",
            "Candidate I",
            "Candidate II",
            "Candidate III",
        ):
            self.assertIn(required_token, zg_txt)

        with open(next_steps_path, "r", encoding="utf-8") as f:
            ns_txt = f.read()
        self.assertIn("coeff-specialist-brief-2026-10-16-v20.html", ns_txt)
        self.assertIn("coeff-specialist-brief-2026-10-16-v19.html", ns_txt)
        self.assertIn("coeff-specialist-brief-2026-10-16-v18.html", ns_txt)
        self.assertIn("coeff-specialist-brief-2026-10-16-v17.html", ns_txt)
        self.assertIn("nb-full-residual-arithmetic-assessment-2026-10-16-v1.html", ns_txt)
        self.assertIn("weil-floor-cofinal-arithmetic-assessment-2026-10-16-v1.html", ns_txt)
        self.assertIn("zero-geometry-arithmetic-assessment-2026-10-16-v1.html", ns_txt)
        self.assertIn("cofinal-candidate-mechanisms-screen-2026-10-16-v1.html", ns_txt)
        self.assertIn("cofinal-candidate-mechanisms-screen-2026-10-16-v2.html", ns_txt)
        self.assertIn("cofinal-candidate-mechanisms-screen-2026-10-16-v3.html", ns_txt)
        self.assertIn("cofinal-candidate-mechanisms-screen-2026-10-16-v4.html", ns_txt)
        self.assertIn("cofinal-candidate-mechanisms-screen-2026-10-16-v5.html", ns_txt)
        self.assertIn(
            "Final wall check: Same open gap. Closest: NS87/98 and PR66/68. No new arithmetic input has yet been supplied.",
            ns_txt,
        )
        self.assertIn(
            "Final wall check: Same open gap. Closest: WEIL-FLOOR (NS24/34/39/43/47/49/50, v1.36/v1.38/v1.53) and KERNEL-API (NS51/55/57/58). No new arithmetic input has yet been supplied.",
            ns_txt,
        )
        self.assertIn(
            "Final wall check: Same open gap. Closest: WEIL-FLOOR (NS24/39/43), NB-GAIN (NS53/61/83/87/98), and ZERO-GEOMETRY / OPERATOR-BRIDGES (NS94/100/101, two-prime-contact, geometric-swarm). No new uniform arithmetic estimate is supplied.",
            ns_txt,
        )

    def test_oct16_cofinal_candidate_mechanisms_screen_package(self) -> None:
        """Verify two-precision candidate-mechanism screen package, hashes, and AST imports."""
        audits_dir = os.path.join(REPO_ROOT, "audits")
        pkg_dir = os.path.join(audits_dir, "cofinal-candidate-mechanisms-screen-2026-10-16-v1")
        script_path = os.path.join(pkg_dir, "verify_cofinal_candidate_mechanisms.py")
        json_path = os.path.join(pkg_dir, "verification.json")
        readme_path = os.path.join(pkg_dir, "README.md")
        proposal_path = os.path.join(pkg_dir, "PROPOSAL.md")
        deriv_path = os.path.join(pkg_dir, "derivation.md")
        html_v1_path = os.path.join(audits_dir, "cofinal-candidate-mechanisms-screen-2026-10-16-v1.html")
        html_v2_path = os.path.join(audits_dir, "cofinal-candidate-mechanisms-screen-2026-10-16-v2.html")
        html_v3_path = os.path.join(audits_dir, "cofinal-candidate-mechanisms-screen-2026-10-16-v3.html")
        html_v4_path = os.path.join(audits_dir, "cofinal-candidate-mechanisms-screen-2026-10-16-v4.html")
        html_v5_path = os.path.join(audits_dir, "cofinal-candidate-mechanisms-screen-2026-10-16-v5.html")

        for req_file in (
            script_path,
            json_path,
            readme_path,
            proposal_path,
            deriv_path,
            html_v1_path,
            html_v2_path,
            html_v3_path,
            html_v4_path,
            html_v5_path,
        ):
            self.assertTrue(os.path.isfile(req_file), f"Missing required file: {req_file}")

        with open(script_path, "r", encoding="utf-8") as sf:
            tree = ast.parse(sf.read(), filename=script_path)
        imported_roots: Set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_roots.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".")[0])
        self.assertEqual(imported_roots & FORBIDDEN_IMPORTS, set())

        with open(json_path, "rb") as bf:
            raw_bytes = bf.read()
        actual_file_sha = hashlib.sha256(raw_bytes).hexdigest()
        data = json.loads(raw_bytes.decode("utf-8"))
        recorded_payload_sha = data["audit_integrity"]["sha256_of_payload"]
        payload_core = {k: v for k, v in data.items() if k != "audit_integrity"}
        recomputed_payload_sha = hashlib.sha256(
            json.dumps(payload_core, sort_keys=True).encode("utf-8")
        ).hexdigest()
        self.assertEqual(recorded_payload_sha, recomputed_payload_sha)
        self.assertEqual(
            recorded_payload_sha,
            "6ccc8fcb120ad5d3b4146c04d8ac03d737d14ba22b260d9edaa1e1d53c28f766",
        )
        self.assertEqual(
            actual_file_sha,
            "800004ef7eb9578617a6a4895108b33ba6cc749a4a6cd8b3dab5db93885dc190",
        )
        self.assertEqual(data["dual_precision_ball_overlap_checks"]["total_checked"], 176)
        self.assertTrue(data["dual_precision_ball_overlap_checks"]["all_passed"])
        self.assertTrue(data["dual_precision_ball_overlap_checks"]["non_overlapping_self_test_passed"])
        self.assertIn("abs_T2_at_rho1", data["cert_256"]["nb_gain_candidates_a_b_c"])
        for row in data["cert_256"]["weil_floor_and_kernel_api_windows"]:
            self.assertIn("full_space_h_even_rel_parseval_tail", row)
            self.assertIn("full_space_xh_odd_rel_parseval_tail", row)
            self.assertIn("full_space_exterior_pole_leakage_bound", row)
            self.assertIn("full_space_ap_quadratic_form_h_even", row)
            self.assertIn("omitted_v8_perp_ap_coupling_h_even", row)
            self.assertIn("full_space_ap_quadratic_form_xh_odd", row)
            self.assertIn("omitted_v8_perp_ap_coupling_xh_odd", row)

        for doc_path in (readme_path, html_v5_path):
            with open(doc_path, "r", encoding="utf-8") as f:
                txt = f.read()
            self.assertIn(recorded_payload_sha, txt)
            self.assertIn(actual_file_sha, txt)

    def test_independent_arb_ball_overlaps_and_identities(self) -> None:
        """Independently reconstruct flint.arb balls from verification.json and verify all 176 overlaps, tail bounds, and kernel enclosures."""
        import importlib.util
        import flint

        flint.ctx.prec = 384
        audits_dir = os.path.join(REPO_ROOT, "audits")
        pkg_dir = os.path.join(audits_dir, "cofinal-candidate-mechanisms-screen-2026-10-16-v1")
        json_path = os.path.join(pkg_dir, "verification.json")
        script_path = os.path.join(pkg_dir, "verify_cofinal_candidate_mechanisms.py")
        with open(json_path, "r", encoding="utf-8") as f:
            data: Dict[str, Any] = json.load(f)

        checked_pairs: List[str] = []

        def check_recursive_overlaps(a: Any, b: Any, path: str) -> None:
            if isinstance(a, dict) and isinstance(b, dict):
                if "str" in a and "str" in b and "lower" in a and "upper" in a:
                    ba = flint.arb(str(a["str"]))
                    bb = flint.arb(str(b["str"]))
                    self.assertTrue(
                        bool(ba.overlaps(bb)),
                        f"Independent flint.arb overlap failed at {path}: {ba} vs {bb}",
                    )
                    self.assertLessEqual(
                        max(float(a["lower"]), float(b["lower"])),
                        min(float(a["upper"]), float(b["upper"])),
                        f"Float endpoint overlap failed at {path}",
                    )
                    checked_pairs.append(path)
                else:
                    for k in a:
                        if k != "prec_bits" and k in b:
                            check_recursive_overlaps(a[k], b[k], f"{path}.{k}")
            elif isinstance(a, list) and isinstance(b, list):
                self.assertEqual(len(a), len(b), f"Length mismatch at {path}")
                for idx, (xa, xb) in enumerate(zip(a, b)):
                    check_recursive_overlaps(xa, xb, f"{path}[{idx}]")

        check_recursive_overlaps(data["cert_256"], data["cert_384"], "root")
        self.assertEqual(len(checked_pairs), 176)

        # Verify Theorem 1 pole-subtraction identity at both 256-bit and 384-bit
        for cert_key, bound_str in (("cert_256", "1e-64"), ("cert_384", "1e-98")):
            t1_rows = data[cert_key]["theorem_1_abel_legendre_pole_cancellation"]
            self.assertEqual(len(t1_rows), 8)
            for r in t1_rows:
                lhs = flint.arb(str(r["lhs_direct"]["str"]))
                rhs = flint.arb(str(r["rhs_boundary_free_integral"]["str"]))
                diff = flint.arb(str(r["diff"]["str"]))
                self.assertTrue(bool(lhs.overlaps(rhs)))
                self.assertTrue(bool(diff.contains(0)))
                self.assertTrue(bool(abs(diff) < flint.arb(bound_str)))

        # Verify Theorem 2 closed-form odd pole moment identity, repaired [3.5, inf) tail bounds, and h(-1.7) > 0
        for cert_key, bound_str in (("cert_256", "1e-28"), ("cert_384", "1e-40")):
            t2_sec = data[cert_key]["theorem_2_critical_zero_and_odd_pole_moment"]
            m_num = flint.arb(str(t2_sec["odd_pole_moment_xh_numerical"]["str"]))
            m_cf = flint.arb(str(t2_sec["odd_pole_moment_xh_closed_form"]["str"]))
            m_diff = flint.arb(str(t2_sec["odd_pole_moment_diff"]["str"]))
            tail_lb = flint.arb(str(t2_sec["odd_pole_moment_tail_35_lower_bound"]["str"]))
            tail_ub = flint.arb(str(t2_sec["odd_pole_moment_tail_35_upper_bound"]["str"]))
            h_neg_17 = flint.arb(str(t2_sec["h_at_minus_1_7"]["str"]))
            self.assertTrue(bool(m_num.overlaps(m_cf)))
            self.assertTrue(bool(m_diff.contains(0)))
            self.assertTrue(bool(abs(m_diff) < flint.arb(bound_str)))
            self.assertTrue(bool(tail_lb > flint.arb("8.53e-1492")))
            self.assertTrue(bool(tail_ub > tail_lb))
            self.assertTrue(bool(tail_ub < flint.arb("1.12e-1490")))
            self.assertTrue(bool(h_neg_17 > flint.arb("1.23565e-36")))
            self.assertTrue(bool(h_neg_17 < flint.arb("1.23566e-36")))

        # Verify h_and_dh_acb directly on negative inputs, complex quadrature boxes, and wide-box guards
        spec = importlib.util.spec_from_file_location("verify_cofinal_candidate_mechanisms", script_path)
        self.assertIsNotNone(spec)
        assert spec is not None and spec.loader is not None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        h_neg, dh_neg = mod.h_and_dh_acb(flint.acb(flint.arb("-1.7")))
        h_pos, dh_pos = mod.h_and_dh_acb(flint.acb(flint.arb("1.7")))
        self.assertTrue(bool(h_neg.real.overlaps(h_pos.real)))
        self.assertTrue(bool(h_neg.real > flint.arb(0)))
        self.assertTrue(bool((dh_neg.real + dh_pos.real).contains(0)))
        h_cplx, _ = mod.h_and_dh_acb(flint.acb(flint.arb("0.5"), flint.arb("0.1")))
        self.assertTrue(bool(h_cplx.real.is_finite()))
        # Wide complex box where Re(e^{2z}) <= 0.5 must return non-finite (nan) to trigger acb.integral bisection
        h_wide, _ = mod.h_and_dh_acb(flint.acb(flint.arb("0.5"), flint.arb("0.8")))
        self.assertFalse(bool(h_wide.real.is_finite()))

        # Verify exact NS83 q=2 transformed target Mellin functional relation 2*|T_2(rho_1)|^2 == 2/|rho_1|^4
        for cert_key in ("cert_256", "cert_384"):
            nb_sec = data[cert_key]["nb_gain_candidates_a_b_c"]
            abs_t2 = flint.arb(str(nb_sec["abs_T2_at_rho1"]["str"]))
            pair_wt = flint.arb(str(nb_sec["pair_weight_q2_at_rho1"]["str"]))
            self.assertTrue(bool((flint.arb(2) * (abs_t2 ** 2)).overlaps(pair_wt)))
            self.assertTrue(bool(abs_t2 > flint.arb("0.00499898883372")))
            self.assertTrue(bool(abs_t2 < flint.arb("0.00499898883373")))


if __name__ == "__main__":
    unittest.main()

