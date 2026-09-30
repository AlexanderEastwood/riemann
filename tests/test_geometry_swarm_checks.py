"""Regression cases for actual failure modes in the local geometric models."""
from fractions import Fraction
import unittest

from tools.geometry_swarm.checks import (
    HyperbolicCase, check_hyperbolic, exterior_supertrace,
    passive_prime_factor, primitive_support, quotient_deck_map,
)


class GeometryCheckTests(unittest.TestCase):
    def test_exterior_degrees_cancel_trace_denominator(self) -> None:
        self.assertEqual(exterior_supertrace([Fraction(4), Fraction(1, 4)]), Fraction(-9, 4))

    def test_extra_dimension_is_not_automatic(self) -> None:
        base = check_hyperbolic(HyperbolicCase(2, 1, (Fraction(1),), 0))
        lift = check_hyperbolic(HyperbolicCase(2, 1, (Fraction(1), Fraction(1)), 0))
        repaired = check_hyperbolic(HyperbolicCase(2, 1, (Fraction(1, 2), Fraction(1, 2)), 1))
        self.assertEqual(base['normalized_weight_without_log_label'], '-1/2')
        self.assertFalse(lift['candidate_condition_holds'])
        self.assertTrue(repaired['candidate_condition_holds'])

    def test_fake_prime_passes_local_algebra_but_fails_support(self) -> None:
        local = check_hyperbolic(HyperbolicCase(6, 1, (Fraction(1),), 0))
        self.assertTrue(local['candidate_condition_holds'])
        self.assertFalse(local['label_is_prime'])
        self.assertFalse(primitive_support([2, 3, 6])['candidate_condition_holds'])
        self.assertFalse(primitive_support([2, 3, 4])['candidate_condition_holds'])
        self.assertFalse(primitive_support([2, 2, 3])['candidate_condition_holds'])
        self.assertTrue(primitive_support([2, 3, 5])['candidate_condition_holds'])

    def test_actual_passive_port_counterexample(self) -> None:
        case = passive_prime_factor(2, 1)
        self.assertEqual(case['ratio'], '7/6')
        self.assertFalse(case['candidate_condition_holds'])

    def test_deck_map_retains_no_power_label(self) -> None:
        for k in (1, 2, 13):
            self.assertEqual(quotient_deck_map(3, k)['reduced_shift_in_period_units'], '0')

    def test_unbounded_or_invalid_work_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            check_hyperbolic(HyperbolicCase(2, 33, (Fraction(1),), 0))
        with self.assertRaises(ValueError):
            check_hyperbolic(HyperbolicCase(2, 1, (Fraction(0),), 0))


if __name__ == '__main__':
    unittest.main()
