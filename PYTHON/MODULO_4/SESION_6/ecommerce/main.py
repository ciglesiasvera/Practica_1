from cart import Cart
from product import Product

""" try:
    
except ValueError as e:
    print(f"Error: {e}") """

product1 = Product("Laptop", 1000, 5)
product2 = Product("Smartphone", 500, 10)
product3 = Product("Tablet", 800, 15)
product4 = Product("Dron", 1500, 3)


carrito = Cart()

carrito.add_products(product1, 2)
carrito.add_products(product1, 2)
carrito.add_products(product2, 1)
carrito.add_products(product3, 1)
carrito.add_products(product4, 1)
carrito.add_products(product4, 1)
carrito.add_products(product4, 1)


carrito.show_cart()

carrito.remove_products("Smartphone")

carrito.show_cart()
