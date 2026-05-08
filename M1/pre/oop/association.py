# Association
# Association is a relationship that two object related with each other but they can exist independently.
# 
# Concept:
# - Independent lifecycle: Both classes can exist independently of each other.
# - Uses-a Relationship: One class uses the functionality of another class without owning it.
# - Weak Coupling: It is a weak relationship between two classes.

class Student:
    def __init__(self, name):
        self.name = name

    def learn(self, teacher):
        print(f"{self.name} is learning from {teacher.name}")    

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} is teaching {student.name}")

    def learn(self):
        print(f"{self.name} is learning new teaching methods")


# Independent creation
student = Student("Alice")
teacher = Teacher("Bob")

# Temporary interaction (Association)
student.learn(teacher)
teacher.teach(student)