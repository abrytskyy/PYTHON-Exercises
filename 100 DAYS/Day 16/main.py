import another_module
print(another_module.another_variable)
#1
#import turtle

#timmy = turtle.Turtle()

#2
#from turtle import Turtle

#timmy = Turtle()
#print(timmy)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse1")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pockemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
