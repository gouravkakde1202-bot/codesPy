# Defining the Student class with an __init__ method
class Student:
    def __init__(self, name, student_id): 
        print("A new student object is being created!")
        self.name = name          
        self.student_id = student_id
        self.is_enrolled = True
student1 = Student("Alok", 101)
student2 = Student("Priya", 102)

print(f"{student1.name}'s ID is {student1.student_id}")

print(f"{student2.name} is enrolled: {student2.is_enrolled}")