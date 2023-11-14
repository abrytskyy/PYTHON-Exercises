# 4.Напишите программу, которая удаляет все дубликаты из списка.

lst = [2,3,2,5,3]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)

# 3.Напишите программу, которая находит индекс определенного элемента в списке.
element = int(input("innput indeks av element"))
lst = [2,-3,2,-5,3]
print(lst[element])

#2.Напишите программу, которая находит количество отрицательных чисел в списке.
lst = [2,-3,2,-5,3]
n = 0
for i in lst:
    if i < 0:
        n += 1
print(n)

# 1.Напишите программу, которая выводит только уникальные элементы списка.
lst = [2,3,2,5,3]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)