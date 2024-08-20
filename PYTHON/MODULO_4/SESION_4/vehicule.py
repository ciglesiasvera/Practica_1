from car import Car

class vehicule(Car):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    def door_open(self):
        print(f"El auto {self.brand} {self.model} con {self.doors} puertas abiertas")