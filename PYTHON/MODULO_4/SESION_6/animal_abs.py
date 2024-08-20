from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "guau"
    
class Cat(Animal):
    def sound(self):
        return "miau"
    
class Pig(Animal):
    def sound(self):
        return "oink"
    def eat(self):
        return "comiendo"
    
#Main
dog = Dog()
cat = Cat()
pig = Pig()

print(dog.sound())
print(cat.sound())
print(pig.sound())
print(pig.eat())