class Reader:

    def __init__(self, fio, n, f, dr, p, x, y):
        self.fio = fio
        self.n = n
        self.f = f
        self.dr = dr
        self.p = p
        self.x = x
        self.y = y
    def takeBook(self):
        print(self.fio, 'взял', self.x, 'книг')

    def returnBook(self):
        print(self.fio, 'вернул', self.y, 'книг')

pers1 = Reader('Ботаников Евгений Мельничуков', '228339', 'Ботанический', '23/12/2002', '88005553535', 5, 5)
pers1.takeBook()
pers1.returnBook()