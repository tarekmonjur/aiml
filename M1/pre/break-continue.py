myList = [1, 2, 3, 4, 5, 'a', 6, 7, 8.1, 9, 10, 'b'];

for i in myList:
    if type(i) == str:
        continue
    else:
        print(i)

print('------------------')

for i in myList:
    if type(i) == str:
        continue;

    if type(i) == float:
        print('Not an integer')
        break
    else:
        print(i)