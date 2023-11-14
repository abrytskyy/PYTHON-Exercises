
# 2. Создать класс Movie, в котором есть поля: title, year, rating. Написать метод showInfo(),
# который выводит значение полей на экран.
# Создать массив из 10 элементов и заполнить значениями:
# " The Shawshank Redemption", 1994, 8.53,
# " Fight Club", 1999, 7.31,
# " The Godfather", 1972, 8.15,
# " The Dark Knight", 2008, 9.1,
# " Pulp Fiction", 1994 , 7.91,
# " Forrest Gump ", 1994 , 7.2,
# " Lord of the Rings 1 ", 2001, 8.4,
# " Lord of the Rings 2", 2003 , 8.1,
# " The Matrix ", 1999 , 8.7,
# " Inception", 2010, 8.92
# - вывести весь массив
# - вывести фильмы, год выпуска которых с 2001 по 2008 включительно
# - вывести фильмы, которые вышли в 1994 году и посчитать их количество
# - посчитать средний рейтинг всех фильмов
# - вывести массив в обратном порядке
class Movie:
    def __init__(self, t, y, r):
        self.title = t
        self.year = y
        self.rating = r

    def show_info(self):
        print(self.title,self.year, self.rating)

data = [
    Movie("The Shawshank Redemption", 1994, 8.53),
    Movie("Fight Club", 1999, 7.31),
    Movie("The Godfather", 1972, 8.15),
    Movie("The Dark Knight", 2008, 9.1),
    Movie("Pulp Fiction", 1994 , 7.91),
    Movie("Forrest Gump ", 1994 , 7.2),
    Movie("Lord of the Rings 1 ", 2001, 8.4),
    Movie("Lord of the Rings 2", 2003 , 8.1),
    Movie("The Matrix ", 1999 , 8.7),
    Movie("Inception", 2010, 8.92)

]
# for m in data:
#     m.show_info()
# for m in data:
#     if m.year >= 2001 and m.year <= 2008:
#         m.show_info()

# n = 0
# for m in data:
#
#     if m.year == 1994:
#         m.show_info()
#         n +=1
#
# print(n)
# sum = 0
# for m in data:
#     sum += m.rating
#
# print(sum/len(data))

for i in range(len(data)-1, -1, -1):
    m= data[i]
    m.show_info()






"""1. Создать класс Product, в котором есть поля: id, title, price. Есть метод showInfo(),
который выводит значение всех полей на экран. Создать массив объектов из 3 элементов.
Заполнить объекты значениями:
34
Transformers: Age of Extinction
19.99$
57
The Expendables 3
14.99$
183
The Patriot
12.99$
Вывести массив на экран"""
class Product:
    def __init__ (self, i, t, p):
        self.id = i
        self.title = t
        self.price = p

    def show_info(self):
        print(self.id, self.title, self.price)

# p1 = Product(34, 'Transformers: Age of Extinction', 19.99)
# p1.show_info()
#
# p2 = Product(57, 'The Expendables 3', 14.99)
# p2.show_info()
data = [
    Product(34, 'Transformers: Age of Extinction', 19.99),
    Product(57, 'The Expendables 3', 14.99),
    Product(183, 'The Patriot', 12.99)
]
# for p in data:
#     p.show_info()





















