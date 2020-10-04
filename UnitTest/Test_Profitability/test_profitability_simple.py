import unittest

from Profitability.Core.exceptions.my_custom_error import MyCustomError
from Profitability.Core.services.profitability_simple import ProfitabilitySimple


class TestProfitabilitySimple(unittest.TestCase):

    def setUp(self):
        self.subject = ProfitabilitySimple

    def test_do_not_allow_zero_values(self):
        self.assertEqual(None, self.subject.calculate_profitability_simple(0, 0))

    def test_do_not_allow_string_values(self):
        self.assertEqual(None, self.subject.calculate_profitability_simple('13', '20'))

    def test_do_not_allow_integer_values(self):
        self.assertEqual(None, self.subject.calculate_profitability_simple(13, 20))

    def test_calculate_simple_positive_profitability(self):
        self.assertAlmostEqual(17.6471, self.subject.calculate_profitability_simple(8500.0, 10000.0), 4)

    def test_calculate_simple_negative_profitability(self):
        self.assertAlmostEqual(-15, self.subject.calculate_profitability_simple(10000.0, 8500.0), 4)

    def test_calculate_simple_negative_profitability(self):
        self.assertAlmostEqual(-15, self.subject.calculate_profitability_simple(10000.0, 1000.0), 4)

    def test_calculate_simple_negative_investment_not_support(self):
        self.assertRaises(MyCustomError, self.subject.calculate_profitability_simple(-10000.0, 8500.0))
