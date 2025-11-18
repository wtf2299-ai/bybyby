import unittest
from strings import *

class TestAllFunctions(unittest.TestCase):

    # ---------- Практическая работа №1 ----------
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(20), 2432902008176640000)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(3.5)
        with self.assertRaises(ValueError):
            factorial("abc")

    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(-12, 18), 6)
        self.assertEqual(gcd(0, 5), 5)
        with self.assertRaises(ValueError):
            gcd(3.5, 2)
        with self.assertRaises(ValueError):
            gcd("a", 2)

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(-3, 7), 21)
        self.assertEqual(lcm(21, 6), 42)

    # ---------- Практическая работа №2 ----------
    def test_classify_age(self):
        self.assertEqual(classify_age(5), "Ребёнок")
        self.assertEqual(classify_age(12), "Ребёнок")
        self.assertEqual(classify_age(15), "Подросток")
        self.assertEqual(classify_age(25), "Взрослый")
        self.assertEqual(classify_age(65), "Пенсионер")
        self.assertEqual(classify_age(-5), "Некорректный ввод")
        self.assertEqual(classify_age("twenty"), "Некорректный ввод")
        self.assertEqual(classify_age(""), "Некорректный ввод")
        self.assertEqual(classify_age(65.0), "Пенсионер")

    # ---------- Практическая работа №3 ----------
    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")
        self.assertEqual(reverse("абв"), "вба")
        self.assertEqual(reverse("12345"), "54321")
        self.assertEqual(reverse("!@#"), "#@!")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertFalse(is_palindrome("madonna"))
        self.assertTrue(is_palindrome("1234321"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("A"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("Айболит"), 3)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("че???"), 1)

    def test_normalize_whitespace(self):
        self.assertEqual(normalize_whitespace("hello   world"), "hello world")
        self.assertEqual(normalize_whitespace("  trim  me  "), "trim me")
        self.assertEqual(normalize_whitespace("one\ttwo"), "one two")
        self.assertEqual(normalize_whitespace("\n\nhello   \n world"), "hello world")
        self.assertEqual(normalize_whitespace(""), "")
        self.assertEqual(normalize_whitespace("   "), "")

    def test_to_slug(self):
        self.assertEqual(to_slug("Hello World"), "hello-world")
        self.assertEqual(to_slug("Привет мир"), "privet-mir")
        self.assertEqual(to_slug("___test___"), "test")
        self.assertEqual(to_slug("Hello!!!World"), "hello-world")
        self.assertEqual(to_slug(""), "")
        self.assertEqual(to_slug("A     B"), "a-b")

    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("camelCase"), "camel_case")
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")
        self.assertEqual(camel_to_snake("simple"), "simple")
        self.assertEqual(camel_to_snake("JSONData"), "json_data")
        self.assertEqual(camel_to_snake("A"), "a")
        self.assertEqual(camel_to_snake("someLongVariableNameTest"), "some_long_variable_name_test")

if __name__ == "__main__":
    unittest.main(verbosity=2)
