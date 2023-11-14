#Создайте лямбда-функцию, которая возвращает список строк, содержащих только символы, являющиеся согласными буквами.
a = ["abc", "aou"]
a1 = []

for i in a:
    str1 = ""
    for j in i:

        if j in "aouei":
            str1 += j
    if str1 == i:
        a1.append(i)
print(a1)

just_vowel_str_list = lambda a: [a1.append(i) for i in a if str1 ==i for j in i if j in "aoeiu"]
print (just_vowel_str_list(["123", "abc1"]))


#Создайте лямбда-функцию, которая возвращает список строк, содержащих только цифры.
just_digit_str_list = lambda a: ["".join(i) for i in a if i.isdigit()]
print (just_digit_str_list(["123", "abc1"]))

#Создайте лямбда-функцию, которая возвращает список строк в обратном порядке.
reverse_str_list = lambda a: ["".join(i[::-1]) for i in a]
print (reverse_str_list(["abc", "abc1"]))


reverse_str_list = lambda a: a[::-1]
print(reverse_str_list(["abc", "abc1"]))

#stroku

reverse_str_list = lambda a: a[::-1]
print(reverse_str_list("abc"))