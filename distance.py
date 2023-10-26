class Distance:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rast(self):
        rast1 = self.b - self.a
        rast2 = self.b - self.c
        rast3 = self.c - self.a
        per = rast1 + rast2 + rast3
        print(per)

ABC = Distance(2.4, 6.9, 6.0 )
ABC.rast()