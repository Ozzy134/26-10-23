class Square:

    def __init__(self, a):
        self.a = a

    def per(self):
        pera = self.a + self.a + self.a + self.a
        print('Перимитр квадрата =', pera)

    def plosh(self):
        sa = self.a * self.a
        print('Площадь квадрата = ', sa)

a = Square(4)
a.per()
a.plosh()