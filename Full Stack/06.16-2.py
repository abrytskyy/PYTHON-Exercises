
# 2. Write a Python function that accepts a string and counts
# the number of upper and lower case letters. Sample String : 'The quick Brow Fox'

result = "The quick Brow Fox"
def without_space(a):
    result1 = ""
    for i in a:
        if i != " ":
            result1 += i
    return result1
def count_letters(a):
    n = 0
    for i in a:
        if i != " ":
            n += 1
    return n

print(without_space(result))
print(count_letters(result))

