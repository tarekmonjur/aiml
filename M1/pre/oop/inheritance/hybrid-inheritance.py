# Hybrid Inheritance

# Hybrid inheritance is a combination of two or more types of inheritance.
# This example combines Multilevel (Grandparent -> Parent -> Child) 
# and Multiple (Parent & Activity -> Child) inheritance.

class Grandparent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print("Name:", self.name)

    def display_age(self):
        print("Age:", self.age)

class Parent(Grandparent):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city

    def display_city(self):
        print("City:", self.city)

class Activity:
    def __init__(self, hobbies):
        self.hobbies = hobbies

    def display_hobbies(self):
        print("Hobbies:", ", ".join(self.hobbies))

class Child(Parent, Activity):
    def __init__(self, name, age, city, hobbies):
        # Calling specific parent constructors for clarity in hybrid structures
        Parent.__init__(self, name, age, city)
        Activity.__init__(self, hobbies)

    def display_info(self):
        self.display_name()
        self.display_age()
        self.display_city()
        self.display_hobbies()

child = Child("Muntasir", 25, "Dhaka", ["running", "football"])
child.display_info()
