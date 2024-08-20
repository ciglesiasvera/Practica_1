class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def run(self):
        print("El vehiculo {self.brand}, con modelo {self.model} ha arrancado")
    def stop(self):
        print("El vehiculo {self.brand}, con modelo {self.model} se ha detenido")
        
