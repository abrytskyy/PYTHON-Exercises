###@Rinkame
#Напишите функцию, которая принимает список чисел и возвращает True,
# если все числа в списке уникальны (не повторяются), и False в противном случае.

def unique_numbers(a):
    a1 = []
    for i in a:
        if i not in a1:
            a1.append(i)
        else:
            return False

    if a == a1:
        return True
print(unique_numbers([1, 1, 2, 3, 4]))


#Напишите функцию, которая принимает строку и возвращает новую строку, в которой удалены все символы, не являющиеся буквами или цифрами.
def not_number_not_digit(a):
    a1 = ""
    for i in a:
        if not i.isdigit() and not i.isalpha():
            a1 += i
    return a1
print(not_number_not_digit("a baba 24 ??? #gal33 ="))

### @RVMartirosov
#Напишите функцию, которая принимает список строк и возвращает новый список, содержащий только уникальные строки в алфавитном порядке.
list_str = ["art", "open", "book", "open"]
def unique_str(a):
    a1 =[]
    a.sort()
    for i in a:
        if i not in a1:
            a1.append(i)
    return a1
print(unique_str(list_str))


#Напишите функцию, которая принимает число и возвращает новое число, в котором порядок цифр обратный исходному числу.

def rev(a):
    a1 = []

    for i in a:
        i = str(i)
        i = i[::-1]
        i = int(i)
        a1.append(i)
    return a1
print(rev([123, 34, 56]))

dig = str(input("input digits devided by space: "))
def rev(a):
    dig1 = []

    a = a.split()
    for i in a:
        i = i[::-1]
        dig1.append(i)
    return dig1
print(rev(dig))

###Артём
#Напишите функцию, которая принимает строку и возвращает новую строку,
# в которой каждое слово начинается с заглавной буквы, а остальные буквы в слове в нижнем регистре.
st = "апишите функцию"
def title_each_world(a):
    a1 = ""
    b1 = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j != 0:
                a1 += a[i][j]

            else:
                a1 += a[i][j].upper()


    b1.append(a1)
    return b1

print(title_each_world(st))


#Напишите функцию, которая принимает список чисел и возвращает сумму всех
# положительных чисел и произведение всех отрицательных чисел.
list1 = [2, 8, -2, -5, 4, 7]

def sum_plus_mult_minus(a):
    sum = 0
    mult = 1
    for i in a:
        if i > 0:
            sum += i
        elif i < 0:
            mult *= i
    return sum, mult
print(sum_plus_mult_minus(list1))

### Катерина
#Напишите функцию, которая принимает строку и возвращает новую строку, в которой все слова записаны в обратном порядке.
st = "Напишите функцию"
def rev(a):
    a = a[::-1]
    return a
print(rev(st))

# Напишите функцию, которая принимает два списка чисел и возвращает список,
# содержащий элементы, которые присутствуют только в одном из списков, но не в обоих.
list1 = [2, 4, 7]
list2 = [4, 7, 9]
def combine(a, b):
    return set(a + b)
print(combine(list1,list2))


###@Denwork21

#Напишите функцию, которая принимает строку и возвращает новую строку, в которой все символы будут в случайном порядке.
import random
st = "Напишите функцию"
def shufle (a):
    a = "".join(random.sample(a, len(a)))
    return a
print(shufle(st))
#Напишите функцию, которая принимает список чисел и возвращает список, содержащий только числа, которые делятся на 3 и 5 одновременно.

list1 = [15, 10, 9, 45]
list2 = list()
def dev_3_5(a):
    for i in a:
        if i % 3 == 0 and i % 5 == 0:
            list2.append(i)
    return list2
print(dev_3_5(list1))
