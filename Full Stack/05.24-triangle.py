#scalene,isosceles or equilateral triangle
a = 20
b = 30
c = 10


if a == b == c:
    print("It's equilateral triangle")
elif (a == b and a != c) or (b == c and b != a) or (a == c and c != b) :
    print("It's a isosceles triangle")
else:
    print("It's scalene triangle")
