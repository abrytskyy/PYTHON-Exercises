print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2

name_lower_case = name.lower()

t = name_lower_case.count("t")
r = name_lower_case.count("r")
u = name_lower_case.count("u")
e = name_lower_case.count("e")

l = name_lower_case.count("l")
o = name_lower_case.count("o")
v = name_lower_case.count("v")

true = t + r + u + e
love = l + o + v + e

true_love = str(true) + str(love)
true_love_int = int(true_love)

if true_love_int < 10 or true_love_int > 90:
    print(
        f"Your love score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int >= 40 and true_love_int <= 50:
    print(f"Your love score is {true_love_int}, you are alright together. ")
else:
    print(f"Your love score is {true_love_int}")
