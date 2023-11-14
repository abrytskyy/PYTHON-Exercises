


a = "restart"
index = a.find("r")
char = a[index]
temp = a.replace(char, "$")
result_str = char + temp[1:]
print(result_str)


a = "abc"
b = "xyz"
a1 = a[:2]
a2 = a[2]
b1 = b[:2]
b2 = b[2]
print(a1  + b2)
print(a2 + b1)


text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])  # дуб,

# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])  # в два обхвата дуб

# разбиение по первым пяти пробелам
splitted_text = text.split(" ", 5)
print(splitted_text)
print(splitted_text[4])  # обхвата дуб, с обломанными ветвями и с обломанной корой


string = ["a", "bc", "def"]

print("".join(string))

string = ["a", "bc", "def"]
symbol = ""
print(symbol.join(string))

#import random
from random import randint

rows = 3
columns = 5

matrix = []

for i in range(rows):
    temp = []
    for j in range(columns):
        number = randint(1, 20)
        temp.append(number)
    matrix.append(temp)
print(*matrix)