###@Rinkame
#3.Напишите программу, которая удаляет повторяющиеся символы из заданной строки.
a = "gdfdyg"
a2 = ""
for i in a:
    if i not in a2:
        a2 += i
print(a2)



#2.Напишите программу, которая проверяет, является ли заданная строка правильным email-адресом.
a = "asd@yahoo.com"
print("@" in a)


# 1.Напишите программу, которая сравнивает две строки и выводит общие символы, которые они содержат.
a = "ar12g"
b = "1213a"
c = list(set(a + b))
d = "".join(c)
print(d)


### @RVMartirosov
#3.Напишите программу, которая заменяет все цифры в заданной строке символом '*'.
a = "gsqwg2"
a1 = ""
for i in a:
    if i.isdigit():
        i = "*"
    a1 += i
print(a1)


# 2.Напишите программу, которая удаляет все согласные буквы из заданной строки.
a = "gdfsaj"
a1 = ""
for i in a:
    if i in "aouie":
        a1 += i
print(a1)


# 1.Напишите программу, которая удаляет все гласные буквы из заданной строки.
a = "gdfsaj"
a1 = ""
for i in a:
    if not i in "aouie":
        a1 += i
print(a1)



### Катерина
#3.Напишите программу, которая проверяет, состоит ли заданная строка только из строчных букв.
a = "fdgrst"
b = True
for i in a:
    if i.istitle():
        b = False
print(b)

#2.Напишите программу, которая проверяет, состоит ли заданная строка только из заглавных букв.
a = "FGHNYJK"
b = True
for i in a:
    if not i.istitle():
        b = False
print(b)

# 1.Напишите программу, которая удаляет заданную подстроку из строки.
a = "223 is delete"
b = a.replace("223 ", "")
print(b)


###@Denwork21

#3.Напишите программу, которая проверяет, состоит ли заданная строка только из цифр.
a = "223"
b = True
c = True
for i in a:
    if not a.isdigit():
        b = False
    if not a.isnumeric():
        c = False
print(b)
print(c)


#2.Напишите программу, которая удаляет все знаки пунктуации из заданной строки.
a = "affg, 22!"
a1 = ""
for i in a:
    if i.isalpha() or i.isdigit() or i == " ":
        a1 += i
print(a1)

#1.Напишите программу, которая сортирует символы в заданной строке в алфавитном порядке.
a = "ghdfsya"
a = list(a)
a.sort()
b = "".join(a)
print(b)

a = "ghdfsya"
b = sorted(a)
a = "".join(b)
print(a)
