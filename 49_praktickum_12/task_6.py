# Сумма продаж
# Есть дерево подразделений внутри компании (каждое подразделение может содержать «дочерние» отделы).
# Напишите рекурсивную функцию, которая подсчитывает суммарные продажи для всех отделов.
# Функция должна проверять:
#   - Аргумент должен быть словарем.
#   - Дочерние отделы (если есть) должны быть списком словарей.
# Если данные не валидны необходимо выбрасывать исключение.
# При вызове функции обработайте возможное исключение.
#
# Пример вывода: Общая сумма продаж: 1140

def summarize_sales(department, sales_name):
    if not isinstance(department, dict):
        raise TypeError("Ожидается словарь с информацией о департаменте.")
    sub_departments = department.get("sub_departments", [])
    if sub_departments and not isinstance(sub_departments, list):
        raise TypeError("Дочерние отделы должны быть списком словарей.")
    total = department[sales_name]
    for sub_dept in sub_departments:
        total += summarize_sales(sub_dept, sales_name)
    return total


company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}

try:
    print(f"Общая сумма продаж: {summarize_sales(company_structure, 'sales')}")
except TypeError as e:
    print("Ошибка:", e)
