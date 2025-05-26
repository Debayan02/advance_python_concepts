class Animal:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"{self.name} is the name of the animal")

dog = Animal(int(20))
dog.display()