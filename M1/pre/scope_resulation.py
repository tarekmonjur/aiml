my_value1 = 10 # Global variable

def my_function():
    my_value1 = 20 # Local variable
    print("Inside the function:", my_value1)

my_function()  # Output: Inside the function: 20
print("Outside the function:", my_value1)  # Output: Outside the function: 10

print('*' * 100)

# LEGB Rule:
# L -> Local,
# E -> Enclosing,
# G -> Global,
# B -> Built-in Scope

my_number = 5 # Global variable

def outer_function():
    my_number = 10 # Enclosing variable

    def inner_function():
        my_number = 15 # Local variable
        print("Inside inner function:", my_number)

    inner_function()  # Output: Inside inner function: 15
    print("Inside outer function:", my_number)  # Output: Inside outer function: 10

outer_function()  # Output: Inside outer function: 10
print("Outside all functions:", my_number)  # Output: Outside all functions: 5

print('*' * 100)

# -------- global keyword --------

my_number = 5 # Global variable
def modify_global():
    my_number = 10 # Enclosing variable
    def inner_function():
        global my_number
        my_number = 20 # Modifying the global variable
        print("Global: Inside inner function:", my_number)  # Output: Inside inner function: 20

    inner_function()  # Output: Inside inner function: 20
    print("Global: Inside outer function:", my_number)  # Output: Inside outer function: 10

modify_global()
print("Global: After modifying global variable:", my_number)  # Output: After modifying global variable: 20

print('*' * 100)

# -------- nonlocal keyword --------
my_number = 5 # Global variable
def modify_local():
    my_number = 10 # Enclosing variable
    def inner_function():
        nonlocal my_number
        my_number = 20 # Modifying the enclosing variable
        print("Nonlocal: Inside inner function:", my_number)  # Output: Inside inner function: 20

    inner_function()  # Output: Inside inner function: 20
    print("Nonlocal: Inside outer function:", my_number)  # Output: Inside outer function: 20

modify_local()
print("Nonlocal: After modifying local variable:", my_number)  # Output: After modifying local variable: 5