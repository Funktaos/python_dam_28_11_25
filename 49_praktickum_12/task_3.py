# Сумма чисел списка
# Напишите рекурсивную функцию, которая вычисляет сумму всех чисел в списке.
# Функция должна проверять:
#   - Аргумент должен быть списком.
#   - Все элементы списка должны быть числами.
# Если данные не валидны необходимо выбрасывать исключение.
# При вызове функции обработайте возможное исключение.
#
# Данные: numbers = [1, 2, 3, 4, 5]
# Пример вывода: 15

def recursive_sum(lst):
    if not isinstance(lst, list):
        raise TypeError("Ожидается список чисел.")
    if not lst:
        return 0
    if not isinstance(lst[0], (int, float)):
        raise ValueError("Список должен содержать только числа.")
    return lst[0] + recursive_sum(lst[1:])


try:
    numbers = [1, 2, 3, 4, 5]
    print(recursive_sum(numbers))
except (TypeError, ValueError) as e:
    print("Ошибка:", e)
