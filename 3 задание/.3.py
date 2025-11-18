import re
import unicodedata
import unittest
#   СТРОКОВЫЕ ФУНКЦИИ
def reverse(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def count_vowels(s: str) -> int:
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
    return sum(1 for c in s if c in vowels)

def normalize_whitespace(s: str) -> str:
    return re.sub(r'\s+', ' ', s).strip()

def to_slug(s: str) -> str:
    
    cyr = {
        'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
        'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m',
        'н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u',
        'ф':'f','х':'h','ц':'c','ч':'ch','ш':'sh','щ':'shch','ъ':'',
        'ы':'y','ь':'','э':'e','ю':'yu','я':'ya'
    }
    s = s.lower()
    s = ''.join(cyr.get(ch, ch) for ch in s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')

def camel_to_snake(s: str) -> str:
    s = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)
    return s.lower()



#   ТЕСТЫ НА UNITTEST


class TestStringFunctions(unittest.TestCase):

    # reverse 
    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")
        self.assertEqual(reverse("абв"), "вба")
        self.assertEqual(reverse("12345"), "54321")
        self.assertEqual(reverse("!@#"), "#@!")

    # is_palindrome
    def test_is_palindrome(self):
        self.assertFalse(is_palindrome("madonna"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertTrue(is_palindrome("1234321"))

    # count_vowels 
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("Айболит"), 3)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("че???"), 1)

    # normalize_whitespace
    def test_normalize_whitespace(self):
        self.assertEqual(normalize_whitespace("hello   world"), "hello world")
        self.assertEqual(normalize_whitespace("  trim  me  "), "trim me")
        self.assertEqual(normalize_whitespace("one\ttwo"), "one two")
        self.assertEqual(normalize_whitespace("\n\nhello   \n world"), "hello world")
        self.assertEqual(normalize_whitespace(""), "")
        self.assertEqual(normalize_whitespace("   "), "")

    # to_slug
    def test_to_slug(self):
        self.assertEqual(to_slug("Hello World"), "hello-world")
        self.assertEqual(to_slug("Привет мир"), "privet-mir")
        self.assertEqual(to_slug("___test___"), "test")
        self.assertEqual(to_slug("Hello!!!World"), "hello-world")
        self.assertEqual(to_slug(""), "")
        self.assertEqual(to_slug("A     B"), "a-b")

    # camel_to_snake
    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("camelCase"), "camel_case")
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")
        self.assertEqual(camel_to_snake("simple"), "simple")
        self.assertEqual(camel_to_snake("JSONData"), "json_data")
        self.assertEqual(camel_to_snake("A"), "a")
        self.assertEqual(camel_to_snake("someLongVariableNameTest"), "some_long_variable_name_test")
#   Запуск тестов

if __name__ == "__main__":
    unittest.main()
