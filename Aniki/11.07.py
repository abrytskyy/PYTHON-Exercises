# Створіть клас Soda (для визначення типу газованої води), що приймає 1 аргумент при ініціалізації (що відповідає
# за добавку до лимонаду, що вибирається).
# У цьому класі реалізуйте метод show_my_drink(), що виводить на друк «Газування та {ДОБАВКА}» у разі наявності
# добавки, а інакше з'явиться така фраза: «Звичайне газування».

class Soda():
    def __init__(self, adding):
        self.adding = adding
    def show_my_drink(self):
        print(self)
        if self.adding:
            print(f"Газування та {self.adding}")
        else:
            print("Звичайне газування")
soda1 = Soda("adding1")
soda2 = Soda("adding2")
print(soda1, soda2)
# print(soda1.adding, soda2.adding)
# soda1.show_my_drink()
# soda2.show_my_drink()

