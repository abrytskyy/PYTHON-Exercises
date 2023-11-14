#Создайте декоратор, который принимает параметр "retry_count" и повторяет выполнение функции заданное количество раз в случае возникновения исключения.

import functools
import time

def retry(retry_count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retry_count):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"An exception occurred: {str(e)}")
                    print("Retrying...")
                    time.sleep(1)  # Подождать перед повторной попыткой
            raise Exception(f"Function {func.__name__} failed after {retry_count} retries.")
        return wrapper
    return decorator

# Пример использования декоратора
@retry(retry_count=3)
def example_function():
    import random
    if random.randint(0, 1):
        raise ValueError("Random error")
    return "Success"

result = example_function()
print(result)


#Создайте декоратор, который принимает список чисел и умножает результат функции на все элементы этого списка.
def multiply_result_by(numbers):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * (reduce(lambda x, y: x * y, numbers, 1))
        return wrapper
    return decorator

# Пример использования декоратора
@multiply_result_by([2, 3, 4])
def example_function(x, y):
    return x + y

result = example_function(5, 6)
print(result)  # Вывод: (5 + 6) * (2 * 3 * 4) = 270