from abc import ABC, abstractmethod

class PayMethod(ABC):
    @abstractmethod
    def pay_process(self, quantity):
        pass
    
# Child clas to process credit card payments
class CreditCardPayment(PayMethod):
    def pay_process(self, quantity):
        print(f"Procesando un pago con tarjeta de credito de {quantity}")
    def card_number_validation(self, cardNumber):
        print(f"Validando numero de tarjeta de {cardNumber}")   

# Child class to process paypal payments           
class PaypalPayment(PayMethod):
    def pay_process(self, quantity):
        print(f"Procesando un pago con PayPal de ${quantity}")
        
# Child class to process cryto paymants
class CryptoPayment(PayMethod):
    def pay_process(self, quantity):
        print(f"Procesando un pago con Crypto de ${quantity}")
        
def make_payment(payment_method, quantity):
    payment_method.pay_process(quantity)
    
# Main
payment1 = CreditCardPayment()
payment2 = PaypalPayment()
payment3 = CryptoPayment()
payment1.card_number_validation("123456")

make_payment(payment1, 100)
make_payment(payment2, 500)
make_payment(payment3, 700)