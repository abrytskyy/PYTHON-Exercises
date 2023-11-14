# Создайте функцию, которая принимает словарь и возвращает новый словарь,
# содержащий только элементы, значения которых являются числами.


vocabulary_input = {200: "Apple", "Orange": 150, "Mango": 200, "Gauva": 128, 100: 100}
def get_dict_digits(data: dict):
    new_dict = {}
    for key, value in data.items():
        if type(value) in (int, float):
            new_dict[key] = value
    return new_dict


print(get_dict_digits(vocabulary_input))