import another
print(another.another_variable)

#import turtle
#timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("LawnGreen")
timmy.forward(150)
timmy.speed(3)
timmy.color("Red")
timmy.right(90)
timmy.forward(150)
timmy.speed(3)
timmy.color("Yellow")
timmy.right(90)
timmy.forward(150)
timmy.speed(6)
timmy.color("Blue")
timmy.right(90)
timmy.forward(300)
timmy.speed(3)
timmy.color("Brown")
timmy.right(90)
timmy.forward(150)
timmy.speed(0)
timmy.color("Gold")
timmy.right(90)
timmy.forward(150)


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
jhkghkg
