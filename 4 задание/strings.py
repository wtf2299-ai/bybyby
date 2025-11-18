import re
import math
from typing import Union

# ----------------------------
# Практическая работа №1
# ----------------------------

def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть неотрицательным целым числом")
    return math.factorial(n)

def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Параметры должны быть целыми числами")
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# ----------------------------
# Практическая работа №2
# ----------------------------

def classify_age(age_input: Union[str, int, float]) -> str:
    try:
        age = int(age_input)
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
    except (ValueError, TypeError):
        return "Некорректный ввод"
    if age <= 12:
        return "Ребёнок"
    elif age <= 17:
        return "Подросток"
    elif age <= 64:
        return "Взрослый"
    else:
        return "Пенсионер"

# ----------------------------
# Практическая работа №3
# ----------------------------

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
