import json

# Abrir y cargar el archivo JSON
with open("PYTHON/MODULO_4/SESION_9/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
# Acceder a los valores del JSON
name = data["name"]
age = data["age"]
hobbies = data["hobbies"]
email = data["email"]
work = data["work"]

# Imprimir los valores
print(f"Nombre: {name}")
print(f"Edad: {age}")
print(f"Hobbies: {hobbies}")
print(f"Correo: {email}")

# Mostrar los datos de trabajo
print("-------Información de empleo-------")
print(f"Empresa: {work['enterprise']}")
print(f"Rol: {work['role']}")
print(f"Años de experiencia: {work['years']}")