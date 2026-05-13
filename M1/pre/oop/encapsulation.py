# Encapsulation

class Parent:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name  # Public method to access private attribute

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age  # Private attribute

    def get_age(self):
        Parent.__name = "Changed Name"  # Attempting to modify private attribute (will not affect the original __name in Parent)
        return self.__age  # Public method to access private attribute

ch = Child("Alice", 10)
print(ch.get_name())  # Accessing private attribute through public method
ch.__name = "Bob"  # Attempting to modify private attribute directly (will not change the original)
print(ch.get_name())  # Still prints "Alice" because __name is private and cannot be modified directly
ch.__age = 15  # Attempting to modify private attribute directly (will not change the original)
print(ch.get_age())  # Accessing age through public method