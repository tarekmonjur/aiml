# -------------- String data type -------------
myString = "This is a string"
multiString = """This is a multi-line string. It can span multiple lines."""
print(type(myString))
print(type(multiString))

# -------------- String Indexing ---------------
print(myString[0])
print(myString[5])
print(myString[-1])
print(len(myString))
print(myString[len(myString) - 1])
print(myString[0:4])

# -------------- String Immutability -------------
# myString[1] = 'a'  # This will raise an error because strings are immutable

# -------------- String Methods -------------
myName = "tarek ahammed monjur"
myName = myName.title()
print(myName)
print(myName.upper())
print(myName.lower())
print(myName.split())
print(myName.swapcase())
replaceName = myName.replace("Monjur", "Noor")
print(replaceName)
print(myName)
print(myName.count("n"))

# -------------- String Formatting -------------
nameInput = input("Enter your name: ")
greeting = "Good morning, {}! Welcome to the world of Python.".format(nameInput)
print(greeting)

myAge = 25
myCity = "New York"
greetingText = "My name is {name}. I am {age} years old and I live in {city}.".format(name=nameInput, age=myAge, city=myCity)
print(greetingText)

greetingFText = f"My name is {nameInput}. I am {myAge} years old and I live in {myCity}"
print(greetingFText)


