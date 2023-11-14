
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = (float(weight)/float(height)**2)
bmi_round=round(bmi)

print("BMi= " + str(bmi_round))
