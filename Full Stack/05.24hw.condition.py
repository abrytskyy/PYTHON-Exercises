# Task 1 - Checking for Evenness of Three Numbers:
# Write a program that asks the user for three numbers and checks if all three numbers are even. Use the % operator to check each number for evenness. If all three numbers are even, display the message "All numbers are even"; otherwise, display "Not all numbers are even."

# Task 2 - Determining the Sign of a Number:
# Write a program that asks the user for a number and displays the message "Positive" if the number is greater than zero, "Negative" if the number is less than zero, or "Zero" if the number is equal to zero.

# Task 3 - Determining Leap Year:
# Write a program that asks the user for a year and displays the message "Leap year" if the year is a leap year or "Not a leap year" if it is not a leap year. A year is a leap year if it is divisible by 4 but not divisible by 100, except for years that are divisible by 400.



# Task 4 - Checking for Divisibility by the Sum of Two Other Numbers:
# Write a program that asks the user for three numbers and checks if the first number is divisible by the sum of the other two numbers without a remainder. Use the % operator to check divisibility. If the first number is divisible by the sum of the other two numbers, display the message "The first number is divisible by the sum of the other two numbers"; otherwise, display "The first number is not divisible by the sum of the other two numbers."
#
# Task 5 - Determining the Season:
# Write a program that asks the user for the number of a month (from 1 to 12) and displays the name of the corresponding season: "Winter," "Spring," "Summer," or "Autumn."
#
# Task 6 - Determining Age Group:
# Write a program that asks the user for their age and displays a message about their age group: "Childhood" (0-12 years), "Youth" (13-17 years), "Adult" (18-64 years), or "Elderly" (65+ years).



# Task 7 - Checking for Palindrome:
# Write a program that asks the user for a number and checks if it is a palindrome. A palindrome is a word, number, or phrase that reads the same forwards and backwards. Use the % operator to compare characters at the beginning and end of the word or phrase. If the word or phrase is a palindrome, display the message "It is a palindrome"; otherwise, display "It is not a palindrome."
#
# Task 8 - Determining Time of Day:
# Write a program that asks the user for the current hour (from 0 to 23) and displays a message about the time of day: "Morning," "Day," "Evening," or "Night."
#
# Task 9 - Admission Eligibility for Professional Course:
# Write a program to determine eligibility for admission to a professional course based on the following criteria:

# Mathematics score >= 65
# Physics score >= 55
# Chemistry score >= 50
# The total score in all three subjects >= 190, OR
# The total score in Mathematics and Physics >= 140
# The program should ask for scores in these subjects and then display whether the candidate is eligible or not.



# Task 10 - Checking for Divisibility by 4:
# Write a program that asks the user for a number and checks if it is divisible by 4 without a remainder. If the number is divisible by 4, display the message "The number is divisible by 4"; otherwise, display "The number is not divisible by 4."
#
# Task 11 - Determining Even or Odd:
# Write a program that asks the user for a number and displays the message "Even" if the number is even or "Odd" if the number is odd.
#
# Task 12 - Determining the Day of the Week:
# Write a program that asks the user for a number from 1 to 7 and displays the corresponding day of the week: 1 - "Monday," 2 - "Tuesday," and so on.


# Task 13 - Checking for Divisibility by Itself and the Sum of Its Digits:
# Write a program that asks the user for a number and checks whether it is divisible by both itself and the sum
# of its digits without a remainder. If the number satisfies both conditions, display the message "The number is
# divisible by itself and the sum of its digits"; otherwise, display "The number does not satisfy both conditions."

a = input("input digit: ")

b = int(a[0] + a[1])
if int(a) % b == 0:
    print("digit is divided by sum of own digits")
else:
    print("digit is not divided by sum of own digits")


# Task 14 - Determining the Winner in "Rock, Paper, Scissors" Game:
# Write a program that asks two players for their choices in the "Rock, Paper, Scissors" game
# (0 - rock, 1 - scissors, 2 - paper) and determines the winner. Rules: rock beats scissors, scissors beat paper,
# and paper beats rock. If both players make the same choice, the program should display the message "Draw"

#1
a = int(input("""Player 1. Type:
 0 - for stone,
 1 - for scissors,
 2 - for paper  
"""))
b = int(input("""Player 2. Type:
 0 - for stone,
 1 - for scissors,
 2 - for paper
"""))
if a == 0:
    if b == 0:
        print("Draw")
    elif b == 1:
        print("Player 1 won")
    else:
        print("Player 2 won")
elif a == 1:
    if b == 0:
        print("Player 2 won")
    elif b == 1:
        print("Draw")
    else:
        print("Player 1 won")
else:
    if b == 0:
        print("Player 1 won")
    elif b == 1:
        print("Player 2 won")
    else:
        print("Draw")

#2
# Prompt the first player for their choice (0 - rock, 1 - scissors, 2 - paper)
player1_choice = int(input("Player 1, enter your choice (0 - rock, 1 - scissors, 2 - paper): "))

# Prompt the second player for their choice (0 - rock, 1 - scissors, 2 - paper)
player2_choice = int(input("Player 2, enter your choice (0 - rock, 1 - scissors, 2 - paper): "))

# Define the rules for the game: rock beats scissors, scissors beat paper, and paper beats rock
# Check for a draw first
if player1_choice == player2_choice:
    result = "Draw"
elif (
    (player1_choice == 0 and player2_choice == 1) or
    (player1_choice == 1 and player2_choice == 2) or
    (player1_choice == 2 and player2_choice == 0)
):
    result = "Player 1 wins"
else:
    result = "Player 2 wins"

# Display the result of the game
print(f"Result: {result}")



# Task 15 - Determining Weight Category:
# Write a program that asks the user for their weight in kilograms and determines their weight category:
# https://en.wikipedia.org/wiki/Body_mass_index
# Use the Body Mass Index (BMI) formula to determine the category.

#1
a = float(input("input your weight in kg: "))
b = float(input("input your height in cm: "))
b = b / 100
bmi = a/(b**2)
if bmi < 16:
    print("Underweight (Severe Thinness)")
elif bmi < 17:
    print("Underweight (Moderate Thinness)")
elif bmi < 18.5:
    print("Underweight (Mild Thinness)")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese (Class I)")
elif bmi < 40:
    print("Obese (Class II)")
else:
    print("Obese (Class III)")

#2
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate the BMI
bmi = weight_kg / (height_m * height_m)

# Determine the weight category based on the BMI
if bmi < 16.0:
    category = "Severe Thinness"
elif bmi >= 16.0 and bmi < 16.9:
    category = "Moderate Thinness"
elif bmi >= 17.0 and bmi < 18.4:
    category = "Mild Thinness"
elif bmi >= 18.5 and bmi < 24.9:
    category = "Normal Weight"
elif bmi >= 25.0 and bmi < 29.9:
    category = "Overweight"
elif bmi >= 30.0 and bmi < 34.9:
    category = "Obesity Class I (Moderate)"
elif bmi >= 35.0 and bmi < 39.9:
    category = "Obesity Class II (Severe)"
else:
    category = "Obesity Class III (Very Severe or Morbidly Obese)"

# Display the weight category to the user
print(f"Your BMI is {bmi:.2f}, and your weight category is: {category}")
