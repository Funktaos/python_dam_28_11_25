import json

# Преобразование Python-объекта в JSON-строку
data = {"name": "Alice", "age": 25, "is_student": False}

json_string = json.dumps(data)  # Преобразование в JSON-строку
print(type(json_string))
print(json_string)


# Запись JSON в файл
data = {"name": "Alice", "age": 25, "is_student": False}

with open("data.json", "w") as file:
    json.dump(data, file)  # Запись JSON в файл
