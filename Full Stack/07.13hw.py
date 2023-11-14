###Ярослав
#Отсортировать список словарей по определенному ключу с использованием лямбда-функции.
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_data = sorted(data,key=lambda x: x["age"] == 30)
print(sorted_data)



#Найти сумму всех положительных чисел в заданном списке с использованием лямбда-функции.
number_list = [1, -2, 3, -4, 5, -6]
sum_positive = sum(filter(lambda x: x > 0, number_list))
print(sum_positive)

list_of_numbers = [2, -1, 4, -3]
sum_positive = lambda x: sum([i for i in x if i > 0])
print(sum_positive(list_of_numbers))


#Отфильтровать список строк, оставив только те, которые содержат только цифры, с использованием лямбда-функции.
string_list4 = ["apple4", "3nana", "acherry", "adate", "afig"]
is_digit = lambda x: [i for i in x if any(j.isdigit() for j in i)]
print(is_digit(string_list4))

#Напишите генератор, который выдает все возможные перестановки букв в слове.

def generate_permutations(word):
    if len(word) <= 1:
        yield word
    else:
        for perm in generate_permutations(word[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + word[0] + perm[i:]

# Example usage
word = "abc"
permutation_gen = generate_permutations(word)

for perm in permutation_gen:
    print(perm)

def permutations(word):
    if len(word) == 1:
        yield word
    else:
        for perm in permutations(word[1:]):
            for i in range(len(word)):
                yield perm[:i] + word[0] + perm[i:]

# Пример использования генератора
word = "abc"
permutation_gen = permutations(word)

for perm in permutation_gen:
    print(perm)

###Артём
#Проверить, все ли слова в заданном списке начинаются с определенной буквы с использованием лямбда-функции.
string_list3 = ["apple", "nana", "acherry", "adate", "afig"]
start_from = lambda x, y: all(word.startswith(y) for word in x)
print(start_from(string_list3, 'a'))

string_list3 = ["apple", "aana", "acherry", "adate", "afig"]
start_from = lambda x,y: all([i[0]==y for i in x])
print(start_from(string_list3,'a'))

#Отсортировать список строк в порядке убывания длины строк с использованием лямбда-функции.
string_list2 = ["apple", "banana", "cherry", "date", "fig"]
print(sorted(string_list2, key=lambda x: len(x),reverse=True ))

#Преобразовать список строк в список их длин с использованием лямбда-функции.
string_list1 = ["apple", "banana", "cherry", "date", "fig"]
lengths1 = lambda x: [len(i) for i in x]
print(lengths1(string_list1))


string_list = ["apple", "banana", "cherry", "date", "fig"]
lengths = list(map(lambda x: len(x), string_list))
print(lengths)
#Отсортировать список строк в порядке убывания длины строк с использованием лямбда-функции.

my_list = ["apple", "banana", "cherry", "date", "fig"]
sorted_list = sorted(my_list, key=lambda x: len(x), reverse=True)
print(sorted_list)

#Напишите генератор, который выдает все возможные перестановки трех цифр.
def three_digit_permutations():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for first_digit in digits:
        for second_digit in digits:
            for third_digit in digits:
                if (first_digit != second_digit) and (first_digit != third_digit) and (second_digit != third_digit):
                    yield (first_digit, second_digit, third_digit)

# Создаем генератор
perm_gen = three_digit_permutations()

# Выводим все возможные перестановки трех цифр
for perm in perm_gen:
    print(perm)


from itertools import permutations

def three_digit_permutations():
    for perm in permutations(range(10), 3):
        yield perm

# Создаем генератор
perm_gen = three_digit_permutations()

# Выводим все возможные перестановки трех цифр
for perm in perm_gen:
    print(perm)
#Напишите генератор, который выдает все пары чисел от 1 до 5.
print([(i,i+1) for i in range(1,5)])

#Напишите генератор, который выдает первые 10 чисел Фибоначчи.
def fibonacci_generator():
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1

# Создаём генератор
fib_gen = fibonacci_generator()

# Выводим первые 10 чисел Фибоначчи
for num in fib_gen:
    print(num)

###Катерина
#Посчитать сумму всех чисел в заданном списке с использованием лямбда-функции.
sum_list = lambda x: sum(x)
print(sum_list([1,2,3,4]))

#Получить список всех гласных букв в заданном слове с использованием лямбда-функции.
vowels = lambda x: [e for e in x if e in "aouei"]
print(vowels("baab"))
#Проверить, является ли заданное слово палиндромом с использованием лямбда-функции.
palindr = lambda x: x == x[::-1]
print(palindr("baab"))

#Напишите генератор, который выдает все квадраты чисел от 1 до 10.
print([i**2 for i in range(1,11)])

#Напишите генератор, который выдает все нечетные числа от 1 до 10.
print([i for i in range(1,11) if i % 2 == 1])

#Напишите генератор, который выдает все четные числа от 1 до 10.
print([i for i in range(1,11) if i % 2 == 0])

###@Denwork21
#Умножить каждый элемент списка на 2 с использованием лямбда-функции.
numbers = [1, 2, 3, 4, 5]
multiply_2 = list(map(lambda x:x*2,numbers))
print(multiply_2)

#Проверить, является ли заданное число четным с использованием лямбда-функции.
even_number = lambda x: x %2 == 0
print(even_number(11))

#Отсортировать список чисел в порядке возрастания с использованием лямбда-функции.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sor_numb = lambda x: sorted(x)
print(sor_numb(numbers))

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sorted(numbers, key=lambda i: i ))
#Напишите генератор, который выдает все подстроки заданного слова.

#Напишите генератор, который выдает все гласные буквы в заданном слове.
word = "Hello World"
print([w for w in word if w in "aouei"])
#Напишите генератор, который выдает все слова в заданном предложении.
sent = "Напишите генератор, который выдает все слова в заданном предложении"
print([w for w in sent.split(" ")])
