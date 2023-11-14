#max age


people = [
    ('Alice', 25),
    ('Bob', 30),
    ('Frank', 35),
    ('Alice', 45)
]

def sort_by_age(people):
    for i in range(len(people)-1):
        for j in range(len(people)-1-i):
            if people[j][1] > people[j+1][1]:
                people[j], people[j+1] = people[j+1], people[j]

sort_by_age(people)
print(people)

people = [
    ('Alice', 25),
    ('Bob', 30),
    ('Frank', 35),
    ('Alice', 45)
]

print(max(people,key=lambda person: person[1]))
print(sorted(people,key=lambda person: person[1]))
print(sum(map(lambda person: person[1], people))/len(people))
print(len([person for person in people if person[1] < 31 ]))
print([(person[0],) for person in people])
print({(person[0],) for person in people})
print(sorted(people,key=lambda person: person[0]))

#k-vo palindr v spiske
str1 = ['level', 'hello', 'radar']
count = 0
for s in str1:
    if s == s[::-1]:
        count += 1
print(count)

#naibolsh raznica mezhdu dvuma sosednimi el v sp
list1 = [2,9,3,10,8]
list2 = []
for l in range(len(list1)-1):
    dif = abs(list1[l+1] - list1[l])
    list2.append(dif)
print(max(list2))


list1 = [2,9,3,10,8]
list2 = []
for l in range(len(list1)):
    dif = abs(list1[l] - list1[l-1])
    list2.append(dif)
print(max(list2))




#vtor naimensh chislo v spiske
list1 = [2,9,3,10,8]

print(list(set(list1))[-2])