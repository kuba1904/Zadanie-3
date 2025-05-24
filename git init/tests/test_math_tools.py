import unittest
from my_awesome_lib.math_tools import calculate_rectangle_area

class TestMathTools(unittest.TestCase):
    def test_area(self):
        self.assertEqual(calculate_rectangle_area(3, 4), 12)

    def test_negative(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-1, 2)