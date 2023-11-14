
list_numbers = [2,5,8,9,4,3]
def devided_by_all (list_numbers):
    list_numbers1 = []
    max1 = max(list_numbers)
    for i in list_numbers:
        if max1 % i == 0:
            list_numbers1.append(i)
    return list_numbers1
print(devided_by_all(list_numbers))



def str_more_5(a):
    a1 = []
    a = a.split()
    for i in a:
        if len(i) > 5:
            a1.append(i)
    return a1
print(str_more_5("a baba galamaga"))




