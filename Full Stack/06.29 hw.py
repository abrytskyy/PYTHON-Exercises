
###Артём
# Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, у которых ключи являются числами и значения больше заданного числа.
dict ={6: "art", 1980: "1980", "les": 1967}
number = 1975
def key_isdigit(a, b):
    a1 = {k:a[k] for k,v in a.items() if isinstance(k, (int, float)) and k > b }
    return a1
print(key_isdigit(dict, number))

#2. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, ключи которых начинаются с гласной буквы.
dict ={"ARTEM": "art", "Ivan": "1980", "les": 1967}
def key_from_vowel(a):
    a1 = {k:a[k] for k,v in a.items() if k[0].lower() in "aouei"}
    # a1 = {}
    # for k,v in a.items():
    #     if k[0].lower() in "aouie":
    #         a1[k] = v
    return a1
print(key_from_vowel(dict))


#1. Создайте функцию, которая принимает два словаря и возвращает новый словарь, содержащий только те элементы,
# у которых значения в обоих исходных словарях являются строками и имеют одинаковую длину.




dict ={"ARTEM": "art", "Ivan": "1980", "Oles": 1967}
dict1 ={"ARTEM": 1980, "Ivan": "abcd", "Oles": "ivo"}
def key_isdigit(a, b):
    c = {}
    for ka,va in a.items():

        for kb,vb in b.items():
            if type(va) == str and type(vb) == str and len(va) == len(vb):
                c[ka] = va
                c[kb] = vb
        return c
print(key_isdigit(dict,dict1))




###Катерина
#3. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, значения которых являются списками и содержат элементы, являющиеся числами.
dict ={"ARTEM": 1980, "Ivan": [1980], "Oles": 1967}
def key_list_with_numbers(a):
    a1 = {k:a[k] for k,v in a.items() if type(v) == list and all(type(j) in (int, float) for j in v) }
    return a1
print(key_list_with_numbers(dict))

#2. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, ключи которых состоят только из букв нижнего регистра.
dict ={"ARTEM": 1980, "Ivan": [1980], "oles": 1967}
def value_list(a):
    a1 = {k:a[k] for k,v in a.items() if type(k) == str and k.islower()}
    return a1
print(value_list(dict))
#1. Создайте функцию, которая принимает словарь и возвращает среднее значение всех числовых значений в словаре.
dict ={"ARTEM": 1980, "Ivan": 1970, "Oles": 1960}
def average_value(a):
    return sum(a.values())/ len(a)
print(average_value(dict))

###@Denwork21
#Создайте функцию, которая принимает словарь и возвращает список ключей, у которых значения являются списками ненулевой длины

#2.Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, значения которых являются списками и содержат хотя бы один элемент.
dict ={"ARTEM": 1980, "Ivan": [1980], "Oles": 1967}
def value_list(a):
    a1 = {k:a[k] for k,v in a.items() if type(v) == list and len(v) > 0}
    return a1
print(value_list(dict))

#1.Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, ключи которых состоят только из букв верхнего регистра.
dict ={"ARTEM": 1980, "Ivan": 1970, "Oles": 1967}
def key_upper(a):
    a1 = {k:a[k] for k,v in a.items() if k.isupper()}
    return a1
print(key_upper(dict))