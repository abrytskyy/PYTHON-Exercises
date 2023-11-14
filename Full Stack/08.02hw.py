###Катерина
#Напишите функцию, которая принимает на вход список слов и возвращает словарь,
# в котором ключами являются слова, а значениями - количество согласных букв в каждом слове.

###Артём
# Создайте словарь, где ключами являются буквы из слова "Android", а значениями - их ASCII-коды.
print(ord("A"))
word = "Android"
ascii_dict = {letter: ord(letter) for letter in word}
print(ascii_dict)

#Создайте словарь, в котором ключами являются буквы из слова "Programming", а значениями - их порядковые номера.
word = "Programming"
letter_positions = {k: v for v in range(len(word)) for k in word[v]}

print(letter_positions)

word = "Programming"
letter_positions = {k: v for v, k in enumerate(word)}

print(letter_positions)

#Напишите функцию, которая принимает на вход список слов и возвращает словарь,
# в котором ключами являются слова, а значениями - количество гласных букв в каждом слове.

words = ["apple", "banana", "orange", "grapefruit"]
def key_words_value_number_of_values(a):
    return {word: sum(letter in "aeiou" for letter in word.lower()) for word in a}
print(key_words_value_number_of_values(words))

def key_words_value_number_of_values(a):
    return {word: sum(1 for letter in word if letter in "aeiou") for word in a}

print(key_words_value_number_of_values(words))


def key_words_value_number_of_values(a):
    a1 = {}
    for i in a:
        num = 0
        for j in i:

            if j in "aeoui":
                num += 1
        a1[i] = num
    return a1
print(key_words_value_number_of_values(words))
