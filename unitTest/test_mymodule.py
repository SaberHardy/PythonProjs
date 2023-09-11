import unittest
# from .mymodule import *
from mymodule import add, subtract


class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        result = add(5, -2)
        self.assertEqual(result, 3)


class TestSubtractFunction(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        result = subtract(5, 2)
        self.assertEqual(result, 3)

    def test_subtract_negative_numbers(self):
        result = subtract(-5, -2)
        self.assertEqual(result, -3)


if __name__ == '__main__':
    unittest.main()
