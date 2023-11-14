s = "acbaaab"
s1 = []
s2 = []
for i in s:
    if i not in s2:
        s2.append(i)
        s1.append([i, s.count(i)])
print(sorted(s1))


s = "acbaaab"
s1 =[]
for i in s:
    if i not in s1:

        s1.append(i)
        s1.append(s.count(i))


print(s1)


s = input("input the word")
if len(s) < 3:
    print("Too shout")
elif s[-3:] == "ing":
    print(s + "ly")
else:
    print(s + "ing")


s = "prion"
print(s[-2:]*4)

s = "Empty string"
s1 = s[-1] + s[1:-1] + s[0]
print(s1)

s = "w"
if len(s) < 2:
    print("Empty string")
else:
    s1 = s[:2] + s[-2:]
    print(s1)


### suma diagonalej

#[0][4], [1][3], [2][2]
lst = [[1, 2, 3, 4, 0],
       [3, 5, 8, 2, 1],
       [9, 4, 1, 0, 2],
       [3, 5, 8, 2, 1],
       [1, 2, 3, 4, 5]]
sum1 = 0
sum2 = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if i + j == len(lst)-1:
            sum2 += lst[i][j]

        if i == j:
            sum1 += lst[i][j]

print(sum1,sum2)




color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
color1 = []
for i in range(len(color)):
    if i not in (0, 4, 5):
        color1.append(color[i])
print(color1)



del color[4:]
color.pop(0)
print(color)

### summa stolbcov
lst = [[1, 2, 3], [3, 5, 8], [9, 4, 1]]

for i in range(len(lst)):
    sum = 0
    for j in range(len(lst)):
        sum += lst [j][i]
    print(sum)

