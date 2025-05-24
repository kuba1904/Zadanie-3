import unittest
from my_awesome_lib.data_utils import convert_date_format

class TestDataUtils(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("24-05-2025"), "2025/05/24")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("2025-05-24")