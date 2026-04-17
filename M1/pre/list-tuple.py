
# ---------------- List is mutable ----------------
myList = [1234, 'Muntasir', 'test',  'Muntaha', 4.5]

# list is mutable, we can change the value of an element in the list
myList[2] = 'Ahmed'
print(myList[-1])
print(len(myList))
print(myList)

textList = list("Hello world")
print(textList)
textList.reverse()
print(textList)

# ---------------- Tuple is immutable ----------------
myTuple = (1234, 'Muntasir', 'test',  'Muntaha', 4.5)
print(myTuple)
# myTuple[2] = 'Ahmed' # This will raise an error because tuple is immutable
print(myTuple[1])
print(len(myTuple))
print(tuple(reversed(myTuple)))

