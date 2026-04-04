# Реверс строки
# Напишите рекурсивную функцию, которая переворачивает строку.
# Если передан не строковый тип, выбросить исключение.
# При вызове функции обработайте возможное исключение.
#
# Данные: text = "recursion"
# Пример вывода: noisrucer

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Ожидается строка.")
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


try:
    text = "recursion"
    print(reverse_string(text))
except TypeError as e:
    print("Ошибка:", e)
