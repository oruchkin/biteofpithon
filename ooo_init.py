class Person:
    def __init__(self, name):
        self.name11 = name

    def sayHi(self):
        print("Привет как дела?", self.name11)

p = Person('Oleg')
p.sayHi()