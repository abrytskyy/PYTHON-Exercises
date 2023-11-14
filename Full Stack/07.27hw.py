###Артём

#Напишите функцию, которая принимает список кортежей (имя, возраст) и
# возвращает список имен, отсортированных по возрастанию возраста, используя lambda и sorted.
list_of_tuples = [("Artem", 20), ("Ivan", 10), ("Taras", 30)]
def ascending_age(a):
    a1 = sorted(a,key = lambda a_item: a_item[1])
    return [(name,age) for name,age in a1]
print(ascending_age(list_of_tuples))


#Создайте программу, которая принимает список чисел и возвращает новый список,
# содержащий только положительные числа, используя lambda и filter.
list1  = [2, 3, -4, -2, 4]
def plus_numbers(a):
    a1 = filter(lambda b: b > 0, a)
    return list(a1)
print(plus_numbers(list1))

#Создайте программу, которая принимает список строк и возвращает новый список,
# содержащий только строки с длиной больше 5 символов, используя lambda и filter.
list1  = ["Artem", "Ivanova", "Igor"]
def more_5(a):
    a1 = filter(lambda b: len(b) > 5, a)
    return list(a1)
print(more_5(list1))


list1  = ["Artem", "Ivanova", "Igor"]
def more_5(a):
    a1 = []
    for i in a:
        if len(i) > 5:
            a1.append(i)
    return a1
print(more_5(list1))

#Напишите функцию, которая принимает два кортежа и возвращает новый кортеж, содержащий элементы обоих кортежей.
tuple1 = (12, 2, 3, 42, 3, 1)
tuple2 = (1, 2, 3, 4, 3, 1)
def combine_tuples(a,b):
    return a + b
print(combine_tuples(tuple1, tuple2))

#Создайте программу, которая принимает два списка и объединяет их в один, затем выводит результат.
list1 = [12, 2, 3, 42, 3, 1]
list2 = [12, 2, 3, 42, 3, 1]
def combine_2lists(a,b):
    a.extend(b)
    return a
print(combine_2lists(list1, list2))



list1 = [12, 2, 3, 42, 3, 1]
list2 = [12, 2, 3, 42, 3, 1]
def combine_2lists(a,b):
    return a+b
print(combine_2lists(list1, list2))



#Напишите функцию, которая принимает список и возвращает новый список без дубликатов.
list1 = [12, 2, 3, 42, 3, 1]
def withouth_dublicates(a):
    return list(set(a))
print(withouth_dublicates(list1))


#Создайте программу, которая меняет местами ключи и значения в словаре и выводит полученный результат.
dict1  = {"Artem":1980, "Ivan":1970, "Igor": 1993}
def change_key_with_value(a):
    a1 = dict()
    for k,v in a.items():
        a1[v] = k
    return a1
print(change_key_with_value(dict1))


