import json

# Преобразование JSON-строки в Python-объект
json_object = '{"name": "Alice", "age": 25, "is_student": false}'
json_objects = '[{"name": "Alice", "age": 25, "is_student": false}, {"name": "Bob", "age": 20, "is_student": true}]'

data_dict = json.loads(json_object)  # Преобразование JSON-строки в Python-объект
print(type(data_dict))
print(data_dict)

data_list = json.loads(json_objects)  # Преобразование JSON-строки в Python-объект
print(type(data_list))
print(data_list)


# Загрузка JSON из файла
with open("data.json", "r") as file:
    data = json.load(file)  # Загрузка JSON из файла

print(type(data))
print(data)
