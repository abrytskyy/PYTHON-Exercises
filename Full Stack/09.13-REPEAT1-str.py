#Удалите все повторяющиеся символы из строки.
str = "Hello world"
str1 = ""
for s in str:
    

#Напишите функцию для объединения списка слов в строку с заданным разделителем.



#Переведите строку в верхний регистр.
#Переведите строку в нижний регистр.
#Проверьте, начинается ли строка с определенного подстроки.
#Проверьте, заканчивается ли строка на определенную подстроку.

str = "Hello world"
str1 = "Hello"
str2 = "world"
print(str.upper())
print(str.lower())
print(str.startswith(str1))
print(str.endswith(str2))

# Напишите функцию для удаления всех пробелов из строки.
str2 = "Напишите программу, которая"
def remove_spaces(str):
    return str.replace(" ", "")
print(remove_spaces(str2))

# Напишите программу, которая переворачивает строку задом наперед.
str = "которая переворачивае"
print(str[::-1])
# Определите, является ли строка палиндромом.
str1 = "aga"
print(str1 == str1[::-1])