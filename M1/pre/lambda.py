square = lambda x: x * x
print(square(5))  # Output: 25

add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

my_list = [('apple', 2), ('banana', 1), ('cherry', 3)]
my_list = sorted(my_list, key=lambda x: x[1])  # Sort by the second element of the tuple
print(my_list)  # Output: [('banana', 1), ('apple', 2), ('cherry', 3)]


my_numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, my_numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, my_numbers))
print(even_numbers)  # Output: [2, 4]

from functools import reduce
product = reduce(lambda x, y: x + y, my_numbers)
print(product)  # Output: 15