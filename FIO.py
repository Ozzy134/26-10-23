class CPerson:

    def __init__(self, f, i, o, s, m, g, p):
        self.f = f
        self.i = i
        self.o = o
        self.s = s
        self.m = m
        self.g = g
        self.p = p

    def pok(self):
        print('ФИО:', self.f, self.i, self.o)
        print('Д.Р:', self.s, self.m, self.g)
        print('Пол:', self.p)

pers1 = CPerson('Бабинов', 'Алексей', 'Евгеньевич', '09', '09', '2007', 'Мужской' )
pers2 = CPerson('Зубенко', 'Михаил', 'Петрович', '228', '339', '1999', 'Мафиозник' )
pers1.pok()
del pers1
pers2.pok()
del pers2
