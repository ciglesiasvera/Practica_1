from account import Account

class SavingsAccount(Account):
    def __init__(self, name, balance = 0, interest_rate = 0.02):
        super().__init__(name, balance)
        self._interest_rate = interest_rate
        
    @property
    def interest_rate(self):
        return self._interest_rate
    
    @interest_rate.setter
    def interest_rate(self, rate):
        if rate < 0:
            print("La tasa de interes no puede ser negativa")
        else:
            self._interest_rate = rate
            
    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interes aplicado ${interest}, tu nuevo saldo es: ${self._balance}")