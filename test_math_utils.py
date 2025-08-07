# test_math_utils.py
import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 7), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-3, 5), 2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(3, 0), 3)

if __name__ == "__main__":
    unittest.main()
