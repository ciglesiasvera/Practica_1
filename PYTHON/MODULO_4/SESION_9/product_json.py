import json
# Read file
def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
    
# Write the json file
def write_json(filename, jsdata):
    with open(filename, "w", encoding="utf-8") as file:
        data = json.dump(jsdata, file, indent = 4)

# Adding a product
def add_product(data, product):
    data["products"].append(product)
    
# Update products quantity
def update_product(data, product_id, new_quatity):
    for product in data["products"]:
        if product["id"] == product_id:
            product["quantity"] = new_quatity
            break
        
# Delete a product
def remove_product(data, product_id):
    data["products"] = [product for product in data ['products'] if product["id"] != product_id]
    
# Show product
def show_products(data):
    print("Lista de productos: ")
    for product in data["products"]:
        print(f"ID: {product["id"]}, Precio: {product['price']}, Nombre: {product.get('name', 'N/A')}, Cantidad: {product.get('quantity')}")
        
#Main
filename = "PYTHON/MODULO_4/SESION_9/products.json"
data = read_json(filename)
show_products(data)

update_product(data, 2, 30)
show_products(data)
remove_product(data, 1)
show_products(data)
write_json(filename, data)

new_product = {"id": 4, "name": "Taza", "price": 10, "quantity": 5}
add_product(data, new_product)
write_json(filename, data)