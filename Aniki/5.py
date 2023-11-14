

def list_numbers(list1):
    min1 = list1[0]
    for i in list1:
        if i < min1:
            min1 = i

    return min1

print(list_numbers([2,3,7,1]))
