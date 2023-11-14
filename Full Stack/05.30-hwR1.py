a = ["Создайте", "барон", "список", "строк", "и", "получите", "набор"]
b =[]
for i in a:
    for j in a:
        if i != j and sorted(i) == sorted(j):
            b.append(j)
print(b)