# Aggregation
# Aggregation is a special form of association that represents a "whole-part" relationship between two classes.
# In an aggregation relationship, one class (the "whole"(parent)) contains a reference to another class (the "part"(child)), but the part can exist independently of the whole.
# This means that if the whole is destroyed, the part can still exist.
# Concept:
# - Weak Relationship: It is a weak relationship between two classes.
# - Has-a Relationship: One class has a reference to another class, but it does not own it.
# - Child can exist without parent: The part can exist without the whole.

class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, teachers):
        self.name = name
        self.teachers = teachers  # Aggregation: Department has a list of teachers

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_teachers(self):
        for teacher in self.teachers:
            print(f"Teacher: {teacher.name}")

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []  # Aggregation: University has a list of departments

    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        for department in self.departments:
            print(f"Department: {department.name}")

# Create teachers
teacher1 = Teacher("Alice")
teacher2 = Teacher("Bob")

# Create department and add teachers
department = Department("Computer Science", [teacher1, teacher2])
teacher3 = Teacher("Tarek")
department.add_teacher(teacher3)

# Create university and add department
university = University("Tech University")
university.add_department(department)

# Display departments in the university
university.show_departments()

# Display teachers in the department
department.show_teachers()