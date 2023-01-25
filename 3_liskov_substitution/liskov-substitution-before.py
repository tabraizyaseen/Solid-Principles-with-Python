"""
Defination:
    Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.

Simplification:
    Every subclass or derived class should be substitutable(capable of being exchanged for another or for something else that is equivalent) 
    for their base or parent class.

PaypalPaymentProcessor requires email address instead of security_code 
"""

from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total



class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Using email address: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor()
processor.pay(order, "hi@arjancodes.com")