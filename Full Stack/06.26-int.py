#  Создайте функцию, которая принимает словарь и возвращает новый словарь,
#  содержащий только элементы, значения которых являются числами.

vocabulary_input1 = {200: "Apple", "Orange": 150, "Mango": 200, "Gauva": 128, 100: 100 }
def vocabulary_digit (a: dict):
    a.update((key, value * 2) for key, value in a.items())

    #for element in a:
        #if type(a.values) == int:
            #a[a.keys] = a[a.values * 2]
#    return a
    return a



print(vocabulary_values_multiply_2(vocabulary_input1))