class Animal:
#   def __init__(self, name):
#       self.name = name """
        
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Guau!"
    
class Cat(Animal):
    def make_sound(self):
        return "Miau!"
    
class Cow(Animal):
    def make_sound(self):
        return "Muuu!"
    
def animal_sound(animal):
    print(animal.make_sound())
    
dog = Dog()
cat = Cat()
cow = Cow()
""" print(dog.name)
animal_sound(dog)
animal_sound(cat)
animal_sound(cow) """
animals = [Dog(), Cat(), Cow(), Dog(), Cow()]
for animal in animals:
    animal_sound(animal)