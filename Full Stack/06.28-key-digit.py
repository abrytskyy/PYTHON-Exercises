# Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы с ключами, состоящими только из букв.
vocabulary_input = {200: "Apple", "Orange": 150, "Mango": 200, "Gauva": 128, 100: 100}
def dict_key_letters(data:dict):
    new_dict = {}
    for key,value in data.items():
        if type(key) == str:
            new_dict[key] = value
    return new_dict
print(dict_key_letters(vocabulary_input))


