import functions


def test_is_prime_1():
    assert functions.is_prime(2) == True


def test_is_prime_2():
    assert functions.is_prime(3) == True


def test_is_prime_3():
    assert functions.is_prime(4) == False


def test_is_prime_4():
    assert functions.is_prime(0) == False


def test_is_prime_5():
    assert functions.is_prime(1) == False


def test_is_prime_6():
    assert functions.is_prime(5) == True


def test_is_prime_7():
    assert functions.is_prime(97) == True
