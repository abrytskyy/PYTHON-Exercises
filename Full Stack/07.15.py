
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [word for word in dictionary]
print(words)    # ['red', 'blue', 'green']

numbers = [n for n in range(10)]
print(numbers)

numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = [n for n in numbers if n > 0]

print(positive_numbers)


numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = []
for n in numbers:
    if n > 0:
        positive_numbers.append(n)

print(positive_numbers)