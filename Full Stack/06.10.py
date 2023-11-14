a = "OpenAI ChatbotQQQA"
max_number = 0
for i in a:

    if i.isupper() and a.count(i) > max_number:


        max_number = a.count(i)
        max_i = i
print(max_number, max_i)




a = "sas das dodod adidas sadadas"
a1 = a.split()
max = 0
for i in a1:
    if i == i[::-1] and len(i) > max:
        max = len(i)
        max_i = i
print(max,max_i)



a = "we like Python"
a1 = ""
b = a.split()
for i in b:
    i = i[::-1]
    a1 += i + " "
c = " ".join(a1)
print(a1)

b = "1234"
print(b[2::])

a = "abc"
b = "1234"
c = ""
length = 0
if len(a) > len(b):
    length = len(b)
else:
    length = len(a)
for i in range(length):
    c += a[i] + b[i]
c = c + a[length::] + b[length::]
print(c)




a = "abcd"
b = "1234"
c = ""
for i in range(len(a)):
    c += a[i] + b[i]
print(c)


