# Ingresar datos
nombre1 = input("Ingresa el nombre de la primera persona: ")
edad1 = int(input("Ingresa la edad de la primera persona: "))
altura1 = int(input("Ingresa la altura de la primera persona: "))
nombre2 = input("Ingresa el nombre de la segunda persona: ")
edad2 = int(input("Ingresa la edad de la segunda persona: "))
altura2 = int(input("Ingresa la altura de la segunda persona: "))
nombre3 = input("Ingresa el nombre de la tercera persona: ")
edad3 = int(input("Ingresa la edad de la tercera persona: "))
altura3 = int(input("Ingresa la altura de la tercera persona: "))
cantP = 3
promedioE = ((edad1 + edad2 + edad3)/cantP)
promedioA = ((altura1 + altura2 + altura3)/cantP)

print(f"Nombre 1: {nombre1}, Edad 1: {edad1}, Altura 1: {altura1}")
print(f"Cantidad de caracteres del nombre 1: {len(nombre1)}")
print(f"Nombre 2: {nombre2}, Edad 2: {edad2}, Altura 2: {altura2}")
print(f"Cantidad de caracteres del nombre 2: {len(nombre2)}")
print(f"Nombre 3: {nombre3}, Edad 3: {edad3}, Altura 3: {altura3}")
print(f"Cantidad de caracteres del nombre 3: {len(nombre3)}")
#print(f"Promedio de edad: " + promedio)
print(f"Promedio de edad: {promedioE:.2f}")
print(f"Promedio de alturas: {promedioA:.2f}")

"""[11:56] Roberto Hernandez
a=int(input("ingresa un valor"))
b=float(input("ingresa otro valor"))"""
 

"""# Imprimir Resultados
print("\nResultados:")
# Imprimir los resultados
print(f"Promedio de edades: {promedio_edades:.2f}")
print(f"Promedio de alturas: {promedio_alturas:.2f} metros")
print(f"Total de caracteres en los nombres: {total_caracteres_nombres}")"""