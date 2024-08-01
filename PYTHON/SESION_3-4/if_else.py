x = int(input("Ingrese un número x: "))
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")
    
y = int(input("Ingrese un número y: "))
if y < 10:
    print("y es menor que 10")
elif y == 10:
    print("y es igual a 10")
elif y < 20:
    print("y es mayor que 10, pero menor que 20")
else:
    print("y es mayor que 20")
    
age = int(input("Ingrese su edad: "))
if age < 18 :
    print("Debe ser mayor de 18 años para registrarse")
elif 18 <= age <= 120 :
    print("Registro exitoso. Bienvenido")
else :
    print("Edad no válida. Por favor ingresa una edad correcta")