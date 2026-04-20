# ----------------- Data Structures in Python-----------------
# ********************************************
# ----------------- 1. Lists -----------------
# *********************************************
# --------- characteristics of lists ---------
# 1. Ordered: Lists maintain the order of elements. When you print a list, the elements will appear in the same order as they were defined.
# 2. Mutable: Lists can be modified after they are created. You can add, remove, or change elements in a list.
# 3. Allow duplicates: Lists can contain duplicate elements. You can have multiple occurrences of the same value in a list.
# 4. Indexing and slicing: Lists support indexing and slicing, which allows you to access specific elements or a range of elements in the list.
# ********************************************
# list[start:stop:step] -> slicing a list
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(fruits[1])  # Output: banana
print(fruits[-1])  # Output: grape
print(fruits[2:4])  # Output: ['cherry', 'mango']
print(fruits[:3])  # Output: ['apple', 'banana', 'cherry']

print("-" * 100)

myList = [1, "hello", 3.14, [1, 2, 3], {"key": "value"}, True, {1, 3, 4, 5, 2, 3, 1}]
print(myList)  # Output: 2

print("-" * 100)

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"],
    "address": {"street": "123 Main St", "zip": "10001"},
}

print(person["hobbies"][0])  # Output: reading

print("-" * 100)

# ----------------- list method -----------------
fruits.append("orange")  # adds an item to the end of the list
print("append = ", fruits)  # Output: ['apple', 'banana', 'cherry', 'mango', 'grape', 'orange']
fruits.insert(1, "blueberry")  # inserts an item at a specified index
print("insert = ", fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'mango', 'grape', 'orange']

# print(fruits[1:-3])  # Output: ['blueberry', 'banana', 'cherry']
# print(fruits[1:4:-1])  # Output: []
print(fruits[3:0:-1])  # Output: ['cherry', 'banana', 'blueberry']
print(fruits[-4:0:-1])  # Output: ['cherry', 'banana', 'blueberry']
print(fruits[-4:-7:-2])  # Output: ['cherry', 'blueberry']
print(fruits[::-1])

fruits.remove("banana")  # removes the first occurrence of an item from the list
print("remove = ", fruits)  # Output: ['apple', 'blueberry', 'cherry', 'mango', 'grape', 'orange']
fruits.pop()  # removes and returns the last item from the list
print("pop = ", fruits)  # Output: ['apple', 'blueberry', 'cherry', 'mango', 'grape']
fruits.sort()  # sorts the items of the list in ascending order
print("sort = ", fruits)  # Output: ['apple', 'blueberry', 'cherry', 'grape', 'mango']
fruits.reverse()  # reverses the order of the items in the list
print("reverse = ", fruits)  # Output: ['mango', 'grape', 'cherry', 'blueberry', 'apple']

print("-" * 100)

# -------------- list concatenation --------------
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# combined_list = list1 + list2
# print("concatenation = ", combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# list1.extend(list2)  # Extend the copy with list2
# print("extend = ", list1)  # Output: [1, 2, 3, 4, 5, 6]

combined_list = list1.copy()  # Create a copy of list1
combined_list.extend(list2)  # Extend the copy with list2
print("extend = ", combined_list, list1, list2)  # Output: [1, 2, 3, 4, 5, 6] [1, 2, 3] [4, 5, 6]
list1.append(7)  # Append 7 to list1
print("append = ", list1, combined_list)  # Output: [1, 2, 3, 7] [1, 2, 3, 4, 5, 6]

print("-" * 100)

