#4. Declare three classes for geometric shapes: Line, Rect, Ellipse. It should be possible to create objects for
# each class with the following commands:
#
# python
# Copy code
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Here, the arguments a, b, c, d represent the coordinates of the upper right and lower left
# corners (arbitrary numbers). In each object, the coordinates should be stored in local properties sp
# (upper right corner) and ep (lower left) as tuples (a, b) and (c, d), respectively.
#
# Create 217 objects of these classes: for each current object, the class is randomly chosen
# (either Line, Rect, or Ellipse). Coordinates are also randomly generated (numeric values). Save all objects in the
# list elements.
#
# Set the coordinates to zero for objects only of the Line class in the elements list.




#5. Declare the class TriangleChecker, objects of which can be created with the command:
#
# python
# Copy code
# tr = TriangleChecker(a, b, c)
# Here, a, b, c are the lengths of the sides of the triangle.
#
# In the TriangleChecker class, declare the method is_triangle(), which would return the following codes:
#
# 1 - if at least one side is not a number (not float or int), or if at least one number is less than or equal to zero;
# 2 - the specified numbers a, b, c cannot be the lengths of the sides of a triangle;
# 3 - the sides a, b, c form a triangle.
#
# Check the parameters a, b, c exactly in this order.
#
# Read a line from the input stream containing three numbers separated by spaces with the command:
#
# python
# Copy code
# a, b, c = map(int, input().split())
#Then, create an object tr of the TriangleChecker class and pass the read values a, b, c to it. Call the is_triangle()
# method from the tr object and print the result on the screen (the code it will return).