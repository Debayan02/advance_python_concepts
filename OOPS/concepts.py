#Object is a bundle of attributes and methods.
#Class is a blueprint used to design the structure and layout of an object. 
#__init__ is a constructor used to create object of class.
#Class variable are created outside the constructor and can be accessed by any object created within
#that class.
#Instance variables are created within a method of class and is specific to that particular method,data
#cant be shared among other methods of same class.

from car import Car,Student

car1 = Car("2025", "Yellow", "Hyundai Verna")
car2 = Car('2026', 'Blue', 'XUV 700')
car3 = Car('2027', 'Black', 'Tata Nexon')

#print(f"This car {car1.model} of {car1.year} is {car1.color}")
#print(f"This car {car2.model} of {car2.year} is {car2.color}")
#print(f"This car {car3.model} of {car3.year} is {car3.color}")

car3.stop_car()
car1.start_car(car1.color,car1.model)

Student1=Student('Debayan','35')
Student2=Student('Kunal','30')
Student3=Student('Abhik','32')

print(f"Name of the students are following: {Student1.name},{Student2.name},{Student3.name}")
print(f"My class of {Student.class_year} has {Student.num_students}")