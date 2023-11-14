###Артём
#Создайте функцию, которая принимает словарь и элемент, и возвращает новый словарь,
# содержащий только элементы, значения которых содержат заданную подстроку.
dict1 = {"art": 1, "bor": "bor", "iv": 5,"art1": 2, "bora": 3 }
elem = "or"
def dict_wit_elem(a, b):
    a1 = {k: a[k] for k,v in a.items() if b in str(v)}
    return a1
print(dict_wit_elem(dict1, elem))

#Создайте функцию, которая принимает словарь и возвращает список уникальных значений в словаре.

dict1 = {"art": 1, "bor": 3, "iv": 5,"art1": 2, "bora": 3 }
def unique(a):
    a1 = {}
    for k,v in a.items():
        if v not in a1.values():
            a1[k] = v
    return a1
print(unique(dict1))


def merge_dicts(dict1, dict2):
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

# Пример использования функции
dict1 = {
    "apple": 20,
    "banana": 35,
    "orange": 30
}

dict2 = {
    "banana": 15,
    "kiwi": 10,
    "grapes": 25
}

result_dict = merge_dicts(dict1, dict2)
print(result_dict)
#Создайте функцию, которая принимает два словаря и объединяет их,
# при этом значения с одинаковыми ключами складываются, а новые ключи добавляются в итоговый словарь
dict1 = {"art": 1, "bor": 3, "iv": 5}
dict2 = {"art": 2, "bora": 3, "iv": 3}
def combine(a,b):
    for ka,va in a.items():
        for kb,vb in b.items():
            if kb in ka:
                a[ka] = va, vb
    for kb,vb in b.items():
        if kb not in a:
            a[kb] = vb
    return a
print((combine(dict1, dict2)))

###Катерина
#Создайте функцию, которая принимает словарь и возвращает сумму всех значений, у которых ключи являются четными числами.
dict1 = {2: "Avto", "bor": 4, 3: True}
def keys_just_digits(a):
    a1 = {k: a[k] for k,v in a.items() if isinstance(k, (int,float)) and k % 2 == 0}
    return a1
print((keys_just_digits(dict1)))

#Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, ключи которых состоят только из цифр.
dict1 = {"art": "Avto", "bor": 4, 3: True}
def keys_just_digits(a):
    a1 = {k: a[k] for k,v in a.items() if isinstance(k, (int,float))}
    return a1
print((keys_just_digits(dict1)))

#Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, значения которых являются строками и начинаются с заглавной буквы.
dict1 = {"art": "Avto", "bor": 4, "iv": True}
def str_from_upper(a):
    a1 = {}
    for k, v in a.items():
        if type(v) == str and v.istitle():
            a1[k] = v
    return a1
print((str_from_upper(dict1)))


dict1 = {"art": "Avto", "bor": 4, "iv": True}
def str_from_upper(a):
    a1 = {k: a[k] for k,v in a.items() if isinstance(v, str) and v.istitle() }
    return a1
print((str_from_upper(dict1)))


###@Denwork21
#Создайте функцию, которая принимает словарь и возвращает список ключей, у которых значение является четным числом.
dict1 = {"art": 1, "bor": 4, "iv": 5}
def list_key_with_value_equal_max(a):
    b = [v for v in a.values() if v % 2 == 0]


    return b
print(list_key_with_value_equal_max(dict1))
#Создайте функцию, которая принимает два словаря и возвращает новый словарь,
# содержащий только те элементы, которые есть в обоих исходных словарях.
dict1 = {"art": 1, "bor": 3, "iv": 5}
dict2 = {"art": 1, "bora": 3, "iv": 3}
def intersect_dict(a, b):
    return {k:a[k] for k in a if k in b and a[k] == b[k]}
print(intersect_dict(dict1, dict2))

#Создайте функцию, которая принимает словарь и возвращает список ключей,
# у которых значение равно максимальному значению в словаре.
dict1 = {"art": 1, "bor": 3, "iv": 5}
def list_key_with_value_equal_max(a):
    b = [v for v in a.values() if v == max(a.values())]


    return b
print(list_key_with_value_equal_max(dict1))


dict1 = {"art": 1, "bor": 3, "iv": 5}
def list_key_with_value_equal_max(a):
    b = []
    for v in a.values():
        if v == max(a.values()):
            b.append(v)
    return b
print(list_key_with_value_equal_max(dict1))
