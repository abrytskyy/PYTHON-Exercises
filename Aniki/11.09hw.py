class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]


    def is_triangle(self):
        if not all(isinstance(i,(int, float)) for i in self.sides):
            print("Потрібно вводити тільки числа!")

        elif all(i>0 for i in self.sides):
            return "З негативними числами нічого не вийде!"
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можна побудувати трикутник!"
        else:
            return "Жаль, але з цього трикутник не зробити."

triangle = TriangleChecker(3, 5, 8)
print(triangle.is_triangle())

triangle1 = TriangleChecker(3, 5, 7)
print(triangle1.is_triangle())

triangle2 = TriangleChecker(3, -5, 8)
print(triangle2.is_triangle())





