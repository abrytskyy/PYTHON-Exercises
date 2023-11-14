def pythongeek(a, b):
    return ' '.join(('Python' * (i % 3 == 0) + 'Geek' * (i % 7 == 0) or str(i)) for i in range(a, b + 1))
print([i**2 for i in range (1,5)])

print([('Python' * (i % 3 == 0) + 'Geek' * (i % 7 == 0) or str(i)) for i in range(14, 21 + 1)])
print("Python"*True)