

#Проверить, все ли элементы в списке положительные числа, используя all.
list1 = [1, 2, -3, 4, 5]
print(all(l > 0 for l in list1))
###Artem
#Проверить, есть ли хотя бы одна строка с длиной более 10 символов в списке, используя any.
array = ["desiat", "devanosto", "kvadratiljon"]
print(any(len(a) > 10 for a in array))

#Проверить, есть ли хотя бы одно отрицательное число в списке, используя any
list1 = [1, 2, -3, 4, 5]
print(any(l < 0 for l in list1))


# Задача на сложение элементов из двух списков, используя функцию zip
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
result = [x + y for x, y in zip(list1, list2)]
print(result)
#Найти произведение элементов из двух списков, объединенных через zip.
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
result = [x * y for x, y in zip(list1, list2)]
print(result)
#Создать словарь из двух списков: один список ключей, другой - значений, используя zip
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
result = [x * y for x, y in zip(list1, list2)]
print(result)
