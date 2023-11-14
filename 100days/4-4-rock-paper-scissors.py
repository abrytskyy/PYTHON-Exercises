rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
  print("Dial 5 to exit")
  your_figur = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  if your_figur == 5:
   break

  print("You choose:")
  if your_figur == 0:
    print(rock)
  elif your_figur == 1:
    print(paper)
  elif your_figur == 2:
    print(scissors)
  else:
    print("You dialed a wrong number. Dial 1,2 or 0")
  print("Computer choose:")
  import random
  figur = random.randint(0, 2)
  if figur == 0:
    print(rock)
  elif figur == 1:
    print(paper)
  else:
    print(scissors)

  if your_figur == figur:
    print ("Draw.")
  if (your_figur == 0 and figur == 1) or (your_figur == 1 and figur == 2) or (your_figur == 2 and figur == 0):
    print ("You lose")
  if (your_figur == 0 and figur == 2) or (your_figur == 1 and figur == 0) or (your_figur == 2 and figur == 1):
    print ("You win")

