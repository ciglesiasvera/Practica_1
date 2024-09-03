#cOPIAR EL CONTENIDO DE UN ARCHIVO A OTRO
def copiar_archivo(archivo_origen,archivo_destino):
    try:
        with open(archivo_origen, "r") as origen:
            contenido = origen.read
    #Abrir el archivo en modo escritura
        with open(archivo_destino, "w") as destino:
            destino.write(contenido)
    except FileNotFoundError:
            print(f"El archivo {archivo_destino} no existe")
            
#Contar palabras de un archivo
def contar_palabra(archivo):
    try:
        with open(archivo, "r") as f:
            contenido = f.read()
            palabras = contenido.spli()
            print(f"El archivo: {archivo} contiene {len(palabras)} palabras")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe")
            
#Main
copiar_archivo("PYTHON\MODULO_4\SESION_8\files\ejemplo.txt", "PYTHON\MODULO_4\SESION_8\files\ejemplo2.txt")
contar_palabra("PYTHON\MODULO_4\SESION_8\files\ejemplo.txt")