#Создайте функцию-счетчик, которая при каждом вызове увеличивает своё значение на единицу.
def add_1():
    count = 0
    def add():
        nonlocal count
        count += 1
        return count
    return add
print(add_1()())
print(add_1()())
print(add_1()())
print(add_1()())

def add_1():
    count = 0
    def add():
        nonlocal count
        count += 1
        return count
    return add
counter = add_1()
print(counter())
print(counter())
print(counter())

#Напишите функцию, которая возвращает другую функцию, возводящую число в заданную степень.
def power(x):
    def power_x(exponent):
        return x ** exponent
    return power_x

print(power(3)(4))

def power(x):
    def power_x(exponent):
        return x ** exponent
    return power_x
func=power(3)
print(func(4))

def power(x):
    def power_x(exponent):
        return x ** exponent
    return power_x(4)
print(power(3))

def power():
    def power_x(x, exponent):
        return x ** exponent
    return power_x(3, 4)
print(power())