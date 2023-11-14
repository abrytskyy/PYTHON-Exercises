tom = ("Tom", 23)
print(tom)
tom = "Tom", 23
print(tom)

tom = ("Tom",)

data = ["Tom", 37, "Google"]
tom = tuple(data)
print(tom)

tom = ("Tom", 37, "Google")
print(len(tom))

tom = ("Tom", 37, "Google", "software developer")
print(tom[0])

#tom[1] = "Tim"
# TypeError: 'tuple' object does not support item assignment

name, age, company, position = ("Tom", 37, "Google", "software developer")
print(age)

tom = ("Tom", 37, "Google", "software developer")

# получем подкортеж с 1 по 3 элемента (не включая)
print(tom[1:3])  # (37, "Google")

# получем подкортеж с 0 по 3 элемента (не включая)
print(tom[:3])  # ("Tom", 37, "Google")

# получем подкортеж с 1 по послдений элемент
print(tom[1:])