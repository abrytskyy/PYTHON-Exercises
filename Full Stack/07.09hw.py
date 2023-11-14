###Ярослав

#Создайте множество, содержащее элементы "apple", "banana" и "cherry".
#Добавьте элемент "orange" в множество.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


#Создайте вложенный словарь, представляющий собой информацию о студенте.
#Внешний словарь должен содержать ключи "name", "age" и "grades". Внутренний словарь (grades) должен содержать предметы в качестве
# ключей и оценки в качестве значений.
# ---Создайте список вложенных словарей, представляющих собой информацию о студентах.
# Каждый словарь должен содержать ключи "name", "age" и "grades" (см. предыдущее задание).
# ---Создайте функцию, которая принимает этот  список и возвращает среднюю оценку каждого студента.

students_list = [
    {
        "name": "Alice",
        "age": 20,
        "grades": {
            "math": 85,
            "history": 90,
            "english": 78
        }
    },
    {
        "name": "Bob",
        "age": 22,
        "grades": {
            "math": 75,
            "history": 82,
            "english": 95
        }
    },
    # Добавьте остальных студентов аналогично
]
def calculate_average_grades(students_list):
    return [(student["name"],round(sum(student["grades"].values()) / len(student["grades"]),2)) for student in students_list]
print(calculate_average_grades(students_list))






#Проверьте, является ли объединение всех множеств из списка подмножеством множества {1, 2, 3, 4, 5, 6}
sets_list = [{2, 4, 6}, {1, 3, 5}, {9, 6}]

full_set = {1, 2, 3, 4, 5, 6}
print((sets_list[0].union(*sets_list[1:])).issubset(full_set))

###Артём
#Создайте функцию, которая принимает вложенный словарь (представляющий собой информацию о студентах и их оценках)
# и возвращает новый словарь, содержащий список студентов, у которых средняя оценка выше заданного порога.
grades_dict = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 94],
    "Charlie": [76, 82, 95]
}

threshold = 85
print({k:v for k,v in grades_dict.items() if sum(v)/len(v) >= threshold})

#Создайте функцию, которая принимает список словарей (представляющих собой информацию о товарах) и
# возвращает новый список, содержащий только товары с количеством больше или равным 10.
products_list = [
    {"name": "apple", "quantity": 5},
    {"name": "banana", "quantity": 15},
    {"name": "cherry", "quantity": 8},
    {"name": "orange", "quantity": 12}
]
print([(product) for product in products_list if product["quantity"] >= 10])

#Найдите пересечение первых двух множеств из списка.
sets = [
    {"apple", "banana", "cherry"},
    {"banana", "orange", "grape", "apple"},
    {"cherry", "grape", "kiwi", "banana"}
]

print(sets[0].intersection(sets[1]))


#Найдите объединение всех множеств из списка.
sets = [
    {"apple", "banana", "cherry"},
    {"banana", "orange", "grape"},
    {"cherry", "grape", "kiwi", "banana"}
]
print(sets[0].union(*sets[1:]))

#Найдите пересечение всех множеств из списка.
sets = [
    {"apple", "banana", "cherry"},
    {"banana", "orange", "grape"},
    {"cherry", "grape", "kiwi", "banana"}
]

print(sets[0].intersection(sets[1], sets[2]))
print(sets[0].intersection(*sets[1:]))


sets = [
    {"apple", "banana", "cherry"},
    {"banana", "orange", "grape"},
    {"cherry", "grape", "kiwi"}
]
set_result = sets[0].intersection(*sets[1:])
#set_result = sets[0].intersection(sets[1], sets[2])
print(set_result)
print(sets[0].intersection(*sets[1:]))

#Объедините все множества из списка в одно множество.
sets = [
    {"apple", "banana", "cherry"},
    {"banana", "orange", "grape"},
    {"cherry", "grape", "kiwi"}
]
sets1 = sets[-1]
for s in range(len(sets)-1):
    sets1 = sets1.union(sets[s])
print(sets1)



