class Car:
  
  def __init__(self, make = "Ferrari", model = "488 GTB", year = 2026):
    self.make = make
    self.model = model
    self.year = year

  def display_info(self): # instance method
    print(f"Car: {self.make}, {self.model}, ({self.year})")  


car = Car()
car.display_info()