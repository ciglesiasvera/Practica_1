class Dog:
    def __init__(self, name, dog_breed):
        self.name = name
        self.dog_breed = dog_breed
        
    def bark(self):
        print(f"The dog {self.name}, bark like this Guau Guau, an the dog breed is {self.dog_breed}")
        
    def eat(self):
        print(f"The dog {self.name}, is eating a bone")
        
    def walk(self):
        print(f"The dog {self.name}, is walking")
        
#Main
dog = Dog("Bono", "Belgian Shepard")
dog.bark()
dog.eat()
dog.walk()