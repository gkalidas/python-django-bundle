class Test(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is sitting now.')

    def sit2(self):
        print(self.name.title(), self.age)


person_1 = Test('Ganesh', 24)
person_2 = Test('Kalidas', 56)

person_1.sit()
person_2.sit2()
