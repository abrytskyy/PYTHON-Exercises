dict1 = {"art":43, "ivan":65}
def sum_dict_values(a):
    return sum(a.values())

print(sum_dict_values(dict1))

my_dict = {"apple":1, "banana": 2}
def keys(a):
    return list(a.keys())

print(keys(my_dict))

my_dict = {"apple":1, "banana": 2}
def keys(a):
    a1 = []
    for key in a.keys():
        a1.append(key)
    return a1

print(keys(my_dict))

my_dict = {"apple":1, "banana": 2}
def keys(a):
    for key in a.keys():
        print(key)
keys(my_dict)



#not prime
list1 = [4,3,9,17,5,24]
list2 = []
list3 = []
for i in list1:
    for j in range(2, i+1):
        if i != j and i % j == 0 and i not in list2:
            list2.append(i)
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)

#prime
list1 = [4,3,9,17,5,24]
list2 = []
for i in list1:
    for j in range(2, i+1):
        if i != j and i % j == 0 and i not in list2:
            list2.append(i)
print(list2)
