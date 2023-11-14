###@Rinkame


#3. Напишите программу, которая принимает два списка чисел и выводит на экран только общие элементы, умноженные на 2.
list1 = [2, 4, 7]
list2 = [4, 7, 9]
list_common = []
def combine_common(l1, l2):
    for i in l1:
        if i in l1 and i in l2:
            list_common.append(i*2)
    return list_common
print (combine_common(list1, list2))

# 2. Напишите функцию, которая принимает список чисел и возвращает новый список,
# содержащий элементы, которые являются суммой предыдущих двух элементов в исходном списке.



#1. Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий только элементы,
# которые делятся на все числа из исходного списка.


###@RVMartirosov
#3. Напишите программу, которая принимает список слов и выводит на экран только те слова, которые содержат две одинаковые соседние буквы.
def neighbour_letter(a):
    a1 = []
    for i in range(len(a)):
        for j in range(len(a[i])-1):
            if a [i][j] == a[i][j+1]:
                a1.append(a[i])
    return a1
print(neighbour_letter(["arttem", "arta", "art"]))

#2. Напишите программу, которая принимает строку и выводит на экран только те слова,
# которые начинаются и заканчиваются на одну и ту же букву.
def start_finish_same_letter(a):
    a1 = []
    for i in a:
        if i[0] == i[-1]:
            a1.append(i)
    return a1
print(start_finish_same_letter(["artem", "arta"]))


#1. Напишите программу, которая принимает список чисел и выводит на экран только числа, которые являются простыми
def simple(a):
    b = True
    for i in a:
        for j in range(i):
            if j % i[j] != 0 and j == i and j == 1:
                b = False
                break
    return b
print(simple([]))
###Артём
#3. Напишите функцию, которая принимает список строк и возвращает новый список,
# содержащий только те строки, которые имеют длину больше 5 символов.
def more5(a):
    a2 = []
    for i in a:
        if len(i) > 5:
            a2.append(i)
    return a2
print(more5(["artemen", "arte", "arsenij"]))


#2. Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
def count_letter(a):
    m = 0
    n = 0
    for i in a:
        for j in i:
            if j.isalpha():
                if j.istitle():
                    n += 1
                else:
                    m += 1
    return n, m
print(count_letter(["Artem", "MyroN"]))


#1. Напишите функцию, которая принимает строку и возвращает новую строку, содержащую только символы, которые не являются цифрами.
def not_digit(a):
    a1 = []
    for i in a:
        if type(i)== str and not i.isdigit():
            a1.append(i)
    return a1
print(not_digit(["234", "234a", "no", True]))


###Катерина
# 3. Напишите программу, которая принимает список слов и выводит на экран только те слова, которые состоят только из цифр.
def just_digit(a):
    a1 = []
    for i in a:
        if type(i)== str and i.isdigit():
            a1.append(i)
    return a1
print(just_digit(["234", "234a", "no", True]))

#2. Напишите программу, которая принимает список слов и выводит на экран только те слова,
# которые имеют длину больше или равную 4 символам и заканчиваются на гласную букву.
def length_4_and_ends_vowel(a):
    a1 = []
    for i in a:
        if len(i) > 4 and i[-1] in "aouei":
            a1.append(i)
    return a1
print(length_4_and_ends_vowel(["priveta", "poka", "privet opat"]))

# 1. Напишите программу, которая принимает строку и подсчитывает количество буквенных символов в верхнем регистре.
def letter_upper(a):
    n = 0
    for i in a:
        if i.isalpha() and i.istitle():
            n += 1
    return n
print(letter_upper("Art ADFafg"))

###@Denwork21
#3. Напишите функцию, которая принимает список чисел и возвращает сумму всех положительных элементов.
def positive_elments(a):
    a1 = []
    for i in a:
        if i > 0:
            a1.append(i)
    return a1
def sum_positive():
    return sum(positive_elments([1, 2, -3, -1, 5]))
print(sum_positive())


    # 2. Напишите функцию, которая принимает строку и возвращает новую строку, содержащую только символы, которые встречаются нечетное количество раз.
def odd(a):
    a1 = ""
    for i in a:
        #print(a.count(i))
        if (i not in a1) and (a.count(i) % 2 == 1):
            a1 += i
    return a1
print(odd("asdaaaas"))



#1. Напишите программу, которая принимает список чисел и выводит на экран только числа, которые являются степенями числа 2.
def in_2(a):
    a2 = []
    for i in a:
        if i % 2 == 0:
            a2.append(i)
    return a2
print(in_2([2, 3, 4, 8, 15 ,64, 17]))

