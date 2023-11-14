dict1 = {1: 3, 2: 2.5, 3: True}
def multiply_value_2(a):
    a1 = {k: 2*v for k,v in a.items() if type(v) in (float, int)}
    return a1
print(multiply_value_2(dict1))
###Артём
#3. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, значения которых являются числами.
dict1 = {1: 3, "art": 2.5, "a": True}
def just_number_values(a):
    a1 = {k: v for k,v in a.items() if type(v) in (int, float)}
    return a1
print(just_number_values(dict1))

# 2. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы с ключами, состоящими только из букв.
dict1 = {1: 3, "art": 2.5, 3: True}
def just_str_keys(a):
    a1 = {k: v for k,v in a.items() if str(k).isalpha()}
    return a1
print(just_str_keys(dict1))

#1. Создайте функцию, которая принимает словарь и возвращает новый словарь, где все значения умножены на 2.
dict1 = {1: 3, 2: 2.5, 3: True}
def multiply_value_2(a):
    a1 = {}
    for k,v in a.items():
        if type(v) in (float, int):
            a1[k] = v*2

    return a1
print(multiply_value_2(dict1))

dict1 = {1: 3, 2: 2.5, 3: True}
def multiply_value_2(a):
    a1 = {k: 2*v for k,v in a.items() if type(v) in (float, int)}
    return a1
print(multiply_value_2(dict1))


### Катерина
#3. Создайте функцию, которая принимает словарь и элемент, и возвращает список всех значений,
# у которых ключ равен заданному элементу.
dict1 = {1: "ar", 2: "bra", 3: True}
elem = 3
def key_equal_elem(a, b):
    a1 = {k: v for k,v in a.items() if k == b}
    return a1
print(key_equal_elem(dict1, elem))

# 2. Создайте функцию, которая принимает словарь и элемент, и возвращает список всех ключей,
# у которых значение равно заданному элементу.
dict1 = {1: "ar", 2: "bra", 3: True}
elem = "bra"
def value_equal_elem(a, b):
    a1 = {k: v for k,v in a.items() if v == b}
    return a1
print(value_equal_elem(dict1, elem))

# 1. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, значения которых являются строками.
dict1 = {1: "ar", 2: "bra", 3: True}
def just_str(a):
    a1 = {k: v for k,v in a.items() if type(v) == str }
    return a1
print(just_str(dict1))



dict1 = {1: "ar", 2: 12, 3: True}
def just_str(a):
    a1 = {}
    for k,v in a.items():
        if type(v) == str:
            a1[k] = v
    return a1
print(just_str(dict1))


###@Denwork21
#3. Создайте функцию, которая принимает словарь и проверяет, есть ли в нем элементы с отрицательными значениями.
dict1 = {"Artem":1980, "Oleg": 1961, "anton": -1974 }
def minus_numbers(a):
    return any(v < 0 for v in a.values())


print(minus_numbers(dict1))

dict1 = {"Artem":1980, "Oleg": 1961, "anton": -1974 }
def minus_numbers(a):
    for v in a.values():
        if v < 0:
            return True

    return False

print(minus_numbers(dict1))

dict1 = {"Artem":1980, "Oleg": 1961, "anton": 1974 }
def minus_numbers(a):
    b = False
    for k,v in a.items():
        if v < 0:
            b =  True
            break
    return b

print(minus_numbers(dict1))

dict1 = {"Artem":1980, "Oleg": 1961, "anton": 1974 }
def minus_numbers(a):
    b = False
    for k,v in a.items():
        if v < 0:
            b =  True
            break
    return b

print(minus_numbers(dict1))



#1. Создайте функцию, которая принимает словарь и возвращает новый словарь, содержащий только элементы с четными значениями.
dict1 = {"Artem":1980, "Oleg": 1961, "anton": 1974 }
def even_values(a):
    a1 = {k: v for k,v in a.items() if v % 2 == 0 }

    return a1
print(even_values(dict1))

dict1 = {"Artem":1980, "Oleg": 1961, "anton": 1974 }
def even_values(a):
    a1 = {}
    for k,v in a.items():
        if v % 2 == 0:
            a1[k] = v
    return a1
print(even_values(dict1))


#2. Создайте функцию, которая принимает словарь и возвращает новый словарь, содержащий только элементы с ключами, начинающимися с буквы "а".
dict1 = {"Artem":1980, "Oleg": 1960, "anton": 1974 }
def key_starts_from_a(a):
    a1 = dict()
    for key,value in a.items():
        if key[0].lower() == "a":
            a1[key] = value
    return a1
print(key_starts_from_a(dict1))
