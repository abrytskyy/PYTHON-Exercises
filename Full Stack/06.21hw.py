###Артём
#Создайте функцию, которая принимает словарь и возвращает новый словарь, где ключи и значения поменяны местами.
dict = {"Artem":20, "Taras":10, "Ivan":15}
def value_more_10(a):
    a1 = {}
    for key,value in a.items():
        a1[value] = key
    return a1
print(value_more_10(dict))

#Создайте функцию, которая принимает словарь и возвращает список всех ключей, у которых значения больше 10.
dict = {6:20, 3:10, 5:15}
def value_more_10(a):
    a1 = []
    for key,value in a.items():
        if value > 10:
            a1.append([key, value])
    return a1
print(value_more_10(dict))

###Катерина

#Создайте функцию, которая принимает словарь и возвращает среднее значение всех его элементов.
dict = {6:20, 3:10, 5:15}
def sum_values(a):
    return sum(a.values())
def average_values(a):
    return sum_values(a)/len(a)
print(average_values(dict))




dict = {6:20, 3:10, 5:15}
def average_values(a):
    return sum(a.values())/len(dict)
print(average_values(dict))


#Создайте функцию, которая принимает словарь и возвращает сумму всех его значений.
dict = {6:20, 3:10, 5:15}
def sum_values(a):
    return sum(a.values())
print(sum_values(dict))


###@Denwork21
#Создайте функцию, которая принимает словарь и возвращает наименьшее значение из всех его элементов.
dict = {6:20, 3:10, 5:15}

def min_elem(a):
    return min(a.items(), key = lambda item:item[1])
    #for i in a:
print(min_elem(dict))


dict = {1:20, 3:10, 5:15}
def get_value(pair):
    return pair[1]
def min_elem(a):

    return min(a.items(), key=get_value)
print(min_elem(dict))


dict = {1:20, 3:10, 5:15}
def min_elem(a):
    return min(a.items(), key=lambda item: item[1])
print(min_elem(dict))


# #Создайте функцию, которая принимает словарь и возвращает наибольшее значение из всех его элементов.
# dict = {1:20, 3:10, 5:15}
#
# def max_elem(a):
#     max = 0
#     max_value = 0
#     for i in a:
#         if a[i] > max_value:
#             max = i
#             max_value = a[i]
#
#     return max, a[max]
# print(max_elem(dict))

