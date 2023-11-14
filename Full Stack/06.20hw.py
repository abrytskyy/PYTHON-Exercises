###Артём
#Создайте функцию, которая принимает словарь и элемент, и удаляет этот элемент из словаря, если он существует.
dict1 = {"artem": "artem ", "taras": 2000}
elem = "artem"
dict2 = {}
def ElemDelInDict(a, b):
    if b in a :
        del a[b]


    return a

print(ElemDelInDict(dict1,elem))


#Создайте функцию, которая принимает словарь и возвращает количество его элементов.
dict1 = {"artem": 1980, "taras": 2000}
def number_of_elem(a):
    return len(a)
print(number_of_elem(dict1))

###Катерина
#Создайте функцию, которая принимает два словаря и объединяет их в один.

dict1 = {"artem": 1980, "taras": 2000}
dict2 = {"ivan": 1983, "taras": 2006}
def combine_dict(a,b):
    dict1.update(dict2)
    return dict1
print(combine_dict(dict1, dict2))


#Создайте функцию, которая принимает словарь и элемент, и проверяет, содержится ли этот элемент в словаре.
dict1 = {"arte": "artem ", "taras": 2000}
elem = "artem"
def ElemInDict(a, b):
    return b in a or b in a.values()
print(ElemInDict(dict1,elem))


###@Denwork21
#Создайте словарь с данными о погоде на несколько дней (дата в качестве ключа).
# Напишите функцию, которая выводит самый холодный и самый теплый день.
dict_wether = {"26.07": 25, "27.07": 20, "28.07": 21}
def most_cold_and_hot(a):
    hottest_day = "hottest day: " +  max(a), max(a.values())
    coldast_day = "coldest day: " + min(a), min(a.values())

    return [hottest_day, coldast_day]
print(most_cold_and_hot(dict_wether))

#Напишите функцию, которая принимает на вход словарь с именами студентов и их оценками и возвращает средний балл группы.
dict1 = {"Peter Odd": 5, "Artem Brytskyy": 6, "Ivan Iv": 4}
def name_and_scores(a):
    sum = 0
    for value in a.values():
        sum += value
    return sum/len(a)
print(name_and_scores(dict1))