# -------------- list comprehension --------------
numbers = range(10)
squares = [num**2 for num in numbers]
print("squares = ", squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("-" * 100)

# ********************************************
# -------------------- tuples ----------------
# ********************************************
# --------- characteristics of tuples ---------
# 1. Ordered: Tuples maintain the order of elements. When you print a tuple, the elements will appear in the same order as they were defined.
# 2. Immutable: Tuples cannot be modified after they are created. You cannot add, remove, or change elements in a tuple. However, if a tuple contains mutable objects (like lists), those objects can be modified.
# 3. Allow duplicates: Tuples can contain duplicate elements. You can have multiple occurrences of the same value in a tuple.
# 4. Indexing and slicing: Tuples support indexing and slicing, which allows you to access specific elements or a range of elements in the tuple, just like lists.
# ********************************************
my_tuple = (1, "hello", 3.14, [1, 2, 3], {"key": "value"}, True, {1, 3, 4, 5, 2, 3, 1})
print(my_tuple)  # Output: (1, 'hello', 3.14, [1, 2, 3], {'key': 'value'}, True, {1, 2, 3, 4, 5})

# ------------------ tuple unpacking -----------------
a, b, c, d, e, f, g = my_tuple
print(a)  # Output: 1
*a, b, c = my_tuple
print(a)
a, b, *c = my_tuple
print(c)
print(my_tuple.count(1))  # Output: 1
print(my_tuple.index("hello"))  # Output: 1

print("-" * 100)

# ********************************************
# -------------------- sets ----------------
# ********************************************
# --------- characteristics of sets ---------
# 1. Unordered: Sets do not maintain any order of elements. When you print a set, the elements may appear in a different order than they were added.
# 2. Unique: Sets do not allow duplicate elements. If you try to add a duplicate element to a set, it will be ignored.
# 3. Mutable: Sets are mutable, which means you can add or remove elements from a set after it has been created. However, the elements themselves must be immutable (e.g., numbers, strings, tuples).
# 4. Indexing and slicing: Sets do not support indexing or slicing because they are unordered collections. You cannot access elements in a set by their position.
my_set = {1, "hello", "hey", 1, "hey", 2, "hello", 3}
print(my_set)  # Output: {1, 2, 3, 'hello', 'hey'}

# ---------- set methods ----------
my_set.add("world")  # adds an item to the set
print("add = ", my_set)  # Output: {1, 2, 3, 'hello', 'hey', 'world'}
my_set.remove("hello")  # removes an item from the set; raises KeyError if the item is not found
print("remove = ", my_set)  # Output: {1, 2, 3, 'hey', 'world'}
my_set.discard("hey")  # removes an item from the set if it is present; does nothing if the item is not found
print("discard = ", my_set)  # Output: {1, 2, 3, 'world'}
my_set.pop()  # removes and returns an arbitrary item from the set; raises KeyError if the set is empty
print("pop = ", my_set)  # Output: {2, 3, 'world'}
my_set.clear()  # removes all items from the set
print("clear = ", my_set)  # Output: set()

print("-" * 100)

# -------------- set operations --------------
# Union: all elements that are in either set1 or set2 (or both)
# Intersection: all elements that are in both set1 and set2
# Difference: all elements that are in set1 but not in set2
# Symmetric Difference: all elements that are in either set1 or set2 but not in both

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)  # returns a new set that is the union of set1 and set2
print("union = ", union_set)  # Output: {1, 2, 3, 4, 5, 6}
intersection_set = set1.intersection(set2)  # returns a new set that is the intersection of set1 and set2
print("intersection = ", intersection_set)  # Output: {3, 4}
difference_set = set1.difference(set2)  # returns a new set that is the difference of set1 and set2
print("difference = ", difference_set)  # Output: {1, 2}
symmetric_difference_set = set1.symmetric_difference(set2)  # returns a new set that is the symmetric difference of set1 and set2
print("symmetric_difference = ", symmetric_difference_set)  # Output: {1, 2, 5, 6}

old_subscribers = {"tarek@gmail.com", "monjur@gmail.com", "muntasir@gmail.com", "muntah@gmail.com"}
new_subscribers = {"nipu@gmail.com", "monjur@gmail.com", "masuda@gmail.com", "muntah@gmail.com"}

# Find new subscribers who are not in the old subscribers list
new_only_subscribers = new_subscribers.difference(old_subscribers)
print("New subscribers who are not in the old subscribers list:", new_only_subscribers)

# Find old subscribers who are not in the new subscribers list
old_only_subscribers = old_subscribers.difference(new_subscribers)
print("Old subscribers who are not in the new subscribers list:", old_only_subscribers)

