#1. Напишите функцию, которая принимает строку и возвращает новую строку,
# содержащую только символы, которые не являются цифрами
result = "1. Напишите функцию"
def not_digit(line1):
    result1 = ""
    for i in line1:
        if not i.isdigit():
            result1 += i
    return result1
print(not_digit(result))



