class Triangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def per(self):
        per1 = 2 * self.a + self.b
        print('Периметр триугольника =', per1)

    def plos(self):
        s = self.a + self.b * 0.5
        print('Площадь триугольника =', s)

a = Triangle(3, 5)
a.per()
a.plos()