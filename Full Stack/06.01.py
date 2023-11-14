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

for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")


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
