# Builder Pattern
# The builder pattern is a design pattern that allows for the step-by-step construction of complex objects.
# It separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

class CarBuilder:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None
        
    def set_make(self, make):
        self.make = make
        return self

    def set_model(self, model):
        self.model = model
        return self

    def set_year(self, year):
        self.year = year
        return self

    def set_color(self, color):
        self.color = color
        return self

    def build(self):
       return Car(self.make, self.model, self.year, self.color)

car = CarBuilder().set_make("Toyota").set_model("Camry").set_year(2020).set_color("Red").build()
print(car)


class SQLQuery:
    "Project class for building SQL queries using the Builder pattern"
    def __init__(self, select, from_table, where=None, order_by=None):
        self.select = select
        self.from_table = from_table
        self.where = where
        self.order_by = order_by

    def __str__(self):
        query = f"SELECT {self.select} FROM {self.from_table}"
        if self.where:
            query += f" WHERE {self.where}"
        if self.order_by:
            query += f" ORDER BY {self.order_by}"
        return query

class SQLQueryBuilder:
    def __init__(self):
        self.select = "*"
        self.from_table = None
        self.where = None
        self.order_by = None

    def set_select(self, select):
        self.select = select
        return self

    def set_from_table(self, from_table):
        self.from_table = from_table
        return self

    def set_where(self, where):
        self.where = where
        return self

    def set_order_by(self, order_by):
        self.order_by = order_by
        return self

    def build(self):
        if not self.from_table:
            raise ValueError("FROM table is required")
        return SQLQuery(self.select, self.from_table, self.where, self.order_by)

query = SQLQueryBuilder().set_select("name, age").set_from_table("users").set_where("age > 18").set_order_by("name").build()
print(query)    