# Пример 1 - Режим "w" для записи
# Создаёт файл, если его нет,
# и записывает строку, перезаписывая содержимое, если файл уже существует
with open("users.txt", "w", encoding="utf-8") as file:
    file.write("ID: 201 | Name: John | Age: 25 | Status: Active\n")


# Пример 2 - Режим "w" для записи
data = [
    "ID: 202 | Name: Alice | Age: 30 | Status: Inactive\n",
    "ID: 203 | Name: Bob | Age: 27 | Status: Active\n",
]

with open("users.txt", "w", encoding="utf-8") as file:
    file.writelines(data)


# Пример 3 - Режим "a" для добавления данных
# Создаёт файл, если его нет,
# и добавляет строку, если файл уже существует
with open("users.txt", "a", encoding="utf-8") as file:
    file.write("Дополнительная строка\n")


# Пример 4 - Режим "r+" для чтения и записи
# Чтение и запись в одном блоке
# Файл должен существовать, иначе возникнет ошибка
with open("users.txt", "r+", encoding="utf-8") as file:
    content = file.read()  # Читаем текущие данные
    file.write("\nДобавленный текст")  # Записываем новые данные


# Пример 5 - Режим "x" для создания нового файла
try:
    with open("new_file.txt", "x", encoding="utf-8") as file:
        file.write("Этот файл создан в режиме 'x'.\n")
except FileExistsError:
    print("Файл уже существует.")


# Пример 6 - Режим "w+" для чтения и записи с перезаписью
with (
    open("52_lesson_27/example.txt", "r", encoding="utf-8") as infile,
    open("output.txt", "w", encoding="utf-8") as outfile,
):
    for line in infile:
        outfile.write(line.upper())  # Записываем в верхнем регистре
