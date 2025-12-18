import functions


def test_fibonacci_1():
    assert functions.fibonacci(0) == 0


def test_fibonacci_2():
    assert functions.fibonacci(1) == 1


def test_fibonacci_3():
    assert functions.fibonacci(5) == 5


def test_fibonacci_4():
    assert functions.fibonacci(10) == 55


def test_fibonacci_5():
    assert functions.fibonacci(-1) is None
