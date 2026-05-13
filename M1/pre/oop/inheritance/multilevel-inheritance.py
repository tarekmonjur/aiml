# Multilevel Inheritance

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

class Child(Parent):
    def __init__(self, name, age, city, hobbies):
        super().__init__(name, age, city)
        self.hobbies = hobbies

    def display_hobbies(self):
        print("Hobbies:", self.hobbies)

    def display_info(self):
        self.display_name()
        self.display_age()
        self.display_city()
        self.display_hobbies()


child = Child("Muntasir", 25, "Dhaka", ["running", "football"])
child.display_info()