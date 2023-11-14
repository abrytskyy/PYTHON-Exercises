
#Создайте функцию, которая принимает вложенный словарь
# (представляющий собой информацию о студентах и их оценках) и возвращает новый словарь,
# содержащий список студентов, у которых средняя оценка выше заданного порога.



# Создайте функцию, которая принимает список словарей
# (представляющих собой информацию о товарах) и возвращает новый список,
# содержащий только товары с количеством больше или равным 10.

a = [
    {"goods": "milk", "number" : 20},
    {"goods": "bread", "number" : 8},
    {"goods": "orange", "number" : 100},
    {"goods": "oil", "number" : 6},
]
b = []
for i in a:

    if i("number") > 10:
        b.append(i)

print(b)
    #for key in i.keys("number"):
        #if i.keys("number") > 10:








#Найдите пересечение первых двух множеств из списка.
users = {"Tom", "Bob", "Alice", "Tom"}
users2 = {"Sam", "Kate", "Bob", "Alice"}
users3 = {"Sam", "Tom", "Bob", "Alice", "Greg"}
users5 = users.intersection(users2)
print(users5)

#Найдите объединение всех множеств из списка.

# Найдите пересечение всех множеств из списка.
users = {"Tom", "Bob", "Alice", "Tom"}
users2 = {"Sam", "Kate", "Bob"}
users3 = {"Sam", "Tom", "Bob", "Alice", "Greg"}
users4 = users.intersection(users2, users3)
print(users4)

# Объедините все множества из списка в одно множество.
users = {"Tom", "Bob", "Alice", "Tom"}
users2 = {"Sam", "Kate", "Bob"}
users3 = {"Sam", "Tom", "Bob", "Alice", "Greg"}
users4 = users.union(users2, users3)
print(users4)
