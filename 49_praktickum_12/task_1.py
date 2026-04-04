# Четные цифры числа
# Напишите функцию, которая рекурсивно вычисляет количество четных цифр числа.
# Сделайте второй вариант этой функции – через хвостовую рекурсию.

def count_even_digits(n):
    n = abs(n)
    if n < 10:
        return 1 if n % 2 == 0 else 0
    else:
        last_digit = n % 10
        return (1 if last_digit % 2 == 0 else 0) + count_even_digits(n // 10)


def count_even_digits_tail(n, acc=0):
    n = abs(n)
    if n < 10:
        return acc + 1 if n % 2 == 0 else acc
    else:
        last_digit = n % 10
        return count_even_digits_tail(n // 10, acc + (1 if last_digit % 2 == 0 else 0))


# Пример использования
print(count_even_digits(1234567))        # 3 (2, 4, 6)
print(count_even_digits_tail(1234567))   # 3
