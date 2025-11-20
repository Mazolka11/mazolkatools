import unittest
from mazolkatools.formating import (
    to_snake_case,
    to_kebab_case,
    capitalize_sentences
)
from mazolkatools.exceptions import InvalidTextError

class TestFormatting(unittest.TestCase):

    def test_to_snake_case_normal(self):
        self.assertEqual(to_snake_case("Hello World"), "hello_world")
        self.assertEqual(to_snake_case("Python is great!"), "python_is_great")
        self.assertEqual(to_snake_case("multiple   spaces"), "multiple_spaces")

    def test_to_snake_case_empty(self):
        self.assertEqual(to_snake_case(""), "")
        self.assertEqual(to_snake_case("   "), "")

    def test_to_snake_case_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            to_snake_case(123)
        with self.assertRaises(InvalidTextError):
            to_snake_case([])

    def test_to_kebab_case_normal(self):
        self.assertEqual(to_kebab_case("Hello World"), "hello-world")
        self.assertEqual(to_kebab_case("Fast & Furious"), "fast_furious")  # & удаляется
        self.assertEqual(to_kebab_case("a-b c_d"), "a-b-c-d")

    def test_to_kebab_case_empty(self):
        self.assertEqual(to_kebab_case(""), "")

    def test_to_kebab_case_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            to_kebab_case(None)

    def test_capitalize_sentences_normal(self):
        self.assertEqual(
            capitalize_sentences("hello world. how are you?"),
            "Hello world. How are you?"
        )
        self.assertEqual(
            capitalize_sentences("one! two? three!"),
            "One! Two? Three!"
        )

    def test_capitalize_sentences_empty(self):
        self.assertEqual(capitalize_sentences(""), "")
        self.assertEqual(capitalize_sentences("..."), "...")

    def test_capitalize_sentences_invalid_type(self):
        with self.assertRaises(InvalidTextError):
            capitalize_sentences(42)
        with self.assertRaises(InvalidTextError):
            capitalize_sentences({})

if __name__ == '__main__':
    unittest.main()