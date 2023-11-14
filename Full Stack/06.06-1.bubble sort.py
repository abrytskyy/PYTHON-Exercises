a = 5
b = 6

print(a, b)
c = a
a = b
b = c
print(a, b)

numbers = [4, 3, 2, 5]
for i in range(len(numbers) - 1): # par menshe na 1
    print(i)
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print(numbers)

a = 5
b = 6

print(a, b)
a,b = b,a
print(a, b)


numbers = [4, 3, 2, 5]
for i in range(len(numbers) - 1): # par menshe na 1
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j], numbers[j + 1]
print(numbers)
