a = 2
b = 1.5
print("sum = ",a+b) if b > 2 else print("multiply", a*b)


people = ["Tom", "Sam", "Bob"]
tom,sam,bob = people
print(tom)


numbers = [1, 2, 3, 4, 5]
num = numbers
num.append(444)
print(id(numbers))
print(id(num))
print(numbers)
print(num)
num1 = list(numbers)
num2 = numbers.copy()
print(id(num1))
print(id(num2))