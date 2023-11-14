###Артём
#1. Напишите программу, которая находит студента с наибольшим именем по алфавиту, у которого возраст находится в определенном диапазоне.
#2. Напишите программу, которая находит студента с наименьшим именем по алфавиту, у которого возраст находится в определенном диапазоне.
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 25},
    {"name": "Eve", "age": 21},

]
a = 18
b = 22
max_length_name = max(students, key=lambda student: a <=student["age"] <= b)
min_length_name = min(students, key=lambda student: a <=student["age"] <= b)
print(max_length_name)
print(min_length_name)