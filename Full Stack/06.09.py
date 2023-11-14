a = [[1, 2, 13, 2, 5], [9, 8, 12, 4, 5]]
for i in a:
    print(max(i), min(i))



a = [[1, 2, 13, 2, 5], [9, 8, 12, 4, 5]]
for i in range(len(a)):
    for j in range(len(a[i])):



a = [[1, 2, 13, 2, 5], [9, 8, 12, 4, 5]]
maxi, maxj = 0, 0
mini, minj = 0, 0

for i in range(len(a)):
    max = a[i][0]
    min = a[i][0]
    for j in range(len(a[i])):
        if a[i][j] > max:
            max = a[i][j]
            maxi, maxj = i, j
        if a[i][j] < min:
            min = a[i][j]
            mini, minj = i, j
    a[maxi][maxj], a[mini][minj] = a[mini][minj], a[maxi][maxj]

print(a)