print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

t1 = name1_lower_case.count("t")
t2 = name2_lower_case.count("t")
t = t1 + t2

r1 = name1_lower_case.count("r")
r2 = name2_lower_case.count("r")
r = r1 + r2

u1 = name1_lower_case.count("u")
u2 = name2_lower_case.count("u")
u = u1 + u2

e1 = name1_lower_case.count("e")
e2 = name2_lower_case.count("e")
e = e1 + e2

l1 = name1_lower_case.count("l")
l2 = name2_lower_case.count("l")
l = l1 + l2

o1 = name1_lower_case.count("o")
o2 = name2_lower_case.count("o")
o = o1 + o2

v1 = name1_lower_case.count("v")
v2 = name2_lower_case.count("v")
v = v1 + v2


true = t + r + u + e
love = l + o + v + e

true_love = str(true) + str(love)
true_love_int = int(true_love)

if true_love_int <= 10 or true_love_int >= 90:
    print(
        f"Your score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int >= 40 and true_love_int <= 50:
    print(f"Your score is {true_love_int}, you are alright together. ")
else:
    print(f"Your score is {true_love_int}")
