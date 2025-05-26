#Metaclass
#All classes in python are treated as objects as the class is created from another class which is meta class.
class Edureka:
    z = 20
print(type(Edureka))
a = type('Python', (Edureka,), {'x':10})
obj = a()
print(obj.z)

c = type('Debayan',(),{'m':30})
print(c.m)