# Контроль ввода
# Пользователь вводит строку с информацией о студенте: фамилия, имя, год рождения, курс – через пробел.
# Напишите функцию, которая проверяет корректность ввода:
# первые два элемента должны быть строками (из букв, без лишних символов),
# вторые два элемента – целые числа в подходящем диапазоне.
# В случае нарушения формата функция должна выбрасывать ошибку.
# В случае корректного ввода функция возвращает словарь с информацией о студенте.
# При вызове функции обработайте исключение.
#
# Пример ввода 1: Smith John 2000 3
# Пример вывода: Введенная информация корректна: {'last_name': 'Smith', 'first_name': 'John', 'birth_year': 2000, 'course': 3}
#
# Пример ввода 2: Smith Jo.hn 2000 3
# Пример вывода: Ошибка ввода: Имя должно содержать только буквы.

def check_student_info(info_str: str):
    parts = info_str.split()
    if len(parts) != 4:
        raise ValueError("Неверное количество элементов. Ожидается: фамилия, имя, год рождения, курс.")

    last_name, first_name, birth_year_str, course_str = parts

    if not last_name.isalpha():
        raise ValueError("Фамилия должна содержать только буквы.")
    if not first_name.isalpha():
        raise ValueError("Имя должно содержать только буквы.")

    try:
        birth_year = int(birth_year_str)
    except ValueError:
        raise ValueError("Год рождения должен быть целым числом.")
    if not (1950 <= birth_year <= 2010):
        raise ValueError(f"Число {birth_year} не похоже на год рождения студента.")

    try:
        course = int(course_str)
    except ValueError:
        raise ValueError("Курс должен быть целым числом.")
    if not (1 <= course <= 6):
        raise ValueError("Курс должен быть в диапазоне от 1 до 6.")

    return {
        "last_name": last_name,
        "first_name": first_name,
        "birth_year": birth_year,
        "course": course
    }


input_str = input("Введите информацию о студенте (фамилия имя год_рождения курс): ")

try:
    student_info = check_student_info(input_str)
    print("Введенная информация корректна:", student_info)
except ValueError as e:
    print("Ошибка ввода:", e)
