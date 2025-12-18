import functions


def test_count_volwels_1():
    assert functions.count_volwels("Python") == 2


def test_count_volwels_2():
    assert functions.count_volwels("AEIOUY") == 6


def test_count_volwels_3():
    assert functions.count_volwels("bcd") == 0


def test_count_volwels_4():
    assert functions.count_volwels("") == 0


def test_count_volwels_5():
    assert functions.count_volwels("Próba żółwia") == 5
