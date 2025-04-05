import unittest
import ppf_calculator as ppf

class TestPPFCalculator(unittest.TestCase):
    def test_principal_zero(self):
        self.assertEqual(ppf.calculate_ppf_maturity(0, 5000, 10, 10, 10), 129687.12)

    def test_principal_100(self):
        self.assertEqual(ppf.calculate_ppf_maturity(10000, 5000, 10, 10, 10), 155624.55)

if __name__ == '__main__':
    unittest.main()
