



###@Rinkame
# 4.Напишите программу, которая проверяет, является ли заданная строка анаграммой другой заданной строки.

a = "dog"
b = "gsdo"
for i in a:
    if i in b:
        b = b.replace(i ,"")
print("" == b)


# 3.Напишите программу, которая находит и печатает все повторяющиеся символы в заданной строке.
a = "1.Напишите программу, которая 2возвращает нов3ую строку,"
a1 = ""
a2 = []
for i in a:
    if i not in a1:
        a1 += i
    else:

        count = a.count(i)
        a2.append([i, count])
print(a1)
print(a2)

#2.Напишите программу, которая проверяет, является ли заданная строка панграммой (т.е. содержит все буквы алфавита).

# a ="Напишите программу, которая разделяет заданную строку на список подстрок по определенному разделителю."
a = "абвуфхцчшщабвггдеёжзийклмнопрстуфхцчшщабвгдеёжзийклмноъыьэюя"
b = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
a1 = True
for i in b:
    if i not in a:
        a1 = False
print(a1)

# for i in a:
#    if i.lower in [а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я]:
#        a1 += i

print(a1)


# 1.Напишите программу, которая удаляет все пробелы из заданной строки.
a ="Напишите программу, которая разделяет заданную строку на список подстрок по определенному разделителю."
a1 = ""
for i in a:
    if i != " ":
        a1 += i

print(a1)

#@RVMartirosov

# 4.Напишите программу, которая разделяет заданную строку на список подстрок по определенному разделителю.
a ="Напишите программу, которая разделяет заданную строку на список подстрок по определенному разделителю."
a = a.split(" п")
print(a)

#3.Напишите программу, которая находит и печатает все цифры в заданной строке.
a = "1.Напишите программу, которая 2возвращает нов3ую строку,"
a1 = ""
a2 = ""
for i in a:
    if i.isdigit():
        a1 += i

    if i.isnumeric():
        a2 += i
print(a1)
print(a2)


#2.Напишите программу, которая проверяет, состоит ли заданная строка только из букв верхнего регистра.
a = "ERRORa"
print(a == a.upper())

#1.Напишите программу, которая возвращает новую строку,
# полученную из заданной строки, в которой удалены все символы пунктуации.
a = "1.Напишите программу, которая возвращает новую строку,"
a1 = ""
for i in a:
    if i == " " or i.isalpha():
        a1 += i
print(a1)



# Катерина

#1.Напишите программу, которая находит и печатает все слова в заданной строке.
a = "Напишите 2программу, Kоторая 3возвращает новую строкуu"
b = ""
for i in a:
    if not i.isdigit():
        b += i
print(b)




#4.Напишите программу, которая заменяет все вхождения одной подстроки на другую в заданной строке.
a = "Напишите программу, Kоторая возвращает новую строку"
b = "Напишите"
c = "Kоторая"
print(a.replace(b, c))



#2.Напишите программу, которая проверяет, заканчивается ли заданная строка определенной подстрокой.
a = "Напишите программу, Kоторая возвращает новую строку"
print(a.endswith("року"))

#3.Напишите программу, которая проверяет, содержит ли заданная строка только цифры.
a ="3233"
print(a.isdigit())


# @Denwork21
# 4.Напишите программу, которая проверяет, начинается ли заданная строка с определенной подстроки.
a = "Напишите программу, Kоторая возвращает новую строку"
print(a.startswith("Напиш"))
print("Напиш" in a[:7])

# 3.Напишите программу, которая возвращает новую строку,
# полученную из заданной строки, в которой все слова записаны с заглавной буквы.
a = "Напишите программу, Kоторая возвращает новую строку"
a = a.title()
print(a)



#2.Напишите программу, которая возвращает новую строку,
# полученную из заданной строки, в которой все слова записаны задом наперед.
a = "Напишите программу, Kоторая возвращает новую строку"
b = a.split()
c = []
for i in b:
    c.append(i[::-1])
d = " ".join(c)
print(d)



# 1.Напишите программу, которая возвращает новую строку, полученную из заданной строки,
# в которой все символы в верхнем регистре заменены на символы в нижнем регистре.

a = "Напишите программу, Kоторая возвращает новую строку"
a = a.lower()
print(a)