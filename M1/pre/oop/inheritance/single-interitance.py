# Single Inheritance

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print("Name:", self.name)

    def display_age(self):
        print("Age:", self.age)

class Child(Parent):
    def __init__(self, name, age, hobbies):
        super().__init__(name, age)
        self.hobbies = hobbies

    def display_hobbies(self):
        print("Hobbies:", self.hobbies)

    def display_info(self):
        self.display_name()
        self.display_age()
        self.display_hobbies()    

single = Child("Muntasir", 25, ["running", "football"])
single.display_info()