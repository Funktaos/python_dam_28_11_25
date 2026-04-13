# Пример 1
with open("52_lesson_27/example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


# Пример 2
with open("52_lesson_27/example.txt", "r", encoding="utf-8") as file:
    content = file.read(10)  # читаем первые 10 символов
    print(content)

# Пример 3
with open("52_lesson_27/example.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Пример 4
with open("52_lesson_27/example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(type(lines))
    print(lines)

# Пример 5
with open("52_lesson_27/example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
