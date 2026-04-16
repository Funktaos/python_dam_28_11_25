from datetime import datetime, timedelta

# Пример 1
# now = datetime.now()  # Получаем текущую дату и время
# print(type(now))  # Объект datetime
# print(now)


# print("Год:", now.year)
# print("Месяц:", now.month)
# print("День:", now.day)
# print("Часы:", now.hour)
# print("Минуты:", now.minute)
# print("Секунды:", now.second)
# print("Микросекунды:", now.microsecond)


# Пример 2 - форматирование даты и времени
# now = datetime.now()
# # Преобразование в строку
# print(str(now))
# # Преобразование в строку указанного формата
# formatted_date = now.strftime("%d.%m.%Y %H:%M:%S.%f")
# print(type(formatted_date))
# print(formatted_date)


# Пример 3 - различные форматы вывода даты и времени
# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))  # 2025-02-28 (ISO формат)
# print(now.strftime("%d/%m/%Y"))  # 28/02/2025 (европейский формат)
# print(now.strftime("%I:%M %p"))  # 02:30 PM (12-часовой формат)
# print(now.strftime("%A, %B %d, %Y"))  # Friday, February 28, 2025


# Пример 4 - создание объекта datetime из строки
# date_string = "28|02|2025 14-30-15"  # Дата в виде строки
# date_obj = datetime.strptime(
#     date_string, "%d|%m|%Y %H-%M-%S"
# )  # Указываем форматы и те же разделители

# print(type(date_obj))
# print(date_obj)


# Пример 5 - сравнение дат
# now = datetime.now()
# deadline = datetime.strptime("01.12.2025", "%d.%m.%Y")

# if now > deadline:
#     print("Срок истёк!")
# else:
#     print("До дедлайна ещё есть время.")


# Пример 6 - разница между датами
# date1 = datetime(2025, 2, 28)
# date2 = datetime(2025, 3, 5)

# difference = date2 - date1  # Разница между датами
# print(type(difference))
# print(difference)
# print(difference.days)


# Пример 7 - разница между датами c учетом времени
# dt1 = datetime(2025, 2, 28, 14, 30)
# dt2 = datetime(2025, 3, 2, 10, 0)

# difference = dt2 - dt1
# print(difference)
# print(difference.total_seconds())


# Пример 8 - использование timedelta для работы с датами

# Дата начала задачи
start_date = datetime(2025, 2, 28)

# Дедлайн через 2 недели
deadline = start_date + timedelta(weeks=2)
print("Дедлайн:", deadline.strftime("%d.%m.%Y"))

# Проверка, прошёл ли дедлайн
today = datetime(2025, 3, 15)  # Текущая дата

if deadline > today:
    print("Дедлайн пропущен!")
else:
    print("Ещё есть время для выполнения задачи.")
