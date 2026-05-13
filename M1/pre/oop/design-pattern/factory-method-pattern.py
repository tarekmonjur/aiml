# Factory Pattern
# The factory pattern is a design pattern that provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.
# It promotes loose coupling by eliminating the need to bind application-specific classes into the code.
# The factory pattern is often used when the exact type of object to be created is not known until runtime,
# or when the creation process is complex and needs to be centralized.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class BkashPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Bkash payment of {amount}")

class RocketPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Rocket payment of {amount}")

class NagadPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Nagad payment of {amount}")

class PaypalPaymentProcessor(PaymentProcessor):
    def check_payment(self, amount):
        print(f"Checking PayPal payment of {amount}")

    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class StripePaymentProcessor(PaymentProcessor):
    def check_payment(self, amount):
        print(f"Checking Stripe payment of {amount}")

    def process_payment(self, amount):
        print(f"Processing Stripe payment of {amount}")


class PaymentProcessorFactory(ABC):

    def create_payment_processor(self):
        processor_class = self._processors.get(self.payment_type)
        if processor_class:
            return processor_class()
        else:
            raise ValueError("Unknown payment processor type")

    @abstractmethod
    def make_payment(amount):
        pass


class BDPaymentProcessorFactory(PaymentProcessorFactory):
    _processors = {
        "bkash": BkashPaymentProcessor,
        "rocket": RocketPaymentProcessor,
        "nagad": NagadPaymentProcessor
    }

    def __init__(self, payment_type):
        self.payment_type = payment_type


    def make_payment(self, amount):
        processor = self.create_payment_processor()
        processor.process_payment(amount)
        return processor

class InternationalPaymentProcessorFactory(PaymentProcessorFactory):
    _processors = {
        "paypal": PaypalPaymentProcessor,
        "stripe": StripePaymentProcessor
    }

    def __init__(self, payment_type):
        self.payment_type = payment_type

    def make_payment(self, amount):
        processor = self.create_payment_processor()
        processor.check_payment(amount)
        processor.process_payment(amount)
        return processor

payment_processor = BDPaymentProcessorFactory("bkash")
payment_processor.make_payment(1000)     

payment_processor = InternationalPaymentProcessorFactory("stripe")
payment_processor.make_payment(2000)  