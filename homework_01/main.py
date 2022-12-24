"""
Домашнее задание №1
Функции и структуры данных
"""
from math import ceil


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, method):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    # >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, ceil((number+1)/2)):
            if number % i == 0:
                return False
        return True

    if method == ODD:
        return [i for i in numbers if i % 2 != 0]
    elif method == EVEN:
        return [i for i in numbers if i % 2 == 0]
    elif method == PRIME:
        return [i for i in numbers if is_prime(i)]
