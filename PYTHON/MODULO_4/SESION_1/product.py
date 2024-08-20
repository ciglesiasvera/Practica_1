class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def show(self):
        return f"The product is: {self.name}, \nPrice: {self.price}, \nQuantity: {self.quantity}"
    
    def add_stock(self, quantity):
        self.quantity += quantity
        print(f"{self.quantity} units was added of the product {self.name}")
        
    def sell(self, quantity):
        if quantity > self.quantity:
            print(f"There are not enough products of {self.product}, there are only {self.quantity}")
        else:
            self.quantity -= quantity
            print(f"{quantity} units of the product {self.name} have been sold and remain in stock {self.quantity}")
            
#Main
product1 = Product("Apple", 100, 50)
product2 = Product("Onion", 600, 20)
product3 = Product("Potato", 50, 100)

print(product1.show())
print(product2.show())
print(product3.show())
product1.add_stock(5)
print(product1.show())
product2.sell(10)
print(product2.show())
product3.sell(1)
print(product3.show())