

people = ["Tom", "Bob", "Sam"]

tom, bob, sam = people

print(tom)  # Tom
print(bob)  # Bob
print(sam)

people = ["Tom", "Sam", "Bob"]

people[1] = "Mike"  # изменение второго элемента
print(people[1])  # Mike
print(people)

numbers = [5] * 6
print(numbers)

students = ["Bob", "Sam"] * 2   # 2 раза повторяем "Bob", "Sam"
print(students)