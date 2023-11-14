#Remove all empty nested lists from the main list.
lst = [[1, 2], [], [3, 4], [], [], [5, 6], []]
#1
print([sublst for sublst in lst if sublst])
#2
print(list(filter(lambda sublst: sublst, lst)))


#Replace all negative numbers in all nested lists with zeros.
lst = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]
lst1 = [[0 if x < 0 else x for x in sublst] for sublst in lst]
print(lst1)


#Generate a new nested list consisting of random numbers.
import random
i = 3
j = 2
n = 10
list_new = [[random.randint(1,n) for _ in range(j)] for _ in range(i)]
print(list_new)


#Create a new nested list in which the strings were initially in reverse order.
lst = [["apple", "banana", "cherry"], ["date", "fig"], ["grape", "honeydew"]]
lst1 = [[x[::-1] for x in sublst] for sublst in lst]
print(lst1)


#Check if all nested lists have the same length.
lst = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]
result = all(len(sublst) == len(lst[0]) for sublst in lst)
print(result)


#Get a list of indices where a specific element is present in all nested lists.
lst = [[1, 2, 3], [4, 3, 6], [7, 8, 3]]
element = 3
lst1 = [(i,j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == element]
print(lst1)


#Create a list where all elements are unique and sorted in ascending order.
lst = [3, 2, 1, 2, 4, 3, 5, 6]
lst_new = sorted(set(lst))
print(lst_new)

