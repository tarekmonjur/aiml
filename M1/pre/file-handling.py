# ------------------- file reading -------------------
# file = open('./M1/pre/hello.py', 'r')
# content = file.read()
# print(content)
# file.close()

# ------------------- file writing -------------------
with open('./M1/pre/new_file.txt', 'w') as file:
  file.write('Hello, this is a new file.\n')
  file.write('This file is created using Python.\n')

print('-'*100)

# ------------------- file reading with context manager -------------------
with open('./M1/pre/new_file.txt', 'r') as file:
    content = file.read()
    print(content)

print('-'*100)

# ------------------- file appending -------------------
with open('./M1/pre/new_file.txt', 'a') as file:
  file.write('Hello, this is a new file.\n')
  file.write('This file is created using Python.\n')

print('-'*100)

# ------------------- file writing by list -------------------
lines_to_write = ['Hello, this is a new file.\n', 'This file is created using Python.\n']
with open('./M1/pre/new_file.txt', 'w') as file:
  file.writelines(lines_to_write)

print('-'*100)

# ------------------- file reading line by line -------------------
with open('./M1/pre/new_file.txt', 'r') as file:
  for line in file:
    print(line.strip())  # strip() removes the newline character at the end of each line

print('-'*100)

# ------------------- file reading into a list -------------------
with open('./M1/pre/new_file.txt', 'r') as file:
  lines = file.readlines()
  print(lines)

print('-'*100)

import os;
# ------------------- file existence check -------------------
file_path = './M1/pre/new_file.txt'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'new_file.txt')

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

print(os.path.abspath(file_path))  # Get the absolute path of the file
print(os.path.dirname(file_path))   # Get the directory name of the file
print('-'*100)

import pathlib;
# ------------------- file existence check using pathlib -------------------
file_path = pathlib.Path('./M1/pre')
if file_path.exists():
  print(f"The file '{file_path}' exists.")
else:
  print(f"The file '{file_path}' does not exist.")

print('-'*100)

# print([file for file in file_path.glob('*.py')])  # List all Python files in the directory



