users10 = ("Tom", "Bob", "Alice")
print(users10[:-1])

users.remove("Tom")
users.add("Tim")
print(users)

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users5 = users & users2
users6 = users ^ users2
print(users5, users6)

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.union(users2)
users4 = users.intersection(users2)
print(users3, users4)


users = {"Tom", "Bob", "Alice"}

for user in users:
    print(user)

users = {"Tom", "Bob", "Alice", "Tom"}
users.discard("Boba")

print(users)
users.add("Artem")
print(users)

users.add("Sam")
print(users)

users = {"Tom", "Bob", "Alice", "Tom"}

print(users)
users.clear()
print(users)

def print_person(name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")


tom = "Tom", 22
print_person(*tom, "Microsoft")  # Name: Tom  Age: 22  Company: Microsoft

bob = ("Bob", 41, "Apple")
print_person(*bob)  # Name: Bob  Age: 41  Company: Apple

name, age, company, position = ("Tom", 37, "Google", "software developer")
print(age)

a= [1, 2]

b=2
c=3

print(a)
print(b)
print(c)

print(id(a))
print(id(b))
print(id(c))
a.append(3)
print(a)
print(id(a))