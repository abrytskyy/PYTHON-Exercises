#Создайте лямбда-функцию, которая возвращает список строк, содержащих только буквы.
just_letters = lambda a: a.isalpha()
print(just_letters(["artem 123", "abc"]))

# Создайте лямбда-функцию, которая возвращает список строк в верхнем регистре.
str_upper = lambda a: a.title()
print(str_upper(["artem", "ivan"]))


#Создайте лямбда-функцию, которая проверяет, является ли каждый элемент списка положительным.

a =[]
pluss = lambda a: [a.append(i) for i in [1,2,3] if i > 0]
print(pluss(a))

a = [2, 3, 5, 8]
b = True
for i in a:
    if i < 0:
        b = False
print(b)
