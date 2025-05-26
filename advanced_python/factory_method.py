from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectange(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Areacalculator:
    def calculate_area(self,shapes):
        return sum(shape.area() for shape in shapes)
    

circle = Circle(5)
rectangle = Rectange(10,4)

calculator = Areacalculator()
print(calculator.calculate_area([circle,rectangle]))