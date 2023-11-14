# 3. Определение дня недели:
# Напишите программу, которая запрашивает у пользователя число от 1 до 7 и выводит
# соответствующий день недели: 1 - "Понедельник", 2 - "Вторник", и так далее.
a = int(input("input digit from 1 to 7: "))
if a == 1:
    print("Monday")
elif a == 2:
    print("Tuesday")
elif a == 3:
    print("Wednesday")
elif a == 4:
    print("Thursday")
elif a == 5:
    print("Friday")
elif a == 6:
    print("Saturday")
elif a == 7:
    print("Sunday")
else:
    print("Wrong number")

# 2. Определение четности числа:
# Напишите программу, которая запрашивает у пользователя число и выводит сообщение "Четное",
# если число четное, или "Нечетное", если число нечетное.
a = int(input("input digit: "))
if a % 2 == 0:
    print("Digit is even")
else:
    print("Digit is odd")

# 1. Проверка на делимость на 4:
# Напишите программу, которая запрашивает у пользователя число и проверяет,
# делится ли оно на 4 без остатка. Если число делится на 4 без остатка,
# выведите сообщение "Число делится на 4", в противном случае - "Число не делится на 4".
a = int(input("input digit: "))
if a % 4 == 0:
    print("Digit is divisible by 4")
else:
    print("Digit is not divisible by 4")


a = int(input("input digit: "))
print(a % 4 == 0)
