# class Employee:
#     def __init__(self, name, salary):
#         self._name = name
#         self.salary = salary

#     @property
#     def name(self):
#         return self._name

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, value):
#         if value <= 0:
#             raise ValueError("Salary cannot be zero or negative")
#         self.__salary = value

# employee = Employee("Alice", 50000)
# print(f"Employee Name: {employee.name}")
# print(f"Employee Salary: {employee.salary}")

# employee.salary = 0
# print(f"Updated Employee Salary: {employee.salary}")


class Employee:
    def __init__(self, salary):
        self.__set_salary(salary)

    def __get_salary(self):
        return self.__salary
    
    def __set_salary(self, value):
        if value <= 0:
            raise ValueError("Salary cannot be zero or negative")
        self.__salary = value
    
    salary = property(__get_salary, __set_salary)

employee = Employee(50000)
print(f"Employee Salary: {employee.salary}")

employee.salary = 0
print(f"Updated Employee Salary: {employee.salary}")