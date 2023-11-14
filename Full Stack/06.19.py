# 4. Напишите программу, которая принимает строку и подсчитывает количество вхождений каждого символа в строку.
# Результат должен быть представлен в виде словаря.
def str_to_dict1(a):
    a1 = {}
    for i in a:
        if i in a1:
            a1[i] += 1
        else:
            a1[i] = 1
    return a1
input_string = input("Input data: ").replace(" ", "")
print(str_to_dict1(input_string))

# 3. Создайте функцию, которая принимает список слов и возвращает словарь, где ключами являются слова, а значениями - их длины.
lst = ["arte", "ivanov"]
def str_to_dict (a):
    a1 = dict()
    for i in a:
        a1[i] = len(i)
    return a1
print(str_to_dict(lst))


#2. Напишите функцию, которая принимает словарь и возвращает список всех значений в словаре.
def get_values(dictionary):
    return list(dictionary.values())


def convert_lst_to_dict(lst):
    output_lst = []
    for data in lst:
        output_lst.append(data.split())
    return dict(output_lst)


input_string = input("Input data: ")

strings = input_string.split(", ")
print(strings)
print(convert_lst_to_dict(strings))

dictionary = convert_lst_to_dict(strings)

print(get_values(dictionary))


object = {}
object = dict()

