class Shape:
    def __init__(self,color,length):
        self.color=color
        self.length=length
    
    def area(self):
        return self.length * self.length

#Using super() when we have __init__
class Triangle(Shape):
    def __init__(self,color,length,height):
        self.height=height
        self.color=color
        self.length=length
        #super().__init__(color,length)
        super().area()
        print(f"The colour of the triangle is {self.color} and is {self.length} cm in length and {height}cm in height")

#Without using super() when we dont have __init__    
class Triangle2(Shape):
    def prop_triangle(self,color,length,height):
        self.height=height
        self.color = color
        self.length = length
        #super().__init__(color,length)
        print(f"The colour of the triangle is {self.color} and is {self.length} cm in length and {height} cm")   


#square=Square("Blue",20,30)
#print("The colour of first triangle")
triangle1=Triangle("Black",30,40)
print("----This is area---------")
print(triangle1.area())
#print("The colour of second triangle")
#triangle2=Triangle2("Blue",30)
#triangle2.prop_triangle("Brown", 40,50)




"""class Shape:
    def __init__(self, color, length, width):
        self.color = color
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class Square(Shape):
    def __init__(self, color, length, width, diagonal):
        self.diagonal = diagonal
        super().__init__(color, length, width)
        super().area()

#Square1 = Square("Blue", 50, 40, 80)
#print(Square1.area())

sq1 = Square("Blue",10,20,40)
print(sq1.area())"""



class Shape:
    def __init__(self, color, length, width):
        self.color = color
        self.length = length
        self.width = width
    
    
class Square(Shape):
    def __init__(self, color, length, width, diagonal):
        self.diagonal = diagonal
        super().__init__(color, length, width)

    def area(self, perimeter):
        print(f"The {perimeter} is perimeter")
        return self.length * self.width

#Square1 = Square("Blue", 50, 40, 80)
#print(Square1.area())

sq1 = Square("Blue",10,20,40)
print(sq1.area(600))