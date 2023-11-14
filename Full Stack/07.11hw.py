###Ярослав
students = [
    {"name": "Emily", "age": 19, "class": "A"},
    {"name": "Daniel", "age": 20, "class": "C"},
    {"name": "Alex", "age": 18, "class": "A"},
    {"name": "Eva", "age": 17, "class": "B"},
    {"name": "Michael", "age": 16, "class": "A"},
    {"name": "Emily", "age": 19, "class": "B"},
    {"name": "Daniel", "age": 20, "class": "A"}
]

# Створимо словник, де ключем буде комбінація імені та віку, а значенням - список студентів з такою комбінацією.
student_dict = {}

for student in students:
    key = (student["name"], student["age"])
    if key in student_dict:
        student_dict[key].append(student)
    else:
        student_dict[key] = [student]

# Зараз в student_dict містяться комбінації імен та віку, де кожній комбінації відповідає список студентів.

# Знайдемо комбінації, де більше одного студента:
duplicate_combinations = {key: students for key, students in student_dict.items() if len(students) > 1}

# Виведемо студентів з однаковими іменами та віками:
for key, students in duplicate_combinations.items():
    print(f"Студенти з іменем '{key[0]}' та віком {key[1]}:")
    for student in students:
        print(f"Ім'я: {student['name']}, Вік: {student['age']}, Клас: {student['class']}")

#2. Напишите программу, которая находит студентов с одинаковыми именами и возрастами.
students = [
    {"name": "Emily", "age": 19, "class": "A"},
    {"name": "Daniel", "age": 20, "class": "C"},
    {"name": "Alex", "age": 18, "class": "A"},
    {"name": "Eva", "age": 17, "class": "B"},
    {"name": "Michael", "age": 16, "class": "A"},
    {"name": "Emily", "age": 19, "class": "B"},
    {"name": "Daniel", "age": 20, "class": "A"}
]
#output:
#students = {
#{"A":
# }



#1. Напишите программу, которая считает средний возраст студентов в каждом классе и выводит результат в виде словаря.
students = [
    {"name": "Alex", "age": 18, "class": "A"},
    {"name": "Eva", "age": 17, "class": "B"},
    {"name": "Michael", "age": 16, "class": "A"},
    {"name": "Emily", "age": 19, "class": "B"},
    {"name": "Daniel", "age": 20, "class": "A"}
]

# Створюємо словник для зберігання суми віку та кількості студентів в кожному класі
class_info = {}

for student in students:
    class_name = student["class"]
    age = student["age"]

    if class_name not in class_info:
        class_info[class_name] = {"sum_age": age, "count": 1}
    else:
        class_info[class_name]["sum_age"] += age
        class_info[class_name]["count"] += 1

# Створюємо словник результатів з середнім віком студентів
average_age_by_class = {}

for class_name, info in class_info.items():
    average_age = info["sum_age"] / info["count"]
    average_age_by_class[class_name] = average_age

print(average_age_by_class)

students = [
    {"name": "Alex", "age": 18, "class": "A"},
    {"name": "Eva", "age": 17, "class": "B"},
    {"name": "Michael", "age": 16, "class": "A"},
    {"name": "Emily", "age": 19, "class": "B"},
    {"name": "Daniel", "age": 20, "class": "A"}
]
students_new = {}
students_number = {}

for student in students:

    if student["class"] not in students_new:

        students_new[student["class"]] = student["age"]
        students_number[student["class"]] = 1

    else:
        students_new[student["class"]] += student["age"]
        students_number[student["class"]] += 1

print(students_new)
print(students_number)

print({k: students_new[k]/students_number[k] for k in students_number.keys()})







###Артём
#2. Напишите программу, которая находит студента с наименьшим именем по алфавиту, у которого возраст находится в
# определенном диапазоне.

#1. Напишите программу, которая находит студента с наибольшим именем по алфавиту,
# у которого возраст находится в определенном диапазоне.
students = [
    {"name": "Alex", "age": 18},
    {"name": "Eva", "age": 17},
    {"name": "Michael", "age": 16},
    {"name": "Emily", "age": 19},
    {"name": "Daniel", "age": 20}
]

min_age = 18
max_age = 25
students_by_age = [student for student in students if min_age <= student["age"] <= max_age]
print(students_by_age)
max_len_name = max(students_by_age, key=lambda student: len(student["name"]))
min_len_name = min(students_by_age, key=lambda student: len(student["name"]))
print(max_len_name)
print(min_len_name)

###Катерина
#2. Напишите программу, которая находит студента с наибольшим возрастом, у которого имя начинается с определенной буквы.
students = [
    {"name": "Alex", "age": 18},
    {"name": "Eva", "age": 17},
    {"name": "Michael", "age": 16},
    {"name": "Emily", "age": 19},
    {"name": "Daniel", "age": 20}
]

letter_to_check = "E"  # Задайте букву, з якою ви хочете порівняти імена

# Фільтруємо студентів за першою буквою імені
filtered_students = [student for student in students if student["name"].startswith(letter_to_check)]

# Знаходимо студента з максимальним віком серед відфільтрованих студентів
max_age_and_start_with = max(filtered_students, key=lambda student: student["age"])

print(max_age_and_start_with)

students = [
    {"name": "Alex", "age": 18},
    {"name": "Eva", "age": 17},
    {"name": "Michael", "age": 16},
    {"name": "Emily", "age": 19},
    {"name": "Daniel", "age": 20}
]
letter = "E"

max_age_and_start_with = max([student for student in students if student["name"].startswith(letter)], key=lambda student: student["age"])

print(max_age_and_start_with)

students = [
    {"name": "Alex", "age": 18},
    {"name": "Eva", "age": 17},
    {"name": "Michael", "age": 16},
    {"name": "Emily", "age": 19},
    {"name": "Daniel", "age": 20}
]
max_age_and_start_with = max(students, key=lambda student: student["age"])
print(max_age_and_start_with)

#1. Напишите программу, которая находит студента с наименьшим именем по длине в списке.

students = [
    {"name": "Алексей", "age": 18, "class": 10},
    {"name": "Екатерина", "age": 17, "class": 11},
    {"name": "Михаил", "age": 16, "class": 9}
]
min_length_name = min(students, key=lambda student: len(student["name"]))
print(min_length_name)


###@Denwork21
#2. Напишите программу, которая находит студента с наибольшим именем по длине в списке.
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 21},
    {"name": "Eve", "age": 23},
    {"name": "Frank", "age": 18}
]
max_length_name = max(students, key=lambda student: len(student["name"]))
print(max_length_name)


#1. Напишите программу, которая находит студентов с наибольшим и наименьшим возрастом в каждом классе и выводит результат в виде словаря.

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 21},
    {"name": "Eve", "age": 23},
    {"name": "Frank", "age": 18}
]
max_age = max(students, key=lambda student: student["age"])
print(max_age)

min_age = min(students, key=lambda student: student["age"])
print(min_age)


# max_height = max(students1, key=lambda student: student["height"])
# print(max_height)


# class_height_info = {}
# for s in students1:
#     class_name = s["class"]
#     height = s["height"]
#     if class_name in class_height_info:
#         class_height_info[class_name]["max_height"] = max(class_height_info[class_name]["max_height"], height)
#         class_height_info[class_name]["min_height"] = min(class_height_info[class_name]["min_height"], height)
#     else:
#         class_height_info[class_name] = {"max_height": height, "min_height": height}
#
#
# max_height = max(students1, key=lambda student: student["height"])
# print(max_height)

