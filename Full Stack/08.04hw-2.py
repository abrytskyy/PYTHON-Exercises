
###Артём
#Создайте множество из всех уникальных букв в слове "hello".
str1 = "hello"
set1 = set(str1)
print(set1)

# Из списка слов выберите только те, которые заканчиваются на "ing".
str1 = "What is ing in the word Viking ?"
str2 = str1.split(" ")
list1 = [s for s in str2 if s.endswith("ing")]
print(list1)

str1 = " What is ing in the word Viking ?"
str2 = str1.split(" ")
list1 = []
for s in str2:
    if s.endswith("ing"):
        list1.append(s)
print(list1)

#Создайте множество из длин слов в строке "The quick brown fox jumps over the lazy dog".
str1 = "The quick brown fox jumps over the lazy dog"
str2 = set(str1.split(" "))
print(str2)


#Из списка строк создайте словарь, где ключами будут строки, а значениями - список их уникальных символов.
strings = ["apple", "banana", "orange", "grapefruit"]


unique_chars_dict = {string: [char for char in string if char not in string[:index]] for index, string in enumerate(strings)}

print(unique_chars_dict)

strings = ["apple", "banana", "orange", "grapefruit"]
dict1 = {string:list(set(string)) for string in strings}
print(dict1)
#dic1 = {k: i for }

#Создайте словарь, в котором ключами будут слова из строки, а значениями - их длины, но только для слов длиной менее 6 символов.
str1 = "artemov u ivanova"

text = "Python is a programming language that lets you work quickly and integrate systems more effectively."
word_length_dict = {k: len(k) for k in text.split() if len(k) < 6}

print(word_length_dict)




#Из списка кортежей (слово, длина) создайте словарь, где слова будут ключами, а длины - значениями.

list1 = [("artem", 5), ("ivan", 4)]
print(dict(list1))
print({k:v for k,v in list1})

