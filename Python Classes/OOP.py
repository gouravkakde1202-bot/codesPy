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
