

a = [1,2,5,3,4]
sum = 0
smallest = 10000
for item in a:
    sum += item
    if item < smallest:
        smallest = item
print(sum,smallest)