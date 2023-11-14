print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7. ")
    elif age < 45 or age > 55:
        bill = 12
        print("Adult tickets are $7. ")
    else:
        bill = 0
        print("Tickets in age 45-55 are free. ")
    photo = input("Do you want a photo taken? Y or N. The price is $3  ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")



else:
    print("Sorry, you have to grow taller before you can ride")