# На екран вивести True, якщо кратне і False - в іншому випадку.
# Завдання робиться без використання умовного оператора.

#парне число:

#a = int(input("input 'a': "))
#print(not bool(a%2))



a = int(input("input 'a': "))
for i in range (2,a):
    print(not bool(a % i))

