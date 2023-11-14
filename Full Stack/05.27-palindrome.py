number = 101
original = number
reversed_number = 0

while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number //= 10
if original == reversed_number:
    print(True)
else:
    print(False)


words = ["d", "a", "fdb", "a", "d"]
string = ""
for word in words:
    string += word
print(string[::-1] == string)

list1 = ["a","b","a"]
list2 = list1[::-1]
print(list1==list2)