import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from Profitability.Core.profitability_simple import ProfitabilitySimple

class TestProfitabilitySimple(unittest.TestCase):

    def setUp(self):
        self.profitabilitySimple = ProfitabilitySimple()

    def test_do_not_allow_zero_values(self):
        self.assertEqual(None, self.profitabilitySimple.Calculate_Profitability_Simple(0, 0))

    def test_do_not_allow_string_values(self):
        self.assertEqual(None, self.profitabilitySimple.Calculate_Profitability_Simple('13', '20'))

    def test_do_not_allow_integer_values(self):
        self.assertEqual(None, self.profitabilitySimple.Calculate_Profitability_Simple(13, 20))

    def test_calculate_simple_positive_values(self):
        self.assertAlmostEqual(17.6471, self.profitabilitySimple.Calculate_Profitability_Simple(10000.0, 8500.0), 4)