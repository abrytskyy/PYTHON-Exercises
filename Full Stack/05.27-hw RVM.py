# 4.Напишите программу, которая находит сумму всех элементов на нечетных позициях в списке.
a = [2, 3, 5, 3, 2, 1]
sum_odd = 0
for i in range(len(a)):
    if i % 2 == 1:
        sum_odd += a[i]

print(sum_odd)


# 3.Напишите программу, которая находит количество элементов в списке,
# которые больше среднего значения всех элементов.

a = [2, 3, 5, 3, 5, 3, 2]

sum = 0
n = 0
m = 0

for i in a:
    sum += i
    n += 1
av = round(sum / n, 2)
print(av)
a1 = []
for i in a:
    if i > av:
        m += 1
print(m)



#2.Напишите программу, которая находит сумму элементов списка, находящихся между двумя заданными индексами.
a = [2, 3, 5, 3, 5, 3, 2]
b = int(input("input index of 1 element: "))
c = int(input("input index of last element: "))

sum = 0

for i in range(b+1, c):
    sum += a[i]

print(sum)




# 1.Напишите программу, которая находит разность между суммой элементов на четных позициях
# и суммой элементов на нечетных позициях в списке
a = [2, 3, 5, 3, 2]
sum_even = 0
sum_odd = 0
for i in range(len(a)):
    if i % 2 == 0:
        sum_even += a[i]
    else:
        sum_odd += a[i]
print(sum_even)
print(sum_odd)
print(sum_even - sum_odd)

