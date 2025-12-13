# 2a
def print_names(names):
    for name in names:
        print(name)


# 2b
def print_number_2_for(numbers):
    numbers_multi = []
    for number in numbers:
        numbers_multi.append(number * 2)
    return numbers_multi


def print_number_2_list(numbers):
    numbers_multi = [number * 2 for number in numbers]
    return numbers_multi


# 2c
def print_elv_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


# 2d
def print_second_numbers(numbers):
    for i in range(1, len(numbers), 2):
        print(numbers[i])

names = ["Kot", "Płaszczka", "Ika", "Krzyś", "Miau"]
print_names(names)

numbers = [12, 11, 456, 23, 809, 343, 98, 23, 1, 234]
numbers_multi = print_number_2_for(numbers)
print(numbers_multi)

numbers_multi = print_number_2_list(numbers)
print(numbers_multi)

print_elv_numbers(numbers)
print("kitku")
print_second_numbers(numbers)