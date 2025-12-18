import functions


def test_word_frequencies_1():
    assert functions.word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}


def test_word_frequencies_2():
    assert functions.word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_3():
    assert functions.word_frequencies("") == {}


def test_word_frequencies_4():
    assert functions.word_frequencies("Python Python python") == {"python": 3}


def test_word_frequencies_5():
    assert functions.word_frequencies("Ala ma kota, a kot ma Ale.") == {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}
