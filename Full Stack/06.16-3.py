#3. Напишите программу, которая принимает список слов и
# выводит на экран только те слова, которые содержат две одинаковые соседние буквы.

result = "Наапишите функцию Напишите"
def two_same_letters(a):
    result1 = ""
    b = ""
    for i in a:
        if i == b:
            result1 += "*"
        else:
            result1 += i

        b = i
    return result1
print(two_same_letters(result))
