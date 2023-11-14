# class KgToPounds:
#     def __init__(self, kg):
#         self.kg = kg
#     def to_pounds(self):
#         return self.kg * 0.45
#
# kgtopounds = KgToPounds(15)
# print(kgtopounds.to_pounds())


class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg
    def to_pounds(self):
        return self.__kg * 0.45

    def set_kg(self, kg):
        if isinstance(kg, (int, float)):
            self.__kg = kg

kgtopounds = KgToPounds(15)
print(kgtopounds.to_pounds())
kgtopounds.__kg = 20
print(kgtopounds.to_pounds())
kgtopounds.set_kg(20)
print(kgtopounds.to_pounds())
