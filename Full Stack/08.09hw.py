###
#Удвоить все числа в списке.
#Привести все строки к нижнему регистру.
#Возвести все числа в квадрат.
#Умножить каждое число на 10.
numbers = [1, 2, 3, 4, 5]
strings = ["Apple", "Banana", "Orange", "Grapefruit"]
# Удвоить все числа в списке
doubled_numbers = list(map(lambda x: x * 2, numbers))
lowercase_strings = list(map(lambda x: x.lower(), strings))
squared_numbers = list(map(lambda x: x**2, numbers))
multiplied_numbers = list(map(lambda x: x*10, numbers))
print(doubled_numbers)
print(lowercase_strings)
print(squared_numbers)
print(multiplied_numbers)


#Посчитайте общее количество символов во всех строках массива.
#Найдите самую короткую строку в массиве.
#Найдите самую длинную строку в массиве.

list1 = ["apple", "banana", "orange", "grapefruit"]
total_characters = sum(len(string) for string in list1)
shortest_string = min(list1, key=len)
longest_string = max(list1, key=len)
print(total_characters,shortest_string,longest_string)
