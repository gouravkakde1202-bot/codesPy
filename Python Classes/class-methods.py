#Define the Student class with methods
class Student:
    def __init__(self, name, student_id): 
        print("A new student object is being created!")
        self.name = name          
        self.student_id = student_id
        self.is_enrolled = True
student1 = Student("Rahul", 101)
student2 = Student("Pranav", 102)
print(f"{student1.name}'s ID is {student1.student_id}")
print(f"{student2.name} is enrolled: {student2.is_enrolled}")


#defining the Dog class with an __init__ method and a get_info method
class Dog:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def get_info(self):
        print(f"{self.name} is {self.age} years old.")
dog1 = Dog("Rocky", 3)
dog2 = Dog("Moti", 5)
dog1.get_info() 
dog2.get_info()

# Creating the Class
class Dog:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def bark(self):
        print(f"{self.name} says Woof!")
dog1 = Dog("Rocky", 3)
dog2 = Dog("Moti", 5)

print(f"Dog 1's name is: {dog1.name}")
print(f"Dog 2's age is: {dog2.age}")
dog1.bark()


# Defining the Employess class with properties and methods
class Employee:
    def __init__(self, name, position, salary):
        self.name = name          
        self.position = position  
        self.salary = salary      

    def display_info(self):
        print(f"Employee Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")
emp1 = Employee("Ram", "Developer", 70000)
emp2 = Employee("Sham", "Designer", 85000)
emp1.display_info()
emp2.display_info()
