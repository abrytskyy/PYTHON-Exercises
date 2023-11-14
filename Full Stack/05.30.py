people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

print(people[0])  # ["Tom", 29]
print(people[0][0])  # Tom
print(people[0][1])

people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
people1 = list(people)
people1.reverse()
people3 = people + people1
print(people3)
slice_people1 = people[3:]  # с 0 по 3
print(slice_people1)

people = ["Tom", "Sam", "Bob"]
i = 0
while i < len(people):
    print(people[i])    # применяем индекс для получения элемента
    i += 1

people = ["Tom", "Bob", "Sam"]
size = len(people)

tom, bob, sam = people
print(size)
print(tom)  # Tom
print(bob)  # Bob
print(sam)  # Sam

numbers = [5] * 6  # 6 раз повторяем 5
print(numbers)  # [5, 5, 5, 5, 5, 5]

people = ["Tom"] * 3  # 3 раза повторяем "Tom"
print(people)  # ["Tom", "Tom", "Tom"]

students = ["Bob", "Sam"] * 2  # 2 раза повторяем "Bob", "Sam"
print(students)  # ["Bob", "Sam", "Bob", "Sam"]

numbers = [1, 2, 3, 4, 5]
#num = [numbers]
#num = list(numbers)
num = numbers.copy()


print(id(num))
print(id(numbers))

numbers1 = []
numbers2 = list()


number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, переходим к новой итерации цикла
        continue
    print(f"number = {number}")

number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, выходим из цикла
        break
    print(f"number = {number}")


i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1




number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")