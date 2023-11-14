list1 = [2, 3, 4, 5, 6]
list2 = [2, 7, 8]

def elem_from_2list(a,b):
    a1 = []
    for i in b:
        if i not in a:
            a1.append(i)
    a2 = a + a1
    return a2
print(elem_from_2list(list1, list2))

def average(a):
    av = sum(a)/ len(a)
    return av

def more_average(a):
    a1 = []
    for i in a:
        if i > average(a):
            a1.append(i)
    return(a1)
print(more_average([4, 3, 6, 8, 2, 7]))

def not_letters1(a):
    a1 = ""
    for i in a:
        if not i.isalpha():
            a1 += i
    return a1
print(not_letters1("aghjk 24 gh2 5gg"))


def not_letters(a):
    a1 = []
    for i in a:
        if not i.isalpha():
            a1.append(i)
            b = "".join(a1)
    return b
print(not_letters("aghjk 24 gh2 5gg"))

def length_three(a,length):
    a1 = []
    for i in a:
        if len(i) > length:
            a1.append(i)
    return(a1)
print(length_three(["apple", "orange", "lol"], 5))

def content_e(a):
    a1 = []
    a = a.split()
    for i in a:
        if "e" in i:
            a1.append(i)
    return a1
print(content_e("bed, bad, true"))
