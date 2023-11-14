age = input("What is your current age? ")

years = 90 - int(age)
days = 365*years
weeks = 52*years
month = 12*years

print(f"You have {days} days, {weeks} weeks and {month} monthes left")
