# Напишите программу, которая переворачивает строку задом наперед.
str = "которая переворачивае"
print(str[::-1])
# Определите, является ли строка палиндромом.
str1 = "aga"
print(str1 == str1[::-1])
# Напишите функцию для удаления всех пробелов из строки.
str2 = "Напишите программу, которая"
def remove_spaces(str):
    return str.replace(" ", "")
print(remove_spaces(str2))
str = "Hello world"
str1 = "Hello"
str2 = "world"
print(str.upper())
print(str.lower())
print(str.startswith(str1))
print(str.endswith(str2))



###Катерина
#Создать список всех палиндромов в диапазоне от 1 до 1000 с использованием генератора списков.
[i for i in range ()]

#Создать список всех чисел от 1 до 100, возведенных в квадрат, если число делится на 3 с использованием генератора списков.
print([i**2 for i in range(1, 101) if i % 3 == 0])

#Создать новый список, содержащий только уникальные элементы из исходного списка с использованием лямбда-функции.
list1 =[3, 1, 2, 3, 1]
unique = lambda x: list(set(x))
print(unique(list1))

#Проверить, есть ли в списке хотя бы одно отрицательное число с использованием лямбда-функции.
numbers = [1, 2, 3, -4, 5]
has_negative = any(lambda x: x < 0 for x in numbers)
print(has_negative)

positive = lambda x: len([i for i in x if i < 0]) > 0
print(positive([1,2,-3]))

#Hайти среднее значение списка чисел с использованием лямбда-функции.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
average = reduce(lambda x, y: x + y, numbers) / len(numbers)
print(average)

avarage = lambda x: sum(x)/len(x)
print(avarage([1, 2, 3, 4]))

###@Denwork21
#Создать список всех чисел от 1 до 1000, которые делятся на 3 и 5 с использованием генератора
# списков.
print([i for i in range(1, 1001) if i%15 == 0])
#Создать список всех слов в предложении, содержащих более 3-х символов с использованием
# генератора списков
sentence = "Это пример предложения с несколькими словами"
print([word for word in sentence.split() if len(word) > 3])

#Создать список всех букв в строке в верхнем регистре с использованием генератора списков.
sentence = "Это пример предложения с Fесколькими словами"
print([word for word in sentence.split() if len(word) > 3])


#Проверить, являются ли все элементы списка положительными числами с использованием лямбда-функции.
positive = lambda x: len([el for el in x if el<0 ])
print(positive([2,3,5,1])==0)

#Найти наибольший элемент в списке чисел с использованием лямбда-функции.
max_number = max([2,3,5,1], key=lambda x: x)
print(max_number)

max_el = lambda x: max(x)
print(max_el([2,3,5,1]))

#Посчитать сумму квадратов чисел в списке с использованием лямбда-функции.
in2 = lambda x: sum([e*e for e in x])
print(in2([1,2,3]))


