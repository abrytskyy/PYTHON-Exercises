#Find the position of a character in a string (recursively).
def factorial(number):
    multiply = 1
    for i in range(1, number+1):
        multiply *= i
    return multiply
print(factorial(5))

def factorial_rec(number):
    if number == 1:
        return 1
    return factorial_rec(num-1)

#Check if a string is a palindrome (recursively).


#Calculate the sum of elements in an array (recursively).

#Calculate the product of elements in an array (recursively).

#Calculate the factorial of a number.
