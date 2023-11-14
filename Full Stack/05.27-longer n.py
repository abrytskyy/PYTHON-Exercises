n = 7
lst = ["Write", "a Python", "program", "to", "find"]
lst1 = []
for i in lst:
    if len(i) > n:
        lst1.append(i)
print(lst1)

n = 4
lst = ["Write", "a Python", "program", "to", "find"]
for i in lst:
    if len(i) > n:
        print(i)

