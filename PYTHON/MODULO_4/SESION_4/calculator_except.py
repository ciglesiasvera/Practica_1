def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Error: Entrada no valida")

def make_operation(a, b, operator):
    try:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Error: no se puede dividir por cero")
            return a / b
        else:
            raise ValueError("Operacion no valida")
        
    except ValueError as e:
        print(e)
        return None
    
# Main
num1 = get_number("Ingresa el primer numero: ")
num2 = get_number("Ingresa el segundo numero: ")
operation = input("Selecciona la operación a ejecutar (+, -, *, /): ")
result = make_operation(num1, num2, operation)

print(f"El resultado de {num1} {operation} {num2} es : {result}")