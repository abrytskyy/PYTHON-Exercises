#5.Проверьте, является ли список множеством (все элементы уникальны).
a = [3, 2, 3, 4, 1]
b = True

for i in a:
    a.remove(i)

    if i in a:
        b = False
        break
print(b)



a = [3, 2, 5, 4]
a_set = set(a)
print(len(a)==len(a_set))

# 4.Создайте список чисел и заполните им новый список,
# в котором каждый элемент старого возводится в квадрат,
# если он чётный, или в куб, если он нечётный.
a = [3, 2, 5, 4]
b = list()
for i in a:
    if i % 2 == 0:
        b.append(i**2)
    else:
        b.append(i**3)
print(b)

#3.Определите, является ли список возрастающей последовательностью чисел.
a = [1, 2, 5, 4]
b = True
for i in range(len(a)-1):
    if a[i+1] < a[i]:
        b = False
        break
print(b)



#2.Создайте  два списка и получите новый список, содержащий только общие элементы.
list1 = ["a",5,"c"]
list2 = [3, 5 , "a", "d"]
for i in list2:
    if i not in list1:
        list1.append(i)
print(list1)

list1 = ["a",5,"c"]
list2 = [3, 5 , "a", "d"]
list3 = list1 + list2
set3 = set(list3)
list3 = list(set3)

print(list3)

# 1.Извлеките все числа из списка строк и сохраните их в новом списке.
a = ["Извлеките1", "все", "2числа"]
b = []
c = ""
for i in a:
    for j in i:
        if j.isdigit():
            b.append(j)
print(b)