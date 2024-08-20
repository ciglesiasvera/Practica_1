class Figures:
    def calculate_area():
        pass
    
class Square:
    def perimeter(self, side):
        return side * 4
class Pentagon:
    def perimeter(self, side):
        return side * 5
class Exagon:
    def perimeter(self, side):
        return side * 6
class Octagon:
    def perimeter(self, side):
        return side * 8
    
square = Square()
pentagon = Pentagon()
exagon = Exagon()
octagon = Octagon()
print(square.perimeter(5))
print(pentagon.perimeter(5))
print(exagon.perimeter(5))
print(octagon.perimeter(5))