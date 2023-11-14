###Артём


# Напишите программу, которая находит произведение элементов кортежа, находящихся на четных индексах.
tuple4 = (1, 2, 3, 4, 5)
list4 = [i for i in tuple4 if i % 2 == 0]
mult = 1
for j in list4:
    mult *= j
print(mult)

#Напишите программу, которая суммирует элементы кортежа, игнорируя элементы с нечетными индексами.
tuple4 = (1, 2, 3, 4, 5)
print(sum([i for i in tuple4 if i % 2 == 0]))

list = []
sum = 0
for i in tuple4:
    if i % 2 == 0:
        sum += i
print(sum)



#Проверьте, является ли множество подмножеством каждого множества в списке множеств.
list_of_sets = [
    {1, 2, 3},
    {1, 2, 3},
    {1, 2, 3, 4},
    {1, 2}
]
target_set = {1, 2}
print(any(not target_set.issubset(s) for s in list_of_sets))


#Удалите все дубликаты из списка, используя множество.
#print(list(set([1, 2 ,3, 1])))

#Найдите количество общих элементов между несколькими множествами.
set1 = {1, 2, 5, 7}
set2 = {7, 4, 8, 1}
print(len(set1 & set2))

###Катерина
#Напишите программу, которая находит разность двух кортежей (элементы, которые есть в первом кортеже, но отсутствуют во втором).
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
print(set(tuple1) - set(tuple2))
print(set(tuple2) - set(tuple1))


#Напишите программу, которая находит пересечение двух кортежей (общие элементы).
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
print(set(tuple1) & set(tuple2))


#Проверьте, содержит ли множество все элементы другого множества.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 2, 1}
print(set1 == set2)

#Найдите разность симметричных множеств.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1^set2)

# Проверьте, содержат ли два множества одинаковые элементы.
set1 = {1, 2, 3}
set2 = {6, 4, 5}

print(any(element in set2 for element in set1))



set1 = {1, 2, 3}
set2 = {4, 6, 1}
for i in set1:
    if i in set2:
        print("Yes")
        break
else:
        print("No")



###@Denwork21

#Напишите программу, которая удаляет заданный элемент из кортежа.
tuple1 = (1, 2, 3)
tuple2 = []
element = tuple1[1]
for i in tuple1:
    if i != element:
        tuple2.append(i)
print(tuple(tuple2))




#Напишите программу, которая объединяет два кортежа в один.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2

print(combined_tuple)


#Проверьте, является ли множество подмножеством всех других множеств.
my_set = {1, 2, 3, 4, 5}
sub = {1, 7}
print(sub.issubset(my_set))

#Удалите случайный элемент из множества.
import random
my_set = {1, 2, 3, 4, 5}
my_set.remove(random.choice(tuple(my_set)))
print(my_set)

#Проверьте, является ли множество симметричным.
my_set = {1, 2, 3, 2, 1}
def symmetry_set(a):
    a = list(a)
    return a

print(symmetry_set(my_set))