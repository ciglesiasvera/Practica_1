import random
secret_number = random.randint(1, 10)
#Ingresar número
print("\nAdivine el número entre 1 y 10, tiene sólo una oportunidad:")
number = int(input("Ingrese su número: "))
if number == secret_number :
    print("Felicitaciones, ha adivinado el número secreto")
else:
    print("¡Ha fallado! Será para la próxima...")