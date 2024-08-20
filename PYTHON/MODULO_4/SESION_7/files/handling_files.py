#Sobreewscribir archivo txt
with open('PYTHON/MODULO_4/SESION_7/files/ejemplo.txt', "w") as file:
    file.write("Hola desde Temuco\n")
    file.write("Esta es una linea nueva\n")
    file.write("Por aca paso Cristian\n")
    file.write("Esta rebueno esto")
    
#Leer archivo
with open('PYTHON/MODULO_4/SESION_7/files/ejemplo.txt', "r") as reading:
    content = reading.read()
    print(content)
    
#agregando un texto al final
with open('PYTHON/MODULO_4/SESION_7/files/ejemplo.txt', "a") as f:
    f.write("\nEsta linea se esta agregando al final")
    
#Leer archivo
with open('PYTHON/MODULO_4/SESION_7/files/ejemplo.txt', "r") as reading:
    content = reading.read()
    print(content)