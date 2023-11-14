###Ярослав
#Напишите программу, которая сортирует кортеж по возрастанию.
print(tuple(sorted(list((3, 2, 5)))))

#Напишите программу, которая меняет порядок элементов в кортеже на обратный.
def reverse_order(a):
    return (a)[::-1], a + (2, 3)
print(reverse_order((1, 5, 6)))

#Найдите сумму элементов, присутствующих в нечетном количестве, в нескольких множествах.
set1 = {1, 2}
set2 = {1, 5, 6}
set3 = {1, 6, 8}
dict1 = {}
def amount_of_repetitions(a,b,c):
    all_sets = list(a) + list(b) + list(c)
    for i in all_sets:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1
def sum_of_odd_occurencies(a,b,c):
    return sum(k for k,v in (amount_of_repetitions(a,b,c)).items() if v % 2 == 1)

print(sum_of_odd_occurencies(set1,set2,set3))



#Найдите симметрическую разность нескольких множеств.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

symmetric_difference3 = (set1 ^ set2) ^ set3

symmetric_difference2 = set1 ^ set2
print(symmetric_difference2)
print(symmetric_difference3)

#Проверьте, содержит ли множество все элементы из нескольких списков.
set1 = {1, 2}
set2 = {5, 6}
set3 = {7, 8, 9, 10}

seta = {1, 2, 5, 6}
print(seta.issuperset(set1) and seta.issuperset(set2))