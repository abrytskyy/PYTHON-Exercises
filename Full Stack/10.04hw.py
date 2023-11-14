#Подсчет согласных букв: Напишите генератор, который подсчитывает количество согласных букв в строке.

def count_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in input_string if char in consonants)
input_str = "Hello, World!"
result = count_consonants(input_str)
print("Number of consonant letters:", result)

