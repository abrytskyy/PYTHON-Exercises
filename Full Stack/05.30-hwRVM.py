# 3.Определите, есть ли в списке повторяющиеся подряд идущие элементы.
a = [3, 2, 5, 4]
for i in range(len(a)):
    print(i)



# 2.Найдите среднее арифметическое элементов списка, исключая минимальный и максимальный элементы.
a = [3, 2, 5, 4]
min = -1000
max = 1000
sum = 0
n = 0
for i in a:
    if i > min:
        min = i
    elif i < max:
        max = i
for i in a:
    if i != min and i != max:
        sum += i
        n += 1
avarage = sum / n
print(avarage)


a = [3, 2, 5, 4]
a.remove(min(a))
a.remove(max(a))
print(sum(a)/len(a))

# 1.Проверьте, содержит ли список повторяющиеся элементы.

a = [3, 2, 5, 4]
a_set = set(a)
print(len(a) != len(a_set))