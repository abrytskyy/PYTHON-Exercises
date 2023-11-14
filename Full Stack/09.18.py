#1. Создать пустой вложенный список.
list1 = [1, 2, 3]
list1.append([])
print(list1)
#2. Добавить элемент во вложенный список.
list1[3].append(2)
print(list1)
#3. Получить длину вложенного списка.
list1 = [1, 2, 3, [2]]
print(len(list1[3]))
#4. Извлечь элемент из вложенного списка по индексу.
lst = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9, 10],
       [-1, -2, -3]]
index_raw = 2
indec_col = 0
print(lst[index_raw][indec_col])
#5. Заменить элемент во вложенном списке по индексу.
lst[2][2] = 90
print(lst)

#13. Найти наибольший элемент во всех вложенных списках.
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [-1, -2, -3]]
max_list = []
for sublst in lst:
    max_list.append(max(sublst))
print(max(max_list))
#14. Найти наименьший элемент во всех вложенных списках.
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [-1, -2, -3]]
min_list = []
for sublst in lst:
    min_list.append(max(sublst))
print(max(max_list))

#15. Сортировать вложенный список по возрастанию.
lst_new = []
for sublst in lst:
    lst_new.append(sublst.sort())
print(lst_new)
