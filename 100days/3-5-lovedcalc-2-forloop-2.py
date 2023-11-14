# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# true love
name3 = (name1 + name2).lower()
score = 0
score1 = 0
for x in name3:
    if x in "true":
        print(x)
        score+=1
print(score)

for x in name3:
    if x in "love":
        print(x)
        score1+=1

print(score1)
score_together = int(str(score) + str(score1))
print(score_together)

if score_together<10 or score_together>90:
    print(f"Your score is {score_together}, you go together like coke and mentos.")
elif (score_together > 40 and score_together<90) or (score_together < 50 and score_together > 10):
    print(f"Your score is {score_together}, you are alright together .")
else:
    print(f"Your score is {score_together}.")