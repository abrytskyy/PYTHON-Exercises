#Write program to get the largest number from a list
list1 = [1,2,7,3]
max = list1[0]
for element in range(len(list1)):
    if list1[element] > max:
        max = list1[element]
print(max)


list = [1,2,7,3]
max = 0
for element in list:
    if element > max:
        max = element
print(max)



#rint(max([1,2,7,3]))
