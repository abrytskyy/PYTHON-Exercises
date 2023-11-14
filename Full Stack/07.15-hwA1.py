

print(list(range(1, 10)))
a = [0, 1]
a += [a[i-2] + a[i-1] for i in range(2,10)]
print(a)
