# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = (float(weight)/float(height)**2)
bmi_round=round(bmi, 2)

print("BMi= " + str(bmi_round))
if bmi_round < 18.5:
    print("You are underweight")
elif bmi_round < 25:
    print("You have a normal weight")
elif bmi_round < 30:
    print("You are overweigh")
elif bmi_round < 35:
    print("You are obese")
else: print("You are clinically obese")



