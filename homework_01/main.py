"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num : int) -> bool:
    if num == 1 :
        return False
    if num % 2 == 0:
        return num == 2
    dig = 3
    while dig ** 2 <= num and num % dig != 0:
        dig += 2
    return dig ** 2 > num

def is_even(num : int) -> bool:
    return num%2 == 0

def is_odd(num : int) -> bool:
    return not is_even(num)

def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD :
        return list(filter(is_odd, numbers))
        #return [i for i in numbers if i % 2 == 1]
    elif filter_type == EVEN :
        return list(filter(is_even, numbers))
        #return [i for i in numbers if i % 2 == 0]
    elif filter_type == PRIME :
        return list(filter(is_prime, numbers))
        #return [i for i in numbers if is_prime(i) == True]
    else :
        pass
