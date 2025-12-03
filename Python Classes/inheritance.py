#Create a class named Person, with firstname and lastname properties, and a printname method.
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)
p1 = Person("Ram", "Ravi")
p1.printname()

#Create a class named Student, which will inherit the properties and methods of the Person class.
class Student(Person):
    pass
x1 = Student("Mohan", "Sharma")
x1.printname()
#Create a class named Student, which will inherit the properties and methods of the Person class.
class Student(Person):
    def __init__(self, firstname, lastname, graduationyear):
        super().__init__(firstname, lastname)
        self.graduationyear = graduationyear

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x2 = Student("Sita", "Verma", 2025)
x2.welcome()

#Create a class named Vehicle, which will be the parent class for other vehicle types.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}")
class Car(Vehicle):
    def __init__(self, brand, model, car_type):
        super().__init__(brand, model)
        self.car_type = car_type

    def display_car_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Type: {self.car_type}")
my_car = Car("Ford", "Mustang", "Convertible")
my_car.display_info()   
my_car.display_car_info()
