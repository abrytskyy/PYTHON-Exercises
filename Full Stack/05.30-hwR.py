# 5.Создайте функцию, список строк и получите новый список,
# содержащий только строки, которые содержат только уникальные символы.
a = "Создайте"
print(set(a))
print(len(a) == len(set(a)))

#a = ["Создайте", "барон", "список", "строк", "и", "получите", "набор"]
#b = []
#for i in a:
#    for j in a:
#        if i != j and len(i)== len(set(j)):
#            b.append(j)
#print(b)

#4.Посчитайте сумму цифр каждого числа в списке и верните новый список с суммами.
a = [34, "234", 15, 2]
b = []

for i in a:
    i  = str(i)
    sum = 0
    for j in i:
        j = int(j)
        sum += j
    b.append(sum)
print(b)



# 3.Проверьте, является ли список анаграммами
# (словами, составленными из одних и тех же символов, но в разном порядке).

a = ["Создайте", "барон", "список", "строк", "и", "получите", "набор", "крост"]
b =[]
for i in a:
    for j in a:
        if i != j and sorted(i) == sorted(j):
            b.append(j)
print(b)


#for i in a:
 #   for j in i:
   #     if j in
   # print(i)


#2.Создайте  список строк и и получите новый список, в котором каждая строка записана задом наперёд
a = ["Создайте", "список", "строк", "и", "получите"]
b = list()
for i in a:
    i = i[::-1]
    b.append(i)
print(b)


# 1.Найдите все пары чисел из списка, сумма которых равна заданному числу, и верните их в новом списке пар.
a = [3, 2, 5, 5, 4, 1]
a_new =[]
b = int(input("Input number: "))
a0 = a[0]
for i in range(1,len(a)):
    if a[i-1] + a[i] == b:
        a_new.append([a[i-1], a[i]])
print(a_new)
