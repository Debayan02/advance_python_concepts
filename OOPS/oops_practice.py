#Design a rectangle class with default attributes for length and width set to 1.
# Include methods to set these attributes and calculate the area.

"""class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def set_dim(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length * self.width)
    
rec1= Rectangle(30,40)
print(rec1.area())"""

#Create a person class with __str__ method.Create a Person class with first and last name attributes and override
#the __str__ method to return full name

from abc import ABC,abstractmethod
class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name = last_name

    @abstractmethod
    def full_name(self):
        pass

class Individual(Person):
    def full_name(self):
        return (self.first_name + " " + self.last_name)
    
Debayan = Individual("Debayan","Pal")
print(Debayan.full_name())


"""class Series_cal:
    def __init__(self,n):
        self.n = n

    def sum(self):
        sum=0
        for i in range(self.n):
            sum+=i
        return sum

Series_cal1=Series_cal(6)"""
#print(Series_cal1.sum())


"""class Highest:
    def __init__(self,alist):
        self.alist=alist

    def largest(self):
        largest = max(self.alist)
        return largest

a=[90,20,30,70,60]
Highest1=Highest(a)
print(Highest1.largest())"""