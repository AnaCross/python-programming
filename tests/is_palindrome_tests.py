import functions


def test_is_palindrome_1():
    assert functions.is_palindrome("kajak") == True


def test_is_palindrome_2():
    assert functions.is_palindrome("Kobyla ma maly bok") == True


def test_is_palindrome_3():
    assert functions.is_palindrome("") == True


def test_is_palindrome_4():
    assert functions.is_palindrome("A") == True


def test_is_palindrome_5():
    assert functions.is_palindrome("python") == False
