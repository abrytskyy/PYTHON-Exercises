# 5.Посчитайте сумму цифр всех чисел в списке и верните наибольшую цифру из этой суммы.
a = [3, 2, 5, 5, 4]
max = a[0]
sum = 0
for i in a:
    sum += i
    if i > max:
        max = i
print(max)
print(sum)


#a = [3, 2, 5, 5, 4]
#print(sum(a))
#print(max(a))

# 4.Создайте два списка и получите новый список, содержащий только элементы,
# которые присутствуют в обоих списках на нечетных позициях.
a = [3, 2, 5, 5, 4]
b = [30, 20, 50, 50, 40]
c = list()
for i in range (len(a)):
    if i % 2 == 1:
        c.append(a[i])
for i in range (len(b)):
    if i % 2 == 1:
        c.append(b[i])
print(c)



# 3.Определите, есть ли в списке повторяющиеся подряд идущие элементы.

a = [3, 2, 5, 5, 4]
a0 = a[0]
b = False
for i in range(1,len(a)):
    if a[i-1] == a[i]:
        b = True
        break
print(b)

a = [3, 2, 5, 5, 4]

b = False
for i in range(1,len(a)):
    #1.1. if a[i-1] == a[i]:  - if i = 0 we check a[0] and a[-1] what is not neighboring
    #1.2. if a[i + 1] == a[i]:  -out og range
        b = True
        break
print(b)




