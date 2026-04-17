a = [1,2,3,3,4,5,5,6,7,8,8,9,10]
b = set(a)
print(b)

print("-"*100)

x = set("hello")
y = set("world")
print(x.intersection(y))
print(x.union(y))
print(x.difference(y))

print("-"*100)

a = {1,2,3}
b = {2,3,4}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))

print("-"*100)

print(a | a)  # Union
print(a & a)  # Intersection
print(a - a)  # Difference