import unittest
from mazolkatools.analysis import (
    word_count,
    char_count,
    top_words
)
from mazolkatools.exceptions import InvalidTextError

class TestAnalysis(unittest.TestCase):

    def test_word_count_normal(self):
        self.assertEqual(word_count("Hello world"), 2)
        self.assertEqual(word_count("One two  three"), 3)
        self.assertEqual(word_count("Word"), 1)

    def test_word_count_empty(self):
        self.assertEqual(word_count(""), 0)
        self.assertEqual(word_count("   "), 0)

    def test_word_count_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            word_count(999)
        with self.assertRaises(InvalidTextError):
            word_count([])

    def test_char_count_normal(self):
        self.assertEqual(char_count("Hello"), 5)
        self.assertEqual(char_count("Hi there!", ignore_spaces=True), 7)  # "Hithere!"
        self.assertEqual(char_count("a b c", ignore_spaces=False), 5)  # с пробелами

    def test_char_count_empty(self):
        self.assertEqual(char_count(""), 0)
        self.assertEqual(char_count("   ", ignore_spaces=True), 0)

    def test_char_count_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            char_count(None)
        with self.assertRaises(InvalidTextError):
            char_count({})

    def test_top_words_normal(self):
        text = "apple banana apple cherry banana apple"
        result = top_words(text, n=2)
        self.assertEqual(result, [("apple", 3), ("banana", 2)])

    def test_top_words_n_greater_than_unique(self):
        text = "a a b"
        result = top_words(text, n=5)
        self.assertEqual(result, [("a", 2), ("b", 1)])  # возвращаем все

    def test_top_words_empty_text(self):
        self.assertEqual(top_words("", n=3), [])

    def test_top_words_invalid_n(self):
        with self.assertRaises(ValueError):
            top_words("text", n=0)
        with self.assertRaises(ValueError):
            top_words("text", n=-1)

    def test_top_words_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            top_words(123, n=2)
        with self.assertRaises(InvalidTextError):
            top_words([], n=1)

if __name__ == '__main__':
    unittest.main()