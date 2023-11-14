# Split string method
names_string = input("Give me everybody's names, separated by a comma and spase ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
import random
name_ch = random.randint(0, len(names)-1)
who_pay = names[name_ch]
print(who_pay)