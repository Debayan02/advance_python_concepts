class Animal:
    def __init__(self,name,is_alive):
        self.name = name
        self.is_alive = is_alive
    
    def display(self):
        print(f"{self.name} is the name of animal and is {self.is_alive} now")

class Cat(Animal):
    def __init__(self,age,is_alive,name):
        self.age = age
        super().__init__(name,is_alive)

    def display_cat(self):
        print(f"{self.name} is the name of cat and is {self.age} years old and is still {self.is_alive}")

cat1 = Cat(20,"False","Biuuuu")
cat1.display_cat()

animal1 = Animal("dog","False")
print(cat1 is animal1)