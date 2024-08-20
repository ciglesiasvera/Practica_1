# Recorriendo una lista
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("si está la manzana")
# Recorriendo una cadena de texto
message = "Hola desde Chile con temporal"
if "Chile" in message:
    print("Si está la palabra Chile")
# tupla  
numeros = (1, 2, 3, 4, 5)
if 3 in numeros:
    print("El número 3 está en la tupla.")
    
# cojuntos   
colores = {"rojo", "verde", "azul"}
if "verde" in colores:
    print("El color verde está en el conjunto.")

estudiante = {"nombre":"roberto","edad":20}   
# Diccionario
if "edad" in estudiante:
    print("La clave 'edad' está en el diccionario.")
    
# Comprobación Negativa
nombres = ["Ana", "Luis", "Carlos"]
if "Juan" not in nombres:
    print("Juan no está en la lista.")   

# Uso en Bucles
for letra in "python":
    if letra in "aeiou":
        print(f"{letra} es una vocal.")  