from savings_account import SavingsAccount

def main():
    account1 = SavingsAccount("Roberto Hernandez", 1000)
    print(f"El nombre del titular es: {account1.name}")
    print(f"El saldo es: {account1.balance}")
    print(f"La tasa de interes es: ${account1.interest_rate * 100}%")
    
    account1.deposit(500)
    account1.withdraw(200)
    account1.apply_interest()
    
    print(f"El saldo es: ${account1._balance}")
    
if __name__ == "__main__":
    main()