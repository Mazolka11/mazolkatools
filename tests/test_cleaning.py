import unittest
from mazolkatools.cleaning import (
    remove_whitespace,
    remove_punctuation,
    normalize_spaces
)
from mazolkatools.exceptions import InvalidTextError


class TestCleaning(unittest.TestCase):

    def test_remove_whitespace_normal(self):
        self.assertEqual(remove_whitespace("  Hello   world  "), "Hello world")
        self.assertEqual(remove_whitespace("Single"), "Single")

    def test_remove_whitespace_empty(self):
        self.assertEqual(remove_whitespace(""), "")
        self.assertEqual(remove_whitespace("   "), "")

    def test_remove_whitespace_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            remove_whitespace(123)
        with self.assertRaises(InvalidTextError):
            remove_whitespace(None)

    def test_remove_punctuation_normal(self):
        self.assertEqual(remove_punctuation("Hi!!!", keep="!"), "Hi!")
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")
        self.assertEqual(remove_punctuation("No punct"), "No punct")

    def test_remove_punctuation_empty(self):
        self.assertEqual(remove_punctuation(""), "")
        self.assertEqual(remove_punctuation("!!!", keep=""), "")

    def test_remove_punctuation_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            remove_punctuation(456)
        with self.assertRaises(InvalidTextError):
            remove_punctuation([])

    def test_normalize_spaces_normal(self):
        self.assertEqual(normalize_spaces("Hello\tworld\nhi"), "Hello world hi")
        self.assertEqual(normalize_spaces("A  B\tC\nD"), "A B C D")

    def test_normalize_spaces_empty(self):
        self.assertEqual(normalize_spaces(""), "")
        self.assertEqual(normalize_spaces("\t\n  "), " ")

    def test_normalize_spaces_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            normalize_spaces(789)
        with self.assertRaises(InvalidTextError):
            normalize_spaces({})

if __name__ == '__main__':
    unittest.main()