# Find subscribers who are in both lists
common_subscribers = old_subscribers.intersection(new_subscribers)
print("Subscribers who are in both lists:", common_subscribers)

# Find all unique subscribers from both lists
all_unique_subscribers = old_subscribers.union(new_subscribers)
print("All unique subscribers from both lists:", all_unique_subscribers)

print("-" * 100)


# ************************************************************
# -------------------- dictionaries ----------------
# ************************************************************
# --------- characteristics of dictionaries ---------
# 1. Unordered: Dictionaries do not maintain any order of key-value pairs. When you print a dictionary, the key-value pairs may appear in a different order than they were added.
# 2. Mutable: Dictionaries are mutable, which means you can add, remove, or change key-value pairs in a dictionary after it has been created. However, the keys themselves must be immutable (e.g., numbers, strings, tuples).
# 3. Unique keys: Dictionary keys must be unique. If you try to add a key that already exists in the dictionary, the new value will overwrite the existing value for that key.
# 4. Key-value pairs: Dictionaries store data in key-value pairs. Each key is associated with a value, and you can access the value by using its corresponding key.
# 5. Indexing and slicing: Dictionaries do not support indexing or slicing because they are unordered collections. You cannot access key-value pairs in a dictionary by their position. Instead, you access values using their corresponding keys.
my_dict = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "traveling", "cooking"],
    "address": {"city": "New York", "street": "123 Main St", "zip": "10001"},
    "verified": True,
    3.14: "pi",
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'traveling', 'cooking'], 'address': {'city': 'New York', 'street': '123 Main St', 'zip': '10001'}, 'verified': True}
print(my_dict["name"])  # Output: Alice
print(my_dict["hobbies"][1])  # Output: traveling
print(my_dict["address"]["city"])  # Output: New York
print(my_dict[3.14])  # Output: pi

print("-" * 100)

# ------------------ dictionary methods -----------------
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'hobbies', 'address', 'verified', 3.14])
print(my_dict.values())  # Output: dict_values(['Alice', 30, ['reading, 'traveling', 'cooking'], {'city': 'New York', 'street': '123 Main St', 'zip': '10001'}, True, 'pi'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('hobbies', ['reading', 'traveling', 'cooking']), ('address', {'city': 'New York', 'street': '123 Main St', 'zip': '10001'}), ('verified', True), (3.14, 'pi')])

print("-" * 100)

print(my_dict.get("country"))  # Output: None
print(my_dict.get("country", "BD"))  # Output: BD

my_dict["email"] = "tarek@gmail.com"  # adds a new key-value pair to the dictionary
my_dict.update({"age": 31, "verified": False})  # updates the value of existing keys in the dictionary
print(my_dict)

print("-" * 100)

my_dict.pop("hobbies")  # removes the key-value pair with the specified key from the dictionary and returns the value; raises KeyError if the key is not found
print(my_dict)

my_dict.popitem()  # removes and returns an arbitrary key-value pair from the dictionary; raises KeyError if the dictionary is empty
print(my_dict)

my_dict.clear()  # removes all key-value pairs from the dictionary
print(my_dict)  # Output: {}

print("-" * 100)

fruits_dist = {"apple": 10, "banana": 20, "cherry": 15}
label_to_key = {label: key for key, label in fruits_dist.items()}  # creates a new dictionary where the keys are the labels from fruits_dist and the values are their corresponding indices
print(label_to_key)  # Output: {'apple': 0, 'banana': 1, 'cherry': 2}


# ------------------ Data Structure Summary Table -----------------
# | Data Structure | Ordered | Mutable | Allow Duplicates | Indexing/Slicing | Syntax Example |
# |----------------|---------|---------|------------------|------------------| ---------------|
# | List           | Yes     | Yes     | Yes              | Yes              | [1, 2, 3] |
# | Tuple          | Yes     | No      | Yes              | Yes              | (1, 2, 3) |
# | Set            | No      | Yes     | No               | No               | {1, 2, 3} |
# | Dictionary     | No      | Yes     | No               | No               | {"key": "value"} |