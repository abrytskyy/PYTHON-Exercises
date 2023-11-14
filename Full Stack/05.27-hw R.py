# 4.Напишите программу, которая находит количество элементов в списке, которые являются палиндромами.
a = ["alla", "hallo", "radar", "roza"]
count = 0
for elem in a:
    if elem == elem[::-1]:
        count +=  1
print(count)

a = ["alla", "hallo", "radar", "roza"]
count = 0
for i in range(len(a)):
    if a[i] == a[i][::-1]:
        count += 1
print(count)





#3.Напишите программу, которая находит сумму элементов на нечетных позициях,
# но только если элемент больше предыдущего.
numbers = [2, -10, 3, 5, 3, 12, 1, -1, 10]
sum1 = 0
for i in range(len(numbers)):
    if i % 2 == 1 and numbers[i] > numbers[i-1]:
        sum1 += numbers[i]

print(sum1)

#2.Напишите программу, которая находит наибольшую разницу между двумя соседними элементами в списке.
numbers = [2, -10, 3, 5, 3, 2, 1, -1, 10]
dif_max = 0
for i in range(len(numbers)):
    dif = numbers[i]-numbers[i-1]
    if dif > dif_max:
        dif_max = dif
print(dif_max)



#1.Напишите программу, которая находит второе наименьшее число в списке
numbers = [2, -10, 3, 5, 3, 2, 1, -1, 10]
index = 0
min1 = min(numbers)
index = numbers.index(min1)

numbers.remove(min1)
min2 = min(numbers)
print(min1)
print(min2)
numbers.insert(index, min1)
print(numbers)


numbers = [2, -10, 3, 5, 3, 2, 1, -1, 10]
index = 0
min1 = min(numbers)
for i in range(len(numbers)):
    if numbers[i] == min1:
        index = i
print(index)
numbers.remove(min1)
min2 = min(numbers)
print(min1)
print(min2)
numbers.insert(index, min1)
print(numbers)


numbers = [10, 3, 5, 3, 2, 1, -1]
min = min(numbers)
print(min)


numbers = [10, 3, 5, 3, 2, 1, -1]
min = 1000
second_min = 1000
for element in numbers:
    if element < min:# 10 < 1000 ##3 < 10 ### 2 < 3 #### 1 < 2 ##### -1 < 1
        second_min = min#1000 ##10 ### 3 #### 2 ##### 1
        min = element#10 ## 3 ### 2 #### 1 ##### -1
    #elif element < min and element != second_min:
        #second_min = element
print(second_min)




a = [2, 3, 5, 3, 2, 1, -1]
min = 10
min1 = 10
for i in a:
    if i < min:
        min = i
print(min)

for i in a:
    if min1 > i > min:
        min1 = i
print(min1)

