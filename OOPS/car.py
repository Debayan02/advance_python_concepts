"""class Car:
    def __init__(self,year,color,model):
        self.year=year
        self.color=color
        self.model=model

    def stop_car(self):
        print(f"Please stop the {self.color} {self.model}")

    def start_car(self,color,model):
        print(f"Please start the {color} {model}")


class Student:
    class_year='2024'
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students+=1"""


class Student:
    nterms = 6
    def fibonacci(nterms):
        count = 0
        n1,n2=0,1
        while count < int(nterms):
            if count == 0:
                count+=1
                return n1
            elif count == 1:
                count+=1
                return n2
            else:
                nth = n1+n2
                n1=n2
                n2=nth
                count+=1
                return nth

std1 = Student()
std1.fibonacci()
