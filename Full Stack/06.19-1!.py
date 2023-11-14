#Напишите функцию, которая принимает список чисел и возвращает сумму всех положительных чисел и
# произведение всех отрицательных чисел.

digits = [3,5,-3,4,-5-3]

def func(a):
    sum1 = 0
    mult = 1
    for i in a:
        if i >0:
            sum1 += i
        else:
            mult *= i

    return sum1, mult

print(func(digits))
