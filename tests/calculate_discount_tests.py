import functions


def test_count_discount_1():
    assert functions.calculate_discount(100, 0.2) == 80


def test_count_discount_2():
    assert functions.calculate_discount(50, 0) == 50


def test_count_discount_3():
    assert functions.calculate_discount(200, 1) == 0


def test_count_discount_4():
    assert functions.calculate_discount(100, -0.1) is ValueError


def test_count_discount_5():
    assert functions.calculate_discount(100, 1.5) is ValueError
