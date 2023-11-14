a = "abc_|¯|____|¯|__|¯¯¯"
b = ""
for n in range(1, len(a)):
    if a[n] != "|":
        print(int(a[n-1] == "|"), end="")
    # if a[n] == a[n+1]:
    #     b += "0"
    # else:
    #     b += "1"
#b = int(b)
print(b)

    #print(a[n])
    # if a[n] = m
    # m = a[n]
