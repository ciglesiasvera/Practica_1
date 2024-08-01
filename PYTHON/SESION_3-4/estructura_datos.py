#lista(list)
frutas=["Tunas","Guayabas","Maracuya"]
numerosPrimos=[3,5,7,11]
print(type(frutas))
print(type(numerosPrimos))
print(frutas[0])
print(numerosPrimos[2])
frutas[0]="Mango"
print(frutas)
frutas.append("Lichi") #Método para agregar un elemento a una lista
print(frutas)
# Buscar la posición de un elemento en la lista de frutas
elemento = "Guayabas"
if elemento in frutas:
    posicion = frutas.index(elemento)
    print(f"La posición de '{elemento}' en la lista de frutas es: {posicion}")
else:
    print(f"'{elemento}' no se encuentra en la lista de frutas.")
# Contar la cantidad de de caracteres de un elemento en la lista de frutas
# Tupla
dimensiones = (1920,1080)
coordenadas = (10,20)
print(type(dimensiones))
print(type(coordenadas))

puntos = (10,20)
#puntos[1] = 30
#No se puede asignar un nuevo valor a una tupla

# Conjuntos
colores = {"rojo", "verde", "blanco", "rojo"}
numeros_unicos = {1, 2, 3, 4, 5}
print(type(colores))
print(type(numeros_unicos))
numeros_unicos.add(6) #método para agregar un elemento al conjunto
print(numeros_unicos)
colores.remove("blanco") #método para remover un elemento de un conjunto
print(colores)
print(len(numeros_unicos))
print(len(colores))

#Diccionarios
personas = {"nombre": "Ana", "edad": 30, "ciudad": "Temuco"}
precios = {"manzana": 12, "banana": 5, "cerezas": 2.5}
print(type(personas))
print(type(precios))
print(personas["nombre"])
print(precios["manzana"])

personas["edad"] = 31 #modificando un valor
print(personas)
personas["ocupacion"] = "Programador"
print(personas)