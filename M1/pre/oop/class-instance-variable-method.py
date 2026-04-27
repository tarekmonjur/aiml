# ----------- Class variable vs Instance variable -----------
class Car:
  wheels = 4  # Class variable

  def __init__(self, make, model, year):
    self.make = make  # Instance variable
    self.model = model  # Instance variable
    self.year = year  # Instance variable

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(f"Car 1: {car1.make}, {car1.model}, ({car1.year}), Wheels: {car1.wheels}")
print(f"Car 2: {car2.make}, {car2.model}, ({car2.year}), Wheels: {car2.wheels}")

print('-'*100)

# Modifying class variable
Car.wheels = 6
print(f"Car 1: {car1.make}, {car1.model}, ({car1.year}), Wheels: {car1.wheels}")
print(f"Car 2: {car2.make}, {car2.model}, ({car2.year}), Wheels: {car2.wheels}")

print('-'*100)

# ----------- Class method vs Instance method -----------
class Vehicle:
  vehicle_type = "Car"  # Class variable
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def display_info(self):  # Instance method
    print(f"Vehicle: {self.make}, {self.model}, ({self.year})")

  @classmethod
  def vehicle_type(cls, vehicle_type):  # Class method
    cls.vehicle_type = vehicle_type
    print(f"This is a {cls.vehicle_type}.")

vehicle1 = Vehicle("Tesla", "Model S", 2022)
vehicle2 = Vehicle("Ford", "Mustang", 2021)
vehicle1.display_info()  # Calling instance method
Vehicle.vehicle_type("Electric Car")  # Calling class method
print(f"Vehicle 1 Type: {vehicle1.vehicle_type}")
print(f"Vehicle 2 Type: {vehicle2.vehicle_type}")
