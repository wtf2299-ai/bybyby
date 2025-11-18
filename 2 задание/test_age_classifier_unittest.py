import unittest
from age_classifier import classify_age

class TestAgeClassifier(unittest.TestCase):
    def test_valid_ages(self):
        cases = {"0": "ребёнок", "5": "ребёнок", "12": "ребёнок",
                 "13": "подросток", "17": "подросток",
                 "18": "взрослый", "25": "взрослый", "64": "взрослый",
                 "65": "пенсионер", "100": "пенсионер"}
        for inp, expected in cases.items():
            self.assertEqual(classify_age(inp), expected)

    def test_negative_numbers(self):
        for inp in ["-1", "-50"]:
            with self.assertRaises(ValueError):
                classify_age(inp)

    def test_invalid_inputs(self):
        for inp in ["", "   ", "twenty", "25.5", "999999999999999999999"]:
            with self.assertRaises(ValueError):
                classify_age(inp)

if __name__ == "__main__":
    unittest.main()
