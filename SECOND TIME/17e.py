name = input ('Type your name ? ')
namel = len(name)

if namel<3:
    print ('Name must be at least 3 characters')

elif namel>10:
    print('Name can be a maximum of 10 characters')

else:
    print ('name looks good')