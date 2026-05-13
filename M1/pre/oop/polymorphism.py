# Polymorphism: the ability of an object to take on many forms

# Method Overriding
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

# Method Overloading (not natively supported in Python, but can be simulated)
from multipledispatch import dispatch
class Calculator:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

cal = Calculator()
print(cal.add(1, 2, 3))