class AgeOutOfRangeError(Exception):
    def __init__(self, age, message = "La edad no se encuentra dentro del rango permitido"):
        self.age = age
        self.message = message
        super().__init__(f"{message} Edad recibida: {age}")
        
def verify_age(age):
    if age < 18 or age > 65:
        raise AgeOutOfRangeError(age)
    else:
        print(f"Edad valida: {age}")
        
#Main
try:
    age = 50
    verify_age(age)
except AgeOutOfRangeError as e:
    print({e})
        
    
    
    