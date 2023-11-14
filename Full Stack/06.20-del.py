

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) -1, -1, -1):
    if numbers[i] < 5:
        del numbers[i]
print(numbers)