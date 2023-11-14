# Дан словарь с информацией о студентах и их предметах.
# Каждый студент представлен вложенным словарем с ключами "имя" и "предметы",
# где предметы являются вложенным словарем с ключами "название" и "оценка".
# Найдите студента с наибольшим средним баллом по предметам.

students = [
{
        "name": "Иван",
        "age": 20,
        "marks": [5, 4, 4, 3, 5]
    },
    {
        "name": "Мария",
        "age": 21,
        "marks": [3, 4, 5, 4, 5]
    },
    {
        "name": "Петр",
        "age": 19,
        "marks": [5, 5, 5, 4, 4]
    }
]

def calculate_max_scores(data):
    dict_out = get_average_scores(students)
    max_score = 0
    name = 0
    dict_max = {}
    for key, val in dict_out.items():
        if val > max_score:
            max_score = val
            name = key
    dict_max[name] = max_score
    return dict_max




def get_average_scores(students):
    dict_out = {}

    for student in students:
        name = student["name"]
        dict_out[name] = calculate_average_scores(student["marks"])
    return dict_out


def calculate_average_scores(lst):
    sum = 0
    for element in lst:
        sum += element
    return sum / len(lst)






print(get_average_scores(students))

print(calculate_max_scores(get_average_scores(students)))

#print(max([2,2,2]))