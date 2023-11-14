# file = open("my_file.txt", encoding='utf-8')
# print(file.read(4))
# print(file.read(4))
# file.seek(0)
# print(file.read(4))
# pos = file.tell()
# print(pos)#on wich position now
#
# print(file.readline(), end="")
# print(file.readline())
#
# strings = file.readlines()
# print(strings)
#
# file.close()
#
# :
#
# try:
#     with open("out.txt2", "w") as file:
#         file.write("Hellow1 + World!\n")
#         file.write("Hellow2 + World!\n")
#         file.write("Hellow3 + World!\n")
# except:
#     print("Error")
#
# try:
#     with open("out.txt2", "a") as file:
#         file.write("Hellow4 + World!\n")
#         file.write("Hellow2 + World!\n")
#         file.write("Hellow36 + World!\n")
# except:
#     print("Error")
#
# try:
#     with open("out.txt2", "a+") as file:
#         file.write("Hellow12 + World!\n")
#         file.write("Hellow25 + World!\n")
#         file.write("Hellow62 + World!\n")
# except:
#     print("Error")
#
# try:
#     with open("out.txt2", "a+") as file:
#         file.seek(0)
#         file.writelines(["HELLO01\n", "HELLO02\n", "HELLO03\n"])
#         strings = file.readlines()
#         print(strings)
# except:
#     print("Error")
#


books = [
    ("Author1", "Book1", 200),
    ("Author1", "Book1", 250),
    ("Author1", "Book1", 300),
    ("Author1", "Book1", 100)

]