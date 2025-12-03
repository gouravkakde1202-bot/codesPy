# Defining the Employess class with properties and methods
class Employee:
    def __init__(self, name, position, salary):
        self.name = name          
        self.position = position  
        self.salary = salary      

    def display_info(self):
        print(f"Employee Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")
emp1 = Employee("Ram", "Developer", 70000)
emp2 = Employee("Sham", "Designer", 65000)
emp1.display_info()
emp2.display_info()
