x = {1: "one", 2: "two", 3: "three"}
print(type(x))
result = {i: "even" if i % 2 == 0 else "odd" for i in range(1, 11)}
print(result)