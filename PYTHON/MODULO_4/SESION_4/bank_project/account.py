class Account:
    def __init__(self, name, balance = 0):
        self._name = name #Protected attribute
        self._balance = balance #Protected attribute
        
    @property
    def name(self):
        return self._name
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("El monto no puede ser negativo o 0")
        else:
            self._balance = amount
            
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Se ha depositado ${amount}. Su nuevo saldo es: ${self.balance}")
        else:
            print("La cantidad ha depositar debe ser positiva")
            
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Se han retirado ${amount}, su nuevo saldo es: ${self._balance}")
        else:
            print("Fondos insuficientes")