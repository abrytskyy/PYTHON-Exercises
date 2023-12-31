#1.Write a program that finds the second smallest number in the list
list1 = [1, 2, -3, 6, 2, 3]
list1.remove(min(list1))
print(min(list1))

#if min repeating:
list1 = [1, 2, -3, 6, 2, -3]
list2 = [el for el in list1 if el != min(list1)]
print(min(list2))

#without list comprehention
list1 = [1, 2, -3, 6, 2, -3]
list2 = []
for el in list1:
    if el > min(list1):
        list2.append(el)
print(min(list2))


#2.Write a program that finds the difference between the sum of elements at even positions and the sum of elements at odd positions in a list
numbers = [5, 2, 8, 1, 3, 7, 1, 2]
numbers_even_positions = []
numbers_odd_positions = []
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers_even_positions.append(numbers[i])
    else:
        numbers_odd_positions.append(numbers[i])
difference = sum(numbers_even_positions) - sum(numbers_odd_positions)
print(difference)

#with comprehention:
numbers = [5, 2, 8, 1, 3, 7, 1, 2]
sum_even = sum(numbers[i] for i in range(len(numbers)) if i % 2 == 0)
sum_odd = sum(numbers[i] for i in range(len(numbers)) if i % 2 != 0)
print(sum_even - sum_odd)

# if positions starts telling from 1, not from 0:
numbers = [5, 2, 8, 1, 3, 7, 1, 2]
numbers_even_positions = []
numbers_odd_positions = []
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers_odd_positions.append(numbers[i])
    else:
        numbers_even_positions.append(numbers[i])
difference = sum(numbers_even_positions) - sum(numbers_odd_positions)
print(difference)


# 3.Write a program that finds the sum of elements in a list located between two specified indexes

list1 = [1, 2, -3, 6, 2, -3]
def sum_between_indexes(lst, first, second):
    sum1 = 0
    for i in range(first,second+1):
        sum1+=list1[i]
    return sum1
print(sum_between_indexes(list1, 2, 4))


# 4.Write a program that finds the number of elements in a list that are greater than the average value of all elements
list1 = [1, 2, -3, 6, 2, -3]
average = sum(list1)/len(list1)
count = 0
for l in list1:
    if l > average:
        count += 1
print(average)
print(count)

#with comprehention:
list1 = [1, 2, -3, 6, 2, -3]
average = sum(list1)/len(list1)
count = len([1 for el in list1 if el > average])
print(count)


# 5.Write a program that finds the sum of elements at odd positions but only if the element is greater than the previous one.
my_list = [1, 3, 2, 4, 6, 2, 8, 5]
def sum_odd_position_if_greater(lst):
    sum_odd = 0
    for i in range(1, len(lst),2):
        if lst[i] > lst[i-1]:
            sum_odd += lst[i]
            return sum_odd
print(sum_odd_position_if_greater(my_list))
