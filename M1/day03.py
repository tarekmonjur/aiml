# -------------- while loop --------------
# while loop -> is used when the number of iterations is not known beforehand.
# while loop -> is condition dependent loop.
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("-"*100)

hello_text = "Hello"
while len(hello_text):
    print(hello_text[0])
    hello_text = hello_text[1:]

print("-"*100)
hello_text = "Hello"
hello_text_count = 0
while hello_text_count < len(hello_text):
    print(hello_text[hello_text_count])
    hello_text_count += 1

print("-"*100)
# -------------- for loop --------------
# for loop -> is used when the number of iterations is known beforehand.
for i in range(5):
    print(i)

print("-"*100)
# for item in container:
#     print(item)

for char in "Hello":
    print(char)

for i in range(5):
    print(i)

print("-"*100)

# -------------- while loop example --------------
guess_number = 7
while True:
    user_input = int(input("Guess the number (between 1 and 10): "))
    if user_input == guess_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Try again!")
