# 3. Определение года високосности:
# Напишите программу, которая запрашивает у пользователя год и выводит сообщение "Год високосный",
# если год является високосным, или "Год не високосный", если год не является високосным. Год является високосным,
# если он кратен 4, но не кратен 100, за исключением годов, кратных 400.
year = int(input("Print year: "))
if year % 400 == 0:
    print("It's a leap year")
elif year % 100 == 0:
    print("It's not a leap year")
elif year % 4 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")




year = int(input("Print year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(" Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

def leapyr(n):
    if n%4==0 and n%100!=0:
        if n%400==0:
            print(n, "is a leap year.")
    elif n%4!=0:
        print(n, "is not a leap year.")
print(leapyr(1900))






# 1. Проверка на четность трех чисел:
# Напишите программу, которая запрашивает у пользователя три числа и проверяет,
# являются ли все три числа четными. Используйте оператор % для проверки каждого числа на четность.
# Если все три числа четные, выведите сообщение "Все числа четные", в противном случае - выведите "Не все числа четные".

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
if a % 2 == 0 and b % 2 ==0 and c % 2 == 0:
    print("All digits are even")
else:
    print("Not all digits are even")


# 2. Определение положительности числа:
# Напишите программу, которая запрашивает у пользователя число и выводит сообщение "Положительное",
# если число больше нуля, "Отрицательное", если число меньше нуля, или "Ноль", если число равно нулю.

number = int(input("Input number: "))
if number > 0:
    print("It's plus number")
elif number < 0:
    print("It's minus number")
else:
    print("It's zero")


