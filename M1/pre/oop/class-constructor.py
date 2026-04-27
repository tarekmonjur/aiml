# ----------- default constructor -----------
class Car1:
  def __init__(self): # dunder method, constructor method
    self.make = ""
    self.model = ""
    self.year = 0

car1 = Car1()
car1.make = "Toyota"
car1.model = "Camry"
car1.year = 2020
print(f"Car 1: {car1.make}, {car1.model}, ({car1.year})")

# ----------- parameterized constructor -----------
class Car2:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

car2 = Car2("Honda", "Civic", 2021)
print(f"Car 2: {car2.make}, {car2.model}, ({car2.year})")

# ----------- default value constructor -----------
class Car3:
  def __init__(self, make = "Ferrari", model = "488 GTB", year = 2026):
    self.make = make
    self.model = model
    self.year = year

car3 = Car3()
print(f"Car 3: {car3.make}, {car3.model}, ({car3.year})")

# ----------- multiple constructors -----------
class Car:

  def __init__(self):
    self.make = ""
    self.model = ""
    self.year = 0

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def __init__(self, make = "Ferrari", model = "488 GTB", year = 2026):
    self.make = make
    self.model = model
    self.year = year

car4 = Car()
print(f"Car 4: {car4.make}, {car4.model}, ({car4.year})")

car5 = Car("Lamborghini", "Huracan", 2022)
print(f"Car 5: {car5.make}, {car5.model}, ({car5.year})")
