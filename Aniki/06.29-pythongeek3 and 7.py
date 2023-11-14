def pythongeek(a,b):
    c = ""
    for n in range(a,b):
        if n % 3 == 0 and n % 7 == 0:
            c += "PythonGeek "
        elif n % 3 == 0:
            c += "Python "
        elif n % 7 == 0:
            c += "Geek "
        else:
            c += str(n)+ " "
    return c
print(pythongeek(20, 30))