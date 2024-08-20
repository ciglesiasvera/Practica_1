# exceptions.py
class InsufficientStockError(Exception):
    """Excepción lanzada cuando no hay suficiente stock para un producto."""
    pass

class Cart:
    def __init__(self):
        self.products = {}

    def add_products(self, product, quantity):
        if product.name in self.products:
            self.products[product.name]["quantity"] += quantity
        else:
            self.products[product.name] = {"product": product, "quantity": quantity}

        try:
            product.reduce_stock(quantity)
        except InsufficientStockError as e:
            print(f"Error al agregar {product.name} al carrito: {e}")
            self.products[product.name]["quantity"] -= quantity

    def remove_products(self, product_name):
        if product_name in self.products:
            del self.products[product_name]

    def calculate_totals(self):
        total = 0
        for item in self.products.values():
            total += item["product"].price * item["quantity"]
        return total

    def show_cart(self):
        if not self.products:
            print("El carrito está vacío")
            return
        print("Carrito de compras:")
        for item in self.products.values():
            product = item["product"]
            quantity = item["quantity"]
            print(f"{product.name} - Cantidad: {quantity}, Precio: ${product.price}")
        print(f"Total: ${self.calculate_totals()}")
