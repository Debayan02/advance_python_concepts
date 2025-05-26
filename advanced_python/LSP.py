#LSP(Liskov Substitution Principle:
#It states that the objects of superclass can be substitued by the objects of subclass without affecting the correctness of the program.

class Bird:
    def fly(self):
        pass

class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class Penguin(NonFlyingBird):
    pass


penguin1 = Penguin()
penguin1.fly()