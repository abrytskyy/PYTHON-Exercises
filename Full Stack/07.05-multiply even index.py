# Напишите программу, которая находит произведение элементов кортежа, находящихся на четных индексах.

numbers = 2, 3, 5, 10, "6", 3.5, 7.5
def multiply_even_elements(set):
    multiply = 1

    for i in range(0, len(set)):

        if i % 2 == 0 and type(set[i]) in {int,float}:
            multiply *= set[i]
    return multiply
print(multiply_even_elements(numbers))