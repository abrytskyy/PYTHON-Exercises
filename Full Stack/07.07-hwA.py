# 6. Напишите программу, которая находит симметрическую разность двух множеств и возвращает список элементов,
# которые присутствуют только в одном из множеств.
tom_set = {"Tom", 37, "Google", "software developer"}
tom_set1 = {"Tom1", 37, "Google1", "software developer"}
tom_set_union = tom_set.union(tom_set1)
print(tom_set_union)

tom_set = {"Tom", 37, "Google", "software developer"}
tom_set1 = {"Tom1", 37, "Google1", "software developer"}
tom_set_union = tom_set.union(tom_set1)
tom_out = []
for i in tom_set_union:
    if i not in tom_out:
        tom_out.append(i)
print(tom_out)



#5. Напишите программу, которая удаляет все повторяющиеся элементы из списка, сохраняя только уникальные элементы.
lst = [2,3,2,5,3,5,3]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)

#4. Напишите программу, которая находит количество общих элементов в списке и множестве.
tom_list = ("Tom", 37, "Google", "software developer")
tom_set = {"Tom1", 37, "Google1", "software developer"}
n = 0
for i in tom_set:
    if i in tom_list:
        n += 1
print(n)

# 3. Напишите программу, которая удаляет первое вхождение определенного элемента из кортежа
tom = ("Tom", 37, "Google", "software developer")
tom = list(tom)
tom.remove(tom[0])
print(tom)
tom = tuple(tom)
print(tom)



tom = ("Tom", 37, "Google", "software developer")
tom = list(tom)
del tom[0]
tom = tuple(tom)
print(tom)

tom = ("Tom", 37, "Google", "software developer")
tom = list(tom)
tom.pop(0)
tom = tuple(tom)
print(tom)

# 2. Напишите программу, которая удаляет все элементы из кортежа
tom = ("Tom", 37, "Google", "software developer")
tom = list(tom)
tom.clear()
tom = tuple(tom)
print(tom)

tom = ("Tom", 37, "Google", "software developer")
tom = list(tom)
tom = ""
tom = tuple(tom)
print(tom)

#1. Напишите программу, которая меняет порядок элементов в кортеже на обратный.
tom = ("Tom", 37, "Google", "software developer")
tom_list = list(tom)
#print(tom_list)
reverse = tom_list[::-1]
reverse = tuple(reverse)
print(reverse)

