import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    def setUp(self):
        self.calc_1 = CompoundInterest(100, 20, 0.1)

    # Tests

    def test_part_one(self):
        get_part_one = self.calc_1.part_one_of_equation(self.calc_1.interest_rate)
        self.assertEqual(1.0083333333, get_part_one)
    
    def test_part_two(self):
        get_part_two = self.calc_1.part_two_of_equation(self.calc_1.years)
        self.assertEqual(240, get_part_two)
    
    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_compound_interest_calc(self):
        get_compound_interest = self.calc_1.compound_interest_calc(self.calc_1.principal_amount, self.calc_1.years, self.calc_1.interest_rate)
        self.assertEqual(732.81, get_compound_interest)

    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

