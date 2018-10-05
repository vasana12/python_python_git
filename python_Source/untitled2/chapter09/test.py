class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("meow")
class Chimera(Cat, Dog):
    pass

Chimera().sound()

