import string


def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = text.replace(" ", "")
    return text[::-1] == text


def fibonacci(n: int) -> int:
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def count_volwels(text: str) -> int:
    text = text.lower()
    count = 0
    for letter in text:
        if letter in "aeiouyóąę":
            count += 1
    return count


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        return ValueError
    else:
        return price - discount * price


def flatten_list(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list += flatten_list(item)
        else:
            flat_list.append(item)
    return flat_list


def word_frequencies(text: str) -> dict:
    text = text.lower()
    t_marks = str.maketrans('', '', string.punctuation)
    words = text.translate(t_marks).split()
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies


def is_prime(n: int) -> bool:
    t_div = [2, 3, 5, 7]
    if n < 2:
        return False
    for div in t_div:
        if n % div == 0 and n != div:
            return False
    return True
