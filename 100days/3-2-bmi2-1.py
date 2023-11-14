# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = (float(weight)/float(height)**2)
bmi_round=round(bmi, 2)

if bmi_round < 18.5:
    print(f"Your BMI is {bmi_round}, you are underweight")
elif bmi_round < 25:
    print(f"Your BMI is {bmi_round}, you are have a normal weight")
elif bmi_round < 30:
    print(f"Your BMI is {bmi_round}, you are overweight")
elif bmi_round < 35:
    print(f"Your BMI is {bmi_round}, you are obese")
else: print(f"Your BMI is {bmi_round}, you are clinically obese")
