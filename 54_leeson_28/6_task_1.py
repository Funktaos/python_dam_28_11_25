import json
from datetime import datetime


def filter_low_scores(threshold, start_date, end_date):
    date_format = "%d-%m-%Y"

    # Преобразуем строковые границы диапазона в объекты datetime
    start_dt = ?
    end_dt = ?

    # Читаем исходные данные из файла
    try:
        ...
    except FileNotFoundError:
        print("Ошибка: Файл grades.json не найден.")
        return []

    filtered_records = []

    # Фильтруем записи
    for record in data:
        ...

    # Сохраняем результат в новый JSON-файл

    return filtered_records


# Пример использования функции:
result = filter_low_scores(70, "01-01-2025", "31-05-2025")
print(f"Найдено записей: {len(result)}")
print(json.dumps(result, ensure_ascii=False, indent=4))
