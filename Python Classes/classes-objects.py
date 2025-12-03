# Defining the Car class
class Car:
    category = "Vehicle"
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start_engine(self):
        print(f"The {self.color} {self.brand}'s engine is starting.")
my_car = Car("Toyota", "Red")
your_car = Car("Honda", "Blue")

print(f"My car is a {my_car.color} {my_car.brand}.")

your_car.start_engine()
