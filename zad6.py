def check_list_int(numbers: list) -> bool:
    for number in numbers:
        if isinstance(number, int):
            continue
        else:
            return False
    return True


def magic_on_lists(number1: list, number2: list) -> list:
    check_list_int(number1)
    check_list_int(number2)
    number3 = number1 + number2
    number3.sort()
    for number in number3:
        if number3.count(number) > 1:
            number3.remove(number)

    number3 = [number ** 3 for number in number3]
    return number3


print(magic_on_lists([1, 2, 3], [2, 3]))
