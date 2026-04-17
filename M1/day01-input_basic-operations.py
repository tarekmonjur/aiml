# string concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
print('----------------------------------------')

# string repetition
greeting = "Hello! "
print(greeting * 3)
print('----------------------------------------')

# # Input and type conversion
# first_number = input("Enter first number: ")  # input() returns a string
# second_number = input("Enter second number: ")
# print(type(first_number), type(second_number))  # Both are strings
# print(first_name+first_number)  # Concatenation of string and number (as string)
# # To perform arithmetic operations, we need to convert the input to numbers
# first_number = int(first_number)  # Convert to integer
# second_number = int(second_number)
# print(first_number + second_number)  # Now we can add the numbers

# Advance Printing
name = "Alice"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")  # Using string concatenation
print("My name is {} and I am {} years old.".format(name, age))  # Using str.format() method
print(f"My name is {name} and I am {age} years old.")  # Using f-strings

year = 2024
month = "June"
day = 15
print(day, month, year)  # Default separator is space
print(day, month, year, sep="-")  # Custom separator
print('-'*50)

print("Result")
print("="*50)
a = 10
b = 5
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")
print(f"a/b = {a/b}")
print(eval("a+b"))  # Evaluates the expression as a Python expression
