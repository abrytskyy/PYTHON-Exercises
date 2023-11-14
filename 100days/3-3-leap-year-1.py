def fun_leap():
    print("Leap")
def fun_not_leap():
    print("Not leap")


year = int(input("Dial a year\n"))
if year % 4 == 0:
    #if year % 400 == 0:
    #    fun_leap()
    #elif year % 100 == 0:
    #    fun_not_leap()
else:
    fun_not_leap
