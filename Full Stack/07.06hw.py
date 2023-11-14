###Ярослав
#6. Напишите программу, которая находит элементы, которые встречаются более одного раза
#в списке, и добавляет их в множество.
my_list = [1, 2, 1, 4, 5]
set_a = {5, 2, 3, 4, 1}
list1 =[]
for i in my_list:
    if my_list.count(i) > 1 and i not in list1:
        list1.append(i)
print(list(set_a) + list1)

#5. Напишите программу, которая проверяет, является ли список и множество одинаковыми
# по содержимому.
my_list = [1, 2, 3, 4, 5]
set_a = {5, 2, 3, 4, 1}
print(my_list == list(set_a))


#4. Напишите программу, которая находит среднее значение всех элементов списка
# и добавляет его в множество.

my_list = [1, 2, 3, 4, 5, 6, 3]
set_a = {1, 2, 3, 4, 5}
avarage = round(sum(my_list)/len(my_list),1)
print(avarage)
list_a = list(set_a)
list_a.append(avarage)
print(set(list_a))


#3. Напишите программу, которая создает новый кортеж, содержащий только уникальные
# элементы из исходного кортежа.
tuple1 = (1,2,3,1,2)
print(tuple(set(tuple1)))

#2. Напишите программу, которая добавляет элемент на определенную позицию в кортеже.

tuple1 = (1,2,3,1,2)
position = 3
el = [9]
print(list(tuple1[:position])  + el + list(tuple1[position:]))


#1. Напишите программу, которая заменяет все вхождения определенного элемента в
tuple1 = (1,2,3,1,2)
elem = 2
second_elem = 7
new_tuple = tuple(second_elem if i == elem else i for i in tuple1)
print(new_tuple)


tuple1 = (1,2,3,1,2)
elem = 2
second_elem = 7
list1 = []
for i in tuple1:
    if i == elem:
        list1.append(second_elem)
    else:
        list1.append(i)
print(tuple(list1))


###Артём
#6. Напишите программу, которая находит симметрическую разность двух множеств
# и возвращает список элементов, которые присутствуют только в одном из множеств.
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
print(set(list(set_a-set_b) + list(set_b-set_a))) #1

print(set_a.symmetric_difference(set_b)) #2
print(set_a ^ set_b) #3





#5. Напишите программу, которая удаляет все повторяющиеся элементы из списка,
# сохраняя только уникальные элементы.
my_list = [1, 2, 3, 4, 5, 6, 3]
print(list(set(my_list)))

#4. Напишите программу, которая находит количество общих элементов в списке и множестве.
my_list = [1, 2, 3, 4, 5, 6, 3]
my_set = {3, 5, 3}
print(len(set(my_list)&my_set))

#3. Напишите программу, которая удаляет первое вхождение определенного
# элемента из кортежа
tuple1 = (1,2,3,1,2)
print(tuple1[1:])

#2. Напишите программу, которая удаляет все элементы из кортежа.
tuple1 = (1,2,3,1,2)
print(list(tuple1).clear())


#1. Напишите программу, которая меняет порядок элементов в кортеже на обратный.
tuple1 = (1,2,3,1,2)
print(tuple1[::-1])
###Катерина
#6. Напишите программу, которая удаляет все элементы из списка,
# которые также присутствуют в множестве.
my_list = [1, 2, 3, 4, 5, 6]
my_set = {3, 5}
def remove_common_elements(input_list, input_set):
    return [x for x in input_list if x not in input_set]
result_list = remove_common_elements(my_list, my_set)
print(result_list)


#5. Напишите программу, которая добавляет элемент в список только в том случае,
# если его нет в множестве.
a = [2, 4, 6]
b = 2
print([i for i in a if i != a])



list1 = [2, 4, 6]
element = 2
def add_elem(a, b):
    return [b for b in a if b not in a]
print(list1)

list1 = [2, 4, 6]
element = 2
if element not in list1:
        list1.append(element)
print(list1)

#4. Напишите программу, которая проверяет, является ли список подмножеством множества.
main_set = {1, 6, 3, 4, 5, 21, 7, 8, 9, 10}
sublist1 = [2, 4, 6]
sublist2 = [2, 11, 6]
def is_subset(main,sub):
    return set(sub).issubset(main)
print(is_subset(main_set, sublist1))

#3. #Напишите программу, которая разделяет кортеж на два, на основе определенного элемента.
def split_tuple(tuple, elem):
    index = tuple.index(elem)
    tuple1 = tuple[:index+1]
    tuple2 = tuple[index+1:]
    return tuple1, tuple2
print(split_tuple((1,2,3,4,5,6),3))

#2. Напишите программу, которая удаляет повторяющиеся элементы из кортежа.
tuple1 = (1,2,3,1,2)
print(tuple(set(tuple1)))


product_category = [500, 600]
print('We currently have %d available units of this item.' % product_category[1])

#1. Напишите программу, которая объединяет два кортежа, добавляя элементы из второго кортежа в конец первого.
set1 = (1, 2, 3,)
set2 = (3, 4, 5)
def sum_set(a, b):
    return a + b
print(sum_set(set1, set2))

###@Denwork21
#6. Напишите программу, которая находит разность двух множеств и возвращает список элементов, которые присутствуют только в одном из множеств.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
def difference_set(a, b):
    return (set1.difference(set2)),(set2.difference(set1))
print(difference_set(set1, set2))


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
def difference_set(a, b):
    return (set1 - set2),(set2-set1)
print(difference_set(set1, set2))



#5. Напишите программу, которая находит объединение двух множеств и возвращает список всех уникальных элементов.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
def union_set(a, b):
    return set1.union(set2)
print(union_set(set1, set2))

#4. Напишите программу, которая находит пересечение двух множеств и возвращает список с общими элементами.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
def intersection_set1(a, b):
    return tuple(list(a.intersection(b)))
print(intersection_set1(set1, set2))

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
def intersection_set(a, b):
    return set1 & set2
print(intersection_set(set1, set2))
    

#3. Напишите программу, которая меняет значение определенного элемента в кортеже.
tuple2 = (1, 7, 3, 4, 5)
index_to_remove = 2
new_elem = (10,)
def change_el_from_tuple(a, b, c):
    return a[:b] + c + a[b + 1:]
print(change_el_from_tuple(tuple2, index_to_remove, new_elem))

#2. Напишите программу, которая удаляет определенный элемент из кортежа.

tuple2 = (1, 7, 3, 4, 5)
index_to_remove = 2
def remove_el_from_tuple(a, b):
    return a[:b] + a[b + 1:]
print(remove_el_from_tuple(tuple2, index_to_remove))


print(tuple2[1:])



#1. Напишите программу, которая добавляет элемент в конец кортежа.
tuple1 = (1,2,3)

def new_element_in_tuple(a,b):
    return a + b
print(new_element_in_tuple(tuple1, (4,)))

