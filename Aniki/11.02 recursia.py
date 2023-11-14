#1*2*3
def faktorial(x):
    if x == 1:
        return 1
    else:
        print(x*2)
        return faktorial(x-1)


result = faktorial(5)
print(result)

def faktorial(x):
    if x == 1:
        return 1
    else:
        return x*faktorial(x-1)


result = faktorial(5)
print(result)