import unittest
from my_awesome_lib.text_processing import is_palindrome

class TestTextProcessing(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Python"))