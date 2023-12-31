#1. Create a text file and write the string "Hello, World!" into it.
with open('hello_world.txt', 'w') as file:
    file.write("Hello, World!")
# checking place for directory where we are now to find file we created:
import os
print(os.getcwd())

#2. Open the file from the previous task, read its contents, and display them on the screen.
with open('hello_world.txt', 'r') as file:
    text = file.read()
print(text)

#3. Create a file in which each line contains a number from 1 to 10, with each number on a new line.
with open('numbers.txt', 'w') as file:
    for number in range(1, 11):
        file.write(str(number) + '\n')

#4. Read the file from the previous task, convert the lines to numbers, and calculate their sum.
with open('numbers.txt', 'r') as file:
    text = file.read()
print(text)

list_string = text.split('\n')
list_int = [int(element) for element in list_string if element.isdigit()]
print(list_int)

print(sum(list_int))

#method2
total_sum = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        print(number)
        total_sum += number
print("The sum of numbers in the file is:", total_sum)


#5. Create a file containing a list of words, with each word on a new line. Read the file, sort the words, and write them back.
words = ["banana", "elderberry", "cherry", "date", "apple"]
with open('words.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')

with open('words.txt', 'r') as file:
    text = file.read()
print(text)

words_list = text.split('\n')
words_list.pop()
words_list.sort()
print(words_list)

with open('words.txt', 'w') as file:
    for word in words_list:
        file.write(word + '\n')

#6.  Find the longest word in the file from the previous task.
with open('words.txt', 'r') as file:
    text = file.read()
words_list = text.split('\n')
words_list.pop()
print(max(words_list, key=len))