# Hierarchical Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Tom")
cat = Cat("Jerry")    

dog.display_name()
print(dog.speak())  # Output: Woof!
cat.display_name()
print(cat.speak())  # Output: Meow!