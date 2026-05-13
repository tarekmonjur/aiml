# Factory Pattern
# The factory pattern is a design pattern that provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.
# It promotes loose coupling by eliminating the need to bind application-specific classes into the code.
# The factory pattern is often used when the exact type of object to be created is not known until runtime,
# or when the creation process is complex and needs to be centralized.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Unknown shape type")

shape1 = ShapeFactory.create_shape("circle")
shape1.draw()
shape2 = ShapeFactory.create_shape("rectangle")
shape2.draw()


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
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Stripe payment of {amount}")

class BDPaymentProcessorFactory:
    __processors = {
        "bkash": BkashPaymentProcessor,
        "rocket": RocketPaymentProcessor,
        "nagad": NagadPaymentProcessor
    }

    @staticmethod
    def create_payment_processor(processor_type):
        processor_class = BDPaymentProcessorFactory.__processors.get(processor_type)
        if processor_class:
            return processor_class()
        else:
            raise ValueError("Unknown payment processor type")


class InternationalPaymentProcessorFactory:
    __processors = {
        "paypal": PaypalPaymentProcessor,
        "stripe": StripePaymentProcessor
    }

    @staticmethod
    def create_payment_processor(processor_type):
        processor_class = InternationalPaymentProcessorFactory.__processors.get(processor_type)
        if processor_class:
            return processor_class()
        else:
            raise ValueError("Unknown payment processor type")


payment_processor = BDPaymentProcessorFactory.create_payment_processor("rocket")
payment_processor.process_payment(1000)

payment_processor = InternationalPaymentProcessorFactory.create_payment_processor("paypal")
payment_processor.process_payment(2000)