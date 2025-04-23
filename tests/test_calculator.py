import unittest
from calculator.calculator import addition, soustraction, multiplication, division

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(1, 2), 3)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(1.5, 2.5), 4.0)

    def test_soustraction(self):
        self.assertEqual(soustraction(3, 2), 1)
        self.assertEqual(soustraction(1, 1), 0)
        self.assertEqual(soustraction(0, 5), -5)
        self.assertEqual(soustraction(5.5, 2.5), 3.0)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-2, 3), -6)
        self.assertEqual(multiplication(0, 5), 0)
        self.assertEqual(multiplication(2.5, 2), 5.0)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(5, 2), 2.5)
        self.assertEqual(division(0, 5), 0)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()
