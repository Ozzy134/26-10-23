class Person:
    kind = "men"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('уничтожен', self.name)

    def say_hello(self):
        self.say(f'Hello {self.kind}')

tom = Person('Tom', 25)
print(tom.name)
bob = Person('Bob', 34)
print(bob.name)