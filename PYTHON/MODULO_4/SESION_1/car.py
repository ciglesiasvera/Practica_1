class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def description(self):
        return f"Car: {self.brand} ,\nModel: {self.model}, \nYear: {self.year}"
    
    def start(self):
        return f"The car, {self.brand} {self.model}, is starting"

#Main
my_car = Car("Ford", "Explorer", 1995)

print(my_car.description())
print(my_car.start())

class Bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def show_detail(self):
        return f"Bike: {self.brand} ,\nModel: {self.model}, \nYear: {self.year}"
    
    def starting(self):
        return f"The bike, {self.brand} {self.model}, is starting"

#Main    
my_bike = Bike("Yamaha", "XR", 2005)
my_bike2 = Bike("Ducatti", "Multiestraba", 2020)

print(my_bike.show_detail())
print(my_bike.starting())

print(my_bike2.show_detail())
print(my_bike2.starting())