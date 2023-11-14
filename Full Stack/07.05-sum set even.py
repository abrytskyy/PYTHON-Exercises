#Напишите программу, которая суммирует элементы кортежа, игнорируя элементы с нечетными индексами.
numbers = 2, 3, 5, 10, "6", 3.5
def sum_even_elements(set):
    sum = 0
    for element in set:

        if type(element) == int and element % 2 == 0:
            sum += element
    return sum
print(sum_even_elements(numbers))