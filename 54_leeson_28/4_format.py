import json

# Пример с отступами
# data = {
#     "name": "Alice",
#     "age": 25,
#     "is_student": False,
#     "courses": {"math": "A", "physics": "B"},
# }

# json_string = json.dumps(data)  # Без отступа
# print(json_string)

# json_string = json.dumps(data, indent=4)  # С отступом
# print(json_string)


# Пример с не-ASCII символами
# data = {"город": "Берлин", "страна": "Германия"}

# json_string = json.dumps(data)  # По умолчанию (ensure_ascii=True)
# print(json_string)

# json_string = json.dumps(data, ensure_ascii=False)  # Отключаем ASCII-кодировку
# print(json_string)


# Пример с сортировкой ключей
data = {"name": "Alice", "age": 25, "is_student": False, "city": "London"}

json_string = json.dumps(data, indent=4)  # Без сортировки ключей
print(json_string)

json_string = json.dumps(data, indent=4, sort_keys=True)  # Сортировка ключей
print(json_string)
