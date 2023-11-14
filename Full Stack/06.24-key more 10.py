# Создайте функцию, которая принимает словарь и
# возвращает список всех ключей, у которых значения больше 10.

vocabulary_input1 = {200: "Apple", "Orange": 150, "Mango": 196, "Gauva": 128, 100: 100 }
def vocabulary_key_more_10(a: dict):
    key_list = []
    for key in a.keys():
        if type(key) == int:
            if key > 10:
                key_list.append(key)

    return key_list
print(vocabulary_key_more_10(vocabulary_input1))
