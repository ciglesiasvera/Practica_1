# hacer clase vehiculo que tenga los metodos moverse y describirse
# clase hija, moto, auto, bicicleta
# todas las clase hija deber un metodo propio
# usando abstracion y herencia

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def __init__(self, distance, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.distance = distance
    def move(self):
        pass
    def detail(self):
        pass
    
class Motorbike(Vehicle):
    def __init__(self, distance, brand, model, year, color):
        super().__init__(distance, brand, model, year, color)
    def move(self, distance):
        print(f"La moto avanzo {distance} kilometros")
    def detail(self, brand, model, year, color):
        print(f"La moto marca {brand}, modelo {model}, anio {year} y de color {color}")
    def accelerate(self, fast):
        print(f"La moto esta acelerando de 0 a 100 en {fast} segundos")
        
class Car(Vehicle):
    def __init__(self, distance, brand, model, year, color):
        super().__init__(distance, brand, model, year, color)
    def move(self, distance):
        print(f"El auto avanzo {distance} kilometros")
    def detail(self, brand, model, year, color):
        print(f"La moto marca {brand}, modelo {model}, anio {year} y de color {color}")
    def brake(self, abs):
        print(f"El auto necesito {abs} metros para frenar")
        
class Bicycle(Vehicle):
    def __init__(self, distance, brand, model, year, color):
        super().__init__(distance, brand, model, year, color)
    def move(self, distance):
        print(f"La bicicleta avanzo {distance} kilometros")
    def detail(self, brand, model, year, color):
        print(f"La bicicleta marca {brand}, modelo {model}, anio {year} y de color {color}")
    def jump(self, meters):
        print(f"La bicicleta salto {meters} metros")
        
# Main
motorbike = Motorbike(100, "Honda", "100", 2022, "Azul")
car = Car(500, "Toyota", "yaris", 2020, "Verde")
bicycle = Bicycle(50, "Trek", "M", 2023, "Amarillo")

motorbike.move(100)
motorbike.detail("Honda", "100", 2020, "red")
car.move(200)
car.brake(20)
bicycle.move(50)
bicycle.detail("Trek", "M", 2023, "Amarillo")
bicycle.jump(4)
car.detail("Toyota", "yaris", 2020, "Verde")
motorbike.accelerate(3)
