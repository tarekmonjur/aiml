
# Arbitrary Positional Arguments. Receives any number of positional arguments as a tuple.
def addition(*args):
    return sum(args)

print(addition(1, 2, 3, 4, 5))  # Output: 15


# Arbitrary Keyword Arguments. Receives any number of keyword arguments as a dictionary.
def my_info(first_name, last_name, age):
    print(f"my name is {first_name} {last_name} and I am {age} years old")

my_info(age=33, first_name="Muntasir", last_name="Ahmed")


# Using **kwargs to accept arbitrary keyword arguments. Receives any number of keyword arguments as a dictionary.
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Muntasir", age=33, city="Feni")