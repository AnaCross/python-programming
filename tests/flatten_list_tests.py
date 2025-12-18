import functions


def test_flatten_list_1():
    assert functions.flatten_list([1, 2, 3]) == [1, 2, 3]


def test_flatten_list_2():
    assert functions.flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_flatten_list_3():
    assert functions.flatten_list([[[1]]]) == [1]


def test_flatten_list_4():
    assert functions.flatten_list([]) == []


def test_flatten_list_5():
    assert functions.flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
