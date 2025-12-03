# Defining the Dog class with an __init__ method and a get_info method
class Dog:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def get_info(self):
        print(f"{self.name} is {self.age} years old.")
dog1 = Dog("Rocky", 23)
dog2 = Dog("Moti", 25)
dog1.get_info() 
dog2.get_info() 
