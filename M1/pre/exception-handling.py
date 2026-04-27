# Error vs Exception
#
# Error: An error is a problem in the program that cannot be handled by the program itself.
# It is usually caused by a bug in the code or a problem with the environment.
# For example, compile time error, syntax errors, indentation errors.
#
# Exception: An exception, on the other hand, is a problem that can be handled by the program.
# It is usually caused by user input or a problem with the data.
# For example, run time error, division by zero, file not found, index out of range, etc.

# Compile Time Errors vs Run Time Errors
#
# Compile Time Errors: Compile time errors are errors that occur during the compilation of the program.
#
# Run Time Errors: Run time errors are errors that occur during the execution of the program.


# This will raise a ZeroDivisionError
import os


try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# This will raise a FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

# try:
#     number = int(input("Enter a number: "))
#     print(f"You entered: {number}")
# except ValueError as e:
#     print(f"Error: {e}")

print("-" * 100)

import os

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "new_file.txt")
    with open(file_path, "r") as file:
        content = file.read()
    result = 10 / 10
    # data = result['foo']
    # data = int("abc")
    data = [1,2,4]
    # print(data[5])
    data = results

except FileNotFoundError as e:
    print(f"File Not Found: {e}")
except ZeroDivisionError as e:
    print(f"Division by Zero: {e}")
except TypeError as e:
    print(f"Type Error: {e}")
except ValueError as e:
	print(f"Value Error: {e}")    
except IndexError as e:
    print(f"Index Error: {e}")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
else:
	print("this part code successfully executed.")
finally:
	print("This part of the code will always execute, regardless of whether an exception occurred or not.")          

print("-" * 100)

def check_extension(filename):
	if not filename.endswith('.txt'):
		raise ValueError("Invalid file extension. Only .txt files are allowed.")
	return True

try:
	check_extension('example.py')
except Exception as e:
      	print(f"Error: {e}")     