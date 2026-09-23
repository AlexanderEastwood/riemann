"""Regression tests for diagnostic reliability, not mathematical certificates."""
from __future__ import annotations

import unittest
from typing import Any

import mpmath as mp

from controls.davenport_heilbronn import F_xi, phi, phi_raw, screen


class ControlRegressionTests(unittest.TestCase):
    def test_negative_tail_preserves_small_positive_value(self) -> None:
        values: list[Any] = []
        for dps in (25, 40):
            with mp.workdps(dps):
                for t in (3, 4):
                    value = phi(-t)
                    self.assertGreater(value, 0)
                    self.assertEqual(value, phi_raw(t))
                values.append(phi(-3))
        with mp.workdps(40):
            self.assertLess(abs(values[0] / values[1] - 1), mp.mpf("1e-22"))

    def test_raw_reciprocity_is_independently_checked(self) -> None:
        with mp.workdps(30):
            for t in (mp.mpf(".3"), mp.mpf("1.1")):
                self.assertLess(abs(phi_raw(t) - phi_raw(-t)), mp.mpf("1e-27"))

    def test_entire_xi_removable_points(self) -> None:
        with mp.workdps(35):
            for z in (mp.mpf(".5"), mp.mpf("-.5")):
                self.assertEqual(F_xi(z), mp.mpf(1) / 4)
            # Independent positive-real closed values at s=-2 and s=-4.
            self.assertLess(abs(F_xi(mp.mpf("-2.5")) -
                                3 * mp.zeta(3) / (4 * mp.pi)), mp.mpf("1e-32"))
            self.assertLess(abs(F_xi(mp.mpf("-4.5")) -
                                15 * mp.zeta(5) / (4 * mp.pi**2)), mp.mpf("1e-32"))
            for endpoint in (mp.mpf(".5"), mp.mpf("-.5")):
                self.assertLess(abs(F_xi(endpoint + mp.mpf("1e-15")) -
                                    mp.mpf(1) / 4), mp.mpf("1e-15"))

    def test_screen_never_promotes_sample_to_proof(self) -> None:
        for result, outcome in ((True, "sampled-pass"), (False, "sampled-failure"),
                                (None, "inconclusive")):
            out = screen(lambda _F, _phi: result, "unit sample",
                         sample_domain="one point", applicability="predicate only")
            self.assertEqual(out["outcome"], outcome)
            self.assertFalse(out["proved_control_obstruction"])
            self.assertNotIn("holds_on_known_false_analogue", out)

    def test_inapplicable_screen_does_not_evaluate(self) -> None:
        def forbidden(_F: Any, _phi: Any) -> bool:
            raise AssertionError("inapplicable candidate must not run")

        out = screen(forbidden, "mismatched input", sample_domain="none",
                     applicability="different gamma factor", applicable=False)
        self.assertEqual(out["outcome"], "not-applicable")


if __name__ == "__main__":
    unittest.main()
