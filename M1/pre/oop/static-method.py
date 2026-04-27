# ----------- class static method -----------
class Student:
    school = 'ABC School'

    @staticmethod
    def get_school():
        return Student.school

print(Student.get_school())

# ----------- class method vs static method -----------
class Employee:
    company = 'XYZ Corporation'

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def get_company():
        return Employee.company
    
print(Employee.get_company())  # Using class method
print(Employee.get_company())  # Using static method

# Use case of static method and class method
# Static method is used when we want to perform a function that is related to the class but does not need access to class or instance variables.
# Class method is used when we want to access or modify class variables.
