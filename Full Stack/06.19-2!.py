#Напишите функцию, которая принимает строку и возвращает новую строку,
# в которой каждое слово начинается с заглавной буквы,
# а остальные буквы в слове в нижнем регистре.

line1 = "в которой каждое слово начинается"
def capital_letter(a):
    cap = False
    for i in a:
        if cap == True:
            i = i.title()
        if i == " ":
            cap = True
        a += i
    return a
print(capital_letter(line1))