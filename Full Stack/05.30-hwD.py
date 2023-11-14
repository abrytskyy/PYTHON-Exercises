#5.Создайте список всех комбинаций из двух списков [1, 2, 3] и [4, 5, 6],
# апример, [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]].

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = []
for i in list1:
    for j in list2:
        list3.append([i, j])
print(list3)


t = [1, 2, 3]
f = [4, 5, 6]

l = []
for j in range(len(t)):
    for i, k in enumerate(f):
        l.append([t[i], k])

print(l)


lists = [[i + j for i in range(2)] for j in range(3)]
print(lists)



list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = []
for i in range(len(list1)):
    for j in range(len(list2)):
        list3.extend([list1[i], list2[j]])
print(list3)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = []
for i in list1:
    for j in list2:
        list3.extend([i, j])
print(list3)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i)
        list3.append(j)
print(list3)




# 4.Создайте список, состоящий из первых букв каждого слова в строке.
s = "Создайте список, состоящий из первых букв каждого слова в строке"
l = []
for word in s.split():
    l.append(word[0])
print(l)



#3.Посчитайте количество уникальных элементов в списке.
list1 = [1,2,3,2,2,3,4,6]
number = 0
for i in list1:
    if list1.count(i) == 1:
        number += 1
print(number)

#2.Найдите наиболее часто встречающийся элемент в списке.

list1 = [1,2,3,2,2,3,4,6]
most_common = list1[0]
number = 1
for i in list1:
    if list1.count(i) > number:
        most_common = list1[i]
print(most_common)

from statistics import mode
list1 = [1,2,3,2,2,3,4,6]
most_common = mode(list1)
print(most_common)

#1.Найдите все простые числа от 1 до 100 и сохраните их в список.
list1 =[]
for i in range(1,101):
    list1.append(i)
print(list1)
