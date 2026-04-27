# Method parameter and argument
# Parameter: A variable in the declaration of function.
# Argument: The actual value of the parameter that gets passed to the function.

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

print("*"*100)

# Method with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()

print("*"*100)

# normalize value between 0 and 1
def normalize(value, min_value, max_value):
    if max_value - min_value == 0:
        return 0
    
    result = (value - min_value) / (max_value - min_value)
    print(f"original value: {value} normalized value: {result}")
    return result

normalize(5, 0, 10)
normalize(15, 10, 20)
normalize(10, 10, 10)

print("*"*100)

# Normalize value between 0 and 1 with default parameter
def normalize(value, max_value=1):
    if max_value == 0:
        return 0
    
    result = value / max_value
    print(f"original value: {value} normalized value: {result}")
    return result

normalize(5, 10)
normalize(15, 20)
normalize(10, 10)

print("*"*100)

# Method with multiple parameters and default parameter
def calculate_price(quantity, price_per_unit, tax_rate=1):
    total_price = quantity * price_per_unit
    tax_amount = total_price * (tax_rate / 100)
    final_price = total_price + tax_amount
    print(f"quantity: {quantity}, price per unit: {price_per_unit}, tax rate: {tax_rate}")
    print(f"total price: {total_price}, tax amount: {tax_amount}, final price: {final_price}")
    return final_price

# positional arguments
calculate_price(1, 10, 1)

# keyword arguments
calculate_price(quantity=1, price_per_unit=10, tax_rate=1)
calculate_price(price_per_unit=10, quantity=1, tax_rate=1)

print("*"*100)

# variable scope, local vs global scope
# local scope: variables defined inside a function
# global scope: variables defined outside a function
global_variable = "I am global"

def my_function():
    local_variable = "I am local"
    print(local_variable, global_variable)

my_function()
print(global_variable)

print("*"*100)

# function return multiple values
def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter # return multiple values as a tuple

# tuple unpacking
area, perimeter = calculate_area_and_perimeter(5, 10)
print(f"Area: {area}, Perimeter: {perimeter}")

print("*"*100)

# function error handling with try-except
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result of {a} divided by {b} is: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "a")

print("*"*100)

# module import and usage
import random

card = ["spades", "hearts", "diamonds", "clubs"]
random_card = random.choice(card)
print(f"Randomly selected card: {random_card}")

print("*"*100)

random_number = random.randint(1, 100)
print(f"Randomly selected number: {random_number}")

