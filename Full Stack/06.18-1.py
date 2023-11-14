#1. Напишите функцию, которая принимает строку и возвращает
# новую строку, содержащую только символы, которые не являются цифрами.
result = "1новую строку, содержащую только символы"
def no_digit(a):
    result1 = ""
    list1 = []
    for i in a:
        if not i.isdigit():
            result1 += i
    return result1
print(no_digit(result))
