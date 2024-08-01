# Vas a crear un programa para obter informacion de un contacto. El programa debe:
# Obtener información del contacto desde la consola.
# Almacenar la información en un diccionario.
# Realizar algunas operaciones básicas con los datos almacenados.
# Los datos son nombre, correo y telefono
#calcular el len de los caracteres del nombre del contacto
#imprimir la informacion completa del contacto
#######################
# Ingresar datos
nombre = input("Ingresa el nombre: ")
correo = input("Ingresa el correo: ")
telefono = input("Ingresa el teléfono: ")

persona = {"nombre": nombre, "correo": correo, "teléfono": telefono}

# Calcular el número de caracteres del nombre del contacto
longitud_nombre = len(persona["nombre"])

# Imprimir la información completa del contacto
print("\nInformación del contacto:")
print(f"nombre: {persona['nombre']}")
print(f"correo: {persona['correo']}")
print(f"teléfono: {persona['teléfono']}")
print(f"Número de caracteres del nombre: {longitud_nombre}")