#the inner class and create an object of it inside the outer class 
class OuterClass:
    class InnerClass:
        def __init__(self, value):
            self.value = value

    def __init__(self, inner_value):
        self.inner_object = self.InnerClass(inner_value)
outer_object = OuterClass("Hello, Inner Class!")
print(outer_object.inner_object.value) 

class Car:
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower

    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = self.Engine(horsepower)
my_car = Car("Toyota", "Camry", 200)
print(f"My car is a {my_car.make} {my_car.model} with {my_car.engine.horsepower} HP.")
# Output: My car is a Toyota Camry with 200 HP.

#Another example-2 of inner class
class University:
    class Department:
        def __init__(self, name):
            self.name = name

    def __init__(self, uni_name, dept_name):
        self.uni_name = uni_name
        self.department = self.Department(dept_name)
my_university = University("ABC University", "Computer Science")
print(f"{my_university.uni_name} has a {my_university.department.name} department.")
# Output: ABC University has a Computer Science department.

#Another example-3 of inner class
class Library:
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
    def __init__(self, name, book_title, book_author):
        self.name = name
        self.book = self.Book(book_title, book_author)
my_library = Library("City Library", "1984", "George Orwell")
print(f"{my_library.name} has the book '{my_library.book.title}' by {my_library.book.author}.")
# Output: City Library has the book '1984' by George Orwell.

#Another example-4 of inner class
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

    def __init__(self, company_name, emp_name, emp_position):
        self.company_name = company_name
        self.employee = self.Employee(emp_name, emp_position)   
my_company = Company("TechCorp", "Alice", "Developer")
print(f"{my_company.company_name} employs {my_company.employee.name} as a {my_company.employee.position}.")
# Output: TechCorp employs Alice as a Developer.

#Another example-5 of inner class
class School:
    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade

    def __init__(self, school_name, student_name, student_grade):
        self.school_name = school_name
        self.student = self.Student(student_name, student_grade)
my_school = School("Greenwood High", "Bob", "10th Grade")
print(f"{my_school.school_name} has a student named {my_school.student.name} in {my_school.student.grade}.")
# Output: Greenwood High has a student named Bob in 10th Grade.

#Another example-6 of inner class
class Hospital:
    class Patient:
        def __init__(self, name, ailment):
            self.name = name
            self.ailment = ailment

    def __init__(self, hospital_name, patient_name, patient_ailment):
        self.hospital_name = hospital_name
        self.patient = self.Patient(patient_name, patient_ailment)
my_hospital = Hospital("City Hospital", "Charlie", "Flu")
print(f"{my_hospital.hospital_name} is treating {my_hospital.patient.name} for {my_hospital.patient.ailment}.")
# Output: City Hospital is treating Charlie for Flu.

