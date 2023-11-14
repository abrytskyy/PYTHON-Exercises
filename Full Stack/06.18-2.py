# 3. Напишите функцию, которая принимает список строк и возвращает новый список,
# содержащий только те строки, которые имеют длину больше 5 символов.
line = "которые имеют длину больше"
def more5_symbols (a):
    line1 = []
    line2 = a.split()
    for i in line2:
        if len(i) > 5:
            line1.append(i)
    return line1
print(more5_symbols(line))



