def kratn(a):
    list1 = []
    n = 0
    for i in range(1,a+1):
        if a % i == 0:
            list1.append(i)
            n = n + 1
    #return list1
    if n > 2:
        return False
    else:
        return True

print(kratn(90))