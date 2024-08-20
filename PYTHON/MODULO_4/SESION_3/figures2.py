class Figure:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        pass

class Square(Figure):
    @property
    def perimeter(self):
        return self.side * 4
    
class Pentagon(Figure):
    @property
    def perimeter(self):
        return self.side * 5
    
class Hexagon(Figure):
    @property
    def perimeter(self):
        return self.side * 6

class Octagon(Figure):
    @property
    def perimeter(self):
        return self.side * 8
    
# Function to get the side value
def get_side():
    while True:
        try:
            side = float(input("Ingresa el valor del lado: "))
            if side > 0:
                return side
            else:
                print("El valor del lado debe ser positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Asking the side value
side = get_side()

# Creating an object with the side value
square = Square(side)
pentagon = Pentagon(side)
hexagon = Hexagon(side)
octagon = Octagon(side)

# Creating an object with the side value
square = Square(5)
pentagon = Pentagon(5)
hexagon = Hexagon(5)
octagon = Octagon(5)

# Printing perimeters using properties
print(f"Cuadrado: Perimetro = {square.perimeter}")
print(f"Pentagono: Perimetro = {pentagon.perimeter}")
print(f"Hexagono: Perimetro = {hexagon.perimeter}")
print(f"Octagono: Perimetro = {octagon.perimeter}")