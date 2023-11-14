###Артём
## raspakovka
#Упакуйте значения 10, 20 и 30 в кортеж и присвойте его переменной my_tuple.
a = 10
b = 20
c = 30
*my_tuple, = a, b, c
print(my_tuple)

# Распакуйте строку "hello" и присвойте каждую букву переменным a, b, c, d, и e.
hello = "hello"
a,b,c,d,e = hello
print(b)
#Распакуйте список [1, 2, 3] и присвойте переменным a, b, и c соответствующие значения.
numbers = [1, 2, 3]
a,b,c = numbers
print(b)

## *args
#Напишите функцию, которая принимает неограниченное количество аргументов *args и возвращает их произведение.
def mult1(*args):
    mult = 1
    for arg in args:
        mult *= arg
    return mult
print(mult1(2, 3, 4, 5, 1))

#Напишите функцию, которая принимает неограниченное количество аргументов *args и возвращает их сумму.


def sum1(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(sum1(2, 3, 4, 5, 1))


##list comprehention

#Создайте генератор, который возвращает все числа в интервале [start, end], заданном аргументами функции.
def interval(a,b):
    n1 = []
    [n1.append(n) for n in range(a, b + 1)]
    print(n1)
interval(2, 5)

#Напишите генератор, который возвращает все нечетные числа от 1 до 100.
numbers = [n for n in range(1, 101) if n % 2 == 1]
print(numbers)


#Реализуйте генератор, который возвращает все четные числа от 1 до 100.
numbers = [n for n in range(1, 101) if n % 2 == 0]
print(numbers)

