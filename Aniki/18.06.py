#1. Людина вводить яку завгодно кількість сантиметрів.
# Программа повинна знайти скільки там повних метрів. Наприклад: 486 см = 4 м.

def count(a):
    b = int(a/100)
    return b
print(count(436))