from libro import Libro
from revista import Revista
from periodico import Periodico

def main():
    # Creando instancias de las clases
    libro = Libro("El Hobbit", "J.R.R. Tolkien", 1937, 310)
    revista = Revista("National Geographic", "Varios", 2023, 800)
    periodico = Periodico("El Pais", "Varios", 2024, "15-08-2024")
    
    # Imprimiendo la información de cada material
    print(libro.informacion())
    print(revista.informacion())
    print(periodico.informacion())

# Ejecutar el main
if __name__ == "__main__":
    main()