list1 = []
for s in sets:
    list1 += list(s)
print(set(list1))

###Катерина
#Создайте два множества с элементами "apple", "banana", "cherry" и "orange". Вычислите и выведите их пересечение.
set1 = {"apple", "banana", "cherry", "orange"}
set2 = {"banana", "cherry", "orange"}
print(set1.intersection(set2))
print(set1 & set2)

#Удалите элемент "banana" из множества.
fruits_set = {"apple", "banana", "orange", "grape"}
fruits_set.remove("banana")
print(fruits_set)
#fruits_set.remove("banana")

fruits_set = {"apple", "banana", "orange", "grape"}
fruits_set.discard("banana")
print(fruits_set)
fruits_set.discard("banana")
print(fruits_set)





#Создайте функцию, которая принимает список словарей (представляющих собой информацию о фруктах) и возвращает новый список,
# содержащий только фрукты определенного цвета (например, "red").
fruits = [
    {"name": "apple", "color": "red", "taste": "sweet"},
    {"name": "banana", "color": "yellow", "taste": "sweet"},
    {"name": "grape", "color": "purple", "taste": "sweet"},
    {"name": "orange", "color": "orange", "taste": "citrus"},
    {"name": "strawberry", "color": "red", "taste": "sweet"}
]

color = "red"


print([fruit for fruit in fruits if fruit["color"] == "red" ])


#Создайте функцию, которая принимает вложенный словарь (представляющий собой информацию о компаниях и их сотрудниках)
# и возвращает новый словарь, содержащий только сотрудников определенной должности (например, "developer").
company_info = {
    "Company A": [
        {"name": "Alice", "position": "developer"},
        {"name": "Bob", "position": "manager"}
    ],
    "Company B": [
        {"name": "Charlie", "position": "developer"},
        {"name": "David", "position": "designer"}
    ]
}


print({k:[employee for employee in v if employee["position"] == "developer"]for k,v in company_info.items()})

filtered_companies = {k: [employee for employee in v if employee["position"] == "developer"] for k, v in company_info.items()}
for company, employees in filtered_companies.items():
    print(f"{company}: {employees}")






###@Denwork21
#Создайте вложенный словарь, представляющий собой информацию о студентах. Внешние ключи - идентификаторы студентов,
# а внутренние ключи - "name", "age", "grade". Затем выведите имена всех студентов, чей возраст меньше 20 лет.
students = {
    1: {"name": "Alice", "age": 18, "grade": "A"},
    2: {"name": "Bob", "age": 22, "grade": "B"},
    3: {"name": "Frank", "age": 19, "grade": "C"},
    4: {"name": "Eva", "age": 21, "grade": "A"}
}
print(list(v["name"] for k,v in students.items() if v["age"] > 20))
print(list(v["name"] for v in students.values() if v["age"] > 20))

#Создайте список словарей, где каждый словарь представляет собой информацию о студенте (ключи: "name", "age", "grade").
# Затем отсортируйте список словарей по возрастанию значения ключа "age"
students = [
    {"name": "Alice", "age": 25, "grade": "A"},
    {"name": "Bob", "age": 30, "grade": "B"},
    {"name": "Frank", "age": 22, "grade": "C"},
    {"name": "Eva", "age": 28, "grade": "A"}
]
print(sorted(students,key=lambda student: student["age"]))

#Создайте список списков, где каждый внутренний список содержит числа от 1 до 5. Затем отсортируйте каждый внутренний список по возрастанию.

lists_of_numbers = [
    [3, 1, 5, 2, 4],
    [5, 4, 3],
    [2, 3, 1, 5, 4]
]
print([sorted(l) for l in lists_of_numbers])


lists_of_numbers = [
    [3, 1, 5, 2, 4],
    [5, 4, 3],
    [2, 3, 1, 5, 4]
]
list_sorted = []
for l in lists_of_numbers:
    list_sorted.append(sorted(l))
print(list_sorted)


#Удалите последнее множество из списка.
sets_list = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
]
sets_list.pop()
print(sets_list)

