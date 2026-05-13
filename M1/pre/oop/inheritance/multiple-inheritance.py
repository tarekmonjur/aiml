# Multiple Inheritance

class Grandparent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print("Name:", self.name)

    def display_age(self):
        print("Age:", self.age)

class Parent:
    def __init__(self, city):
        self.city = city

    def display_city(self):
        print("City:", self.city)

class Child(Grandparent, Parent):
    def __init__(self, name, age, city, hobbies):
        Grandparent.__init__(self, name, age)
        Parent.__init__(self, city)
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