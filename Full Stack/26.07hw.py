#Вводится двумерный список в виде таблицы целых чисел (см. пример ниже). С помощью list comprehension
# преобразовать двумерный список в одномерный так, чтобы значения элементов шли в обратном порядке.
# Результат отобразить в виде строки из чисел, записанных через пробел.
[]

tabl = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
]
def transform(a):
    a1 =[]

    for i in reversed(a):
        for j in reversed(i):
            a1.append(j)
    return a1
print(transform(tabl))

tabl = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
]
def transform(a):
    a1 =[]
    a = a[::-1]
    for i in a:
        a1.append(i[::-1])
    return a1
print(transform(tabl))

#Фильтрация слов из списка на основе их длины (например, все слова длиной менее 5 символов).
list_word= ["artem", "ivan", "alibaba"]
def filtr_length(a, b):
    a1 = []
    for i in a:
        if len(i) > b:
            a1.append(i)
    return a1
print(filtr_length(list_word, 5))


#Извлечь из списка только числа, находящиеся в определенном диапазоне.
lst = [2, 101, 25, -10]
def number_in_range(a, b, c):
    a1 = []
    for i in a:
        if i in range(b,c):
            a1.append(i)
    return a1
print(number_in_range(lst,10, 110))


#Отфильтровать имена, начинающиеся с определенной буквы, из списка имен.
list1 = ["Artem", "Ivan", "Ivo", "Anton"]
def filter(a, b):
    a1 = []
    for i in a:
        if i[0].lower() == b.lower():
            a1.append(i)
    return(a1)
print(filter(list1, "a"))
