class ErrorInvalidAge(Exception):
    pass

def verifyAge(age):
    if age < 18:
        raise ValueError(" Para registrase debe ser mayor de 18 anios")
    return "Registro exitoso"
try:
    message = verifyAge(18)
    print(message)
except ValueError as e:
    print(f"Error{e}")