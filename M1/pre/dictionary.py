person = {"name": "Muntasir", "age": 33, "city": "Feni"}
print(person , type(person))
print('----------------------------------')
print(person.keys(), person.values(), person.items())
print('----------------------------------')
for key in person.keys():
    print(key)
print('----------------------------------')
for value in person.values():
    print(value)
print('----------------------------------')
for key, value in person.items():
    print(key, value)
print('----------------------------------')
a = [1,2,3]
b = ["bangla", "english", "arabic"]
c = dict(zip(a,b))
print(c)