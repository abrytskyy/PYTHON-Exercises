#Создайте список чисел и получите его итератор.
# Используйте итератор для получения следующего элемента списка.
numbers_list = [1, 2, 3, 4, 5]
iterator = iter(numbers_list)
for i in range(len(numbers_list)):
    print(next(iterator))


#Создайте словарь итератора, где ключами будут числа от 1 до N, а значениями - соответствующие итераторы.



# Создайте список из квадратов чисел от 1 до 10 с помощью выражения-генератора.
def list_a(a):
    return[i*i for i in range (1, a+1)]
print(list_a(10))
#Создайте множество из первых 10 четных чисел с помощью выражения-генератора.
def set_c(a):
    return {i for i in range(1,a+1) if i % 2 == 0}

print(sorted(set_c(20)))

#Создайте множество из квадратов чисел от 1 до 10 с помощью set comprehension.
def set_b(a):
    return {i*i for i in range(1,a+1) if i % 2 == 0}

print(sorted(set_b(10)))

#Создайте множество из первых 10 четных чисел с помощью set comprehension.
def set_a(a):
    return {i for i in range(1,a+1) if i % 2 == 0}

print(set_a(21))


#Создайте словарь, где ключами будут числа от 1 до 10, а значениями - их квадраты, с помощью dictionary comprehension.
def dict_b(a):

    return {i: i*i for i in range(1,a+1)}
print(dict_b(10))

#Создайте словарь, где ключами будут буквы из слова "привет",
# а значениями - их позиции в слове, с помощью dictionary comprehension.



privet = "привет"
def dict_a(a):

    return {a[i]: i for i in range(len((a)))}
print(dict_a(privet))


privet = "привет"
def dict_a(a):
    a1 = {}
    for i in range(len((a))):
        a1[a[i]]= i
    return a1
print(dict_a(privet))


