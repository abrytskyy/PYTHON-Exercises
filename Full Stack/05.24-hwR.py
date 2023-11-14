# 3. Определение весовой категории:
# Напишите программу, которая запрашивает у пользователя его вес в килограммах
# и определяет его весовую категорию: "Недостаточный вес", "Нормальный вес", "Избыточный вес" или "Ожирение".
# Используйте формулу индекса массы тела (ИМТ) для определения категории.


b = int(input("input your height in cm: "))
b = b / 100
a = bmi/(b**2)
if bmi < 16:
    print("Severe Thinness")
elif bmi < 17:
    print("Moderate Thinness")
elif bmi < 18.5:
    print("Mild Thinness")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese Class I")
elif bmi < 40:
    print("Obese Class II")
else:
    print("Obese Class III")




a = int(input("input your weight in kg: "))
b = int(input("input your height in cm: "))
b = b / 100
bmi = a/(b**2)
if bmi < 16:
    print("Severe Thinness")
elif bmi < 17:
    print("Moderate Thinness")
elif bmi < 18.5:
    print("Mild Thinness")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese Class I")
elif bmi < 40:
    print("Obese Class II")
else:
    print("Obese Class III")




# 2. Определение победителя в игре "Камень, ножницы, бумага":
# Напишите программу, которая запрашивает у двух игроков их выбор в игре
# "Камень, ножницы, бумага" (0 - камень, 1 - ножницы, 2 - бумага) и определяет победителя.
# Правила: камень побеждает ножницы, ножницы побеждают бумагу, бумага побеждает камень.
# Если выборы игроков одинаковы, программа должна выводить сообщение "Ничья".
a = int(input("""Player 1. Type:
 0 - for stone,
 1 - for scissors,
 2 - for paper  
"""))
b = int(input("""Player 2. Type:
 0 - for stone,
 1 - for scissors,
 2 - for paper
"""))
if a == 0:
    if b == 0:
        print("Draw")
    elif b == 1:
        print("Player 1 won")
    else:
        print("Player 2 won")
elif a == 1:
    if b == 0:
        print("Player 2 won")
    elif b == 1:
        print("Draw")
    else:
        print("Player 1 won")
else:
    if b == 0:
        print("Player 1 won")
    elif b == 1:
        print("Player 2 won")
    else:
        print("Draw")



# 1. Напишите программу, которая запрашивает у пользователя число и проверяет,
# делится ли оно и на само себя, и на сумму своих цифр без остатка.
# Если число удовлетворяет обоим условиям, выведите сообщение
# "Число делится и на само себя, и на сумму своих цифр", в противном случае -
# "Число не удовлетворяет обоим условиям".
a = input("input digit: ")

b = int(a[0] + a[1])
if int(a) % b == 0:
    print("digit is divided by sum of own digits")
else:
    print("digit is not divided by sum of own digits")
