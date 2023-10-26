class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        print(f'x = {self.x}, y = {self.y}, z = {self.z}')

    def distance(self):
        dxy = self.y - self.x
        dzy = self.z - self.y
        print(f'Расстояние между xy: {dxy}. Расстояние между zy: {dzy}')

    def doubl(self):
        return 2 * self.x, 2 * self.y, 2 * self.z

a = Point3D(1,2,3)
b = Point3D(4,5,6)
c = Point3D(-5, -457, 0)
a.info()
b.info()
c.info()
a.z = 1231243123
a.info()
a.distance()
a.doubl()