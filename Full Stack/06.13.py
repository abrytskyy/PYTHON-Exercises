def replace_digits_to_asteriks(a):
    a1 = ""
    for i in a:
        if i.isdigit():
            i = "*"
        a1 += i
    return a1
print(replace_digits_to_asteriks("jsg3"))