#2. Определение победителя в игре "Камень, ножницы, бумага":
# Напишите программу, которая запрашивает у двух игроков их выбор в игре
# "Камень, ножницы, бумага" (0 - камень, 1 - ножницы, 2 - бумага) и определяет победителя.
# Правила: камень побеждает ножницы, ножницы побеждают бумагу, бумага побеждает камень.
# Если выборы игроков одинаковы, программа должна выводить сообщение "Ничья".
player1 = int(input("Input 0 - камень, 1 - ножницы, 2 - бумага"))
player2 = int(input("Input 0 - камень, 1 - ножницы, 2 - бумага"))

result = player1 - player2

if player1 == player2:
    print("Nichja")
elif result == -1 or result == 2:
    print("player1")
else:
    print("player2")

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

