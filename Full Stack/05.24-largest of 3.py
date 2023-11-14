print(max([2,2,2]))


a = int(input("Input 1 number: "))
b = int(input("Input 2 number: "))
c = int(input("Input 3 number: "))


if (c < a > b) or (b == c and b < a):
    print("number 1 is the biggest")
elif (a < b > c) or (a == c and a < b):
    print("number 2 is the biggest")
elif (a < c > b) or (a == b and a < c):
    print("number 3 is the biggest")
elif a == b and a > c:
    print ("number 1 and 2 are same and are the biggest")
elif a == c and a > b:
    print("number 1 and 3 are same and are the biggest")
elif b == c and b > a:
    print("number 2 and 3 are same and are the biggest")
else:
    print("all numbers are same")







