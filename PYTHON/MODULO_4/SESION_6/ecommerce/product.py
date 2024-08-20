# exceptions.py
class InsufficientStockError(Exception):
    """Excepción lanzada cuando no hay suficiente stock para un producto."""
    pass

class Product:
    def __init__(self, name, price, quantity_in_stock):
        self.__name = name #private attribute
        self.__price = price #private attribute
        self.__quantity_in_stock = quantity_in_stock #private attribute
        
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock
    
    # Setting using properties
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__price = value
        
    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity):
        if quantity < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.__quantity_in_stock = quantity
        
    def reduce_stock(self, quantity):
        if quantity > self.__quantity_in_stock:
            raise InsufficientStockError("Stock insuficiente para la cantidad solicitada")
        self.__quantity_in_stock -= quantity