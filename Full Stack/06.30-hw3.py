# 3. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, у которых ключи являются числами и
# значения больше заданного числа.


dict1 = {6: "a", "a": 8, 8: "c"}
digit = int(input("input digit: "))
def key_digit_more_than(dictionary1):
    dict3 = {}

    for key,val in dictionary1.items():
        if (type(key) == int or type(key) == float) and key > digit:
            dict3[key] = val
    return dict3

print(key_digit_more_than(dict1))