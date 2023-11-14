# Напишите генератор, который выдает первые 10 чисел Фибоначчи.
n = 10
a = [0, 1]
[a.append[-1] + a[-2] for i in range(2, n)]
print(a)

a = [0, 1]
for i in range(2,10):

    a.append(a[i-2] + a[i-1])
print(a)


numbers = [n for n in range(10)]
fib_seq = [0, 1]
[fib_seq.append(fib_seq[-1] + fib_seq[-2]) for _ in range(2, n)]
 print(fib_seq[:n])

#Напишите генератор, который выдает все пары чисел от 1 до 5.
a = []
a = [i+i+1 for i in range(1, 5)]

a = []
for i in range (1, 5):
    a.append([i + i + 1])
print(a)


