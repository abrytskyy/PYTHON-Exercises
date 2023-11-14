# 1. Создайте функцию, которая принимает два словаря и возвращает новый словарь,
# содержащий только те элементы, у которых значения
# в обоих исходных словарях являются строками и имеют одинаковую длину.

dict1 = {10: "a", "b": 8}
dict2 = {"c": 6, 8: "b"}
def two_dictionary(dictionary1, dictionary2):
    dict3 = {}
    dictionary1.update(dictionary2)
    for key,val in dictionary1.items():
        if type(val) == str and len(val) == 1:
            dict3[key] = val
    return dict3

print(two_dictionary(dict1,dict2))
