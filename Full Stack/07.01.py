# Дан словарь с информацией о продуктах в магазине. Каждый продукт представлен вложенным словарем с ключами
# "название", "цена" и "количество". Посчитайте общую стоимость всех продуктов.

products = [
    {
        "name": "яблоки",
        "price": 10,
        "quantity": 5
    },
    {
        "name": "бананы",
        "price": 15,
        "quantity": 3
    },
    {
        "name": "апельсины",
        "price": 12,
        "quantity": 4
    }
]
def total_price(a):

    sum = 0
    for i in a:
        sum += i["price"] * i["quantity"]
    return sum
print(total_price(products))


# Дан словарь с информацией о сотрудниках компании. Каждый сотрудник представлен вложенным словарем с ключами
# "имя", "должность" и "зарплата". Найдите сотрудника с наибольшей зарплатой.

employees = [
    {
        "name": "Алексей",
        "position": "менеджер",
        "salary": 50000
    },
    {
        "name": "Елена",
        "position": "разработчик",
        "salary": 60000
    },
    {
        "name": "Дмитрий",
        "position": "дизайнер",
        "salary": 55000
    }
]
def max_salary(a):
    i1 = {}
    max = 0
    for i in a:
        if i["salary"] > max:
            i1.clear()
            i1[i["name"]] = i["salary"]
    return i1
print(max_salary(employees))
