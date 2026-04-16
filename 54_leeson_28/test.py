import json

# Преобразование Python-объекта в JSON-строку
data = {"name": "Alice", "age": set((25, 2, 3)), "is_student": False}

json_string = json.dumps(data)  # Преобразование в JSON-строку
print(type(json_string))
print(json_string)
