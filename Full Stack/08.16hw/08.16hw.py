

#Запишите в файл список имён друзей, каждое имя на новой строке.
friend_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

with open('friends.txt', 'w') as file:
    for name in friend_names:
        file.write(name + '\n')

file = open("out.txt", "w")
file.write("Oleg\n")
file.write("Ivan\n")
file.write("Taras\n")
file.close()

try:
    with open("out.txt1", "w") as file:
        file.write("Illa\n")
        file.write("Bogdan\n")
        file.write("Jurij\n")
except:
    print("Error")
#Прочитайте содержимое текстового файла и подсчитайте количество слов.
with open("out.txt", "r") as file:
    content = file.read()
    print(content)
    print(len(content.split()))