class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        return f"El nombre es: {self.name} y tiene {self.age} años"
class Employe(Person):
    def __init__(self, name, age, income):
        super().__init__(name, age)
        self.income = income
        
    def description(self):
        return f"{super().description()} y gana {self.income} pesos al mes"
    
#Main
employe = Employe("Robert", 38, 500000)
print(employe.description)