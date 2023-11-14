#Создайте функцию, которая принимает словарь и
# возвращает новый словарь, где ключи и значения поменяны местами.

vocabulary_input1 = {200: "Apple", "Orange": 150, "Mango": 196, "Gauva": 128}
def vocabulary_key_value_exchange(a: dict):
    new_dict = dict([(value, key) for key, value in a.items()])

    return new_dict
print(vocabulary_key_value_exchange(vocabulary_input1))