for number in range(1, 101):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

number = int(input("Input any number:"))
if number <= 0:
  print("You dialed a wrong number. Number should be more than 0. Try again")
else:

  if number % 15 == 0:
    number = str(number)
    print(number + " FizzBuzz")
  elif number % 3 == 0:
    number = str(number)
    print(number + " Fizz")
  elif number % 5 == 0:
    number = str(number)
    print(number + " Buzz")
  else:
    print(number)