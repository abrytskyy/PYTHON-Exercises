#Создайте декоратор, который проверяет, что переданное значение аргумента положительное.

def decorator(func):
    def wrapper(*args, ** kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Argument must be positive")
            return func(*args, ** kwargs)
        return wrapper

@decorator
def add(a, b):
    return a + b


@decorator
def mult(a, b):
    return a * b

try:
    print(add(2, 5))
    print(add(-2, 5))
except ValueError as ex:
    print(ex)

print(mult(6, 8))
