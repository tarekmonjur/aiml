# Singleton Design Pattern
# The singleton design pattern is a software design pattern that restricts the instantiation of a class to a single instance and provides a global point of access to that instance.
# This is useful when exactly one object is needed to coordinate actions across the system.

class Singleton:
    __instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        # __init__ always runs after __new__, so we use a flag to prevent re-initialization
        if not getattr(self, '_initialized', False):
            self.name = name
            self._initialized = True

s1 = Singleton('Alice')
s2 = Singleton('Bob')
print(f"s1 name: {s1.name}")
print(f"s2 name: {s2.name}") # Will still be 'Alice' because of Singleton pattern