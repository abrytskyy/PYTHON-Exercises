a = [1, 2, 3],[4, 5, 6], [4, 3, 2]
a2 = []

for i in range(len(a)):
    sum = 0
    for j in range(len(a[i])):
        sum += a[j][i]
    a2.append(sum)
print(max(a2))


a = [[1, 2, 13, 13, 1], [9, 8, 12, 4, 5]]
for i in a:
    #max(i), min(i) = min(i), max(i)
    #print(i)

        index_max = i.index(max(i))
        index_min = i.index(min(i))
        i[index_max], i[index_min] = i[index_min], i[index_max]
print(a)

