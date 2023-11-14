print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print()
left_or_right = input("""You are standing on the big island.
On your left hand is the lake. On you righ hand is valley.

Type 'Left' if you going Left og 'Right' if you going Right\n""")
left_or_right_lower = left_or_right.lower()
if left_or_right_lower == "left":
    print()
    swim_or_wait = input("""************************************************************
Good choise...You are standing in front of the lake now. In the sky behind you is a giant trout. Are you going to Swim or Wait?

Type 'Swim' or 'Wait'\n""")
    swim_or_wait_lower = swim_or_wait.lower()
    if swim_or_wait_lower == "wait":
        print()
        door = input("""************************************************************
Good...But trout still coming.On your left side you have 3 doors to hide you. Which door you choose? Red, blue or yellow?

Type 'Red', 'Blue' or 'Yellow'\n""")
        door_lower = door.lower()
        if door_lower == "yellow":
            print("Congratulation! YOU WIN THE GAME!")
        elif door_lower == "red":
            print("You were burned by fire...GAME OVER")
        elif door_lower == "blue":
            print("You were eaten by beasts...GAME OVER")
        else:
            print("You type wrong symbols...GAME OVER")
    else:
        print("You were attacked by trout in the water... GAME OVER")
else:
    print("You fall into a hole...GAME OVER")