students = [
    {"name": "Алексей", "age": 18, "class": 10},
    {"name": "Екатерина", "age": 17, "class": 11},
    {"name": "Михаил", "age": 16, "class": 9}
]
# 1. Напишите программу, которая находит студента с наибольшим именем по алфавиту, у которого возраст находится в определенном диапазоне.
max = "a"
best = {}
for student in students:
    if student["age"] > 15:
        if student["name"][0].lower() > max:
            max = student["name"][0].lower()
            best = student
print(best)

# 2. Напишите программу, которая находит студента с наименьшим именем по алфавиту, у которого возраст находится в определенном диапазоне.
min = "ь"
best = {}
for student in students:
    if student["age"] > 15:
        if student["name"][0].lower() < min:
            min = student["name"][0].lower()
            lowest = student
print(lowest)