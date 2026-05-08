# Composition
# Composition is a strong form of association where one class (the composite) contains another class (the component) as a part of its state. 
# The part object depends on the whole object for its existence. If the whole object is destroyed, the part object will also be destroyed.
# This means that if the composite(parent) is destroyed, the component(child) will also be destroyed.
# Concept:
# - Strong Relationship: It is a strong relationship between two classes.
# - Tight Coupling: The lifecycle of the component is tightly coupled with the lifecycle of the composite.
# - Lifecycle Dependency: The component cannot exist without the composite.
# - Has-a Relationship: One class has a reference to another class, and it owns it.

class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        print(f"Engine started with power: {self.power}")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self, name, make, power):
        self.name = name
        self.make = make
        self.engine = Engine(power)  # Composition: Car has an Engine

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def show_details(self):
        print(f"Car: {self.name}, Make: {self.make}, Engine Power: {self.engine.power}")    

car = Car("Camry", "Toyota", 200)
car.start()
car.show_details()
