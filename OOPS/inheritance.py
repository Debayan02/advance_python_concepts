#Inheritance allows a class to inherit methods and variables of another class,thus extends the feature of
#code reuseability and extensibility
#Multiple Inheratance:-Child class inherits from more than one parent class
#Multilevel Inheritance allows a class to inherit from parent class which itself is a chile class of another 
#parent class

class Animal:
    def __init__(self,name,is_alive):
        self.name=name
        self.is_alive=is_alive
    
    def sleep(self):
        print(f"{self.name} is sleeping")

    
class Dog(Animal):

    def __init__(self,name,is_alive,colour):
        self.colour = colour
        super().__init__(name,is_alive)
        super().sleep()

    def speak_dog(self,age):
        self.age=age
        print(f"{self.name} barks and {self.is_alive} and is {age} years old and is {self.colour} in colour")

    def bark_dog(self,sound_habit):
        self.sound_habit = sound_habit
        print(f"{self.name} is {self.is_alive} and goes for {self.sound_habit} loudly")
    

    
class Cat(Animal):
    def speak_cat(self):
        self.is_alive='False'
        print(f"{self.name} mew and {self.is_alive}")

class Predator(Dog):
    pass


dog1 = Dog("Tommy","True","White")
dog1.speak_dog(40)
dog1.sleep()
