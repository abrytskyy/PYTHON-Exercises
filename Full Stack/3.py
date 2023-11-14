# Напишите функцию, которая принимает список чисел и возвращает список, содержащий только четные числа.
result = [2, 4, 6,9,8,11,2, 5]
def even_number(list1):
    result1 = []
    for element in list1:
        if element % 2 == 0:
            result1.append(element)
    return result1
print(even_number(result))





