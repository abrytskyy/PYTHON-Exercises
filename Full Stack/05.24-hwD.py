# 1. Проверка на палиндром:
# Напишите программу, которая запрашивает у пользователя число  и проверяет,
# является ли оно палиндромом. Палиндром - это слово, число или фраза, которые читаются
# одинаково в обоих направлениях. Используйте оператор % для сравнения символов в начале и
# конце слова или фразы. Если слово или фраза является палиндромом, выведите сообщение "Это палиндром",
# в противном случае - выведите "Это не палиндром".
a = input("innput something: ")
rev_a = reversed(a)
print(list(a) == list(rev_a))


a = input("innput something: ")
a_rev = a[::-1]
print(a == a_rev)






# 2. Определение времени суток:
# Напишите программу, которая запрашивает у пользователя текущий час (от 0 до 23) и выводит сообщение
# о времени суток: "Утро", "День", "Вечер" или "Ночь".
time = int(input("Write hour between 0 and 23, without minutes: "))

if time <= 6:
    print("Night")
elif time <= 12:
    print("Morning")
elif time <= 18:
    print("Day")
else:
    print("Evening")





# 3. Напишите программу для определения права на поступление на профессиональный курс на основе следующих критериев:
# Критерии отбора: баллы по математике >=65 и баллы по физике >=55 и баллы по химии >=50 и общее количество баллов по всем трем предметам >=190 или общее количество баллов по математике и физике >=140
# Введите оценки, полученные по физике: 65
# Введите оценки, полученные по химии: 51
# Введите баллы, полученные по математике: 72 Всего баллов по математике, физике и химии: 188
# общее количество баллов по математике и физике: 137
# Кандидат не соответствует требованиям. Ожидаемый результат: Кандидат не имеет права на допуск.
a = int(input("Input mark in physics: "))
b = int(input("Input mark in chemistry: "))
c = int(input("Input mark in mathemathics: "))
if a >= 65 and b >= 51 and c >= 72:
    print("Candidate meets requirements")
else:
    print("Candidate don't meets requirements")






