### List Comprehension
# Создать список всех целых чисел от -10 до 10 с использованием генератора списков.
numbers = [n for n in range(-10, 11)]
print(numbers)


# Создать список всех факториалов чисел от 1 до 10 с использованием генератора списков.
fakt = 1
for i in range(1, 11):
    fakt *= i
    print(fakt)


numbers = [n * numbers for n in range(1, 11)]
print(numbers)


# Создать список всех возможных комбинаций букв "ABC" и цифр "123" с использованием генератора списков
a = "ABC"
b = "123"
ab = ""
for i in range(len(a)):
    for j in range(len(b)):
        ab += a[i] + b[j]
print(ab)



a = "ABC"
b = "123"
ab = [a for a in range(len(b))]



### Лямбда

#Найти наибольшую длину строки в списке с использованием лямбда-функции.
a = ["as", "asdf", "abc"]
longest = lambda l : max(l, key = len)
print(longest(a))

#Проверить, является ли строка палиндромом с использованием лямбда-функции.
a = "abcdcba"
palindrom = lambda a: print(a == a[::-1])
palindrom(a)


#Умножить каждый элемент списка на заданное число с использованием лямбда-функции.

a = ["asd", 3, "gfd", True]
a1 =[]
b = 5
for i in a:
    a1.append(i*b)
print(a1)


a = ["asd", 3, "gfd", True]
a1 =[]
b = 5
for i in a:
    temp = lambda i: i*b
    a1.append(temp(i))
print(a1)



multiply = lambda a, b: a*b
print(multiply((["asd", 3, "gfd", True]),5))