#Interface Seperation Principle suggests we should not create multiple unrlated methods inside a class as the subclass which will inherit from super class has to implement it even though
#it doesn't need to.

class Iprinter:
    def print(self):
        pass

class Iscanner:
    def scan(self):
        pass

class Icopier:
    def copy(self):
        pass

class Ifax:
    def fax(self):
        pass


class Printer(Iprinter):
    def print(self):
        print("Printing...")

class Scanner(Iscanner):
    def scan(self):
        print("scanning...")

class Fax(Ifax):
    def fax(self):
        print("Faxing....")

printer1 = Printer()
printer1.print()