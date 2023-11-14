#str
number = input("input number: ")
print(number[::-1])

#int
number = int(input("Input number: "))
number1 = number % 10
number //= 10
number2 = number % 10
number //= 10
print(number1, number2, number)         #1 option
print(f"{number1}{number2}{number}")    #2 option
print(number1, end="")                  #3 option
print(number2, end="")
print(number)


