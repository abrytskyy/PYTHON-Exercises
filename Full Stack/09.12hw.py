#Разделить строку на подстроки по заданному разделителю.
def split_with(string, spliter):
    return string.split(spliter)
print(split_with('Разделить строку на подстроки', ' '))


#Заменить подстроку в строке на другую подстроку.
string1 = 'Заменить подстроку в строке'
substring1 = 'подстроку в строке'
substring2 = 'строку в подстроке'
string2 = string1.replace(substring1, substring2)
print(string2)

#Обрезать пробельные символы в начале и конце строки.
#3
string = '   Обрезать пробельные символы в начале и конце строки  '
string_list = string.split()
for s in string_list:
    print(s, end = ' ')
print()

#2
string = '   Обрезать пробельные символы в начале и конце строки  '
string_list = string.split()
string = ' '.join(string_list)
print(string)


#1
string = '   Обрезать пробельные символы в начале и конце строки  '
print(string.strip())

#Проверить, является ли строка палиндромом.
a = 'abba'
print(a == a[::-1])

#Подсчитать количество определенного символа в строке.
#3
string = 'Подсчитать количество определенного символа в строке'
symbol = 'о'
print(string.count(symbol))


#2
string = 'Подсчитать количество определенного символа в строке'
symbol = 'о'
print(sum([1 for s in string if s==symbol]))

#1
def number_of_symbol(string,symbol):
    n = 0
    for s in string:
        if s == symbol:
            n += 1
    return n
print(number_of_symbol('Подсчитать количество определенного символа в строке', 'о'))



#Сделать строку строчной (в нижнем регистре).
def lower_str(a):
    return a.lower()
print(lower_str('Сделать строку строчной'))


#Сделать строку заглавной (в верхнем регистре).
def upper_str(a):
    return a.upper()
print(upper_str("Сделать строку заглавной"))

#Определить длину строки.
#2
print(len("Определить длину строки."))

#1
def length(a):
    return len(a)
print(length("Определить длину строки."))

