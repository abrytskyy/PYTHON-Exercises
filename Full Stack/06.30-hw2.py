#2. Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, ключи которых начинаются с гласной буквы.


dict1 = {"b": "a", "a": 8}

def key_from_vowel(dictionary1):
    dict3 = {}

    for key,val in dictionary1.items():
        if key[0] == "a" or key[0] == "e" or key[0] == "i" or key[0] == "o" or key[0] == "u":
            dict3[key] = val
    return dict3

print(key_from_vowel(dict1))