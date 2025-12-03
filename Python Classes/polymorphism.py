# Different classes with the same method name demonstrating polymorphism
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")    
cat = Cat()
cow = Cow()
cat.sound()  
cow.sound()  
def animal_sound(animal):
    animal.sound()
animal_sound(cat)  
animal_sound(cow)  

animals = [Cat(), Cow()]
for animal in animals:
    animal.sound()  