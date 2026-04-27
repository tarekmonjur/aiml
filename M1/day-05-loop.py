# ------- for loop with list -------
my_fruit_list = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in my_fruit_list:
    print(f"list: {fruit}")

print("*"*100)

# ------- for loop with range -------
for i in range(5):
    print(f"i: {i}")

print("*"*100)

# ------- for loop with set -------
my_fruit_set = {"apple", "banana", "cherry", "date", "elderberry"}
for fruit in my_fruit_set:
    print(f"set: {fruit}")

print("*"*100)

# ------- for loop with dictionary -------
my_fruit_dict = {"apple": 6, "banana": 2, "cherry": 3, "date": 4, "elderberry": 5}
for fruit_key in my_fruit_dict:
    print(f"dict1: {fruit_key}, quantity: {my_fruit_dict[fruit_key]}")

print("*"*100)

for fruit_key, fruit_value in my_fruit_dict.items():
    print(f"dict2: {fruit_key}, quantity: {fruit_value}")

print("*"*100)

# ------- for loop with enumerate -------
my_fruit_list = ["apple", "banana", "cherry", "date", "elderberry"]
for index, fruit_value in enumerate(my_fruit_list, start=1):
    print(f"index: {index}, fruit: {fruit_value}")

my_fruit_dict = dict(sorted(my_fruit_dict.items(), key=lambda x: x[1]))
print(f"sorted by quantity: {my_fruit_dict}")

print("*"*100)

# --------- map with for loop ---------
my_price_dict = {"apple": 5.0, "banana": 3.0, "cherry": 20, "date": 40, "elderberry": 6.0}

my_expensive_fruit_dict = {}
for key, value in my_price_dict.items():
    my_expensive_fruit_dict[key] = value*2
print(f"expensive fruits: {my_expensive_fruit_dict}")

print("*"*100)

# --------- map with for loop comprehension ---------
my_expensive_fruit_list = {key: value*2 for key, value in my_price_dict.items()}
print(f"expensive fruits: {my_expensive_fruit_list}")

print("*"*100)

# --------- filter with for loop ---------
my_cheap_fruit_dict = {}
for key, value in my_price_dict.items():
    if value < 10:
        my_cheap_fruit_dict[key] = value
print(f"cheap fruits: {my_cheap_fruit_dict}")

print("*"*100)

# --------- filter with for loop comprehension ---------
my_cheap_fruit_list = {key: value for key, value in my_price_dict.items() if value < 10}
print(f"cheap fruits: {my_cheap_fruit_list}")

print("*"*100)

# --------- list map with for loop -----------
my_expensive_fruit_list = []
for key, value in my_price_dict.items():
    my_expensive_fruit_list.append((key, value*2))
print(f"expensive fruits: {my_expensive_fruit_list}")

print("*"*100)

# ------------ zip with for loop -------------
fruit_names = ["apple", "banana", "cherry", "date", "elderberry"]
fruit_prices = [5.0, 3.0, 20, 40]
# print(zip(fruit_names, fruit_prices))
for name, price in zip(fruit_names, fruit_prices):
    print(f"fruit: {name}, price: {price}")

print("*"*100)

# ------------ nested for loop with dist -------------
my_employee_dict = {
    "Alice": {"age": 30, "department": "HR"},
    "Bob": {"age": 25, "department": "Engineering"},
    "Charlie": {"age": 35, "department": "Marketing"}
}

for employee_name, employee_info in my_employee_dict.items():
    print(f"Employee: {employee_name}")
    for info_key, info_value in employee_info.items():
        print(f"  {info_key}: {info_value}")


print("*"*100)

# ----------- nested for loop with list and dist -------------
my_employee_list = [
    {"name": "Alice", "age": 30, "department": "HR"},
    {"name": "Bob", "age": 25, "department": "Engineering"},
    {"name": "Charlie", "age": 35, "department": "Marketing"}
]

for employee in my_employee_list:
    print(f"Employee: {employee['name']}")
    for key, value in employee.items():
        if key != "name":
            print(f"  {key}: {value}")