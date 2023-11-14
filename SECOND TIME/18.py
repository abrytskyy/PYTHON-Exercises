weight = int(input('Weight: '))
lk = input('(L)bs or (K)g:')

if lk.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight * 2.2
    print(f"You are {converted} pounds")
