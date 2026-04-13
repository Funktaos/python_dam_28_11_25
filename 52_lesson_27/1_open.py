# Пример 1
file = open("52_lesson_27/example.txt", "r", encoding="utf-8")
print(file)  # файловый объект
print(type(file))
text = file.read()  # уже содержимое файла
print(text)
file.close()

# Пример 2
with open("52_lesson_27/example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
