# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
number_of_names = len(names)
payer = random.randint(1, number_of_names - 1)
print(f"{names[payer]} is going to buy the meal today! ")